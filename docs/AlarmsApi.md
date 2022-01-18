# swagger_client.AlarmsApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_alarms_get**](AlarmsApi.md#grid_alarms_get) | **GET** /grid/alarms | Lists current alarms
[**grid_health_get**](AlarmsApi.md#grid_health_get) | **GET** /grid/health | Gives an indication of the current health of the grid
[**grid_health_topology_get**](AlarmsApi.md#grid_health_topology_get) | **GET** /grid/health/topology | Provides the grid topology and associated health at each level

# **grid_alarms_get**
> ListCurrentAlarmsResponse grid_alarms_get(include_acknowledged=include_acknowledged, limit=limit)

Lists current alarms

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
api_instance = swagger_client.AlarmsApi(swagger_client.ApiClient(configuration))
include_acknowledged = true # bool | if set, acknowledged alarms are also returned (optional)
limit = 25 # int | maximum number of results (optional) (default to 25)

try:
    # Lists current alarms
    api_response = api_instance.grid_alarms_get(include_acknowledged=include_acknowledged, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlarmsApi->grid_alarms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_acknowledged** | **bool**| if set, acknowledged alarms are also returned | [optional] 
 **limit** | **int**| maximum number of results | [optional] [default to 25]

### Return type

[**ListCurrentAlarmsResponse**](ListCurrentAlarmsResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_health_get**
> GridHealthResponse grid_health_get()

Gives an indication of the current health of the grid

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
api_instance = swagger_client.AlarmsApi(swagger_client.ApiClient(configuration))

try:
    # Gives an indication of the current health of the grid
    api_response = api_instance.grid_health_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlarmsApi->grid_health_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GridHealthResponse**](GridHealthResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_health_topology_get**
> GridHealthTopologyResponse grid_health_topology_get(depth=depth)

Provides the grid topology and associated health at each level

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
api_instance = swagger_client.AlarmsApi(swagger_client.ApiClient(configuration))
depth = 'node' # str | topology depth level to provide (optional) (default to node)

try:
    # Provides the grid topology and associated health at each level
    api_response = api_instance.grid_health_topology_get(depth=depth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlarmsApi->grid_health_topology_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **depth** | **str**| topology depth level to provide | [optional] [default to node]

### Return type

[**GridHealthTopologyResponse**](GridHealthTopologyResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

