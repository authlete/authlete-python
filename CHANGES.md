CHANGES
=======

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


1.0.2 (2019-08-09)
------------------

Renamed `user_info_*` to `userinfo_*`.


1.0.1 (2019-08-02)
------------------

Updated `setup.py` to fix `packages`, and add `install_requires` and `license`.


1.0.0 (2019-07-30)
------------------

First release.
