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


import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="authlete",
    version="1.1.3",
    license="Apache License, Version 2.0",
    author="Authlete, Inc.",
    author_email="admin@authlete.com",
    description="Python library for Authlete",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/authlete/authlete-python",
    packages=[
        "authlete.api",
        "authlete.aws",
        "authlete.aws.apigateway",
        "authlete.conf",
        "authlete.dto",
        "authlete.types",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Security",
    ],
    install_requires=[
        "requests",
    ]
)
