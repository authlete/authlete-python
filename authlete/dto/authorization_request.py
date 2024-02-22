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

import urllib

from authlete.types.jsonable import Jsonable


class AuthorizationRequest(Jsonable):
    def __init__(self, nameAndValues: dict = {}, parameters: dict = {}, **kwargs) -> None:
        """
        Initializes a new instance of the AuthorizationRequest class.

        Args:
            nameAndValues (dict): A dictionary of name and values for initialization.
            parameters (dict): A dictionary of parameters for the request.
            **kwargs: Additional keyword arguments with single parameters.
        """
        nameAndTypes = {
            'parameters': str,
            'context':    str
        }

        nameAndValues['context'] = kwargs.pop(
            'context', 
            nameAndValues.get('context', None)
        )

        parameters.update(kwargs)
        nameAndValues['parameters'] = urllib.parse.urlencode(parameters)
        
        super().__init__(nameAndValues, nameAndTypes)
