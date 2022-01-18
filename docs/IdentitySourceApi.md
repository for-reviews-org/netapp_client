# swagger_client.IdentitySourceApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_identity_source_get**](IdentitySourceApi.md#grid_identity_source_get) | **GET** /grid/identity-source | Lists Identity Sources
[**grid_identity_source_put**](IdentitySourceApi.md#grid_identity_source_put) | **PUT** /grid/identity-source | Set or update the Identity Source
[**grid_identity_source_synchronize_post**](IdentitySourceApi.md#grid_identity_source_synchronize_post) | **POST** /grid/identity-source/synchronize | Requests that users and groups from the identity source be synchronized as soon as possible

# **grid_identity_source_get**
> IdentitySourceGetPutResponse grid_identity_source_get()

Lists Identity Sources

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
api_instance = swagger_client.IdentitySourceApi(swagger_client.ApiClient(configuration))

try:
    # Lists Identity Sources
    api_response = api_instance.grid_identity_source_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentitySourceApi->grid_identity_source_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdentitySourceGetPutResponse**](IdentitySourceGetPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_identity_source_put**
> IdentitySourceGetPutResponse grid_identity_source_put(body, test=test)

Set or update the Identity Source

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
api_instance = swagger_client.IdentitySourceApi(swagger_client.ApiClient(configuration))
body = swagger_client.IdentitySource() # IdentitySource | 
test = true # bool | If specified, tests communication with the identity source, but does not modify the stored configuration. Always succeeds if \"disable\" is omitted or set to true.  (optional)

try:
    # Set or update the Identity Source
    api_response = api_instance.grid_identity_source_put(body, test=test)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentitySourceApi->grid_identity_source_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentitySource**](IdentitySource.md)|  | 
 **test** | **bool**| If specified, tests communication with the identity source, but does not modify the stored configuration. Always succeeds if \&quot;disable\&quot; is omitted or set to true.  | [optional] 

### Return type

[**IdentitySourceGetPutResponse**](IdentitySourceGetPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_identity_source_synchronize_post**
> grid_identity_source_synchronize_post(body=body)

Requests that users and groups from the identity source be synchronized as soon as possible

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
api_instance = swagger_client.IdentitySourceApi(swagger_client.ApiClient(configuration))
body = 'body_example' # str | Ignored, leave blank (optional)

try:
    # Requests that users and groups from the identity source be synchronized as soon as possible
    api_instance.grid_identity_source_synchronize_post(body=body)
except ApiException as e:
    print("Exception when calling IdentitySourceApi->grid_identity_source_synchronize_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Ignored, leave blank | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

