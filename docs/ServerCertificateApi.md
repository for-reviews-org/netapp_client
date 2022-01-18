# swagger_client.ServerCertificateApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_internal_ca_certificate_get**](ServerCertificateApi.md#grid_internal_ca_certificate_get) | **GET** /grid/internal-ca-certificate | Retrieves the public CA certificate for the StorageGRID system in Privacy-Enhanced Mail (PEM) format.
[**grid_management_certificate_get**](ServerCertificateApi.md#grid_management_certificate_get) | **GET** /grid/management-certificate | Retrieves the management interface server certificate
[**grid_management_certificate_update_post**](ServerCertificateApi.md#grid_management_certificate_update_post) | **POST** /grid/management-certificate/update | Updates the management interface server certificate
[**grid_storage_api_certificate_get**](ServerCertificateApi.md#grid_storage_api_certificate_get) | **GET** /grid/storage-api-certificate | Retrieves the object storage API service endpoints server certificate
[**grid_storage_api_certificate_update_post**](ServerCertificateApi.md#grid_storage_api_certificate_update_post) | **POST** /grid/storage-api-certificate/update | Updates the object storage API service endpoints server certificate

# **grid_internal_ca_certificate_get**
> InternalCaCertificateGetResponse grid_internal_ca_certificate_get()

Retrieves the public CA certificate for the StorageGRID system in Privacy-Enhanced Mail (PEM) format.

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
api_instance = swagger_client.ServerCertificateApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the public CA certificate for the StorageGRID system in Privacy-Enhanced Mail (PEM) format.
    api_response = api_instance.grid_internal_ca_certificate_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerCertificateApi->grid_internal_ca_certificate_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InternalCaCertificateGetResponse**](InternalCaCertificateGetResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_management_certificate_get**
> CertificateRetrieveResponse grid_management_certificate_get()

Retrieves the management interface server certificate

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
api_instance = swagger_client.ServerCertificateApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the management interface server certificate
    api_response = api_instance.grid_management_certificate_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerCertificateApi->grid_management_certificate_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CertificateRetrieveResponse**](CertificateRetrieveResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_management_certificate_update_post**
> grid_management_certificate_update_post(body)

Updates the management interface server certificate

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
api_instance = swagger_client.ServerCertificateApi(swagger_client.ApiClient(configuration))
body = swagger_client.CertificateUpdateRequest() # CertificateUpdateRequest | 

try:
    # Updates the management interface server certificate
    api_instance.grid_management_certificate_update_post(body)
except ApiException as e:
    print("Exception when calling ServerCertificateApi->grid_management_certificate_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CertificateUpdateRequest**](CertificateUpdateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_storage_api_certificate_get**
> CertificateRetrieveResponse grid_storage_api_certificate_get()

Retrieves the object storage API service endpoints server certificate

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
api_instance = swagger_client.ServerCertificateApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the object storage API service endpoints server certificate
    api_response = api_instance.grid_storage_api_certificate_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerCertificateApi->grid_storage_api_certificate_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CertificateRetrieveResponse**](CertificateRetrieveResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_storage_api_certificate_update_post**
> grid_storage_api_certificate_update_post(body)

Updates the object storage API service endpoints server certificate

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
api_instance = swagger_client.ServerCertificateApi(swagger_client.ApiClient(configuration))
body = swagger_client.CertificateUpdateRequest() # CertificateUpdateRequest | 

try:
    # Updates the object storage API service endpoints server certificate
    api_instance.grid_storage_api_certificate_update_post(body)
except ApiException as e:
    print("Exception when calling ServerCertificateApi->grid_storage_api_certificate_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CertificateUpdateRequest**](CertificateUpdateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

