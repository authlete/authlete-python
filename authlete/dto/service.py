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


from authlete.dto.credential_issuer_metadata import CredentialIssuerMetadata
from authlete.dto.hsk                        import Hsk
from authlete.dto.named_uri                  import NamedUri
from authlete.dto.pair                       import Pair
from authlete.dto.scope                      import Scope
from authlete.dto.sns_credentials            import SnsCredentials
from authlete.dto.trust_anchor               import TrustAnchor
from authlete.types.attachment_type          import AttachmentType
from authlete.types.claim_type               import ClaimType
from authlete.types.client_auth_method       import ClientAuthMethod
from authlete.types.client_registration_type import ClientRegistrationType
from authlete.types.delivery_mode            import DeliveryMode
from authlete.types.display                  import Display
from authlete.types.fapi_mode                import FapiMode
from authlete.types.grant_type               import GrantType
from authlete.types.jsonable                 import Jsonable
from authlete.types.jws_alg                  import JWSAlg
from authlete.types.prompt                   import Prompt
from authlete.types.response_type            import ResponseType
from authlete.types.service_profile          import ServiceProfile
from authlete.types.sns                      import Sns
from authlete.types.user_code_charset        import UserCodeCharset


class Service(Jsonable):
    def __init__(self, nameAndValues=None):
        nameAndTypes = {
            'serviceName':                                 str,
            'apiKey':                                      int,
            'apiSecret':                                   str,
            'issuer':                                      str,
            'authorizationEndpoint':                       str,
            'tokenEndpoint':                               str,
            'revocationEndpoint':                          str,
            'supportedRevocationAuthMethods':              ClientAuthMethod,          # list of ClientAuthMethod
            'userInfoEndpoint':                            str,
            'jwksUri':                                     str,
            'jwks':                                        str,
            'registrationEndpoint':                        str,
            'registrationManagementEndpoint':              str,
            'supportedScopes':                             Scope,                     # list of Scope
            'supportedResponseTypes':                      ResponseType,              # list of ResponseType
            'supportedGrantTypes':                         GrantType,                 # list of GrantType
            'supportedAcrs':                               str,                       # list of str
            'supportedTokenAuthMethods':                   ClientAuthMethod,          # list of ClientAuthMethod
            'supportedDisplays':                           Display,                   # list of Display
            'supportedClaimTypes':                         ClaimType,                 # list of ClaimType
            'supportedClaims':                             str,                       # list of str
            'serviceDocumentation':                        str,
            'supportedClaimLocales':                       str,                       # list of str
            'supportedUiLocales':                          str,                       # list of str
            'policyUri':                                   str,
            'tosUri':                                      str,
            'authenticationCallbackEndpoint':              str,
            'authenticationCallbackApiKey':                str,
            'authenticationCallbackApiSecret':             str,
            'supportedSnses':                              Sns,                       # list of Sns
            'snsCredentials':                              SnsCredentials,            # list of SnsCredentials
            'createdAt':                                   int,
            'modifiedAt':                                  int,
            'developerAuthenticationCallbackEndpoint':     str,
            'developerAuthenticationCallbackApiKey':       str,
            'developerAuthenticationCallbackApiSecret':    str,
            'supportedDeveloperSnses':                     Sns,                       # list of Sns
            'developerSnsCredentials':                     SnsCredentials,            # list of SnsCredentials
            'clientsPerDeveloper':                         int,
            'directAuthorizationEndpointEnabled':          bool,
            'directTokenEndpointEnabled':                  bool,
            'directRevocationEndpointEnabled':             bool,
            'directUserInfoEndpointEnabled':               bool,
            'directJwksEndpointEnabled':                   bool,
            'directIntrospectionEndpointEnabled':          bool,
            'singleAccessTokenPerSubject':                 bool,
            'pkceRequired':                                bool,
            'pkceS256Required':                            bool,
            'refreshTokenKept':                            bool,
            'refreshTokenDurationKept':                    bool,
            'refreshTokenDurationReset':                   bool,
            'errorDescriptionOmitted':                     bool,
            'errorUriOmitted':                             bool,
            'clientIdAliasEnabled':                        bool,
            'supportedServiceProfiles':                    ServiceProfile,            # list of ServiceProfile
            'tlsClientCertificateBoundAccessTokens':       bool,
            'introspectionEndpoint':                       str,
            'supportedIntrospectionAuthMethods':           ClientAuthMethod,          # list of ClientAuthMethod
            'mutualTlsValidatePkiCertChain':               bool,
            'trustedRootCertificates':                     str,                       # list of str
            'dynamicRegistrationSupported':                bool,
            'endSessionEndpoint':                          str,
            'description':                                 str,
            'accessTokenType':                             str,
            'accessTokenSignAlg':                          JWSAlg,
            'accessTokenDuration':                         int,
            'refreshTokenDuration':                        int,
            'idTokenDuration':                             int,
            'authorizationResponseDuration':               int,
            'pushedAuthReqDuration':                       int,
            'metadata':                                    Pair,                      # list of Pair
            'accessTokenSignatureKeyId':                   str,
            'authorizationSignatureKeyId':                 str,
            'idTokenSignatureKeyId':                       str,
            'userInfoSignatureKeyId':                      str,
            'supportedBackchannelTokenDeliveryModes':      DeliveryMode,              # list of DeliveryMode
            'backchannelAuthenticationEndpoint':           str,
            'backchannelUserCodeParameterSupported':       bool,
            'backchannelAuthReqIdDuration':                int,
            'backchannelPollingInterval':                  int,
            'backchannelBindingMessageRequiredInFapi':     bool,
            'allowableClockSkew':                          int,
            'deviceAuthorizationEndpoint':                 str,
            'deviceVerificationUri':                       str,
            'deviceVerificationUriComplete':               str,
            'deviceFlowCodeDuration':                      int,
            'deviceFlowPollingInterval':                   int,
            'userCodeCharset':                             UserCodeCharset,
            'userCodeLength':                              int,
            'pushedAuthReqEndpoint':                       str,
            'mtlsEndpointAliases':                         NamedUri,                  # list of NamedUri
            'supportedAuthorizationDetailsTypes':          str,                       # list of str
            'supportedTrustFrameworks':                    str,                       # list of str
            'supportedEvidence':                           str,                       # list of str
            'supportedIdentityDocuments':                  str,                       # list of str
            'supportedDocuments':                          str,                       # list of str
            'supportedVerificationMethods':                str,                       # list of str
            'supportedDocumentsMethods':                   str,                       # list of str
            'supportedDocumentsCheckMethods':              str,                       # list of str
            'supportedElectronicRecords':                  str,                       # list of str
            'supportedVerifiedClaims':                     str,                       # list of str
            'supportedAttachments':                        AttachmentType,            # list of AttachmentType
            'supportedDigestAlgorithms':                   str,                       # list of str
            'missingClientIdAllowed':                      bool,
            'parRequired':                                 bool,
            'requestObjectRequired':                       bool,
            'traditionalRequestObjectProcessingApplied':   bool,
            'claimShortcutRestrictive':                    bool,
            'scopeRequired':                               bool,
            'nbfOptional':                                 bool,
            'issSuppressed':                               bool,
            'attributes':                                  Pair,                      # list of Pair
            'supportedCustomClientMetadata':               str,                       # list of str
            'tokenExpirationLinked':                       bool,
            'frontChannelRequestObjectEncryptionRequired': bool,
            'requestObjectEncryptionAlgMatchRequired':     bool,
            'requestObjectEncryptionEncMatchRequired':     bool,
            'hsmEnabled':                                  bool,
            'hsks':                                        Hsk,                       # list of Hsk
            'grantManagementEndpoint':                     str,
            'grantManagementActionRequired':               bool,
            'unauthorizedOnClientConfigSupported':         bool,
            'dcrScopeUsedAsRequestable':                   bool,
            'predefinedTransformedClaims':                 str,
            'loopbackRedirectionUriVariable':              bool,
            'requestObjectAudienceChecked':                bool,
            'accessTokenForExternalAttachmentEmbedded':    bool,
            'refreshTokenIdempotent':                      bool,
            'federationEnabled':                           bool,
            'organizationName':                            str,
            'authorityHints':                              str,                       # list of str
            'trustAnchors':                                TrustAnchor,               # list of TrustAnchor
            'federationJwks':                              str,
            'federationSignatureKeyId':                    str,
            'federationConfigurationDuration':             int,
            'signedJwksUri':                               str,
            'federationRegistrationEndpoint':              str,
            'supportedClientRegistrationTypes':            ClientRegistrationType,    # list of ClientRegistrationType
            'tokenExchangeByIdentifiableClientsOnly':      bool,
            'tokenExchangeByConfidentialClientsOnly':      bool,
            'tokenExchangeByPermittedClientsOnly':         bool,
            'tokenExchangeEncryptedJwtRejected':           bool,
            'tokenExchangeUnsignedJwtRejected':            bool,
            'jwtGrantByIdentifiableClientsOnly':           bool,
            'jwtGrantEncryptedJwtRejected':                bool,
            'jwtGrantUnsignedJwtRejected':                 bool,
            'dcrDuplicateSoftwareIdBlocked':               bool,
            'resourceSignatureKeyId':                      str,
            'rsResponseSigned':                            bool,
            'openidDroppedOnRefreshWithoutOfflineAccess':  bool,
            'verifiableCredentialsEnabled':                bool,
            'credentialIssuerMetadata':                    CredentialIssuerMetadata,
            'credentialOfferDuration':                     int,
            'idTokenAudType':                              str,
            'supportedPromptValues':                       Prompt,                    # list of Prompt
            'verifiedClaimsValidationSchemaSet':           str,
            'preAuthorizedGrantAnonymousAccessSupported':  bool,
            'cnonceDuration':                              int,
            'credentialTransactionDuration':               int,
            'credentialDuration':                          int,
            'credentialJwks':                              str,
            'credentialJwksUri':                           str,
            'idTokenReissuable':                           bool,
            'introspectionSignatureKeyId':                 str,
            'fapiModes':                                   FapiMode,                  # list of FapiMode
            'dpopNonceRequired':                           bool,
            'dpopNonceDuration':                           int
        }

        super().__init__(nameAndValues, nameAndTypes)
