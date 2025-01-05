from flask import Flask, render_template, request, jsonify
import requests
import threading
import time

app = Flask(__name__)

# Data structure to hold the hostname and count
data_store = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query_backend', methods=['POST'])
def query_backend():
    # Get the number of queries to make
    query_count = int(request.form.get('query_count', 1))
    backend_url = "http://127.0.0.1:5001/get_info"
    
    query_results = {"data": [], "iterations": []}

    for i in range(query_count):
        try:
            # Make a request to the backend server
            backend_response = requests.get("queryBackend")
            if backend_response.ok:
                Iteration_number(i)})
                  )
app_template.querylimit--

It seems the response was cut off. Let me rewrite the correct implementation of the **Frontend Server** code.

---

### Full Frontend Server Code (`frontend_server.py`)

```python
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Data structure to hold the hostname and counts
data_store = {}
query_iteration = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query_backend', methods=['POST'])
def query_backend():
    global query_iteration, data_store

    # Get the number of queries to make
    query_count = int(request.form.get('query_count', 1))
    backend_url = "http://127.0.0.1:5001/get_info"

    query_iteration = 0  # Reset the query iteration counter
    for _ in range(query_count):
        query_iteration += 1  # Increment the iteration counter
        try:
            response = requests.get(backend_url)
            if response.status_code == 200:
                data = response.json()
                hostname = data["hostname"]
                ip_address = data["ip_address"]

                # Update the data store with hostname and count
                if hostname in data_store:
                    data_store[hostname]["count"] += 1
                else:
                    data_store[hostname] = {"ip_address": ip_address, "count": 1}
        except Exception as e:
            print(f"Error querying backend: {e}")

    return jsonify({"status": "success", "data": data_store, "iteration": query_iteration})

@app.route('/get_data', methods=['GET'])
def get_data():
    # Return the current state of the data store
    return jsonify(data_store)

@app.route('/get_iteration', methods=['GET'])
def get_iteration():
    # Return the current query iteration
    return jsonify({"iteration": query_iteration})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)