#
# Copyright (C) 2019 Authlete, Inc.
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


class AuthleteApiException(Exception):
    def __init__(self, url, queryParams, requestBody, \
        message=None, cause=None, response=None):
        self._url         = url
        self._queryParams = queryParams
        self._requestBody = requestBody
        self._message     = message
        self._cause       = cause
        self._response    = response

        super().__init__(message)


    @property
    def url(self):
        """Get the url of the Authlete API.

        Returns:
            str : The URL of the Authlete API.
        """
        return self._url


    @property
    def queryParams(self):
        """Get the query parameters of the request.

        Returns:
            dict : The query parameters. May be None.
        """
        return self._queryParams


    @property
    def requestBody(self):
        """Get the HTTP message body of the request.

        Returns:
            str : The request body. May be None.
        """
        return self._requestBody


    @property
    def message(self):
        """Get the error message.

        Returns:
            str : The error message.
        """
        return self._message


    @property
    def cause(self):
        """Get the cause of this exception.

        Returns:
            requests.exceptions.RequestException : The cause of this exception. May be None.
        """
        return self._cause


    @property
    def response(self):
        """Get the response from the API.

        Returns:
            requests.Response : The response from the API. May be None.
        """
        return self._response
