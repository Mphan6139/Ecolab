from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from landing import *
from ardware import *

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True
app.config['TESTING'] = True

currUser = None

@app.route("/")
def hello():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.lower()

    for user in users:
        if user.name == processed_text:
            currUser = user
            redirect('/landing')
            return currUser
    
    return False

@app.route('/landing')
def landing():
    return render_template('landing.html', user=str(currUser))


if __name__ == '__main__':
    app.run(debug = True)


