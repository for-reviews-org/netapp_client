# swagger_client.AccountsApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_accounts_cache_get**](AccountsApi.md#grid_accounts_cache_get) | **GET** /grid/accounts-cache | Lists cached Storage Tenant Accounts
[**grid_accounts_get**](AccountsApi.md#grid_accounts_get) | **GET** /grid/accounts | Lists Storage Tenant Accounts
[**grid_accounts_id_change_password_post**](AccountsApi.md#grid_accounts_id_change_password_post) | **POST** /grid/accounts/{id}/change-password | Changes the root user password for the Storage Tenant Account
[**grid_accounts_id_delete**](AccountsApi.md#grid_accounts_id_delete) | **DELETE** /grid/accounts/{id} | Deletes a single Storage Tenant Account
[**grid_accounts_id_get**](AccountsApi.md#grid_accounts_id_get) | **GET** /grid/accounts/{id} | Retrieves a single Storage Tenant Account
[**grid_accounts_id_patch**](AccountsApi.md#grid_accounts_id_patch) | **PATCH** /grid/accounts/{id} | Updates a single Storage Tenant Account
[**grid_accounts_id_put**](AccountsApi.md#grid_accounts_id_put) | **PUT** /grid/accounts/{id} | Replaces a single Storage Tenant Account
[**grid_accounts_id_usage_get**](AccountsApi.md#grid_accounts_id_usage_get) | **GET** /grid/accounts/{id}/usage | Gets the storage usage information for the Storage Tenant Account
[**grid_accounts_post**](AccountsApi.md#grid_accounts_post) | **POST** /grid/accounts | Creates a new Storage Tenant Account

# **grid_accounts_cache_get**
> ListAccountsCacheResponse grid_accounts_cache_get(limit=limit)

Lists cached Storage Tenant Accounts

Lists the tenant accounts in the cache and includes additional information, such as objectCount and dataBytes. Updates to tenants might take 15 minutes to appear in cached data.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
limit = 25 # int | maximum number of results (optional) (default to 25)

try:
    # Lists cached Storage Tenant Accounts
    api_response = api_instance.grid_accounts_cache_get(limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->grid_accounts_cache_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| maximum number of results | [optional] [default to 25]

### Return type

[**ListAccountsCacheResponse**](ListAccountsCacheResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_accounts_get**
> ListAccountsResponse grid_accounts_get(limit=limit, marker=marker, include_marker=include_marker, order=order)

Lists Storage Tenant Accounts

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
limit = 25 # int | maximum number of results (optional) (default to 25)
marker = 'marker_example' # str | marker-style pagination offset (value is Account's id) (optional)
include_marker = true # bool | if set, the marker element is also returned (optional)
order = 'order_example' # str | pagination order (desc requires marker) (optional)

try:
    # Lists Storage Tenant Accounts
    api_response = api_instance.grid_accounts_get(limit=limit, marker=marker, include_marker=include_marker, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->grid_accounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| maximum number of results | [optional] [default to 25]
 **marker** | **str**| marker-style pagination offset (value is Account&#x27;s id) | [optional] 
 **include_marker** | **bool**| if set, the marker element is also returned | [optional] 
 **order** | **str**| pagination order (desc requires marker) | [optional] 

### Return type

[**ListAccountsResponse**](ListAccountsResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_accounts_id_change_password_post**
> grid_accounts_id_change_password_post(body, id)

Changes the root user password for the Storage Tenant Account

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChangePassword() # ChangePassword | 
id = 'id_example' # str | ID of Storage Tenant Account

try:
    # Changes the root user password for the Storage Tenant Account
    api_instance.grid_accounts_id_change_password_post(body, id)
except ApiException as e:
    print("Exception when calling AccountsApi->grid_accounts_id_change_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangePassword**](ChangePassword.md)|  | 
 **id** | **str**| ID of Storage Tenant Account | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_accounts_id_delete**
> grid_accounts_id_delete(id)

Deletes a single Storage Tenant Account

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of Storage Tenant Account

try:
    # Deletes a single Storage Tenant Account
    api_instance.grid_accounts_id_delete(id)
except ApiException as e:
    print("Exception when calling AccountsApi->grid_accounts_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Storage Tenant Account | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_accounts_id_get**
> GetPatchPutAccountResponse grid_accounts_id_get(id)

Retrieves a single Storage Tenant Account

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of Storage Tenant Account

try:
    # Retrieves a single Storage Tenant Account
    api_response = api_instance.grid_accounts_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->grid_accounts_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Storage Tenant Account | 

### Return type

[**GetPatchPutAccountResponse**](GetPatchPutAccountResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_accounts_id_patch**
> GetPatchPutAccountResponse grid_accounts_id_patch(body, id)

Updates a single Storage Tenant Account

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccountNoId() # AccountNoId | 
id = 'id_example' # str | ID of Storage Tenant Account

try:
    # Updates a single Storage Tenant Account
    api_response = api_instance.grid_accounts_id_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->grid_accounts_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountNoId**](AccountNoId.md)|  | 
 **id** | **str**| ID of Storage Tenant Account | 

### Return type

[**GetPatchPutAccountResponse**](GetPatchPutAccountResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_accounts_id_put**
> GetPatchPutAccountResponse grid_accounts_id_put(body, id)

Replaces a single Storage Tenant Account

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Account() # Account | 
id = 'id_example' # str | ID of Storage Tenant Account

try:
    # Replaces a single Storage Tenant Account
    api_response = api_instance.grid_accounts_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->grid_accounts_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Account**](Account.md)|  | 
 **id** | **str**| ID of Storage Tenant Account | 

### Return type

[**GetPatchPutAccountResponse**](GetPatchPutAccountResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_accounts_id_usage_get**
> AccountUsageResponse grid_accounts_id_usage_get(id, strict_consistency=strict_consistency)

Gets the storage usage information for the Storage Tenant Account

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of Storage Tenant Account
strict_consistency = true # bool | If true, the request fails if the results cannot be retrieved at a strong-global consistency. If false (default), attempts to retrieve usage information use strong-global consistency initially but fall back to a strong-site consistency. (optional)

try:
    # Gets the storage usage information for the Storage Tenant Account
    api_response = api_instance.grid_accounts_id_usage_get(id, strict_consistency=strict_consistency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->grid_accounts_id_usage_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Storage Tenant Account | 
 **strict_consistency** | **bool**| If true, the request fails if the results cannot be retrieved at a strong-global consistency. If false (default), attempts to retrieve usage information use strong-global consistency initially but fall back to a strong-site consistency. | [optional] 

### Return type

[**AccountUsageResponse**](AccountUsageResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_accounts_post**
> CreateAccountResponse grid_accounts_post(body)

Creates a new Storage Tenant Account

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PostAccountRequest() # PostAccountRequest | 

try:
    # Creates a new Storage Tenant Account
    api_response = api_instance.grid_accounts_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->grid_accounts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostAccountRequest**](PostAccountRequest.md)|  | 

### Return type

[**CreateAccountResponse**](CreateAccountResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

