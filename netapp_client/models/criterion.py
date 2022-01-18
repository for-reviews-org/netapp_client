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

class Criterion(object):
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
        'user_metadata': 'bool',
        'metadata_type': 'str',
        'metadata_name': 'str',
        'operator': 'IlmOperator',
        'value': 'str'
    }

    attribute_map = {
        'user_metadata': 'userMetadata',
        'metadata_type': 'metadataType',
        'metadata_name': 'metadataName',
        'operator': 'operator',
        'value': 'value'
    }

    def __init__(self, user_metadata=False, metadata_type='system', metadata_name=None, operator=None, value=None):  # noqa: E501
        """Criterion - a model defined in Swagger"""  # noqa: E501
        self._user_metadata = None
        self._metadata_type = None
        self._metadata_name = None
        self._operator = None
        self._value = None
        self.discriminator = None
        if user_metadata is not None:
            self.user_metadata = user_metadata
        if metadata_type is not None:
            self.metadata_type = metadata_type
        self.metadata_name = metadata_name
        self.operator = operator
        if value is not None:
            self.value = value

    @property
    def user_metadata(self):
        """Gets the user_metadata of this Criterion.  # noqa: E501

        deprecated. Indicates if the filtering metadata specified is user metadata  # noqa: E501

        :return: The user_metadata of this Criterion.  # noqa: E501
        :rtype: bool
        """
        return self._user_metadata

    @user_metadata.setter
    def user_metadata(self, user_metadata):
        """Sets the user_metadata of this Criterion.

        deprecated. Indicates if the filtering metadata specified is user metadata  # noqa: E501

        :param user_metadata: The user_metadata of this Criterion.  # noqa: E501
        :type: bool
        """

        self._user_metadata = user_metadata

    @property
    def metadata_type(self):
        """Gets the metadata_type of this Criterion.  # noqa: E501

        indicates the type of filtered metadata  # noqa: E501

        :return: The metadata_type of this Criterion.  # noqa: E501
        :rtype: str
        """
        return self._metadata_type

    @metadata_type.setter
    def metadata_type(self, metadata_type):
        """Sets the metadata_type of this Criterion.

        indicates the type of filtered metadata  # noqa: E501

        :param metadata_type: The metadata_type of this Criterion.  # noqa: E501
        :type: str
        """
        allowed_values = ["user", "system", "tag"]  # noqa: E501
        if metadata_type not in allowed_values:
            raise ValueError(
                "Invalid value for `metadata_type` ({0}), must be one of {1}"  # noqa: E501
                .format(metadata_type, allowed_values)
            )

        self._metadata_type = metadata_type

    @property
    def metadata_name(self):
        """Gets the metadata_name of this Criterion.  # noqa: E501

        system metadata identifier, user metadata name, or tag name  # noqa: E501

        :return: The metadata_name of this Criterion.  # noqa: E501
        :rtype: str
        """
        return self._metadata_name

    @metadata_name.setter
    def metadata_name(self, metadata_name):
        """Sets the metadata_name of this Criterion.

        system metadata identifier, user metadata name, or tag name  # noqa: E501

        :param metadata_name: The metadata_name of this Criterion.  # noqa: E501
        :type: str
        """
        if metadata_name is None:
            raise ValueError("Invalid value for `metadata_name`, must not be `None`")  # noqa: E501

        self._metadata_name = metadata_name

    @property
    def operator(self):
        """Gets the operator of this Criterion.  # noqa: E501


        :return: The operator of this Criterion.  # noqa: E501
        :rtype: IlmOperator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this Criterion.


        :param operator: The operator of this Criterion.  # noqa: E501
        :type: IlmOperator
        """
        if operator is None:
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

    @property
    def value(self):
        """Gets the value of this Criterion.  # noqa: E501

        entry against which the metadata values specified by metadataName should be compared  # noqa: E501

        :return: The value of this Criterion.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Criterion.

        entry against which the metadata values specified by metadataName should be compared  # noqa: E501

        :param value: The value of this Criterion.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(Criterion, dict):
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
        if not isinstance(other, Criterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
