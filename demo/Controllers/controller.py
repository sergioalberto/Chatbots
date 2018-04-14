#!/usr/bin/env python

# Created by Eng.Sergio GQ
# 13/4/2018
# Cartago, Costa Rica

import socket
import sys, logging, json
from logging.handlers import RotatingFileHandler

from demo.configuration.constants import *

# sudo pip install flask
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

class Controller:

    def __init__(self, config):
        formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
        handler = RotatingFileHandler(Constants.LOG_FILE, maxBytes=10000000, backupCount=5)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        app.logger.addHandler(handler)
        #reload(sys)
        #sys.setdefaultencoding('utf-8')

        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        app.run(host=IPAddr, debug=True)
