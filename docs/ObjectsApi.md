# swagger_client.ObjectsApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_object_metadata_post**](ObjectsApi.md#grid_object_metadata_post) | **POST** /grid/object-metadata | Retrieves metadata for an object

# **grid_object_metadata_post**
> ObjectMetadataGetResponse grid_object_metadata_post(body)

Retrieves metadata for an object

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
api_instance = swagger_client.ObjectsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ObjectMetadataRequest() # ObjectMetadataRequest | 

try:
    # Retrieves metadata for an object
    api_response = api_instance.grid_object_metadata_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->grid_object_metadata_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectMetadataRequest**](ObjectMetadataRequest.md)|  | 

### Return type

[**ObjectMetadataGetResponse**](ObjectMetadataGetResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

