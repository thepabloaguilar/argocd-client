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


class ClusterHelp(object):
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
        'chat_text': 'str',
        'chat_url': 'str'
    }

    attribute_map = {
        'chat_text': 'chatText',
        'chat_url': 'chatUrl'
    }

    def __init__(self, chat_text=None, chat_url=None, local_vars_configuration=None):  # noqa: E501
        """ClusterHelp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._chat_text = None
        self._chat_url = None
        self.discriminator = None

        if chat_text is not None:
            self.chat_text = chat_text
        if chat_url is not None:
            self.chat_url = chat_url

    @property
    def chat_text(self):
        """Gets the chat_text of this ClusterHelp.  # noqa: E501


        :return: The chat_text of this ClusterHelp.  # noqa: E501
        :rtype: str
        """
        return self._chat_text

    @chat_text.setter
    def chat_text(self, chat_text):
        """Sets the chat_text of this ClusterHelp.


        :param chat_text: The chat_text of this ClusterHelp.  # noqa: E501
        :type: str
        """

        self._chat_text = chat_text

    @property
    def chat_url(self):
        """Gets the chat_url of this ClusterHelp.  # noqa: E501


        :return: The chat_url of this ClusterHelp.  # noqa: E501
        :rtype: str
        """
        return self._chat_url

    @chat_url.setter
    def chat_url(self, chat_url):
        """Sets the chat_url of this ClusterHelp.


        :param chat_url: The chat_url of this ClusterHelp.  # noqa: E501
        :type: str
        """

        self._chat_url = chat_url

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
        if not isinstance(other, ClusterHelp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterHelp):
            return True

        return self.to_dict() != other.to_dict()
