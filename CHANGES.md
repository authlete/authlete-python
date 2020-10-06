CHANGES
=======

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
