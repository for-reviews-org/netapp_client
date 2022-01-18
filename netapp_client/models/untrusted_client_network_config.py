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

class UntrustedClientNetworkConfig(object):
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
        'default': 'str',
        'untrusted_nodes': 'list[NodeId]'
    }

    attribute_map = {
        'default': 'default',
        'untrusted_nodes': 'untrustedNodes'
    }

    def __init__(self, default='trusted', untrusted_nodes=None):  # noqa: E501
        """UntrustedClientNetworkConfig - a model defined in Swagger"""  # noqa: E501
        self._default = None
        self._untrusted_nodes = None
        self.discriminator = None
        if default is not None:
            self.default = default
        if untrusted_nodes is not None:
            self.untrusted_nodes = untrusted_nodes

    @property
    def default(self):
        """Gets the default of this UntrustedClientNetworkConfig.  # noqa: E501

        The default setting for the Client Network on nodes added to the grid  # noqa: E501

        :return: The default of this UntrustedClientNetworkConfig.  # noqa: E501
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this UntrustedClientNetworkConfig.

        The default setting for the Client Network on nodes added to the grid  # noqa: E501

        :param default: The default of this UntrustedClientNetworkConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["trusted", "untrusted"]  # noqa: E501
        if default not in allowed_values:
            raise ValueError(
                "Invalid value for `default` ({0}), must be one of {1}"  # noqa: E501
                .format(default, allowed_values)
            )

        self._default = default

    @property
    def untrusted_nodes(self):
        """Gets the untrusted_nodes of this UntrustedClientNetworkConfig.  # noqa: E501

        A list of the UUIDs of nodes whose Client Network is untrusted  # noqa: E501

        :return: The untrusted_nodes of this UntrustedClientNetworkConfig.  # noqa: E501
        :rtype: list[NodeId]
        """
        return self._untrusted_nodes

    @untrusted_nodes.setter
    def untrusted_nodes(self, untrusted_nodes):
        """Sets the untrusted_nodes of this UntrustedClientNetworkConfig.

        A list of the UUIDs of nodes whose Client Network is untrusted  # noqa: E501

        :param untrusted_nodes: The untrusted_nodes of this UntrustedClientNetworkConfig.  # noqa: E501
        :type: list[NodeId]
        """

        self._untrusted_nodes = untrusted_nodes

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
        if issubclass(UntrustedClientNetworkConfig, dict):
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
        if not isinstance(other, UntrustedClientNetworkConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other