from flask import Flask, jsonify, request
import socket

app = Flask(__name__)

@app.route("/info", methods=["GET"])
def info():
    """
    Provides the backend server's name and IP address as JSON.
    """
    hostname = socket.gethostname()
    ip_address = request.remote_addr  # IP of the requester
    return jsonify({"name": hostname, "ip": ip_address})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)  # Running backend on port 5001