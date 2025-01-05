from flask import Flask, render_template, request, jsonify
import requests
from collections import defaultdict

app = Flask(__name__)

# In-memory storage for data and counters
data_list = []
name_counter = defaultdict(int)

@app.route("/")
def index():
    """
    Renders the main webpage.
    """
    return render_template("index.html")

@app.route("/query-backend", methods=["POST"])
def query_backend():
    """
    Queries the backend server and updates the data list.
    """
    backend_url = "http://127.0.0.1:5001/info"  # Backend server URL
    num_iterations = int(request.form.get("iterations", 1))

    for _ in range(num_iterations):
        try:
            response = requests.get(backend_url)
            response.raise_for_status()
            backend_data = response.json()

            # Update name counter and data list
            name = backend_data["name"]
            name_counter[name] += 1
            data_list.append({
                "name": name,
                "ip": backend_data["ip"],
                "count": name_counter[name]
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"success": True, "data": data_list})

@app.route("/get-data", methods=["GET"])
def get_data():
    """
    Returns the current data list as JSON.
    """
    return jsonify(data_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Running frontend on port 5000