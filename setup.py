# Copyright 2019-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from setuptools import find_namespace_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("src/braket/ocean_plugin/_version.py") as f:
    version = f.readlines()[-1].split()[-1].strip("\"'")

setup(
    name="amazon-braket-ocean-plugin",
    version=version,
    license="Apache License 2.0",
    python_requires=">= 3.7",
    packages=find_namespace_packages(where="src", exclude=("test",)),
    package_dir={"": "src"},
    install_requires=["amazon-braket-sdk", "dimod>=0.8.13", "boto3", "boltons", "jsonref"],
    extras_require={
        "test": [
            "black",
            "flake8",
            "isort",
            "pre-commit",
            "pylint",
            "pytest",
            "pytest-cov",
            "pytest-rerunfailures",
            "pytest-xdist",
            "sphinx",
            "sphinx-rtd-theme",
            "sphinxcontrib-apidoc",
            "tox",
            "dwave-ocean-sdk",
        ]
    },
    url="https://github.com/aws/amazon-braket-ocean-plugin-python",
    author="Amazon Web Services",
    description=(
        "An open source framework for interacting with D-Wave's Ocean library through Amazon Braket"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Amazon AWS Quantum",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
