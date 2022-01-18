# coding: utf-8

"""
    StorageGRID Management API v3

    REST API for managing StorageGRID deployments. Copyright (c) 2021 NetApp, Inc. All Rights Reserved  # noqa: E501

    OpenAPI spec version: 3.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import netapp_client
from netapp_client.api.s3_object_lock_api import S3ObjectLockApi  # noqa: E501
from netapp_client.rest import ApiException


class TestS3ObjectLockApi(unittest.TestCase):
    """S3ObjectLockApi unit test stubs"""

    def setUp(self):
        self.api = S3ObjectLockApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_grid_compliance_global_get(self):
        """Test case for grid_compliance_global_get

        Retrieves the global S3 Object Lock settings  # noqa: E501
        """
        pass

    def test_grid_compliance_global_put(self):
        """Test case for grid_compliance_global_put

        Replaces the global S3 Object Lock settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
