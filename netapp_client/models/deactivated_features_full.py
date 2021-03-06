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

class DeactivatedFeaturesFull(object):
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
        'grid': 'PermissionsListExceptRoot',
        'tenant': 'TenantPermissionsListExceptRoot'
    }

    attribute_map = {
        'grid': 'grid',
        'tenant': 'tenant'
    }

    def __init__(self, grid=None, tenant=None):  # noqa: E501
        """DeactivatedFeaturesFull - a model defined in Swagger"""  # noqa: E501
        self._grid = None
        self._tenant = None
        self.discriminator = None
        if grid is not None:
            self.grid = grid
        if tenant is not None:
            self.tenant = tenant

    @property
    def grid(self):
        """Gets the grid of this DeactivatedFeaturesFull.  # noqa: E501


        :return: The grid of this DeactivatedFeaturesFull.  # noqa: E501
        :rtype: PermissionsListExceptRoot
        """
        return self._grid

    @grid.setter
    def grid(self, grid):
        """Sets the grid of this DeactivatedFeaturesFull.


        :param grid: The grid of this DeactivatedFeaturesFull.  # noqa: E501
        :type: PermissionsListExceptRoot
        """

        self._grid = grid

    @property
    def tenant(self):
        """Gets the tenant of this DeactivatedFeaturesFull.  # noqa: E501


        :return: The tenant of this DeactivatedFeaturesFull.  # noqa: E501
        :rtype: TenantPermissionsListExceptRoot
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this DeactivatedFeaturesFull.


        :param tenant: The tenant of this DeactivatedFeaturesFull.  # noqa: E501
        :type: TenantPermissionsListExceptRoot
        """

        self._tenant = tenant

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
        if issubclass(DeactivatedFeaturesFull, dict):
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
        if not isinstance(other, DeactivatedFeaturesFull):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
