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

        self._apiVersion              = cnf.apiVersion
        self._baseUrl                 = cnf.baseUrl.rstrip('/')
        self._serviceOwnerCredentials = (cnf.serviceOwnerApiKey, cnf.serviceOwnerApiSecret)
        self._serviceCredentials      = (cnf.serviceApiKey,      cnf.serviceApiSecret)
        self._settings                = Settings()

        # When the version of Authlete APIs is 3 (or higher).
        if cnf.apiVersion == "V3":
            # An access token is required for accessing the Authlete APIs.
            if cnf.serviceAccessToken is None:
                raise RuntimeError("'serviceAccessToken' of the configuration is None.")
            self._accessToken = cnf.serviceAccessToken

            # Some Authlete APIs require the prefix '/api/{serviceId}'
            self._apiPrefix = "/api/{}".format(cnf.serviceApiKey)
        else:
            # No access token is required for accessing the Authlete APIs.
            self._accessToken = None

            # All Authlete APIs have the same prefix '/api'
            self._apiPrefix = "/api"


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

        # If an access token is provided for accessing the Authlete API.
        if self._accessToken is not None:
            # Turn off the Basic Authentication with the pair of API key and API secret.
            credentials = None

        try:
            # Call the Authlete API.
            response = self.__sendRequest(method, url, queryParams, data, credentials, self._accessToken)
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


    def __sendRequest(self, method, url, params, data, credentials, accessToken):
        # headers
        headers = {
            "Accept":       "application/json",
            "Content-Type": "application/json"
        }

        # If an access token is provided.
        if accessToken is not None:
            headers["Authorization"] = "Bearer {}".format(accessToken)

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
            '{}/auth/authorization'.format(self._apiPrefix),
            request, AuthorizationResponse)


    def authorizationFail(self, request):
        return self.__callServicePostApi(
            '{}/auth/authorization/fail'.format(self._apiPrefix),
            request, AuthorizationFailResponse)


    def authorizationIssue(self, request):
        return self.__callServicePostApi(
            '{}/auth/authorization/issue'.format(self._apiPrefix),
            request, AuthorizationIssueResponse)


    def token(self, request):
        return self.__callServicePostApi(
            '{}/auth/token'.format(self._apiPrefix),
            request, TokenResponse)


    def tokenCreate(self, request):
        return self.__callServicePostApi(
            '{}/auth/token/create'.format(self._apiPrefix),
            request, TokenCreateResponse)


    def tokenDelete(self, token):
        self.__callServiceDeleteApi(
            '{}/auth/token/delete/{}'.format(self._apiPrefix, token))


    def tokenFail(self, request):
        return self.__callServicePostApi(
            '{}/auth/token/fail'.format(self._apiPrefix),
            request, TokenFailResponse)


    def tokenIssue(self, request):
        return self.__callServicePostApi(
            '{}/auth/token/issue'.format(self._apiPrefix),
            request, TokenIssueResponse)


    def tokenRevoke(self, request):
        return self.__callServicePostApi(
            '{}/auth/token/revoke'.format(self._apiPrefix),
            request, TokenRevokeResponse)


    def tokenUpdate(self, request):
        return self.__callServicePostApi(
            '{}/auth/token/update'.format(self._apiPrefix),
            request, TokenUpdateResponse)


    def getTokenList(self, clientIdentifier=None, subject=None, start=None, end=None):
        params = self.__buildDict(
            clientIdentifier=clientIdentifier,
            subject=subject, start=start, end=end)

        return self.__callServiceGetApi(
            '{}/auth/token/get/list'.format(self._apiPrefix),
            TokenListResponse, params)


    def revocation(self, request):
        return self.__callServicePostApi(
            '{}/auth/revocation'.format(self._apiPrefix),
            request, RevocationResponse)


    def userinfo(self, request):
        return self.__callServicePostApi(
            '{}/auth/userinfo'.format(self._apiPrefix),
            request, UserInfoResponse)


    def userinfoIssue(self, request):
        return self.__callServicePostApi(
            '{}/auth/userinfo/issue'.format(self._apiPrefix),
            request, UserInfoIssueResponse)


    def introspection(self, request):
        return self.__callServicePostApi(
            '{}/auth/introspection'.format(self._apiPrefix),
            request, IntrospectionResponse)


    def standardIntrospection(self, request):
        return self.__callServicePostApi(
            '{}/auth/introspection/standard'.format(self._apiPrefix),
            request, StandardIntrospectionResponse)


    def createService(self, service):
        return self.__callServiceOwnerPostApi(
            '/api/service/create',
            service, Service)


    def deleteService(self, apiKey):
        if self._apiVersion == "V3":
            path = '{}/service/delete'.format(self._apiPrefix)
        else:
            path = '{}/service/delete/{}'.format(self._apiPrefix, apiKey)

        self.__callServiceOwnerDeleteApi(path)


    def getService(self, apiKey):
        if self._apiVersion == "V3":
            path = '{}/service/get'.format(self._apiPrefix)
        else:
            path = '{}/service/get/{}'.format(self._apiPrefix, apiKey)

        return self.__callServiceOwnerGetApi(path, Service)


    def getServiceList(self, start=None, end=None):
        params = self.__buildDict(start=start, end=end)

        return self.__callServiceOwnerGetApi(
            '/api/service/get/list',
            ServiceListResponse, params)


    def updateService(self, service):
        if self._apiVersion == "V3":
            path = '{}/service/update'.format(self._apiPrefix)
        else:
            path = '{}/service/update/{}'.format(self._apiPrefix, service.apiKey)

        return self.__callServiceOwnerPostApi(path, service, Service)


    def getServiceJwks(self, pretty=True, includePrivateKeys=False):
        params = self.__buildDict(
            pretty=pretty, includePrivateKeys=includePrivateKeys)

        return self.__callServiceGetApi(
            '{}/service/jwks/get'.format(self._apiPrefix),
            None, params)


    def getServiceConfiguration(self, request=None):
        if request is None:
            request = ServiceConfigurationRequest()
            request.pretty = True

        return self.__callServicePostApi(
            '{}/service/configuration'.format(self._apiPrefix),
            request)


    def createClient(self, client):
        return self.__callServicePostApi(
            '{}/client/create'.format(self._apiPrefix),
            client, Client)


    def dynamicClientRegister(self, request):
        return self.__callServicePostApi(
            '{}/client/registration'.format(self._apiPrefix),
            request, ClientRegistrationResponse)


    def dynamicClientGet(self, request):
        return self.__callServicePostApi(
            '{}/client/registration/get'.format(self._apiPrefix),
            request, ClientRegistrationResponse)


    def dynamicClientUpdate(self, request):
        return self.__callServicePostApi(
            '{}/client/registration/update'.format(self._apiPrefix),
            request, ClientRegistrationResponse)


    def dynamicClientDelete(self, request):
        return self.__callServicePostApi(
            '{}/client/registration/delete'.format(self._apiPrefix),
            request, ClientRegistrationResponse)


    def deleteClient(self, clientId):
        return self.__callServiceDeleteApi(
            '{}/client/delete/{}'.format(self._apiPrefix, clientId))


    def getClient(self, clientId):
        return self.__callServiceGetApi(
            '{}/client/get/{}'.format(self._apiPrefix, clientId),
            Client)


    def getClientList(self, developer=None, start=None, end=None):
        params = self.__buildDict(
            developer=developer, start=start, end=end)

        return self.__callServiceGetApi(
            '{}/client/get/list'.format(self._apiPrefix),
            ClientListResponse, params)


    def updateClient(self, client):
        return self.__callServicePostApi(
            '{}/client/update/{}'.format(self._apiPrefix, client.clientId),
            client, Client)


    def getRequestableScopes(self, clientId):
        responseBody = self.__callServiceGetApi(
            '{}/client/extension/requestable_scopes/get/{}'.format(self._apiPrefix, clientId))

        dct = json.loads(responseBody)

        return dct['requestableScopes']


    def setRequestableScopes(self, clientId, scopes):
        requestBody = { 'requestableScopes': scopes }

        responseBody = self.__callServicePostApi(
            '{}/client/extension/requestable_scopes/update/{}'.format(self._apiPrefix, clientId),
            requestBody)

        dct = json.loads(responseBody)

        return dct['requestableScopes']


    def deleteRequestableScopes(self, clientId):
        self.__callServiceDeleteApi(
            '{}/client/extension/requestable_scopes/delete/{}'.format(self._apiPrefix, clientId))


    def getGrantedScopes(self, clientId, subject):
        requestBody = { 'subject': subject }

        return self.__callServicePostApi(
            '{}/client/granted_scopes/get/{}'.format(self._apiPrefix, clientId),
            requestBody, GrantedScopesGetResponse)


    def deleteGrantedScopes(self, clientId, subject):
        requestBody = { 'subject': subject }

        self.__callServicePostApi(
            '{}/client/granted_scopes/delete/{}'.format(self._apiPrefix, clientId),
            requestBody, ApiResponse)


    def deleteClientAuthorization(self, clientId, subject):
        request = ClientAuthorizationDeleteRequest()
        request.subject = subject

        self.__callServicePostApi(
            '{}/client/authorization/delete/{}'.format(self._apiPrefix, clientId),
            request, ApiResponse)


    def getClientAuthorizationList(self, request):
        return self.__callServicePostApi(
            '{}/client/authorization/get/list'.format(self._apiPrefix),
            request, AuthorizedClientListResponse)


    def updateClientAuthorization(self, clientId, request):
        self.__callServicePostApi(
            '{}/client/authorization/update/{}'.format(self._apiPrefix, clientId),
            request, ApiResponse)


    def refreshClientSecret(self, clientId):
        return self.__callServiceGetApi(
            '{}/client/secret/refresh/{}'.format(self._apiPrefix, clientId),
            ClientSecretRefreshResponse)


    def updateClientSecret(self, clientId, clientSecret):
        request = ClientSecretUpdateRequest()
        request.clientId      = clientId
        request.clilentSecret = clientSecret

        return self.__callServicePostApi(
            '{}/client/secret/update/{}'.format(self._apiPrefix, clientId),
            request, ClientSecretUpdateResponse)


    def verifyJose(self, request):
        return self.__callServicePostApi(
            '{}/jose/verify'.format(self._apiPrefix),
            request, JoseVerifyResponse)


    def backchannelAuthentication(self, request):
        return self.__callServicePostApi(
            '{}/backchannel/authentication'.format(self._apiPrefix),
            request, BackchannelAuthenticationResponse)


    def backchannelAuthenticationIssue(self, request):
        return self.__callServicePostApi(
            '{}/backchannel/authentication/issue'.format(self._apiPrefix),
            request, BackchannelAuthenticationIssueResponse)


    def backchannelAuthenticationFail(self, request):
        return self.__callServicePostApi(
            '{}/backchannel/authentication/fail'.format(self._apiPrefix),
            request, BackchannelAuthenticationFailResponse)


    def backchannelAuthenticationComplete(self, request):
        return self.__callServicePostApi(
            '{}/backchannel/authentication/complete'.format(self._apiPrefix),
            request, BackchannelAuthenticationCompleteResponse)


    def deviceAuthorization(self, request):
        return self.__callServicePostApi(
            '{}/device/authorization'.format(self._apiPrefix),
            request, DeviceAuthorizationResponse)


    def deviceComplete(self, request):
        return self.__callServicePostApi(
            '{}/device/complete'.format(self._apiPrefix),
            request, DeviceCompleteResponse)


    def deviceVerification(self, request):
        return self.__callServicePostApi(
            '{}/device/verification'.format(self._apiPrefix),
            request, DeviceVerificationResponse)


    def pushAuthorizationRequest(self, request):
        return self.__callServicePostApi(
            '{}/pushed_auth_req'.format(self._apiPrefix),
            request, PushedAuthReqResponse)


    def hskCreate(self, request):
        return self.__callServicePostApi(
            '{}/hsk/create'.format(self._apiPrefix),
            request, HskResponse)


    def hskDelete(self, handle):
        return self.__callServiceGetApi(
            '{}/hsk/delete/{}'.format(self._apiPrefix, handle),
            HskResponse)


    def hskGet(self, handle):
        return self.__callServiceGetApi(
            '{}/hsk/get/{}'.format(self._apiPrefix, handle),
            HskResponse)


    def hskGetList(self):
        return self.__callServiceGetApi(
            '{}/hsk/get/list'.format(self._apiPrefix),
            HskListResponse)


    def echo(self, parameters):
        responseBody = self.__callServiceGetApi(
            '/misc/echo', None, parameters)

        return json.loads(responseBody)


    def gm(self, request):
        return self.__callServicePostApi(
            '{}/gm'.format(self._apiPrefix),
            request, GrantManagementResponse)


    def updateClientLockFlag(self, clientIdentifier, clientLocked):
        requestBody = { 'clientLocked': clientLocked }

        self.__callServicePostApi(
            '{}/client/lock_flag/update/{}'.format(self._apiPrefix, clientIdentifier),
            requestBody)


    def federationConfiguration(self, request):
        return self.__callServicePostApi(
            '{}/federation/configuration'.format(self._apiPrefix),
            request, FederationConfigurationResponse)


    def federationRegistration(self, request):
        return self.__callServicePostApi(
            '{}/federation/registration'.format(self._apiPrefix),
            request, FederationRegistrationResponse)


    def credentialIssuerMetadata(self, request):
        return self.__callServicePostApi(
            '{}/vci/metadata'.format(self._apiPrefix),
            request, CredentialIssuerMetadataResponse)


    def credentialJwtIssuerMetadata(self, request):
        return self.__callServicePostApi(
            '{}/vci/jwtissuer'.format(self._apiPrefix),
            request, CredentialJwtIssuerMetadataResponse)


    def credentialIssuerJwks(self, request):
        return self.__callServicePostApi(
            '{}/vci/jwks'.format(self._apiPrefix),
            request, CredentialIssuerJwksResponse)


    def credentialOfferCreate(self, request):
        return self.__callServicePostApi(
            '{}/vci/offer/create'.format(self._apiPrefix),
            request, CredentialOfferCreateResponse)


    def credentialOfferInfo(self, request):
        return self.__callServicePostApi(
            '{}/vci/offer/info'.format(self._apiPrefix),
            request, CredentialOfferInfoResponse)


    def credentialSingleParse(self, request):
        return self.__callServicePostApi(
            '{}/vci/single/parse'.format(self._apiPrefix),
            request, CredentialSingleParseResponse)


    def credentialSingleIssue(self, request):
        return self.__callServicePostApi(
            '{}/vci/single/issue'.format(self._apiPrefix),
            request, CredentialSingleIssueResponse)


    def credentialBatchParse(self, request):
        return self.__callServicePostApi(
            '{}/vci/batch/parse'.format(self._apiPrefix),
            request, CredentialBatchParseResponse)


    def credentialBatchIssue(self, request):
        return self.__callServicePostApi(
            '{}/vci/batch/issue'.format(self._apiPrefix),
            request, CredentialBatchIssueResponse)


    def credentialDeferredParse(self, request):
        return self.__callServicePostApi(
            '{}/vci/deferred/parse'.format(self._apiPrefix),
            request, CredentialDeferredParseResponse)


    def credentialDeferredIssue(self, request):
        return self.__callServicePostApi(
            '{}/vci/deferred/issue'.format(self._apiPrefix),
            request, CredentialDeferredIssueResponse)


    def idTokenReissue(self, request):
        return self.__callServicePostApi(
            '{}/idtoken/reissue'.format(self._apiPrefix),
            request, IDTokenReissueResponse)


    def authorizationTicketInfo(self, request):
        return self.__callServicePostApi(
            '{}/auth/authorization/ticket/info'.format(self._apiPrefix),
            request, AuthorizationTicketInfoResponse)


    def authorizationTicketUpdate(self, request):
        return self.__callServicePostApi(
            '{}/auth/authorization/ticket/update'.format(self._apiPrefix),
            request, AuthorizationTicketUpdateResponse)
