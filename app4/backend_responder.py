# backend_server.py
from flask import Flask, jsonify
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def get_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    time_stamp = datetime.now()
    return jsonify({
        "hostname": hostname,
        "ip_address": ip_address,
        "time_stamp": time_stamp
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Backend server runs on port 5001