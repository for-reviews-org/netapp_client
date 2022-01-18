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

class CertificatePublicData(object):
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
        'server_certificate_encoded': 'str',
        'ca_bundle_encoded': 'str'
    }

    attribute_map = {
        'server_certificate_encoded': 'serverCertificateEncoded',
        'ca_bundle_encoded': 'caBundleEncoded'
    }

    def __init__(self, server_certificate_encoded=None, ca_bundle_encoded=None):  # noqa: E501
        """CertificatePublicData - a model defined in Swagger"""  # noqa: E501
        self._server_certificate_encoded = None
        self._ca_bundle_encoded = None
        self.discriminator = None
        if server_certificate_encoded is not None:
            self.server_certificate_encoded = server_certificate_encoded
        if ca_bundle_encoded is not None:
            self.ca_bundle_encoded = ca_bundle_encoded

    @property
    def server_certificate_encoded(self):
        """Gets the server_certificate_encoded of this CertificatePublicData.  # noqa: E501

        X.509 server certificate in PEM-encoding; omit or null if using default certificates  # noqa: E501

        :return: The server_certificate_encoded of this CertificatePublicData.  # noqa: E501
        :rtype: str
        """
        return self._server_certificate_encoded

    @server_certificate_encoded.setter
    def server_certificate_encoded(self, server_certificate_encoded):
        """Sets the server_certificate_encoded of this CertificatePublicData.

        X.509 server certificate in PEM-encoding; omit or null if using default certificates  # noqa: E501

        :param server_certificate_encoded: The server_certificate_encoded of this CertificatePublicData.  # noqa: E501
        :type: str
        """

        self._server_certificate_encoded = server_certificate_encoded

    @property
    def ca_bundle_encoded(self):
        """Gets the ca_bundle_encoded of this CertificatePublicData.  # noqa: E501

        intermediate CA certificate bundle in concatenated PEM-encoding; omit or null when there is no intermediate CA  # noqa: E501

        :return: The ca_bundle_encoded of this CertificatePublicData.  # noqa: E501
        :rtype: str
        """
        return self._ca_bundle_encoded

    @ca_bundle_encoded.setter
    def ca_bundle_encoded(self, ca_bundle_encoded):
        """Sets the ca_bundle_encoded of this CertificatePublicData.

        intermediate CA certificate bundle in concatenated PEM-encoding; omit or null when there is no intermediate CA  # noqa: E501

        :param ca_bundle_encoded: The ca_bundle_encoded of this CertificatePublicData.  # noqa: E501
        :type: str
        """

        self._ca_bundle_encoded = ca_bundle_encoded

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
        if issubclass(CertificatePublicData, dict):
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
        if not isinstance(other, CertificatePublicData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
