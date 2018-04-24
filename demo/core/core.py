#!/usr/bin/env python

# Created by Eng.Sergio GQ
# 14/4/2018
# Cartago, Costa Rica

from demo.core.google.google_conversation import *
from demo.core.ibm.ibm_conversations import *

class Core:

    def __init__(self, sdk_info):
        self.sdk = sdk_info['SDK']
        if (self.sdk.lower() == "google"):
            self.is_google = True
            self.google_conversation = Google_Conversation(sdk_info['ACCESS_TOKEN'])
        else:
            self.is_google = False
            self.ibm_conversations = IBM_Conversations(sdk_info['IBM_USERNAME'],
                                                       sdk_info['IBM_PASSWORD'],
                                                       sdk_info['IBM_WORKSPACE_ID'])

    # Allow to get the Google text response
    # Parameters:
    # => json_response: The JSON Google response
    # Return:
    # => String: The text response
    def __get_google_text_response(self, json_response):
        response = json_response['result']['fulfillment']['speech']
        return response

    # Allow to get the IBM text response
    # Parameters:
    # => json_response: The JSON IBM response
    # Return:
    # => String: The text response
    def __get_ibm_text_response(self, json_response):
        response = json_response['output']['text'][0]
        return response

    # Chat with the bot
    # Parameters:
    # => text_to_send: text to send bot
    # => session_id: id to user identify
    # Return:
    # => String: The text response
    def chat_with_bot(self, text_to_send, session_id=""):

        if self.is_google:
            response = self.google_conversation.chat(text_to_send, session_id, False)
            return self.__get_google_text_response(response)
        else:
            response = self.ibm_conversations.chat(text_to_send, session_id, False)
            return self.__get_ibm_text_response(response)
