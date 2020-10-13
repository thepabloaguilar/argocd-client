# coding: utf-8
# Copyright (c) 2020, Globo (https://github.com/globocom)
# License: BSD-3-Clause

"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import argocd_client
from argocd_client.models.v1alpha1_repository import V1alpha1Repository  # noqa: E501
from argocd_client.rest import ApiException

class TestV1alpha1Repository(unittest.TestCase):
    """V1alpha1Repository unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1Repository
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = argocd_client.models.v1alpha1_repository.V1alpha1Repository()  # noqa: E501
        if include_optional :
            return V1alpha1Repository(
                connection_state = argocd_client.models.connection_state_contains_information_about_remote_resource_connection_state.ConnectionState contains information about remote resource connection state(
                    attempted_at = argocd_client.models.v1_time.v1Time(
                        nanos = 56, 
                        seconds = '0', ), 
                    message = '0', 
                    status = '0', ), 
                enable_lfs = True, 
                inherited_creds = True, 
                insecure = True, 
                insecure_ignore_host_key = True, 
                name = '0', 
                password = '0', 
                repo = '0', 
                ssh_private_key = '0', 
                tls_client_cert_data = '0', 
                tls_client_cert_key = '0', 
                type = '0', 
                username = '0'
            )
        else :
            return V1alpha1Repository(
        )

    def testV1alpha1Repository(self):
        """Test V1alpha1Repository"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
