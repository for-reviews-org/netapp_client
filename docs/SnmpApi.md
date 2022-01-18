# swagger_client.SnmpApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_snmp_get**](SnmpApi.md#grid_snmp_get) | **GET** /grid/snmp | Gets the SNMP configuration
[**grid_snmp_put**](SnmpApi.md#grid_snmp_put) | **PUT** /grid/snmp | Replaces the SNMP configuration

# **grid_snmp_get**
> SnmpGetPutSnmpResponse grid_snmp_get()

Gets the SNMP configuration

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
api_instance = swagger_client.SnmpApi(swagger_client.ApiClient(configuration))

try:
    # Gets the SNMP configuration
    api_response = api_instance.grid_snmp_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnmpApi->grid_snmp_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SnmpGetPutSnmpResponse**](SnmpGetPutSnmpResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_snmp_put**
> SnmpGetPutSnmpResponse grid_snmp_put(body)

Replaces the SNMP configuration

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
api_instance = swagger_client.SnmpApi(swagger_client.ApiClient(configuration))
body = swagger_client.SnmpConfig() # SnmpConfig | 

try:
    # Replaces the SNMP configuration
    api_response = api_instance.grid_snmp_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnmpApi->grid_snmp_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SnmpConfig**](SnmpConfig.md)|  | 

### Return type

[**SnmpGetPutSnmpResponse**](SnmpGetPutSnmpResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

