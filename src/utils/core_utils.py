
#for URLs and other constants
import utils.SITE as SITE
import utils.site_parsing as PARSE
#for making the actual requests
import requests



def attempt_login(username:str, password:str, session = None):
    """
        Creates a requests.session, makes a POST request to the LMS site, upon success, it writes
        the session cookies to the flask session object, to be used for future requests
    """
    session = requests.session()

    USER_DATA = {
        'username':username,
        'password':password
    }
    response = session.post(
        url=SITE.AUTH_URL,
        data=USER_DATA,
        stream=True  #set it to stream || to test ; non stream version seems to respond faster, need to investigate
    )
    
    response.close() #instantly close the response, as we dont need the 80,000+ character response that contains irrelevant data (html, inline css, and javascript)

    print(session.cookies)
    #Successful login
    if response.status_code == 200:
        #convert to a dictionary
        cookie_dict = requests.utils.dict_from_cookiejar(session.cookies)
        
        # return session.cookies, on a successful login
        return cookie_dict
    
    #if login fails, return the response code
    return response.status_code


def get_subjects(cookies) -> list[dict]:
    """
        Creates a session objects, attaches the login cookies to this instance, and makes the fetch request for the subjects
        Returns a JSON Object containing subject details:
            - Name
            - Instructor
            - Attendance
            - Link
            - Course ID
    """
    
    session = requests.session()

    #Insert the session cookies
    session.cookies = requests.utils.cookiejar_from_dict(cookie_dict=cookies)
    response = session.get(SITE.SUBJECTS_URL)

    html_content = response.content
    #pass the html_content to a custom parsing block, that converts it into a neat json object 
    
    subjects = PARSE.parse_subjects(html=html_content)
    

    return subjects


def get_subject_materials(link, cookies):
    """
        Fetches the given link, and returns a JSON containing links to the resource and titles
        TODO: Need to implement some sort of "downlaoder than can handle different "hidden" links to get the pdf/docx/pptx downloaded.
        
    """
    
    session = requests.session()
    session.cookies = requests.utils.cookiejar_from_dict(cookie_dict=cookies)
    
    response = session.get(link)
    #get the string version of the response to pass to the parser
    response = response.content
    
    material_json = PARSE.parse_materials(response)
    
    
    return material_json

    