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
from netapp_client.api.ntp_servers_api import NtpServersApi  # noqa: E501
from netapp_client.rest import ApiException


class TestNtpServersApi(unittest.TestCase):
    """NtpServersApi unit test stubs"""

    def setUp(self):
        self.api = NtpServersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_grid_ntp_servers_get(self):
        """Test case for grid_ntp_servers_get

        Lists configured external NTP servers  # noqa: E501
        """
        pass

    def test_grid_ntp_servers_update_post(self):
        """Test case for grid_ntp_servers_update_post

        Change the external NTP servers used by the grid  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
