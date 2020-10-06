#
# Copyright (C) 2020 Authlete, Inc.
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


import pprint
import re
from json import loads
from authlete.api.authlete_api_impl           import AuthleteApiImpl
from authlete.aws.arn                         import ARN
from authlete.conf.authlete_env_configuration import AuthleteEnvConfiguration
from authlete.dto.introspection_request       import IntrospectionRequest


class Authorizer:
    # Regular expression to extract an access token from the value of
    # the Authorization HTTP header.
    BEARER_TOKEN_PATTERN = re.compile('^Bearer[ ]+([^ ]+)[ ]*$', re.I)

    # Default timeout values for Authlete API calls.
    DEFAULT_CONNECTION_TIMEOUT = 7.0
    DEFAULT_READ_TIMEOUT       = 7.0


    def __init__(self, api=None, verbose=False, policy=True):
        """Constructor.

        To conform to specifications related to OAuth 2.0, a Lambda authorizer
        has to tell Amazon API Gateway to return "401 Unauthorized" to the API
        caller in some cases (e.g. when the presented access token has expired).
        According to AWS's technical documents and tutorials, the authorizer
        has to thrown an exception with a message ``Unauthorized`` to achieve it.
        However, such simple exception drops all valuable information about the
        "Unauthorized" response and makes debugging very hard.

        Therefore, by default, in other words, when ``policy`` is True (default),
        this authorizer implementation always returns an IAM policy which
        represents either "Allow" or "Deny" even in error cases where an
        exception with a message ``Unauthorized`` should be thrown.

        Args:
            api (:obj:`authlete.api.AuthleteApi`, optional) : Implementation of AuthleteApi (AuthleteImpl).
            verbose (bool, optional) : True for verbose logging by log() and plog() methods. Default is False.
            policy  (bool, optional) : True to return a policy even in error cases. Default is True.
        """
        if api is None:
            # Build a caller for Authlete APIs. AuthleteEnvConfiguration
            # reads configuration from the environemt variables such as
            # AUTHLETE_SERVICE_APIKEY, AUTHLETE_SERVICE_APISECRET and
            # AUTHLETE_BASE_URL.
            api = AuthleteApiImpl(AuthleteEnvConfiguration())
            settings = api.getSettings()
            settings.connectionTimeout = self.__class__.DEFAULT_CONNECTION_TIMEOUT
            settings.readTimeout       = self.__class__.DEFAULT_READ_TIMEOUT

        self.api     = api
        self.verbose = verbose
        self.policy  = policy


    def handle(self, event, context, scopes_determiner=None):
        """Judge whether the resource access is allowed or denied.

        The third argument ``scopes_determiner`` is a function. If given,
        it is called to generate a list of scopes which are required to
        access the resource. The function takes the following 4 arguments:
        ``event`` (the event given to the authorizer), ``context`` (the
        context given to the authorizer), ``method`` (the HTTP method of
        the resource access) and ``path`` (the path of the resource).

        If ``scopes_determiner`` is not given, ``determine_scopes()``
        method is called instead to generate a list of required scopes.
        Developers can choose either to give ``scopes_determiner`` to
        this ``handle()`` method or to make a subclass of this class and
        override ``determine_scopes()`` method.

        Args:
            event (dict)      : The event given to the authorizer.
            context (dict)    : The context given to the authorizer.
            scopes_determiner : A function to determine required scopes.

        Returns:
            An IAM policy that tells Amazon API Gateway to allow or deny
            the resource access.

        Raises:
            When ``policy`` property is False (its default value is True),
            this method may raise a RuntimeError to indicate that Amazon
            API Gateway should return "401 Unauthorized" or
            "500 Internal Server Error" to the API caller.
        """

        # Notify subclasses of entry.
        self.__on_enter(event, context)

        # Build an IntrospectionRequest to introspect the access token.
        # It is a request to Authlete's /api/auth/introspection API.
        request = self.__build_introspection_request(event, context, scopes_determiner)

        response  = None
        exception = None

        try:
            # Introspect the access token by Authlete's introspection API.
            # The API response is an instance of IntrospectionResponse.
            response = self.api.introspection(request)

            # Notify subclasses of the introspection result.
            self.__on_introspection(event, context, request, response)
        except Exception as e:
            # The API call failed.
            exception = e

        if exception:
            # Notify subclasses of the introspection error.
            self.__on_introspection_error(event, context, request, exception)

            if self.policy:
                # Tell Amazon API Gateway to reject the resource access.
                return self.__deny(event, context, request, response, exception)
            else:
                # 500 Internal Server Error
                raise self.__internal_server_error(event, context)

        # Dispatch based on the result of the introspection.
        return self.__dispatch(event, context, request, response)


    def determine_scopes(self, event, context, method, path):
        """Get the list of scopes required to access the resource.

        Subclasses are expected to override this method as necessary.

        Args:
            event   (dict) : The event given to the authorizer.
            context (dict) : The context given to the authorizer.
            method  (str)  : The HTTP method.
            path    (str)  : The resource path.

        Returns:
            List of scope names or None.
        """
        return None


    def update_policy_context(self, event, context, request, response, exception, ctx):
        """Update the context embedded in the policy.

        Args:
            event     (dict) : The event given to the authorizer.
            context   (dict) : The context given to the authorizer.
            request   (:obj:`authlete.dto.IntrospectionRequest`)  : Request to Authlete's introspection API. May be null.
            response  (:obj:`authlete.dto.IntrospectionResponse`) : Response from Authlete's introspection API. May be null.
            exception (:obj:`Exception`) : Exception raised during the API call to Authlete's introspection API. May be null.
            ctx       (dict) : The policy context to update.
        """
        pass


    def __on_enter(self, event, context):
        if self.verbose:
            self.log('[on_enter]')
            self.log('event =')
            self.plog(event)
            self.log('context =')
            self.plog(context)

        self.on_enter(event, context)


    def on_enter(self, event, context):
        """Called when the handle() method starts.

        Args:
            event   (dict) : The event given to the authorizer.
            context (dict) : The context given to the authorizer.
        """
        pass


    def __on_introspection_error(self, event, context, request, exception):
        if self.verbose is None:
            self.log('[on_introspection_error]')
            self.log('request =')
            self.plog(request)
            self.log('exception =')
            self.plog(exception)

        self.on_introspection_error(event, context, request, exception)


    def on_introspection_error(self, event, context, request, exception):
        """Called when the call to Authlete's introspection API failed.

        Args:
            event     (dict) : The event given to the authorizer.
            context   (dict) : The context given to the authorizer.
            request   (:obj:`authlete.dto.IntrospectionRequest`) : Request to Authlete's introspection API.
            exception (:obj:`Exception`) : Exception raised during the call to Authlete's introspection API. This may be AuthleteApiException.
        """
        pass


    def __on_introspection(self, event, context, request, response):
        if self.verbose:
            self.log('[on_introspection]')
            self.log('request =')
            self.plog(request)
            self.log('response =')
            self.plog(response)

        self.on_introspection(event, context, request, response)


    def on_introspection(self, event, context, request, response):
        """Called when introspection succeeded.

        Args:
            event   (dict) : The event given to the authorizer.
            context (dict) : The context given to the authorizer.
            response (:obj:`authlete.dto.IntrospectionResponse`) : Response from Authlete's introspection API.
        """
        pass


    def __on_allow(self, event, context, request, response, policy):
        if self.verbose:
            self.log('[on_allow]')
            self.log('policy =')
            self.plog(policy)

        self.on_allow(event, context, request, response, policy)


    def on_allow(self, event, context, request, response, policy):
        """Called when the access to the resource is allowed.

        Args:
            event    (dict) : The event given to the authorizer.
            context  (dict) : The context given to the authorizer.
            request  (:obj:`authlete.dto.IntrospectionRequest`)  : Request to Authlete's introspection API.
            response (:obj:`authlete.dto.IntrospectionResponse`) : Response from Authlete's introspection API.
            policy   (dict) : IAM policy that allows the access to the resource.
        """
        pass


    def __on_deny(self, event, context, request, response, exception, policy):
        if self.verbose:
            self.log('[on_deny]')
            self.log('policy =')
            self.plog(policy)

        self.on_deny(event, context, request, response, exception, policy)


    def on_deny(self, event, context, request, response, exception, policy):
        """Called when the access to the resource is denied.

        Args:
            event     (dict) : The event given to the authorizer.
            context   (dict) : The context given to the authorizer.
            request   (:obj:`authlete.dto.IntrospectionRequest`)  : Request to Authlete's introspection API. May be null.
            response  (:obj:`authlete.dto.IntrospectionResponse`) : Response from Authlete's introspection API. May be null.
            exception (:obj:`Exception`) : Exception raised during the call to Authlete's introspection API. May be null.
            policy    (dict) : IAM policy that denies the access to the resource.
        """
        pass


    def log(self, msg):
        print(msg)


    def plog(self, obj):
        pprint.pprint(obj, width=200)


    def __on_unauthorized(self, event, context):
        if self.verbose:
            self.log('[unauthorized]')

        self.on_unauthorized(event, context)


    def on_unauthorized(self, event, context):
        """Called when an exception for '401 Unauthorized' is thrown.

        Args:
            event   (dict) : The event given to the authorizer.
            context (dict) : The context given to the authorizer.
        """
        pass


    def __unauthorized(self, event, context):
        # Notify subclasses of 'Unauthorized'.
        self.__on_unauthorized(event, context)

        # Return an exception that tells Amazon API Gateway to respond with
        # "401 Unauthorized".
        return RuntimeError('Unauthorized')


    def __on_internal_server_error(self, event, context):
        if self.verbose:
            self.log('[internal_server_error]')

        self.on_internal_server_error(event, context)


    def on_internal_server_error(self, event, context):
        """Called when an exception for '500 Internal Server Error' is thrown.

        Args:
            event   (dict) : The event given to the authorizer.
            context (dict) : The context given to the authorizer.
        """
        pass


    def __internal_server_error(self, event, context):
        # Notify subclasses of 'Internal Server Error'.
        self.__on_internal_server_error(event, context)

        # Return an exception that tells Amazon API Gateway to respond with
        # "500 Internal Server Error".
        return RuntimeError('Internal Server Error')


    def __build_introspection_request(self, event, context, scopes_determiner):
        # Parse the ARN (Amazon Resource Name).
        arn = self.__parse_arn(event)

        # Parse the resource part of the ARN and extract the HTTP method and
        # the path of the resource.
        resource = self.__parse_resource(arn)
        method   = resource['method']
        path     = resource['path']

        # Extract the access token.
        token = self.__extract_access_token(event)

        # Extract the client certificate in PEM format.
        certificate = self.__extract_client_certificate(event)

        # Scopes required to access the resource.
        if scopes_determiner:
            scopes = scopes_determiner(event, context, method, path)
        else:
            scopes = self.determine_scopes(event, context, method, path)

        # Build an introspection request.
        request = IntrospectionRequest()
        request.token             = token
        request.scopes            = scopes
        request.clientCertificate = certificate

        return request


    def __parse_arn(self, event):
        # Parse the ARN (Amazon Resource Name). The format expected here
        # is as follows.
        #
        #   arn:{partition}:execute-api:{region}:{account-id}:{api-id}/{stage}/{http-method}/{resource-path}
        #
        # See also:
        #
        #   Amazon Resource Names (ARNs)
        #     https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html
        #
        #   API Gateway Amazon Resource Name (ARN) reference
        #     https://docs.aws.amazon.com/apigateway/latest/developerguide/arn-format-reference.html
        #
        return ARN.parse(event['methodArn'])


    def __parse_resource(self, arn):
        # Split the resource part of the ARN. The format expected here is
        # as follows.
        #
        #   {api-id}/{stage}/{http-method}/{resource-path}
        #
        # See also:
        #
        #   API Gateway Amazon Resource Name (ARN) reference
        #     https://docs.aws.amazon.com/apigateway/latest/developerguide/arn-format-reference.html
        #
        elements = arn.resource.split('/', 3)

        return {
            'method': elements[2],
            'path':   elements[3],
        }


    def __extract_access_token(self, event):
        # The value of the Authorization HTTP header
        header_value = event.get('authorizationToken')
        if header_value is None:
            return None

        # Check if the header value contains a bearer token.
        match = self.__class__.BEARER_TOKEN_PATTERN.fullmatch(header_value)
        if match is None:
            return None

        # Extract the access token.
        return match.group(1)


    def __extract_client_certificate(self, event):
        # Introducing mutual TLS authentication for Amazon API Gateway
        #   https://aws.amazon.com/blogs/compute/introducing-mutual-tls-authentication-for-amazon-api-gateway/

        try:
            # v2 payload
            return event['requestContext']['authentication']['clientCert']['clientCertPem']
        except Exception:
            pass

        try:
            # v1 payload
            return event['requestContext']['identity']['clientCert']['clientCertPem']
        except Exception:
            return None


    def __dispatch(self, event, context, request, response):
        # The 'action' property contained in a response from Authlete's
        # introspection API indicates the HTTP status that should be returned
        # to the client application from the protected resource endpoint.
        action = response.action.name

        if action == 'OK':
            # The access token is valid. Tell Amazon API Gateway to accept
            # the resource access.
            return self.__allow(event, context, request, response)
        elif action == 'BAD_REQUEST':
            # The access to the resource contains no access token.
            # Tell Amazon API Gateway to reject the resource access.
            return self.__deny(event, context, request, response, None)
        elif action == 'FORBIDDEN':
            # The access token does not cover the required scopes.
            # Tell Amazon API Gateway to reject the resource access.
            return self.__deny(event, context, request, response, None)
        elif action == 'UNAUTHORIZED':
            # The access token does not exist or has expired. Or, the
            # certificate thumbprint associated with the access token does
            # not match that of the certificate presented in mutual TLS
            # connection of the resource access.
            if self.policy:
                # Tell Amazon API Gateway to reject the resource access.
                return self.__deny(event, context, request, response, None)
            else:
                # Tell Amazon API Gateway to respond with "401 Unauthorized".
                raise self.__unauthorized(event, context)
        else:
            # Unknown action. This should not happen.
            if self.policy:
                # Tell Amazon API Gateway to reject the resource access.
                return self.__deny(event, context, request, response, None)
            else:
                # Tell Amazon API Gateway to respond with "500 Internal Server Error".
                raise self.__internal_server_error(event, context)


    def __build_policy_context(self, event, context, request, response, exception):
        # Output from an Amazon API Gateway Lambda authorizer
        # https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-output.html
        #
        #   Notice that you cannot set a JSON object or array as a valid value
        #   of any key in the context map.
        #
        ctx = {}

        if request:
            ctx.update({
                'introspection_request': request.to_json()
            })

        if response:
            ctx.update({
                'introspection_response': response.to_json(),

                # Some pieces of information about the access token in the form of
                # RFC 7662 (OAuth 2.0 Token Introspection), "2.2. Introspection Response".
                'scope':     ' '.join(response.scopes) if response.scopes else None,
                'client_id': self.__extract_client_id(response),
                'sub':       response.subject,
                'exp':       int(response.expiresAt / 1000),

                # 'challenge' here is a value of 'WWW-Authenticate' HTTP header that
                # conforms to RFC 6750 (The OAuth 2.0 Authorization Framework: Bearer
                # Token Usage), "3. The WWW-Authenticate Response Header Field".
                'challenge': response.responseContent if response.action.name != 'OK' else None,

                # Authlete-specific
                'action':        response.action.name,
                'resultMessage': response.resultMessage,
            })

        if exception:
            ctx.update({
                'introspection_exception': self.__exception_to_string(exception)
            })

        # Give subclasses a chance to update the policy context.
        self.update_policy_context(event, context, request, response, exception, ctx)

        return ctx


    def __exception_to_string(self, exception):
        cls    = exception.__class__.__name__
        n_args = len(exception.args)

        if n_args == 0:
            return "{}()".format(cls)
        elif isinstance(exception.args[0], str):
            remaining = '' if n_args == 1 else ', ...'
            return "{}('{}'{})".format(cls, exception.args[0], remaining)
        else:
            return "{}(...)".format(cls)


    def __extract_client_id(self, response):
        if response.clientIdAliasUsed:
            return response.clientIdAlias

        if response.clientId == 0:
            return None

        return str(response.clientId)


    def __allow(self, event, context, request, response):
        # The content of 'context' in the policy.
        ctx = self.__build_policy_context(event, context, request, response, None)

        # Generate an IAM policy that allows the access to the resource.
        # The value of the 'subject' property contained in a response from
        # Authlete's introspection API is the subject of the user who is
        # associated with the access token.
        policy = self.__generate_policy(response.subject, 'Allow', event['methodArn'], ctx)

        # Notify subclasses that the access to the resource is allowed.
        self.__on_allow(event, context, request, response, policy)

        return policy


    def __deny(self, event, context, request, response, exception):
        # The content of 'context' in the policy.
        ctx = self.__build_policy_context(event, context, request, response, exception)

        # Generate an IAM policy that denies the access to the resource.
        # The value of the 'subject' property contained in a response from
        # Authlete's introspection API is the subject of the user who is
        # associated with the access token.
        policy = self.__generate_policy(response.subject, 'Deny', event['methodArn'], ctx)

        # Notify subclasses that the access to the resource is denied.
        self.__on_deny(event, context, request, response, exception, policy)

        return policy


    def __generate_policy(self, subject, effect, resource, context):
        # Lambda authorizer response format
        #   https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html#http-api-lambda-authorizer.payload-format-response

        return {
            'principalId': subject,
            'policyDocument': {
                'Version': '2012-10-17',
                'Statement': [{
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': resource
                }]
            },
            'context': context
        }
