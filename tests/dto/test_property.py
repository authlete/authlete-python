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
from authlete.dto.property import Property


class TestProperty(unittest.TestCase):
    def test_from_json(self):
        jsn = '''{
          "key":    "K",
          "value":  "V",
          "hidden": true
        }'''

        prop = Property.from_json(jsn)

        self.assertEqual(prop.key,   "K")
        self.assertEqual(prop.value, "V")
        self.assertTrue( prop.hidden)


    def test_from_json_default(self):
        prop = Property.from_json('{}')

        self.assertIsNone(prop.key)
        self.assertIsNone(prop.value)
        self.assertFalse( prop.hidden)


    def test_to_json(self):
        prop = Property()
        prop.key    = "K"
        prop.value  = "V"
        prop.hidden = True

        jsn = prop.to_json()
        dct = json.loads(jsn)

        self.assertEqual(dct['key'],   "K")
        self.assertEqual(dct['value'], "V")
        self.assertTrue( dct['hidden'])


    def test_to_json_default(self):
        prop = Property()

        jsn = prop.to_json()
        dct = json.loads(jsn)

        self.assertIsNone(dct['key'])
        self.assertIsNone(dct['value'])
        self.assertFalse( dct['hidden'])
