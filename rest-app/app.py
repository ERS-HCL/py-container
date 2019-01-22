from flask import Flask
app = Flask(__name__)

@app.route('/api/info')
def api_info():
    return 'API version 1.0 in rest-app Python webapp!'
