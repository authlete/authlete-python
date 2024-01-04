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


from enum import Enum


class GrantType(Enum):
    AUTHORIZATION_CODE  = 'authorization_code'
    IMPLICIT            = 'implicit'
    PASSWORD            = 'password'
    CLIENT_CREDENTIALS  = 'client_credentials'
    REFRESH_TOKEN       = 'refresh_token'
    CIBA                = 'urn:openid:params:grant-type:ciba'
    DEVICE_CODE         = 'urn:ietf:params:oauth:grant-type:device_code'
    TOKEN_EXCHANGE      = 'urn:ietf:params:oauth:grant-type:token-exchange'
    JWT_BEARER          = 'urn:ietf:params:oauth:grant-type:jwt-bearer'
    PRE_AUTHORIZED_CODE = 'urn:ietf:params:oauth:grant-type:pre-authorized_code'
