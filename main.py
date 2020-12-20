from flask import jsonify, render_template
import connexion

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


def create_app():
    # app = Flask(__name__, template_folder='templates')
    app = connexion.App(__name__, specification_dir='specification')
    app.add_api('swagger.yml')
    return app


app = create_app()


@app.route('/items', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': items})


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/')
def index():
    return 'Python REST API in Flask'


app.run(host='0.0.0.0', port=48080, debug=True)
