# swagger_client.AlertHistoryApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_alert_history_get**](AlertHistoryApi.md#grid_alert_history_get) | **GET** /grid/alert-history | Lists resolved alerts

# **grid_alert_history_get**
> AlertHistoryListResponse grid_alert_history_get(name=name, time_triggered_earliest=time_triggered_earliest, time_triggered_latest=time_triggered_latest, severity=severity, node=node, inhibited=inhibited)

Lists resolved alerts

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
api_instance = swagger_client.AlertHistoryApi(swagger_client.ApiClient(configuration))
name = ['name_example'] # list[str] | The unique name of one or more alert rules (optional)
time_triggered_earliest = '2013-10-20T19:20:30+01:00' # datetime | The earliest time a resolved alert was triggered (optional)
time_triggered_latest = '2013-10-20T19:20:30+01:00' # datetime | The latest time a resolved alert was triggered (optional)
severity = ['severity_example'] # list[str] | One or more severity levels (optional)
node = ['node_example'] # list[str] | Node name(s) (optional)
inhibited = true # bool | If true, only return resolved alerts that were inhibited (suppressed by another alert) during their entire lifespan. If false, only return resolved alerts that were not inhibited. If omitted, return both inhibited and uninhibited resolved alerts. (optional)

try:
    # Lists resolved alerts
    api_response = api_instance.grid_alert_history_get(name=name, time_triggered_earliest=time_triggered_earliest, time_triggered_latest=time_triggered_latest, severity=severity, node=node, inhibited=inhibited)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertHistoryApi->grid_alert_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**list[str]**](str.md)| The unique name of one or more alert rules | [optional] 
 **time_triggered_earliest** | **datetime**| The earliest time a resolved alert was triggered | [optional] 
 **time_triggered_latest** | **datetime**| The latest time a resolved alert was triggered | [optional] 
 **severity** | [**list[str]**](str.md)| One or more severity levels | [optional] 
 **node** | [**list[str]**](str.md)| Node name(s) | [optional] 
 **inhibited** | **bool**| If true, only return resolved alerts that were inhibited (suppressed by another alert) during their entire lifespan. If false, only return resolved alerts that were not inhibited. If omitted, return both inhibited and uninhibited resolved alerts. | [optional] 

### Return type

[**AlertHistoryListResponse**](AlertHistoryListResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

