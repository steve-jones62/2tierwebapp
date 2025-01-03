#! /usr/bin/env python3
# frontend_server.py
import os
from flask import Flask, render_template, send_from_directory
import requests
import socket
import json
from datetime import datetime



app = Flask(__name__)
HOSTNAME = socket.gethostname()
IP_ADDR = socket.gethostbyname(HOSTNAME)
NAMESPACE = "gitops-webby" if "gitops" in HOSTNAME else "webby"
PORT = "30999" if "gitops" in HOSTNAME else "5001"
# BASE_URL = f"http://ocp01-hpe02.pedemo.ignw.io:{PORT}"
# Changed with new RHOS Route - make sure it is created
BASE_URL = "https://webby-webby.apps.ocp-hpe02.pedemo.ignw.io/" if "webby" in HOSTNAME else "https://127.0.0.1/"


# This grabs the file 'index.html' out of the TEMPLATES subdir and serves it.
@app.route('/')
def root():
    time_stamp = datetime.now()
    return render_template('index.html', hostname=HOSTNAME, ip_addr=IP_ADDR, time_stamp=time_stamp, base_url = BASE_URL)

@app.route('/index')
def index():
    time_stamp = datetime.now()
    return render_template('index.html', hostname=HOSTNAME, ip_addr=IP_ADDR, time_stamp=time_stamp, base_url = BASE_URL)

# This is to fix the favicon file not being found by Flask - no idea why it cannot
@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/query-backend', methods=['GET'])
def query_backend():
    backend_url = 'http://127.0.0.1:5001/info'
    try:
        response = requests.get(backend_url)
        print (response.json())
        return response.json()
        
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Frontend server runs on port 5000