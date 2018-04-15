#!/usr/bin/env python

# Created by Eng.Sergio GQ
# 14/4/2018
# Cartago, Costa Rica

from demo.core.google_conversation import *

class Core:

    def __init__(self, sdk_info):
        self.sdk = sdk_info['SDK']
        if (self.sdk.lower() == "google"):
            self.is_google = True
            self.google_conversation = Google_Conversation(sdk_info['ACCESS_TOKEN'])
        else:
            self.is_google = False

    # Allow to get the google text response
    # Parameters:
    # => json_response: The JSON Google response
    # Return:
    # => String: The text response
    def __get_google_text_response(self, json_response):
        response = json_response['result']['fulfillment']['speech']
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
            return ""
