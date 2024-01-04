#
# Copyright (C) 2019-2024 Authlete, Inc.
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


from os import getenv
from authlete.conf.authlete_configuration import AuthleteConfiguration


class AuthleteEnvConfiguration(AuthleteConfiguration):
    def __init__(self):
        nameAndValues = {
            'apiVersion':              getenv('AUTHLETE_API_VERSION'),
            'baseUrl':                 getenv('AUTHLETE_BASE_URL'),
            'serviceOwnerApiKey':      getenv('AUTHLETE_SERVICEOWNER_APIKEY'),
            'serviceOwnerApiSecret':   getenv('AUTHLETE_SERVICEOWNER_APISECRET'),
            'serviceOwnerAccessToken': getenv('AUTHLETE_SERVICEOWNER_ACCESSTOKEN'),
            'serviceApiKey':           getenv('AUTHLETE_SERVICE_APIKEY'),
            'serviceApiSecret':        getenv('AUTHLETE_SERVICE_APISECRET'),
            'serviceAccessToken':      getenv('AUTHLETE_SERVICE_ACCESSTOKEN'),
            'dpopKey':                 getenv('AUTHLETE_DPOP_KEY'),
            'clientCertificate':       getenv('AUTHLETE_CLIENT_CERTIFICATE')
        }

        super().__init__(nameAndValues)
