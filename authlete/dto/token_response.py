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
from authlete.dto.pair                 import Pair
from authlete.dto.property             import Property
from authlete.dto.token_action         import TokenAction
from authlete.dto.token_info           import TokenInfo
from authlete.types.client_auth_method import ClientAuthMethod
from authlete.types.grant_type         import GrantType
from authlete.types.token_type         import TokenType


class TokenResponse(ApiResponse):
    def __init__(self, nameAndValues=None):
        nameAndTypes = {
            'action':                   TokenAction,
            'responseContent':          str,
            'username':                 str,
            'password':                 str,
            'ticket':                   str,
            'accessToken':              str,
            'accessTokenExpiresAt':     int,
            'accessTokenDuration':      int,
            'refreshToken':             str,
            'refreshTokenExpiresAt':    int,
            'refreshTokenDuration':     int,
            'idToken':                  str,
            'grantType':                GrantType,
            'clientId':                 int,
            'clientIdAlias':            str,
            'clientIdAliasUsed':        bool,
            'clientEntityId':           str,
            'clientEntityIdUsed':       bool,
            'subject':                  str,
            'scopes':                   str,               # list of str
            'properties':               Property,          # list of Property
            'jwtAccessToken':           str,
            'clientAuthMethod':         ClientAuthMethod,
            'resources':                str,               # list of str
            'accessTokenResources':     str,               # list of str
            'authorizationDetails':     AuthzDetails,
            'grantId':                  str,
            'serviceAttributes':        Pair,              # list of Pair
            'clientAttributes':         Pair,              # list of Pair
            'audiences':                str,               # list of str
            'requestedTokenType':       TokenType,
            'subjectToken':             str,
            'subjectTokenType':         TokenType,
            'subjectTokenInfo':         TokenInfo,
            'actorToken':               str,
            'actorTokenType':           TokenType,
            'actorTokenInfo':           TokenInfo,
            'assertion':                str,
            'previousRefreshTokenUsed': bool,
            'cnonce':                   str,
            'cnonceExpiresAt':          int,
            'cnonceDuration':           int,
            'requestedIdTokenClaims':   str,               # list of str
            'dpopNonce':                str,
            'refreshTokenScopes':       str                # list of str
        }

        super().__init__(nameAndValues, nameAndTypes)
