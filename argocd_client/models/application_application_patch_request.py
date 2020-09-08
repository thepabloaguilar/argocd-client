# coding: utf-8

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


class ApplicationApplicationPatchRequest(object):
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
        'name': 'str',
        'patch': 'str',
        'patch_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'patch': 'patch',
        'patch_type': 'patchType'
    }

    def __init__(self, name=None, patch=None, patch_type=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationApplicationPatchRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._patch = None
        self._patch_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if patch is not None:
            self.patch = patch
        if patch_type is not None:
            self.patch_type = patch_type

    @property
    def name(self):
        """Gets the name of this ApplicationApplicationPatchRequest.  # noqa: E501


        :return: The name of this ApplicationApplicationPatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationApplicationPatchRequest.


        :param name: The name of this ApplicationApplicationPatchRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def patch(self):
        """Gets the patch of this ApplicationApplicationPatchRequest.  # noqa: E501


        :return: The patch of this ApplicationApplicationPatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._patch

    @patch.setter
    def patch(self, patch):
        """Sets the patch of this ApplicationApplicationPatchRequest.


        :param patch: The patch of this ApplicationApplicationPatchRequest.  # noqa: E501
        :type: str
        """

        self._patch = patch

    @property
    def patch_type(self):
        """Gets the patch_type of this ApplicationApplicationPatchRequest.  # noqa: E501


        :return: The patch_type of this ApplicationApplicationPatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._patch_type

    @patch_type.setter
    def patch_type(self, patch_type):
        """Sets the patch_type of this ApplicationApplicationPatchRequest.


        :param patch_type: The patch_type of this ApplicationApplicationPatchRequest.  # noqa: E501
        :type: str
        """

        self._patch_type = patch_type

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
        if not isinstance(other, ApplicationApplicationPatchRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationApplicationPatchRequest):
            return True

        return self.to_dict() != other.to_dict()