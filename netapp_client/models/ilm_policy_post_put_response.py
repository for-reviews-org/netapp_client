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
from swagger_client.models.response import Response  # noqa: F401,E501

class IlmPolicyPostPutResponse(Response):
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
        'data': 'IlmPolicy'
    }
    if hasattr(Response, "swagger_types"):
        swagger_types.update(Response.swagger_types)

    attribute_map = {
        'data': 'data'
    }
    if hasattr(Response, "attribute_map"):
        attribute_map.update(Response.attribute_map)

    def __init__(self, data=None, *args, **kwargs):  # noqa: E501
        """IlmPolicyPostPutResponse - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self.discriminator = None
        self.data = data
        Response.__init__(self, *args, **kwargs)

    @property
    def data(self):
        """Gets the data of this IlmPolicyPostPutResponse.  # noqa: E501


        :return: The data of this IlmPolicyPostPutResponse.  # noqa: E501
        :rtype: IlmPolicy
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this IlmPolicyPostPutResponse.


        :param data: The data of this IlmPolicyPostPutResponse.  # noqa: E501
        :type: IlmPolicy
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if issubclass(IlmPolicyPostPutResponse, dict):
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
        if not isinstance(other, IlmPolicyPostPutResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
