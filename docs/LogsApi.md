# swagger_client.LogsApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_logs_collect_post**](LogsApi.md#grid_logs_collect_post) | **POST** /grid/logs/collect | Start a new log collection procedure
[**grid_logs_collection_delete**](LogsApi.md#grid_logs_collection_delete) | **DELETE** /grid/logs/collection | Deletes the previous log collection archive
[**grid_logs_collection_get**](LogsApi.md#grid_logs_collection_get) | **GET** /grid/logs/collection | Download log collection archive after procedure completes
[**grid_logs_get**](LogsApi.md#grid_logs_get) | **GET** /grid/logs | Log collection procedure status

# **grid_logs_collect_post**
> Response grid_logs_collect_post(body)

Start a new log collection procedure

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
api_instance = swagger_client.LogsApi(swagger_client.ApiClient(configuration))
body = swagger_client.LogCollectionRequest() # LogCollectionRequest | 

try:
    # Start a new log collection procedure
    api_response = api_instance.grid_logs_collect_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->grid_logs_collect_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogCollectionRequest**](LogCollectionRequest.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_logs_collection_delete**
> grid_logs_collection_delete()

Deletes the previous log collection archive

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
api_instance = swagger_client.LogsApi(swagger_client.ApiClient(configuration))

try:
    # Deletes the previous log collection archive
    api_instance.grid_logs_collection_delete()
except ApiException as e:
    print("Exception when calling LogsApi->grid_logs_collection_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_logs_collection_get**
> str grid_logs_collection_get(set_cookie=set_cookie)

Download log collection archive after procedure completes

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
api_instance = swagger_client.LogsApi(swagger_client.ApiClient(configuration))
set_cookie = 56 # int | if present, a cookie named \"logs-package-download-started-{cookie_value}\" will be sent on success (optional)

try:
    # Download log collection archive after procedure completes
    api_response = api_instance.grid_logs_collection_get(set_cookie=set_cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->grid_logs_collection_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_cookie** | **int**| if present, a cookie named \&quot;logs-package-download-started-{cookie_value}\&quot; will be sent on success | [optional] 

### Return type

**str**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_logs_get**
> LogsGetResponse grid_logs_get()

Log collection procedure status

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
api_instance = swagger_client.LogsApi(swagger_client.ApiClient(configuration))

try:
    # Log collection procedure status
    api_response = api_instance.grid_logs_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->grid_logs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LogsGetResponse**](LogsGetResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

