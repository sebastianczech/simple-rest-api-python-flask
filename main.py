from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Python REST API in Flask'

app.run(host='0.0.0.0', port=48080)
