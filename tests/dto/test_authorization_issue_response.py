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
from authlete.dto.authorization_issue_action   import AuthorizationIssueAction
from authlete.dto.authorization_issue_response import AuthorizationIssueResponse


class TestAuthorizationIssueResponse(unittest.TestCase):
    def test_from_json(self):
        jsn = '''{
          "resultCode":           "RESULT_CODE",
          "resultMessage":        "RESULT_MESSAGE",
          "action":               "LOCATION",
          "responseContent":      "RESPONSE_CONTENT",
          "accessTokenExpiresAt": 12345,
          "accessTokenDuration":  67890,
          "authorizationCode":    "AUTHORIZATION_CODE",
          "jwtAccessToken":       "JWT_ACCESS_TOKEN"
        }'''

        res = AuthorizationIssueResponse.from_json(jsn)

        self.assertEqual(res.resultCode,    "RESULT_CODE")
        self.assertEqual(res.resultMessage, "RESULT_MESSAGE")

        action = res.action
        self.assertIsInstance(action, AuthorizationIssueAction)
        self.assertIs(action, AuthorizationIssueAction.LOCATION)

        self.assertEqual(res.responseContent,      "RESPONSE_CONTENT")
        self.assertEqual(res.accessTokenExpiresAt, 12345)
        self.assertEqual(res.accessTokenDuration,  67890)
        self.assertEqual(res.authorizationCode,    "AUTHORIZATION_CODE")
        self.assertEqual(res.jwtAccessToken,       "JWT_ACCESS_TOKEN")


    def test_from_json_default(self):
        res = AuthorizationIssueResponse.from_json('{}')

        self.assertIsNone(res.resultCode)
        self.assertIsNone(res.resultMessage)
        self.assertIsNone(res.action)
        self.assertIsNone(res.responseContent)

        expiresAt = res.accessTokenExpiresAt
        self.assertIsInstance(expiresAt, int)
        self.assertEqual(expiresAt, 0)

        duration = res.accessTokenDuration
        self.assertIsInstance(duration, int)
        self.assertEqual(duration, 0)

        self.assertIsNone(res.authorizationCode)
        self.assertIsNone(res.jwtAccessToken)


    def test_to_json(self):
        res = AuthorizationIssueResponse()
        res.resultCode           = "RESULT_CODE"
        res.resultMessage        = "RESULT_MESSAGE"
        res.action               = AuthorizationIssueAction.BAD_REQUEST
        res.responseContent      = "RESPONSE_CONTENT"
        res.accessTokenExpiresAt = 12345
        res.accessTokenDuration  = 67890
        res.authorizationCode    = "AUTHORIZATION_CODE"
        res.jwtAccessToken       = "JWT_ACCESS_TOKEN"

        jsn = res.to_json()
        dct = json.loads(jsn)

        self.assertEqual(dct['resultCode'],    "RESULT_CODE")
        self.assertEqual(dct['resultMessage'], "RESULT_MESSAGE")

        action = dct['action']
        self.assertIsInstance(action, str)
        self.assertEqual(action, "BAD_REQUEST")

        self.assertEqual(dct['responseContent'], "RESPONSE_CONTENT")

        expiresAt = dct['accessTokenExpiresAt']
        self.assertIsInstance(expiresAt, int)
        self.assertEqual(expiresAt, 12345)

        duration = dct['accessTokenDuration']
        self.assertIsInstance(duration, int)
        self.assertEqual(duration, 67890)

        self.assertEqual(dct['authorizationCode'], "AUTHORIZATION_CODE")
        self.assertEqual(dct['jwtAccessToken'],    "JWT_ACCESS_TOKEN")


    def test_to_json_default(self):
        res = AuthorizationIssueResponse()

        jsn = res.to_json()
        dct = json.loads(jsn)

        self.assertIsNone(dct['resultCode'])
        self.assertIsNone(dct['resultMessage'])
        self.assertIsNone(dct['action'])
        self.assertIsNone(dct['responseContent'])

        expiresAt = dct['accessTokenExpiresAt']
        self.assertIsInstance(expiresAt, int)
        self.assertEqual(expiresAt, 0)

        duration = dct['accessTokenDuration']
        self.assertIsInstance(duration, int)
        self.assertEqual(duration, 0)

        self.assertIsNone(dct['authorizationCode'])
        self.assertIsNone(dct['jwtAccessToken'])
