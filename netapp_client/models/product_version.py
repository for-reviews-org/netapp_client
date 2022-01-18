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

class ProductVersion(object):
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
        'product_version': 'str'
    }

    attribute_map = {
        'product_version': 'productVersion'
    }

    def __init__(self, product_version=None):  # noqa: E501
        """ProductVersion - a model defined in Swagger"""  # noqa: E501
        self._product_version = None
        self.discriminator = None
        self.product_version = product_version

    @property
    def product_version(self):
        """Gets the product_version of this ProductVersion.  # noqa: E501

        the product release version currently running on the Admin Node serving the request   # noqa: E501

        :return: The product_version of this ProductVersion.  # noqa: E501
        :rtype: str
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """Sets the product_version of this ProductVersion.

        the product release version currently running on the Admin Node serving the request   # noqa: E501

        :param product_version: The product_version of this ProductVersion.  # noqa: E501
        :type: str
        """
        if product_version is None:
            raise ValueError("Invalid value for `product_version`, must not be `None`")  # noqa: E501

        self._product_version = product_version

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
        if issubclass(ProductVersion, dict):
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
        if not isinstance(other, ProductVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
