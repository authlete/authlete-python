Authlete Library for Python
===========================

Overview
--------

This is the official Python library for [Authlete](https://www.authlete.com/)
Web APIs.

License
-------

  Apache License, Version 2.0

Source Code
-----------

  <code>https://github.com/authlete/authlete-python</code>

PyPI (Python Package Index)
---------------------------

  <code>https://pypi.org/project/authlete/</code>

Install
-------

    pip install authlete

Quick Start
-----------

The following code simulates "Authorization Code Flow". Replace `CLIENT_ID`,
`SERVICE_API_KEY` and `SERVICE_API_SECRET` in the code with your own properly.
The code assumes that the client type of the client application is 'public'
(otherwise client authentication would be required at the token endpoint) and
the number of registered redirect URIs is one (otherwise `redirect_uri` request
parameter would be required).

```python
from authlete.api  import *
from authlete.conf import *
from authlete.dto  import *


#--------------------------------------------------
# Your Configuration
#--------------------------------------------------
authlete_api_server = 'https://api.authlete.com'
service_api_key     = 'SERVICE_API_KEY'
service_api_secret  = 'SERVICE_API_SECRET'
client_id           = 'CLIENT_ID'
user_id             = 'USER_ID'


#--------------------------------------------------
# AuthleteApi
#--------------------------------------------------

# Configuration to access Authlete APIs.
cnf = AuthleteConfiguration()
cnf.baseUrl          = authlete_api_server
cnf.serviceApiKey    = service_api_key
cnf.serviceApiSecret = service_api_secret

# Authlete API caller
api = AuthleteApiImpl(cnf)


#--------------------------------------------------
# /api/auth/authorization API
#--------------------------------------------------

# Prepare a request to /api/auth/authorization API.
req = AuthorizationRequest()
req.parameters = 'response_type=code&client_id={}'.format(client_id)

# Call /api/auth/authorization API. The class of the
# response is authlete.dto.AuthorizationResponse.
res = api.authorization(req)


#--------------------------------------------------
# /api/auth/authorization/issue API
#--------------------------------------------------

# Prepare a request to /api/auth/authorization/issue API.
req = AuthorizationIssueRequest()
req.ticket  = res.ticket
req.subject = user_id

# Call /api/auth/authorization/issue API. The class of the
# response is authlete.dto.AuthorizationIssueResponse.
res = api.authorizationIssue(req)

# An authorization response returned to the user agent.
print('HTTP/1.1 302 Found')
print('Location: {}'.format(res.responseContent))


#--------------------------------------------------
# /api/auth/token API
#--------------------------------------------------

# Prepare a request to /api/auth/token API.
req = TokenRequest()
req.parameters = 'client_id={}&grant_type=authorization_code&code={}'\
    .format(client_id, res.authorizationCode)

# Call /api/auth/token API. The class of the response is
# authlete.dto.TokenResponse.
res = api.token(req)

# A token response returned to the client.
print("\nHTTP/1.1 200 OK")
print("Content-Type: application/json\n")
print(res.responseContent)
```

Description
-----------

#### How To Get AuthleteApi

All the methods to communicate with Authlete Web APIs are gathered in
`authlete.api.AuthleteApi` interface. `authlete.api.AuthleteApiImpl` class is
the only implementation of the interface. The constructor of `AuthleteApiImpl`
class requires an instance of `authlete.conf.AuthleteConfiguration` class.

```python
# Prepare an instance of AuthleteConfiguration.
cnf = AuthleteConfiguration()
cnf.baseUrl               = ...
cnf.serviceOwnerApiKey    = ...
cnf.serviceOwnerApiSecret = ...
cnf.serviceApiKey         = ...
cnf.serviceApiSecret      = ...

# Get an implementation of AuthleteApi interface.
api = AuthleteApiImpl(cnf)
```

`AuthleteConfiguration` class has two subclasses, `AuthleteEnvConfiguration`
and `AuthleteIniConfiguration`.

`AuthleteEnvConfiguration` class reads settings from the following environment
variables.

- `AUTHLETE_BASE_URL`
- `AUTHLETE_SERVICEOWNER_APIKEY`
- `AUTHLETE_SERVICEOWNER_APISECRET`
- `AUTHLETE_SERVICE_APIKEY`
- `AUTHLETE_SERVICE_APISECRET`

The constructor of `AuthleteEnvConfiguration` reads the environment variables,
so what you have to do in Python code is just to create an instance of the
class as follows.

```python
cnf = AuthleteEnvConfiguration()
```

On the other hand, `AuthleteIniConfiguration` class reads an INI file. The
format of the file `AuthleteIniConfiguration` expects is as follows.

```ini
[authlete]
base_url                 = ...
service_owner.api_key    = ...
service_owner.api_secret = ...
service.api_key          = ...
service.api_secret       = ...
```

The constructor of `AuthleteIniConfiguration` accepts an optional parameter
which represents the name of an INI file. If the parameter is omitted,
`authlete.ini` is used as the default file. If the name of your INI file is
not `authlete.ini`, pass the file name to the constructor explicitly as follows.

```python
cnf = AuthleteIniConfiguration('configuration.ini')
```

#### AuthleteApi Settings

`getSettings()` method of `AuthleteApi` interface returns an instance of
`authlete.api.Settings` class. You can set connection timeout and read timeout
via the instance.

```python
settings = api.getSettings()
settings.connectionTimeout = 5.0
settings.readTimeout       = 5.0
```

#### AuthleteApi Method Categories

Methods in `AuthleteApi` interface can be divided into some categories.

##### Methods for Authorization Endpoint Implementation

- `authorization(request)`
- `authorizationFail(equest)`
- `authorizationIssue(request)`

##### Methods for Token Endpoint Implementation

- `token(request)`
- `tokenFail(request)`
- `tokenIssue(request)`

##### Methods for Service Management

- `createService(service)`
- `deleteService(serviceApiKey)`
- `getService(serviceApiKey)`
- `getServiceList(start=None, end=None)`
- `updateService(service)`

##### Methods for Client Application Management

- `createClient(client)`
- `deleteClient(clientId)`
- `getClient(clientId)`
- `getClientList(developer=None, start=None, end=None)`
- `updateClient(client)`
- `refreshClientSecret(clientId)`
- `updateClientSecret(clientId, clientSecret)`

##### Methods for Access Token Introspection

- `introspection(request)`
- `standardIntrospection(request)`
- `getTokenList(clientIdentifier=None, subject=None, start=None, end=None)`

##### Methods for Revocation Endpoint Implementation

- `revocation(request)`

##### Methods for User Info Endpoint Implementation

- `userinfo(request)`
- `userinfoIssue(request)`

##### Methods for JWK Set Endpoint Implementation

- `getServiceJwks(pretty=True, includePrivateKeys=False)`

##### Methods for OpenID Connect Discovery

- `getServiceConfiguration(pretty=True)`

##### Methods for Token Operations

- `tokenCreate(request)`
- `tokenDelete(token)`
- `tokenUpdate(request)`

##### Methods for Requestable Scopes per Client (deprecated; Client APIs suffice)

- `getRequestableScopes(clientId)`
- `setRequestableScopes(clientId, scopes)`
- `deleteRequestableScopes(clientId)`

##### Methods for Records of Granted Scopes

- `getGrantedScopes(clientId, subject)`
- `deleteGrantedScopes(clientId, subject)`

##### Methods for Authorization Management on a User-Client Combination Basis

- `deleteClientAuthorization(clientId, subject)`
- `getClientAuthorizationList(request)`
- `updateClientAuthorization(clientId, request)`

##### Methods for JOSE

- `verifyJose(request)`

##### Methods for CIBA (Client Initiated Backchannel Authentication)

- `backchannelAuthentication(request)`
- `backchannelAuthenticationIssue(request)`
- `backchannelAuthenticationFail(request)`
- `backchannelAuthenticationComplete(request)`

##### Methods for OpenID Connect Dynamic Client Registration

- `dynamicClientRegister(request)`
- `dynamicClientGet(request)`
- `dynamicClientUpdate(request)`
- `dynamicClientDelete(request)`

##### Methods for Device Flow

- `deviceAuthorization(request)`
- `deviceComplete(request)`
- `deviceVerification(request)`

##### Methods for PAR (Pushed Authorization Request)

- `pushAuthorizationRequest(request)`

Authlete Version
----------------

Some APIs and features don't work (even if they are defined in the `AuthleteApi`
interface) if Authlete API server you use doesn't support them. For example,
CIBA works only in Authlete 2.1 onwards. Please contact us if you want to use
newer Authlete versions.

Features available in Authlete 2.0 and onwards:

- Financial-grade API (FAPI)
- OAuth 2.0 Mutual TLS Client Authentication and Certificate Bound Access Tokens (MTLS)
- JWT-based Client Authentication (RFC 7523)
- Scope attributes
- UK Open Banking Security Profile

Features available in Authlete 2.1 and onwards:

- Client Initiated Backchannel Authentication (CIBA)
- JWT Secured Authorization Response Mode for OAuth 2.0 (JARM)
- Dynamic Client Registration (RFC 7591 & RFC 7592)
- OAuth 2.0 Device Authorization Grant (Device Flow)
- JWT-based Access Token

See [Spec Sheet](https://www.authlete.com/legal/spec_sheet/) for further details.

See Also
--------

- [authlete-python-django](https://github.com/authlete/authlete-python-django/) : Authlete library for Django
- [django-oauth-server](https://github.com/authlete/django-oauth-server/) : Authorization server implementation using Django
- [django-resource-server](https://github.com/authlete/django-resource-server/) : Resource server implementation using Django

Contact
-------

Contact Form : https://www.authlete.com/contact/

| Purpose   | Email Address        |
|:----------|:---------------------|
| General   | info@authlete.com    |
| Sales     | sales@authlete.com   |
| PR        | pr@authlete.com      |
| Technical | support@authlete.com |
