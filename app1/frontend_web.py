# Frontend Application (frontend.py)
# required for 'send_from_directory
import os
import requests
# required for http server activites
from flask import Flask, render_template, send_from_directory


app = Flask(__name__)

# This grabs the file 'index.html' out of the TEMPLATES subdir and serves it.
@app.route('/')
def index():
    return render_template('index.html')

# This is to fix the favicon file not being found by Flask - no idea why it cannot
@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/data', methods=['POST'])
def add_data():
    data = requests.get('data')
    if data:
        response = requests.post('http://127.0.0.1:5000/api/data', json={"value": data})
        return response.json(), response.status_code
    return {"message": "Invalid input!"}, 400

@app.route('/data', methods=['GET'])
def get_data():
    response = requests.get('http://127.0.0.1:5000/api/data')
    return response.json(), response.status_code

if __name__ == '__main__':
    # We are making our app listen on the local host IP:5000
    app.run(debug=True, port=5001, host='0.0.0.0')
