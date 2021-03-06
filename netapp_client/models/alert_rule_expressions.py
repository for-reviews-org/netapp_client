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

class AlertRuleExpressions(object):
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
        'minor': 'str',
        'major': 'str',
        'critical': 'str'
    }

    attribute_map = {
        'minor': 'minor',
        'major': 'major',
        'critical': 'critical'
    }

    def __init__(self, minor=None, major=None, critical=None):  # noqa: E501
        """AlertRuleExpressions - a model defined in Swagger"""  # noqa: E501
        self._minor = None
        self._major = None
        self._critical = None
        self.discriminator = None
        if minor is not None:
            self.minor = minor
        if major is not None:
            self.major = major
        if critical is not None:
            self.critical = critical

    @property
    def minor(self):
        """Gets the minor of this AlertRuleExpressions.  # noqa: E501


        :return: The minor of this AlertRuleExpressions.  # noqa: E501
        :rtype: str
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this AlertRuleExpressions.


        :param minor: The minor of this AlertRuleExpressions.  # noqa: E501
        :type: str
        """

        self._minor = minor

    @property
    def major(self):
        """Gets the major of this AlertRuleExpressions.  # noqa: E501


        :return: The major of this AlertRuleExpressions.  # noqa: E501
        :rtype: str
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this AlertRuleExpressions.


        :param major: The major of this AlertRuleExpressions.  # noqa: E501
        :type: str
        """

        self._major = major

    @property
    def critical(self):
        """Gets the critical of this AlertRuleExpressions.  # noqa: E501


        :return: The critical of this AlertRuleExpressions.  # noqa: E501
        :rtype: str
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        """Sets the critical of this AlertRuleExpressions.


        :param critical: The critical of this AlertRuleExpressions.  # noqa: E501
        :type: str
        """

        self._critical = critical

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
        if issubclass(AlertRuleExpressions, dict):
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
        if not isinstance(other, AlertRuleExpressions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
