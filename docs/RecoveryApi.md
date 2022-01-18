# swagger_client.RecoveryApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_recovery_available_nodes_get**](RecoveryApi.md#grid_recovery_available_nodes_get) | **GET** /grid/recovery/available-nodes | Lists grid nodes not connected to the grid
[**grid_recovery_delete**](RecoveryApi.md#grid_recovery_delete) | **DELETE** /grid/recovery | Resets the recovery procedure to the not-started state
[**grid_recovery_get**](RecoveryApi.md#grid_recovery_get) | **GET** /grid/recovery | Gets the recovery status
[**grid_recovery_post**](RecoveryApi.md#grid_recovery_post) | **POST** /grid/recovery | Starts the recovery procedure, retrieves configuration file and installs software

# **grid_recovery_available_nodes_get**
> AvailableNodesResponse grid_recovery_available_nodes_get()

Lists grid nodes not connected to the grid

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
api_instance = swagger_client.RecoveryApi(swagger_client.ApiClient(configuration))

try:
    # Lists grid nodes not connected to the grid
    api_response = api_instance.grid_recovery_available_nodes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->grid_recovery_available_nodes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AvailableNodesResponse**](AvailableNodesResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_recovery_delete**
> grid_recovery_delete()

Resets the recovery procedure to the not-started state

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
api_instance = swagger_client.RecoveryApi(swagger_client.ApiClient(configuration))

try:
    # Resets the recovery procedure to the not-started state
    api_instance.grid_recovery_delete()
except ApiException as e:
    print("Exception when calling RecoveryApi->grid_recovery_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_recovery_get**
> RecoveryStatusResponse grid_recovery_get()

Gets the recovery status

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
api_instance = swagger_client.RecoveryApi(swagger_client.ApiClient(configuration))

try:
    # Gets the recovery status
    api_response = api_instance.grid_recovery_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->grid_recovery_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RecoveryStatusResponse**](RecoveryStatusResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_recovery_post**
> RecoveryStatusResponse grid_recovery_post(body)

Starts the recovery procedure, retrieves configuration file and installs software

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
api_instance = swagger_client.RecoveryApi(swagger_client.ApiClient(configuration))
body = swagger_client.PostRecoveryRequest() # PostRecoveryRequest | 

try:
    # Starts the recovery procedure, retrieves configuration file and installs software
    api_response = api_instance.grid_recovery_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->grid_recovery_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostRecoveryRequest**](PostRecoveryRequest.md)|  | 

### Return type

[**RecoveryStatusResponse**](RecoveryStatusResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

