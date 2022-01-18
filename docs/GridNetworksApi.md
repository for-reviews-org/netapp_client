# swagger_client.GridNetworksApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_grid_networks_get**](GridNetworksApi.md#grid_grid_networks_get) | **GET** /grid/grid-networks | Lists the current Grid Networks
[**grid_grid_networks_update_post**](GridNetworksApi.md#grid_grid_networks_update_post) | **POST** /grid/grid-networks/update | Change the Grid Network list

# **grid_grid_networks_get**
> GetGridNetworkListResponse grid_grid_networks_get()

Lists the current Grid Networks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.GridNetworksApi(swagger_client.ApiClient(configuration))

try:
    # Lists the current Grid Networks
    api_response = api_instance.grid_grid_networks_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridNetworksApi->grid_grid_networks_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetGridNetworkListResponse**](GetGridNetworkListResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_grid_networks_update_post**
> Response grid_grid_networks_update_post(body)

Change the Grid Network list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.GridNetworksApi(swagger_client.ApiClient(configuration))
body = swagger_client.GridNetworkListUpdateRequest() # GridNetworkListUpdateRequest | 

try:
    # Change the Grid Network list
    api_response = api_instance.grid_grid_networks_update_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridNetworksApi->grid_grid_networks_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GridNetworkListUpdateRequest**](GridNetworkListUpdateRequest.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

