# swagger_client.AlertRulesApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_alert_rules_get**](AlertRulesApi.md#grid_alert_rules_get) | **GET** /grid/alert-rules | Lists alert rules
[**grid_alert_rules_id_delete**](AlertRulesApi.md#grid_alert_rules_id_delete) | **DELETE** /grid/alert-rules/{id} | Deletes a single custom alert rule
[**grid_alert_rules_id_get**](AlertRulesApi.md#grid_alert_rules_id_get) | **GET** /grid/alert-rules/{id} | Retrieves a single alert rule
[**grid_alert_rules_id_put**](AlertRulesApi.md#grid_alert_rules_id_put) | **PUT** /grid/alert-rules/{id} | Replaces a single alert rule
[**grid_alert_rules_post**](AlertRulesApi.md#grid_alert_rules_post) | **POST** /grid/alert-rules | Creates a custom alert rule

# **grid_alert_rules_get**
> AlertRulesListResponse grid_alert_rules_get()

Lists alert rules

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
api_instance = swagger_client.AlertRulesApi(swagger_client.ApiClient(configuration))

try:
    # Lists alert rules
    api_response = api_instance.grid_alert_rules_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertRulesApi->grid_alert_rules_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertRulesListResponse**](AlertRulesListResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_alert_rules_id_delete**
> grid_alert_rules_id_delete(id)

Deletes a single custom alert rule

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
api_instance = swagger_client.AlertRulesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Rule ID

try:
    # Deletes a single custom alert rule
    api_instance.grid_alert_rules_id_delete(id)
except ApiException as e:
    print("Exception when calling AlertRulesApi->grid_alert_rules_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Rule ID | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_alert_rules_id_get**
> AlertRuleGetPostPutResponse grid_alert_rules_id_get(id)

Retrieves a single alert rule

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
api_instance = swagger_client.AlertRulesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Rule ID

try:
    # Retrieves a single alert rule
    api_response = api_instance.grid_alert_rules_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertRulesApi->grid_alert_rules_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Rule ID | 

### Return type

[**AlertRuleGetPostPutResponse**](AlertRuleGetPostPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_alert_rules_id_put**
> AlertRuleGetPostPutResponse grid_alert_rules_id_put(body, id)

Replaces a single alert rule

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
api_instance = swagger_client.AlertRulesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AlertRule() # AlertRule | The new state of the rule. For default (non-custom) rules, you can only update the "enable", "expressions", and "for" properties.
id = 'id_example' # str | Rule ID

try:
    # Replaces a single alert rule
    api_response = api_instance.grid_alert_rules_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertRulesApi->grid_alert_rules_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertRule**](AlertRule.md)| The new state of the rule. For default (non-custom) rules, you can only update the &quot;enable&quot;, &quot;expressions&quot;, and &quot;for&quot; properties. | 
 **id** | **str**| Rule ID | 

### Return type

[**AlertRuleGetPostPutResponse**](AlertRuleGetPostPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_alert_rules_post**
> AlertRuleGetPostPutResponse grid_alert_rules_post(body)

Creates a custom alert rule

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
api_instance = swagger_client.AlertRulesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AlertRulePostBody() # AlertRulePostBody | 

try:
    # Creates a custom alert rule
    api_response = api_instance.grid_alert_rules_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertRulesApi->grid_alert_rules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertRulePostBody**](AlertRulePostBody.md)|  | 

### Return type

[**AlertRuleGetPostPutResponse**](AlertRuleGetPostPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

