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
from authlete.dto.authorization_fail_action   import AuthorizationFailAction
from authlete.dto.authorization_fail_response import AuthorizationFailResponse


class TestAuthorizationFailResponse(unittest.TestCase):
    def test_from_json(self):
        jsn = '''{
          "resultCode":      "CODE",
          "resultMessage":   "MESSAGE",
          "action":          "LOCATION",
          "responseContent": "CONTENT"
        }'''

        res = AuthorizationFailResponse.from_json(jsn)

        self.assertEqual(res.resultCode,    "CODE")
        self.assertEqual(res.resultMessage, "MESSAGE")

        action = res.action
        self.assertIsInstance(action, AuthorizationFailAction)
        self.assertIs(action, AuthorizationFailAction.LOCATION)

        self.assertEqual(res.responseContent, "CONTENT")


    def test_from_json_default(self):
        res = AuthorizationFailResponse.from_json('{}')

        self.assertIsNone(res.resultCode)
        self.assertIsNone(res.resultMessage)
        self.assertIsNone(res.action)
        self.assertIsNone(res.responseContent)


    def test_to_json(self):
        res = AuthorizationFailResponse()
        res.resultCode      = "CODE"
        res.resultMessage   = "MESSAGE"
        res.action          = AuthorizationFailAction.BAD_REQUEST
        res.responseContent = "CONTENT"

        jsn = res.to_json()
        dct = json.loads(jsn)

        self.assertEqual(dct['resultCode'],    "CODE")
        self.assertEqual(dct['resultMessage'], "MESSAGE")

        action = dct['action']
        self.assertIsInstance(action, str)
        self.assertEqual(action, "BAD_REQUEST")

        self.assertEqual(dct['responseContent'], "CONTENT")


    def test_to_json_default(self):
        res = AuthorizationFailResponse()

        jsn = res.to_json()
        dct = json.loads(jsn)

        self.assertIsNone(dct['resultCode'])
        self.assertIsNone(dct['resultMessage'])
        self.assertIsNone(dct['action'])
        self.assertIsNone(dct['responseContent'])
