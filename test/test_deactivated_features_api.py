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
from swagger_client.api.deactivated_features_api import DeactivatedFeaturesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDeactivatedFeaturesApi(unittest.TestCase):
    """DeactivatedFeaturesApi unit test stubs"""

    def setUp(self):
        self.api = DeactivatedFeaturesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_grid_deactivated_features_get(self):
        """Test case for grid_deactivated_features_get

        Retrieves the deactivated features configuration  # noqa: E501
        """
        pass

    def test_grid_deactivated_features_put(self):
        """Test case for grid_deactivated_features_put

        Replaces the deactivated features configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
