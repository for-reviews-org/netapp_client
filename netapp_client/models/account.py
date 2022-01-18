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
from netapp_client.models.account_no_id import AccountNoId  # noqa: F401,E501

class Account(AccountNoId):
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
        'id': 'str'
    }
    if hasattr(AccountNoId, "swagger_types"):
        swagger_types.update(AccountNoId.swagger_types)

    attribute_map = {
        'id': 'id'
    }
    if hasattr(AccountNoId, "attribute_map"):
        attribute_map.update(AccountNoId.attribute_map)

    def __init__(self, id=None, *args, **kwargs):  # noqa: E501
        """Account - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self.discriminator = None
        self.id = id
        AccountNoId.__init__(self, *args, **kwargs)

    @property
    def id(self):
        """Gets the id of this Account.  # noqa: E501

        a unique identifier for the account (automatically assigned when an account is created)  # noqa: E501

        :return: The id of this Account.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Account.

        a unique identifier for the account (automatically assigned when an account is created)  # noqa: E501

        :param id: The id of this Account.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if issubclass(Account, dict):
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
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
