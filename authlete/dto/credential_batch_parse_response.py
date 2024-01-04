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


from authlete.dto.api_response                  import ApiResponse
from authlete.dto.credential_batch_parse_action import CredentialBatchParseAction
from authlete.dto.credential_request_info       import CredentialRequestInfo


class CredentialBatchParseResponse(ApiResponse):
    def __init__(self, nameAndValues=None):
        nameAndTypes = {
            'action':          CredentialBatchParseAction,
            'responseContent': str,
            'info':            CredentialRequestInfo        # list of CredentialRequestInfo
        }

        super().__init__(nameAndValues, nameAndTypes)