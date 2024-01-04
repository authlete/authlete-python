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


from authlete.dto.api_response         import ApiResponse
from authlete.dto.authz_details        import AuthzDetails
from authlete.dto.grant                import Grant
from authlete.dto.introspection_action import IntrospectionAction
from authlete.dto.pair                 import Pair
from authlete.dto.property             import Property
from authlete.types.grant_type         import GrantType


class IntrospectionResponse(ApiResponse):
    def __init__(self, nameAndValues=None):
        nameAndTypes = {
            'action':                IntrospectionAction,
            'clientId':              int,
            'subject':               str,
            'scopes':                str,           # list of str
            'existent':              bool,
            'usable':                bool,
            'sufficient':            bool,
            'refreshable':           bool,
            'responseContent':       str,
            'expiresAt':             int,
            'properties':            Property,      # list of Property
            'clientIdAlias':         str,
            'clientIdAliasUsed':     bool,
            'clientEntityId':        str,
            'clientEntityIdUsed':    bool,
            'certificateThumbprint': str,
            'resources':             str,           # list of str
            'accessTokenResources':  str,           # list of str
            'authorizationDetails':  AuthzDetails,
            'grantId':               str,
            'grant':                 Grant,
            'consentedClaims':       str,           # list of str
            'serviceAttributes':     Pair,          # list of Pair
            'clientAttributes':      Pair,          # list of Pair
            'forExternalAttachment': bool,
            'acr':                   str,
            'authTime':              int,
            'grantType':             GrantType,
            'forCredentialIssuance': bool,
            'cnonce':                str,
            'cnonceExpiresAt':       int,
            'issuableCredentials':   str,
            'dpopNonce':             str
        }

        super().__init__(nameAndValues, nameAndTypes)
