# swagger_client.AlertSilencesApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_alert_silences_get**](AlertSilencesApi.md#grid_alert_silences_get) | **GET** /grid/alert-silences | Lists alert silences
[**grid_alert_silences_id_delete**](AlertSilencesApi.md#grid_alert_silences_id_delete) | **DELETE** /grid/alert-silences/{id} | Deletes a single alert silence
[**grid_alert_silences_id_get**](AlertSilencesApi.md#grid_alert_silences_id_get) | **GET** /grid/alert-silences/{id} | Retrieves an alert silence
[**grid_alert_silences_id_put**](AlertSilencesApi.md#grid_alert_silences_id_put) | **PUT** /grid/alert-silences/{id} | Replaces a single alert silence
[**grid_alert_silences_post**](AlertSilencesApi.md#grid_alert_silences_post) | **POST** /grid/alert-silences | Creates a new alert silence

# **grid_alert_silences_get**
> AlertSilenceListResponse grid_alert_silences_get()

Lists alert silences

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
api_instance = swagger_client.AlertSilencesApi(swagger_client.ApiClient(configuration))

try:
    # Lists alert silences
    api_response = api_instance.grid_alert_silences_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertSilencesApi->grid_alert_silences_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertSilenceListResponse**](AlertSilenceListResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_alert_silences_id_delete**
> grid_alert_silences_id_delete(id)

Deletes a single alert silence

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
api_instance = swagger_client.AlertSilencesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | alert silence ID

try:
    # Deletes a single alert silence
    api_instance.grid_alert_silences_id_delete(id)
except ApiException as e:
    print("Exception when calling AlertSilencesApi->grid_alert_silences_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| alert silence ID | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_alert_silences_id_get**
> AlertSilenceGetPostPutResponse grid_alert_silences_id_get(id)

Retrieves an alert silence

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
api_instance = swagger_client.AlertSilencesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | alert silence ID

try:
    # Retrieves an alert silence
    api_response = api_instance.grid_alert_silences_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertSilencesApi->grid_alert_silences_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| alert silence ID | 

### Return type

[**AlertSilenceGetPostPutResponse**](AlertSilenceGetPostPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_alert_silences_id_put**
> AlertSilenceGetPostPutResponse grid_alert_silences_id_put(body, id)

Replaces a single alert silence

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
api_instance = swagger_client.AlertSilencesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AlertSilence() # AlertSilence | 
id = 'id_example' # str | alert silence ID

try:
    # Replaces a single alert silence
    api_response = api_instance.grid_alert_silences_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertSilencesApi->grid_alert_silences_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertSilence**](AlertSilence.md)|  | 
 **id** | **str**| alert silence ID | 

### Return type

[**AlertSilenceGetPostPutResponse**](AlertSilenceGetPostPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_alert_silences_post**
> AlertSilenceGetPostPutResponse grid_alert_silences_post(body)

Creates a new alert silence

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
api_instance = swagger_client.AlertSilencesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AlertSilencePostRequest() # AlertSilencePostRequest | 

try:
    # Creates a new alert silence
    api_response = api_instance.grid_alert_silences_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertSilencesApi->grid_alert_silences_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertSilencePostRequest**](AlertSilencePostRequest.md)|  | 

### Return type

[**AlertSilenceGetPostPutResponse**](AlertSilenceGetPostPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

