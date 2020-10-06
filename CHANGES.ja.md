変更点
======

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

