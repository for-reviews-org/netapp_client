# swagger_client.DeactivatedFeaturesApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_deactivated_features_get**](DeactivatedFeaturesApi.md#grid_deactivated_features_get) | **GET** /grid/deactivated-features | Retrieves the deactivated features configuration
[**grid_deactivated_features_put**](DeactivatedFeaturesApi.md#grid_deactivated_features_put) | **PUT** /grid/deactivated-features | Replaces the deactivated features configuration

# **grid_deactivated_features_get**
> DeactivatedFeaturesGetPutResponse grid_deactivated_features_get()

Retrieves the deactivated features configuration

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
api_instance = swagger_client.DeactivatedFeaturesApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the deactivated features configuration
    api_response = api_instance.grid_deactivated_features_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeactivatedFeaturesApi->grid_deactivated_features_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeactivatedFeaturesGetPutResponse**](DeactivatedFeaturesGetPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_deactivated_features_put**
> DeactivatedFeaturesGetPutResponse grid_deactivated_features_put(body)

Replaces the deactivated features configuration

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
api_instance = swagger_client.DeactivatedFeaturesApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeactivatedFeaturesFull() # DeactivatedFeaturesFull | 

try:
    # Replaces the deactivated features configuration
    api_response = api_instance.grid_deactivated_features_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeactivatedFeaturesApi->grid_deactivated_features_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeactivatedFeaturesFull**](DeactivatedFeaturesFull.md)|  | 

### Return type

[**DeactivatedFeaturesGetPutResponse**](DeactivatedFeaturesGetPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

