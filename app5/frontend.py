from flask import Flask, render_template, jsonify, request
import requests
from threading import Thread
import time

app = Flask(__name__)

# Data storage for the table
data_store = {}

@app.route('/')
def index():
    """
    Renders the main webpage.
    """
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_querying():
    """
    Starts querying the backend server.
    """
    iterations = int(request.json.get('iterations', 1))
    backend_url = "http://127.0.0.1:5001/info"

    for _ in range(iterations):
        try:
            response = requests.get(backend_url)
            if response.status_code == 200:
                result = response.json()
                name = result['name']
                ip = result['ip']
                if name in data_store:
                    data_store[name]['count'] += 1
                else:
                    data_store[name] = {'ip': ip, 'count': 1}
        except requests.exceptions.RequestException as e:
            print(f"Error querying backend server: {e}")
        time.sleep(1)  # Simulate delay between queries

    return jsonify({"status": "Completed", "data": data_store})

@app.route('/data', methods=['GET'])
def get_data():
    """
    Returns the collected data as JSON.
    """
    return jsonify(data_store)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)