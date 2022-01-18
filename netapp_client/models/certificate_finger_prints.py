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

class CertificateFingerPrints(object):
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
        'sha_1': 'str',
        'sha_256': 'str'
    }

    attribute_map = {
        'sha_1': 'SHA-1',
        'sha_256': 'SHA-256'
    }

    def __init__(self, sha_1=None, sha_256=None):  # noqa: E501
        """CertificateFingerPrints - a model defined in Swagger"""  # noqa: E501
        self._sha_1 = None
        self._sha_256 = None
        self.discriminator = None
        self.sha_1 = sha_1
        self.sha_256 = sha_256

    @property
    def sha_1(self):
        """Gets the sha_1 of this CertificateFingerPrints.  # noqa: E501

        certificate fingerprint using the SHA-1 hash function  # noqa: E501

        :return: The sha_1 of this CertificateFingerPrints.  # noqa: E501
        :rtype: str
        """
        return self._sha_1

    @sha_1.setter
    def sha_1(self, sha_1):
        """Sets the sha_1 of this CertificateFingerPrints.

        certificate fingerprint using the SHA-1 hash function  # noqa: E501

        :param sha_1: The sha_1 of this CertificateFingerPrints.  # noqa: E501
        :type: str
        """
        if sha_1 is None:
            raise ValueError("Invalid value for `sha_1`, must not be `None`")  # noqa: E501

        self._sha_1 = sha_1

    @property
    def sha_256(self):
        """Gets the sha_256 of this CertificateFingerPrints.  # noqa: E501

        certificate fingerprint using the SHA-256 hash function  # noqa: E501

        :return: The sha_256 of this CertificateFingerPrints.  # noqa: E501
        :rtype: str
        """
        return self._sha_256

    @sha_256.setter
    def sha_256(self, sha_256):
        """Sets the sha_256 of this CertificateFingerPrints.

        certificate fingerprint using the SHA-256 hash function  # noqa: E501

        :param sha_256: The sha_256 of this CertificateFingerPrints.  # noqa: E501
        :type: str
        """
        if sha_256 is None:
            raise ValueError("Invalid value for `sha_256`, must not be `None`")  # noqa: E501

        self._sha_256 = sha_256

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
        if issubclass(CertificateFingerPrints, dict):
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
        if not isinstance(other, CertificateFingerPrints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
