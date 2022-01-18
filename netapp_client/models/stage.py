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

class Stage(object):
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
        'text': 'str',
        'key': 'str'
    }

    attribute_map = {
        'text': 'text',
        'key': 'key'
    }

    def __init__(self, text=None, key=None):  # noqa: E501
        """Stage - a model defined in Swagger"""  # noqa: E501
        self._text = None
        self._key = None
        self.discriminator = None
        self.text = text
        self.key = key

    @property
    def text(self):
        """Gets the text of this Stage.  # noqa: E501

        the localized name of the stage  # noqa: E501

        :return: The text of this Stage.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Stage.

        the localized name of the stage  # noqa: E501

        :param text: The text of this Stage.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def key(self):
        """Gets the key of this Stage.  # noqa: E501

        an i18n key representing the current stage  # noqa: E501

        :return: The key of this Stage.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Stage.

        an i18n key representing the current stage  # noqa: E501

        :param key: The key of this Stage.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501
        allowed_values = ["maintenance.install.steps.retrieveGridNodeConfig.name", "maintenance.install.steps.hotfixDownload.name", "maintenance.install.steps.configureNetworking.name", "maintenance.install.steps.hotfixApply.name", "maintenance.install.steps.configureServices.name", "maintenance.install.steps.waitingForAdmin.name", "maintenance.install.steps.synchronizeNtp.name", "maintenance.install.steps.startDynip.name", "maintenance.install.steps.installModeReboot.name", "maintenance.install.steps.waitForManualSteps.name", "maintenance.install.steps.preparingStorage.name", "maintenance.install.steps.waitingToStartServices.name", "maintenance.install.steps.startCassandra.name", "maintenance.install.steps.startCassandraWithProgress.name", "maintenance.install.steps.startAdc.name", "maintenance.install.steps.streamingCassandra.name", "maintenance.install.steps.streamingCassandraWithProgress.name", "maintenance.install.steps.waitForCassandra.name", "maintenance.install.steps.createCassandraSchema.name", "maintenance.install.steps.expandingCassandra.name", "maintenance.install.steps.recoverCassandra.name", "maintenance.install.steps.startServices.name", "maintenance.install.steps.waitForOtherGridNodes.name", "maintenance.install.steps.waitForDownload.name", "maintenance.install.steps.done.name"]  # noqa: E501
        if key not in allowed_values:
            raise ValueError(
                "Invalid value for `key` ({0}), must be one of {1}"  # noqa: E501
                .format(key, allowed_values)
            )

        self._key = key

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
        if issubclass(Stage, dict):
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
        if not isinstance(other, Stage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
