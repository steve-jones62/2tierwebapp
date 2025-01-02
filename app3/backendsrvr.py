from flask import Flask, jsonify
import socket

app = Flask(__name__)
@app.route('/', methods=['GET'])
def root():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return jsonify({
        'hostname': hostname,
        'ip_address': ip_address
    })

@app.route('/apisvc', methods=['GET'])
def index():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return jsonify({
        'hostname': hostname,
        'ip_address': ip_address
    })

@app.route('/info', methods=['GET'])
def get_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return jsonify({
        'hostname': hostname,
        'ip_address': ip_address
    })
@app.route('/api/v1/view', methods=['GET'])
def view():
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    time_stamp = datetime.now()
    return_info = {
        'Host_Name': hostname,
        'IP_Address': ip_addr,
        'Timestamp': time_stamp
    }
    return jsonify(return_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
