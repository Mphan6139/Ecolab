from flask import Flask, render_template, flash, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from landing import *
from multiprocessing import Process
from ardware import *
from threading import Thread


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True
app.config['TESTING'] = True

currUser = None

@app.route("/")
def hello():
    return render_template('home.html')


@app.route('/', methods=['POST'])
# @app.route('/background_process_test')
# @app.route('/background_process_test')
def my_form_post():
    text = request.form['text']
    processed_text = text.lower()

    print(processed_text)
    for user in users:
        if user.name == processed_text:
            currUser = user
            redirect(url_for('/landing'))
            return currUser

    return 'hi'

@app.route('/landing')
def landing():
    return render_template('landing.html', user=str(currUser))


if __name__ == '__main__':
    # a = ArdWare()
    # print(a)
    # p.start()
    t = Thread(target=d.run, args=())
    t.start()
    app.run(debug = True, use_reloader=False)
    # p.join()
    t.join()
