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

class Credentials(object):
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
        'username': 'str',
        'password': 'str',
        'cookie': 'bool',
        'csrf_token': 'bool'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'cookie': 'cookie',
        'csrf_token': 'csrfToken'
    }

    def __init__(self, username=None, password=None, cookie=None, csrf_token=False):  # noqa: E501
        """Credentials - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._password = None
        self._cookie = None
        self._csrf_token = None
        self.discriminator = None
        self.username = username
        self.password = password
        if cookie is not None:
            self.cookie = cookie
        if csrf_token is not None:
            self.csrf_token = csrf_token

    @property
    def username(self):
        """Gets the username of this Credentials.  # noqa: E501


        :return: The username of this Credentials.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Credentials.


        :param username: The username of this Credentials.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this Credentials.  # noqa: E501


        :return: The password of this Credentials.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Credentials.


        :param password: The password of this Credentials.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def cookie(self):
        """Gets the cookie of this Credentials.  # noqa: E501

        flag to ask for an authorization token in the response using the Set-Cookie header  # noqa: E501

        :return: The cookie of this Credentials.  # noqa: E501
        :rtype: bool
        """
        return self._cookie

    @cookie.setter
    def cookie(self, cookie):
        """Sets the cookie of this Credentials.

        flag to ask for an authorization token in the response using the Set-Cookie header  # noqa: E501

        :param cookie: The cookie of this Credentials.  # noqa: E501
        :type: bool
        """

        self._cookie = cookie

    @property
    def csrf_token(self):
        """Gets the csrf_token of this Credentials.  # noqa: E501

        flag to ask for a CSRF token in the response using the Set-Cookie header. See the Administrator Guide for more information  # noqa: E501

        :return: The csrf_token of this Credentials.  # noqa: E501
        :rtype: bool
        """
        return self._csrf_token

    @csrf_token.setter
    def csrf_token(self, csrf_token):
        """Sets the csrf_token of this Credentials.

        flag to ask for a CSRF token in the response using the Set-Cookie header. See the Administrator Guide for more information  # noqa: E501

        :param csrf_token: The csrf_token of this Credentials.  # noqa: E501
        :type: bool
        """

        self._csrf_token = csrf_token

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
        if issubclass(Credentials, dict):
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
        if not isinstance(other, Credentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
