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


from authlete.dto.named_uri            import NamedUri
from authlete.dto.pair                 import Pair
from authlete.dto.scope                import Scope
from authlete.dto.sns_credentials      import SnsCredentials
from authlete.types.claim_type         import ClaimType
from authlete.types.client_auth_method import ClientAuthMethod
from authlete.types.delivery_mode      import DeliveryMode
from authlete.types.display            import Display
from authlete.types.grant_type         import GrantType
from authlete.types.jsonable           import Jsonable
from authlete.types.jwe_alg            import JWEAlg
from authlete.types.jwe_enc            import JWEEnc
from authlete.types.jws_alg            import JWSAlg
from authlete.types.response_type      import ResponseType
from authlete.types.service_profile    import ServiceProfile
from authlete.types.sns                import Sns
from authlete.types.user_code_charset  import UserCodeCharset


class Service(Jsonable):
    def __init__(self, nameAndValues=None):
        nameAndTypes = {
            'serviceName':                              str,
            'apiKey':                                   int,
            'apiSecret':                                str,
            'issuer':                                   str,
            'authorizationEndpoint':                    str,
            'tokenEndpoint':                            str,
            'revocationEndpoint':                       str,
            'supportedRevocationAuthMethods':           ClientAuthMethod,  # list of ClientAuthMethod
            'userInfoEndpoint':                         str,
            'jwksUri':                                  str,
            'jwks':                                     str,
            'registrationEndpoint':                     str,
            'registrationManagementEndpoint':           str,
            'supportedScopes':                          Scope,             # list of Scope
            'supportedResponseTypes':                   ResponseType,      # list of ResponseType
            'supportedGrantTypes':                      GrantType,         # list of GrantType
            'supportedAcrs':                            str,               # list of str
            'supportedTokenAuthMethods':                ClientAuthMethod,  # list of ClientAuthMethod
            'supportedDisplays':                        Display,           # list of Display
            'supportedClaimTypes':                      ClaimType,         # list of ClaimType
            'supportedClaims':                          str,               # list of str
            'serviceDocumentation':                     str,
            'supportedClaimLocales':                    str,               # list of str
            'supportedUiLocales':                       str,               # list of str
            'policyUri':                                str,
            'tosUri':                                   str,
            'authenticationCallbackEndpoint':           str,
            'authenticationCallbackApiKey':             str,
            'authenticationCallbackApiSecret':          str,
            'supportedSnses':                           Sns,               # list of Sns
            'snsCredentials':                           SnsCredentials,    # list of SnsCredentials
            'createdAt':                                int,
            'modifiedAt':                               int,
            'developerAuthenticationCallbackEndpoint':  str,
            'developerAuthenticationCallbackApiKey':    str,
            'developerAuthenticationCallbackApiSecret': str,
            'supportedDeveloperSnses':                  Sns,               # list of Sns
            'developerSnsCredentials':                  SnsCredentials,    # list of SnsCredentials
            'clientsPerDeveloper':                      int,
            'directAuthorizationEndpointEnabled':       bool,
            'directTokenEndpointEnabled':               bool,
            'directRevocationEndpointEnabled':          bool,
            'directUserInfoEndpointEnabled':            bool,
            'directJwksEndpointEnabled':                bool,
            'directIntrospectionEndpointEnabled':       bool,
            'singleAccessTokenPerSubject':              bool,
            'pkceRequire':                              bool,
            'pkceS256Required':                         bool,
            'refreshTokenKept':                         bool,
            'refreshTokenDurationKept':                 bool,
            'errorDescriptionOmitted':                  bool,
            'errorUriOmitted':                          bool,
            'clientIdAliasEnabled':                     bool,
            'supportedServiceProfiles':                 ServiceProfile,    # list of ServiceProfile
            'tlsClientCertificateBoundAccessTokens':    bool,
            'introspectionEndpoint':                    str,
            'supportedIntrospectionAuthMethods':        ClientAuthMethod,  # list of ClientAuthMethod
            'mutualTlsValiddatePkiCertChain':           bool,
            'trustedRootCertificates':                  str,               # list of str
            'dynamicRegistrationSupported':             bool,
            'endSessionEndpoint':                       str,
            'description':                              str,
            'accessTokenType':                          str,
            'accessTokenSignAlg':                       JWSAlg,
            'accessTokenDuration':                      int,
            'refreshTokenDuration':                     int,
            'idTokenDuration':                          int,
            'authorizationResponseDuration':            int,
            'pushedAuthReqDuration':                    int,
            'metadata':                                 Pair,              # list of Pair
            'accessTokenSignatureKeyId':                str,
            'authorizationSignatureKeyId':              str,
            'idTokenSignatureKeyId':                    str,
            'userInfoSignatureKeyId':                   str,
            'supportedBackchannelTokenDeliveryModes':   DeliveryMode,      # list of DeliveryMode
            'backchannelAuthenticationEndpoint':        str,
            'backchannelUserCodeParameterSupported':    bool,
            'backchannelAuthReqIdDuration':             int,
            'backchannelPollingInterval':               int,
            'backchannelBindingMessageRequiredInFapi':  bool,
            'allowableClockSkew':                       int,
            'deviceAuthorizationEndpoint':              str,
            'deviceVerificationUri':                    str,
            'deviceVerificationUriComplete':            str,
            'deviceFlowCodeDuration':                   int,
            'deviceFlowPollingInterval':                int,
            'userCodeCharset':                          UserCodeCharset,
            'userCodeLength':                           int,
            'pushedAuthReqEndpoint':                    str,
            'mtlsEndpointAliases':                      NamedUri,          # list of NamedUri
            'supportedAuthorizationDataTypes':          str,               # list of str
            'supportedTrustFrameworks':                 str,               # list of str
            'supportedEvidence':                        str,               # list of str
            'supportedIdentityDocuments':               str,               # list of str
            'supportedVerificationMethods':             str,               # list of str
            'supportedVerifiedClaims':                  str,               # list of str
            'missingClientIdAllowed':                   bool,
            'parRequired':                              bool,
            'requestObjectRequired':                    bool,
            'traditionalRequestObjectProcessingApplied':bool,
        }

        super().__init__(nameAndValues, nameAndTypes)
