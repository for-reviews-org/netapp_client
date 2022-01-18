# swagger_client.RegionsApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_regions_get**](RegionsApi.md#grid_regions_get) | **GET** /grid/regions | Lists configured regions
[**grid_regions_put**](RegionsApi.md#grid_regions_put) | **PUT** /grid/regions | Change the regions used by the grid

# **grid_regions_get**
> RegionsGetResponse grid_regions_get()

Lists configured regions

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
api_instance = swagger_client.RegionsApi(swagger_client.ApiClient(configuration))

try:
    # Lists configured regions
    api_response = api_instance.grid_regions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->grid_regions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RegionsGetResponse**](RegionsGetResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_regions_put**
> RegionsGetResponse grid_regions_put(body)

Change the regions used by the grid

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
api_instance = swagger_client.RegionsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.RegionName()] # list[RegionName] | Region names

try:
    # Change the regions used by the grid
    api_response = api_instance.grid_regions_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->grid_regions_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[RegionName]**](RegionName.md)| Region names | 

### Return type

[**RegionsGetResponse**](RegionsGetResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

