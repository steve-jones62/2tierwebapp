from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Store data as a list of dictionaries
data_list = []

@app.route('/')
def index():
    """
    Displays the main page with the input form and dynamic table.
    """
    return render_template('index.html', data=data_list)

@app.route('/query_backend', methods=['POST'])
def query_backend():
    """
    Queries the backend server multiple times and processes the data.
    """
    global data_list
    backend_url = "http://localhost:5001/get_info"
    num_queries = int(request.form.get("num_queries", 1))

    for _ in range(num_queries):
        try:
            response = requests.get(backend_url)
            if response.status_code == 200:
                backend_data = response.json()
                name = backend_data.get("name", "Unknown")
                ip = backend_data.get("ip", "Unknown")
                
                # Check if the name is already in the list
                for entry in data_list:
                    if entry["name"] == name:
                        entry["count"] += 1
                        break
                else:
                    # Add new entry if name doesn't exist
                    data_list.append({"name": name, "ip": ip, "count": 1})
        except requests.RequestException as e:
            print(f"Error querying backend: {e}")
    
    return jsonify({"status": "success", "data": data_list})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)