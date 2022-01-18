# swagger_client.ExpansionNodesApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_expansion_nodes_get**](ExpansionNodesApi.md#grid_expansion_nodes_get) | **GET** /grid/expansion/nodes | Retrieves the list of grid nodes available for expansion
[**grid_expansion_nodes_id_delete**](ExpansionNodesApi.md#grid_expansion_nodes_id_delete) | **DELETE** /grid/expansion/nodes/{id} | Removes a grid node from all procedures; the grid node may be added back in by rebooting it 
[**grid_expansion_nodes_id_get**](ExpansionNodesApi.md#grid_expansion_nodes_id_get) | **GET** /grid/expansion/nodes/{id} | Retrieves a grid node
[**grid_expansion_nodes_id_put**](ExpansionNodesApi.md#grid_expansion_nodes_id_put) | **PUT** /grid/expansion/nodes/{id} | Configures a grid node
[**grid_expansion_nodes_id_reset_post**](ExpansionNodesApi.md#grid_expansion_nodes_id_reset_post) | **POST** /grid/expansion/nodes/{id}/reset | Resets a grid node&#x27;s configuration and returns it back to pending state

# **grid_expansion_nodes_get**
> ListNodesResponse grid_expansion_nodes_get()

Retrieves the list of grid nodes available for expansion

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
api_instance = swagger_client.ExpansionNodesApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the list of grid nodes available for expansion
    api_response = api_instance.grid_expansion_nodes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionNodesApi->grid_expansion_nodes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListNodesResponse**](ListNodesResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_expansion_nodes_id_delete**
> grid_expansion_nodes_id_delete(id)

Removes a grid node from all procedures; the grid node may be added back in by rebooting it 

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
api_instance = swagger_client.ExpansionNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | node ID

try:
    # Removes a grid node from all procedures; the grid node may be added back in by rebooting it 
    api_instance.grid_expansion_nodes_id_delete(id)
except ApiException as e:
    print("Exception when calling ExpansionNodesApi->grid_expansion_nodes_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| node ID | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_expansion_nodes_id_get**
> GetNodeResponse grid_expansion_nodes_id_get(id)

Retrieves a grid node

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
api_instance = swagger_client.ExpansionNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | node ID

try:
    # Retrieves a grid node
    api_response = api_instance.grid_expansion_nodes_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionNodesApi->grid_expansion_nodes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| node ID | 

### Return type

[**GetNodeResponse**](GetNodeResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_expansion_nodes_id_put**
> PutNodeResponse grid_expansion_nodes_id_put(body, id)

Configures a grid node

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
api_instance = swagger_client.ExpansionNodesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Node() # Node | 
id = 'id_example' # str | node ID

try:
    # Configures a grid node
    api_response = api_instance.grid_expansion_nodes_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionNodesApi->grid_expansion_nodes_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Node**](Node.md)|  | 
 **id** | **str**| node ID | 

### Return type

[**PutNodeResponse**](PutNodeResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_expansion_nodes_id_reset_post**
> grid_expansion_nodes_id_reset_post(id, body=body)

Resets a grid node's configuration and returns it back to pending state

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
api_instance = swagger_client.ExpansionNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | node ID
body = 'body_example' # str |  (optional)

try:
    # Resets a grid node's configuration and returns it back to pending state
    api_instance.grid_expansion_nodes_id_reset_post(id, body=body)
except ApiException as e:
    print("Exception when calling ExpansionNodesApi->grid_expansion_nodes_id_reset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| node ID | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

