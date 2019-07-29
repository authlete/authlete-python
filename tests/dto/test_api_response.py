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
from authlete.dto.api_response import ApiResponse


class TestApiResponse(unittest.TestCase):
    def test_from_json(self):
        jsn = '''{
          "resultCode":    "C",
          "resultMessage": "M"
        }'''

        res = ApiResponse.from_json(jsn)

        self.assertEqual(res.resultCode,    "C")
        self.assertEqual(res.resultMessage, "M")


    def test_from_json_default(self):
        res = ApiResponse.from_json('{}')

        self.assertIsNone(res.resultCode)
        self.assertIsNone(res.resultMessage)


    def test_to_json(self):
        res = ApiResponse()
        res.resultCode    = "C"
        res.resultMessage = "M"

        jsn = res.to_json()
        dct = json.loads(jsn)

        self.assertEqual(dct['resultCode'],    "C")
        self.assertEqual(dct['resultMessage'], "M")


    def test_to_json_default(self):
        res = ApiResponse()

        jsn = res.to_json()
        dct = json.loads(jsn)

        self.assertIsNone(dct['resultCode'])
        self.assertIsNone(dct['resultMessage'])
