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


from authlete.dto.client_extension     import ClientExtension
from authlete.dto.tagged_value         import TaggedValue
from authlete.types.application_type   import ApplicationType
from authlete.types.client_auth_method import ClientAuthMethod
from authlete.types.client_type        import ClientType
from authlete.types.delivery_mode      import DeliveryMode
from authlete.types.grant_type         import GrantType
from authlete.types.jsonable           import Jsonable
from authlete.types.response_type      import ResponseType
from authlete.types.subject_type       import SubjectType
from authlete.types.jwe_alg            import JWEAlg
from authlete.types.jwe_enc            import JWEEnc
from authlete.types.jws_alg            import JWSAlg


class Client(Jsonable):
    def __init__(self, nameAndValues=None):
        nameAndTypes = {
            'developer':                             str,
            'clientId':                              int,
            'clientIdAlias':                         str,
            'clientIdAliasEnabled':                  bool,
            'clientSecret':                          str,
            'clientType':                            ClientType,
            'redirectUris':                          str,              # list of str
            'responseTypes':                         ResponseType,     # list of ResponseType
            'grantTypes':                            GrantType,        # list of GrantType
            'applicationType':                       ApplicationType,
            'contacts':                              str,              # list of str
            'clientName':                            str,
            'clientNames':                           TaggedValue,      # list of TaggedValue
            'logoUri':                               str,
            'logoUris':                              TaggedValue,      # list of TaggedValue
            'clientUri':                             str,
            'clientUris':                            TaggedValue,      # list of TaggedValue
            'policyUri':                             str,
            'policyUris':                            TaggedValue,      # list of TaggedValue
            'tosUri':                                str,
            'tosUris':                               TaggedValue,      # list of TaggedValue
            'jwksUri':                               str,
            'jwks':                                  str,
            'derivedSectorIdentifier':               str,
            'sectorIdentifierUri':                   str,
            'subjectType':                           SubjectType,
            'idTokenSignAlg':                        JWSAlg,
            'idTokenEncryptionAlg':                  JWEAlg,
            'idTokenEncryptionEnc':                  JWEEnc,
            'userInfoSignAlg':                       JWSAlg,
            'userInfoEncryptionAlg':                 JWEAlg,
            'userInfoEncryptionEnc':                 JWEEnc,
            'requestSignAlg':                        JWSAlg,
            'requestEncryptionAlg':                  JWEAlg,
            'requestEncryptionEnc':                  JWEEnc,
            'tokenAuthMethod':                       ClientAuthMethod,
            'tokenAuthSignAlg':                      JWSAlg,
            'defaultMaxAge':                         int,
            'defaultAcrs':                           str,              # list of str
            'authTimeRequired':                      bool,
            'loginUri':                              str,
            'requestUris':                           str,              # list of str
            'description':                           str,
            'descriptions':                          TaggedValue,      # list of TaggedValue
            'createdAt':                             int,
            'modifiedAt':                            int,
            'extension':                             ClientExtension,
            'tlsClientAuthSubjectDn':                str,
            'tlsClientAuthSanDns':                   str,
            'tlsClientAuthSanUri':                   str,
            'tlsClientAuthSanIp':                    str,
            'tlsClientAuthSanEmail':                 str,
            'tlsClientCertificateBoundAccessTokens': bool,
            'selfSignedCertificateKeyId':            str,
            'softwareId':                            str,
            'softwareVersion':                       str,
            'authorizationSignAlg':                  JWSAlg,
            'authorizationEncryptionAlg':            JWEAlg,
            'authorizationEncryptionEnc':            JWEEnc,
            'bcDeliveryMode':                        DeliveryMode,
            'bcNotificationEndpoint':                str,
            'bcRequestSignAlg':                      JWSAlg,
            'bcUserCodeRequired':                    bool,
            'dynamicallyRegistered':                 bool,
            'registrationAccessTokenHash':           str,
            'authorizationDataTypes':                str,              # list of str
            'parRequired':                           bool,
            'requestObjectRequired':                 bool,
        }

        super().__init__(nameAndValues, nameAndTypes)
