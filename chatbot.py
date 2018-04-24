#!/usr/bin/env python

# Created by Eng.Sergio GQ
# 13/4/2018
# Cartago, Costa Rica

import argparse
import six

if six.PY2:
    import ConfigParser as configparser
else:
    import configparser
from demo.controllers.controller import *

config = configparser.ConfigParser()

def config_read(configuration_file):
    return config.read(configuration_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Chatbot demo')
    parser.add_argument('-conf', '--configuration_file', help='The configuration file. e.g: configFile.ini', required=True)
    parser.add_argument('-sdk', '--sdk_kind', help='Google or IBM SDK. e.g: Google', required=True)
    args = parser.parse_args()

    configuration_file = args.configuration_file
    config_read(configuration_file)

    information = {}
    information['SDK'] = args.sdk_kind
    information['ACCESS_TOKEN'] = config.get('GOOGLE', 'CLIENT_ACCESS_TOKEN')

    information['IBM_USERNAME'] = config.get('IBM', 'USERNAME')
    information['IBM_PASSWORD'] = config.get('IBM', 'PASSWORD')
    information['IBM_WORKSPACE_ID'] = config.get('IBM', 'WORKSPACE_ID')

    controller = Controller(information)
