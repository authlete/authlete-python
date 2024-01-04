#
# Copyright (C) 2024 Authlete, Inc.
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


class FapiMode(Enum):
    FAPI1_BASELINE                          = 'fapi1_baseline'
    FAPI1_ADVANCED                          = 'fapi1_advanced'
    FAPI2_SECURITY                          = 'fapi2_security'
    FAPI2_MESSAGE_SIGNING_AUTH_REQ          = 'fapi2_message_signing_auth_req'
    FAPI2_MESSAGE_SIGNING_AUTH_RES          = 'fapi2_message_signing_auth_res'
    FAPI2_MESSAGE_SIGNING_INTROSPECTION_RES = 'fapi2_message_signing_introspection_res'
