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

class MetricsData(object):
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
        'result_type': 'str',
        'result': 'list[MetricsDataResultItem]'
    }

    attribute_map = {
        'result_type': 'resultType',
        'result': 'result'
    }

    def __init__(self, result_type=None, result=None):  # noqa: E501
        """MetricsData - a model defined in Swagger"""  # noqa: E501
        self._result_type = None
        self._result = None
        self.discriminator = None
        self.result_type = result_type
        self.result = result

    @property
    def result_type(self):
        """Gets the result_type of this MetricsData.  # noqa: E501

        the type of query results returned  # noqa: E501

        :return: The result_type of this MetricsData.  # noqa: E501
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        """Sets the result_type of this MetricsData.

        the type of query results returned  # noqa: E501

        :param result_type: The result_type of this MetricsData.  # noqa: E501
        :type: str
        """
        if result_type is None:
            raise ValueError("Invalid value for `result_type`, must not be `None`")  # noqa: E501
        allowed_values = ["matrix", "scalar", "string", "vector"]  # noqa: E501
        if result_type not in allowed_values:
            raise ValueError(
                "Invalid value for `result_type` ({0}), must be one of {1}"  # noqa: E501
                .format(result_type, allowed_values)
            )

        self._result_type = result_type

    @property
    def result(self):
        """Gets the result of this MetricsData.  # noqa: E501

        the result rows from the query (format depends on resultType)  # noqa: E501

        :return: The result of this MetricsData.  # noqa: E501
        :rtype: list[MetricsDataResultItem]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this MetricsData.

        the result rows from the query (format depends on resultType)  # noqa: E501

        :param result: The result of this MetricsData.  # noqa: E501
        :type: list[MetricsDataResultItem]
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

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
        if issubclass(MetricsData, dict):
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
        if not isinstance(other, MetricsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
