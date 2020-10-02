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


import json
import requests
from authlete.api.authlete_api            import AuthleteApi
from authlete.api.authlete_api_exception  import AuthleteApiException
from authlete.api.settings                import Settings
from authlete.dto                         import *
from authlete.conf.authlete_configuration import AuthleteConfiguration
from authlete.types.jsonable              import Jsonable


class AuthleteApiImpl(AuthleteApi):
    def __init__(self, cnf):
        """Implementation of AuthleteApi.

        Args:
            cnf (authlete.dto.AuthleteConfiguration)
        """

        if isinstance(cnf, AuthleteConfiguration) == False:
            raise RuntimeError("'cnf' must be an instance of AuthleteConfiguration.")

        if cnf.baseUrl is None:
            raise RuntimeError("'baseUrl' of the configuration is None.")

        self._baseUrl                 = cnf.baseUrl.rstrip('/')
        self._serviceOwnerCredentials = (cnf.serviceOwnerApiKey, cnf.serviceOwnerApiSecret)
        self._serviceCredentials      = (cnf.serviceApiKey,      cnf.serviceApiSecret)
        self._settings                = Settings()


    def __callApi(self, method, credentials, path, queryParams, requestBody, responseClass):
        # The URL of the Authlete API.
        url = self._baseUrl + path

        # Convert 'requestBody' to an instance of str. The format is JSON.
        if requestBody is None:
            data = None
        elif isinstance(requestBody, Jsonable):
            data = requestBody.to_json()
        else:
            data = json.dumps(requestBody)

        try:
            # Call the Authlete API.
            response = self.__sendRequest(method, url, queryParams, data, credentials)
        except Exception as cause:
            raise AuthleteApiException(
                url, queryParams, data, "API call to " + path + " failed.", cause)

        # If the HTTP status code is not 2XX.
        if response.status_code < 200 or 300 <= response.status_code:
            message = self.__extractResultMessage(response.text)
            if message is None:
                message = "{} API returned {}".format(path, response.status_code)
            raise AuthleteApiException(url, queryParams, data, message, None, response)

        # Create an instance of responseClass from the HTTP message body of the response.
        return self.__deserializeResponseBody(response.text, responseClass)


    def __sendRequest(self, method, url, params, data, credentials):
        # headers
        headers = {
            "Accept":       "application/json",
            "Content-Type": "application/json"
        }

        # timeout
        timeout = (self._settings.connectionTimeout, self._settings.readTimeout)

        return requests.request(method, url, params=params,
            data=data, headers=headers, auth=credentials, timeout=timeout)


    def __extractResultMessage(self, body):
        if body is None:
            return None

        # The response body may be JSON which contains 'resultMessage'.
        try:
            # Convert the JSON string into a Python dictionary.
            dct = json.loads(body)
            return dct['resultMessage']
        except Exception:
            return None


    def __deserializeResponseBody(self, body, responseClass):
        if body is None:
            return None

        if responseClass is None:
            return body

        return responseClass.from_json(body)


    def __callGetApi(self, credentials, path, responseClass, queryParams):
        return self.__callApi('GET', credentials, path, queryParams, None, responseClass)


    def __callPostApi(self, credentials, path, requestBody, responseClass):
        return self.__callApi('POST', credentials, path, None, requestBody, responseClass)


    def __callDeleteApi(self, credentials, path, queryParams):
        return self.__callApi('DELETE', credentials, path, queryParams, None, None)


    def __callServiceGetApi(self, path, responseClass=None, queryParams=None):
        return self.__callGetApi(self._serviceCredentials, path, responseClass, queryParams)


    def __callServicePostApi(self, path, requestBody, responseClass=None):
        return self.__callPostApi(self._serviceCredentials, path, requestBody, responseClass)


    def __callServiceDeleteApi(self, path, queryParams=None):
        return self.__callDeleteApi(self._serviceCredentials, path, queryParams)


    def __callServiceOwnerGetApi(self, path, responseClass=None, queryParams=None):
        return self.__callGetApi(self._serviceOwnerCredentials, path, responseClass, queryParams)


    def __callServiceOwnerPostApi(self, path, requestBody, responseClass=None):
        return self.__callPostApi(self._serviceOwnerCredentials, path, requestBody, responseClass)


    def __callServiceOwnerDeleteApi(self, path, queryParams=None):
        return self.__callDeleteApi(self._serviceOwnerCredentials, path, queryParams)


    def __buildDict(self, **kwargs):
        dct = {}

        for key, value in kwargs.items():
            if value is not None:
                dct[key] = value

        return dct


    def getSettings(self):
        return self._settings


    def authorization(self, request):
        return self.__callServicePostApi(
            '/api/auth/authorization',
            request, AuthorizationResponse)


    def authorizationFail(self, request):
        return self.__callServicePostApi(
            '/api/auth/authorization/fail',
            request, AuthorizationFailResponse)


    def authorizationIssue(self, request):
        return self.__callServicePostApi(
            '/api/auth/authorization/issue',
            request, AuthorizationIssueResponse)


    def token(self, request):
        return self.__callServicePostApi(
            '/api/auth/token',
            request, TokenResponse)


    def tokenCreate(self, request):
        return self.__callServicePostApi(
            '/api/auth/token/create',
            request, TokenCreateResponse)


    def tokenDelete(self, token):
        self.__callServiceDeleteApi(
            '/api/auth/token/delete/{}'.format(token))


    def tokenFail(self, request):
        return self.__callServicePostApi(
            '/api/auth/token/fail',
            request, TokenFailResponse)


    def tokenIssue(self, request):
        return self.__callServicePostApi(
            '/api/auth/token/issue',
            request, TokenIssueResponse)


    def tokenUpdate(self, request):
        return self.__callServicePostApi(
            '/api/auth/token/update',
            request, TokenUpdateResponse)


    def getTokenList(self, clientIdentifier=None, subject=None, start=None, end=None):
        params = self.__buildDict(
            clientIdentifier=clientIdentifier,
            subject=subject, start=start, end=end)

        return self.__callServiceGetApi(
            '/api/auth/token/get/list',
            TokenListResponse, params)


    def revocation(self, request):
        return self.__callServicePostApi(
            '/api/auth/revocation',
            request, RevocationResponse)


    def userinfo(self, request):
        return self.__callServicePostApi(
            '/api/auth/userinfo',
            request, UserInfoResponse)


    def userinfoIssue(self, request):
        return self.__callServicePostApi(
            '/api/auth/userinfo/issue',
            request, UserInfoIssueResponse)


    def introspection(self, request):
        return self.__callServicePostApi(
            '/api/auth/introspection',
            request, IntrospectionResponse)


    def standardIntrospection(self, request):
        return self.__callServicePostApi(
            '/api/auth/introspection/standard',
            request, StandardIntrospectionResponse)


    def createService(self, service):
        return self.__callServiceOwnerPostApi(
            '/api/service/create',
            service, Service)


    def deleteService(self, apiKey):
        self.__callServiceOwnerDeleteApi(
            '/api/service/delete/{}'.format(apiKey))


    def getService(self, apiKey):
        return self.__callServiceOwnerGetApi(
            '/api/service/get/{}'.format(apiKey),
            Service)


    def getServiceList(self, start=None, end=None):
        params = self.__buildDict(start=start, end=end)

        return self.__callServiceOwnerGetApi(
            '/api/service/get/list',
            ServiceListResponse, params)


    def updateService(self, service):
        return self.__callServiceOwnerPostApi(
            '/api/service/update/{}'.format(service.apiKey),
            service, Service)


    def getServiceJwks(self, pretty=True, includePrivateKeys=False):
        params = self.__buildDict(
            pretty=pretty, includePrivateKeys=includePrivateKeys)

        return self.__callServiceGetApi(
            '/api/service/jwks/get',
            None, params)


    def getServiceConfiguration(self, pretty=True):
        params = self.__buildDict(pretty=pretty)

        return self.__callServiceGetApi(
            '/api/service/configuration',
            None, params)


    def createClient(self, client):
        return self.__callServicePostApi(
            '/api/client/create',
            client, Client)


    def dynamicClientRegister(self, request):
        return self.__callServicePostApi(
            '/api/client/registration',
            request, ClientRegistrationResponse)


    def dynamicClientGet(self, request):
        return self.__callServicePostApi(
            '/api/client/registration/get',
            request, ClientRegistrationResponse)


    def dynamicClientUpdate(self, request):
        return self.__callServicePostApi(
            '/api/client/registration/update',
            request, ClientRegistrationResponse)


    def dynamicClientDelete(self, request):
        return self.__callServicePostApi(
            '/api/client/registration/delete',
            request, ClientRegistrationResponse)


    def deleteClient(self, clientId):
        return self.__callServiceDeleteApi(
            '/api/client/delete/{}'.format(clientId))


    def getClient(self, clientId):
        return self.__callServiceGetApi(
            '/api/client/get/{}'.format(clientId),
            Client)


    def getClientList(self, developer=None, start=None, end=None):
        params = self.__buildDict(
            developer=developer, start=start, end=end)

        return self.__callServiceGetApi(
            '/api/client/get/list',
            ClientListResponse, params)


    def updateClient(self, client):
        return self.__callServicePostApi(
            '/api/client/update/{}'.format(client.clientId),
            client, Client)


    def getRequestableScopes(self, clientId):
        responseBody = self.__callServiceGetApi(
            '/api/client/extension/requestable_scopes/get/{}'.format(clientId))

        dct = json.loads(responseBody)

        return dct['requestableScopes']


    def setRequestableScopes(self, clientId, scopes):
        requestBody = { 'requestableScopes': scopes }

        responseBody = self.__callServicePostApi(
            '/api/client/extension/requestable_scopes/update/{}'.format(clientId),
            requestBody)

        dct = json.loads(responseBody)

        return dct['requestableScopes']


    def deleteRequestableScopes(self, clientId):
        self.__callServiceDeleteApi(
            '/api/client/extension/requestable_scopes/delete/{}'.format(clientId))


    def getGrantedScopes(self, clientId, subject):
        requestBody = { 'subject': subject }

        return self.__callServicePostApi(
            '/api/client/granted_scopes/get/{}'.format(clientId),
            requestBody, GrantedScopesGetResponse)


    def deleteGrantedScopes(self, clientId, subject):
        requestBody = { 'subject': subject }

        self.__callServicePostApi(
            '/api/client/granted_scopes/delete/{}'.format(clientId),
            requestBody, ApiResponse)


    def deleteClientAuthorization(self, clientId, subject):
        request = ClientAuthorizationDeleteRequest()
        request.subject = subject

        self.__callServicePostApi(
            '/api/client/authorization/delete/{}'.format(clientId),
            request, ApiResponse)


    def getClientAuthorizationList(self, request):
        return self.__callServicePostApi(
            '/api/client/authorization/get/list',
            request, AuthorizedClientListResponse)


    def updateClientAuthorization(self, clientId, request):
        self.__callServicePostApi(
            '/api/client/authorization/update/{}'.format(clientId),
            request, ApiResponse)


    def refreshClientSecret(self, clientId):
        return self.__callServiceGetApi(
            '/api/client/secret/refresh/{}'.format(clientId),
            ClientSecretRefreshResponse)


    def updateClientSecret(self, clientId, clientSecret):
        request = ClientSecretUpdateRequest()
        request.clientId      = clientId
        request.clilentSecret = clientSecret

        return self.__callServicePostApi(
            '/api/client/secret/update/{}'.format(clientId),
            request, ClientSecretUpdateResponse)


    def verifyJose(self, request):
        return self.__callServicePostApi(
            '/api/jose/verify',
            request, JoseVerifyResponse)


    def backchannelAuthentication(self, request):
        return self.__callServicePostApi(
            '/api/backchannel/authentication',
            request, BackchannelAuthenticationResponse)


    def backchannelAuthenticationIssue(self, request):
        return self.__callServicePostApi(
            '/api/backchannel/authentication/issue',
            request, BackchannelAuthenticationIssueResponse)


    def backchannelAuthenticationFail(self, request):
        return self.__callServicePostApi(
            '/api/backchannel/authentication/fail',
            request, BackchannelAuthenticationFailResponse)


    def backchannelAuthenticationComplete(self, request):
        return self.__callServicePostApi(
            '/api/backchannel/authentication/complete',
            request, BackchannelAuthenticationCompleteResponse)


    def deviceAuthorization(self, request):
        return self.__callServicePostApi(
            '/api/device/authorization',
            request, DeviceAuthorizationResponse)


    def deviceComplete(self, request):
        return self.__callServicePostApi(
            '/api/device/complete',
            request, DeviceCompleteResponse)


    def deviceVerification(self, request):
        return self.__callServicePostApi(
            '/api/device/verification',
            request, DeviceVerificationResponse)


    def pushAuthorizationRequest(self, request):
        return self.__callServicePostApi(
            '/api/pushed_auth_req',
            request, PushedAuthReqResponse)
