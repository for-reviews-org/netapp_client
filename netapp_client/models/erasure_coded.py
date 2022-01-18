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

class ErasureCoded(object):
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
        'pool_id': 'str',
        'profile_id': 'str'
    }

    attribute_map = {
        'pool_id': 'poolId',
        'profile_id': 'profileId'
    }

    def __init__(self, pool_id=None, profile_id=None):  # noqa: E501
        """ErasureCoded - a model defined in Swagger"""  # noqa: E501
        self._pool_id = None
        self._profile_id = None
        self.discriminator = None
        self.pool_id = pool_id
        self.profile_id = profile_id

    @property
    def pool_id(self):
        """Gets the pool_id of this ErasureCoded.  # noqa: E501

        storage pool where object data is stored  # noqa: E501

        :return: The pool_id of this ErasureCoded.  # noqa: E501
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this ErasureCoded.

        storage pool where object data is stored  # noqa: E501

        :param pool_id: The pool_id of this ErasureCoded.  # noqa: E501
        :type: str
        """
        if pool_id is None:
            raise ValueError("Invalid value for `pool_id`, must not be `None`")  # noqa: E501

        self._pool_id = pool_id

    @property
    def profile_id(self):
        """Gets the profile_id of this ErasureCoded.  # noqa: E501

        erasure coding profile used. Erasure coded object data only  # noqa: E501

        :return: The profile_id of this ErasureCoded.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this ErasureCoded.

        erasure coding profile used. Erasure coded object data only  # noqa: E501

        :param profile_id: The profile_id of this ErasureCoded.  # noqa: E501
        :type: str
        """
        if profile_id is None:
            raise ValueError("Invalid value for `profile_id`, must not be `None`")  # noqa: E501

        self._profile_id = profile_id

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
        if issubclass(ErasureCoded, dict):
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
        if not isinstance(other, ErasureCoded):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other