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
from authlete.dto.address import Address


class TestAddress(unittest.TestCase):
    def test_from_json(self):
        jsn = '''{
          "formatted":      "F",
          "street_address": "S",
          "locality":       "L",
          "region":         "R",
          "postal_code":    "P",
          "country":        "C"
        }'''

        addr = Address.from_json(jsn)

        self.assertEqual(addr.formatted,     "F")
        self.assertEqual(addr.streetAddress, "S")
        self.assertEqual(addr.locality,      "L")
        self.assertEqual(addr.region,        "R")
        self.assertEqual(addr.postalCode,    "P")
        self.assertEqual(addr.country,       "C")


    def test_from_json_default(self):
        addr = Address.from_json('{}')

        self.assertIsNone(addr.formatted)
        self.assertIsNone(addr.streetAddress)
        self.assertIsNone(addr.locality)
        self.assertIsNone(addr.region)
        self.assertIsNone(addr.postalCode)
        self.assertIsNone(addr.country)


    def test_to_json(self):
        addr = Address()
        addr.formatted     = "F"
        addr.streetAddress = "S"
        addr.locality      = "L"
        addr.region        = "R"
        addr.postalCode    = "P"
        addr.country       = "C"

        jsn = addr.to_json()
        dct = json.loads(jsn)

        self.assertEqual(dct['formatted'],      "F")
        self.assertEqual(dct['street_address'], "S")
        self.assertEqual(dct['locality'],       "L")
        self.assertEqual(dct['region'],         "R")
        self.assertEqual(dct['postal_code'],    "P")
        self.assertEqual(dct['country'],        "C")


    def test_to_json_default(self):
        addr = Address()

        jsn = addr.to_json()
        dct = json.loads(jsn)

        self.assertIsNone(dct['formatted'])
        self.assertIsNone(dct['street_address'])
        self.assertIsNone(dct['locality'])
        self.assertIsNone(dct['region'])
        self.assertIsNone(dct['postal_code'])
        self.assertIsNone(dct['country'])


    def test_streetAddress(self):
        addr = Address()
        addr.streetAddress = "S"
        self.assertEqual(addr.streetAddress,  "S")
        self.assertEqual(addr.street_address, "S")


    def test_postalCode(self):
        addr = Address()
        addr.postalCode = "P"
        self.assertEqual(addr.postalCode,  "P")
        self.assertEqual(addr.postal_code, "P")
