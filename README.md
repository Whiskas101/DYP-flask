# DYP-flask

A `Flask` API that filters through the bloat to deliver the relevant student information in a JSON format, ready to be used by any application.

[Here is the official site for reference.](https://mydy.dypatil.edu/rait/)

## Setup Instructions

The following command will install every dependency needed for the API to run. 
Naturally, since it abstracts over the old but official website, you must have valid student credentials to actually use this API. 
<sub>I will create a dummy account accessible by anyone eventually, for demonstration purposes.</sub>

On Linux
> `python3 -m pip install -r requirements.txt`

On Windows
> `python -m pip install -r requirements.txt`

The API was built using python3.10 on Windows Subsystem for Linux.


## How it works

### Overview
The Official site is often slow to load, has session cookies that expire quickly, and redirects the user a bit too much. It also prevents downloading of study materials, which combined with its unreliable speed, and a hard-to-use PDF viewer.

These, and some other issues are addressed. The DYP-Flask API only fetches the data that is relevant and most commonly fetched. That being the Student Attendance Stat & Subject specific .ppt/.pdf/.docx files. This is achieved by manually isolating the requests that contain this information, and only loading that specific part of the page. Since the website uses server side rendering, the returned content has to be parsed and packaged into JSON objects. The application can then implement caching to prevent unnecessary login requests, for merely seeing the data stored.

The DYP-flask also aims to provide downloadable links to the study materials for each subject, preventing the need to make unnecessary subsequent requests for previously seen content, while giving the end user the choice to use their own viewer. yet again, something lacking in the official site.

## Stuff Used
The following were used while working on this project:
 - Flask
 - Python's built-in requests (`sessions` mainly)
 - Postman 
 - mitmproxy (for finding endpoints)
 - BeautifulSoup with lxml (for extracting data from SSR HTML code, into a `JSON` Object)

### To Do
 - Complete this readme.md file
 - Handle different types of links: flexpaper, presentation, docx, redirected page with downloadable links
 - Rate Limiting, to prevent abuse
 - Student Data Analysis

