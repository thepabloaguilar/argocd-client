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


class V1alpha1ApplicationSpec(object):
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
        'destination': 'V1alpha1ApplicationDestination',
        'ignore_differences': 'list[V1alpha1ResourceIgnoreDifferences]',
        'info': 'list[V1alpha1Info]',
        'project': 'str',
        'revision_history_limit': 'str',
        'source': 'V1alpha1ApplicationSource',
        'sync_policy': 'V1alpha1SyncPolicy'
    }

    attribute_map = {
        'destination': 'destination',
        'ignore_differences': 'ignoreDifferences',
        'info': 'info',
        'project': 'project',
        'revision_history_limit': 'revisionHistoryLimit',
        'source': 'source',
        'sync_policy': 'syncPolicy'
    }

    def __init__(self, destination=None, ignore_differences=None, info=None, project=None, revision_history_limit=None, source=None, sync_policy=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ApplicationSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._destination = None
        self._ignore_differences = None
        self._info = None
        self._project = None
        self._revision_history_limit = None
        self._source = None
        self._sync_policy = None
        self.discriminator = None

        if destination is not None:
            self.destination = destination
        if ignore_differences is not None:
            self.ignore_differences = ignore_differences
        if info is not None:
            self.info = info
        if project is not None:
            self.project = project
        if revision_history_limit is not None:
            self.revision_history_limit = revision_history_limit
        if source is not None:
            self.source = source
        if sync_policy is not None:
            self.sync_policy = sync_policy

    @property
    def destination(self):
        """Gets the destination of this V1alpha1ApplicationSpec.  # noqa: E501


        :return: The destination of this V1alpha1ApplicationSpec.  # noqa: E501
        :rtype: V1alpha1ApplicationDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this V1alpha1ApplicationSpec.


        :param destination: The destination of this V1alpha1ApplicationSpec.  # noqa: E501
        :type: V1alpha1ApplicationDestination
        """

        self._destination = destination

    @property
    def ignore_differences(self):
        """Gets the ignore_differences of this V1alpha1ApplicationSpec.  # noqa: E501


        :return: The ignore_differences of this V1alpha1ApplicationSpec.  # noqa: E501
        :rtype: list[V1alpha1ResourceIgnoreDifferences]
        """
        return self._ignore_differences

    @ignore_differences.setter
    def ignore_differences(self, ignore_differences):
        """Sets the ignore_differences of this V1alpha1ApplicationSpec.


        :param ignore_differences: The ignore_differences of this V1alpha1ApplicationSpec.  # noqa: E501
        :type: list[V1alpha1ResourceIgnoreDifferences]
        """

        self._ignore_differences = ignore_differences

    @property
    def info(self):
        """Gets the info of this V1alpha1ApplicationSpec.  # noqa: E501


        :return: The info of this V1alpha1ApplicationSpec.  # noqa: E501
        :rtype: list[V1alpha1Info]
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this V1alpha1ApplicationSpec.


        :param info: The info of this V1alpha1ApplicationSpec.  # noqa: E501
        :type: list[V1alpha1Info]
        """

        self._info = info

    @property
    def project(self):
        """Gets the project of this V1alpha1ApplicationSpec.  # noqa: E501

        Project is a application project name. Empty name means that application belongs to 'default' project.  # noqa: E501

        :return: The project of this V1alpha1ApplicationSpec.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this V1alpha1ApplicationSpec.

        Project is a application project name. Empty name means that application belongs to 'default' project.  # noqa: E501

        :param project: The project of this V1alpha1ApplicationSpec.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def revision_history_limit(self):
        """Gets the revision_history_limit of this V1alpha1ApplicationSpec.  # noqa: E501

        This limits this number of items kept in the apps revision history. This should only be changed in exceptional circumstances. Setting to zero will store no history. This will reduce storage used. Increasing will increase the space used to store the history, so we do not recommend increasing it. Default is 10.  # noqa: E501

        :return: The revision_history_limit of this V1alpha1ApplicationSpec.  # noqa: E501
        :rtype: str
        """
        return self._revision_history_limit

    @revision_history_limit.setter
    def revision_history_limit(self, revision_history_limit):
        """Sets the revision_history_limit of this V1alpha1ApplicationSpec.

        This limits this number of items kept in the apps revision history. This should only be changed in exceptional circumstances. Setting to zero will store no history. This will reduce storage used. Increasing will increase the space used to store the history, so we do not recommend increasing it. Default is 10.  # noqa: E501

        :param revision_history_limit: The revision_history_limit of this V1alpha1ApplicationSpec.  # noqa: E501
        :type: str
        """

        self._revision_history_limit = revision_history_limit

    @property
    def source(self):
        """Gets the source of this V1alpha1ApplicationSpec.  # noqa: E501


        :return: The source of this V1alpha1ApplicationSpec.  # noqa: E501
        :rtype: V1alpha1ApplicationSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this V1alpha1ApplicationSpec.


        :param source: The source of this V1alpha1ApplicationSpec.  # noqa: E501
        :type: V1alpha1ApplicationSource
        """

        self._source = source

    @property
    def sync_policy(self):
        """Gets the sync_policy of this V1alpha1ApplicationSpec.  # noqa: E501


        :return: The sync_policy of this V1alpha1ApplicationSpec.  # noqa: E501
        :rtype: V1alpha1SyncPolicy
        """
        return self._sync_policy

    @sync_policy.setter
    def sync_policy(self, sync_policy):
        """Sets the sync_policy of this V1alpha1ApplicationSpec.


        :param sync_policy: The sync_policy of this V1alpha1ApplicationSpec.  # noqa: E501
        :type: V1alpha1SyncPolicy
        """

        self._sync_policy = sync_policy

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
        if not isinstance(other, V1alpha1ApplicationSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ApplicationSpec):
            return True

        return self.to_dict() != other.to_dict()
