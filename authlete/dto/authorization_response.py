#
# Copyright (C) 2019-2020 Authlete, Inc.
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


from authlete.dto.api_response         import ApiResponse
from authlete.dto.authorization_action import AuthorizationAction
from authlete.dto.client               import Client
from authlete.dto.scope                import Scope
from authlete.dto.service              import Service
from authlete.types.display            import Display
from authlete.types.prompt             import Prompt


class AuthorizationResponse(ApiResponse):
    def __init__(self, nameAndValues=None):
        nameAndTypes = {
            'action':               AuthorizationAction,
            'service':              Service,
            'client':               Client,
            'display':              Display,
            'maxAge':               int,
            'scopes':               Scope,  # list of Scope
            'uiLocales':            str,    # list of str
            'claimsLocales':        str,    # list of str
            'claims':               str,    # list of str
            'acrEssential':         bool,
            'clientIdAliasUsed':    bool,
            'acrs':                 str,    # list of str
            'subject':              str,
            'loginHint':            str,
            'prompts':              Prompt, # list of Prompt
            'requestObjectPayload': str,
            'idTokenClaims':        str,
            'userInfoClaims':       str,
            'resources':            str,    # list of str
            'purpose':              str,
            'responseContent':      str,
            'ticket':               str
        }

        super().__init__(nameAndValues, nameAndTypes)
