from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
<<<<<<< HEAD
    return '<h1>Hello World</h1>'
=======
    return 'Hello everyone!!!'
>>>>>>> 360ed0cb22bdb413ad0c2b33f4afff284f45fcac
