#
# Copyright (C) 2020 Authlete, Inc.
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
from authlete.aws.arn import ARN


class TestARN(unittest.TestCase):
    def test_parse(self):
        arn_string   = 'arn:aws:execute-api:us-east-2:123456789012:aabbccddee/stage-name/GET/pets'
        arn_instance = ARN.parse(arn_string)

        self.assertEqual(arn_instance.partition, "aws")
        self.assertEqual(arn_instance.service,   "execute-api")
        self.assertEqual(arn_instance.region,    "us-east-2")
        self.assertEqual(arn_instance.account,   "123456789012")
        self.assertEqual(arn_instance.resource,  "aabbccddee/stage-name/GET/pets")

        self.assertEqual(str(arn_instance), arn_string)
