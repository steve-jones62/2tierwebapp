from flask import Flask, jsonify, request
import socket

app = Flask(__name__)

@app.route('/get_info', methods=['GET'])
def get_info():
    hostname = socket.gethostname()
    ip_address = request.remote_addr
    return jsonify({"name": hostname, "ip": ip_address})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)