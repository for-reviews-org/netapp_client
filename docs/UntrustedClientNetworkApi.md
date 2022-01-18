# swagger_client.UntrustedClientNetworkApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_untrusted_client_network_get**](UntrustedClientNetworkApi.md#grid_untrusted_client_network_get) | **GET** /grid/untrusted-client-network | Gets the untrusted client network configuration
[**grid_untrusted_client_network_put**](UntrustedClientNetworkApi.md#grid_untrusted_client_network_put) | **PUT** /grid/untrusted-client-network | Replaces the untrusted client network configuration

# **grid_untrusted_client_network_get**
> UntrustedClientNetworkGetPutResponse grid_untrusted_client_network_get()

Gets the untrusted client network configuration

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
api_instance = swagger_client.UntrustedClientNetworkApi(swagger_client.ApiClient(configuration))

try:
    # Gets the untrusted client network configuration
    api_response = api_instance.grid_untrusted_client_network_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UntrustedClientNetworkApi->grid_untrusted_client_network_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UntrustedClientNetworkGetPutResponse**](UntrustedClientNetworkGetPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_untrusted_client_network_put**
> UntrustedClientNetworkGetPutResponse grid_untrusted_client_network_put(body)

Replaces the untrusted client network configuration

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
api_instance = swagger_client.UntrustedClientNetworkApi(swagger_client.ApiClient(configuration))
body = swagger_client.UntrustedClientNetworkConfig() # UntrustedClientNetworkConfig | 

try:
    # Replaces the untrusted client network configuration
    api_response = api_instance.grid_untrusted_client_network_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UntrustedClientNetworkApi->grid_untrusted_client_network_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UntrustedClientNetworkConfig**](UntrustedClientNetworkConfig.md)|  | 

### Return type

[**UntrustedClientNetworkGetPutResponse**](UntrustedClientNetworkGetPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

