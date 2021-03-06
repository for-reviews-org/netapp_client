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
from netapp_client.models.response import Response  # noqa: F401,E501

class PassphraseGetResponse(Response):
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
        'read_only': 'bool',
        'alerts': 'list[PassphraseGetAlert]'
    }
    if hasattr(Response, "swagger_types"):
        swagger_types.update(Response.swagger_types)

    attribute_map = {
        'read_only': 'readOnly',
        'alerts': 'alerts'
    }
    if hasattr(Response, "attribute_map"):
        attribute_map.update(Response.attribute_map)

    def __init__(self, read_only=None, alerts=None, *args, **kwargs):  # noqa: E501
        """PassphraseGetResponse - a model defined in Swagger"""  # noqa: E501
        self._read_only = None
        self._alerts = None
        self.discriminator = None
        if read_only is not None:
            self.read_only = read_only
        if alerts is not None:
            self.alerts = alerts
        Response.__init__(self, *args, **kwargs)

    @property
    def read_only(self):
        """Gets the read_only of this PassphraseGetResponse.  # noqa: E501

        true if the provisioning passphrase is currently being updated  # noqa: E501

        :return: The read_only of this PassphraseGetResponse.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this PassphraseGetResponse.

        true if the provisioning passphrase is currently being updated  # noqa: E501

        :param read_only: The read_only of this PassphraseGetResponse.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def alerts(self):
        """Gets the alerts of this PassphraseGetResponse.  # noqa: E501

        Only present when the provisioning passphrase is currently being updated or when the last update failed.   # noqa: E501

        :return: The alerts of this PassphraseGetResponse.  # noqa: E501
        :rtype: list[PassphraseGetAlert]
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this PassphraseGetResponse.

        Only present when the provisioning passphrase is currently being updated or when the last update failed.   # noqa: E501

        :param alerts: The alerts of this PassphraseGetResponse.  # noqa: E501
        :type: list[PassphraseGetAlert]
        """

        self._alerts = alerts

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
        if issubclass(PassphraseGetResponse, dict):
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
        if not isinstance(other, PassphraseGetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
