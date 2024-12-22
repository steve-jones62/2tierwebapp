# Backend Server (backend.py)
from flask import Flask, request, jsonify
# required for 'send_from_directory
import os

app = Flask(__name__)

# Mock database
data_store = []

# This is to fix the favicon file not being found by Flask - no idea why it cannot
@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.json
        if data:
            data_store.append(data)
            return jsonify({"message": "Data added successfully!", "data": data}), 201
        else:
            return jsonify({"message": "Invalid data!"}), 400
    elif request.method == 'GET':
        return jsonify(data_store), 200

if __name__ == '__main__':
    # We are making our app listen on the local host IP:5000
    app.run(debug=True, port=5000, host='0.0.0.0')
