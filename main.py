from flask import Flask, jsonify

app = Flask(__name__)

items = [
    {
        'id': 1,
        'name': u'Unkown item'
    },
    {
        'id': 2,
        'name': u'Secret item'
    }
]


@app.route('/items', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': items})


@app.route('/')
def index():
    return 'Python REST API in Flask'


app.run(host='0.0.0.0', port=48080)
