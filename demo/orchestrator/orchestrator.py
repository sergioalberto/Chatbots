#!/usr/bin/env python

# Created by Eng.Sergio GQ
# 15/4/2018
# Cartago, Costa Rica

from demo.core.core import *

class Orchestrator:

    def __init__(self, sdk_info):
        self.core = Core(sdk_info)

    def chat_with_bot(self, text_to_send):
        return "hello"

