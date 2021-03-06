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


class ApplicationApplicationRollbackRequest(object):
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
        'dry_run': 'bool',
        'id': 'str',
        'name': 'str',
        'prune': 'bool'
    }

    attribute_map = {
        'dry_run': 'dryRun',
        'id': 'id',
        'name': 'name',
        'prune': 'prune'
    }

    def __init__(self, dry_run=None, id=None, name=None, prune=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationApplicationRollbackRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dry_run = None
        self._id = None
        self._name = None
        self._prune = None
        self.discriminator = None

        if dry_run is not None:
            self.dry_run = dry_run
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if prune is not None:
            self.prune = prune

    @property
    def dry_run(self):
        """Gets the dry_run of this ApplicationApplicationRollbackRequest.  # noqa: E501


        :return: The dry_run of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this ApplicationApplicationRollbackRequest.


        :param dry_run: The dry_run of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

    @property
    def id(self):
        """Gets the id of this ApplicationApplicationRollbackRequest.  # noqa: E501


        :return: The id of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplicationApplicationRollbackRequest.


        :param id: The id of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApplicationApplicationRollbackRequest.  # noqa: E501


        :return: The name of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationApplicationRollbackRequest.


        :param name: The name of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def prune(self):
        """Gets the prune of this ApplicationApplicationRollbackRequest.  # noqa: E501


        :return: The prune of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :rtype: bool
        """
        return self._prune

    @prune.setter
    def prune(self, prune):
        """Sets the prune of this ApplicationApplicationRollbackRequest.


        :param prune: The prune of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :type: bool
        """

        self._prune = prune

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
        if not isinstance(other, ApplicationApplicationRollbackRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationApplicationRollbackRequest):
            return True

        return self.to_dict() != other.to_dict()
