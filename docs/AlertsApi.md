# swagger_client.AlertsApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_alerts_get**](AlertsApi.md#grid_alerts_get) | **GET** /grid/alerts | Lists active alerts

# **grid_alerts_get**
> AlertsListResponse grid_alerts_get(include=include)

Lists active alerts

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
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
include = ['include_example'] # list[str] | types of alerts to include (default: active) (optional)

try:
    # Lists active alerts
    api_response = api_instance.grid_alerts_get(include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->grid_alerts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**list[str]**](str.md)| types of alerts to include (default: active) | [optional] 

### Return type

[**AlertsListResponse**](AlertsListResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

