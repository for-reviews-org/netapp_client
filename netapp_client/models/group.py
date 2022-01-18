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
from netapp_client.models.post_group_request import PostGroupRequest  # noqa: F401,E501

class Group(PostGroupRequest):
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
        'account_id': 'str',
        'id': 'str',
        'federated': 'bool',
        'group_urn': 'str'
    }
    if hasattr(PostGroupRequest, "swagger_types"):
        swagger_types.update(PostGroupRequest.swagger_types)

    attribute_map = {
        'account_id': 'accountId',
        'id': 'id',
        'federated': 'federated',
        'group_urn': 'groupURN'
    }
    if hasattr(PostGroupRequest, "attribute_map"):
        attribute_map.update(PostGroupRequest.attribute_map)

    def __init__(self, account_id=None, id=None, federated=None, group_urn=None, *args, **kwargs):  # noqa: E501
        """Group - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._id = None
        self._federated = None
        self._group_urn = None
        self.discriminator = None
        self.account_id = account_id
        self.id = id
        self.federated = federated
        self.group_urn = group_urn
        PostGroupRequest.__init__(self, *args, **kwargs)

    @property
    def account_id(self):
        """Gets the account_id of this Group.  # noqa: E501

        Storage Tenant Account ID, or zero for Grid Administrators  # noqa: E501

        :return: The account_id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Group.

        Storage Tenant Account ID, or zero for Grid Administrators  # noqa: E501

        :param account_id: The account_id of this Group.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def id(self):
        """Gets the id of this Group.  # noqa: E501

        UUID for the Group (generated automatically)  # noqa: E501

        :return: The id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Group.

        UUID for the Group (generated automatically)  # noqa: E501

        :param id: The id of this Group.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def federated(self):
        """Gets the federated of this Group.  # noqa: E501

        true if the Group is federated, for example, an LDAP Group  # noqa: E501

        :return: The federated of this Group.  # noqa: E501
        :rtype: bool
        """
        return self._federated

    @federated.setter
    def federated(self, federated):
        """Sets the federated of this Group.

        true if the Group is federated, for example, an LDAP Group  # noqa: E501

        :param federated: The federated of this Group.  # noqa: E501
        :type: bool
        """
        if federated is None:
            raise ValueError("Invalid value for `federated`, must not be `None`")  # noqa: E501

        self._federated = federated

    @property
    def group_urn(self):
        """Gets the group_urn of this Group.  # noqa: E501

        contains the Group uniqueName and Account ID (generated automatically)  # noqa: E501

        :return: The group_urn of this Group.  # noqa: E501
        :rtype: str
        """
        return self._group_urn

    @group_urn.setter
    def group_urn(self, group_urn):
        """Sets the group_urn of this Group.

        contains the Group uniqueName and Account ID (generated automatically)  # noqa: E501

        :param group_urn: The group_urn of this Group.  # noqa: E501
        :type: str
        """
        if group_urn is None:
            raise ValueError("Invalid value for `group_urn`, must not be `None`")  # noqa: E501

        self._group_urn = group_urn

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
        if issubclass(Group, dict):
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
        if not isinstance(other, Group):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
