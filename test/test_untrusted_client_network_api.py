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
from netapp_client.api.untrusted_client_network_api import UntrustedClientNetworkApi  # noqa: E501
from netapp_client.rest import ApiException


class TestUntrustedClientNetworkApi(unittest.TestCase):
    """UntrustedClientNetworkApi unit test stubs"""

    def setUp(self):
        self.api = UntrustedClientNetworkApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_grid_untrusted_client_network_get(self):
        """Test case for grid_untrusted_client_network_get

        Gets the untrusted client network configuration  # noqa: E501
        """
        pass

    def test_grid_untrusted_client_network_put(self):
        """Test case for grid_untrusted_client_network_put

        Replaces the untrusted client network configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
