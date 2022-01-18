# swagger_client.AuditApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_audit_get**](AuditApi.md#grid_audit_get) | **GET** /grid/audit | Gets the audit configuration
[**grid_audit_put**](AuditApi.md#grid_audit_put) | **PUT** /grid/audit | Replaces the audit configuration

# **grid_audit_get**
> AuditGetPutAuditResponse grid_audit_get()

Gets the audit configuration

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
api_instance = swagger_client.AuditApi(swagger_client.ApiClient(configuration))

try:
    # Gets the audit configuration
    api_response = api_instance.grid_audit_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->grid_audit_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuditGetPutAuditResponse**](AuditGetPutAuditResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_audit_put**
> AuditGetPutAuditResponse grid_audit_put(body)

Replaces the audit configuration

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
api_instance = swagger_client.AuditApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuditConfig() # AuditConfig | 

try:
    # Replaces the audit configuration
    api_response = api_instance.grid_audit_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->grid_audit_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuditConfig**](AuditConfig.md)|  | 

### Return type

[**AuditGetPutAuditResponse**](AuditGetPutAuditResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

