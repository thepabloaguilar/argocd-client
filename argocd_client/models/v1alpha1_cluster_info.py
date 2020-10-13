# coding: utf-8
# Copyright (c) 2020, Globo (https://github.com/globocom)
# License: BSD-3-Clause

"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argocd_client.configuration import Configuration


class V1alpha1ClusterInfo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'applications_count': 'str',
        'cache_info': 'V1alpha1ClusterCacheInfo',
        'connection_state': 'V1alpha1ConnectionState',
        'server_version': 'str'
    }

    attribute_map = {
        'applications_count': 'applicationsCount',
        'cache_info': 'cacheInfo',
        'connection_state': 'connectionState',
        'server_version': 'serverVersion'
    }

    def __init__(self, applications_count=None, cache_info=None, connection_state=None, server_version=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ClusterInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._applications_count = None
        self._cache_info = None
        self._connection_state = None
        self._server_version = None
        self.discriminator = None

        if applications_count is not None:
            self.applications_count = applications_count
        if cache_info is not None:
            self.cache_info = cache_info
        if connection_state is not None:
            self.connection_state = connection_state
        if server_version is not None:
            self.server_version = server_version

    @property
    def applications_count(self):
        """Gets the applications_count of this V1alpha1ClusterInfo.  # noqa: E501


        :return: The applications_count of this V1alpha1ClusterInfo.  # noqa: E501
        :rtype: str
        """
        return self._applications_count

    @applications_count.setter
    def applications_count(self, applications_count):
        """Sets the applications_count of this V1alpha1ClusterInfo.


        :param applications_count: The applications_count of this V1alpha1ClusterInfo.  # noqa: E501
        :type: str
        """

        self._applications_count = applications_count

    @property
    def cache_info(self):
        """Gets the cache_info of this V1alpha1ClusterInfo.  # noqa: E501


        :return: The cache_info of this V1alpha1ClusterInfo.  # noqa: E501
        :rtype: V1alpha1ClusterCacheInfo
        """
        return self._cache_info

    @cache_info.setter
    def cache_info(self, cache_info):
        """Sets the cache_info of this V1alpha1ClusterInfo.


        :param cache_info: The cache_info of this V1alpha1ClusterInfo.  # noqa: E501
        :type: V1alpha1ClusterCacheInfo
        """

        self._cache_info = cache_info

    @property
    def connection_state(self):
        """Gets the connection_state of this V1alpha1ClusterInfo.  # noqa: E501


        :return: The connection_state of this V1alpha1ClusterInfo.  # noqa: E501
        :rtype: V1alpha1ConnectionState
        """
        return self._connection_state

    @connection_state.setter
    def connection_state(self, connection_state):
        """Sets the connection_state of this V1alpha1ClusterInfo.


        :param connection_state: The connection_state of this V1alpha1ClusterInfo.  # noqa: E501
        :type: V1alpha1ConnectionState
        """

        self._connection_state = connection_state

    @property
    def server_version(self):
        """Gets the server_version of this V1alpha1ClusterInfo.  # noqa: E501


        :return: The server_version of this V1alpha1ClusterInfo.  # noqa: E501
        :rtype: str
        """
        return self._server_version

    @server_version.setter
    def server_version(self, server_version):
        """Sets the server_version of this V1alpha1ClusterInfo.


        :param server_version: The server_version of this V1alpha1ClusterInfo.  # noqa: E501
        :type: str
        """

        self._server_version = server_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1ClusterInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ClusterInfo):
            return True

        return self.to_dict() != other.to_dict()
