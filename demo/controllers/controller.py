#!/usr/bin/env python

# Created by Eng.Sergio GQ
# 13/4/2018
# Cartago, Costa Rica

import socket, uuid, os
import sys, logging, json, base64
from logging.handlers import RotatingFileHandler

from demo.configuration.constants import *
from demo.orchestrator.orchestrator import *

# sudo pip install flask
from flask import Flask, render_template, request, jsonify, session
from flask.sessions import SessionInterface
from beaker.middleware import SessionMiddleware

global orchestrator
orchestrator = None

class BeakerSessionInterface(SessionInterface):
    def open_session(self, app, request):
        session = request.environ['beaker.session']
        return session

    def save_session(self, app, session, response):
        session.save()

# create a session key
if not os.path.exists("session.key") or not os.path.exists("session.secret"):
    session_secret = uuid.uuid4().hex
    session_key = uuid.uuid4().hex

    with open("session.secret", 'w') as f:
        f.write(session_secret)
    with open("session.key", 'w') as f:
        f.write(session_key)
else:
    with open("session.secret") as f:
        session_secret = f.read()
    with open("session.key") as f:
        session_key = f.read()

session_opts = {
    'session.lock_dir': '/',
    'session.data_dir': '/',
    'session.type': 'memory',
    'session.cookie_expires': int(60*5.5),
    'session.secret': session_secret,
    'session.key': session_key,
    'session.auto': True
}

app = Flask(__name__)
app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)
app.session_interface = BeakerSessionInterface()

@app.after_request
def after_request(response):
    response.headers.add('Cache-Control', 'no-cache, no-store, must-revalidate')
    response.headers.add('Pragma', 'no-cache')
    response.headers.add('Expires', '0')
    return response

@app.route("/", methods=['GET'])
def index():

    if not session.has_key('session_id'):
        session['session_id'] = uuid.uuid4().hex
    print ("MyId: "+session['session_id'])
    return render_template('index.html')

@app.route("/sendText", methods=['GET'])
def sent_text():

    if not session.has_key('session_id'):
        session['session_id'] = uuid.uuid4().hex

    print ("MyId: "+session['session_id'])
    text_to_send = request.args.get('textToSend', '')
    global orchestrator
    response = orchestrator.chat_with_bot(text_to_send, session['session_id'])

    return jsonify(response=response)

class Controller:

    def __init__(self, config):

        global orchestrator
        orchestrator = Orchestrator(config)

        #formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
        #handler = RotatingFileHandler(Constants.LOG_FILE, maxBytes=10000000, backupCount=5)
        #handler.setLevel(logging.DEBUG)
        #handler.setFormatter(formatter)
        #app.logger.addHandler(handler)
        #reload(sys)
        #sys.setdefaultencoding('utf-8')

        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        app.run(host=IPAddr, debug=False)
