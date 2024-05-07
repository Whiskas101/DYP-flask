
from bs4 import BeautifulSoup


def parse_subjects(html) -> list[dict]:
    """
        Creates a BeautifulSoup object that finds each subject block,
        returns an array of JSON Objects containing Name, Instructor, Attendance & Link
        to that particular subject
    """
    
    soup = BeautifulSoup(html, 'lxml')
    result = []
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

        subject_dict = {
            'name':subject_name,
            'instructor':subject_instructor,
            'attendance':subject_attendance,
            'link':subject_link
        }
        
        result.append(subject_dict)
        
    return result
    
