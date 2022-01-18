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

class GridNetworkListAlert(object):
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
        'severity': 'str',
        'text': 'str',
        'key': 'str'
    }

    attribute_map = {
        'severity': 'severity',
        'text': 'text',
        'key': 'key'
    }

    def __init__(self, severity=None, text=None, key=None):  # noqa: E501
        """GridNetworkListAlert - a model defined in Swagger"""  # noqa: E501
        self._severity = None
        self._text = None
        self._key = None
        self.discriminator = None
        if severity is not None:
            self.severity = severity
        if text is not None:
            self.text = text
        if key is not None:
            self.key = key

    @property
    def severity(self):
        """Gets the severity of this GridNetworkListAlert.  # noqa: E501

        type of alert  # noqa: E501

        :return: The severity of this GridNetworkListAlert.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this GridNetworkListAlert.

        type of alert  # noqa: E501

        :param severity: The severity of this GridNetworkListAlert.  # noqa: E501
        :type: str
        """
        allowed_values = ["info", "warning", "error"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def text(self):
        """Gets the text of this GridNetworkListAlert.  # noqa: E501

        description of the alert  # noqa: E501

        :return: The text of this GridNetworkListAlert.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this GridNetworkListAlert.

        description of the alert  # noqa: E501

        :param text: The text of this GridNetworkListAlert.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def key(self):
        """Gets the key of this GridNetworkListAlert.  # noqa: E501

        key for localizing the alert text  # noqa: E501

        :return: The key of this GridNetworkListAlert.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this GridNetworkListAlert.

        key for localizing the alert text  # noqa: E501

        :param key: The key of this GridNetworkListAlert.  # noqa: E501
        :type: str
        """

        self._key = key

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
        if issubclass(GridNetworkListAlert, dict):
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
        if not isinstance(other, GridNetworkListAlert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
