# swagger_client.S3ObjectLockApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_compliance_global_get**](S3ObjectLockApi.md#grid_compliance_global_get) | **GET** /grid/compliance-global | Retrieves the global S3 Object Lock settings
[**grid_compliance_global_put**](S3ObjectLockApi.md#grid_compliance_global_put) | **PUT** /grid/compliance-global | Replaces the global S3 Object Lock settings

# **grid_compliance_global_get**
> ComplianceGlobalGetPutResponse grid_compliance_global_get()

Retrieves the global S3 Object Lock settings

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
api_instance = swagger_client.S3ObjectLockApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the global S3 Object Lock settings
    api_response = api_instance.grid_compliance_global_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3ObjectLockApi->grid_compliance_global_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ComplianceGlobalGetPutResponse**](ComplianceGlobalGetPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_compliance_global_put**
> ComplianceGlobalGetPutResponse grid_compliance_global_put(body)

Replaces the global S3 Object Lock settings

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
api_instance = swagger_client.S3ObjectLockApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComplianceGlobalPutRequest() # ComplianceGlobalPutRequest | 

try:
    # Replaces the global S3 Object Lock settings
    api_response = api_instance.grid_compliance_global_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3ObjectLockApi->grid_compliance_global_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComplianceGlobalPutRequest**](ComplianceGlobalPutRequest.md)|  | 

### Return type

[**ComplianceGlobalGetPutResponse**](ComplianceGlobalGetPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

