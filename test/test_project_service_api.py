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
from argocd_client.api.project_service_api import ProjectServiceApi  # noqa: E501
from argocd_client.rest import ApiException


class TestProjectServiceApi(unittest.TestCase):
    """ProjectServiceApi unit test stubs"""

    def setUp(self):
        self.api = argocd_client.api.project_service_api.ProjectServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_mixin6(self):
        """Test case for create_mixin6

        Create a new project.  # noqa: E501
        """
        pass

    def test_create_token(self):
        """Test case for create_token

        Create a new project token.  # noqa: E501
        """
        pass

    def test_delete_mixin6(self):
        """Test case for delete_mixin6

        Delete deletes a project  # noqa: E501
        """
        pass

    def test_delete_token(self):
        """Test case for delete_token

        Delete a new project token.  # noqa: E501
        """
        pass

    def test_get_mixin6(self):
        """Test case for get_mixin6

        Get returns a project by name  # noqa: E501
        """
        pass

    def test_get_sync_windows_state(self):
        """Test case for get_sync_windows_state

        GetSchedulesState returns true if there are any active sync syncWindows  # noqa: E501
        """
        pass

    def test_list_events(self):
        """Test case for list_events

        ListEvents returns a list of project events  # noqa: E501
        """
        pass

    def test_list_mixin6(self):
        """Test case for list_mixin6

        List returns list of projects  # noqa: E501
        """
        pass

    def test_update_mixin6(self):
        """Test case for update_mixin6

        Update updates a project  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()