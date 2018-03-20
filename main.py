from flask import Flask, request, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
	return render_template('user_signup.html', title="User Signup")

@app.route('/welcome', methods=['POST'])
def validate():
    # define variables
    # check for empty fields
    # check character length 3-20
    # check passwords match
    # check valid email

@app.route('/welcome', methods=["POST"])
def welcome():
    user = request.form['user']
    return render_template('welcome_page.html', title="Welcome Page", name=user)

app.run()