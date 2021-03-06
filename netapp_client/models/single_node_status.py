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

class SingleNodeStatus(object):
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
        'id': 'str',
        'stage': 'str',
        'error': 'str'
    }

    attribute_map = {
        'id': 'id',
        'stage': 'stage',
        'error': 'error'
    }

    def __init__(self, id=None, stage=None, error=None):  # noqa: E501
        """SingleNodeStatus - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._stage = None
        self._error = None
        self.discriminator = None
        self.id = id
        self.stage = stage
        if error is not None:
            self.error = error

    @property
    def id(self):
        """Gets the id of this SingleNodeStatus.  # noqa: E501


        :return: The id of this SingleNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SingleNodeStatus.


        :param id: The id of this SingleNodeStatus.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def stage(self):
        """Gets the stage of this SingleNodeStatus.  # noqa: E501

        log collection procedure stage  # noqa: E501

        :return: The stage of this SingleNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this SingleNodeStatus.

        log collection procedure stage  # noqa: E501

        :param stage: The stage of this SingleNodeStatus.  # noqa: E501
        :type: str
        """
        if stage is None:
            raise ValueError("Invalid value for `stage`, must not be `None`")  # noqa: E501
        allowed_values = ["queued", "collecting", "done"]  # noqa: E501
        if stage not in allowed_values:
            raise ValueError(
                "Invalid value for `stage` ({0}), must be one of {1}"  # noqa: E501
                .format(stage, allowed_values)
            )

        self._stage = stage

    @property
    def error(self):
        """Gets the error of this SingleNodeStatus.  # noqa: E501

        an error message if a problem has occurred on this grid node, otherwise null  # noqa: E501

        :return: The error of this SingleNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this SingleNodeStatus.

        an error message if a problem has occurred on this grid node, otherwise null  # noqa: E501

        :param error: The error of this SingleNodeStatus.  # noqa: E501
        :type: str
        """

        self._error = error

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
        if issubclass(SingleNodeStatus, dict):
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
        if not isinstance(other, SingleNodeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
