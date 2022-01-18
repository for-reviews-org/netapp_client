# swagger_client.GroupsApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_groups_federated_group_short_name_get**](GroupsApi.md#grid_groups_federated_group_short_name_get) | **GET** /grid/groups/federated-group/{shortName} | Retrieves a federated Grid Administrator Group by unique name
[**grid_groups_get**](GroupsApi.md#grid_groups_get) | **GET** /grid/groups | Lists Grid Administrator Groups
[**grid_groups_group_short_name_get**](GroupsApi.md#grid_groups_group_short_name_get) | **GET** /grid/groups/group/{shortName} | Retrieves a local Grid Administrator Group by unique name
[**grid_groups_id_delete**](GroupsApi.md#grid_groups_id_delete) | **DELETE** /grid/groups/{id} | Deletes a single Grid Administrator Group
[**grid_groups_id_get**](GroupsApi.md#grid_groups_id_get) | **GET** /grid/groups/{id} | Retrieves a single Grid Administrator Group by UUID
[**grid_groups_id_patch**](GroupsApi.md#grid_groups_id_patch) | **PATCH** /grid/groups/{id} | Updates a single Grid Administrator Group
[**grid_groups_id_put**](GroupsApi.md#grid_groups_id_put) | **PUT** /grid/groups/{id} | Replaces a single Grid Administrator Group
[**grid_groups_post**](GroupsApi.md#grid_groups_post) | **POST** /grid/groups | Creates a new Grid Administrator Group

# **grid_groups_federated_group_short_name_get**
> GetPatchPostPutGroupResponse grid_groups_federated_group_short_name_get(short_name)

Retrieves a federated Grid Administrator Group by unique name

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
short_name = 'short_name_example' # str | uniqueName minus prefix

try:
    # Retrieves a federated Grid Administrator Group by unique name
    api_response = api_instance.grid_groups_federated_group_short_name_get(short_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->grid_groups_federated_group_short_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_name** | **str**| uniqueName minus prefix | 

### Return type

[**GetPatchPostPutGroupResponse**](GetPatchPostPutGroupResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_groups_get**
> ListGroupsResponse grid_groups_get(type=type, limit=limit, marker=marker, include_marker=include_marker, order=order)

Lists Grid Administrator Groups

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | filter by group type (optional)
limit = 25 # int | maximum number of results (optional) (default to 25)
marker = 'marker_example' # str | marker-style pagination offset (value is Group's URN) (optional)
include_marker = true # bool | if set, the marker element is also returned (optional)
order = 'order_example' # str | pagination order (desc requires marker) (optional)

try:
    # Lists Grid Administrator Groups
    api_response = api_instance.grid_groups_get(type=type, limit=limit, marker=marker, include_marker=include_marker, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->grid_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| filter by group type | [optional] 
 **limit** | **int**| maximum number of results | [optional] [default to 25]
 **marker** | **str**| marker-style pagination offset (value is Group&#x27;s URN) | [optional] 
 **include_marker** | **bool**| if set, the marker element is also returned | [optional] 
 **order** | **str**| pagination order (desc requires marker) | [optional] 

### Return type

[**ListGroupsResponse**](ListGroupsResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_groups_group_short_name_get**
> GetPatchPostPutGroupResponse grid_groups_group_short_name_get(short_name)

Retrieves a local Grid Administrator Group by unique name

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
short_name = 'short_name_example' # str | uniqueName minus prefix

try:
    # Retrieves a local Grid Administrator Group by unique name
    api_response = api_instance.grid_groups_group_short_name_get(short_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->grid_groups_group_short_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_name** | **str**| uniqueName minus prefix | 

### Return type

[**GetPatchPostPutGroupResponse**](GetPatchPostPutGroupResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_groups_id_delete**
> grid_groups_id_delete(id)

Deletes a single Grid Administrator Group

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Group ID

try:
    # Deletes a single Grid Administrator Group
    api_instance.grid_groups_id_delete(id)
except ApiException as e:
    print("Exception when calling GroupsApi->grid_groups_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group ID | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_groups_id_get**
> GetPatchPostPutGroupResponse grid_groups_id_get(id)

Retrieves a single Grid Administrator Group by UUID

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Group ID

try:
    # Retrieves a single Grid Administrator Group by UUID
    api_response = api_instance.grid_groups_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->grid_groups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group ID | 

### Return type

[**GetPatchPostPutGroupResponse**](GetPatchPostPutGroupResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_groups_id_patch**
> GetPatchPostPutGroupResponse grid_groups_id_patch(body, id)

Updates a single Grid Administrator Group

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PatchGroupRequest() # PatchGroupRequest | 
id = 'id_example' # str | Group ID

try:
    # Updates a single Grid Administrator Group
    api_response = api_instance.grid_groups_id_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->grid_groups_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchGroupRequest**](PatchGroupRequest.md)|  | 
 **id** | **str**| Group ID | 

### Return type

[**GetPatchPostPutGroupResponse**](GetPatchPostPutGroupResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_groups_id_put**
> GetPatchPostPutGroupResponse grid_groups_id_put(body, id)

Replaces a single Grid Administrator Group

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Group() # Group | 
id = 'id_example' # str | Group ID

try:
    # Replaces a single Grid Administrator Group
    api_response = api_instance.grid_groups_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->grid_groups_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Group**](Group.md)|  | 
 **id** | **str**| Group ID | 

### Return type

[**GetPatchPostPutGroupResponse**](GetPatchPostPutGroupResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_groups_post**
> GetPatchPostPutGroupResponse grid_groups_post(body)

Creates a new Grid Administrator Group

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PostGroupRequest() # PostGroupRequest | 

try:
    # Creates a new Grid Administrator Group
    api_response = api_instance.grid_groups_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->grid_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostGroupRequest**](PostGroupRequest.md)|  | 

### Return type

[**GetPatchPostPutGroupResponse**](GetPatchPostPutGroupResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

