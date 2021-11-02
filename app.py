from flask import Flask
app = Flask(__name__)

@app.route('/')
def New():
    return"<body bgcolor='yellow' text='red'><h1>Hi I am Ishita</h1></body>"
     


