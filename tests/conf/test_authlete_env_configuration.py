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


import os
import unittest
from authlete.conf.authlete_env_configuration import AuthleteEnvConfiguration


class TestAuthleteEnvConfiguration(unittest.TestCase):
    def test_1(self):
        os.environ["AUTHLETE_BASE_URL"]                 = "B"
        os.environ["AUTHLETE_SERVICEOWNER_APIKEY"]      = "SO_K"
        os.environ["AUTHLETE_SERVICEOWNER_APISECRET"]   = "SO_S"
        os.environ["AUTHLETE_SERVICEOWNER_ACCESSTOKEN"] = "SO_T"
        os.environ["AUTHLETE_SERVICE_APIKEY"]           = "S_K"
        os.environ["AUTHLETE_SERVICE_APISECRET"]        = "S_S"
        os.environ["AUTHLETE_SERVICE_ACCESSTOKEN"]      = "S_T"

        cnf = AuthleteEnvConfiguration()

        self.assertEqual(cnf.baseUrl,                 "B")
        self.assertEqual(cnf.serviceOwnerApiKey,      "SO_K")
        self.assertEqual(cnf.serviceOwnerApiSecret,   "SO_S")
        self.assertEqual(cnf.serviceOwnerAccessToken, "SO_T")
        self.assertEqual(cnf.serviceApiKey,           "S_K")
        self.assertEqual(cnf.serviceApiSecret,        "S_S")
        self.assertEqual(cnf.serviceAccessToken,      "S_T")
