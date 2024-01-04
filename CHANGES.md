CHANGES
=======

1.3.0 (2024-01-04)
------------------

- `AccessToken` class
    * Added `refreshTokenScopes`.

- `AuthorizationIssueRequest` class
    * Added `authorizationDetails`.
    * Added `consentedClaims`.
    * Added `claimsForTx`.
    * Added `verifiedClaimsForTx`.
    * Added `jwtAtClaims`.
    * Added `accessToken`.
    * Added `idTokenAudType`.
    * Added `accessTokenDuration`.

- `AuthleteApi` class
    * Changed the `pretty=True` argument of the `getServiceConfiguration` method to `request=None`.
    * Added `tokenRevoke` method.
    * Added `hskCreate` method.
    * Added `hskDelete` method.
    * Added `hskGet` method.
    * Added `hskGetList` method.
    * Added `echo` method.
    * Added `gm` method.
    * Added `updateClientLockFlag` method.
    * Added `federationConfiguration` method.
    * Added `federationRegistration` method.
    * Added `credentialIssuerMetadata` method.
    * Added `credentialJwtIssuerMetadata` method.
    * Added `credentialIssuerJwks` method.
    * Added `credentialOfferCreate` method.
    * Added `credentialOfferInfo` method.
    * Added `credentialSingleParse` method.
    * Added `credentialSingleIssue` method.
    * Added `credentialBatchParse` method.
    * Added `credentialBatchIssue` method.
    * Added `credentialDeferredParse` method.
    * Added `credentialDeferredIssue` method.
    * Added `idTokenReissue` method.
    * Added `authorizationTicketInfo` method.
    * Added `authorizationTicketUpdate` method.

- `AuthleteApiImpl` class
    * Updated to support the Authlete API version 3.

- `AuthleteConfiguration` class
    * Added `apiVersion`.
    * Added `dpopKey`.
    * Added `clientCertificate`.

- `AuthleteEnvConfiguration` class
    * Added `apiVersion`.
    * Added `dpopKey`.
    * Added `clientCertificate`.

- `AuthleteIniConfiguration` class
    * Added `apiVersion`.
    * Added `dpopKey`.
    * Added `clientCertificate`.

- `AuthorizationIssueResponse` class
    * Added `ticketInfo`.

- `AuthorizationRequest` class
    * Added `context`.

- `AuthorizationResponse` class
    * Added `dynamicScopes`.
    * Added `claimsAtUserInfo`.
    * Added `clientEntityIdUsed`.
    * Added `transformedClaims`.
    * Added `authorizationDetails`.
    * Added `gmAction`.
    * Added `grantId`.
    * Added `grantSubject`.
    * Added `requestedClaimsForTx`.
    * Added `requestedVerifiedClaimsForTx`.
    * Added `credentialOfferInfo`.
    * Added `issuableCredentials`.

- `Client` class
    * Renamed `authorizationDataTypes` to `authorizationDetailsTypes`. (spec change)
    * Added `attributes`.
    * Added `customMetadata`.
    * Added `frontChannelRequestObjectEncryptionRequired`.
    * Added `requestObjectEncryptionAlgMatchRequired`.
    * Added `requestObjectEncryptionEncMatchRequired`.
    * Added `digestAlgorithm`.
    * Added `singleAccessTokenPerSubject`.
    * Added `pkceRequired`.
    * Added `pkceS256Required`.
    * Added `rsSignedRequestKeyId`.
    * Added `rsRequestSigned`.
    * Added `dpopRequired`.
    * Added `locked`.
    * Added `fapiModes`.
    * Added `entityId`.
    * Added `trustAnchorId`.
    * Added `trustChain`.
    * Added `trustChainExpiresAt`.
    * Added `trustChainUpdatedAt`.
    * Added `organizationName`.
    * Added `signedJwksUri`.
    * Added `clientRegistrationTypes`.
    * Added `automaticallyRegistered`.
    * Added `explicitlyRegistered`.
    * Added `credentialOfferEndpoint`.
    * Added `credentialResponseEncryptionRequired`.

- `ClientExtension` class
    * Added `tokenExchangePermitted`.

- `GrantType` class
    * Added `TOKEN_EXCHANGE`.
    * Added `JWT_BEARER`.
    * Added `PRE_AUTHORIZED_CODE`.

- `IntrospectionRequest` class
    * Added `resources`.
    * Added `uri`.
    * Added `message`.
    * Added `headers`.
    * Added `requiredComponents`.
    * Added `acrValues`.
    * Added `maxAge`.
    * Added `dpopNonceRequired`.

- `IntrospectionResponse` class
    * Added `clientEntityId`.
    * Added `clientEntityIdUsed`.
    * Added `authorizationDetails`.
    * Added `grantId`.
    * Added `grant`.
    * Added `consentedClaims`.
    * Added `serviceAttributes`.
    * Added `clientAttributes`.
    * Added `forExternalAttachment`.
    * Added `acr`.
    * Added `authTime`.
    * Added `grantType`.
    * Added `forCredentialIssuance`.
    * Added `cnonce`.
    * Added `cnonceExpiresAt`.
    * Added `issuableCredentials`.
    * Added `dpopNonce`.

- `Prompt` class
    * Added `CREATE`.

- `PushedAuthReqRequest` class
    * Added `dpop`.
    * Added `htm`.
    * Added `htu`.
    * Added `dpopNonceRequired`.

- `PushedAuthReqResponse` class
    * Added `clientAuthMethod`.
    * Added `dpopNonce`.

- `RevocationRequest` class
    * Added `clientCertificate`.
    * Added `clientCertificatePath`.

- `Service` class
    * Renamed `pkceRequire` to `pkceRequired`. (bug)
    * Renamed `mutualTlsValiddatePkiCertChain` to `mutualTlsValidatePkiCertChain`. (bug)
    * Renamed `supportedAuthorizationDataTypes` to `supportedAuthorizationDetailsTypes`. (spec change)
    * Added `refreshTokenDurationReset`.
    * Added `supportedDocuments`.
    * Added `supportedDocumentsMethods`.
    * Added `supportedDocumentsCheckMethods`.
    * Added `supportedElectronicRecords`.
    * Added `supportedAttachments`.
    * Added `supportedDigestAlgorithms`.
    * Added `nbfOptional`.
    * Added `issSuppressed`.
    * Added `attributes`.
    * Added `supportedCustomClientMetadata`.
    * Added `tokenExpirationLinked`.
    * Added `frontChannelRequestObjectEncryptionRequired`.
    * Added `requestObjectEncryptionAlgMatchRequired`.
    * Added `requestObjectEncryptionEncMatchRequired`.
    * Added `hsmEnabled`.
    * Added `hsks`.
    * Added `grantManagementEndpoint`.
    * Added `grantManagementActionRequired`.
    * Added `unauthorizedOnClientConfigSupported`.
    * Added `dcrScopeUsedAsRequestable`.
    * Added `predefinedTransformedClaims`.
    * Added `loopbackRedirectionUriVariable`.
    * Added `requestObjectAudienceChecked`.
    * Added `accessTokenForExternalAttachmentEmbedded`.
    * Added `refreshTokenIdempotent`.
    * Added `federationEnabled`.
    * Added `organizationName`.
    * Added `authorityHints`.
    * Added `trustAnchors`.
    * Added `federationJwks`.
    * Added `federationSignatureKeyId`.
    * Added `federationConfigurationDuration`.
    * Added `signedJwksUri`.
    * Added `federationRegistrationEndpoint`.
    * Added `supportedClientRegistrationTypes`.
    * Added `tokenExchangeByIdentifiableClientsOnly`.
    * Added `tokenExchangeByConfidentialClientsOnly`.
    * Added `tokenExchangeByPermittedClientsOnly`.
    * Added `tokenExchangeEncryptedJwtRejected`.
    * Added `tokenExchangeUnsignedJwtRejected`.
    * Added `jwtGrantByIdentifiableClientsOnly`.
    * Added `jwtGrantEncryptedJwtRejected`.
    * Added `jwtGrantUnsignedJwtRejected`.
    * Added `dcrDuplicateSoftwareIdBlocked`.
    * Added `resourceSignatureKeyId`.
    * Added `rsResponseSigned`.
    * Added `openidDroppedOnRefreshWithoutOfflineAccess`.
    * Added `verifiableCredentialsEnabled`.
    * Added `credentialIssuerMetadata`.
    * Added `credentialOfferDuration`.
    * Added `idTokenAudType`.
    * Added `supportedPromptValues`.
    * Added `verifiedClaimsValidationSchemaSet`.
    * Added `preAuthorizedGrantAnonymousAccessSupported`.
    * Added `cnonceDuration`.
    * Added `credentialTransactionDuration`.
    * Added `credentialDuration`.
    * Added `credentialJwks`.
    * Added `credentialJwksUri`.
    * Added `idTokenReissuable`.
    * Added `introspectionSignatureKeyId`.
    * Added `fapiModes`.
    * Added `dpopNonceRequired`.
    * Added `dpopNonceDuration`.

- `StandardIntrospectionAction` class
    * Added `JWT`.

- `StandardIntrospectionRequest` class
    * Added `withHiddenProperties`.
    * Added `rsUri`.
    * Added `httpAcceptHeader`.
    * Added `introspectionSignAlg`.
    * Added `introspectionEncryptionAlg`.
    * Added `introspectionEncryptionEnc`.
    * Added `sharedKeyForSign`.
    * Added `sharedKeyForEncryption`.
    * Added `publicKeyForEncryption`.

- `TokenAction` class
    * Added `TOKEN_EXCHANGE`.
    * Added `JWT_BEARER`.
    * Added `ID_TOKEN_REISSUABLE`.

- `TokenCreateRequest` class
    * Added `clientEntityIdUsed`.
    * Added `authorizationDetails`.
    * Added `resources`.
    * Added `forExternalAttachment`.
    * Added `jwtAtClaims`.
    * Added `acr`.
    * Added `authTime`.

- `TokenCreateResponse` class
    * Added `jwtAccessToken`.
    * Added `authorizationDetails`.
    * Added `forExternalAttachment`.
    * Added `refreshTokenScopes`.

- `TokenIssueRequest` class
    * Added `jwtAtClaims`.
    * Added `accessToken`.
    * Added `accessTokenDuration`.

- `TokenIssueResponse` class
    * Added `clientEntityId`.
    * Added `clientEntityIdUsed`.
    * Added `authorizationDetails`.
    * Added `serviceAttributes`.
    * Added `clientAttributes`.
    * Added `refreshTokenScopes`.

- `TokenRequest` class
    * Added `jwtAtClaims`.
    * Added `accessToken`.
    * Added `accessTokenDuration`.
    * Added `dpopNonceRequired`.

- `TokenResponse` class
    * Added `clientEntityId`.
    * Added `clientEntityIdUsed`.
    * Added `clientAuthMethod`.
    * Added `authorizationDetails`.
    * Added `grantId`.
    * Added `serviceAttributes`.
    * Added `clientAttributes`.
    * Added `audiences`.
    * Added `requestedTokenType`.
    * Added `subjectToken`.
    * Added `subjectTokenType`.
    * Added `subjectTokenInfo`.
    * Added `actorToken`.
    * Added `actorTokenType`.
    * Added `actorTokenInfo`.
    * Added `assertion`.
    * Added `previousRefreshTokenUsed`.
    * Added `cnonce`.
    * Added `cnonceExpiresAt`.
    * Added `cnonceDuration`.
    * Added `requestedIdTokenClaims`.
    * Added `dpopNonce`.
    * Added `refreshTokenScopes`.

- `TokenUpdateRequest` class
    * Added `refreshTokenExpiresAt`.
    * Added `refreshTokenExpiresAtUpdatedOnScopeUpdate`.
    * Added `authorizationDetails`.
    * Added `forExternalAttachment`.
    * Added `tokenId`.

- `TokenUpdateResponse` class
    * Added `refreshTokenExpiresAt`.
    * Added `authorizationDetails`.
    * Added `forExternalAttachment`.
    * Added `tokenId`.

- `UserInfoIssueRequest` class
    * Added `claimsForTx`.
    * Added `verifiedClaimsForTx`.
    * Added `requestSignature`.
    * Added `headers`.

- `UserInfoIssueResponse` class
    * Added `signature`.
    * Added `signatureInput`.
    * Added `contentDigest`.

- `UserInfoRequest` class
    * Added `uri`.
    * Added `headers`.
    * Added `message`.
    * Added `dpopNonceRequired`.

- `UserInfoResponse` class
    * Added `clientEntityId`.
    * Added `clientEntityIdUsed`.
    * Added `transformedClaims`.
    * Added `consentedClaims`.
    * Added `requestedClaimsForTx`.
    * Added `requestedVerifiedClaimsForTx`.
    * Added `serviceAttributes`.
    * Added `clientAttributes`.
    * Added `dpopNonce`.

- New types
    * `AttachmentType` class
    * `AuthorizationTicketInfo` class
    * `AuthorizationTicketInfoAction` class
    * `AuthorizationTicketInfoRequest` class
    * `AuthorizationTicketInfoResponse` class
    * `AuthzDetails` class
    * `AuthzDetailsElement` class
    * `ClientRegistrationType` class
    * `CredentialBatchIssueAction` class
    * `CredentialBatchIssueRequest` class
    * `CredentialBatchIssueResponse` class
    * `CredentialBatchParseAction` class
    * `CredentialBatchParseRequest` class
    * `CredentialBatchParseResponse` class
    * `CredentialDeferredIssueAction` class
    * `CredentialDeferredIssueRequest` class
    * `CredentialDeferredIssueResponse` class
    * `CredentialDeferredParseAction` class
    * `CredentialDeferredParseRequest` class
    * `CredentialDeferredParseResponse` class
    * `CredentialIssuanceOrder` class
    * `CredentialIssuerJwksAction` class
    * `CredentialIssuerJwksRequest` class
    * `CredentialIssuerJwksResponse` class
    * `CredentialIssuerMetadata` class
    * `CredentialIssuerMetadataAction` class
    * `CredentialIssuerMetadataRequest` class
    * `CredentialIssuerMetadataResponse` class
    * `CredentialJwtIssuerMetadataAction` class
    * `CredentialJwtIssuerMetadataRequest` class
    * `CredentialJwtIssuerMetadataResponse` class
    * `CredentialOfferCreateAction` class
    * `CredentialOfferCreateRequest` class
    * `CredentialOfferCreateResponse` class
    * `CredentialOfferInfo` class
    * `CredentialOfferInfoAction` class
    * `CredentialOfferInfoRequest` class
    * `CredentialOfferInfoResponse` class
    * `CredentialRequestInfo` class
    * `CredentialSingleIssueAction` class
    * `CredentialSingleIssueRequest` class
    * `CredentialSingleIssueResponse` class
    * `CredentialSingleParseAction` class
    * `CredentialSingleParseRequest` class
    * `CredentialSingleParseResponse` class
    * `DynamicScope` class
    * `EntityType` class
    * `FapiMode` class
    * `FederationConfigurationAction` class
    * `FederationConfigurationRequest` class
    * `FederationConfigurationResponse` class
    * `FederationRegistrationAction` class
    * `FederationRegistrationRequest` class
    * `FederationRegistrationResponse` class
    * `GMAction` class
    * `Grant` class
    * `GrantManagementAction` class
    * `GrantManagementRequest` class
    * `GrantManagementResponse` class
    * `GrantScope` class
    * `Hsk` class
    * `HskAction` class
    * `HskCreateRequest` class
    * `HskListAction` class
    * `HskListResponse` class
    * `HskResponse` class
    * `IDTokenReissueAction` class
    * `IDTokenReissueRequest` class
    * `IDTokenReissueResponse` class
    * `ServiceConfigurationRequest` class
    * `StringArray` class
    * `TokenInfo` class
    * `TokenRevokeRequest` class
    * `TokenRevokeResponse` class
    * `TrustAnchor` class


1.2.1 (2020-11-05)
------------------

- `Service` class
    * Added `claimShortcutRestrictive`.
    * Added `scopeRequired`.


1.2.0 (2020-10-08)
------------------

- README files
    * Added "AWS Support" section.


1.1.5 (2020-10-07)
------------------

- `authlete.aws.apigateway.Authorizer` class
    * Improved the way to extract an access token to support both "TOKEN" and
      "REQUEST" types of Lambda Event Payload.


1.1.4 (2020-10-07)
------------------

- `authlete.aws.apigateway.Authorizer` class
    * Introduced `policy` property to control behaviors in error cases.
    * Changed the content of `context` embedded in policies.


1.1.3 (2020-10-04)
------------------

- `authlete.aws.apigateway.Authorizer` class
    * Ensured `client_id` in `context` in IAM policies is always a string or `None`.


1.1.2 (2020-10-04)
------------------

- `authlete.aws.apigateway.Authorizer` class
    * Changed the behavior in the case of no access token.
    * Removed `on_no_access_token` hook.


1.1.1 (2020-10-04)
------------------

- `authlete.aws.apigateway.Authorizer` class
    * Added `update_policy_context` method.
    * Changed the content of `context` embedded in policies.
    * Changed interfaces of some hook methods.


1.1.0 (2020-10-04)
------------------

- `AuthleteApi` class
    * Added `tokenDelete` method.

- New packages
    * `authlete.aws`
    * `authlete.aws.apigateway`


1.0.3 (2020-10-01)
------------------

- `AuthleteApi` class
    * Added `pushedAuthorizationRequest` method.

- `AuthorizationFailReason` class
    * Added `INVALID_TARGET`.

- `AuthorizationIssueRequest` class
    * Added `idtHeaderParams`.

- `AuthorizationResponse` class
    * Added `purpose`.
    * Added `resources`.

- `BackchannelAuthenticationCompleteRequest` class
    * Added `idtHeaderParams`.

- `BackchannelAuthenticationCompleteResponse` class
    * Added `resources`.

- `BackchannelAuthenticationFailReason` class
    * Added `INVALID_TARGET`.

- `BackchannelAuthenticationResponse` class
    * Added `resources`.

- `Client` class
    * Added `authorizationDataTypes`.
    * Added `derivedSectorIdentifier`.
    * Added `parRequired`.
    * Added `requestObjectRequired`.
    * Renamed `sectorIdentifier` to `sectorIdentifierUri`.

- `ClientExtension` class
    * Added `accessTokenDuration`.
    * Added `refreshTokenDuration`.

- `DeviceAuthorizationResponse` class
    * Added `resources`.

- `DeviceVerificationResponse` class
    * Added `resources`.

- `IntrospectionRequest` class
    * Added `dpop`.
    * Added `htm`.
    * Added `htu`.

- `IntrospectionResponse` class
    * Added `accessTokenResources`.
    * Added `resources`.

- `Service` class
    * Added `endSessionEndpoint`.
    * Added `missingClientIdAllowed`.
    * Added `parRequired`.
    * Added `pushedAuthReqDuration`.
    * Added `refreshTokenDurationKept`.
    * Added `requestObjectRequired`.
    * Added `supportedAuthorizationDataTypes`.
    * Added `supportedEvidence`.
    * Added `supportedIdentityDocuments`.
    * Added `supportedTrustFrameworks`.
    * Added `supportedVerificationMethods`.
    * Added `supportedVerifiedClaims`.
    * Added `traditionalRequestObjectProcessingApplied`.
    * Renamed `requestObjectEndpoint` to `pushedAuthReqEndpoint`.

- `TokenCreateRequest` class
    * Added `certificateThumbprint`.
    * Added `dpopKeyThumbprint`.

- `TokenFailReason` class
    * Added `INVALID_TARGET`.

- `TokenIssueResponse` class
    * Added `accessTokenResources`.

- `TokenRequest` class
    * Added `dpop`.
    * Added `htm`.
    * Added `htu`.

- `TokenResponse` class
    * Added `accessTokenResources`.
    * Added `resources`.

- `TokenUpdateRequest` class
    * Added `certificateThumbprint`.
    * Added `dpopKeyThumbprint`.

- `UserInfoRequest` class
    * Added `dpop`.
    * Added `htm`.
    * Added `htu`.

- `UserInfoResponse` class
    * Added `userInfoClaims`.

- New classes
    * `PushedAuthReqAction`
    * `PushedAuthReqRequest`
    * `PushedAuthReqResponse`


1.0.2 (2019-08-09)
------------------

Renamed `user_info_*` to `userinfo_*`.


1.0.1 (2019-08-02)
------------------

Updated `setup.py` to fix `packages`, and add `install_requires` and `license`.


1.0.0 (2019-07-30)
------------------

First release.
