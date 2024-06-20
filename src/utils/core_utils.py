
#for URLs, Parsing methods and other constants
import utils.SITE as SITE
import utils.site_parsing as PARSE

#for making the actual requests
import requests



def attempt_login(username:str, password:str, session = None):
    """
        Creates a requests.session, makes a POST request to the LMS site, upon success, it writes
        the session cookies to the flask session object, to be used for future requests
        
            Parameters:
                username (str): A string of the student's official username
                password (str): A string of the student's password
                
            Returns:
                cookie_dict (dict): A dictionary containing the session cookies, as obtained by the Official site
    """
    with requests.session() as session:

        USER_DATA = {
            'username':username,
            'password':password
        }
        response = session.post(
            url=SITE.AUTH_URL,
            data=USER_DATA,
            #stream=True  #set it to stream || to test ; non stream version seems to respond faster, need to investigate
        )
        
        #response.close() #instantly close the response, as we dont need the 80,000+ character response that contains irrelevant data (html, inline css, and javascript)
        # print("NEG!!!====",response.content)
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
        Creates a session object, attaches the login cookies to this instance, and makes the fetch request for the subjects
            
        Parameters:
            cookies (dict): Cookies generated upon login action done on the official site
            
        Returns:
            subjects (list[dict]): Array of JSON Object/Python Dictionary containing subject details for logged in user:\n
                \t- Name
                \t- Instructor
                \t- Attendance
                \t- Link
                \t- Course ID
    """
    
    with requests.session() as session:

        #Insert the session cookies
        session.cookies = requests.utils.cookiejar_from_dict(cookie_dict=cookies)
        response = session.get(SITE.SUBJECTS_URL)

        html_content = response.content
        #pass the html_content to a custom parsing block, that converts it into a neat json object 
        subjects = PARSE.parse_subjects(html=html_content)
        print(subjects)

        return subjects


def get_subject_materials(link : str , cookies) -> list[dict]:
    """
        Fetches the given link, and returns a JSON containing links to the resource and titles
        
        
        Parameters:
            link (str): The subject link to be fetched and processed
            cookies (dict): Cookies generated upon login action done on the official site
            
        Returns:
            materials_json (list[dict]): List of course materials for a particular subject
    """
    
    with requests.session() as session:
        session.cookies = requests.utils.cookiejar_from_dict(cookie_dict=cookies)
        
        response = session.get(link)
        #get the string version of the response to pass to the parser
        response = response.content
        
        materials_json = PARSE.parse_materials(response)
        
        
        return materials_json


def get_download_link(link : str, link_type, cookies):
    """
        Finds and returns a link to the .pdf, .pptx, or .docx resource for easy downloading.
        
        Parameters:
            link (str): The subject link to be fetched and processed
            cookies (dict): Cookies generated upon login action done on the official site
        
        Returns:
            An Object containing the following
            name: name of the file 
            link: link to the file requested
    """
    
    # TODO: Implement a check to determine the kind of link (3-4 types exist I believe)
    with requests.session() as session:
            
        session.cookies = requests.utils.cookiejar_from_dict(cookie_dict=cookies)

        response = session.get(link)
        
        #parsing the response to extract the link
        extracted_link = PARSE.parse_resource_link(response.content, link_type)
        
        content = None
        #Return object
        if (extracted_link != None):
            
            start = extracted_link.rfind('/') + 1 #get the last "/" and ahead of it, is the file name
            name = extracted_link[start:]
            content = {
                'name': name,
                'link': extracted_link
            }
            
        
        
        return content
        
        
    
    