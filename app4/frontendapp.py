# frontend_server.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/query-backend', methods=['GET'])
def query_backend():
    backend_url = 'http://127.0.0.1:5001/info'
    try:
        response = requests.get(backend_url)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Frontend server runs on port 5000