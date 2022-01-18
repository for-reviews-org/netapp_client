# swagger_client.ConfigApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_config_get**](ConfigApi.md#grid_config_get) | **GET** /grid/config | Retrieves global configuration and token information
[**grid_config_management_get**](ConfigApi.md#grid_config_management_get) | **GET** /grid/config/management | Retrieves the global management API and UI configuration
[**grid_config_management_put**](ConfigApi.md#grid_config_management_put) | **PUT** /grid/config/management | Changes the global management API and UI configuration
[**grid_config_product_version_get**](ConfigApi.md#grid_config_product_version_get) | **GET** /grid/config/product-version | Retrieves the product release version
[**versions_get**](ConfigApi.md#versions_get) | **GET** /versions | Retrieves the major versions of the management API supported by the product release 

# **grid_config_get**
> ConfigGetResponse grid_config_get()

Retrieves global configuration and token information

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
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves global configuration and token information
    api_response = api_instance.grid_config_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->grid_config_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigGetResponse**](ConfigGetResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_config_management_get**
> ConfigManagementGetPutResponse grid_config_management_get()

Retrieves the global management API and UI configuration

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
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the global management API and UI configuration
    api_response = api_instance.grid_config_management_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->grid_config_management_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigManagementGetPutResponse**](ConfigManagementGetPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_config_management_put**
> ConfigManagementGetPutResponse grid_config_management_put(body)

Changes the global management API and UI configuration

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
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConfigManagement() # ConfigManagement | 

try:
    # Changes the global management API and UI configuration
    api_response = api_instance.grid_config_management_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->grid_config_management_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfigManagement**](ConfigManagement.md)|  | 

### Return type

[**ConfigManagementGetPutResponse**](ConfigManagementGetPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_config_product_version_get**
> ProductVersionGetResponse grid_config_product_version_get()

Retrieves the product release version

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
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the product release version
    api_response = api_instance.grid_config_product_version_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->grid_config_product_version_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProductVersionGetResponse**](ProductVersionGetResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **versions_get**
> ApiVersionsGetResponse versions_get()

Retrieves the major versions of the management API supported by the product release 

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
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the major versions of the management API supported by the product release 
    api_response = api_instance.versions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->versions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiVersionsGetResponse**](ApiVersionsGetResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

