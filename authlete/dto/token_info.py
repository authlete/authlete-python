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


from authlete.dto.authz_details import AuthzDetails
from authlete.dto.property      import Property
from authlete.dto.scope         import Scope
from authlete.types.jsonable    import Jsonable


class TokenInfo(Jsonable):
    def __init__(self, nameAndValues: dict = {}):
        """
        Args:
            nameAndValues (dict): A dictionary of name and values for initialization.
        """
        nameAndTypes = {
            'clientId':             int,
            'subject':              str,
            'scopes':               Scope,        # list of Scope
            'expiresAt':            int,
            'properties':           Property,     # list of Property
            'clientIdAlias':        str,
            'clientIdAliasUsed':    bool,
            'clientEntityId':       str,
            'clientEntityIdUsed':   bool,
            'resources':            str,          # list of str
            'authorizationDetails': AuthzDetails
        }

        super().__init__(nameAndValues, nameAndTypes)
