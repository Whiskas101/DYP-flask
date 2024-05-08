from bs4 import BeautifulSoup


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
        
        #The handling for the different potential scenarios regarding the way the download links have to be made available is 
        # to be seperated from this request.
        activity_object = {
            'name':name,
            'link':link
        }
        
        course_materials.append(activity_object)
        

    return course_materials


def parse_resource_link(html: str) -> str:
    # ideally there should be only one link, and I will proceed accordingly
    # It's not known whether there can be multiple links uploaded within an activity instance in the official site.
    
    
    