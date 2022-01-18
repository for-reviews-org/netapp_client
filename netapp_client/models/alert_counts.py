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

class AlertCounts(object):
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
        'critical': 'int',
        'major': 'int',
        'minor': 'int'
    }

    attribute_map = {
        'critical': 'critical',
        'major': 'major',
        'minor': 'minor'
    }

    def __init__(self, critical=None, major=None, minor=None):  # noqa: E501
        """AlertCounts - a model defined in Swagger"""  # noqa: E501
        self._critical = None
        self._major = None
        self._minor = None
        self.discriminator = None
        if critical is not None:
            self.critical = critical
        if major is not None:
            self.major = major
        if minor is not None:
            self.minor = minor

    @property
    def critical(self):
        """Gets the critical of this AlertCounts.  # noqa: E501


        :return: The critical of this AlertCounts.  # noqa: E501
        :rtype: int
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        """Sets the critical of this AlertCounts.


        :param critical: The critical of this AlertCounts.  # noqa: E501
        :type: int
        """

        self._critical = critical

    @property
    def major(self):
        """Gets the major of this AlertCounts.  # noqa: E501


        :return: The major of this AlertCounts.  # noqa: E501
        :rtype: int
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this AlertCounts.


        :param major: The major of this AlertCounts.  # noqa: E501
        :type: int
        """

        self._major = major

    @property
    def minor(self):
        """Gets the minor of this AlertCounts.  # noqa: E501


        :return: The minor of this AlertCounts.  # noqa: E501
        :rtype: int
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this AlertCounts.


        :param minor: The minor of this AlertCounts.  # noqa: E501
        :type: int
        """

        self._minor = minor

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
        if issubclass(AlertCounts, dict):
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
        if not isinstance(other, AlertCounts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other