# swagger_client.TrafficClassesApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_traffic_classes_get**](TrafficClassesApi.md#grid_traffic_classes_get) | **GET** /grid/traffic-classes | Get all traffic class policy names and IDs, and which bandwidth limits are in use
[**grid_traffic_classes_policies_get**](TrafficClassesApi.md#grid_traffic_classes_policies_get) | **GET** /grid/traffic-classes/policies | Get all traffic class policy names
[**grid_traffic_classes_policies_id_delete**](TrafficClassesApi.md#grid_traffic_classes_policies_id_delete) | **DELETE** /grid/traffic-classes/policies/{id} | Delete a traffic class policy
[**grid_traffic_classes_policies_id_get**](TrafficClassesApi.md#grid_traffic_classes_policies_id_get) | **GET** /grid/traffic-classes/policies/{id} | Get a traffic class policy by ID
[**grid_traffic_classes_policies_id_put**](TrafficClassesApi.md#grid_traffic_classes_policies_id_put) | **PUT** /grid/traffic-classes/policies/{id} | Replace an existing traffic class policy
[**grid_traffic_classes_policies_post**](TrafficClassesApi.md#grid_traffic_classes_policies_post) | **POST** /grid/traffic-classes/policies | Create a new traffic class policy

# **grid_traffic_classes_get**
> TrafficClassesInfoResponse grid_traffic_classes_get()

Get all traffic class policy names and IDs, and which bandwidth limits are in use

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
api_instance = swagger_client.TrafficClassesApi(swagger_client.ApiClient(configuration))

try:
    # Get all traffic class policy names and IDs, and which bandwidth limits are in use
    api_response = api_instance.grid_traffic_classes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficClassesApi->grid_traffic_classes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TrafficClassesInfoResponse**](TrafficClassesInfoResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_traffic_classes_policies_get**
> TrafficClassesPolicyNamesResponse grid_traffic_classes_policies_get()

Get all traffic class policy names

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
api_instance = swagger_client.TrafficClassesApi(swagger_client.ApiClient(configuration))

try:
    # Get all traffic class policy names
    api_response = api_instance.grid_traffic_classes_policies_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficClassesApi->grid_traffic_classes_policies_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TrafficClassesPolicyNamesResponse**](TrafficClassesPolicyNamesResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_traffic_classes_policies_id_delete**
> grid_traffic_classes_policies_id_delete(id)

Delete a traffic class policy

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
api_instance = swagger_client.TrafficClassesApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Policy ID

try:
    # Delete a traffic class policy
    api_instance.grid_traffic_classes_policies_id_delete(id)
except ApiException as e:
    print("Exception when calling TrafficClassesApi->grid_traffic_classes_policies_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Policy ID | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_traffic_classes_policies_id_get**
> TrafficClassesPolicyResponse grid_traffic_classes_policies_id_get(id)

Get a traffic class policy by ID

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
api_instance = swagger_client.TrafficClassesApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Policy ID

try:
    # Get a traffic class policy by ID
    api_response = api_instance.grid_traffic_classes_policies_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficClassesApi->grid_traffic_classes_policies_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Policy ID | 

### Return type

[**TrafficClassesPolicyResponse**](TrafficClassesPolicyResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_traffic_classes_policies_id_put**
> TrafficClassesPolicyResponse grid_traffic_classes_policies_id_put(body, id)

Replace an existing traffic class policy

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
api_instance = swagger_client.TrafficClassesApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrafficClassesPolicy() # TrafficClassesPolicy | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Policy ID

try:
    # Replace an existing traffic class policy
    api_response = api_instance.grid_traffic_classes_policies_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficClassesApi->grid_traffic_classes_policies_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrafficClassesPolicy**](TrafficClassesPolicy.md)|  | 
 **id** | [**str**](.md)| Policy ID | 

### Return type

[**TrafficClassesPolicyResponse**](TrafficClassesPolicyResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_traffic_classes_policies_post**
> TrafficClassesPolicyResponse grid_traffic_classes_policies_post(body)

Create a new traffic class policy

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
api_instance = swagger_client.TrafficClassesApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrafficClassesPolicy() # TrafficClassesPolicy | 

try:
    # Create a new traffic class policy
    api_response = api_instance.grid_traffic_classes_policies_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficClassesApi->grid_traffic_classes_policies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrafficClassesPolicy**](TrafficClassesPolicy.md)|  | 

### Return type

[**TrafficClassesPolicyResponse**](TrafficClassesPolicyResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

