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


class RepositoryKsonnetEnvironment(object):
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
        'destination': 'RepositoryKsonnetEnvironmentDestination',
        'k8s_version': 'str',
        'name': 'str'
    }

    attribute_map = {
        'destination': 'destination',
        'k8s_version': 'k8sVersion',
        'name': 'name'
    }

    def __init__(self, destination=None, k8s_version=None, name=None, local_vars_configuration=None):  # noqa: E501
        """RepositoryKsonnetEnvironment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._destination = None
        self._k8s_version = None
        self._name = None
        self.discriminator = None

        if destination is not None:
            self.destination = destination
        if k8s_version is not None:
            self.k8s_version = k8s_version
        if name is not None:
            self.name = name

    @property
    def destination(self):
        """Gets the destination of this RepositoryKsonnetEnvironment.  # noqa: E501


        :return: The destination of this RepositoryKsonnetEnvironment.  # noqa: E501
        :rtype: RepositoryKsonnetEnvironmentDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this RepositoryKsonnetEnvironment.


        :param destination: The destination of this RepositoryKsonnetEnvironment.  # noqa: E501
        :type: RepositoryKsonnetEnvironmentDestination
        """

        self._destination = destination

    @property
    def k8s_version(self):
        """Gets the k8s_version of this RepositoryKsonnetEnvironment.  # noqa: E501

        KubernetesVersion is the kubernetes version the targeted cluster is running on.  # noqa: E501

        :return: The k8s_version of this RepositoryKsonnetEnvironment.  # noqa: E501
        :rtype: str
        """
        return self._k8s_version

    @k8s_version.setter
    def k8s_version(self, k8s_version):
        """Sets the k8s_version of this RepositoryKsonnetEnvironment.

        KubernetesVersion is the kubernetes version the targeted cluster is running on.  # noqa: E501

        :param k8s_version: The k8s_version of this RepositoryKsonnetEnvironment.  # noqa: E501
        :type: str
        """

        self._k8s_version = k8s_version

    @property
    def name(self):
        """Gets the name of this RepositoryKsonnetEnvironment.  # noqa: E501


        :return: The name of this RepositoryKsonnetEnvironment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RepositoryKsonnetEnvironment.


        :param name: The name of this RepositoryKsonnetEnvironment.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, RepositoryKsonnetEnvironment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepositoryKsonnetEnvironment):
            return True

        return self.to_dict() != other.to_dict()
