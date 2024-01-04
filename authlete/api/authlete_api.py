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


from abc import ABCMeta, abstractmethod


class AuthleteApi(metaclass=ABCMeta):
    @abstractmethod
    def getSettings(self):
        """Get the settings of this instance.

        You can set connection timeout and read timeout by configuring the Settings object.

        Returns:
            authlete.api.Settings

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def authorization(self, request):
        """Call Authlete's /auth/authorization API.

        Args:
            request (authlete.dto.AuthorizationRequest)

        Returns:
            authlete.dto.AuthorizationResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def authorizationFail(self, request):
        """Call Authlete's /auth/authorization/fail API.

        Args:
            request (authlete.dto.AuthorizationFailRequest)

        Returns:
            authlete.dto.AuthorizationFailResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def authorizationIssue(self, request):
        """Call Authlete's /auth/authorization/issue API.

        Args:
            request (authlete.dto.AuthorizationIssueRequest)

        Returns:
            authlete.dto.AuthorizationIssueResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def token(self, request):
        """Call Authlete's /auth/token API.

        Args:
            request (authlete.dto.TokenRequest)

        Returns:
            authlete.dto.TokenResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def tokenCreate(self, request):
        """Call Authlete's /auth/token/create API.

        Args:
            request (authlete.dto.TokenCreateRequest)

        Returns:
            authlete.dto.TokenCreateResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def tokenDelete(self, token):
        """Delete an access token.

        Call Authlete's /auth/token/delete/{token} API.

        Args:
            token (str) : An access token.

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def tokenFail(self, request):
        """Call Authlete's /auth/token/fail API.

        Args:
            request (authlete.dto.TokenFailRequest)

        Returns:
            authlete.dto.TokenFailResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def tokenIssue(self, request):
        """Call Authlete's /auth/token/issue API.

        Args:
            request (authlete.dto.TokenIssueRequest)

        Returns:
            authlete.dto.TokenIssueResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def tokenRevoke(self, request):
        """Call Authlete's /auth/token/revoke API.

        Args:
            request (authlete.dto.TokenRevokeRequest)

        Returns:
            authlete.dto.TokenRevokeResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def tokenUpdate(self, request):
        """Call Authlete's /auth/token/update API.

        Args:
            request (authlete.dto.TokenUpdateRequest)

        Returns:
            authlete.dto.TokenUpdateResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def getTokenList(self, clientIdentifier=None, subject=None, start=None, end=None):
        """Get the list of access tokens.

        Call Authlete's /auth/token/get/list API.

        Args:
            clientIdentifier (str) : The client ID or its alias.
            subject (str) : The subject (unique user ID) of the targeted access tokens.
            start (int) : The start index (inclusive) of the result set.
            end (int) : The end index (exclusive) of the result set.

        Returns:
            authlete.dto.TokenListResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def revocation(self, request):
        """Call Authlete's /auth/revocation API.

        Args:
            request (authlete.dto.RevocationRequest)

        Returns:
            authlete.dto.RevocationResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def userinfo(self, request):
        """Call Authlete's /auth/userinfo API.

        Args:
            request (authlete.dto.UserInfoRequest)

        Returns:
            authlete.dto.UserInfoResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def userinfoIssue(self, request):
        """Call Authlete's /auth/userinfo/issue API.

        Args:
            request (authlete.dto.UserInfoIssueRequest)

        Returns:
            authlete.dto.UserInfoIssueResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def introspection(self, request):
        """Call Authlete's /auth/introspection API.

        Args:
            request (authlete.dto.IntrospectionRequest)

        Returns:
            authlete.dto.IntrospectionResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def standardIntrospection(self, request):
        """Call Authlete's /auth/introspection/standard API.

        Args:
            request (authlete.dto.StandardIntrospectionRequest)

        Returns:
            authlete.dto.StandardIntrospectionResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def createService(self, service):
        """Create a service.

        Call Authlete's /service/create API.

        Args:
            service (authlete.dto.Service)

        Returns:
            authlete.dto.Service

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def deleteService(self, apiKey):
        """Delete a service.

        Call Authlete's /service/delete/{apiKey} API.

        Args:
            apiKey (int) : The API key of the service.

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def getService(self, apiKey):
        """Get information about a service.

        Call Authlete's /service/get/{apiKey} API.

        Args:
            apiKey (int) : The API key of the service.

        Returns:
            authlete.dto.Service

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def getServiceList(self, start=None, end=None):
        """Get the list of services.

        Call Authlete's /service/get/list API.

        Args:
            start (int) : The start index (inclusive) of the result set.
            end (int) : The end index (exclusive) of the result set.

        Returns:
            authlete.dto.ServiceListResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def updateService(self, service):
        """Update a service.

        Call Authlete's /service/update/{apiKey} API.

        Args:
            service (authlete.dto.Service)

        Returns:
            authlete.dto.Service

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def getServiceJwks(self, pretty=True, includePrivateKeys=False):
        """Get the JWK Set of a service.

        Call Authlete's /service/jwks/get API.

        Args:
            pretty (bool) : True to get the JSON in pretty format.
            includePrivateKeys (bool) : True to keep private keys in the JSON.

        Returns:
            str : The WK Set of the service in JSON format.

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def getServiceConfiguration(self, request=None):
        """Get the configuration of the service in JSON format.

        Call Authlete's /service/configuration API.

        Args:
            request (authlete.dto.ServiceConfigurationRequest)

        Returns:
            str : The configuration of the service in JSON format.

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def createClient(self, client):
        """Create a client.

        Call Authlete's /client/create API.

        Args:
            client (authlete.dto.Client)

        Returns
            authlete.dto.Client

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def dynamicClientRegister(self, request):
        """Register a client.

        Call Authlete's /client/registration API.

        Args:
            request (authlete.dto.ClientRegistrationRequest)

        Returns:
            authlete.dto.ClientRegistrationResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def dynamicClientGet(self, request):
        """Get a dynamically registered client.

        Call Authlete's /client/registration/get API.

        Args:
            request (authlete.dto.ClientRegistrationRequest)

        Returns:
            authlete.dto.ClientRegistrationResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def dynamicClientUpdate(self, request):
        """Update a dynamically registered client.

        Call Authlete's /client/registration/update API.

        Args:
            request (authlete.dto.ClientRegistrationRequest)

        Returns:
            authlete.dto.ClientRegistrationResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def dynamicClientDelete(self, request):
        """Delete a dynamically registered client.

        Call Authlete's /client/registration/delete API.

        Args:
            request (authlete.dto.ClientRegistrationRequest)

        Returns:
            authlete.dto.ClientRegistrationResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def deleteClient(self, clientId):
        """Delete a client.

        Call Authlete's /client/delete/{clientId} API.

        Args:
            clientId (int)

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def getClient(self, clientId):
        """Get information about a client.

        Call Authlete's /client/get/{clientId} API.

        Args:
            clientId (int)

        Returns:
            authlete.dto.Client

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def getClientList(self, developer=None, start=None, end=None):
        """Get the list of client applications.

        Call Authlete's /client/get/list API.

        Args:
            developer (str) : The developer of the targeted client applications.
            start (int) : The start index (inclusive) of the result set.
            end (int): The end index (exclusive) of the result set.

        Returns:
            authlete.dto.ClientListResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def updateClient(self, client):
        """Update a client.

        Call Authlete's /client/update/{clientId} API.

        Args:
            client (authlete.dto.Client)

        Returns:
            authlete.dto.Client

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def getRequestableScopes(self, clientId):
        """Get the requestable scopes assigned to a client.

        Call Authlete's /client/extension/requestable_scopes/get/{clientId} API.

        Args:
            clientId (int)

        Returns:
            list : Scope names (list of str).

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def setRequestableScopes(self, clientId, scopes):
        """Set the requestable scopes assigned to a client.

        Call Authlete's /client/extension/requestable_scopes/update/{clientId} API.

        Args:
            clientId (int)
            scopes (list) : Scope names (list of str)

        Returns:
            list : The resultant set of requestable scopes (list of str).

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def deleteRequestableScopes(self, clientId):
        """Clear the requestable scopes assigned to a client.

        Call Authlete's /client/extension/requestable_scopes/delete/{clientId} API.

        Args:
            clientId (int)

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def getGrantedScopes(self, clientId, subject):
        """Get the set of scopes that a user has granted to a client application.

        Call Authlete's /client/granted_scopes/get/{clientId} API.

        Args:
            clientId (int)
            subject (str) : A unique user identifier.

        Returns:
            authlete.dto.GrantedScopesGetResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def deleteGrantedScopes(self, clientId, subject):
        """Delete records about the set of scopes that a user has granted to a client application.

        Call Authlete's /client/granted_scopes/delete/{clientId} API.

        Args:
            clientId (int)
            subject (str) : A unique user identifier.

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def deleteClientAuthorization(self, clientId, subject):
        """Delete all existing access tokens issued to the client application by the user.

        Args:
            clientId (int)
            subject (str) : A unique user identifier.

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def getClientAuthorizationList(self, request):
        """Get the list of client applications authorized by the user.

        Args:
            request (authlete.dto.ClientAuthorizationGetListRequest)

        Returns:
            authlete.dto.AuthorizedClientListResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def updateClientAuthorization(self, clientId, request):
        """Update attributes of all existing access tokens issued to the client application by the user.

        Args:
            clientId (int)
            request (authlete.dto.ClientAuthorizationUpdateRequest)

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def refreshClientSecret(self, clientId):
        """Refresh the client secret of a client.

        Args:
            clientId (int)

        Returns:
            authlete.dto.ClientSecretRefreshResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def updateClientSecret(self, clientId, clientSecret):
        """Update the client secret of a client.

        Args:
            clientId (int)
            clientSecret (str) : The new value of the client secret.

        Returns:
            authlete.dto.ClientSecretUpdateResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def verifyJose(self, request):
        """Verify a JOSE object.

        Args:
            request (authlete.dto.JoseVerifyRequest)

        Returns:
            authlete.dto.JoseVerifyResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def backchannelAuthentication(self, request):
        """Call Authlete's /backchannel/authentication API.

        Args:
            request (authlete.dto.BackchannelAuthenticationRequest)

        Returns:
            authlete.dto.BackchannelAuthenticationResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def backchannelAuthenticationIssue(self, request):
        """Call Authlete's /backchannel/authentication/issue API.

        Args:
            request (authlete.dto.BackchannelAuthenticationIssueRequest)

        Returns:
            authlete.dto.BackchannelAuthenticationIssueResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def backchannelAuthenticationFail(self, request):
        """Call Authlete's /backchannel/authentication/fail API.

        Args:
            request (authlete.dto.BackchannelAuthenticationFailRequest)

        Returns:
            authlete.dto.BackchannelAuthenticationFailResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def backchannelAuthenticationComplete(self, request):
        """Call Authlete's /backchannel/authentication/complete API.

        Args:
            request (authlete.dto.BackchannelAuthenticationCompleteRequest)

        Returns:
            authlete.dto.BackchannelAuthenticationCompleteResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def deviceAuthorization(self, request):
        """Call Authlete's /device/authorization API.

        Args:
            request (authlete.dto.DeviceAuthorizationRequest)

        Returns:
            authlete.dto.DeviceAuthorizationResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def deviceComplete(self, request):
        """Call Authlete's /device/complete API.

        Args:
            request (authlete.dto.DeviceCompleteRequest)

        Returns:
            authlete.dto.DeviceCompleteResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def deviceVerification(self, request):
        """Call Authlete's /device/verification API.

        Args:
            request (authlete.dto.DeviceVerificationRequest)

        Returns:
            authlete.dto.DeviceVerificationResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def pushAuthorizationRequest(self, request):
        """Call Authlete's /push_auth_req API.

        Args:
            request (authlete.dto.PushedAuthReqRequest)

        Returns:
            authlete.dto.PushedAuthReqResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def hskCreate(self, request):
        """Call Authlete's /hsk/create API.

        Args:
            request (authlete.dto.HskCreateRequest)

        Returns:
            authlete.dto.HskResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def hskDelete(self, handle):
        """Call Authlete's /hsk/delete/{handle} API.

        Args:
            handle (str)

        Returns:
            authlete.dto.HskResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def hskGet(self, handle):
        """Call Authlete's /hsk/get/{handle} API.

        Args:
            handle (str)

        Returns:
            authlete.dto.HskResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def hskGetList(self):
        """Call Authlete's /hsk/get/list API.

        Returns:
            authlete.dto.HskListResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def echo(self, parameters):
        """Call Authlete's /misc/echo API.

        Args:
            parameters (dict)

        Returns:
            dict

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def gm(self, request):
        """Call Authlete's /gm API.

        Args:
            request (authlete.dto.GrantManagementRequest)

        Returns:
            authlete.dto.GrantManagementResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def updateClientLockFlag(self, clientIdentifier, clientLocked):
        """Call Authlete's /gm API.

        Args:
            clientIdentifier (str)
            clientLocked (bool)

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def federationConfiguration(self, request):
        """Call Authlete's /federation/configuration API.

        Args:
            request (authlete.dto.FederationConfigurationRequest)

        Returns:
            authlete.dto.FederationConfigurationResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def federationRegistration(self, request):
        """Call Authlete's /federation/registration API.

        Args:
            request (authlete.dto.FederationRegistrationRequest)

        Returns:
            authlete.dto.FederationRegistrationResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def credentialIssuerMetadata(self, request):
        """Call Authlete's /vci/metadata API.

        Args:
            request (authlete.dto.CredentialIssuerMetadataRequest)

        Returns:
            authlete.dto.CredentialIssuerMetadataResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def credentialJwtIssuerMetadata(self, request):
        """Call Authlete's /vci/jwtissuer API.

        Args:
            request (authlete.dto.CredentialJwtIssuerMetadataRequest)

        Returns:
            authlete.dto.CredentialJwtIssuerMetadataResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def credentialIssuerJwks(self, request):
        """Call Authlete's /vci/jwks API.

        Args:
            request (authlete.dto.CredentialIssuerJwksRequest)

        Returns:
            authlete.dto.CredentialIssuerJwksResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def credentialOfferCreate(self, request):
        """Call Authlete's /vci/offer/create API.

        Args:
            request (authlete.dto.CredentialOfferCreateRequest)

        Returns:
            authlete.dto.CredentialOfferCreateResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def credentialOfferInfo(self, request):
        """Call Authlete's /vci/offer/info API.

        Args:
            request (authlete.dto.CredentialOfferInfoRequest)

        Returns:
            authlete.dto.CredentialOfferInfoResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def credentialSingleParse(self, request):
        """Call Authlete's /vci/single/parse API.

        Args:
            request (authlete.dto.CredentialSingleParseRequest)

        Returns:
            authlete.dto.CredentialSingleParseResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def credentialSingleIssue(self, request):
        """Call Authlete's /vci/single/issue API.

        Args:
            request (authlete.dto.CredentialSingleIssueRequest)

        Returns:
            authlete.dto.CredentialSingleIssueResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def credentialBatchParse(self, request):
        """Call Authlete's /vci/batch/parse API.

        Args:
            request (authlete.dto.CredentialBatchParseRequest)

        Returns:
            authlete.dto.CredentialBatchParseResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def credentialBatchIssue(self, request):
        """Call Authlete's /vci/batch/issue API.

        Args:
            request (authlete.dto.CredentialBatchIssueRequest)

        Returns:
            authlete.dto.CredentialBatchIssueResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def credentialDeferredParse(self, request):
        """Call Authlete's /vci/deferred/parse API.

        Args:
            request (authlete.dto.CredentialDeferredParseRequest)

        Returns:
            authlete.dto.CredentialDeferredParseResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def credentialDeferredIssue(self, request):
        """Call Authlete's /vci/deferred/issue API.

        Args:
            request (authlete.dto.CredentialDeferredIssueRequest)

        Returns:
            authlete.dto.CredentialDeferredIssueResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def idTokenReissue(self, request):
        """Call Authlete's /idtoken/reissue API.

        Args:
            request (authlete.dto.IDTokenReissueRequest)

        Returns:
            authlete.dto.IDTokenReissueResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def authorizationTicketInfo(self, request):
        """Call Authlete's /auth/authorization/ticket/info API.

        Args:
            request (authlete.dto.AuthorizationTicketInfoRequest)

        Returns:
            authlete.dto.AuthorizationTicketInfoResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass


    @abstractmethod
    def authorizationTicketUpdate(self, request):
        """Call Authlete's /auth/authorization/ticket/update API.

        Args:
            request (authlete.dto.AuthorizationTicketUpdateRequest)

        Returns:
            authlete.dto.AuthorizationTicketUpdateResponse

        Raises:
            authlete.api.AuthleteApiException
        """
        pass
