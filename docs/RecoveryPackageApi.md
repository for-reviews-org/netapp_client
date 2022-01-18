# swagger_client.RecoveryPackageApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_recovery_package_post**](RecoveryPackageApi.md#grid_recovery_package_post) | **POST** /grid/recovery-package | Downloads the Recovery Package

# **grid_recovery_package_post**
> str grid_recovery_package_post(body, set_cookie=set_cookie)

Downloads the Recovery Package

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
api_instance = swagger_client.RecoveryPackageApi(swagger_client.ApiClient(configuration))
body = swagger_client.PassphrasePostRequest() # PassphrasePostRequest | 
set_cookie = 56 # int | if present, a cookie named \"recovery-package-download-started-{cookie_value}\" will be sent on success (optional)

try:
    # Downloads the Recovery Package
    api_response = api_instance.grid_recovery_package_post(body, set_cookie=set_cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryPackageApi->grid_recovery_package_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PassphrasePostRequest**](PassphrasePostRequest.md)|  | 
 **set_cookie** | **int**| if present, a cookie named \&quot;recovery-package-download-started-{cookie_value}\&quot; will be sent on success | [optional] 

### Return type

**str**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/zip, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

