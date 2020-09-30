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


from authlete.dto.api_response                      import ApiResponse
from authlete.dto.backchannel_authentication_action import BackchannelAuthenticationAction
from authlete.dto.scope                             import Scope
from authlete.types.delivery_mode                   import DeliveryMode
from authlete.types.user_identification_hint_type   import UserIdentificationHintType


class BackchannelAuthenticationResponse(ApiResponse):
    def __init__(self, nameAndValues=None):
        nameAndTypes = {
            'action':                  BackchannelAuthenticationAction,
            'responseContent':         str,
            'clientId':                int,
            'clientIdAlias':           str,
            'clientIdAliasUsed':       bool,
            'clientName':              str,
            'deliveryMode':            DeliveryMode,
            'scopes':                  Scope,         # list of Scope
            'claimNames':              str,           # list of str
            'clientNotificationToken': str,
            'acrs':                    str,           # list of str
            'hintType':                UserIdentificationHintType,
            'hint':                    str,
            'sub':                     str,
            'bindingMessage':          str,
            'userCode':                str,
            'userCodeRequired':        bool,
            'requestedExpiry':         int,
            'requestContext':          str,
            'resources':               str,           # list of str
            'warnings':                str,           # list of str
            'ticket':                  str
        }

        super().__init__(nameAndValues, nameAndTypes)
