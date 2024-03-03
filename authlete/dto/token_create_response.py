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


from authlete.dto.api_response        import ApiResponse
from authlete.dto.authz_details       import AuthzDetails
from authlete.dto.property            import Property
from authlete.dto.token_create_action import TokenCreateAction
from authlete.types.grant_type        import GrantType


class TokenCreateResponse(ApiResponse):
    def __init__(self, nameAndValues: dict = {}):
        """
        Args:
            nameAndValues (dict): A dictionary of name and values for initialization.
        """
        nameAndTypes = {
            'action':                TokenCreateAction,
            'grantType':             GrantType,
            'clientId':              int,
            'subject':               str,
            'scopes':                str,                # list of str
            'accessToken':           str,
            'tokenType':             str,
            'expiresIn':             int,
            'expiresAt':             int,
            'refreshToken':          str,
            'properties':            Property,           # list of Property
            'jwtAccessToken':        str,
            'authorizationDetails':  AuthzDetails,
            'forExternalAttachment': bool,
            'tokenId':               str,
            'refreshTokenScopes':    str                 # list of str
        }

        super().__init__(nameAndValues, nameAndTypes)
