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


class EntityType(Enum):
    OPENID_RELYING_PARTY       = 'openid_relying_party'
    OPENID_PROVIDER            = 'openid_provider'
    OAUTH_AUTHORIZATION_SERVER = 'oauth_authorization_server'
    OAUTH_CLIENT               = 'oauth_client'
    OAUTH_RESOURCE             = 'oauth_resource'
    FEDERATION_ENTITY          = 'federation_entity'
    OPENID_CREDENTIAL_ISSUER   = 'openid_credential_issuer'
