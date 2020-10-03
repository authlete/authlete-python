#
# Copyright (C) 2020 Authlete, Inc.
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


class ARN(Jsonable):
    def __init__(self, nameAndValues=None):
        nameAndTypes = {
            'partition': str,
            'service':   str,
            'region':    str,
            'account':   str,
            'resource':  str,
        }

        super().__init__(nameAndValues, nameAndTypes)


    def __str__(self):
        return ':'.join(['arn', self.partition, self.service, self.region, self.account, self.resource])


    @classmethod
    def parse(cls, arn):
        """Creates an instance of this class from an ARN string."""

        # Amazon Resource Names (ARNs)
        # https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html
        #
        #   Format
        #      arn:partition:service:region:account-id:resource-id
        #      arn:partition:service:region:account-id:resource-type/resource-id
        #      arn:partition:service:region:account-id:resource-type:resource-id
        #
        elements = arn.split(':', 5)
        nameAndValues = {
            'partition': elements[1],
            'service':   elements[2],
            'region':    elements[3],
            'account':   elements[4],
            'resource':  elements[5],
        }

        return cls(nameAndValues)
