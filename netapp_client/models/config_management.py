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

class ConfigManagement(object):
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
        'min_api_version': 'int'
    }

    attribute_map = {
        'min_api_version': 'minApiVersion'
    }

    def __init__(self, min_api_version=None):  # noqa: E501
        """ConfigManagement - a model defined in Swagger"""  # noqa: E501
        self._min_api_version = None
        self.discriminator = None
        self.min_api_version = min_api_version

    @property
    def min_api_version(self):
        """Gets the min_api_version of this ConfigManagement.  # noqa: E501

        enables or disables earlier API versions  # noqa: E501

        :return: The min_api_version of this ConfigManagement.  # noqa: E501
        :rtype: int
        """
        return self._min_api_version

    @min_api_version.setter
    def min_api_version(self, min_api_version):
        """Sets the min_api_version of this ConfigManagement.

        enables or disables earlier API versions  # noqa: E501

        :param min_api_version: The min_api_version of this ConfigManagement.  # noqa: E501
        :type: int
        """
        if min_api_version is None:
            raise ValueError("Invalid value for `min_api_version`, must not be `None`")  # noqa: E501

        self._min_api_version = min_api_version

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
        if issubclass(ConfigManagement, dict):
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
        if not isinstance(other, ConfigManagement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
