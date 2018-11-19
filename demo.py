#!/usr/bin/env python

# Created by Eng.Sergio GQ
# 14/4/2018
# Cartago, Costa Rica

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os, uuid
import sys
import argparse
import six

if six.PY2:
    import ConfigParser as configparser
else:
    import configparser

from demo.core.core import *

config = configparser.ConfigParser()

def config_read(configuration_file):
    return config.read(configuration_file)

def main(information):

    print ("----------------------------------------------------------------------------------")
    print ("Welcome to chatbot terminal.")
    print ("Here you can test and chat with a chatbot that you have trained on Google or IBM.")
    print ("Created by Sergio GQ.")
    print ("Cartago, Costa Rica.")
    print ("----------------------------------------------------------------------------------")
    print ("")
    print ("Note: To quit, just type 'Bye'.")
    print ("")

    session_id = uuid.uuid4().hex
    chat = Core(information)

    while True:
        message = raw_input('Type a message ... : ')

        if (message.lower() == "bye"):
            break

        print (" >> You: "+message)
        response = chat.chat_with_bot(message, session_id)
        print (" >> GAPBot: "+response)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Chatbot demo using Google or IBM SDK')
    parser.add_argument('-conf', '--configuration_file', help='The configuration file. e.g: configFile.ini', required=True)
    parser.add_argument('-sdk', '--sdk_kind', help='Google or IBM SDK. e.g: Google', required=True)
    args = parser.parse_args()

    configuration_file = args.configuration_file
    if not config_read(configuration_file):
        print ('The file {} could not found'.format(configuration_file))
    else:
        information = {}
        information['SDK'] = args.sdk_kind
        information['ACCESS_TOKEN'] = config.get('GOOGLE', 'CLIENT_ACCESS_TOKEN')

        information['IBM_USERNAME'] = config.get('IBM', 'USERNAME')
        information['IBM_PASSWORD'] = config.get('IBM', 'PASSWORD')
        information['IBM_WORKSPACE_ID'] = config.get('IBM', 'WORKSPACE_ID')

        main(information)
