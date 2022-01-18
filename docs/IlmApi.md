# swagger_client.IlmApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_ilm_criteria_get**](IlmApi.md#grid_ilm_criteria_get) | **GET** /grid/ilm-criteria | Lists criteria available for creating an ILM rule
[**grid_ilm_evaluate_post**](IlmApi.md#grid_ilm_evaluate_post) | **POST** /grid/ilm-evaluate | Evaluates proposed ILM policy
[**grid_ilm_policies_get**](IlmApi.md#grid_ilm_policies_get) | **GET** /grid/ilm-policies | Lists ILM policies
[**grid_ilm_policies_id_delete**](IlmApi.md#grid_ilm_policies_id_delete) | **DELETE** /grid/ilm-policies/{id} | Deletes a (proposed) ILM policy
[**grid_ilm_policies_id_get**](IlmApi.md#grid_ilm_policies_id_get) | **GET** /grid/ilm-policies/{id} | Retrieves a single ILM policy
[**grid_ilm_policies_id_put**](IlmApi.md#grid_ilm_policies_id_put) | **PUT** /grid/ilm-policies/{id} | Replaces a proposed ILM policy and optionally activates it
[**grid_ilm_policies_post**](IlmApi.md#grid_ilm_policies_post) | **POST** /grid/ilm-policies | Creates a proposed or active policy
[**grid_ilm_rules_get**](IlmApi.md#grid_ilm_rules_get) | **GET** /grid/ilm-rules | Lists ILM rules
[**grid_ilm_rules_id_delete**](IlmApi.md#grid_ilm_rules_id_delete) | **DELETE** /grid/ilm-rules/{id} | Deletes an ILM rule
[**grid_ilm_rules_id_get**](IlmApi.md#grid_ilm_rules_id_get) | **GET** /grid/ilm-rules/{id} | Retrieves a single ILM rule
[**grid_ilm_rules_id_put**](IlmApi.md#grid_ilm_rules_id_put) | **PUT** /grid/ilm-rules/{id} | Replaces a single ILM rule
[**grid_ilm_rules_post**](IlmApi.md#grid_ilm_rules_post) | **POST** /grid/ilm-rules | Creates a new ILM rule

# **grid_ilm_criteria_get**
> IlmCriteriaListResponse grid_ilm_criteria_get()

Lists criteria available for creating an ILM rule

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
api_instance = swagger_client.IlmApi(swagger_client.ApiClient(configuration))

try:
    # Lists criteria available for creating an ILM rule
    api_response = api_instance.grid_ilm_criteria_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IlmApi->grid_ilm_criteria_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IlmCriteriaListResponse**](IlmCriteriaListResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_ilm_evaluate_post**
> IlmEvaluateResponse grid_ilm_evaluate_post(body)

Evaluates proposed ILM policy

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
api_instance = swagger_client.IlmApi(swagger_client.ApiClient(configuration))
body = swagger_client.IlmEvaluateRequest() # IlmEvaluateRequest | 

try:
    # Evaluates proposed ILM policy
    api_response = api_instance.grid_ilm_evaluate_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IlmApi->grid_ilm_evaluate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IlmEvaluateRequest**](IlmEvaluateRequest.md)|  | 

### Return type

[**IlmEvaluateResponse**](IlmEvaluateResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_ilm_policies_get**
> IlmPoliciesListResponse grid_ilm_policies_get(type=type)

Lists ILM policies

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
api_instance = swagger_client.IlmApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | filter by policy type (optional)

try:
    # Lists ILM policies
    api_response = api_instance.grid_ilm_policies_get(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IlmApi->grid_ilm_policies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| filter by policy type | [optional] 

### Return type

[**IlmPoliciesListResponse**](IlmPoliciesListResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_ilm_policies_id_delete**
> grid_ilm_policies_id_delete(id)

Deletes a (proposed) ILM policy

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
api_instance = swagger_client.IlmApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ILM policy ID

try:
    # Deletes a (proposed) ILM policy
    api_instance.grid_ilm_policies_id_delete(id)
except ApiException as e:
    print("Exception when calling IlmApi->grid_ilm_policies_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ILM policy ID | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_ilm_policies_id_get**
> IlmPolicyGetResponse grid_ilm_policies_id_get(id)

Retrieves a single ILM policy

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
api_instance = swagger_client.IlmApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ILM policy ID

try:
    # Retrieves a single ILM policy
    api_response = api_instance.grid_ilm_policies_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IlmApi->grid_ilm_policies_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ILM policy ID | 

### Return type

[**IlmPolicyGetResponse**](IlmPolicyGetResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_ilm_policies_id_put**
> IlmPolicyPostPutResponse grid_ilm_policies_id_put(body, id)

Replaces a proposed ILM policy and optionally activates it

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
api_instance = swagger_client.IlmApi(swagger_client.ApiClient(configuration))
body = swagger_client.IlmPolicy() # IlmPolicy | 
id = 'id_example' # str | ILM policy ID

try:
    # Replaces a proposed ILM policy and optionally activates it
    api_response = api_instance.grid_ilm_policies_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IlmApi->grid_ilm_policies_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IlmPolicy**](IlmPolicy.md)|  | 
 **id** | **str**| ILM policy ID | 

### Return type

[**IlmPolicyPostPutResponse**](IlmPolicyPostPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_ilm_policies_post**
> IlmPolicyPostPutResponse grid_ilm_policies_post(body)

Creates a proposed or active policy

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
api_instance = swagger_client.IlmApi(swagger_client.ApiClient(configuration))
body = swagger_client.IlmPolicyCommon() # IlmPolicyCommon | 

try:
    # Creates a proposed or active policy
    api_response = api_instance.grid_ilm_policies_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IlmApi->grid_ilm_policies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IlmPolicyCommon**](IlmPolicyCommon.md)|  | 

### Return type

[**IlmPolicyPostPutResponse**](IlmPolicyPostPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_ilm_rules_get**
> IlmRulesListResponse grid_ilm_rules_get(include=include)

Lists ILM rules

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
api_instance = swagger_client.IlmApi(swagger_client.ApiClient(configuration))
include = 'include_example' # str | include optional information (optional)

try:
    # Lists ILM rules
    api_response = api_instance.grid_ilm_rules_get(include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IlmApi->grid_ilm_rules_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| include optional information | [optional] 

### Return type

[**IlmRulesListResponse**](IlmRulesListResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_ilm_rules_id_delete**
> grid_ilm_rules_id_delete(id)

Deletes an ILM rule

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
api_instance = swagger_client.IlmApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ILM rule ID

try:
    # Deletes an ILM rule
    api_instance.grid_ilm_rules_id_delete(id)
except ApiException as e:
    print("Exception when calling IlmApi->grid_ilm_rules_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ILM rule ID | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_ilm_rules_id_get**
> IlmRuleGetPostPutResponse grid_ilm_rules_id_get(id, include=include)

Retrieves a single ILM rule

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
api_instance = swagger_client.IlmApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ILM rule ID
include = 'include_example' # str | include optional information (optional)

try:
    # Retrieves a single ILM rule
    api_response = api_instance.grid_ilm_rules_id_get(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IlmApi->grid_ilm_rules_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ILM rule ID | 
 **include** | **str**| include optional information | [optional] 

### Return type

[**IlmRuleGetPostPutResponse**](IlmRuleGetPostPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_ilm_rules_id_put**
> IlmRuleGetPostPutResponse grid_ilm_rules_id_put(body, id)

Replaces a single ILM rule

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
api_instance = swagger_client.IlmApi(swagger_client.ApiClient(configuration))
body = swagger_client.IlmRuleRequest() # IlmRuleRequest | 
id = 'id_example' # str | ILM rule ID

try:
    # Replaces a single ILM rule
    api_response = api_instance.grid_ilm_rules_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IlmApi->grid_ilm_rules_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IlmRuleRequest**](IlmRuleRequest.md)|  | 
 **id** | **str**| ILM rule ID | 

### Return type

[**IlmRuleGetPostPutResponse**](IlmRuleGetPostPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_ilm_rules_post**
> IlmRuleGetPostPutResponse grid_ilm_rules_post(body)

Creates a new ILM rule

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
api_instance = swagger_client.IlmApi(swagger_client.ApiClient(configuration))
body = swagger_client.IlmRuleRequest() # IlmRuleRequest | 

try:
    # Creates a new ILM rule
    api_response = api_instance.grid_ilm_rules_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IlmApi->grid_ilm_rules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IlmRuleRequest**](IlmRuleRequest.md)|  | 

### Return type

[**IlmRuleGetPostPutResponse**](IlmRuleGetPostPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

