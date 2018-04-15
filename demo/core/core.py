#!/usr/bin/env python

# Created by Eng.Sergio GQ
# 14/4/2018
# Cartago, Costa Rica

from demo.core.google_conversation import *

class Core:

    def __init__(self, sdk_info):
        self.sdk = sdk_info['SDK']
        if (self.sdk == "Google"):
            self.is_google = True
            self.google_conversation = Google_Conversation(sdk_info['ACCESS_TOKEN'])
        else:
            self.is_google = False

    def __get_text(self, json_response):
        response = json_response['result']['fulfillment']['speech']
        return response

    def chat_with_bot(self, text_to_send, session_id=""):

        if self.is_google:
            response = self.google_conversation.chat(text_to_send, session_id, False)
            return self.__get_text(response)
        else:
            return ""
