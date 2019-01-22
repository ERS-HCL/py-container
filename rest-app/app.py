from flask import Flask
app = Flask(__name__)

@app.route('/api/info')
def hello_world():
    return 'API version 1.0 in rest-app Python webapp!'
