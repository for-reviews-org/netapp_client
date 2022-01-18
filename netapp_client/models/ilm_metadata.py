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

class IlmMetadata(object):
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
        'id': 'str',
        'type': 'str',
        'unit': 'str',
        'operators': 'list[IlmOperator]'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'unit': 'unit',
        'operators': 'operators'
    }

    def __init__(self, id=None, type=None, unit=None, operators=None):  # noqa: E501
        """IlmMetadata - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._unit = None
        self._operators = None
        self.discriminator = None
        self.id = id
        self.type = type
        if unit is not None:
            self.unit = unit
        self.operators = operators

    @property
    def id(self):
        """Gets the id of this IlmMetadata.  # noqa: E501

        the unique identifier of the system metadata  # noqa: E501

        :return: The id of this IlmMetadata.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IlmMetadata.

        the unique identifier of the system metadata  # noqa: E501

        :param id: The id of this IlmMetadata.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this IlmMetadata.  # noqa: E501

        the value type of this metadata  # noqa: E501

        :return: The type of this IlmMetadata.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IlmMetadata.

        the value type of this metadata  # noqa: E501

        :param type: The type of this IlmMetadata.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["integer", "string"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def unit(self):
        """Gets the unit of this IlmMetadata.  # noqa: E501

        the unit for the metadata value where applicable  # noqa: E501

        :return: The unit of this IlmMetadata.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this IlmMetadata.

        the unit for the metadata value where applicable  # noqa: E501

        :param unit: The unit of this IlmMetadata.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def operators(self):
        """Gets the operators of this IlmMetadata.  # noqa: E501

        the list of supported operators for this metadata  # noqa: E501

        :return: The operators of this IlmMetadata.  # noqa: E501
        :rtype: list[IlmOperator]
        """
        return self._operators

    @operators.setter
    def operators(self, operators):
        """Sets the operators of this IlmMetadata.

        the list of supported operators for this metadata  # noqa: E501

        :param operators: The operators of this IlmMetadata.  # noqa: E501
        :type: list[IlmOperator]
        """
        if operators is None:
            raise ValueError("Invalid value for `operators`, must not be `None`")  # noqa: E501

        self._operators = operators

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
        if issubclass(IlmMetadata, dict):
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
        if not isinstance(other, IlmMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
