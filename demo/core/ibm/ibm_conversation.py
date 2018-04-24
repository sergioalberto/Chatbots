#!/usr/bin/env python

# Created by Eng.Sergio GQ
# 23/4/2018
# Cartago, Costa Rica

import json

from watson_developer_cloud import AssistantV1

class IBM_Conversation:

    def __init__(self, username, password, workspace_id):
        self.username = username
        self.password = password
        self.workspace_id = workspace_id
        self.lastResponse = None

        self.assistant = AssistantV1(
            username=username,
            password=password,
            version='2017-04-21')

        self.assistant.set_http_config({'timeout': 100})

    # Allow to chat with a bot
    # Parameters:
    # => text_to_send: text to send bot
    # => context: user context
    # => verbose: if you want to print something
    # Return:
    # => JSON: Object return IBM
    def chat(self, text_to_send, verbose=True):
        print ("To chat with "+text_to_send)
        context = None
        if (self.lastResponse != None):
            context = self.lastResponse["context"]

        self.lastResponse = self.assistant.message(workspace_id=self.workspace_id, input={
            'text': text_to_send}, context=context)

        result = json.dumps(self.lastResponse, indent=2)
        if verbose:
            print(result)

        return self.lastResponse
