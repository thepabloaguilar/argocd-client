# coding: utf-8

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
from argocd_client.models.protobuf_any import ProtobufAny  # noqa: E501
from argocd_client.rest import ApiException

class TestProtobufAny(unittest.TestCase):
    """ProtobufAny unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProtobufAny
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = argocd_client.models.protobuf_any.ProtobufAny()  # noqa: E501
        if include_optional :
            return ProtobufAny(
                type_url = '0', 
                value = 'YQ=='
            )
        else :
            return ProtobufAny(
        )

    def testProtobufAny(self):
        """Test ProtobufAny"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
