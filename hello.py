from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#new endpoint
@app.route('/space')
def to_space():
    return 'Welcome to space!'

@app.route('/home')
def my_home():
    return 'Welcome home.'