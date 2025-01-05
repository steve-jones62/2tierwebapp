from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# List to store collected data
collected_data = []
name_counter = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query_backend', methods=['POST'])
def query_backend():
    global collected_data, name_counter

    # Get the number of queries from the frontend
    query_count = int(request.form.get('query_count', 1))
    backend_url = "http://127.0.0.1:5001/get_info"
    
    for _ in range(query_count):
        try:
            response = requests.get(backend_url)
            if response.status_code == 200:
                data = response.json()
                name = data["name"]
                ip = data["ip"]
                
                # Increment counters for duplicate names
                if name in name_counter:
                    name_counter[name] += 1
                else:
                    name_counter[name] = 1
                
                # Add entry to collected data with the count
                collected_data.append({
                    "query_number": len(collected_data) + 1,
                    "name": name,
                    "ip": ip,
                    "count": name_counter[name]
                })
        except Exception as e:
            print(f"Error querying backend: {e}")
    
    return jsonify({"status": "success", "data": collected_data})

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(collected_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)