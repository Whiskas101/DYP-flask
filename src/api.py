
#main entry point for the app
from flask import Flask, request, session

#Core functionality of the app, authentication and fetching commonly used data
#exists within this module
from utils import core_utils

app = Flask(__name__)
app.secret_key = 'this_college_fucking_sucks'

@app.route('/test')
def hello_warudo():
    return f'''
        向かって来るのか？\n
        ザワールドー
    '''

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # data from the end user
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Send login request to the dypatil site
        response = core_utils.attempt_login(username=username, password=password)

        #set the session cookie obtained previously
        session['session_cookie'] = response


        #return the cookies of the session object, or the status code if it fails to login
        return response


@app.route('/subjects', methods=['GET'])
def subjects():
    cookies = session['session_cookie']
    #Maybe a decorator, or an if statement can be implemented here to avoid cookies being empty (user session ended/user log out)
    #potential boost in readability here, by using a decorator to validate the existence of a session cookie instead

    response = core_utils.get_subjects(cookies=cookies)

    print(response)
    return response


if __name__ == "__main__":
    app.run()







