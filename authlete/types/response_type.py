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


from enum import Enum


class ResponseType(Enum):
    NONE                = 'none'
    CODE                = 'code'
    TOKEN               = 'token'
    ID_TOKEN            = 'id_token'
    CODE_TOKEN          = 'code token'
    CODE_ID_TOKEN       = 'code id_token'
    ID_TOKEN_TOKEN      = 'id_token token'
    CODE_ID_TOKEN_TOKEN = 'code id_token token'
