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
from json import dumps, loads


class Jsonable(object):
    def __init__(self, nameAndValues=None, nameAndTypes=None):
        # If there is no attribute to add dynamically.
        if nameAndTypes is None:
            return

        # If no initial data set is given
        if nameAndValues is None:
            nameAndValues = {}

        # For each attribute to add dynamically.
        for attrName, attrType in nameAndTypes.items():
            # Get the value of the attribute from the initial data set.
            # The value may not be found.
            value = nameAndValues.get(attrName)

            # Convert the type of the value to a more specific one if possible.
            attrValue = self.__to_attr_value(value, attrType)

            # Add an attribute dynamically with the initial value.
            self.__dict__[attrName] = attrValue


    def __to_attr_value(self, value, attrType):
        if value is None:
            # Return the default value of the type.
            return self.__default_value(attrType)

        if isinstance(value, list):
            # Convert the type of each element by __to_attr_value().
            return list(map(lambda element: self.__to_attr_value(element, attrType), value))

        # If the type is Jsonable or its subclass.
        if issubclass(attrType, Jsonable):
            # Create a new instance by using the constructor of the type.
            return attrType(value)
        # If the type is Enum or its subclass.
        elif issubclass(attrType, Enum):
            if isinstance(value, attrType):
                return value
            else:
                # Find the enum entry whose name is 'value'.
                return attrType[value]
        else:
            # No conversion. For example, in case of attrType == str.
            return value


    def __default_value(self, attrType):
        if attrType == bool:
            return False
        elif attrType == int:
            return int(0)
        elif attrType == float:
            return float(0)
        else:
            return None


    def __setattr__(self, name, value):
        if hasattr(self, name):
            super().__setattr__(name, value)
        else:
            raise AttributeError(
                "'{}' object has no attribute '{}'".format(
                    type(self).__qualname__, name))


    def __str__(self):
        # JSON
        return self.to_json()


    def __repr__(self):
        # CLASSNAME(JSON)
        cls = type(self).__qualname__
        jsn = self.to_json(indent=2)
        return '{}({})'.format(cls, jsn)


    def __dumps(self, obj):
        if obj is None:
            return None
        elif isinstance(obj, list):
            return list(map(lambda element: self.__dumps(element), obj))
        elif isinstance(obj, Enum):
            return obj.name
        elif isinstance(obj, Jsonable):
            return vars(obj)
        else:
            return obj


    def to_json(self, indent=None):
        """Gets the JSON representation of this object."""
        return dumps(vars(self), indent=indent, default=self.__dumps)


    @classmethod
    def from_json(cls, json):
        """Creates an instance of this class from a JSON string."""
        return cls(loads(json))
