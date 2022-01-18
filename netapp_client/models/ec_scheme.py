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

class EcScheme(object):
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
        'grid_node_redundancy': 'int',
        'storage_overhead': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'grid_node_redundancy': 'gridNodeRedundancy',
        'storage_overhead': 'storageOverhead'
    }

    def __init__(self, id=None, name=None, grid_node_redundancy=None, storage_overhead=None):  # noqa: E501
        """EcScheme - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._grid_node_redundancy = None
        self._storage_overhead = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.grid_node_redundancy = grid_node_redundancy
        self.storage_overhead = storage_overhead

    @property
    def id(self):
        """Gets the id of this EcScheme.  # noqa: E501

        a unique identifier for the Erasure Coding Scheme (generated automatically)  # noqa: E501

        :return: The id of this EcScheme.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EcScheme.

        a unique identifier for the Erasure Coding Scheme (generated automatically)  # noqa: E501

        :param id: The id of this EcScheme.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this EcScheme.  # noqa: E501

        the EC Scheme's name  # noqa: E501

        :return: The name of this EcScheme.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EcScheme.

        the EC Scheme's name  # noqa: E501

        :param name: The name of this EcScheme.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def grid_node_redundancy(self):
        """Gets the grid_node_redundancy of this EcScheme.  # noqa: E501

        the number of node outages that can be tolerated  # noqa: E501

        :return: The grid_node_redundancy of this EcScheme.  # noqa: E501
        :rtype: int
        """
        return self._grid_node_redundancy

    @grid_node_redundancy.setter
    def grid_node_redundancy(self, grid_node_redundancy):
        """Sets the grid_node_redundancy of this EcScheme.

        the number of node outages that can be tolerated  # noqa: E501

        :param grid_node_redundancy: The grid_node_redundancy of this EcScheme.  # noqa: E501
        :type: int
        """
        if grid_node_redundancy is None:
            raise ValueError("Invalid value for `grid_node_redundancy`, must not be `None`")  # noqa: E501

        self._grid_node_redundancy = grid_node_redundancy

    @property
    def storage_overhead(self):
        """Gets the storage_overhead of this EcScheme.  # noqa: E501

        the additional storage percent required to manage parity fragments for each erasure coded object   # noqa: E501

        :return: The storage_overhead of this EcScheme.  # noqa: E501
        :rtype: int
        """
        return self._storage_overhead

    @storage_overhead.setter
    def storage_overhead(self, storage_overhead):
        """Sets the storage_overhead of this EcScheme.

        the additional storage percent required to manage parity fragments for each erasure coded object   # noqa: E501

        :param storage_overhead: The storage_overhead of this EcScheme.  # noqa: E501
        :type: int
        """
        if storage_overhead is None:
            raise ValueError("Invalid value for `storage_overhead`, must not be `None`")  # noqa: E501

        self._storage_overhead = storage_overhead

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
        if issubclass(EcScheme, dict):
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
        if not isinstance(other, EcScheme):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other