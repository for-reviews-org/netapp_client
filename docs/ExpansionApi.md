# swagger_client.ExpansionApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_expansion_delete**](ExpansionApi.md#grid_expansion_delete) | **DELETE** /grid/expansion | Cancels the expansion procedure and resets all user configuration of expansion grid nodes 
[**grid_expansion_expand_post**](ExpansionApi.md#grid_expansion_expand_post) | **POST** /grid/expansion/expand | Executes the expansion procedure, adding configured grid nodes to the grid
[**grid_expansion_get**](ExpansionApi.md#grid_expansion_get) | **GET** /grid/expansion | Retrieves the status of the current expansion procedure
[**grid_expansion_start_post**](ExpansionApi.md#grid_expansion_start_post) | **POST** /grid/expansion/start | Initiates the expansion procedure, allowing configuration of the expansion grid nodes 

# **grid_expansion_delete**
> grid_expansion_delete()

Cancels the expansion procedure and resets all user configuration of expansion grid nodes 

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
api_instance = swagger_client.ExpansionApi(swagger_client.ApiClient(configuration))

try:
    # Cancels the expansion procedure and resets all user configuration of expansion grid nodes 
    api_instance.grid_expansion_delete()
except ApiException as e:
    print("Exception when calling ExpansionApi->grid_expansion_delete: %s\n" % e)
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

# **grid_expansion_expand_post**
> grid_expansion_expand_post(body)

Executes the expansion procedure, adding configured grid nodes to the grid

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
api_instance = swagger_client.ExpansionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProvisioningPassphrase() # ProvisioningPassphrase | 

try:
    # Executes the expansion procedure, adding configured grid nodes to the grid
    api_instance.grid_expansion_expand_post(body)
except ApiException as e:
    print("Exception when calling ExpansionApi->grid_expansion_expand_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProvisioningPassphrase**](ProvisioningPassphrase.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_expansion_get**
> GetExpansionStatusResponse grid_expansion_get()

Retrieves the status of the current expansion procedure

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
api_instance = swagger_client.ExpansionApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the status of the current expansion procedure
    api_response = api_instance.grid_expansion_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionApi->grid_expansion_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetExpansionStatusResponse**](GetExpansionStatusResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_expansion_start_post**
> GetExpansionStatusResponse grid_expansion_start_post(body=body)

Initiates the expansion procedure, allowing configuration of the expansion grid nodes 

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
api_instance = swagger_client.ExpansionApi(swagger_client.ApiClient(configuration))
body = 'body_example' # str |  (optional)

try:
    # Initiates the expansion procedure, allowing configuration of the expansion grid nodes 
    api_response = api_instance.grid_expansion_start_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionApi->grid_expansion_start_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | [optional] 

### Return type

[**GetExpansionStatusResponse**](GetExpansionStatusResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

