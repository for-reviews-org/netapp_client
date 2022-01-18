# coding: utf-8

"""
    StorageGRID Management API v3

    REST API for managing StorageGRID deployments. Copyright (c) 2021 NetApp, Inc. All Rights Reserved  # noqa: E501

    OpenAPI spec version: 3.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.identity_source_api import IdentitySourceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestIdentitySourceApi(unittest.TestCase):
    """IdentitySourceApi unit test stubs"""

    def setUp(self):
        self.api = IdentitySourceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_grid_identity_source_get(self):
        """Test case for grid_identity_source_get

        Lists Identity Sources  # noqa: E501
        """
        pass

    def test_grid_identity_source_put(self):
        """Test case for grid_identity_source_put

        Set or update the Identity Source  # noqa: E501
        """
        pass

    def test_grid_identity_source_synchronize_post(self):
        """Test case for grid_identity_source_synchronize_post

        Requests that users and groups from the identity source be synchronized as soon as possible  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()