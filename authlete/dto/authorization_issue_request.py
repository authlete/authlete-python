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


from authlete.dto.authz_details import AuthzDetails
from authlete.dto.property      import Property
from authlete.types.jsonable    import Jsonable


class AuthorizationIssueRequest(Jsonable):
    def __init__(self, nameAndValues={}):
        nameAndTypes = {
            'ticket':               str,
            'subject':              str,
            'sub':                  str,
            'authTime':             int,
            'acr':                  str,
            'claims':               str,
            'properties':           Property,      # list of Property
            'scopes':               str,           # list of str
            'idtHeaderParams':      str,
            'authorizationDetails': AuthzDetails,
            'consentedClaims':      str,           # list of str
            'claimsForTx':          str,
            'verifiedClaimsForTx':  str,           # list of str
            'jwtAtClaims':          str,
            'accessToken':          str,
            'idTokenAudType':       str,
            'accessTokenDuration':  int
        }

        super().__init__(nameAndValues, nameAndTypes)
