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

class AgentAddress(object):
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
        'protocol': 'str',
        'network': 'str',
        'port': 'int'
    }

    attribute_map = {
        'protocol': 'protocol',
        'network': 'network',
        'port': 'port'
    }

    def __init__(self, protocol='udp', network='all', port=None):  # noqa: E501
        """AgentAddress - a model defined in Swagger"""  # noqa: E501
        self._protocol = None
        self._network = None
        self._port = None
        self.discriminator = None
        if protocol is not None:
            self.protocol = protocol
        if network is not None:
            self.network = network
        if port is not None:
            self.port = port

    @property
    def protocol(self):
        """Gets the protocol of this AgentAddress.  # noqa: E501

        SNMP agent address protocol  # noqa: E501

        :return: The protocol of this AgentAddress.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this AgentAddress.

        SNMP agent address protocol  # noqa: E501

        :param protocol: The protocol of this AgentAddress.  # noqa: E501
        :type: str
        """
        allowed_values = ["udp", "udp6", "tcp", "tcp6"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def network(self):
        """Gets the network of this AgentAddress.  # noqa: E501

        Local network interface to bind to  # noqa: E501

        :return: The network of this AgentAddress.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this AgentAddress.

        Local network interface to bind to  # noqa: E501

        :param network: The network of this AgentAddress.  # noqa: E501
        :type: str
        """
        allowed_values = ["grid", "admin", "client", "all"]  # noqa: E501
        if network not in allowed_values:
            raise ValueError(
                "Invalid value for `network` ({0}), must be one of {1}"  # noqa: E501
                .format(network, allowed_values)
            )

        self._network = network

    @property
    def port(self):
        """Gets the port of this AgentAddress.  # noqa: E501

        Local port to bind to  # noqa: E501

        :return: The port of this AgentAddress.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this AgentAddress.

        Local port to bind to  # noqa: E501

        :param port: The port of this AgentAddress.  # noqa: E501
        :type: int
        """

        self._port = port

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
        if issubclass(AgentAddress, dict):
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
        if not isinstance(other, AgentAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
