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

class HealthTopologySiteLevel(object):
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
        'id': 'HealthTopologyId',
        'name': 'HealthTopologyName',
        'unique_name': 'HealthTopologyUniqueName',
        'type': 'str',
        'oid': 'HealthTopologyOid',
        'state': 'HealthTopologyState',
        'severity': 'HealthTopologySeverity',
        'children': 'list[HealthTopologyNodeLevel]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'unique_name': 'uniqueName',
        'type': 'type',
        'oid': 'oid',
        'state': 'state',
        'severity': 'severity',
        'children': 'children'
    }

    def __init__(self, id=None, name=None, unique_name=None, type=None, oid=None, state=None, severity=None, children=None):  # noqa: E501
        """HealthTopologySiteLevel - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._unique_name = None
        self._type = None
        self._oid = None
        self._state = None
        self._severity = None
        self._children = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.unique_name = unique_name
        self.type = type
        self.oid = oid
        self.state = state
        self.severity = severity
        if children is not None:
            self.children = children

    @property
    def id(self):
        """Gets the id of this HealthTopologySiteLevel.  # noqa: E501


        :return: The id of this HealthTopologySiteLevel.  # noqa: E501
        :rtype: HealthTopologyId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HealthTopologySiteLevel.


        :param id: The id of this HealthTopologySiteLevel.  # noqa: E501
        :type: HealthTopologyId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this HealthTopologySiteLevel.  # noqa: E501


        :return: The name of this HealthTopologySiteLevel.  # noqa: E501
        :rtype: HealthTopologyName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HealthTopologySiteLevel.


        :param name: The name of this HealthTopologySiteLevel.  # noqa: E501
        :type: HealthTopologyName
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def unique_name(self):
        """Gets the unique_name of this HealthTopologySiteLevel.  # noqa: E501


        :return: The unique_name of this HealthTopologySiteLevel.  # noqa: E501
        :rtype: HealthTopologyUniqueName
        """
        return self._unique_name

    @unique_name.setter
    def unique_name(self, unique_name):
        """Sets the unique_name of this HealthTopologySiteLevel.


        :param unique_name: The unique_name of this HealthTopologySiteLevel.  # noqa: E501
        :type: HealthTopologyUniqueName
        """
        if unique_name is None:
            raise ValueError("Invalid value for `unique_name`, must not be `None`")  # noqa: E501

        self._unique_name = unique_name

    @property
    def type(self):
        """Gets the type of this HealthTopologySiteLevel.  # noqa: E501


        :return: The type of this HealthTopologySiteLevel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HealthTopologySiteLevel.


        :param type: The type of this HealthTopologySiteLevel.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["site"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def oid(self):
        """Gets the oid of this HealthTopologySiteLevel.  # noqa: E501


        :return: The oid of this HealthTopologySiteLevel.  # noqa: E501
        :rtype: HealthTopologyOid
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """Sets the oid of this HealthTopologySiteLevel.


        :param oid: The oid of this HealthTopologySiteLevel.  # noqa: E501
        :type: HealthTopologyOid
        """
        if oid is None:
            raise ValueError("Invalid value for `oid`, must not be `None`")  # noqa: E501

        self._oid = oid

    @property
    def state(self):
        """Gets the state of this HealthTopologySiteLevel.  # noqa: E501


        :return: The state of this HealthTopologySiteLevel.  # noqa: E501
        :rtype: HealthTopologyState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this HealthTopologySiteLevel.


        :param state: The state of this HealthTopologySiteLevel.  # noqa: E501
        :type: HealthTopologyState
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def severity(self):
        """Gets the severity of this HealthTopologySiteLevel.  # noqa: E501


        :return: The severity of this HealthTopologySiteLevel.  # noqa: E501
        :rtype: HealthTopologySeverity
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this HealthTopologySiteLevel.


        :param severity: The severity of this HealthTopologySiteLevel.  # noqa: E501
        :type: HealthTopologySeverity
        """
        if severity is None:
            raise ValueError("Invalid value for `severity`, must not be `None`")  # noqa: E501

        self._severity = severity

    @property
    def children(self):
        """Gets the children of this HealthTopologySiteLevel.  # noqa: E501


        :return: The children of this HealthTopologySiteLevel.  # noqa: E501
        :rtype: list[HealthTopologyNodeLevel]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this HealthTopologySiteLevel.


        :param children: The children of this HealthTopologySiteLevel.  # noqa: E501
        :type: list[HealthTopologyNodeLevel]
        """

        self._children = children

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
        if issubclass(HealthTopologySiteLevel, dict):
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
        if not isinstance(other, HealthTopologySiteLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
