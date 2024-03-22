from flask import Flask, jsonify, request, send_from_directory, redirect, url_for
from authlib.integrations.flask_client import OAuth
import os
from dotenv import load_dotenv
load_dotenv()  # This loads the environment variables from .env file

app = Flask(__name__, static_folder='public')
app.secret_key = os.environ.get('SECRET_KEY', 'your_default_secret_key')

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.environ.get('GOOGLE_CLIENT_ID'),
    client_secret=os.environ.get('GOOGLE_CLIENT_SECRET'),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid profile email'},
)

tasks = []

@app.route('/')
def hello_world():
    return 'Hello, World! <a href="/login">Login</a>'

@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/auth')
def auth():
    token = google.authorize_access_token()
    user = google.parse_id_token(token)
    return f'Hello, {user["email"]}!'

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task_data = request.json
    tasks.append(task_data['task'])  # Assuming JSON contains a 'task' key
    return jsonify({'success': True}), 201

@app.route('/index', methods=['GET'])
def serve_index():
    return send_from_directory('public', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
