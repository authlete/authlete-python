変更点
======

1.3.0 (2024 年 01 月 04 日)
---------------------------

- `AccessToken` クラス
    * `refreshTokenScopes` を追加。

- `AuthorizationIssueRequest` クラス
    * `authorizationDetails` を追加。
    * `consentedClaims` を追加。
    * `claimsForTx` を追加。
    * `verifiedClaimsForTx` を追加。
    * `jwtAtClaims` を追加。
    * `accessToken` を追加。
    * `idTokenAudType` を追加。
    * `accessTokenDuration` を追加。

- `AuthleteApi` クラス
    * `getServiceConfiguration` メソッドの引数 `pretty=True` を `request=None` へ変更。
    * `tokenRevoke` メソッドを追加。
    * `hskCreate` メソッドを追加。
    * `hskDelete` メソッドを追加。
    * `hskGet` メソッドを追加。
    * `hskGetList` メソッドを追加。
    * `echo` メソッドを追加。
    * `gm` メソッドを追加。
    * `updateClientLockFlag` メソッドを追加。
    * `federationConfiguration` メソッドを追加。
    * `federationRegistration` メソッドを追加。
    * `credentialIssuerMetadata` メソッドを追加。
    * `credentialJwtIssuerMetadata` メソッドを追加。
    * `credentialIssuerJwks` メソッドを追加。
    * `credentialOfferCreate` メソッドを追加。
    * `credentialOfferInfo` メソッドを追加。
    * `credentialSingleParse` メソッドを追加。
    * `credentialSingleIssue` メソッドを追加。
    * `credentialBatchParse` メソッドを追加。
    * `credentialBatchIssue` メソッドを追加。
    * `credentialDeferredParse` メソッドを追加。
    * `credentialDeferredIssue` メソッドを追加。
    * `idTokenReissue` メソッドを追加。
    * `authorizationTicketInfo` メソッドを追加。
    * `authorizationTicketUpdate` メソッドを追加。

- `AuthleteApiImpl` クラス
    * Authlete API バージョン 3 をサポート。

- `AuthleteConfiguration` クラス
    * `apiVersion` を追加。
    * `dpopKey` を追加。
    * `clientCertificate` を追加。

- `AuthleteEnvConfiguration` クラス
    * `apiVersion` を追加。
    * `dpopKey` を追加。
    * `clientCertificate` を追加。

- `AuthleteIniConfiguration` クラス
    * `apiVersion` を追加。
    * `dpopKey` を追加。
    * `clientCertificate` を追加。

- `AuthorizationIssueResponse` クラス
    * `ticketInfo` を追加。

- `AuthorizationRequest` クラス
    * `context` を追加。

- `AuthorizationResponse` クラス
    * `dynamicScopes` を追加。
    * `claimsAtUserInfo` を追加。
    * `clientEntityIdUsed` を追加。
    * `transformedClaims` を追加。
    * `authorizationDetails` を追加。
    * `gmAction` を追加。
    * `grantId` を追加。
    * `grantSubject` を追加。
    * `requestedClaimsForTx` を追加。
    * `requestedVerifiedClaimsForTx` を追加。
    * `credentialOfferInfo` を追加。
    * `issuableCredentials` を追加。

- `Client` クラス
    * `authorizationDataTypes` を `authorizationDetailsTypes` へ変更。 (仕様変更)
    * `attributes` を追加。
    * `customMetadata` を追加。
    * `frontChannelRequestObjectEncryptionRequired` を追加。
    * `requestObjectEncryptionAlgMatchRequired` を追加。
    * `requestObjectEncryptionEncMatchRequired` を追加。
    * `digestAlgorithm` を追加。
    * `singleAccessTokenPerSubject` を追加。
    * `pkceRequired` を追加。
    * `pkceS256Required` を追加。
    * `rsSignedRequestKeyId` を追加。
    * `rsRequestSigned` を追加。
    * `dpopRequired` を追加。
    * `locked` を追加。
    * `fapiModes` を追加。
    * `entityId` を追加。
    * `trustAnchorId` を追加。
    * `trustChain` を追加。
    * `trustChainExpiresAt` を追加。
    * `trustChainUpdatedAt` を追加。
    * `organizationName` を追加。
    * `signedJwksUri` を追加。
    * `clientRegistrationTypes` を追加。
    * `automaticallyRegistered` を追加。
    * `explicitlyRegistered` を追加。
    * `credentialOfferEndpoint` を追加。
    * `credentialResponseEncryptionRequired` を追加。

- `ClientExtension` クラス
    * `tokenExchangePermitted` を追加。

- `GrantType` クラス
    * `TOKEN_EXCHANGE` を追加。
    * `JWT_BEARER` を追加。
    * `PRE_AUTHORIZED_CODE` を追加。

- `IntrospectionRequest` クラス
    * `resources` を追加。
    * `uri` を追加。
    * `message` を追加。
    * `headers` を追加。
    * `requiredComponents` を追加。
    * `acrValues` を追加。
    * `maxAge` を追加。
    * `dpopNonceRequired` を追加。

- `IntrospectionResponse` クラス
    * `clientEntityId` を追加。
    * `clientEntityIdUsed` を追加。
    * `authorizationDetails` を追加。
    * `grantId` を追加。
    * `grant` を追加。
    * `consentedClaims` を追加。
    * `serviceAttributes` を追加。
    * `clientAttributes` を追加。
    * `forExternalAttachment` を追加。
    * `acr` を追加。
    * `authTime` を追加。
    * `grantType` を追加。
    * `forCredentialIssuance` を追加。
    * `cnonce` を追加。
    * `cnonceExpiresAt` を追加。
    * `issuableCredentials` を追加。
    * `dpopNonce` を追加。

- `Prompt` クラス
    * `CREATE` を追加。

- `PushedAuthReqRequest` クラス
    * `dpop` を追加。
    * `htm` を追加。
    * `htu` を追加。
    * `dpopNonceRequired` を追加。

- `PushedAuthReqResponse` クラス
    * `clientAuthMethod` を追加。
    * `dpopNonce` を追加。

- `RevocationRequest` クラス
    * `clientCertificate` を追加。
    * `clientCertificatePath` を追加。

- `Service` クラス
    * `pkceRequire` を `pkceRequired` へ変更。 (不具合修正)
    * `mutualTlsValiddatePkiCertChain` を `mutualTlsValidatePkiCertChain` へ変更。 (不具合修正)
    * `supportedAuthorizationDataTypes` を `supportedAuthorizationDetailsTypes` へ変更。 (仕様変更)
    * `refreshTokenDurationReset` を追加。
    * `supportedDocuments` を追加。
    * `supportedDocumentsMethods` を追加。
    * `supportedDocumentsCheckMethods` を追加。
    * `supportedElectronicRecords` を追加。
    * `supportedAttachments` を追加。
    * `supportedDigestAlgorithms` を追加。
    * `nbfOptional` を追加。
    * `issSuppressed` を追加。
    * `attributes` を追加。
    * `supportedCustomClientMetadata` を追加。
    * `tokenExpirationLinked` を追加。
    * `frontChannelRequestObjectEncryptionRequired` を追加。
    * `requestObjectEncryptionAlgMatchRequired` を追加。
    * `requestObjectEncryptionEncMatchRequired` を追加。
    * `hsmEnabled` を追加。
    * `hsks` を追加。
    * `grantManagementEndpoint` を追加。
    * `grantManagementActionRequired` を追加。
    * `unauthorizedOnClientConfigSupported` を追加。
    * `dcrScopeUsedAsRequestable` を追加。
    * `predefinedTransformedClaims` を追加。
    * `loopbackRedirectionUriVariable` を追加。
    * `requestObjectAudienceChecked` を追加。
    * `accessTokenForExternalAttachmentEmbedded` を追加。
    * `refreshTokenIdempotent` を追加。
    * `federationEnabled` を追加。
    * `organizationName` を追加。
    * `authorityHints` を追加。
    * `trustAnchors` を追加。
    * `federationJwks` を追加。
    * `federationSignatureKeyId` を追加。
    * `federationConfigurationDuration` を追加。
    * `signedJwksUri` を追加。
    * `federationRegistrationEndpoint` を追加。
    * `supportedClientRegistrationTypes` を追加。
    * `tokenExchangeByIdentifiableClientsOnly` を追加。
    * `tokenExchangeByConfidentialClientsOnly` を追加。
    * `tokenExchangeByPermittedClientsOnly` を追加。
    * `tokenExchangeEncryptedJwtRejected` を追加。
    * `tokenExchangeUnsignedJwtRejected` を追加。
    * `jwtGrantByIdentifiableClientsOnly` を追加。
    * `jwtGrantEncryptedJwtRejected` を追加。
    * `jwtGrantUnsignedJwtRejected` を追加。
    * `dcrDuplicateSoftwareIdBlocked` を追加。
    * `resourceSignatureKeyId` を追加。
    * `rsResponseSigned` を追加。
    * `openidDroppedOnRefreshWithoutOfflineAccess` を追加。
    * `verifiableCredentialsEnabled` を追加。
    * `credentialIssuerMetadata` を追加。
    * `credentialOfferDuration` を追加。
    * `idTokenAudType` を追加。
    * `supportedPromptValues` を追加。
    * `verifiedClaimsValidationSchemaSet` を追加。
    * `preAuthorizedGrantAnonymousAccessSupported` を追加。
    * `cnonceDuration` を追加。
    * `credentialTransactionDuration` を追加。
    * `credentialDuration` を追加。
    * `credentialJwks` を追加。
    * `credentialJwksUri` を追加。
    * `idTokenReissuable` を追加。
    * `introspectionSignatureKeyId` を追加。
    * `fapiModes` を追加。
    * `dpopNonceRequired` を追加。
    * `dpopNonceDuration` を追加。

- `StandardIntrospectionAction` クラス
    * `JWT` を追加。

- `StandardIntrospectionRequest` クラス
    * `withHiddenProperties` を追加。
    * `rsUri` を追加。
    * `httpAcceptHeader` を追加。
    * `introspectionSignAlg` を追加。
    * `introspectionEncryptionAlg` を追加。
    * `introspectionEncryptionEnc` を追加。
    * `sharedKeyForSign` を追加。
    * `sharedKeyForEncryption` を追加。
    * `publicKeyForEncryption` を追加。

- `TokenAction` クラス
    * `TOKEN_EXCHANGE` を追加。
    * `JWT_BEARER` を追加。
    * `ID_TOKEN_REISSUABLE` を追加。

- `TokenCreateRequest` クラス
    * `clientEntityIdUsed` を追加。
    * `authorizationDetails` を追加。
    * `resources` を追加。
    * `forExternalAttachment` を追加。
    * `jwtAtClaims` を追加。
    * `acr` を追加。
    * `authTime` を追加。

- `TokenCreateResponse` クラス
    * `jwtAccessToken` を追加。
    * `authorizationDetails` を追加。
    * `forExternalAttachment` を追加。
    * `refreshTokenScopes` を追加。

- `TokenIssueRequest` クラス
    * `jwtAtClaims` を追加。
    * `accessToken` を追加。
    * `accessTokenDuration` を追加。

- `TokenIssueResponse` クラス
    * `clientEntityId` を追加。
    * `clientEntityIdUsed` を追加。
    * `authorizationDetails` を追加。
    * `serviceAttributes` を追加。
    * `clientAttributes` を追加。
    * `refreshTokenScopes` を追加。

- `TokenRequest` クラス
    * `jwtAtClaims` を追加。
    * `accessToken` を追加。
    * `accessTokenDuration` を追加。
    * `dpopNonceRequired` を追加。

- `TokenResponse` クラス
    * `clientEntityId` を追加。
    * `clientEntityIdUsed` を追加。
    * `clientAuthMethod` を追加。
    * `authorizationDetails` を追加。
    * `grantId` を追加。
    * `serviceAttributes` を追加。
    * `clientAttributes` を追加。
    * `audiences` を追加。
    * `requestedTokenType` を追加。
    * `subjectToken` を追加。
    * `subjectTokenType` を追加。
    * `subjectTokenInfo` を追加。
    * `actorToken` を追加。
    * `actorTokenType` を追加。
    * `actorTokenInfo` を追加。
    * `assertion` を追加。
    * `previousRefreshTokenUsed` を追加。
    * `cnonce` を追加。
    * `cnonceExpiresAt` を追加。
    * `cnonceDuration` を追加。
    * `requestedIdTokenClaims` を追加。
    * `dpopNonce` を追加。
    * `refreshTokenScopes` を追加。

- `TokenUpdateRequest` クラス
    * `refreshTokenExpiresAt` を追加。
    * `refreshTokenExpiresAtUpdatedOnScopeUpdate` を追加。
    * `authorizationDetails` を追加。
    * `forExternalAttachment` を追加。
    * `tokenId` を追加。

- `TokenUpdateResponse` クラス
    * `refreshTokenExpiresAt` を追加。
    * `authorizationDetails` を追加。
    * `forExternalAttachment` を追加。
    * `tokenId` を追加。

- `UserInfoIssueRequest` クラス
    * `claimsForTx` を追加。
    * `verifiedClaimsForTx` を追加。
    * `requestSignature` を追加。
    * `headers` を追加。

- `UserInfoIssueResponse` クラス
    * `signature` を追加。
    * `signatureInput` を追加。
    * `contentDigest` を追加。

- `UserInfoRequest` クラス
    * `uri` を追加。
    * `headers` を追加。
    * `message` を追加。
    * `dpopNonceRequired` を追加。

- `UserInfoResponse` クラス
    * `clientEntityId` を追加。
    * `clientEntityIdUsed` を追加。
    * `transformedClaims` を追加。
    * `consentedClaims` を追加。
    * `requestedClaimsForTx` を追加。
    * `requestedVerifiedClaimsForTx` を追加。
    * `serviceAttributes` を追加。
    * `clientAttributes` を追加。
    * `dpopNonce` を追加。

- 新しいクラス
    * `AttachmentType` クラス
    * `AuthorizationTicketInfo` クラス
    * `AuthorizationTicketInfoAction` クラス
    * `AuthorizationTicketInfoRequest` クラス
    * `AuthorizationTicketInfoResponse` クラス
    * `AuthzDetails` クラス
    * `AuthzDetailsElement` クラス
    * `ClientRegistrationType` クラス
    * `CredentialBatchIssueAction` クラス
    * `CredentialBatchIssueRequest` クラス
    * `CredentialBatchIssueResponse` クラス
    * `CredentialBatchParseAction` クラス
    * `CredentialBatchParseRequest` クラス
    * `CredentialBatchParseResponse` クラス
    * `CredentialDeferredIssueAction` クラス
    * `CredentialDeferredIssueRequest` クラス
    * `CredentialDeferredIssueResponse` クラス
    * `CredentialDeferredParseAction` クラス
    * `CredentialDeferredParseRequest` クラス
    * `CredentialDeferredParseResponse` クラス
    * `CredentialIssuanceOrder` クラス
    * `CredentialIssuerJwksAction` クラス
    * `CredentialIssuerJwksRequest` クラス
    * `CredentialIssuerJwksResponse` クラス
    * `CredentialIssuerMetadata` クラス
    * `CredentialIssuerMetadataAction` クラス
    * `CredentialIssuerMetadataRequest` クラス
    * `CredentialIssuerMetadataResponse` クラス
    * `CredentialJwtIssuerMetadataAction` クラス
    * `CredentialJwtIssuerMetadataRequest` クラス
    * `CredentialJwtIssuerMetadataResponse` クラス
    * `CredentialOfferCreateAction` クラス
    * `CredentialOfferCreateRequest` クラス
    * `CredentialOfferCreateResponse` クラス
    * `CredentialOfferInfo` クラス
    * `CredentialOfferInfoAction` クラス
    * `CredentialOfferInfoRequest` クラス
    * `CredentialOfferInfoResponse` クラス
    * `CredentialRequestInfo` クラス
    * `CredentialSingleIssueAction` クラス
    * `CredentialSingleIssueRequest` クラス
    * `CredentialSingleIssueResponse` クラス
    * `CredentialSingleParseAction` クラス
    * `CredentialSingleParseRequest` クラス
    * `CredentialSingleParseResponse` クラス
    * `DynamicScope` クラス
    * `EntityType` クラス
    * `FapiMode` クラス
    * `FederationConfigurationAction` クラス
    * `FederationConfigurationRequest` クラス
    * `FederationConfigurationResponse` クラス
    * `FederationRegistrationAction` クラス
    * `FederationRegistrationRequest` クラス
    * `FederationRegistrationResponse` クラス
    * `GMAction` クラス
    * `Grant` クラス
    * `GrantManagementAction` クラス
    * `GrantManagementRequest` クラス
    * `GrantManagementResponse` クラス
    * `GrantScope` クラス
    * `Hsk` クラス
    * `HskAction` クラス
    * `HskCreateRequest` クラス
    * `HskListAction` クラス
    * `HskListResponse` クラス
    * `HskResponse` クラス
    * `IDTokenReissueAction` クラス
    * `IDTokenReissueRequest` クラス
    * `IDTokenReissueResponse` クラス
    * `ServiceConfigurationRequest` クラス
    * `StringArray` クラス
    * `TokenInfo` クラス
    * `TokenRevokeRequest` クラス
    * `TokenRevokeResponse` クラス
    * `TrustAnchor` クラス


1.2.1 (2020 年 11 月 05 日)
---------------------------

- `Service` クラス
    * `claimShortcutRestrictive` 追加。
    * `scopeRequired` 追加。


1.2.0 (2020 年 10 月 08 日)
---------------------------

- README ファイル
    * 「AWS サポート」セクションを追加。


1.1.5 (2020 年 10 月 07 日)
---------------------------

- `authlete.aws.apigateway.Authorizer` クラス
    * Lambda Event Payload のタイプの "TOKEN" と "REQUEST" を両方サポートできるよう、
      アクセストークンの抽出方法を改善。


1.1.4 (2020 年 10 月 07 日)
---------------------------

- `authlete.aws.apigateway.Authorizer` クラス
    * エラー時の動作を制御するため `policy` プロパティーを導入。
    * ポリシーに埋め込む `context` の内容を変更。


1.1.3 (2020 年 10 月 04 日)
---------------------------

- `authlete.aws.apigateway.Authorizer` クラス
    * IAM ポリシーの `context` 内の `client_id` が常に文字列または `None` になることを保証。


1.1.2 (2020 年 10 月 04 日)
---------------------------

- `authlete.aws.apigateway.Authorizer` クラス
    * アクセストークンが無い場合の挙動を変更。
    * `on_no_access_token` フックを削除。


1.1.1 (2020 年 10 月 04 日)
---------------------------

- `authlete.aws.apigateway.Authorizer` クラス
    * `update_policy_context` メソッド追加。
    * ポリシーに埋め込む `context` の内容変更。
    * フックメソッド群のインターフェース変更。


1.1.0 (2020 年 10 月 04 日)
---------------------------

- `AuthleteApi` クラス
    * `tokenDelete` メソッド追加。

- 新しいパッケージ
    * `authlete.aws`
    * `authlete.aws.apigateway`


1.0.3 (2020 年 10 月 01 日)
---------------------------

- `AuthleteApi` クラス
    * `pushAuthorizationRequest` メソッド追加。

- `AuthorizationFailReason` クラス
    * `INVALID_TARGET` 追加。

- `AuthorizationIssueRequest` クラス
    * `idtHeaderParams` 追加。

- `AuthorizationResponse` クラス
    * `purpose` 追加。
    * `resources` 追加。

- `BackchannelAuthenticationCompleteRequest` クラス
    * `idtHeaderParams` 追加。

- `BackchannelAuthenticationCompleteResponse` クラス
    * `resources` 追加。

- `BackchannelAuthenticationFailReason` クラス
    * `INVALID_TARGET` 追加。

- `BackchannelAuthenticationResponse` クラス
    * `resources` 追加。

- `Client` クラス
    * `authorizationDataTypes` 追加。
    * `derivedSectorIdentifier` 追加。
    * `parRequired` 追加。
    * `requestObjectRequired` 追加。
    * `sectorIdentifier` を `sectorIdentifierUri` に変更。

- `ClientExtension` クラス
    * `accessTokenDuration` 追加。
    * `refreshTokenDuration` 追加。

- `DeviceAuthorizationResponse` クラス
    * `resources` 追加。

- `DeviceVerificationResponse` クラス
    * `resources` 追加。

- `IntrospectionRequest` クラス
    * `dpop` 追加。
    * `htm` 追加。
    * `htu` 追加。

- `IntrospectionResponse` クラス
    * `accessTokenResources` 追加。
    * `resources` 追加。

- `Service` クラス
    * `endSessionEndpoint` 追加。
    * `missingClientIdAllowed` 追加。
    * `parRequired` 追加。
    * `pushedAuthReqDuration` 追加。
    * `refreshTokenDurationKept` 追加。
    * `requestObjectRequired` 追加。
    * `supportedAuthorizationDataTypes` 追加。
    * `supportedEvidence` 追加。
    * `supportedIdentityDocuments` 追加。
    * `supportedTrustFrameworks` 追加。
    * `supportedVerificationMethods` 追加。
    * `supportedVerifiedClaims` 追加。
    * `traditionalRequestObjectProcessingApplied` 追加。
    * `requestObjectEndpoint` を `pushedAuthReqEndpoint` に変更。

- `TokenCreateRequest` クラス
    * `certificateThumbprint` 追加。
    * `dpopKeyThumbprint` 追加。

- `TokenFailReason` クラス
    * `INVALID_TARGET` 追加。

- `TokenIssueResponse` クラス
    * `accessTokenResources` 追加。

- `TokenRequest` クラス
    * `dpop` 追加。
    * `htm` 追加。
    * `htu` 追加。

- `TokenResponse` クラス
    * `accessTokenResources` 追加。
    * `resources` 追加。

- `TokenUpdateRequest` クラス
    * `certificateThumbprint` 追加。
    * `dpopKeyThumbprint` 追加。

- `UserInfoRequest` クラス
    * `dpop` 追加。
    * `htm` 追加。
    * `htu` 追加。

- `UserInfoResponse` クラス
    * `userInfoClaims` 追加。

- 新しいクラス
    * `PushedAuthReqAction`
    * `PushedAuthReqRequest`
    * `PushedAuthReqResponse`


1.0.2 (2019 年 08 月 09 日)
---------------------------

`user_info_*` から `userinfo_*` に変更。


1.0.1 (2019 年 08 月 02 日)
---------------------------

`setup.up` を更新。 `packages` の修正、および `install_requires` と `license` の追加。


1.0.0 (2019 年 07 月 30 日)
---------------------------

最初のリリース

