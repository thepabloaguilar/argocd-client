# coding: utf-8

"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import argocd_client
from argocd_client.api.version_service_api import VersionServiceApi  # noqa: E501
from argocd_client.rest import ApiException


class TestVersionServiceApi(unittest.TestCase):
    """VersionServiceApi unit test stubs"""

    def setUp(self):
        self.api = argocd_client.api.version_service_api.VersionServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_version(self):
        """Test case for version

        Version returns version information of the API server  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
