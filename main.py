from flask import Flask, request, render_template
import re

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
    invalid_user_error = 'Please enter a valid username'
    invalid_password_error = 'Please enter a valid password'
    passwords_dont_match_error = 'Passwords do not match'
    invalid_email_error = ''
    
    # check username and password
    while len(user) > 2 and len(user) < 21:
        if re.search(' ', user):
            break
        invalid_user_error = ''
        break

    while len(password) > 2 and len(password) < 21:
        if re.search(' ', password):
            break
        invalid_password_error = ''
        break

    # check if passwords match
    if password == password2 and len(password) > 0:
        passwords_dont_match_error = ''
        
    # check valid email
    while email != '':
        if len(email) < 3:
            invalid_email_error = 'Your email must be longer than 3 characters.'
            break
        if len(email) > 20:
            invalid_email_error = 'Your email cannot be longer than 20 characters'
            break
        if re.search(' ', email):
            invalid_email_error = 'Your email cannot contain spaces'
            break
        at_sign = 0
        period = 0
        for char in email:
            if char == '@':
                at_sign += 1
            elif char == '.':
                period += 1
        
        if at_sign == 1 and period == 1:
            invalid_email_error = ''
        else:
            invalid_email_error = 'Your email must contain only one "@" and one "."'
        break

    if not invalid_user_error and not invalid_password_error and not passwords_dont_match_error and not invalid_email_error:
        return render_template('welcome_page.html', title="Welcome Page", name=user)
    else:
        return render_template('user_signup.html', name=user, email=email, invalid_user_error=invalid_user_error, 
        invalid_password_error=invalid_password_error,
        passwords_dont_match_error=passwords_dont_match_error,
        invalid_email_error=invalid_email_error)

'''@app.route('/welcome', methods=['POST'])
def welcome():
    user = request.form['user']
    return render_template('welcome_page.html', title="Welcome Page", name=user)'''

app.run()