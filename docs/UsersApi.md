# swagger_client.UsersApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_users_current_user_change_password_post**](UsersApi.md#grid_users_current_user_change_password_post) | **POST** /grid/users/current-user/change-password | Updates the current Grid Administrator User&#x27;s password
[**grid_users_federated_user_short_name_get**](UsersApi.md#grid_users_federated_user_short_name_get) | **GET** /grid/users/federated-user/{shortName} | Retrieves a federated Grid Administrator User by unique name
[**grid_users_get**](UsersApi.md#grid_users_get) | **GET** /grid/users | Lists Grid Administrator Users
[**grid_users_id_change_password_post**](UsersApi.md#grid_users_id_change_password_post) | **POST** /grid/users/{id}/change-password | Updates a local Grid Administrator User password by UUID
[**grid_users_id_delete**](UsersApi.md#grid_users_id_delete) | **DELETE** /grid/users/{id} | Deletes a single Grid Administrator User
[**grid_users_id_get**](UsersApi.md#grid_users_id_get) | **GET** /grid/users/{id} | Retrieves a single Grid Administrator User
[**grid_users_id_patch**](UsersApi.md#grid_users_id_patch) | **PATCH** /grid/users/{id} | Updates a single Grid Administrator User
[**grid_users_id_put**](UsersApi.md#grid_users_id_put) | **PUT** /grid/users/{id} | Replaces a single Grid Administrator User
[**grid_users_post**](UsersApi.md#grid_users_post) | **POST** /grid/users | Creates a new local Grid Administrator User
[**grid_users_root_change_password_post**](UsersApi.md#grid_users_root_change_password_post) | **POST** /grid/users/root/change-password | Updates the root Grid Administrator password
[**grid_users_root_get**](UsersApi.md#grid_users_root_get) | **GET** /grid/users/root | Retrieves the root Grid Administrator
[**grid_users_user_short_name_change_password_post**](UsersApi.md#grid_users_user_short_name_change_password_post) | **POST** /grid/users/user/{shortName}/change-password | Updates a local Grid Administrator User password by unique name
[**grid_users_user_short_name_get**](UsersApi.md#grid_users_user_short_name_get) | **GET** /grid/users/user/{shortName} | Retrieves a local Grid Administrator User by unique name

# **grid_users_current_user_change_password_post**
> grid_users_current_user_change_password_post(body)

Updates the current Grid Administrator User's password

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.PasswordChangeRequest() # PasswordChangeRequest | 

try:
    # Updates the current Grid Administrator User's password
    api_instance.grid_users_current_user_change_password_post(body)
except ApiException as e:
    print("Exception when calling UsersApi->grid_users_current_user_change_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordChangeRequest**](PasswordChangeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_users_federated_user_short_name_get**
> GetPatchPostPutUserResponse grid_users_federated_user_short_name_get(short_name)

Retrieves a federated Grid Administrator User by unique name

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
short_name = 'short_name_example' # str | uniqueName minus prefix

try:
    # Retrieves a federated Grid Administrator User by unique name
    api_response = api_instance.grid_users_federated_user_short_name_get(short_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->grid_users_federated_user_short_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_name** | **str**| uniqueName minus prefix | 

### Return type

[**GetPatchPostPutUserResponse**](GetPatchPostPutUserResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_users_get**
> ListUsersResponse grid_users_get(type=type, limit=limit, marker=marker, include_marker=include_marker, order=order)

Lists Grid Administrator Users

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | filter by user type (optional)
limit = 25 # int | maximum number of results (optional) (default to 25)
marker = 'marker_example' # str | marker-style pagination offset (value is User's URN) (optional)
include_marker = true # bool | if set, the marker element is also returned (optional)
order = 'order_example' # str | pagination order (desc requires marker) (optional)

try:
    # Lists Grid Administrator Users
    api_response = api_instance.grid_users_get(type=type, limit=limit, marker=marker, include_marker=include_marker, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->grid_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| filter by user type | [optional] 
 **limit** | **int**| maximum number of results | [optional] [default to 25]
 **marker** | **str**| marker-style pagination offset (value is User&#x27;s URN) | [optional] 
 **include_marker** | **bool**| if set, the marker element is also returned | [optional] 
 **order** | **str**| pagination order (desc requires marker) | [optional] 

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_users_id_change_password_post**
> grid_users_id_change_password_post(body, id)

Updates a local Grid Administrator User password by UUID

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.PasswordChangeRequest() # PasswordChangeRequest | 
id = 'id_example' # str | User ID

try:
    # Updates a local Grid Administrator User password by UUID
    api_instance.grid_users_id_change_password_post(body, id)
except ApiException as e:
    print("Exception when calling UsersApi->grid_users_id_change_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordChangeRequest**](PasswordChangeRequest.md)|  | 
 **id** | **str**| User ID | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_users_id_delete**
> grid_users_id_delete(id)

Deletes a single Grid Administrator User

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | User ID

try:
    # Deletes a single Grid Administrator User
    api_instance.grid_users_id_delete(id)
except ApiException as e:
    print("Exception when calling UsersApi->grid_users_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_users_id_get**
> GetPatchPostPutUserResponse grid_users_id_get(id)

Retrieves a single Grid Administrator User

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | User ID

try:
    # Retrieves a single Grid Administrator User
    api_response = api_instance.grid_users_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->grid_users_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID | 

### Return type

[**GetPatchPostPutUserResponse**](GetPatchPostPutUserResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_users_id_patch**
> GetPatchPostPutUserResponse grid_users_id_patch(body, id)

Updates a single Grid Administrator User

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.PatchUserRequest() # PatchUserRequest | 
id = 'id_example' # str | User ID

try:
    # Updates a single Grid Administrator User
    api_response = api_instance.grid_users_id_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->grid_users_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchUserRequest**](PatchUserRequest.md)|  | 
 **id** | **str**| User ID | 

### Return type

[**GetPatchPostPutUserResponse**](GetPatchPostPutUserResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_users_id_put**
> GetPatchPostPutUserResponse grid_users_id_put(body, id)

Replaces a single Grid Administrator User

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.User() # User | 
id = 'id_example' # str | User ID

try:
    # Replaces a single Grid Administrator User
    api_response = api_instance.grid_users_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->grid_users_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)|  | 
 **id** | **str**| User ID | 

### Return type

[**GetPatchPostPutUserResponse**](GetPatchPostPutUserResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_users_post**
> GetPatchPostPutUserResponse grid_users_post(body)

Creates a new local Grid Administrator User

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.PostUserRequest() # PostUserRequest | 

try:
    # Creates a new local Grid Administrator User
    api_response = api_instance.grid_users_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->grid_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostUserRequest**](PostUserRequest.md)|  | 

### Return type

[**GetPatchPostPutUserResponse**](GetPatchPostPutUserResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_users_root_change_password_post**
> grid_users_root_change_password_post(body)

Updates the root Grid Administrator password

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.PasswordChangeRequest() # PasswordChangeRequest | 

try:
    # Updates the root Grid Administrator password
    api_instance.grid_users_root_change_password_post(body)
except ApiException as e:
    print("Exception when calling UsersApi->grid_users_root_change_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordChangeRequest**](PasswordChangeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_users_root_get**
> GetPatchPostPutUserResponse grid_users_root_get()

Retrieves the root Grid Administrator

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the root Grid Administrator
    api_response = api_instance.grid_users_root_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->grid_users_root_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPatchPostPutUserResponse**](GetPatchPostPutUserResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_users_user_short_name_change_password_post**
> grid_users_user_short_name_change_password_post(body, short_name)

Updates a local Grid Administrator User password by unique name

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.PasswordChangeRequest() # PasswordChangeRequest | 
short_name = 'short_name_example' # str | uniqueName minus prefix

try:
    # Updates a local Grid Administrator User password by unique name
    api_instance.grid_users_user_short_name_change_password_post(body, short_name)
except ApiException as e:
    print("Exception when calling UsersApi->grid_users_user_short_name_change_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordChangeRequest**](PasswordChangeRequest.md)|  | 
 **short_name** | **str**| uniqueName minus prefix | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_users_user_short_name_get**
> GetPatchPostPutUserResponse grid_users_user_short_name_get(short_name)

Retrieves a local Grid Administrator User by unique name

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
short_name = 'short_name_example' # str | uniqueName minus prefix

try:
    # Retrieves a local Grid Administrator User by unique name
    api_response = api_instance.grid_users_user_short_name_get(short_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->grid_users_user_short_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_name** | **str**| uniqueName minus prefix | 

### Return type

[**GetPatchPostPutUserResponse**](GetPatchPostPutUserResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

