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
from netapp_client.api.metrics_api import MetricsApi  # noqa: E501
from netapp_client.rest import ApiException


class TestMetricsApi(unittest.TestCase):
    """MetricsApi unit test stubs"""

    def setUp(self):
        self.api = MetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_grid_metric_labels_label_values_get(self):
        """Test case for grid_metric_labels_label_values_get

        Lists the values for a metric label  # noqa: E501
        """
        pass

    def test_grid_metric_names_get(self):
        """Test case for grid_metric_names_get

        Lists all available metric names  # noqa: E501
        """
        pass

    def test_grid_metric_query_get(self):
        """Test case for grid_metric_query_get

        Performs an instant metric query at a single point in time  # noqa: E501
        """
        pass

    def test_grid_metric_query_range_get(self):
        """Test case for grid_metric_query_range_get

        Performs a metric query over a range of time  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
