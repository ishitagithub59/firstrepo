from flask import Flask
app = Flask(__name__)

@app.route('/')
def New():
    return"<body bgcolor='green' text='white'><h1>Hi I am Anuja</h1></body>"
     