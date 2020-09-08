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
from argocd_client.api.account_service_api import AccountServiceApi  # noqa: E501
from argocd_client.rest import ApiException


class TestAccountServiceApi(unittest.TestCase):
    """AccountServiceApi unit test stubs"""

    def setUp(self):
        self.api = argocd_client.api.account_service_api.AccountServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_can_i(self):
        """Test case for can_i

        """
        pass

    def test_create_token_mixin10(self):
        """Test case for create_token_mixin10

        """
        pass

    def test_delete_token_mixin10(self):
        """Test case for delete_token_mixin10

        """
        pass

    def test_get_account(self):
        """Test case for get_account

        """
        pass

    def test_list_accounts(self):
        """Test case for list_accounts

        """
        pass

    def test_update_password(self):
        """Test case for update_password

        UpdatePassword updates an account's password to a new value  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()