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


from authlete.types.jsonable import Jsonable
from authlete.types.jwe_alg  import JWEAlg;
from authlete.types.jwe_enc  import JWEEnc;


class CredentialIssuerMetadata(Jsonable):
    def __init__(self, nameAndValues={}):
        nameAndTypes = {
            'credentialIssuer':                               str,
            'authorizationServers':                           str,     # list of str
            'credentialEndpoint':                             str,
            'batchCredentialEndpoint':                        str,
            'deferredCredentialEndpoint':                     str,
            'credentialResponseEncryptionAlgValuesSupported': JWEAlg,  # list of JWEAlg
            'credentialResponseEncryptionEncValuesSupported': JWEEnc,  # list of JWEEnc
            'requireCredentialResponseEncryption':            bool,
            'credentialsSupported':                           str
        }

        super().__init__(nameAndValues, nameAndTypes)
