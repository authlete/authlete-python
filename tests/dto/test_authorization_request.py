#
# Copyright (C) 2024 Authlete, Inc.
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

import urllib
from authlete.dto.authorization_request import AuthorizationRequest
from authlete.dto.property import Property



class TestAuthorizationRequest(unittest.TestCase):

    def test_from_parameters(self):

        prmtrs :dict = {
            "response_type": "code",
            "client_id": "heyboy!"
        }

        prmtrs_enc = urllib.parse.urlencode(prmtrs)

        req1 = AuthorizationRequest(**prmtrs)
        self.assertEqual(req1.parameters, prmtrs_enc)    

        req2 = AuthorizationRequest(parameters = prmtrs)
        self.assertEqual(req2.parameters, prmtrs_enc)