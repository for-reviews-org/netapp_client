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

class Replicated(object):
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
        'pool_id': 'str',
        'temporary_pool_id': 'str',
        'cloud_storage_pool_id': 'str',
        'copies': 'int'
    }

    attribute_map = {
        'pool_id': 'poolId',
        'temporary_pool_id': 'temporaryPoolId',
        'cloud_storage_pool_id': 'cloudStoragePoolId',
        'copies': 'copies'
    }

    def __init__(self, pool_id=None, temporary_pool_id=None, cloud_storage_pool_id=None, copies=None):  # noqa: E501
        """Replicated - a model defined in Swagger"""  # noqa: E501
        self._pool_id = None
        self._temporary_pool_id = None
        self._cloud_storage_pool_id = None
        self._copies = None
        self.discriminator = None
        if pool_id is not None:
            self.pool_id = pool_id
        if temporary_pool_id is not None:
            self.temporary_pool_id = temporary_pool_id
        if cloud_storage_pool_id is not None:
            self.cloud_storage_pool_id = cloud_storage_pool_id
        self.copies = copies

    @property
    def pool_id(self):
        """Gets the pool_id of this Replicated.  # noqa: E501

        One or more storage pools where object data is saved, specified as comma-separated values. Either poolId or cloudStoragePoolId is required.  # noqa: E501

        :return: The pool_id of this Replicated.  # noqa: E501
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this Replicated.

        One or more storage pools where object data is saved, specified as comma-separated values. Either poolId or cloudStoragePoolId is required.  # noqa: E501

        :param pool_id: The pool_id of this Replicated.  # noqa: E501
        :type: str
        """

        self._pool_id = pool_id

    @property
    def temporary_pool_id(self):
        """Gets the temporary_pool_id of this Replicated.  # noqa: E501

        Temporary locations are deprecated and should not be used for new ILM rules. If you select the Strict ingest behavior, the temporary location is ignored.  # noqa: E501

        :return: The temporary_pool_id of this Replicated.  # noqa: E501
        :rtype: str
        """
        return self._temporary_pool_id

    @temporary_pool_id.setter
    def temporary_pool_id(self, temporary_pool_id):
        """Sets the temporary_pool_id of this Replicated.

        Temporary locations are deprecated and should not be used for new ILM rules. If you select the Strict ingest behavior, the temporary location is ignored.  # noqa: E501

        :param temporary_pool_id: The temporary_pool_id of this Replicated.  # noqa: E501
        :type: str
        """

        self._temporary_pool_id = temporary_pool_id

    @property
    def cloud_storage_pool_id(self):
        """Gets the cloud_storage_pool_id of this Replicated.  # noqa: E501

        Cloud Storage Pool where object data is saved. Cloud Storage Pools cannot be used in the same placement as a storage pool. Either poolId or cloudStoragePoolId is required.  # noqa: E501

        :return: The cloud_storage_pool_id of this Replicated.  # noqa: E501
        :rtype: str
        """
        return self._cloud_storage_pool_id

    @cloud_storage_pool_id.setter
    def cloud_storage_pool_id(self, cloud_storage_pool_id):
        """Sets the cloud_storage_pool_id of this Replicated.

        Cloud Storage Pool where object data is saved. Cloud Storage Pools cannot be used in the same placement as a storage pool. Either poolId or cloudStoragePoolId is required.  # noqa: E501

        :param cloud_storage_pool_id: The cloud_storage_pool_id of this Replicated.  # noqa: E501
        :type: str
        """

        self._cloud_storage_pool_id = cloud_storage_pool_id

    @property
    def copies(self):
        """Gets the copies of this Replicated.  # noqa: E501

        number of replicated copies  # noqa: E501

        :return: The copies of this Replicated.  # noqa: E501
        :rtype: int
        """
        return self._copies

    @copies.setter
    def copies(self, copies):
        """Sets the copies of this Replicated.

        number of replicated copies  # noqa: E501

        :param copies: The copies of this Replicated.  # noqa: E501
        :type: int
        """
        if copies is None:
            raise ValueError("Invalid value for `copies`, must not be `None`")  # noqa: E501

        self._copies = copies

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
        if issubclass(Replicated, dict):
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
        if not isinstance(other, Replicated):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
