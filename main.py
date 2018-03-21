from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
	return render_template('user_signup.html', title="User Signup")

@app.route('/validate', methods=['POST'])
def validate():
  
    # define variables
    user = request.form['user']
    password = request.form['password']
    password2 = request.form['password2']
    email = request.form['email']
    
    # define error variables
    empty_field_error = ''
    invalid_chars_error = ''
    passwords_dont_match_error = ''
    invalid_email_error = ''
    
    # check for empty fields
    check_list = [user,password,password2]
    for field in check_list:
        if len(field) < 1:
            empty_field_error = 'Please fill out field'
            
    # check character length 3-20
    for field in check_list:
        if len(field) < 3 or len(field)> 20:
            invalid_chars_error = 'Please enter phrase no less than 3 and no greater than 20'

    # check passwords match
    while password != password2:
        passwords_dont_match_error = 'Passwords do not match'
        password = ''
        password2 = ''
        
    # check valid email
    while email != '':
        at_sign = 0
        period = 0
        for char in email:
            if char == '@':
                at_sign += 1
            if char == '.':
                period += 1
        
        if at_sign == 1 and period == 1:
            invalid_email_error = ''
        else:
            invalid_email_error = 'Please enter a valid email address'

    if not empty_field_error and not invalid_chars_error and not passwords_dont_match_error and not invalid_email_error:
        return render_template('welcome_page.html', title="Welcome Page", name=user)
    else:
        return render_template('user_signup.html', name=user, empty_field_error=empty_field_error, 
        invalid_chars_error=invalid_chars_error,
        passwords_dont_match_error=passwords_dont_match_error,
        invalid_email_error=invalid_email_error)

'''@app.route('/welcome', methods=['POST'])
def welcome():
    user = request.form['user']
    return render_template('welcome_page.html', title="Welcome Page", name=user)'''

app.run()