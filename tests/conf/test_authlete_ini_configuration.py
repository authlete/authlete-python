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


import unittest
from authlete.conf.authlete_ini_configuration import AuthleteIniConfiguration


class TestAuthleteIniConfiguration(unittest.TestCase):
    def test_1(self):
        cnf = AuthleteIniConfiguration("tests/conf/authlete.ini")

        self.assertEqual(cnf.baseUrl,                 "B")
        self.assertEqual(cnf.serviceOwnerApiKey,      "SO_K")
        self.assertEqual(cnf.serviceOwnerApiSecret,   "SO_S")
        self.assertEqual(cnf.serviceOwnerAccessToken, "SO_T")
        self.assertEqual(cnf.serviceApiKey,           "S_K")
        self.assertEqual(cnf.serviceApiSecret,        "S_S")
        self.assertEqual(cnf.serviceAccessToken,      "S_T")
