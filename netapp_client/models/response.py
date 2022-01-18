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

class Response(object):
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
        'response_time': 'datetime',
        'status': 'str',
        'api_version': 'str',
        'deprecated': 'bool',
        'data': 'object'
    }

    attribute_map = {
        'response_time': 'responseTime',
        'status': 'status',
        'api_version': 'apiVersion',
        'deprecated': 'deprecated',
        'data': 'data'
    }

    def __init__(self, response_time=None, status=None, api_version=None, deprecated=False, data=None):  # noqa: E501
        """Response - a model defined in Swagger"""  # noqa: E501
        self._response_time = None
        self._status = None
        self._api_version = None
        self._deprecated = None
        self._data = None
        self.discriminator = None
        if response_time is not None:
            self.response_time = response_time
        self.status = status
        self.api_version = api_version
        if deprecated is not None:
            self.deprecated = deprecated
        if data is not None:
            self.data = data

    @property
    def response_time(self):
        """Gets the response_time of this Response.  # noqa: E501

        the date and time when the response was generated  # noqa: E501

        :return: The response_time of this Response.  # noqa: E501
        :rtype: datetime
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        """Sets the response_time of this Response.

        the date and time when the response was generated  # noqa: E501

        :param response_time: The response_time of this Response.  # noqa: E501
        :type: datetime
        """

        self._response_time = response_time

    @property
    def status(self):
        """Gets the status of this Response.  # noqa: E501

        the result of the request  # noqa: E501

        :return: The status of this Response.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Response.

        the result of the request  # noqa: E501

        :param status: The status of this Response.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["success", "error"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def api_version(self):
        """Gets the api_version of this Response.  # noqa: E501

        the major and minor version of the API  # noqa: E501

        :return: The api_version of this Response.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this Response.

        the major and minor version of the API  # noqa: E501

        :param api_version: The api_version of this Response.  # noqa: E501
        :type: str
        """
        if api_version is None:
            raise ValueError("Invalid value for `api_version`, must not be `None`")  # noqa: E501

        self._api_version = api_version

    @property
    def deprecated(self):
        """Gets the deprecated of this Response.  # noqa: E501

        whether the requested API is deprecated, default false  # noqa: E501

        :return: The deprecated of this Response.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this Response.

        whether the requested API is deprecated, default false  # noqa: E501

        :param deprecated: The deprecated of this Response.  # noqa: E501
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def data(self):
        """Gets the data of this Response.  # noqa: E501

        the response data for the request (required on success and optional on error; type and content vary by request)  # noqa: E501

        :return: The data of this Response.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Response.

        the response data for the request (required on success and optional on error; type and content vary by request)  # noqa: E501

        :param data: The data of this Response.  # noqa: E501
        :type: object
        """

        self._data = data

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
        if issubclass(Response, dict):
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
        if not isinstance(other, Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
