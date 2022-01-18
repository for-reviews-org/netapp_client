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

class SnmpConfig(object):
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
        'enable_snmp': 'bool',
        'community_strings': 'list[str]',
        'rousers': 'list[str]',
        'sys_location': 'str',
        'sys_contact': 'str',
        'trapcommunity': 'str',
        'authtrapenable': 'int',
        'disable_notifications': 'bool',
        'trap_destinations': 'list[TrapDestination]',
        'agent_addresses': 'list[AgentAddress]',
        'usm_users': 'list[UsmUser]'
    }

    attribute_map = {
        'enable_snmp': 'enable_snmp',
        'community_strings': 'community_strings',
        'rousers': 'rousers',
        'sys_location': 'sysLocation',
        'sys_contact': 'sysContact',
        'trapcommunity': 'trapcommunity',
        'authtrapenable': 'authtrapenable',
        'disable_notifications': 'disable_notifications',
        'trap_destinations': 'trap_destinations',
        'agent_addresses': 'agent_addresses',
        'usm_users': 'usm_users'
    }

    def __init__(self, enable_snmp=False, community_strings=None, rousers=None, sys_location=None, sys_contact=None, trapcommunity=None, authtrapenable=None, disable_notifications=False, trap_destinations=None, agent_addresses=None, usm_users=None):  # noqa: E501
        """SnmpConfig - a model defined in Swagger"""  # noqa: E501
        self._enable_snmp = None
        self._community_strings = None
        self._rousers = None
        self._sys_location = None
        self._sys_contact = None
        self._trapcommunity = None
        self._authtrapenable = None
        self._disable_notifications = None
        self._trap_destinations = None
        self._agent_addresses = None
        self._usm_users = None
        self.discriminator = None
        if enable_snmp is not None:
            self.enable_snmp = enable_snmp
        if community_strings is not None:
            self.community_strings = community_strings
        if rousers is not None:
            self.rousers = rousers
        if sys_location is not None:
            self.sys_location = sys_location
        if sys_contact is not None:
            self.sys_contact = sys_contact
        if trapcommunity is not None:
            self.trapcommunity = trapcommunity
        if authtrapenable is not None:
            self.authtrapenable = authtrapenable
        if disable_notifications is not None:
            self.disable_notifications = disable_notifications
        if trap_destinations is not None:
            self.trap_destinations = trap_destinations
        if agent_addresses is not None:
            self.agent_addresses = agent_addresses
        if usm_users is not None:
            self.usm_users = usm_users

    @property
    def enable_snmp(self):
        """Gets the enable_snmp of this SnmpConfig.  # noqa: E501

        Whether the SNMP agent is enabled  # noqa: E501

        :return: The enable_snmp of this SnmpConfig.  # noqa: E501
        :rtype: bool
        """
        return self._enable_snmp

    @enable_snmp.setter
    def enable_snmp(self, enable_snmp):
        """Sets the enable_snmp of this SnmpConfig.

        Whether the SNMP agent is enabled  # noqa: E501

        :param enable_snmp: The enable_snmp of this SnmpConfig.  # noqa: E501
        :type: bool
        """

        self._enable_snmp = enable_snmp

    @property
    def community_strings(self):
        """Gets the community_strings of this SnmpConfig.  # noqa: E501

        An array of SNMP community strings. Individual strings cannot contain whitespace.  # noqa: E501

        :return: The community_strings of this SnmpConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._community_strings

    @community_strings.setter
    def community_strings(self, community_strings):
        """Sets the community_strings of this SnmpConfig.

        An array of SNMP community strings. Individual strings cannot contain whitespace.  # noqa: E501

        :param community_strings: The community_strings of this SnmpConfig.  # noqa: E501
        :type: list[str]
        """

        self._community_strings = community_strings

    @property
    def rousers(self):
        """Gets the rousers of this SnmpConfig.  # noqa: E501

        USM users allowed read-only access  # noqa: E501

        :return: The rousers of this SnmpConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._rousers

    @rousers.setter
    def rousers(self, rousers):
        """Sets the rousers of this SnmpConfig.

        USM users allowed read-only access  # noqa: E501

        :param rousers: The rousers of this SnmpConfig.  # noqa: E501
        :type: list[str]
        """

        self._rousers = rousers

    @property
    def sys_location(self):
        """Gets the sys_location of this SnmpConfig.  # noqa: E501

        SNMP system location  # noqa: E501

        :return: The sys_location of this SnmpConfig.  # noqa: E501
        :rtype: str
        """
        return self._sys_location

    @sys_location.setter
    def sys_location(self, sys_location):
        """Sets the sys_location of this SnmpConfig.

        SNMP system location  # noqa: E501

        :param sys_location: The sys_location of this SnmpConfig.  # noqa: E501
        :type: str
        """

        self._sys_location = sys_location

    @property
    def sys_contact(self):
        """Gets the sys_contact of this SnmpConfig.  # noqa: E501

        SNMP system contact  # noqa: E501

        :return: The sys_contact of this SnmpConfig.  # noqa: E501
        :rtype: str
        """
        return self._sys_contact

    @sys_contact.setter
    def sys_contact(self, sys_contact):
        """Sets the sys_contact of this SnmpConfig.

        SNMP system contact  # noqa: E501

        :param sys_contact: The sys_contact of this SnmpConfig.  # noqa: E501
        :type: str
        """

        self._sys_contact = sys_contact

    @property
    def trapcommunity(self):
        """Gets the trapcommunity of this SnmpConfig.  # noqa: E501

        default trap community. Cannot contain whitespace.  # noqa: E501

        :return: The trapcommunity of this SnmpConfig.  # noqa: E501
        :rtype: str
        """
        return self._trapcommunity

    @trapcommunity.setter
    def trapcommunity(self, trapcommunity):
        """Sets the trapcommunity of this SnmpConfig.

        default trap community. Cannot contain whitespace.  # noqa: E501

        :param trapcommunity: The trapcommunity of this SnmpConfig.  # noqa: E501
        :type: str
        """

        self._trapcommunity = trapcommunity

    @property
    def authtrapenable(self):
        """Gets the authtrapenable of this SnmpConfig.  # noqa: E501

        1 - enable SNMP authentication traps, 2 - disable SNMP authentication traps (default)  # noqa: E501

        :return: The authtrapenable of this SnmpConfig.  # noqa: E501
        :rtype: int
        """
        return self._authtrapenable

    @authtrapenable.setter
    def authtrapenable(self, authtrapenable):
        """Sets the authtrapenable of this SnmpConfig.

        1 - enable SNMP authentication traps, 2 - disable SNMP authentication traps (default)  # noqa: E501

        :param authtrapenable: The authtrapenable of this SnmpConfig.  # noqa: E501
        :type: int
        """

        self._authtrapenable = authtrapenable

    @property
    def disable_notifications(self):
        """Gets the disable_notifications of this SnmpConfig.  # noqa: E501

        Disable all SNMP notifications  # noqa: E501

        :return: The disable_notifications of this SnmpConfig.  # noqa: E501
        :rtype: bool
        """
        return self._disable_notifications

    @disable_notifications.setter
    def disable_notifications(self, disable_notifications):
        """Sets the disable_notifications of this SnmpConfig.

        Disable all SNMP notifications  # noqa: E501

        :param disable_notifications: The disable_notifications of this SnmpConfig.  # noqa: E501
        :type: bool
        """

        self._disable_notifications = disable_notifications

    @property
    def trap_destinations(self):
        """Gets the trap_destinations of this SnmpConfig.  # noqa: E501

        SNMP trap destinations for V1, V2C, and Inform notifications  # noqa: E501

        :return: The trap_destinations of this SnmpConfig.  # noqa: E501
        :rtype: list[TrapDestination]
        """
        return self._trap_destinations

    @trap_destinations.setter
    def trap_destinations(self, trap_destinations):
        """Sets the trap_destinations of this SnmpConfig.

        SNMP trap destinations for V1, V2C, and Inform notifications  # noqa: E501

        :param trap_destinations: The trap_destinations of this SnmpConfig.  # noqa: E501
        :type: list[TrapDestination]
        """

        self._trap_destinations = trap_destinations

    @property
    def agent_addresses(self):
        """Gets the agent_addresses of this SnmpConfig.  # noqa: E501

        Local binding addresses for the SNMP agent.  # noqa: E501

        :return: The agent_addresses of this SnmpConfig.  # noqa: E501
        :rtype: list[AgentAddress]
        """
        return self._agent_addresses

    @agent_addresses.setter
    def agent_addresses(self, agent_addresses):
        """Sets the agent_addresses of this SnmpConfig.

        Local binding addresses for the SNMP agent.  # noqa: E501

        :param agent_addresses: The agent_addresses of this SnmpConfig.  # noqa: E501
        :type: list[AgentAddress]
        """

        self._agent_addresses = agent_addresses

    @property
    def usm_users(self):
        """Gets the usm_users of this SnmpConfig.  # noqa: E501

        USM user definitions  # noqa: E501

        :return: The usm_users of this SnmpConfig.  # noqa: E501
        :rtype: list[UsmUser]
        """
        return self._usm_users

    @usm_users.setter
    def usm_users(self, usm_users):
        """Sets the usm_users of this SnmpConfig.

        USM user definitions  # noqa: E501

        :param usm_users: The usm_users of this SnmpConfig.  # noqa: E501
        :type: list[UsmUser]
        """

        self._usm_users = usm_users

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
        if issubclass(SnmpConfig, dict):
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
        if not isinstance(other, SnmpConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
