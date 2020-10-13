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


class V1alpha1ResourceDiff(object):
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
        'diff': 'str',
        'group': 'str',
        'hook': 'bool',
        'kind': 'str',
        'live_state': 'str',
        'name': 'str',
        'namespace': 'str',
        'normalized_live_state': 'str',
        'predicted_live_state': 'str',
        'target_state': 'str'
    }

    attribute_map = {
        'diff': 'diff',
        'group': 'group',
        'hook': 'hook',
        'kind': 'kind',
        'live_state': 'liveState',
        'name': 'name',
        'namespace': 'namespace',
        'normalized_live_state': 'normalizedLiveState',
        'predicted_live_state': 'predictedLiveState',
        'target_state': 'targetState'
    }

    def __init__(self, diff=None, group=None, hook=None, kind=None, live_state=None, name=None, namespace=None, normalized_live_state=None, predicted_live_state=None, target_state=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ResourceDiff - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._diff = None
        self._group = None
        self._hook = None
        self._kind = None
        self._live_state = None
        self._name = None
        self._namespace = None
        self._normalized_live_state = None
        self._predicted_live_state = None
        self._target_state = None
        self.discriminator = None

        if diff is not None:
            self.diff = diff
        if group is not None:
            self.group = group
        if hook is not None:
            self.hook = hook
        if kind is not None:
            self.kind = kind
        if live_state is not None:
            self.live_state = live_state
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if normalized_live_state is not None:
            self.normalized_live_state = normalized_live_state
        if predicted_live_state is not None:
            self.predicted_live_state = predicted_live_state
        if target_state is not None:
            self.target_state = target_state

    @property
    def diff(self):
        """Gets the diff of this V1alpha1ResourceDiff.  # noqa: E501


        :return: The diff of this V1alpha1ResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._diff

    @diff.setter
    def diff(self, diff):
        """Sets the diff of this V1alpha1ResourceDiff.


        :param diff: The diff of this V1alpha1ResourceDiff.  # noqa: E501
        :type: str
        """

        self._diff = diff

    @property
    def group(self):
        """Gets the group of this V1alpha1ResourceDiff.  # noqa: E501


        :return: The group of this V1alpha1ResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this V1alpha1ResourceDiff.


        :param group: The group of this V1alpha1ResourceDiff.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def hook(self):
        """Gets the hook of this V1alpha1ResourceDiff.  # noqa: E501


        :return: The hook of this V1alpha1ResourceDiff.  # noqa: E501
        :rtype: bool
        """
        return self._hook

    @hook.setter
    def hook(self, hook):
        """Sets the hook of this V1alpha1ResourceDiff.


        :param hook: The hook of this V1alpha1ResourceDiff.  # noqa: E501
        :type: bool
        """

        self._hook = hook

    @property
    def kind(self):
        """Gets the kind of this V1alpha1ResourceDiff.  # noqa: E501


        :return: The kind of this V1alpha1ResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1alpha1ResourceDiff.


        :param kind: The kind of this V1alpha1ResourceDiff.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def live_state(self):
        """Gets the live_state of this V1alpha1ResourceDiff.  # noqa: E501


        :return: The live_state of this V1alpha1ResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._live_state

    @live_state.setter
    def live_state(self, live_state):
        """Sets the live_state of this V1alpha1ResourceDiff.


        :param live_state: The live_state of this V1alpha1ResourceDiff.  # noqa: E501
        :type: str
        """

        self._live_state = live_state

    @property
    def name(self):
        """Gets the name of this V1alpha1ResourceDiff.  # noqa: E501


        :return: The name of this V1alpha1ResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1ResourceDiff.


        :param name: The name of this V1alpha1ResourceDiff.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this V1alpha1ResourceDiff.  # noqa: E501


        :return: The namespace of this V1alpha1ResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1alpha1ResourceDiff.


        :param namespace: The namespace of this V1alpha1ResourceDiff.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def normalized_live_state(self):
        """Gets the normalized_live_state of this V1alpha1ResourceDiff.  # noqa: E501


        :return: The normalized_live_state of this V1alpha1ResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._normalized_live_state

    @normalized_live_state.setter
    def normalized_live_state(self, normalized_live_state):
        """Sets the normalized_live_state of this V1alpha1ResourceDiff.


        :param normalized_live_state: The normalized_live_state of this V1alpha1ResourceDiff.  # noqa: E501
        :type: str
        """

        self._normalized_live_state = normalized_live_state

    @property
    def predicted_live_state(self):
        """Gets the predicted_live_state of this V1alpha1ResourceDiff.  # noqa: E501


        :return: The predicted_live_state of this V1alpha1ResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._predicted_live_state

    @predicted_live_state.setter
    def predicted_live_state(self, predicted_live_state):
        """Sets the predicted_live_state of this V1alpha1ResourceDiff.


        :param predicted_live_state: The predicted_live_state of this V1alpha1ResourceDiff.  # noqa: E501
        :type: str
        """

        self._predicted_live_state = predicted_live_state

    @property
    def target_state(self):
        """Gets the target_state of this V1alpha1ResourceDiff.  # noqa: E501


        :return: The target_state of this V1alpha1ResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._target_state

    @target_state.setter
    def target_state(self, target_state):
        """Sets the target_state of this V1alpha1ResourceDiff.


        :param target_state: The target_state of this V1alpha1ResourceDiff.  # noqa: E501
        :type: str
        """

        self._target_state = target_state

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
        if not isinstance(other, V1alpha1ResourceDiff):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ResourceDiff):
            return True

        return self.to_dict() != other.to_dict()
