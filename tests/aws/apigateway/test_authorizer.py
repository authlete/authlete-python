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


import base64
import datetime
import secrets
import unittest
from cryptography                              import x509
from cryptography.hazmat.primitives            import hashes
from cryptography.hazmat.primitives            import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid                     import NameOID
from authlete.api.authlete_api_impl            import AuthleteApiImpl
from authlete.aws.apigateway.authorizer        import Authorizer
from authlete.conf.authlete_env_configuration  import AuthleteEnvConfiguration
from authlete.dto.token_create_request         import TokenCreateRequest
from authlete.types.grant_type                 import GrantType


class TestAuthorizer(unittest.TestCase):
    CNF = AuthleteEnvConfiguration()
    API = AuthleteApiImpl(CNF) if CNF.baseUrl and CNF.serviceApiKey and CNF.serviceApiSecret else None
    RSN = 'Configuration for Authlete API is not available'
    ARN = 'arn:dummy-partition:execute-api:dummy-region:dummy-account-id:dummy-api-id/dummy-stage/GET/dummy_path'


    def api(self):
        # Authlete API
        return self.__class__.API


    def authorizer(self, verbose=False, policy=True):
        # If verbose output is needed, give 'verbose=True' to the constructor.
        return Authorizer(verbose=verbose, policy=policy)


    def get_client(self):
        # Get a client that belongs to the service.
        return self.api().getClientList(start=0, end=1).clients[0]


    def create_token(self, certificate=None, extra=None):
        nameAndValues = {
            'grantType': GrantType.AUTHORIZATION_CODE,
            'clientId':  self.get_client().clientId,
            'subject':   'authlete-python-test',
            'scopes':    ['openid']
        }

        if certificate:
            nameAndValues.update({
                'certificateThumbprint': self.compute_certificate_thumbprint(certificate)
            })

        if extra:
            nameAndValues.update(extra)

        # Create an access token.
        return self.api().tokenCreate(TokenCreateRequest(nameAndValues)).accessToken


    def delete_token(self, token):
        self.api().tokenDelete(token)


    def create_event(self, token=None, certificate=None, payloadType='REQUEST', payloadVersion=2):
        # Input to an Amazon API Gateway Lambda authorizer
        # https://docs.amazonaws.cn/en_us/apigateway/latest/developerguide/api-gateway-lambda-authorizer-input.html
        event = {
            'type':      payloadType,
            'methodArn': self.__class__.ARN
        }

        if token:
            value = 'Bearer {}'.format(token)
            if payloadType == 'TOKEN':
                event.update({
                    'authorizationToken': value
                })
            else:
                event.update({
                    'headers': {
                        'authorization': value
                    }
                })

        if certificate:
            dict_name = 'identity' if payloadVersion == 1 else 'authentication'
            event.update({
                'requestContext': {
                    dict_name: {
                        'clientCert': {
                            'clientCertPem': self.certificate_to_pem(certificate)
                        }
                    }
                }
            })

        return event


    def create_certificate(self):
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

        name = 'client.example.com'
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, name)
        ])

        # Create a self-signed certificate.
        certificate = x509.CertificateBuilder().subject_name(
            subject
        ).issuer_name(
            issuer
        ).public_key(
            key.public_key()
        ).serial_number(
            x509.random_serial_number()
        ).not_valid_before(
            datetime.datetime.utcnow()
        ).not_valid_after(
            datetime.datetime.utcnow() + datetime.timedelta(days=10)
        ).add_extension(
            x509.SubjectAlternativeName([
                x509.DNSName(name)
            ]),
            critical=False
        ).sign(key, hashes.SHA256())

        return certificate


    def compute_certificate_thumbprint(self, certificate):
        # base64url-encoded SHA-256 hash. See RFC 8705 Section 3.1.
        fingerprint = certificate.fingerprint(hashes.SHA256())
        return self.base64url(fingerprint)


    def base64url(self, input):
        return base64.urlsafe_b64encode(input).decode('utf-8').rstrip('=')


    def certificate_to_pem(self, certificate):
        return certificate.public_bytes(serialization.Encoding.PEM).decode('utf-8')


    def assert_effect(self, policy, effect):
        actual = policy['policyDocument']['Statement'][0]['Effect']
        self.assertEqual(actual, effect)


    def assert_allow(self, policy):
        self.assert_effect(policy, 'Allow')


    def assert_deny(self, policy):
        self.assert_effect(policy, 'Deny')


    def assert_unauthorized(self, exception):
        self.assertEqual(exception.args[0], 'Unauthorized')


    def fail_unauthorized(self):
        self.fail('Exception with "Unauthorized" should be raised.')


    @unittest.skipUnless(API, RSN)
    def test_no_access_token(self):
        event = self.create_event()

        # Because 'event' contains no access token, handle() method
        # returns an IAM policy that denies the resource access.
        policy = self.authorizer().handle(event, None)

        self.assert_deny(policy)


    @unittest.skipUnless(API, RSN)
    def test_invalid_access_token_1(self):
        event = self.create_event('invalid-access-token')

        try:
            # Because 'event' contains no access token, handle() method
            # will throw an exception that represents 'Unauthorized'.
            self.authorizer(policy=False).handle(event, None)
            self.fail_unauthorized()
        except Exception as exception:
            self.assert_unauthorized(exception)


    @unittest.skipUnless(API, RSN)
    def test_invalid_access_token_2(self):
        event = self.create_event('invalid-access-token')

        # Because 'event' contains no access token, handle() method
        # returns an IAM policy that denies the resource access.
        policy = self.authorizer().handle(event, None)

        self.assert_deny(policy)


    @unittest.skipUnless(API, RSN)
    def test_payload_type_request(self):
        token = self.create_token()
        event = self.create_event(token)

        policy = self.authorizer().handle(event, None)

        self.delete_token(token)
        self.assert_allow(policy)


    @unittest.skipUnless(API, RSN)
    def test_payload_type_token(self):
        token = self.create_token()
        event = self.create_event(token, payloadType='TOKEN')

        policy = self.authorizer().handle(event, None)

        self.delete_token(token)
        self.assert_allow(policy)


    @unittest.skipUnless(API, RSN)
    def test_insufficient_scope_1(self):
        token = self.create_token()
        event = self.create_event(token)

        # A function to generate a list of scopes that are required to
        # access the resource.
        scopes_determiner = lambda evt, ctx, method, path : ['__dummy_scope__']

        # Because the scope '__dummy_scope__' contained in the array returned
        # by 'scopes_determiner' is not covered by the access token, handle()
        # method returns an IAM policy that denies the resource access.
        policy = self.authorizer().handle(event, None, scopes_determiner)

        self.delete_token(token)
        self.assert_deny(policy)


    @unittest.skipUnless(API, RSN)
    def test_insufficient_scope_2(self):
        token = self.create_token()
        event = self.create_event(token)

        class CustomAuthorizer(Authorizer):
            def __init__(self, api=None, verbose=False):
                super().__init__(api, verbose)

            def determine_scopes(self, event, context, method, path):
                return ['__dummy_scope_2__']

        # Because the scope '__dummy_scope_2__' contained in the array returned
        # by 'determine_scopes' in CustomAuthorizer is not covered by the access
        # token, handle() method returns an IAM policy that denies the resource
        # access.
        policy = CustomAuthorizer().handle(event, None)

        self.delete_token(token)
        self.assert_deny(policy)


    @unittest.skipUnless(API, RSN)
    def test_certificate_binding_allow(self):
        certificate = self.create_certificate()
        token = self.create_token(certificate)
        event = self.create_event(token, certificate)

        # Make the authorizer introspect the access token.
        policy = self.authorizer().handle(event, None)

        self.delete_token(token)
        self.assert_allow(policy)


    @unittest.skipUnless(API, RSN)
    def test_certificate_binding_invalid_1(self):
        certificate = self.create_certificate()
        token = self.create_token(extra = {
            # Invalid thumbprint that is to be bound to the access token.
            'certificateThumbprint': secrets.token_urlsafe(32)
        })
        event = self.create_event(token, certificate)

        try:
            # Because the certificate thumbprint bound to the access token is
            # different from that of the certificate in the 'event', handle()
            # method will throw an exception that represents 'Unauthorized'.
            self.authorizer(policy=False).handle(event, None)
            self.fail_unauthorized()
        except Exception as exception:
            self.assert_unauthorized(exception)

        self.delete_token(token)


    @unittest.skipUnless(API, RSN)
    def test_certificate_binding_invalid_2(self):
        certificate = self.create_certificate()
        token = self.create_token(extra = {
            # Invalid thumbprint that is to be bound to the access token.
            'certificateThumbprint': secrets.token_urlsafe(32)
        })
        event = self.create_event(token, certificate)

        # Because the certificate thumbprint bound to the access token is
        # different from that of the certificate in the 'event', handle()
        # method will return an IAM policy that denies the resource access.
        policy = self.authorizer().handle(event, None)

        self.delete_token(token)
        self.assert_deny(policy)


    @unittest.skipUnless(API, RSN)
    def test_certificate_binding_payload_version_1(self):
        certificate = self.create_certificate()
        token = self.create_token(certificate)
        event = self.create_event(token, certificate, payloadVersion=1)

        # Make the authorizer introspect the access token.
        policy = self.authorizer().handle(event, None)

        self.delete_token(token)
        self.assert_allow(policy)


    @unittest.skipUnless(API, RSN)
    def test_certificate_binding_no_certificate_1(self):
        certificate = self.create_certificate()
        token = self.create_token(certificate)
        event = self.create_event(token)

        try:
            # Because 'event' contains no client certificate, handle() method
            # will throw an exception that represents 'Unauthorized'.
            self.authorizer(policy=False).handle(event, None)
            self.fail_unauthorized()
        except Exception as exception:
            self.assert_unauthorized(exception)

        self.delete_token(token)


    @unittest.skipUnless(API, RSN)
    def test_certificate_binding_no_certificate_2(self):
        certificate = self.create_certificate()
        token = self.create_token(certificate)
        event = self.create_event(token)

        # Because 'event' contains no client certificate, handle() method
        # will return an IAM policy that denies the resource access.
        policy = self.authorizer().handle(event, None)

        self.delete_token(token)
        self.assert_deny(policy)


    @unittest.skipUnless(API, RSN)
    def test_hooks_1(self):
        token = self.create_token()
        event = self.create_event(token)

        class CustomAuthorizer(Authorizer):
            def __init__(self, api=None, verbose=False):
                super().__init__(api, verbose)
                self.records = {}

            def on_enter(self, event, context):
                self.records['on_enter'] = True

            def on_introspection(self, event, context, request, response):
                self.records['on_introspection'] = True

            def on_allow(self, event, context, request, response, policy):
                self.records['on_allow'] = True

            def update_policy_context(self, event, context, request, response, exception, ctx):
                self.records['update_policy_context'] = True
                ctx['hooked'] = True

        authorizer = CustomAuthorizer()
        policy     = authorizer.handle(event, None)
        records    = authorizer.records

        self.delete_token(token)
        self.assert_allow(policy)

        self.assertTrue(records.get('on_enter'))
        self.assertTrue(records.get('on_introspection'))
        self.assertTrue(records.get('on_allow'))
        self.assertTrue(records.get('update_policy_context'))

        context = policy['context']
        self.assertTrue(context.get('hooked'))
        self.assertIsNotNone(context.get('introspection_request'))
        self.assertIsNotNone(context.get('introspection_response'))
