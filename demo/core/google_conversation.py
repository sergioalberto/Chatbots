#!/usr/bin/env python

# Created by Eng.Sergio GQ
# 14/4/2018
# Cartago, Costa Rica

import os
import json
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

    # Allow to chat with a bot
    # Parameters:
    # => text_to_send: text to send bot
    # => session_id: id to user identify
    # => verbose: if you want to print something
    # Return:
    # => JSON: Object return Google
    def chat(self, text_to_send, session_id="", verbose=True):

        if not session_id:
            self.session_id = uuid.uuid4().hex
        else:
            self.session_id = session_id

        return self.__send_message(text_to_send, self.session_id, verbose=verbose)

    # Allow to send a text to bot
    # Parameters:
    # => text_to_send: text to send bot
    # => session_id: id to user identify
    # => lang: The language to use. e.i: en, es
    # => verbose: if you want to print something
    # Return:
    # => JSON: Object return Google
    def __send_message(self, text_to_send, session_id, lang='en', verbose=True):

        ai = apiai.ApiAI(self.access_token)

        request = ai.text_request()

        request.lang = lang  # optional, default value equal 'en'

        # some unuque session id for user identification
        request.session_id = session_id

        request.query = text_to_send

        response = request.getresponse()
        response = json.loads(response.read().decode())

        if verbose:
            print (response)

        return response
