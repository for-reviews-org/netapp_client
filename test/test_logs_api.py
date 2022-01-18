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
from netapp_client.api.logs_api import LogsApi  # noqa: E501
from netapp_client.rest import ApiException


class TestLogsApi(unittest.TestCase):
    """LogsApi unit test stubs"""

    def setUp(self):
        self.api = LogsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_grid_logs_collect_post(self):
        """Test case for grid_logs_collect_post

        Start a new log collection procedure  # noqa: E501
        """
        pass

    def test_grid_logs_collection_delete(self):
        """Test case for grid_logs_collection_delete

        Deletes the previous log collection archive  # noqa: E501
        """
        pass

    def test_grid_logs_collection_get(self):
        """Test case for grid_logs_collection_get

        Download log collection archive after procedure completes  # noqa: E501
        """
        pass

    def test_grid_logs_get(self):
        """Test case for grid_logs_get

        Log collection procedure status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
