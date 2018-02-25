from flask import Flask
app = Flask(__name__)

@app.route('/')
def portfolio():
    return '<h1>Welcome to my portfolio.<h1>' + '<h2>My name is Pete.</h2>'

@app.route('/projects')
def projects():
    return 'My projects:' + '\n' + '<ul><li>Python</li><li>Flask</li><li>Django</li></ul>'

@app.route('/aboutMe')
def aboutMe():
    return 'I am a Python web developer and love playing logic games in my spare time.'

app.run(debug=True)