from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True
app.config['TESTING'] = True

posts = [
    {
        'author': 'me',
        'title': 'the title'
    },
    {
        'author':'you',
        'title':'the second title'
    }
]

@app.route("/")
def hello():
    return render_template('home.html', posts = posts)


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text


if __name__ == '__main__':
    app.run(debug = True)


