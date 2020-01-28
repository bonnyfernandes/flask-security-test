from flask import Flask, request, redirect, render_template
from mongoengine import connect
from uuid import uuid4
from models.user import User


app = Flask(__name__)
app.db = connect('API', host='mongodb://localhost/flask-security-test')


@app.route('/')
def signup():
    return render_template("register.html")


@app.route('/signin')
def signin():
    return render_template("login.html")

@app.route('/register')
def signup():

    return "Registered"


if __name__ == '__main__':
    app.run(port=5000, debug=True)