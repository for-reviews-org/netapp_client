# coding: utf-8

"""
    StorageGRID Management API v3

    REST API for managing StorageGRID deployments. Copyright (c) 2021 NetApp, Inc. All Rights Reserved  # noqa: E501

    OpenAPI spec version: 3.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PatchGroupRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'display_name': 'str',
        'management_read_only': 'bool',
        'policies': 'Policies'
    }

    attribute_map = {
        'display_name': 'displayName',
        'management_read_only': 'managementReadOnly',
        'policies': 'policies'
    }

    def __init__(self, display_name=None, management_read_only=None, policies=None):  # noqa: E501
        """PatchGroupRequest - a model defined in Swagger"""  # noqa: E501
        self._display_name = None
        self._management_read_only = None
        self._policies = None
        self.discriminator = None
        if display_name is not None:
            self.display_name = display_name
        if management_read_only is not None:
            self.management_read_only = management_read_only
        if policies is not None:
            self.policies = policies

    @property
    def display_name(self):
        """Gets the display_name of this PatchGroupRequest.  # noqa: E501

        the human-readable name for the Group (required for local Groups and imported automatically for federated Groups)  # noqa: E501

        :return: The display_name of this PatchGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PatchGroupRequest.

        the human-readable name for the Group (required for local Groups and imported automatically for federated Groups)  # noqa: E501

        :param display_name: The display_name of this PatchGroupRequest.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def management_read_only(self):
        """Gets the management_read_only of this PatchGroupRequest.  # noqa: E501

        Whether the group is read-only. Users can view settings and features but cannot make changes or perform operations. Local users can change their passwords.  # noqa: E501

        :return: The management_read_only of this PatchGroupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._management_read_only

    @management_read_only.setter
    def management_read_only(self, management_read_only):
        """Sets the management_read_only of this PatchGroupRequest.

        Whether the group is read-only. Users can view settings and features but cannot make changes or perform operations. Local users can change their passwords.  # noqa: E501

        :param management_read_only: The management_read_only of this PatchGroupRequest.  # noqa: E501
        :type: bool
        """

        self._management_read_only = management_read_only

    @property
    def policies(self):
        """Gets the policies of this PatchGroupRequest.  # noqa: E501


        :return: The policies of this PatchGroupRequest.  # noqa: E501
        :rtype: Policies
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this PatchGroupRequest.


        :param policies: The policies of this PatchGroupRequest.  # noqa: E501
        :type: Policies
        """

        self._policies = policies

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PatchGroupRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PatchGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
