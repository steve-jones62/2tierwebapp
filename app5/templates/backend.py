from flask import Flask, jsonify, request
import socket

app = Flask(__name__)

@app.route('/get_info', methods=['GET'])
def get_info():
    """
    Returns the backend server's name and IP address in JSON format.
    """
    server_name = socket.gethostname()
    server_ip = request.remote_addr
    return jsonify({"name": server_name, "ip": server_ip})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)