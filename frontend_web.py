# Backend Server (backend.py)
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database
data_store = []

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
    app.run(debug=True, port=5000, host=0.0.0.0)
