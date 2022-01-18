# swagger_client.GridPasswordsApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_change_provisioning_passphrase_get**](GridPasswordsApi.md#grid_change_provisioning_passphrase_get) | **GET** /grid/change-provisioning-passphrase | Retrieves the status of the provisioning passphrase change
[**grid_change_provisioning_passphrase_post**](GridPasswordsApi.md#grid_change_provisioning_passphrase_post) | **POST** /grid/change-provisioning-passphrase | Changes the provisioning passphrase

# **grid_change_provisioning_passphrase_get**
> PassphraseGetResponse grid_change_provisioning_passphrase_get()

Retrieves the status of the provisioning passphrase change

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
api_instance = swagger_client.GridPasswordsApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the status of the provisioning passphrase change
    api_response = api_instance.grid_change_provisioning_passphrase_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridPasswordsApi->grid_change_provisioning_passphrase_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PassphraseGetResponse**](PassphraseGetResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_change_provisioning_passphrase_post**
> grid_change_provisioning_passphrase_post(body)

Changes the provisioning passphrase

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
api_instance = swagger_client.GridPasswordsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChangePassphraseRequest() # ChangePassphraseRequest | 

try:
    # Changes the provisioning passphrase
    api_instance.grid_change_provisioning_passphrase_post(body)
except ApiException as e:
    print("Exception when calling GridPasswordsApi->grid_change_provisioning_passphrase_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangePassphraseRequest**](ChangePassphraseRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

