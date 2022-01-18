# swagger_client.LicenseApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_license_get**](LicenseApi.md#grid_license_get) | **GET** /grid/license | Retrieves the grid license
[**grid_license_update_post**](LicenseApi.md#grid_license_update_post) | **POST** /grid/license/update | Updates the grid license

# **grid_license_get**
> GetLicenseResponse grid_license_get()

Retrieves the grid license

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
api_instance = swagger_client.LicenseApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the grid license
    api_response = api_instance.grid_license_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->grid_license_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetLicenseResponse**](GetLicenseResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_license_update_post**
> grid_license_update_post(body)

Updates the grid license

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
api_instance = swagger_client.LicenseApi(swagger_client.ApiClient(configuration))
body = swagger_client.LicenseUpdateRequest() # LicenseUpdateRequest | 

try:
    # Updates the grid license
    api_instance.grid_license_update_post(body)
except ApiException as e:
    print("Exception when calling LicenseApi->grid_license_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LicenseUpdateRequest**](LicenseUpdateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

