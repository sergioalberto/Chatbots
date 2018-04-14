#!/usr/bin/env python

# Created by Eng.Sergio GQ
# 14/4/2018
# Cartago, Costa Rica

import os.path
import sys
import uuid

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

class Google_Conversation:

    def __init__(self, access_token):
        self.access_token = access_token

    def chat(self, text_to_send, session_id=""):
        if not session_id:
            self.session_id = uuid.uuid4().hex
        else:
            self.session_id = session_id

        return self.__send_message(text_to_send, self.session_id)

    def __send_message(self, text_to_send, session_id, lang='en'):
        ai = apiai.ApiAI(self.access_token)

        request = ai.text_request()

        request.lang = lang  # optional, default value equal 'en'

        # some unuque session id for user identification
        request.session_id = session_id

        request.query = text_to_send

        response = request.getresponse()
        # result = response['result']

        print (response.read())
        return response

google = Google_Conversation("6bbadc113b4844ed817948672713d5d0")
google.chat("Hello")
