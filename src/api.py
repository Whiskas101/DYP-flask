#for logging
import logging


# main entry point for the app
from flask import Flask, request, session, Response

# For rate limiting the API
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Core functionality of the app, authentication and fetching commonly used data
# exists within this module
from utils import core_utils

app = Flask(__name__)
app.secret_key = 'this_college_fucking_sucks'

limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="memory://" # I know that using default in memory storage is bad practice, but its acceptable for the small scale API that this is
)                           # This is going on be an a 1gb RAM machine anyway

limiter.init_app(app)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

@app.route('/')
@limiter.limit("100 per minute")
def hello_warudo():
    return f'''
        向かって来るのか？\n
        ザワールドー
    '''

@app.route('/login', methods=['POST'])
@limiter.limit("6 per minute")
def login():
    if request.method == 'POST':
        # data from the end user
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Send login request to the dypatil site
        response = core_utils.attempt_login(username=username, password=password)
        # print(response)
        #set the session cookie obtained previously
        if response != None:
            session['session_cookie'] = response
            return response


        #return the cookies of the session object, or the status code if it fails to login
        return Response(status=401)

@app.route('/subjects', methods=['GET'])
@limiter.limit("3 per minute")
def subjects():

    cookies = session['session_cookie']
    logging.debug(f"{cookies} obtained")

    response = core_utils.get_subjects(cookies=cookies)

    return response

@app.route('/materials', methods=['POST'])
@limiter.limit("15 per minute")
def subject_material():
    if request.method == "POST":
        target_link = request.form.get('link') # this link must be of the form https://mydy.dypatil.edu/rait/course/view.php?id=[SUBJECT_ID]

        cookies = session['session_cookie']
        
        response = core_utils.get_subject_materials(target_link, cookies=cookies)
        
        return response

@app.route('/download', methods=['POST'])
@limiter.limit("15 per minute")
def download_resource():
    
    if request.method == "POST":
        target_link = request.form.get('link') #this link must be of the form https://https://mydy.dypatil.edu/rait/mod/flexpaper/view.php?id=606779
                                                # or https://mydy.dypatil.edu/rait/mod/presentation/view.php?id=611990
        link_type = request.form.get('type')
        cookies = session['session_cookie']
        
        response = core_utils.get_download_link(target_link, link_type, cookies)
        
        if(response != None):
            return response

        return Response(status=401)
    
        
if __name__ == "__main__":
    
    logging.debug(f"Started {__file__} at 0.0.0.0:8000")
    
    app.run(
        debug=True, 
        host='0.0.0.0', 
        port=8000
    )







