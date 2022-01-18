# swagger_client.EndpointDomainNamesApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_domain_names_get**](EndpointDomainNamesApi.md#grid_domain_names_get) | **GET** /grid/domain-names | Lists endpoint domain names
[**grid_domain_names_put**](EndpointDomainNamesApi.md#grid_domain_names_put) | **PUT** /grid/domain-names | Change the endpoint domain names

# **grid_domain_names_get**
> DomainNamesGetPutResponse grid_domain_names_get()

Lists endpoint domain names

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
api_instance = swagger_client.EndpointDomainNamesApi(swagger_client.ApiClient(configuration))

try:
    # Lists endpoint domain names
    api_response = api_instance.grid_domain_names_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointDomainNamesApi->grid_domain_names_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DomainNamesGetPutResponse**](DomainNamesGetPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_domain_names_put**
> DomainNamesGetPutResponse grid_domain_names_put(body)

Change the endpoint domain names

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
api_instance = swagger_client.EndpointDomainNamesApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] | endpoint domain names

try:
    # Change the endpoint domain names
    api_response = api_instance.grid_domain_names_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointDomainNamesApi->grid_domain_names_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| endpoint domain names | 

### Return type

[**DomainNamesGetPutResponse**](DomainNamesGetPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

