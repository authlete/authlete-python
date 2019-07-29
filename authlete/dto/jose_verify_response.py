#
# Copyright (C) 2019 Authlete, Inc.
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


from authlete.dto.api_response import ApiResponse


class JoseVerifyResponse(ApiResponse):
    def __init__(self, nameAndValues=None):
        nameAndTypes = {
            'valid':             bool,
            'signatureValid':    bool,
            'missingClaims':     str,  # list of str
            'invalidClaims':     str,  # list of str
            'errorDescriptions': str   # list of str
        }

        super().__init__(nameAndValues, nameAndTypes)
