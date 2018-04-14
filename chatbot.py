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
    parser.add_argument('-conf', '--configuration_file', help='The configuration file', required=True)
    args = parser.parse_args()

    configuration_file = args.configuration_file
    config_read(configuration_file)

    print(config.sections())
    controller = Controller(config)
