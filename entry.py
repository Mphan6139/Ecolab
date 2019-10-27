from flask import Flask,render_template
from landing import *

app = Flask(__name__)

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

@app.route("/about")
def about():
    return render_template('home.html',title = 'About')






if __name__ == '__main__':
    app.run(debug = True)


