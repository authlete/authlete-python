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


from authlete.dto.api_response    import ApiResponse
from authlete.dto.pair            import Pair
from authlete.dto.property        import Property
from authlete.dto.string_array    import StringArray
from authlete.dto.userinfo_action import UserInfoAction


class UserInfoResponse(ApiResponse):
    def __init__(self, nameAndValues=None):
        nameAndTypes = {
            'action':                       UserInfoAction,
            'clientId':                     int,
            'subject':                      str,
            'scopes':                       str,          # list of str
            'claims':                       str,          # list of str
            'token':                        str,
            'responseContent':              str,
            'properties':                   Property,     # list of Property
            'clientIdAlias':                str,
            'clientIdAliasUsed':            bool,
            'clientEntityId':               str,
            'clientEntityIdUsed':           bool,
            'userInfoClaims':               str,
            'transformedClaims':            str,
            'consentedClaims':              str,          # list of str
            'requestedClaimsForTx':         str,          # list of str
            'requestedVerifiedClaimsForTx': StringArray,  # list of StringArray
            'serviceAttributes':            Pair,         # list of Pair
            'clientAttributes':             Pair,         # list of Pair
            'dpopNonce':                    str
        }

        super().__init__(nameAndValues, nameAndTypes)
