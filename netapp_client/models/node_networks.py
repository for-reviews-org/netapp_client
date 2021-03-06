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

class NodeNetworks(object):
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
        'grid': 'AllOfnodeNetworksGrid',
        'admin': 'AllOfnodeNetworksAdmin',
        'client': 'AllOfnodeNetworksClient'
    }

    attribute_map = {
        'grid': 'grid',
        'admin': 'admin',
        'client': 'client'
    }

    def __init__(self, grid=None, admin=None, client=None):  # noqa: E501
        """NodeNetworks - a model defined in Swagger"""  # noqa: E501
        self._grid = None
        self._admin = None
        self._client = None
        self.discriminator = None
        self.grid = grid
        if admin is not None:
            self.admin = admin
        if client is not None:
            self.client = client

    @property
    def grid(self):
        """Gets the grid of this NodeNetworks.  # noqa: E501


        :return: The grid of this NodeNetworks.  # noqa: E501
        :rtype: AllOfnodeNetworksGrid
        """
        return self._grid

    @grid.setter
    def grid(self, grid):
        """Sets the grid of this NodeNetworks.


        :param grid: The grid of this NodeNetworks.  # noqa: E501
        :type: AllOfnodeNetworksGrid
        """
        if grid is None:
            raise ValueError("Invalid value for `grid`, must not be `None`")  # noqa: E501

        self._grid = grid

    @property
    def admin(self):
        """Gets the admin of this NodeNetworks.  # noqa: E501


        :return: The admin of this NodeNetworks.  # noqa: E501
        :rtype: AllOfnodeNetworksAdmin
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this NodeNetworks.


        :param admin: The admin of this NodeNetworks.  # noqa: E501
        :type: AllOfnodeNetworksAdmin
        """

        self._admin = admin

    @property
    def client(self):
        """Gets the client of this NodeNetworks.  # noqa: E501


        :return: The client of this NodeNetworks.  # noqa: E501
        :rtype: AllOfnodeNetworksClient
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this NodeNetworks.


        :param client: The client of this NodeNetworks.  # noqa: E501
        :type: AllOfnodeNetworksClient
        """

        self._client = client

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
        if issubclass(NodeNetworks, dict):
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
        if not isinstance(other, NodeNetworks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
