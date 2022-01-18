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

class TrafficClassMatcher(object):
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
        'type': 'str',
        'inverse': 'bool',
        'members': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'inverse': 'inverse',
        'members': 'members'
    }

    def __init__(self, type=None, inverse=False, members=None):  # noqa: E501
        """TrafficClassMatcher - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._inverse = None
        self._members = None
        self.discriminator = None
        self.type = type
        if inverse is not None:
            self.inverse = inverse
        self.members = members

    @property
    def type(self):
        """Gets the type of this TrafficClassMatcher.  # noqa: E501

        The attribute of the request to match. * `bucket` - The S3 bucket (or Swift container) being accessed * `bucket-regex` - A regular expression to evaluate against the S3 bucket (or Swift container) being accessed * `cidr` - Matches if the client request source IP is in the specified IPv4 CIDR (RFC4632) * `endpoint` - The UUID of the load balancer endpoint which the client is connecting to * `tenant` - Matches if the S3 bucket (or Swift container) is owned by the tenant account with this ID   # noqa: E501

        :return: The type of this TrafficClassMatcher.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TrafficClassMatcher.

        The attribute of the request to match. * `bucket` - The S3 bucket (or Swift container) being accessed * `bucket-regex` - A regular expression to evaluate against the S3 bucket (or Swift container) being accessed * `cidr` - Matches if the client request source IP is in the specified IPv4 CIDR (RFC4632) * `endpoint` - The UUID of the load balancer endpoint which the client is connecting to * `tenant` - Matches if the S3 bucket (or Swift container) is owned by the tenant account with this ID   # noqa: E501

        :param type: The type of this TrafficClassMatcher.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["bucket", "bucket-regex", "cidr", "endpoint", "tenant"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def inverse(self):
        """Gets the inverse of this TrafficClassMatcher.  # noqa: E501

        If true, the matcher will apply for all requests that do not match __Warning:__ Creating an inverse matcher with more than 1 member will likely match all requests. Use with caution.  # noqa: E501

        :return: The inverse of this TrafficClassMatcher.  # noqa: E501
        :rtype: bool
        """
        return self._inverse

    @inverse.setter
    def inverse(self, inverse):
        """Sets the inverse of this TrafficClassMatcher.

        If true, the matcher will apply for all requests that do not match __Warning:__ Creating an inverse matcher with more than 1 member will likely match all requests. Use with caution.  # noqa: E501

        :param inverse: The inverse of this TrafficClassMatcher.  # noqa: E501
        :type: bool
        """

        self._inverse = inverse

    @property
    def members(self):
        """Gets the members of this TrafficClassMatcher.  # noqa: E501

        A list of members to match on. The policy will match a request if _ANY_ of the elements listed match.  # noqa: E501

        :return: The members of this TrafficClassMatcher.  # noqa: E501
        :rtype: list[str]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this TrafficClassMatcher.

        A list of members to match on. The policy will match a request if _ANY_ of the elements listed match.  # noqa: E501

        :param members: The members of this TrafficClassMatcher.  # noqa: E501
        :type: list[str]
        """
        if members is None:
            raise ValueError("Invalid value for `members`, must not be `None`")  # noqa: E501

        self._members = members

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
        if issubclass(TrafficClassMatcher, dict):
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
        if not isinstance(other, TrafficClassMatcher):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other