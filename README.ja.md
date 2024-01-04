Python 用 Authlete ライブラリ
=============================

概要
----

[Authlete](https://www.authlete.com) Web API 用の公式 Python ライブラリです。

ライセンス
----------

  Apache License, Version 2.0

ソースコード
------------

  <code>https://github.com/authlete/authlete-python</code>

PyPI (Python Package Index)
---------------------------

  <code>https://pypi.org/project/authlete/</code>

インストール
------------

    pip install authlete

クイックスタート
----------------

下記のコードは「認可コードフロー」をシミュレートするものです。コード内の `CLIENT_ID`,
`SERVICE_API_KEY`, `SERVICE_API_SECRET` を適宜あなたのもので置き換えてください。
コードでは、クライアントアプリケーションのクライアントタイプが public であること
（そうでない場合はトークンエンドポイントでクライアント認証が要求される）、
登録されているリダイレクト URI の数が一つであること（そうでない場合は `redirect_uri`
リクエストパラメーターが要求される）を想定しています。

```python
from authlete.api  import *
from authlete.conf import *
from authlete.dto  import *


#--------------------------------------------------
# あなたの設定
#--------------------------------------------------
authlete_api_server = 'https://api.authlete.com'
service_api_key     = 'SERVICE_API_KEY'
service_api_secret  = 'SERVICE_API_SECRET'
client_id           = 'CLIENT_ID'
user_id             = 'USER_ID'

# Authlete バージョンが 3.0 以上の場合
service_access_token = 'SERVICE_ACCESS_TOKEN'
service_api_secret   = None


#--------------------------------------------------
# AuthleteApi
#--------------------------------------------------

# Authlete API にアクセスするための設定
cnf = AuthleteConfiguration()
cnf.baseUrl          = authlete_api_server
cnf.serviceApiKey    = service_api_key
cnf.serviceApiSecret = service_api_secret

# Authlete バージョンが 3.0 以上の場合
cnf.apiVersion         = "V3"
cnf.serviceAccessToken = service_access_token
cnf.serviceApiSecret   = None

# Authlete API を呼び出すためのインスタンス
api = AuthleteApiImpl(cnf)


#--------------------------------------------------
# /api/auth/authorization API
#--------------------------------------------------

# /api/auth/authorization API へのリクエストを用意する。
req = AuthorizationRequest()
req.parameters = 'response_type=code&client_id={}'.format(client_id)

# /api/auth/authorization API をコールする。
# レスポンスのクラスは authlete.dto.AuthorizationResponse.
res = api.authorization(req)


#--------------------------------------------------
# /api/auth/authorization/issue API
#--------------------------------------------------

# /api/auth/authorization/issue API へのリクエストを用意する。
req = AuthorizationIssueRequest()
req.ticket  = res.ticket
req.subject = user_id

# /api/auth/authorization/issue API をコールする。
# レスポンスのクラスは authlete.dto.AuthorizationIssueResponse.
res = api.authorizationIssue(req)

# ユーザーエージェントに返す認可レスポンス
print('HTTP/1.1 302 Found')
print('Location: {}'.format(res.responseContent))


#--------------------------------------------------
# /api/auth/token API
#--------------------------------------------------

# /api/auth/token API へのリクエストを用意する。
req = TokenRequest()
req.parameters = 'client_id={}&grant_type=authorization_code&code={}'\
    .format(client_id, res.authorizationCode)

# /api/auth/token API をコールする。
# レスポンスのクラスは authlete.dto.TokenResponse.
res = api.token(req)

# クライアントに返すトークンレスポンス
print("\nHTTP/1.1 200 OK")
print("Content-Type: application/json\n")
print(res.responseContent)
```

説明
----

#### AuthleteApi の取得方法

Authlete Web API とやりとりするメソッドは全て `authlete.api.AuthleteApi`
インターフェースに集められています。 `authlete.api.AuthleteApiImpl` クラスが
`AuthleteApi` を実装する唯一の実装です。 `AuthleteApiImpl` クラスのコンストラクタは
`authlete.conf.AuthleteConfiguration` クラスのインスタンスを必要とします。

```python
# AuthleteConfiguration のインスタンスを用意する。
cnf = AuthleteConfiguration()
cnf.baseUrl               = ...
cnf.serviceOwnerApiKey    = ...
cnf.serviceOwnerApiSecret = ...
cnf.serviceApiKey         = ...
cnf.serviceApiSecret      = ...

# Authlete バージョンが 3.0 以上の場合
cnf.apiVersion         = "V3"
cnf.serviceAccessToken = ...
cnf.serviceApiSecret   = None

# AuthleteApi インターフェースの実装を取得する。
api = AuthleteApiImpl(cnf)
```

`AuthleteConfiguration` には、 `AuthleteEnvConfiguration` と
`AuthleteIniConfiguration` という二つのサブクラスがあります。

`AuthleteEnvConfiguration` クラスは次の環境変数から設定を読み込みます。

- `AUTHLETE_API_VERSION`
- `AUTHLETE_BASE_URL`
- `AUTHLETE_SERVICEOWNER_APIKEY`
- `AUTHLETE_SERVICEOWNER_APISECRET`
- `AUTHLETE_SERVICE_APIKEY`
- `AUTHLETE_SERVICE_APISECRET`
- `AUTHLETE_SERVICE_ACCESSTOKEN`

`AuthleteEnvConfiguration` のコンストラクタが環境変数を読み込むので、Python
コードに書かなければならないのは、次のようにインスタンスを生成する処理だけです。

```python
cnf = AuthleteEnvConfiguration()
```

一方、 `AuthleteIniConfiguration` クラスは INI ファイルを読みます。
`AuthleteIniConfiguration` が想定しているファイルフォーマットは次の通りです。

```ini
[authlete]
api_version              = ...
base_url                 = ...
service_owner.api_key    = ...
service_owner.api_secret = ...
service.api_key          = ...
service.api_secret       = ...
service.access_token     = ...
```

`AuthleteIniConfiguration` のコンストラクタは、INI
ファイルの名前をオプショナルパラメーターとして受け取ります。パラメーターが省略された場合、
`authlete.ini` がデフォルトとして使用されます。INI ファイルの名前が `authlete.ini`
でない場合は、次のように明示的にコンストラクタにファイル名を渡してください。

```python
cnf = AuthleteIniConfiguration('configuration.ini')
```

#### AuthleteApi の設定

`AuthleteApi` インターフェースの `getSettings()` メソッドは
`authlete.api.Settings` クラスのインスタンスを返します。
このインスタンスを介して、接続タイムアウトとリードタイムアウトを設定することができます。

```python
settings = api.getSettings()
settings.connectionTimeout = 5.0
settings.readTimeout       = 5.0
```

#### AuthleteApi メソッドのカテゴリー

`AuthleteApi` インターフェースのメソッド群はいくつかのカテゴリーに分けることができます。

##### 認可エンドポイント実装のためのメソッド群

- `authorization(request)`
- `authorizationFail(equest)`
- `authorizationIssue(request)`

##### トークンエンドポイント実装のためのメソッド群

- `token(request)`
- `tokenFail(request)`
- `tokenIssue(request)`
- `idTokenReissue(request)`

##### サービス管理のためのメソッド群

- `createService(service)`
- `deleteService(serviceApiKey)`
- `getService(serviceApiKey)`
- `getServiceList(start=None, end=None)`
- `updateService(service)`

##### クライアントアプリケーション管理のためのメソッド群

- `createClient(client)`
- `deleteClient(clientId)`
- `getClient(clientId)`
- `getClientList(developer=None, start=None, end=None)`
- `updateClient(client)`
- `refreshClientSecret(clientId)`
- `updateClientSecret(clientId, clientSecret)`

##### アクセストークンの情報取得のためのメソッド群

- `introspection(request)`
- `standardIntrospection(request)`
- `getTokenList(clientIdentifier=None, subject=None, start=None, end=None)`

##### アクセストークン取り消しエンドポイント実装のためのメソッド群

- `revocation(request)`

##### ユーザー情報エンドポイント実装のためのメソッド群

- `userinfo(request)`
- `userinfoIssue(request)`

##### JWK セットエンドポイント実装のためのメソッド群

- `getServiceJwks(pretty=True, includePrivateKeys=False)`

##### OpenID Connect Discovery のためのメソッド群

- `getServiceConfiguration(pretty=True)`

##### トークン操作のためのメソッド群

- `tokenCreate(request)`
- `tokenDelete(token)`
- `tokenRevoke(request)`
- `tokenUpdate(request)`

##### クライアント毎の要求可能スコープ群に関するメソッド群 (非推奨; Client API で代替可能)

- `getRequestableScopes(clientId)`
- `setRequestableScopes(clientId, scopes)`
- `deleteRequestableScopes(clientId)`

##### 付与されたスコープの記録に関するメソッド群

- `getGrantedScopes(clientId, subject)`
- `deleteGrantedScopes(clientId, subject)`

##### ユーザー・クライアント単位の認可管理に関するメソッド群

- `deleteClientAuthorization(clientId, subject)`
- `getClientAuthorizationList(request)`
- `updateClientAuthorization(clientId, request)`

##### JOSE に関するメソッド群

- `verifyJose(request)`

##### CIBA (Client Initiated Backchannel Authentication) に関するメソッド群

- `backchannelAuthentication(request)`
- `backchannelAuthenticationIssue(request)`
- `backchannelAuthenticationFail(request)`
- `backchannelAuthenticationComplete(request)`

##### OpenID Connect Dynamic Client Registration に関するメソッド群

- `dynamicClientRegister(request)`
- `dynamicClientGet(request)`
- `dynamicClientUpdate(request)`
- `dynamicClientDelete(request)`

##### Device Flow に関するメソッド群

- `deviceAuthorization(request)`
- `deviceComplete(request)`
- `deviceVerification(request)`

##### PAR (Pushed Authorization Request) に関するメソッド群

- `pushAuthorizationRequest(request)`

##### Grant Management for OAuth 2.0 に関するメソッド群

- `gm(request)`

##### OpenID Federation 1.0 に関するメソッド群

- `federationConfiguration(request)`
- `federationRegistration(request)`

##### Verifiable Credentials に関するメソッド群

- `credentialIssuerMetadata(request)`
- `credentialIssuerJwks(request)`
- `credentialJwtIssuerMetadata(request)`
- `credentialOfferCreate(request)`
- `credentialOfferInfo(request)`
- `credentialSingleParse(request)`
- `credentialSingleIssue(request)`
- `credentialBatchParse(request)`
- `credentialBatchIssue(request)`
- `credentialDeferredParse(request)`
- `credentialDeferredIssue(request)`

Authlete バージョン
-------------------

幾つかの API や機能は、使用されている Authlete API サーバーがサポートしていなければ（たとえ
`AuthleteApi` インターフェースで定義されているとしても）使うことができません。例えば、CIBA は
Authlete 2.1 以降でのみ機能します。新しい Authlete バージョンを使用されたい場合は、ご連絡ください。

Authlete 2.0 以降で利用できる機能：

- Financial-grade API (FAPI)
- OAuth 2.0 Mutual TLS Client Authentication and Certificate Bound Access Tokens (MTLS)
- JWT-based Client Authentication (RFC 7523)
- Scope attributes
- UK Open Banking Security Profile

Authlete 2.1 以降で利用できる機能：

- Client Initiated Backchannel Authentication (CIBA)
- JWT Secured Authorization Response Mode for OAuth 2.0 (JARM)
- Dynamic Client Registration (RFC 7591 & RFC 7592)
- OAuth 2.0 Device Authorization Grant (Device Flow)
- JWT-based Access Token

詳細情報は [スペックシート](https://www.authlete.com/ja/legal/spec_sheet/)
を参照してください。

AWS サポート
------------

[Amazon API Gateway](https://aws.amazon.com/api-gateway/) 上に構築した API を、
[RFC 8705](https://www.rfc-editor.org/rfc/rfc8705.html) (OAuth 2.0 Mutual-TLS
Client Authentication and Certificate-Bound Access Tokens)
に準拠する「証明書に紐付くアクセストークン」により保護する
[Lambda Authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html)
の実装を支援するユーティリティークラスが、このライブラリには含まれています。

下記は、そのユーティリティークラスを用いて書かれた、短いものの完全に動作する
Lambda Authorizer の実装例です。

```python
from authlete.aws.apigateway.authorizer import Authorizer

authorizer = Authorizer()

def lambda_handler(event, context):
    return authorizer.handle(event, context)
```

詳細は "[Financial-grade Amazon API Gateway](https://www.authlete.com/developers/tutorial/financial_grade_apigateway/)"
を参照してください。

その他の情報
------------

- [authlete-python-django](https://github.com/authlete/authlete-python-django/) : Django 用 Authlete ライブラリ
- [django-oauth-server](https://github.com/authlete/django-oauth-server/) : Django による認可サーバーの実装
- [django-resource-server](https://github.com/authlete/django-resource-server/) : Django によるリソースサーバーの実装

コンタクト
----------

コンタクトフォーム : https://www.authlete.com/contact/

| 目的 | メールアドレス       |
|:-----|:---------------------|
| 一般 | info@authlete.com    |
| 営業 | sales@authlete.com   |
| 広報 | pr@authlete.com      |
| 技術 | support@authlete.com |
