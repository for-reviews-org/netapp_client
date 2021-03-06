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

class EcProfile(object):
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
        'name': 'str',
        'pool_id': 'str',
        'scheme_id': 'str',
        'active': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'pool_id': 'poolId',
        'scheme_id': 'schemeId',
        'active': 'active'
    }

    def __init__(self, id=None, name=None, pool_id=None, scheme_id=None, active=None):  # noqa: E501
        """EcProfile - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._pool_id = None
        self._scheme_id = None
        self._active = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.pool_id = pool_id
        self.scheme_id = scheme_id
        self.active = active

    @property
    def id(self):
        """Gets the id of this EcProfile.  # noqa: E501

        a unique identifier for the Erasure Coding Profile (generated automatically)  # noqa: E501

        :return: The id of this EcProfile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EcProfile.

        a unique identifier for the Erasure Coding Profile (generated automatically)  # noqa: E501

        :param id: The id of this EcProfile.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this EcProfile.  # noqa: E501

        the EC Profile's name  # noqa: E501

        :return: The name of this EcProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EcProfile.

        the EC Profile's name  # noqa: E501

        :param name: The name of this EcProfile.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def pool_id(self):
        """Gets the pool_id of this EcProfile.  # noqa: E501

        the Storage Pool ID of the selected scheme  # noqa: E501

        :return: The pool_id of this EcProfile.  # noqa: E501
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this EcProfile.

        the Storage Pool ID of the selected scheme  # noqa: E501

        :param pool_id: The pool_id of this EcProfile.  # noqa: E501
        :type: str
        """
        if pool_id is None:
            raise ValueError("Invalid value for `pool_id`, must not be `None`")  # noqa: E501

        self._pool_id = pool_id

    @property
    def scheme_id(self):
        """Gets the scheme_id of this EcProfile.  # noqa: E501

        the selected scheme for the EC profile  # noqa: E501

        :return: The scheme_id of this EcProfile.  # noqa: E501
        :rtype: str
        """
        return self._scheme_id

    @scheme_id.setter
    def scheme_id(self, scheme_id):
        """Sets the scheme_id of this EcProfile.

        the selected scheme for the EC profile  # noqa: E501

        :param scheme_id: The scheme_id of this EcProfile.  # noqa: E501
        :type: str
        """
        if scheme_id is None:
            raise ValueError("Invalid value for `scheme_id`, must not be `None`")  # noqa: E501

        self._scheme_id = scheme_id

    @property
    def active(self):
        """Gets the active of this EcProfile.  # noqa: E501

        whether the profile is active or deactivated  # noqa: E501

        :return: The active of this EcProfile.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this EcProfile.

        whether the profile is active or deactivated  # noqa: E501

        :param active: The active of this EcProfile.  # noqa: E501
        :type: bool
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

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
        if issubclass(EcProfile, dict):
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
        if not isinstance(other, EcProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
