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
from netapp_client.models.alert_rule_post_body import AlertRulePostBody  # noqa: F401,E501

class AlertRule(AlertRulePostBody):
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
        'custom': 'bool',
        'group': 'str',
        'original_properties': 'OriginalProperties'
    }
    if hasattr(AlertRulePostBody, "swagger_types"):
        swagger_types.update(AlertRulePostBody.swagger_types)

    attribute_map = {
        'id': 'id',
        'custom': 'custom',
        'group': 'group',
        'original_properties': 'originalProperties'
    }
    if hasattr(AlertRulePostBody, "attribute_map"):
        attribute_map.update(AlertRulePostBody.attribute_map)

    def __init__(self, id=None, custom=None, group=None, original_properties=None, *args, **kwargs):  # noqa: E501
        """AlertRule - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._custom = None
        self._group = None
        self._original_properties = None
        self.discriminator = None
        self.id = id
        self.custom = custom
        self.group = group
        if original_properties is not None:
            self.original_properties = original_properties
        AlertRulePostBody.__init__(self, *args, **kwargs)

    @property
    def id(self):
        """Gets the id of this AlertRule.  # noqa: E501

        the unique identifier of the alert rule  # noqa: E501

        :return: The id of this AlertRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertRule.

        the unique identifier of the alert rule  # noqa: E501

        :param id: The id of this AlertRule.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def custom(self):
        """Gets the custom of this AlertRule.  # noqa: E501

        whether this is a user-created rule (true) or a default rule (false)  # noqa: E501

        :return: The custom of this AlertRule.  # noqa: E501
        :rtype: bool
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this AlertRule.

        whether this is a user-created rule (true) or a default rule (false)  # noqa: E501

        :param custom: The custom of this AlertRule.  # noqa: E501
        :type: bool
        """
        if custom is None:
            raise ValueError("Invalid value for `custom`, must not be `None`")  # noqa: E501

        self._custom = custom

    @property
    def group(self):
        """Gets the group of this AlertRule.  # noqa: E501

        the name of the group this rule belongs to  # noqa: E501

        :return: The group of this AlertRule.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this AlertRule.

        the name of the group this rule belongs to  # noqa: E501

        :param group: The group of this AlertRule.  # noqa: E501
        :type: str
        """
        if group is None:
            raise ValueError("Invalid value for `group`, must not be `None`")  # noqa: E501

        self._group = group

    @property
    def original_properties(self):
        """Gets the original_properties of this AlertRule.  # noqa: E501


        :return: The original_properties of this AlertRule.  # noqa: E501
        :rtype: OriginalProperties
        """
        return self._original_properties

    @original_properties.setter
    def original_properties(self, original_properties):
        """Sets the original_properties of this AlertRule.


        :param original_properties: The original_properties of this AlertRule.  # noqa: E501
        :type: OriginalProperties
        """

        self._original_properties = original_properties

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
        if issubclass(AlertRule, dict):
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
        if not isinstance(other, AlertRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
