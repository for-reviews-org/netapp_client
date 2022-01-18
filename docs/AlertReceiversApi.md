# swagger_client.AlertReceiversApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_alert_receivers_get**](AlertReceiversApi.md#grid_alert_receivers_get) | **GET** /grid/alert-receivers | Lists alert notification receivers
[**grid_alert_receivers_id_delete**](AlertReceiversApi.md#grid_alert_receivers_id_delete) | **DELETE** /grid/alert-receivers/{id} | Deletes a single alert notification receiver
[**grid_alert_receivers_id_get**](AlertReceiversApi.md#grid_alert_receivers_id_get) | **GET** /grid/alert-receivers/{id} | Retrieves an alert notification receiver
[**grid_alert_receivers_id_put**](AlertReceiversApi.md#grid_alert_receivers_id_put) | **PUT** /grid/alert-receivers/{id} | Replaces a single alert notification receiver
[**grid_alert_receivers_post**](AlertReceiversApi.md#grid_alert_receivers_post) | **POST** /grid/alert-receivers | Creates a new alert notification receiver

# **grid_alert_receivers_get**
> ListAlertNotificationReceiversResponse grid_alert_receivers_get()

Lists alert notification receivers

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
api_instance = swagger_client.AlertReceiversApi(swagger_client.ApiClient(configuration))

try:
    # Lists alert notification receivers
    api_response = api_instance.grid_alert_receivers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertReceiversApi->grid_alert_receivers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListAlertNotificationReceiversResponse**](ListAlertNotificationReceiversResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_alert_receivers_id_delete**
> grid_alert_receivers_id_delete(id)

Deletes a single alert notification receiver

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
api_instance = swagger_client.AlertReceiversApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | alert notification receiver ID

try:
    # Deletes a single alert notification receiver
    api_instance.grid_alert_receivers_id_delete(id)
except ApiException as e:
    print("Exception when calling AlertReceiversApi->grid_alert_receivers_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| alert notification receiver ID | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_alert_receivers_id_get**
> GetPostPutAlertNotificationReceiverResponse grid_alert_receivers_id_get(id)

Retrieves an alert notification receiver

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
api_instance = swagger_client.AlertReceiversApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | alert notification receiver ID

try:
    # Retrieves an alert notification receiver
    api_response = api_instance.grid_alert_receivers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertReceiversApi->grid_alert_receivers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| alert notification receiver ID | 

### Return type

[**GetPostPutAlertNotificationReceiverResponse**](GetPostPutAlertNotificationReceiverResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_alert_receivers_id_put**
> GetPostPutAlertNotificationReceiverResponse grid_alert_receivers_id_put(body, id)

Replaces a single alert notification receiver

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
api_instance = swagger_client.AlertReceiversApi(swagger_client.ApiClient(configuration))
body = swagger_client.AlertNotificationReceiver() # AlertNotificationReceiver | 
id = 'id_example' # str | alert notification receiver ID

try:
    # Replaces a single alert notification receiver
    api_response = api_instance.grid_alert_receivers_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertReceiversApi->grid_alert_receivers_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertNotificationReceiver**](AlertNotificationReceiver.md)|  | 
 **id** | **str**| alert notification receiver ID | 

### Return type

[**GetPostPutAlertNotificationReceiverResponse**](GetPostPutAlertNotificationReceiverResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_alert_receivers_post**
> GetPostPutAlertNotificationReceiverResponse grid_alert_receivers_post(body, test=test, use_secrets_from=use_secrets_from)

Creates a new alert notification receiver

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
api_instance = swagger_client.AlertReceiversApi(swagger_client.ApiClient(configuration))
body = swagger_client.AlertNotificationReceiverPostRequest() # AlertNotificationReceiverPostRequest | 
test = true # bool | If specified, tests the validity of the notification receiver and requests sending a test email. Does not save the receiver. (optional)
use_secrets_from = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | If specified, uses the password and client key (if set) from the saved receiver matching this UUID. Applicable only when \"test\" is also specified. (optional)

try:
    # Creates a new alert notification receiver
    api_response = api_instance.grid_alert_receivers_post(body, test=test, use_secrets_from=use_secrets_from)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertReceiversApi->grid_alert_receivers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertNotificationReceiverPostRequest**](AlertNotificationReceiverPostRequest.md)|  | 
 **test** | **bool**| If specified, tests the validity of the notification receiver and requests sending a test email. Does not save the receiver. | [optional] 
 **use_secrets_from** | [**str**](.md)| If specified, uses the password and client key (if set) from the saved receiver matching this UUID. Applicable only when \&quot;test\&quot; is also specified. | [optional] 

### Return type

[**GetPostPutAlertNotificationReceiverResponse**](GetPostPutAlertNotificationReceiverResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

