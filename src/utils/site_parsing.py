from bs4 import BeautifulSoup
import re

def parse_subjects(html: str) -> list[dict]:
    """
        Creates a BeautifulSoup object that finds each subject block,
        returns an array of JSON Objects containing Name, Instructor, Attendance & Link
        to that particular subject
        
        Parameters:
            html (str): string object containing the response content (html, inline-css & inline-js code)
            
        Returns:
            subjects (list[dict]): List of dictionary object containing the subject details:\n
                \t- Name
                \t- Instructor
                \t- Attendance
                \t- Link
                \t- Course ID
    """
    
    soup = BeautifulSoup(html, 'lxml')
    subjects = []
    subject_containers = soup.find_all(class_="subcontent-container")

    for subject in subject_containers:
        #convert to raw string, so it can be parsed after being converted to BS4
        subject = str(subject)
        soup = BeautifulSoup(subject, 'lxml')

        #Name
        subject_name = soup.find('h4')
        subject_name = subject_name.contents[0] # getting the data within the actual tag that stored the name

        #Instructor
        subject_instructor = soup.select_one('.istruinfocontainer > div') # probably meant to write "instructor-info-container" but you never know 💀
        subject_instructor = subject_instructor.contents[0]

        #Subject Attendance
        subject_attendance = soup.select_one('.prg-container > span') #progress container is the weird horizontal graph thingy
        subject_attendance = subject_attendance.contents[0]
        
        #Subject links
        subject_link = soup.find('a')
        subject_link = subject_link['href']
        
        #Course id
        course_id = subject_link[-4:]

        subject_dict = {
            'name':subject_name,
            'instructor':subject_instructor,
            'attendance':subject_attendance,
            'link':subject_link,
            'course_id':course_id
        }
        
        subjects.append(subject_dict)
        
    return subjects
    

def parse_materials(html : str) -> list[dict]:
    """
        Similar to parse_subjects, it gets all the "activity" within a subjects, extracts a name and link to that subject, and
        return an array of JSON Objects containing these properties.
        
        Parameters:
            html (str): string object containing the response content (html, inline-css & inline-js code)

        Returns:
            course_materials (list[dict]): List of dict objects containing name and link to each course material available for given subject 
    """
    
    
    soup = BeautifulSoup(html, 'lxml')
    
    activities = soup.select(".activityinstance")

    # SELECTING all anchor tags, seems to give me access to past semester and all their contents, might be useful
    # Something to look into for the future.
    
    course_materials = []
    for activity in activities:
        soup = BeautifulSoup(str(activity), 'lxml')
        link = soup.select_one("a")
        link = link['href']
        print(link)
        
        name = soup.find("span")
        name = name.contents[0]
        link_type = link[34:-19] # 34 and -19 are just constants to remove the unecessary part of the link
        
        #The handling for the different potential scenarios regarding the way the download links have to be made available is 
        # to be seperated from this request.
        activity_object = {
            'name':name,
            'link':link,
            'type':link_type
        }
        
        course_materials.append(activity_object)
        

    return course_materials


def parse_resource_link(html: str, link_type: str) -> str:
    """
        Given a link to a resource, dyquestion, presentation etc, returns a downloadable link to the content
        
        Parameters:
            html (str) : raw response data that is to be processes
            link_type (str) : type of the resource [dyquestion, presentation, page, etc]
    """
    
    
    # Currently only supporting a subset of all types, but the most frequently used.
    # It's not known whether there can be multiple links uploaded within an activity instance in the official site.
    
    # extract the type of link (dyquestion, forum, flexpaper, etc etc)
    
    soup = BeautifulSoup(html, 'lxml')
    
    

    # This method extracts the link from the javascript code that loads the actual document
    def flexpaper_parse(soup):
        #find the script that handles "displaying the pdf file within the custom (flexpaper) pdf viewer"
        script_tag = soup.find('script', string=re.compile(r"\$\(.*?\).FlexPaperViewer"))
        if script_tag != None:
            #Extract the PDFFILE link from within its config by means of regex
            pdf_url_pattern = re.compile(r"PDFFile\s*:\s*'([^']+)'")
            pdf_url_match = pdf_url_pattern.search(script_tag.string)

            if(pdf_url_match):
                #successfully found the PDFFILE url
                pdf_url = pdf_url_match.group(1)
                print("PDF file URL:", pdf_url)
                return pdf_url
                # print(pdf_url_match)
                
            else:
                print("Did not find the link within flexpaper config")
                return None
    
    #This method is slightly slower as it extracts after loading a new page.
    def default_parse(soup):
        presentation_content = soup.find('div', attrs={'role':'main'})

        soup = BeautifulSoup(str(presentation_content), 'lxml')
        link_to_content = soup.find("a")
        link_to_content = link_to_content['href']
        
        print("FIRST: ",link_to_content) 
        return link_to_content
    
    
    match link_type:
        
        case "flexpaper":
            return flexpaper_parse(soup)
        
        case "resource":
            return default_parse(soup)
        
        case "presentation":
            return default_parse(soup)
        
        case "dyquestion":
            return default_parse(soup)

        case "forum":
            # Currently I have no plans on supporting a forum via this API
            return None
        
        case "quiz":
            #  quizzes are also not being supported by this API
            return None
        
        case _:
            return None

    
    
    
    
    
    
    
    
    
