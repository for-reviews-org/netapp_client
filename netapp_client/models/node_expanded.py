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
from swagger_client.models.node import Node  # noqa: F401,E501

class NodeExpanded(Node):
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
        'hardware': 'Hardware',
        'progress': 'Progress',
        'current_cassandra_data': 'int',
        'estimated_cassandra_data': 'int',
        'site_cassandra_data': 'int'
    }
    if hasattr(Node, "swagger_types"):
        swagger_types.update(Node.swagger_types)

    attribute_map = {
        'hardware': 'hardware',
        'progress': 'progress',
        'current_cassandra_data': 'currentCassandraData',
        'estimated_cassandra_data': 'estimatedCassandraData',
        'site_cassandra_data': 'siteCassandraData'
    }
    if hasattr(Node, "attribute_map"):
        attribute_map.update(Node.attribute_map)

    def __init__(self, hardware=None, progress=None, current_cassandra_data=None, estimated_cassandra_data=None, site_cassandra_data=None, *args, **kwargs):  # noqa: E501
        """NodeExpanded - a model defined in Swagger"""  # noqa: E501
        self._hardware = None
        self._progress = None
        self._current_cassandra_data = None
        self._estimated_cassandra_data = None
        self._site_cassandra_data = None
        self.discriminator = None
        if hardware is not None:
            self.hardware = hardware
        if progress is not None:
            self.progress = progress
        if current_cassandra_data is not None:
            self.current_cassandra_data = current_cassandra_data
        if estimated_cassandra_data is not None:
            self.estimated_cassandra_data = estimated_cassandra_data
        if site_cassandra_data is not None:
            self.site_cassandra_data = site_cassandra_data
        Node.__init__(self, *args, **kwargs)

    @property
    def hardware(self):
        """Gets the hardware of this NodeExpanded.  # noqa: E501


        :return: The hardware of this NodeExpanded.  # noqa: E501
        :rtype: Hardware
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this NodeExpanded.


        :param hardware: The hardware of this NodeExpanded.  # noqa: E501
        :type: Hardware
        """

        self._hardware = hardware

    @property
    def progress(self):
        """Gets the progress of this NodeExpanded.  # noqa: E501


        :return: The progress of this NodeExpanded.  # noqa: E501
        :rtype: Progress
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this NodeExpanded.


        :param progress: The progress of this NodeExpanded.  # noqa: E501
        :type: Progress
        """

        self._progress = progress

    @property
    def current_cassandra_data(self):
        """Gets the current_cassandra_data of this NodeExpanded.  # noqa: E501

        The number of bytes of Cassandra data currently on the new Storage Node. This number and the Estimated Cassandra Data Load are used to calculate the progress of the Cassandra data streaming stage during an expansion of an existing site.   # noqa: E501

        :return: The current_cassandra_data of this NodeExpanded.  # noqa: E501
        :rtype: int
        """
        return self._current_cassandra_data

    @current_cassandra_data.setter
    def current_cassandra_data(self, current_cassandra_data):
        """Sets the current_cassandra_data of this NodeExpanded.

        The number of bytes of Cassandra data currently on the new Storage Node. This number and the Estimated Cassandra Data Load are used to calculate the progress of the Cassandra data streaming stage during an expansion of an existing site.   # noqa: E501

        :param current_cassandra_data: The current_cassandra_data of this NodeExpanded.  # noqa: E501
        :type: int
        """

        self._current_cassandra_data = current_cassandra_data

    @property
    def estimated_cassandra_data(self):
        """Gets the estimated_cassandra_data of this NodeExpanded.  # noqa: E501

        The total number of bytes of Cassandra data expected for the new Storage Node. This number and the Current Cassandra Data Load are used to calculate the progress of the Cassandra data streaming stage during an expansion of an existing site.   # noqa: E501

        :return: The estimated_cassandra_data of this NodeExpanded.  # noqa: E501
        :rtype: int
        """
        return self._estimated_cassandra_data

    @estimated_cassandra_data.setter
    def estimated_cassandra_data(self, estimated_cassandra_data):
        """Sets the estimated_cassandra_data of this NodeExpanded.

        The total number of bytes of Cassandra data expected for the new Storage Node. This number and the Current Cassandra Data Load are used to calculate the progress of the Cassandra data streaming stage during an expansion of an existing site.   # noqa: E501

        :param estimated_cassandra_data: The estimated_cassandra_data of this NodeExpanded.  # noqa: E501
        :type: int
        """

        self._estimated_cassandra_data = estimated_cassandra_data

    @property
    def site_cassandra_data(self):
        """Gets the site_cassandra_data of this NodeExpanded.  # noqa: E501

        The total number of bytes of Cassandra data in the same site at the start of the expansion. This number is used to calculate the Estimated Cassandra Data Load when data streaming begins during an expansion of an existing site.   # noqa: E501

        :return: The site_cassandra_data of this NodeExpanded.  # noqa: E501
        :rtype: int
        """
        return self._site_cassandra_data

    @site_cassandra_data.setter
    def site_cassandra_data(self, site_cassandra_data):
        """Sets the site_cassandra_data of this NodeExpanded.

        The total number of bytes of Cassandra data in the same site at the start of the expansion. This number is used to calculate the Estimated Cassandra Data Load when data streaming begins during an expansion of an existing site.   # noqa: E501

        :param site_cassandra_data: The site_cassandra_data of this NodeExpanded.  # noqa: E501
        :type: int
        """

        self._site_cassandra_data = site_cassandra_data

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
        if issubclass(NodeExpanded, dict):
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
        if not isinstance(other, NodeExpanded):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other