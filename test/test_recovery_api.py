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
from netapp_client.api.recovery_api import RecoveryApi  # noqa: E501
from netapp_client.rest import ApiException


class TestRecoveryApi(unittest.TestCase):
    """RecoveryApi unit test stubs"""

    def setUp(self):
        self.api = RecoveryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_grid_recovery_available_nodes_get(self):
        """Test case for grid_recovery_available_nodes_get

        Lists grid nodes not connected to the grid  # noqa: E501
        """
        pass

    def test_grid_recovery_delete(self):
        """Test case for grid_recovery_delete

        Resets the recovery procedure to the not-started state  # noqa: E501
        """
        pass

    def test_grid_recovery_get(self):
        """Test case for grid_recovery_get

        Gets the recovery status  # noqa: E501
        """
        pass

    def test_grid_recovery_post(self):
        """Test case for grid_recovery_post

        Starts the recovery procedure, retrieves configuration file and installs software  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
