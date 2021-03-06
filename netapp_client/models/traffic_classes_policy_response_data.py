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
from netapp_client.models.traffic_classes_policy_readonly import TrafficClassesPolicyReadonly  # noqa: F401,E501

class TrafficClassesPolicyResponseData(TrafficClassesPolicyReadonly):
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
        'name': 'str',
        'description': 'str',
        'matchers': 'list[TrafficClassMatcher]',
        'limits': 'list[TrafficClassLimit]'
    }
    if hasattr(TrafficClassesPolicyReadonly, "swagger_types"):
        swagger_types.update(TrafficClassesPolicyReadonly.swagger_types)

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'matchers': 'matchers',
        'limits': 'limits'
    }
    if hasattr(TrafficClassesPolicyReadonly, "attribute_map"):
        attribute_map.update(TrafficClassesPolicyReadonly.attribute_map)

    def __init__(self, name=None, description=None, matchers=None, limits=None, *args, **kwargs):  # noqa: E501
        """TrafficClassesPolicyResponseData - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._matchers = None
        self._limits = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        if matchers is not None:
            self.matchers = matchers
        if limits is not None:
            self.limits = limits
        TrafficClassesPolicyReadonly.__init__(self, *args, **kwargs)

    @property
    def name(self):
        """Gets the name of this TrafficClassesPolicyResponseData.  # noqa: E501

        A name for the policy  # noqa: E501

        :return: The name of this TrafficClassesPolicyResponseData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrafficClassesPolicyResponseData.

        A name for the policy  # noqa: E501

        :param name: The name of this TrafficClassesPolicyResponseData.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this TrafficClassesPolicyResponseData.  # noqa: E501

        A description of the policy  # noqa: E501

        :return: The description of this TrafficClassesPolicyResponseData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TrafficClassesPolicyResponseData.

        A description of the policy  # noqa: E501

        :param description: The description of this TrafficClassesPolicyResponseData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def matchers(self):
        """Gets the matchers of this TrafficClassesPolicyResponseData.  # noqa: E501

        The set of parameters to match. The traffic class will match requests where _ANY_ of these matchers match. _Note:_ One of each matcher type can be specified.  # noqa: E501

        :return: The matchers of this TrafficClassesPolicyResponseData.  # noqa: E501
        :rtype: list[TrafficClassMatcher]
        """
        return self._matchers

    @matchers.setter
    def matchers(self, matchers):
        """Sets the matchers of this TrafficClassesPolicyResponseData.

        The set of parameters to match. The traffic class will match requests where _ANY_ of these matchers match. _Note:_ One of each matcher type can be specified.  # noqa: E501

        :param matchers: The matchers of this TrafficClassesPolicyResponseData.  # noqa: E501
        :type: list[TrafficClassMatcher]
        """

        self._matchers = matchers

    @property
    def limits(self):
        """Gets the limits of this TrafficClassesPolicyResponseData.  # noqa: E501

        Optional limits to impose on client requests matched by this traffic class. _Note:_ One of each matcher type can be specified.  # noqa: E501

        :return: The limits of this TrafficClassesPolicyResponseData.  # noqa: E501
        :rtype: list[TrafficClassLimit]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this TrafficClassesPolicyResponseData.

        Optional limits to impose on client requests matched by this traffic class. _Note:_ One of each matcher type can be specified.  # noqa: E501

        :param limits: The limits of this TrafficClassesPolicyResponseData.  # noqa: E501
        :type: list[TrafficClassLimit]
        """

        self._limits = limits

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
        if issubclass(TrafficClassesPolicyResponseData, dict):
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
        if not isinstance(other, TrafficClassesPolicyResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
