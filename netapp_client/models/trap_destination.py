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

class TrapDestination(object):
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
        'host': 'str',
        'port': 'int',
        'community': 'str',
        'usm_user': 'str',
        'protocol': 'str'
    }

    attribute_map = {
        'type': 'type',
        'host': 'host',
        'port': 'port',
        'community': 'community',
        'usm_user': 'usmUser',
        'protocol': 'protocol'
    }

    def __init__(self, type=None, host=None, port=None, community=None, usm_user=None, protocol='udp'):  # noqa: E501
        """TrapDestination - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._host = None
        self._port = None
        self._community = None
        self._usm_user = None
        self._protocol = None
        self.discriminator = None
        self.type = type
        self.host = host
        if port is not None:
            self.port = port
        if community is not None:
            self.community = community
        if usm_user is not None:
            self.usm_user = usm_user
        if protocol is not None:
            self.protocol = protocol

    @property
    def type(self):
        """Gets the type of this TrapDestination.  # noqa: E501

        SNMP trap destination type  # noqa: E501

        :return: The type of this TrapDestination.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TrapDestination.

        SNMP trap destination type  # noqa: E501

        :param type: The type of this TrapDestination.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["trapsink", "trap2sink", "informsink", "trapsess", "informsess"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def host(self):
        """Gets the host of this TrapDestination.  # noqa: E501

        SNMP trap destination host  # noqa: E501

        :return: The host of this TrapDestination.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this TrapDestination.

        SNMP trap destination host  # noqa: E501

        :param host: The host of this TrapDestination.  # noqa: E501
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def port(self):
        """Gets the port of this TrapDestination.  # noqa: E501

        SNMP trap destination port  # noqa: E501

        :return: The port of this TrapDestination.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this TrapDestination.

        SNMP trap destination port  # noqa: E501

        :param port: The port of this TrapDestination.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def community(self):
        """Gets the community of this TrapDestination.  # noqa: E501

        SNMP trap destination community (cannot be used with usmUser). Cannot contain whitespace.  # noqa: E501

        :return: The community of this TrapDestination.  # noqa: E501
        :rtype: str
        """
        return self._community

    @community.setter
    def community(self, community):
        """Sets the community of this TrapDestination.

        SNMP trap destination community (cannot be used with usmUser). Cannot contain whitespace.  # noqa: E501

        :param community: The community of this TrapDestination.  # noqa: E501
        :type: str
        """

        self._community = community

    @property
    def usm_user(self):
        """Gets the usm_user of this TrapDestination.  # noqa: E501

        USM user to send notification under (cannot be used with community). Cannot contain whitespace.  # noqa: E501

        :return: The usm_user of this TrapDestination.  # noqa: E501
        :rtype: str
        """
        return self._usm_user

    @usm_user.setter
    def usm_user(self, usm_user):
        """Sets the usm_user of this TrapDestination.

        USM user to send notification under (cannot be used with community). Cannot contain whitespace.  # noqa: E501

        :param usm_user: The usm_user of this TrapDestination.  # noqa: E501
        :type: str
        """

        self._usm_user = usm_user

    @property
    def protocol(self):
        """Gets the protocol of this TrapDestination.  # noqa: E501

        SNMP trap destination protocol  # noqa: E501

        :return: The protocol of this TrapDestination.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this TrapDestination.

        SNMP trap destination protocol  # noqa: E501

        :param protocol: The protocol of this TrapDestination.  # noqa: E501
        :type: str
        """
        allowed_values = ["udp", "tcp"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

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
        if issubclass(TrapDestination, dict):
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
        if not isinstance(other, TrapDestination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other