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

class ObjectMetadata(object):
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
        'version_id': 'str',
        'account_id': 'str',
        'name': 'str',
        'container': 'str',
        'object_size_bytes': 'int',
        'disk_size_bytes': 'int',
        'creation_time': 'datetime',
        'modified_time': 'datetime',
        'last_access_time': 'datetime',
        'user_metadata': 'dict(str, list[str])',
        'tags': 'dict(str, str)',
        'locations': 'list[ObjectMetadataLocation]',
        'segmentation': 'ObjectMetadataSegmentation',
        'encrypted': 'bool',
        'raw': 'object'
    }

    attribute_map = {
        'id': 'id',
        'version_id': 'versionId',
        'account_id': 'accountId',
        'name': 'name',
        'container': 'container',
        'object_size_bytes': 'objectSizeBytes',
        'disk_size_bytes': 'diskSizeBytes',
        'creation_time': 'creationTime',
        'modified_time': 'modifiedTime',
        'last_access_time': 'lastAccessTime',
        'user_metadata': 'userMetadata',
        'tags': 'tags',
        'locations': 'locations',
        'segmentation': 'segmentation',
        'encrypted': 'encrypted',
        'raw': 'raw'
    }

    def __init__(self, id=None, version_id=None, account_id=None, name=None, container=None, object_size_bytes=None, disk_size_bytes=None, creation_time=None, modified_time=None, last_access_time=None, user_metadata=None, tags=None, locations=None, segmentation=None, encrypted=False, raw=None):  # noqa: E501
        """ObjectMetadata - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._version_id = None
        self._account_id = None
        self._name = None
        self._container = None
        self._object_size_bytes = None
        self._disk_size_bytes = None
        self._creation_time = None
        self._modified_time = None
        self._last_access_time = None
        self._user_metadata = None
        self._tags = None
        self._locations = None
        self._segmentation = None
        self._encrypted = None
        self._raw = None
        self.discriminator = None
        self.id = id
        if version_id is not None:
            self.version_id = version_id
        if account_id is not None:
            self.account_id = account_id
        self.name = name
        self.container = container
        self.object_size_bytes = object_size_bytes
        if disk_size_bytes is not None:
            self.disk_size_bytes = disk_size_bytes
        self.creation_time = creation_time
        self.modified_time = modified_time
        self.last_access_time = last_access_time
        if user_metadata is not None:
            self.user_metadata = user_metadata
        if tags is not None:
            self.tags = tags
        self.locations = locations
        self.segmentation = segmentation
        self.encrypted = encrypted
        self.raw = raw

    @property
    def id(self):
        """Gets the id of this ObjectMetadata.  # noqa: E501

        a unique identifier for the object  # noqa: E501

        :return: The id of this ObjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ObjectMetadata.

        a unique identifier for the object  # noqa: E501

        :param id: The id of this ObjectMetadata.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def version_id(self):
        """Gets the version_id of this ObjectMetadata.  # noqa: E501

        the object version ID. Objects that are not versioned have a null version ID  # noqa: E501

        :return: The version_id of this ObjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this ObjectMetadata.

        the object version ID. Objects that are not versioned have a null version ID  # noqa: E501

        :param version_id: The version_id of this ObjectMetadata.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def account_id(self):
        """Gets the account_id of this ObjectMetadata.  # noqa: E501

        the ID of the Tenant Account that uploaded the object. Objects uploaded by anonymous users have a null account ID   # noqa: E501

        :return: The account_id of this ObjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ObjectMetadata.

        the ID of the Tenant Account that uploaded the object. Objects uploaded by anonymous users have a null account ID   # noqa: E501

        :param account_id: The account_id of this ObjectMetadata.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this ObjectMetadata.  # noqa: E501

        the name of the object, including any prefixes but excluding the bucket or container name   # noqa: E501

        :return: The name of this ObjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ObjectMetadata.

        the name of the object, including any prefixes but excluding the bucket or container name   # noqa: E501

        :param name: The name of this ObjectMetadata.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def container(self):
        """Gets the container of this ObjectMetadata.  # noqa: E501

        the name of the Swift container or S3 bucket that contains the object  # noqa: E501

        :return: The container of this ObjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this ObjectMetadata.

        the name of the Swift container or S3 bucket that contains the object  # noqa: E501

        :param container: The container of this ObjectMetadata.  # noqa: E501
        :type: str
        """
        if container is None:
            raise ValueError("Invalid value for `container`, must not be `None`")  # noqa: E501

        self._container = container

    @property
    def object_size_bytes(self):
        """Gets the object_size_bytes of this ObjectMetadata.  # noqa: E501

        the original object size in bytes  # noqa: E501

        :return: The object_size_bytes of this ObjectMetadata.  # noqa: E501
        :rtype: int
        """
        return self._object_size_bytes

    @object_size_bytes.setter
    def object_size_bytes(self, object_size_bytes):
        """Sets the object_size_bytes of this ObjectMetadata.

        the original object size in bytes  # noqa: E501

        :param object_size_bytes: The object_size_bytes of this ObjectMetadata.  # noqa: E501
        :type: int
        """
        if object_size_bytes is None:
            raise ValueError("Invalid value for `object_size_bytes`, must not be `None`")  # noqa: E501

        self._object_size_bytes = object_size_bytes

    @property
    def disk_size_bytes(self):
        """Gets the disk_size_bytes of this ObjectMetadata.  # noqa: E501

        the amount of disk space consumed by the object; not available if segmented object  # noqa: E501

        :return: The disk_size_bytes of this ObjectMetadata.  # noqa: E501
        :rtype: int
        """
        return self._disk_size_bytes

    @disk_size_bytes.setter
    def disk_size_bytes(self, disk_size_bytes):
        """Sets the disk_size_bytes of this ObjectMetadata.

        the amount of disk space consumed by the object; not available if segmented object  # noqa: E501

        :param disk_size_bytes: The disk_size_bytes of this ObjectMetadata.  # noqa: E501
        :type: int
        """

        self._disk_size_bytes = disk_size_bytes

    @property
    def creation_time(self):
        """Gets the creation_time of this ObjectMetadata.  # noqa: E501

        date and time when the object was uploaded  # noqa: E501

        :return: The creation_time of this ObjectMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this ObjectMetadata.

        date and time when the object was uploaded  # noqa: E501

        :param creation_time: The creation_time of this ObjectMetadata.  # noqa: E501
        :type: datetime
        """
        if creation_time is None:
            raise ValueError("Invalid value for `creation_time`, must not be `None`")  # noqa: E501

        self._creation_time = creation_time

    @property
    def modified_time(self):
        """Gets the modified_time of this ObjectMetadata.  # noqa: E501

        date and time when the object was last modified  # noqa: E501

        :return: The modified_time of this ObjectMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this ObjectMetadata.

        date and time when the object was last modified  # noqa: E501

        :param modified_time: The modified_time of this ObjectMetadata.  # noqa: E501
        :type: datetime
        """
        if modified_time is None:
            raise ValueError("Invalid value for `modified_time`, must not be `None`")  # noqa: E501

        self._modified_time = modified_time

    @property
    def last_access_time(self):
        """Gets the last_access_time of this ObjectMetadata.  # noqa: E501

        date and time when the object was last accessed. To use this option, updates to Last Access Time must be enabled for the S3 bucket or Swift container   # noqa: E501

        :return: The last_access_time of this ObjectMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._last_access_time

    @last_access_time.setter
    def last_access_time(self, last_access_time):
        """Sets the last_access_time of this ObjectMetadata.

        date and time when the object was last accessed. To use this option, updates to Last Access Time must be enabled for the S3 bucket or Swift container   # noqa: E501

        :param last_access_time: The last_access_time of this ObjectMetadata.  # noqa: E501
        :type: datetime
        """
        if last_access_time is None:
            raise ValueError("Invalid value for `last_access_time`, must not be `None`")  # noqa: E501

        self._last_access_time = last_access_time

    @property
    def user_metadata(self):
        """Gets the user_metadata of this ObjectMetadata.  # noqa: E501

        key-value pairs for any user-defined metadata applied to the object.  # noqa: E501

        :return: The user_metadata of this ObjectMetadata.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._user_metadata

    @user_metadata.setter
    def user_metadata(self, user_metadata):
        """Sets the user_metadata of this ObjectMetadata.

        key-value pairs for any user-defined metadata applied to the object.  # noqa: E501

        :param user_metadata: The user_metadata of this ObjectMetadata.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._user_metadata = user_metadata

    @property
    def tags(self):
        """Gets the tags of this ObjectMetadata.  # noqa: E501

        key-value pairs for any tags applied to the object  # noqa: E501

        :return: The tags of this ObjectMetadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ObjectMetadata.

        key-value pairs for any tags applied to the object  # noqa: E501

        :param tags: The tags of this ObjectMetadata.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def locations(self):
        """Gets the locations of this ObjectMetadata.  # noqa: E501

        how and where the object is stored  # noqa: E501

        :return: The locations of this ObjectMetadata.  # noqa: E501
        :rtype: list[ObjectMetadataLocation]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this ObjectMetadata.

        how and where the object is stored  # noqa: E501

        :param locations: The locations of this ObjectMetadata.  # noqa: E501
        :type: list[ObjectMetadataLocation]
        """
        if locations is None:
            raise ValueError("Invalid value for `locations`, must not be `None`")  # noqa: E501

        self._locations = locations

    @property
    def segmentation(self):
        """Gets the segmentation of this ObjectMetadata.  # noqa: E501


        :return: The segmentation of this ObjectMetadata.  # noqa: E501
        :rtype: ObjectMetadataSegmentation
        """
        return self._segmentation

    @segmentation.setter
    def segmentation(self, segmentation):
        """Sets the segmentation of this ObjectMetadata.


        :param segmentation: The segmentation of this ObjectMetadata.  # noqa: E501
        :type: ObjectMetadataSegmentation
        """
        if segmentation is None:
            raise ValueError("Invalid value for `segmentation`, must not be `None`")  # noqa: E501

        self._segmentation = segmentation

    @property
    def encrypted(self):
        """Gets the encrypted of this ObjectMetadata.  # noqa: E501

        object is encrypted  # noqa: E501

        :return: The encrypted of this ObjectMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this ObjectMetadata.

        object is encrypted  # noqa: E501

        :param encrypted: The encrypted of this ObjectMetadata.  # noqa: E501
        :type: bool
        """
        if encrypted is None:
            raise ValueError("Invalid value for `encrypted`, must not be `None`")  # noqa: E501

        self._encrypted = encrypted

    @property
    def raw(self):
        """Gets the raw of this ObjectMetadata.  # noqa: E501

        all object metadata in the unprocessed internal storage format  # noqa: E501

        :return: The raw of this ObjectMetadata.  # noqa: E501
        :rtype: object
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        """Sets the raw of this ObjectMetadata.

        all object metadata in the unprocessed internal storage format  # noqa: E501

        :param raw: The raw of this ObjectMetadata.  # noqa: E501
        :type: object
        """
        if raw is None:
            raise ValueError("Invalid value for `raw`, must not be `None`")  # noqa: E501

        self._raw = raw

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
        if issubclass(ObjectMetadata, dict):
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
        if not isinstance(other, ObjectMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
