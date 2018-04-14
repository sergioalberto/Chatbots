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

import os.path
import sys
import uuid

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = '6bbadc113b4844ed817948672713d5d0'


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'en'  # optional, default value equal 'en'

    # some unuque session id for user identification
    request.session_id = uuid.uuid4().hex

    request.query = "Hello"

    response = request.getresponse()
    # result = response['result']

    print (response.read())
    #print (result['resolvedQuery'].lower())

if __name__ == '__main__':
    main()
