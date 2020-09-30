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


from enum import Enum, auto


class AuthorizationFailReason(Enum):
    UNKNOWN                    = auto()
    NOT_LOGGED_IN              = auto()
    MAX_AGE_NOT_SUPPORTED      = auto()
    EXCEEDS_MAX_AGE            = auto()
    DIFFERENT_SUBJECT          = auto()
    ACR_NOT_SATISFIED          = auto()
    DENIED                     = auto()
    SERVER_ERROR               = auto()
    NOT_AUTHENTICATED          = auto()
    ACCOUNT_SELECTION_REQUIRED = auto()
    CONSENT_REQUIRED           = auto()
    INTERACTION_REQUIRED       = auto()
    INVALID_TARGET             = auto()
