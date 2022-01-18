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
from netapp_client.models.patch_group_request import PatchGroupRequest  # noqa: F401,E501

class PostGroupRequest(PatchGroupRequest):
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
        'unique_name': 'str'
    }
    if hasattr(PatchGroupRequest, "swagger_types"):
        swagger_types.update(PatchGroupRequest.swagger_types)

    attribute_map = {
        'unique_name': 'uniqueName'
    }
    if hasattr(PatchGroupRequest, "attribute_map"):
        attribute_map.update(PatchGroupRequest.attribute_map)

    def __init__(self, unique_name=None, *args, **kwargs):  # noqa: E501
        """PostGroupRequest - a model defined in Swagger"""  # noqa: E501
        self._unique_name = None
        self.discriminator = None
        if unique_name is not None:
            self.unique_name = unique_name
        PatchGroupRequest.__init__(self, *args, **kwargs)

    @property
    def unique_name(self):
        """Gets the unique_name of this PostGroupRequest.  # noqa: E501

        the machine-readable name for the Group (unique within an Account; must begin with group/ or federated-group/)  # noqa: E501

        :return: The unique_name of this PostGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._unique_name

    @unique_name.setter
    def unique_name(self, unique_name):
        """Sets the unique_name of this PostGroupRequest.

        the machine-readable name for the Group (unique within an Account; must begin with group/ or federated-group/)  # noqa: E501

        :param unique_name: The unique_name of this PostGroupRequest.  # noqa: E501
        :type: str
        """

        self._unique_name = unique_name

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
        if issubclass(PostGroupRequest, dict):
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
        if not isinstance(other, PostGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
