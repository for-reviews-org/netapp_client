# swagger_client.NodeHealthApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_node_health_get**](NodeHealthApi.md#grid_node_health_get) | **GET** /grid/node-health | Provides health details for the nodes, including alert severities and connection states

# **grid_node_health_get**
> NodeHealthResponse grid_node_health_get()

Provides health details for the nodes, including alert severities and connection states

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
api_instance = swagger_client.NodeHealthApi(swagger_client.ApiClient(configuration))

try:
    # Provides health details for the nodes, including alert severities and connection states
    api_response = api_instance.grid_node_health_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeHealthApi->grid_node_health_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeHealthResponse**](NodeHealthResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

