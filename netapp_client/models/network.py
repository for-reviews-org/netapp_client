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

class Network(object):
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
        'mac': 'str',
        'ip': 'str',
        'gateway': 'str',
        'config': 'str'
    }

    attribute_map = {
        'mac': 'mac',
        'ip': 'ip',
        'gateway': 'gateway',
        'config': 'config'
    }

    def __init__(self, mac=None, ip=None, gateway=None, config=None):  # noqa: E501
        """Network - a model defined in Swagger"""  # noqa: E501
        self._mac = None
        self._ip = None
        self._gateway = None
        self._config = None
        self.discriminator = None
        if mac is not None:
            self.mac = mac
        if ip is not None:
            self.ip = ip
        if gateway is not None:
            self.gateway = gateway
        if config is not None:
            self.config = config

    @property
    def mac(self):
        """Gets the mac of this Network.  # noqa: E501

        network interface MAC address (pre-populated)  # noqa: E501

        :return: The mac of this Network.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this Network.

        network interface MAC address (pre-populated)  # noqa: E501

        :param mac: The mac of this Network.  # noqa: E501
        :type: str
        """

        self._mac = mac

    @property
    def ip(self):
        """Gets the ip of this Network.  # noqa: E501

        the CIDR network address for the network interface  # noqa: E501

        :return: The ip of this Network.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Network.

        the CIDR network address for the network interface  # noqa: E501

        :param ip: The ip of this Network.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def gateway(self):
        """Gets the gateway of this Network.  # noqa: E501

        the default gateway of the network  # noqa: E501

        :return: The gateway of this Network.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this Network.

        the default gateway of the network  # noqa: E501

        :param gateway: The gateway of this Network.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def config(self):
        """Gets the config of this Network.  # noqa: E501

        Describes how the interface is configured. A value of 'fixed' indicates that the configuration cannot be changed. A value of 'dhcp' indicates that the interface is configured by DHCP. A value of 'static' indicates that the interface is statically configured. Interfaces configured by DHCP can be changed to static and vice versa.   # noqa: E501

        :return: The config of this Network.  # noqa: E501
        :rtype: str
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Network.

        Describes how the interface is configured. A value of 'fixed' indicates that the configuration cannot be changed. A value of 'dhcp' indicates that the interface is configured by DHCP. A value of 'static' indicates that the interface is statically configured. Interfaces configured by DHCP can be changed to static and vice versa.   # noqa: E501

        :param config: The config of this Network.  # noqa: E501
        :type: str
        """
        allowed_values = ["static", "dhcp", "fixed"]  # noqa: E501
        if config not in allowed_values:
            raise ValueError(
                "Invalid value for `config` ({0}), must be one of {1}"  # noqa: E501
                .format(config, allowed_values)
            )

        self._config = config

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
        if issubclass(Network, dict):
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
        if not isinstance(other, Network):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
