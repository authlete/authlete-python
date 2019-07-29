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


from authlete.types.jsonable import Jsonable


class Address(Jsonable):
    def __init__(self, nameAndValues=None):
        nameAndTypes = {
            'formatted':      str,
            'street_address': str,
            'locality':       str,
            'region':         str,
            'postal_code':    str,
            'country':        str
        }

        super().__init__(nameAndValues, nameAndTypes)


    @property
    def streetAddress(self):
        return self.street_address


    @streetAddress.setter
    def streetAddress(self, value):
        self.street_address = value


    @property
    def postalCode(self):
        return self.postal_code


    @postalCode.setter
    def postalCode(self, value):
        self.postal_code = value
