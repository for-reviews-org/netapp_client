# swagger_client.ErasureCodingApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_ec_profiles_get**](ErasureCodingApi.md#grid_ec_profiles_get) | **GET** /grid/ec-profiles | Lists EC profiles
[**grid_schemes_get**](ErasureCodingApi.md#grid_schemes_get) | **GET** /grid/schemes | Lists EC schemes

# **grid_ec_profiles_get**
> EcProfileListResponse grid_ec_profiles_get(show_deactivated=show_deactivated)

Lists EC profiles

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
api_instance = swagger_client.ErasureCodingApi(swagger_client.ApiClient(configuration))
show_deactivated = true # bool | include deactivated profiles (default is to exclude) (optional)

try:
    # Lists EC profiles
    api_response = api_instance.grid_ec_profiles_get(show_deactivated=show_deactivated)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ErasureCodingApi->grid_ec_profiles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_deactivated** | **bool**| include deactivated profiles (default is to exclude) | [optional] 

### Return type

[**EcProfileListResponse**](EcProfileListResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_schemes_get**
> EcSchemesListResponse grid_schemes_get()

Lists EC schemes

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
api_instance = swagger_client.ErasureCodingApi(swagger_client.ApiClient(configuration))

try:
    # Lists EC schemes
    api_response = api_instance.grid_schemes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ErasureCodingApi->grid_schemes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EcSchemesListResponse**](EcSchemesListResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

