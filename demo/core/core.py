#!/usr/bin/env python

# Created by Eng.Sergio GQ
# 14/4/2018
# Cartago, Costa Rica

from demo.core.google_conversation import *

class Core:

    def __init__(self, sdk_info):
        sdk = sdk_info['SDK']
        if (sdk == "Google"):
            self.is_google = True
            self.google_conversation = Google_Conversation(sdk_info['ACCESS_TOKEN'])
        else:
            self.is_google = False

    def chat(self, text_to_send, session_id=""):
        if self.is_google:
            return self.google_conversation.chat()
