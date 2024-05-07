
#for URLs and other constants
import utils.SITE as SITE
import utils.site_parsing as PARSE
#for making the actual requests
import requests



def attempt_login(username:str, password:str, session = None):

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

    session = requests.session()

    #Insert the session cookies
    session.cookies = requests.utils.cookiejar_from_dict(cookie_dict=cookies)
    response = session.get(SITE.SUBJECTS_URL)

    html_content = response.content
    #pass the html_content to a custom parsing block, that converts it into a neat json object 
    
    subjects = PARSE.parse_subjects(html=html_content)
    

    return subjects
    