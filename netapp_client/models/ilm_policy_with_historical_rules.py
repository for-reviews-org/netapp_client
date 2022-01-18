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
from netapp_client.models.ilm_policy import IlmPolicy  # noqa: F401,E501

class IlmPolicyWithHistoricalRules(IlmPolicy):
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
        'historical_rules': 'list[IlmRule]'
    }
    if hasattr(IlmPolicy, "swagger_types"):
        swagger_types.update(IlmPolicy.swagger_types)

    attribute_map = {
        'historical_rules': 'historicalRules'
    }
    if hasattr(IlmPolicy, "attribute_map"):
        attribute_map.update(IlmPolicy.attribute_map)

    def __init__(self, historical_rules=None, *args, **kwargs):  # noqa: E501
        """IlmPolicyWithHistoricalRules - a model defined in Swagger"""  # noqa: E501
        self._historical_rules = None
        self.discriminator = None
        if historical_rules is not None:
            self.historical_rules = historical_rules
        IlmPolicy.__init__(self, *args, **kwargs)

    @property
    def historical_rules(self):
        """Gets the historical_rules of this IlmPolicyWithHistoricalRules.  # noqa: E501

        list of rule definitions at the time they were added to a policy, if they differ from the current definitions  # noqa: E501

        :return: The historical_rules of this IlmPolicyWithHistoricalRules.  # noqa: E501
        :rtype: list[IlmRule]
        """
        return self._historical_rules

    @historical_rules.setter
    def historical_rules(self, historical_rules):
        """Sets the historical_rules of this IlmPolicyWithHistoricalRules.

        list of rule definitions at the time they were added to a policy, if they differ from the current definitions  # noqa: E501

        :param historical_rules: The historical_rules of this IlmPolicyWithHistoricalRules.  # noqa: E501
        :type: list[IlmRule]
        """

        self._historical_rules = historical_rules

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
        if issubclass(IlmPolicyWithHistoricalRules, dict):
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
        if not isinstance(other, IlmPolicyWithHistoricalRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
