#
# Copyright (C) 2019 Authlete, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the
# License.


import json
import unittest
from authlete.dto.authorization_fail_reason  import AuthorizationFailReason
from authlete.dto.authorization_fail_request import AuthorizationFailRequest


class TestAuthorizationFailRequest(unittest.TestCase):
    def test_from_json(self):
        jsn = '''{
          "ticket":      "TICKET",
          "reason":      "DENIED",
          "description": "DESCRIPTION"
        }'''

        req = AuthorizationFailRequest.from_json(jsn)

        self.assertEqual(req.ticket, "TICKET")

        reason = req.reason
        self.assertIsInstance(reason, AuthorizationFailReason)
        self.assertIs(reason, AuthorizationFailReason.DENIED)

        self.assertEqual(req.description, "DESCRIPTION")


    def test_from_json_default(self):
        req = AuthorizationFailRequest.from_json('{}')

        self.assertIsNone(req.ticket)
        self.assertIsNone(req.reason)
        self.assertIsNone(req.description)


    def test_to_json(self):
        req = AuthorizationFailRequest()
        req.ticket      = "TICKET"
        req.reason      = AuthorizationFailReason.UNKNOWN
        req.description = "DESCRIPTION"

        jsn = req.to_json()
        dct = json.loads(jsn)

        self.assertEqual(dct['ticket'], "TICKET")

        reason = dct['reason']
        self.assertIsInstance(reason, str)
        self.assertEqual(reason, "UNKNOWN")

        self.assertEqual(dct['description'], "DESCRIPTION")


    def test_to_json_default(self):
        req = AuthorizationFailRequest()

        jsn = req.to_json()
        dct = json.loads(jsn)

        self.assertIsNone(dct['ticket'])
        self.assertIsNone(dct['reason'])
        self.assertIsNone(dct['description'])
