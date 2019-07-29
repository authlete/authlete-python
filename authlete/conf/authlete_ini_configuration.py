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


from configparser import ConfigParser
from authlete.conf.authlete_configuration import AuthleteConfiguration


class AuthleteIniConfiguration(AuthleteConfiguration):
    def __init__(self, file="authlete.ini"):
        ini = ConfigParser()
        ini.read(file)

        if ini.has_section('authlete'):
            section = ini['authlete']
        else:
            section = ini.defaults()

        nameAndValues = {
            'baseUrl':                 section.get('base_url'),
            'serviceOwnerApiKey':      section.get('service_owner.api_key'),
            'serviceOwnerApiSecret':   section.get('service_owner.api_secret'),
            'serviceOwnerAccessToken': section.get('service_owner.access_token'),
            'serviceApiKey':           section.get('service.api_key'),
            'serviceApiSecret':        section.get('service.api_secret'),
            'serviceAccessToken':      section.get('service.access_token')
        }

        super().__init__(nameAndValues)
