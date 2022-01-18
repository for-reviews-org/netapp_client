# coding: utf-8

"""
    StorageGRID Management API v3

    REST API for managing StorageGRID deployments. Copyright (c) 2021 NetApp, Inc. All Rights Reserved  # noqa: E501

    OpenAPI spec version: 3.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AccountsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def grid_accounts_cache_get(self, **kwargs):  # noqa: E501
        """Lists cached Storage Tenant Accounts  # noqa: E501

        Lists the tenant accounts in the cache and includes additional information, such as objectCount and dataBytes. Updates to tenants might take 15 minutes to appear in cached data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_cache_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: maximum number of results
        :return: ListAccountsCacheResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.grid_accounts_cache_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.grid_accounts_cache_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def grid_accounts_cache_get_with_http_info(self, **kwargs):  # noqa: E501
        """Lists cached Storage Tenant Accounts  # noqa: E501

        Lists the tenant accounts in the cache and includes additional information, such as objectCount and dataBytes. Updates to tenants might take 15 minutes to appear in cached data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_cache_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: maximum number of results
        :return: ListAccountsCacheResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method grid_accounts_cache_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/grid/accounts-cache', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListAccountsCacheResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def grid_accounts_get(self, **kwargs):  # noqa: E501
        """Lists Storage Tenant Accounts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: maximum number of results
        :param str marker: marker-style pagination offset (value is Account's id)
        :param bool include_marker: if set, the marker element is also returned
        :param str order: pagination order (desc requires marker)
        :return: ListAccountsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.grid_accounts_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.grid_accounts_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def grid_accounts_get_with_http_info(self, **kwargs):  # noqa: E501
        """Lists Storage Tenant Accounts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: maximum number of results
        :param str marker: marker-style pagination offset (value is Account's id)
        :param bool include_marker: if set, the marker element is also returned
        :param str order: pagination order (desc requires marker)
        :return: ListAccountsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'marker', 'include_marker', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method grid_accounts_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'marker' in params:
            query_params.append(('marker', params['marker']))  # noqa: E501
        if 'include_marker' in params:
            query_params.append(('includeMarker', params['include_marker']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/grid/accounts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListAccountsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def grid_accounts_id_change_password_post(self, body, id, **kwargs):  # noqa: E501
        """Changes the root user password for the Storage Tenant Account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_id_change_password_post(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChangePassword body: (required)
        :param str id: ID of Storage Tenant Account (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.grid_accounts_id_change_password_post_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.grid_accounts_id_change_password_post_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def grid_accounts_id_change_password_post_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Changes the root user password for the Storage Tenant Account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_id_change_password_post_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChangePassword body: (required)
        :param str id: ID of Storage Tenant Account (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method grid_accounts_id_change_password_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `grid_accounts_id_change_password_post`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `grid_accounts_id_change_password_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/grid/accounts/{id}/change-password', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def grid_accounts_id_delete(self, id, **kwargs):  # noqa: E501
        """Deletes a single Storage Tenant Account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_id_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of Storage Tenant Account (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.grid_accounts_id_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.grid_accounts_id_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def grid_accounts_id_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Deletes a single Storage Tenant Account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_id_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of Storage Tenant Account (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method grid_accounts_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `grid_accounts_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/grid/accounts/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def grid_accounts_id_get(self, id, **kwargs):  # noqa: E501
        """Retrieves a single Storage Tenant Account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of Storage Tenant Account (required)
        :return: GetPatchPutAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.grid_accounts_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.grid_accounts_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def grid_accounts_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves a single Storage Tenant Account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of Storage Tenant Account (required)
        :return: GetPatchPutAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method grid_accounts_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `grid_accounts_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/grid/accounts/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetPatchPutAccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def grid_accounts_id_patch(self, body, id, **kwargs):  # noqa: E501
        """Updates a single Storage Tenant Account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_id_patch(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountNoId body: (required)
        :param str id: ID of Storage Tenant Account (required)
        :return: GetPatchPutAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.grid_accounts_id_patch_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.grid_accounts_id_patch_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def grid_accounts_id_patch_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Updates a single Storage Tenant Account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_id_patch_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountNoId body: (required)
        :param str id: ID of Storage Tenant Account (required)
        :return: GetPatchPutAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method grid_accounts_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `grid_accounts_id_patch`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `grid_accounts_id_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/grid/accounts/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetPatchPutAccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def grid_accounts_id_put(self, body, id, **kwargs):  # noqa: E501
        """Replaces a single Storage Tenant Account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_id_put(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Account body: (required)
        :param str id: ID of Storage Tenant Account (required)
        :return: GetPatchPutAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.grid_accounts_id_put_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.grid_accounts_id_put_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def grid_accounts_id_put_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Replaces a single Storage Tenant Account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_id_put_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Account body: (required)
        :param str id: ID of Storage Tenant Account (required)
        :return: GetPatchPutAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method grid_accounts_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `grid_accounts_id_put`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `grid_accounts_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/grid/accounts/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetPatchPutAccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def grid_accounts_id_usage_get(self, id, **kwargs):  # noqa: E501
        """Gets the storage usage information for the Storage Tenant Account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_id_usage_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of Storage Tenant Account (required)
        :param bool strict_consistency: If true, the request fails if the results cannot be retrieved at a strong-global consistency. If false (default), attempts to retrieve usage information use strong-global consistency initially but fall back to a strong-site consistency.
        :return: AccountUsageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.grid_accounts_id_usage_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.grid_accounts_id_usage_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def grid_accounts_id_usage_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Gets the storage usage information for the Storage Tenant Account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_id_usage_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of Storage Tenant Account (required)
        :param bool strict_consistency: If true, the request fails if the results cannot be retrieved at a strong-global consistency. If false (default), attempts to retrieve usage information use strong-global consistency initially but fall back to a strong-site consistency.
        :return: AccountUsageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'strict_consistency']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method grid_accounts_id_usage_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `grid_accounts_id_usage_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'strict_consistency' in params:
            query_params.append(('strictConsistency', params['strict_consistency']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/grid/accounts/{id}/usage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountUsageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def grid_accounts_post(self, body, **kwargs):  # noqa: E501
        """Creates a new Storage Tenant Account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostAccountRequest body: (required)
        :return: CreateAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.grid_accounts_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.grid_accounts_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def grid_accounts_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates a new Storage Tenant Account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.grid_accounts_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostAccountRequest body: (required)
        :return: CreateAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method grid_accounts_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `grid_accounts_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/grid/accounts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateAccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
