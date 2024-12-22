# Frontend Application (frontend.py)
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def add_data():
    data = request.form.get('data')
    if data:
        response = requests.post('http://127.0.0.1:5000/api/data', json={"value": data})
        return response.json(), response.status_code
    return {"message": "Invalid input!"}, 400

@app.route('/data', methods=['GET'])
def get_data():
    response = requests.get('http://127.0.0.1:5000/api/data')
    return response.json(), response.status_code

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
