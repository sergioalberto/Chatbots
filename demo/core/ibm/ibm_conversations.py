#!/usr/bin/env python

# Created by Eng.Sergio GQ
# 23/4/2018
# Cartago, Costa Rica

from demo.core.ibm.ibm_conversation import *

class IBM_Conversations:

    def __init__(self, username, password, workspace_id):
        self.username = username
        self.password = password
        self.workspace_id = workspace_id
        self.conversations = {}

    # Allow to chat with a bot
    # Parameters:
    # => text_to_send: text to send bot
    # => context: user context
    # => verbose: if you want to print something
    # Return:
    # => JSON: Object return IBM
    def chat(self, text_to_send, session_id="", verbose=True):
        result = None
        if session_id:
            conversation = None
            if session_id in self.conversations:
                conversation = self.conversations.get(session_id)
            else:
                conversation = IBM_Conversation(self.username, self.password, self.workspace_id)

            result = conversation.chat(text_to_send, verbose)

            self.conversations[session_id] = conversation

        return result
