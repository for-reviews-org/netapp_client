# swagger_client.AuthApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_delete**](AuthApi.md#authorize_delete) | **DELETE** /authorize | Delete authorization token
[**authorize_post**](AuthApi.md#authorize_post) | **POST** /authorize | Get authorization token
[**authorize_saml_post**](AuthApi.md#authorize_saml_post) | **POST** /authorize-saml | Get the authentication request URI for the SAML identity provider
[**saml_response_post**](AuthApi.md#saml_response_post) | **POST** /saml-response | SAML identity provider authentication response

# **authorize_delete**
> AuthorizeResponseDelete authorize_delete()

Delete authorization token

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
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))

try:
    # Delete authorization token
    api_response = api_instance.authorize_delete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->authorize_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthorizeResponseDelete**](AuthorizeResponseDelete.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorize_post**
> AuthorizeResponse authorize_post(body)

Get authorization token

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
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
body = swagger_client.Credentials() # Credentials | 

try:
    # Get authorization token
    api_response = api_instance.authorize_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->authorize_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Credentials**](Credentials.md)|  | 

### Return type

[**AuthorizeResponse**](AuthorizeResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorize_saml_post**
> authorize_saml_post(body)

Get the authentication request URI for the SAML identity provider

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
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuthorizeSaml() # AuthorizeSaml | 

try:
    # Get the authentication request URI for the SAML identity provider
    api_instance.authorize_saml_post(body)
except ApiException as e:
    print("Exception when calling AuthApi->authorize_saml_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorizeSaml**](AuthorizeSaml.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **saml_response_post**
> AuthorizeResponse saml_response_post(saml_response=saml_response, relay_state=relay_state)

SAML identity provider authentication response

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
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
saml_response = 'saml_response_example' # str |  (optional)
relay_state = 'relay_state_example' # str |  (optional)

try:
    # SAML identity provider authentication response
    api_response = api_instance.saml_response_post(saml_response=saml_response, relay_state=relay_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->saml_response_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_response** | **str**|  | [optional] 
 **relay_state** | **str**|  | [optional] 

### Return type

[**AuthorizeResponse**](AuthorizeResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

