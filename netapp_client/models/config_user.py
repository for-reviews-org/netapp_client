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

class ConfigUser(object):
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
        'username': 'str',
        'unique_name': 'str',
        'first_name': 'str',
        'full_name': 'str',
        'federated': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'unique_name': 'uniqueName',
        'first_name': 'firstName',
        'full_name': 'fullName',
        'federated': 'federated'
    }

    def __init__(self, id=None, username=None, unique_name=None, first_name=None, full_name=None, federated=None):  # noqa: E501
        """ConfigUser - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._username = None
        self._unique_name = None
        self._first_name = None
        self._full_name = None
        self._federated = None
        self.discriminator = None
        self.id = id
        self.username = username
        self.unique_name = unique_name
        self.first_name = first_name
        self.full_name = full_name
        self.federated = federated

    @property
    def id(self):
        """Gets the id of this ConfigUser.  # noqa: E501

        UUID for the User (generated automatically)  # noqa: E501

        :return: The id of this ConfigUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConfigUser.

        UUID for the User (generated automatically)  # noqa: E501

        :param id: The id of this ConfigUser.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def username(self):
        """Gets the username of this ConfigUser.  # noqa: E501

        the username that is used to sign in  # noqa: E501

        :return: The username of this ConfigUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ConfigUser.

        the username that is used to sign in  # noqa: E501

        :param username: The username of this ConfigUser.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def unique_name(self):
        """Gets the unique_name of this ConfigUser.  # noqa: E501

        the machine-readable name for the User (unique within an Account)  # noqa: E501

        :return: The unique_name of this ConfigUser.  # noqa: E501
        :rtype: str
        """
        return self._unique_name

    @unique_name.setter
    def unique_name(self, unique_name):
        """Sets the unique_name of this ConfigUser.

        the machine-readable name for the User (unique within an Account)  # noqa: E501

        :param unique_name: The unique_name of this ConfigUser.  # noqa: E501
        :type: str
        """
        if unique_name is None:
            raise ValueError("Invalid value for `unique_name`, must not be `None`")  # noqa: E501

        self._unique_name = unique_name

    @property
    def first_name(self):
        """Gets the first_name of this ConfigUser.  # noqa: E501

        the User's first name  # noqa: E501

        :return: The first_name of this ConfigUser.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ConfigUser.

        the User's first name  # noqa: E501

        :param first_name: The first_name of this ConfigUser.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def full_name(self):
        """Gets the full_name of this ConfigUser.  # noqa: E501

        the human-readable name for the User  # noqa: E501

        :return: The full_name of this ConfigUser.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this ConfigUser.

        the human-readable name for the User  # noqa: E501

        :param full_name: The full_name of this ConfigUser.  # noqa: E501
        :type: str
        """
        if full_name is None:
            raise ValueError("Invalid value for `full_name`, must not be `None`")  # noqa: E501

        self._full_name = full_name

    @property
    def federated(self):
        """Gets the federated of this ConfigUser.  # noqa: E501

        true if the User is federated, for example, an LDAP User  # noqa: E501

        :return: The federated of this ConfigUser.  # noqa: E501
        :rtype: bool
        """
        return self._federated

    @federated.setter
    def federated(self, federated):
        """Sets the federated of this ConfigUser.

        true if the User is federated, for example, an LDAP User  # noqa: E501

        :param federated: The federated of this ConfigUser.  # noqa: E501
        :type: bool
        """
        if federated is None:
            raise ValueError("Invalid value for `federated`, must not be `None`")  # noqa: E501

        self._federated = federated

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
        if issubclass(ConfigUser, dict):
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
        if not isinstance(other, ConfigUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
