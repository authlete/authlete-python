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
from authlete.dto.authorization_issue_request import AuthorizationIssueRequest
from authlete.dto.property                    import Property


class TestAuthorizationIssueRequest(unittest.TestCase):
    def test_from_json(self):
        jsn = '''{
          "ticket":     "TICKET",
          "subject":    "SUBJECT",
          "sub":        "SUB",
          "authTime":   12345678,
          "acr":        "ACR",
          "claims":     "CLAIMS",
          "properties": [
            { "key": "K0", "value": "V0", "hidden": true },
            { "key": "K1", "value": "V1", "hidden": false }
          ],
          "scopes": [
            "S0", "S1"
          ]
        }'''

        req = AuthorizationIssueRequest.from_json(jsn)

        self.assertEqual(req.ticket,   "TICKET")
        self.assertEqual(req.subject,  "SUBJECT")
        self.assertEqual(req.sub,      "SUB")
        self.assertEqual(req.authTime, 12345678)
        self.assertEqual(req.acr,      "ACR")
        self.assertEqual(req.claims,   "CLAIMS")

        props = req.properties
        self.assertIsInstance(props, list)
        self.assertEqual(len(props), 2)

        prop0 = props[0]
        self.assertIsInstance(prop0, Property)
        self.assertEqual(prop0.key,   "K0")
        self.assertEqual(prop0.value, "V0")
        self.assertTrue( prop0.hidden)

        prop1 = props[1]
        self.assertIsInstance(prop1, Property)
        self.assertEqual(prop1.key,   "K1")
        self.assertEqual(prop1.value, "V1")
        self.assertFalse(prop1.hidden)

        scopes = req.scopes
        self.assertIsInstance(scopes, list)
        self.assertEqual(len(scopes), 2)
        self.assertEqual(scopes[0], "S0")
        self.assertEqual(scopes[1], "S1")


    def test_to_json(self):
        prop0 = Property()
        prop0.key    = "K0"
        prop0.value  = "V0"
        prop0.hidden = True
        prop1 = Property()
        prop1.key    = "K1"
        prop1.value  = "V1"
        prop1.hidden = False

        req = AuthorizationIssueRequest()
        req.ticket     = "TICKET"
        req.subject    = "SUBJECT"
        req.sub        = "SUB"
        req.authTime   = 12345678
        req.acr        = "ACR"
        req.claims     = "CLAIMS"
        req.properties = [ prop0, prop1 ]
        req.scopes     = [ "S0", "S1" ]

        jsn = req.to_json()
        dct = json.loads(jsn)

        self.assertEqual(dct['ticket'],   "TICKET")
        self.assertEqual(dct['subject'],  "SUBJECT")
        self.assertEqual(dct['sub'],      "SUB")
        self.assertEqual(dct['authTime'], 12345678)
        self.assertEqual(dct['acr'],      "ACR")
        self.assertEqual(dct['claims'],   "CLAIMS")

        props = dct['properties']
        self.assertIsInstance(props, list)
        self.assertEqual(len(props), 2)

        self.assertIsInstance(props[0], dict)
        self.assertEqual(props[0]['key'],   "K0")
        self.assertEqual(props[0]['value'], "V0")
        self.assertTrue( props[0]['hidden'])
        self.assertEqual(props[1]['key'],   "K1")
        self.assertEqual(props[1]['value'], "V1")
        self.assertFalse(props[1]['hidden'])

        scopes = dct['scopes']
        self.assertIsInstance(scopes, list)
        self.assertEqual(len(scopes), 2)
        self.assertEqual(scopes[0],   "S0")
        self.assertEqual(scopes[1],   "S1")
