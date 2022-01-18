# swagger_client.ClientCertificatesApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_client_certificates_get**](ClientCertificatesApi.md#grid_client_certificates_get) | **GET** /grid/client-certificates | Lists all client certificates configured on the grid
[**grid_client_certificates_id_delete**](ClientCertificatesApi.md#grid_client_certificates_id_delete) | **DELETE** /grid/client-certificates/{id} | Deletes a single client certificate
[**grid_client_certificates_id_get**](ClientCertificatesApi.md#grid_client_certificates_id_get) | **GET** /grid/client-certificates/{id} | Retrieves a single client certificate
[**grid_client_certificates_id_put**](ClientCertificatesApi.md#grid_client_certificates_id_put) | **PUT** /grid/client-certificates/{id} | Replaces a single client certificate
[**grid_client_certificates_post**](ClientCertificatesApi.md#grid_client_certificates_post) | **POST** /grid/client-certificates | Creates a client certificate

# **grid_client_certificates_get**
> ListClientCertificatesResponse grid_client_certificates_get()

Lists all client certificates configured on the grid

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
api_instance = swagger_client.ClientCertificatesApi(swagger_client.ApiClient(configuration))

try:
    # Lists all client certificates configured on the grid
    api_response = api_instance.grid_client_certificates_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientCertificatesApi->grid_client_certificates_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListClientCertificatesResponse**](ListClientCertificatesResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_client_certificates_id_delete**
> grid_client_certificates_id_delete(id)

Deletes a single client certificate

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
api_instance = swagger_client.ClientCertificatesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Client certificate ID

try:
    # Deletes a single client certificate
    api_instance.grid_client_certificates_id_delete(id)
except ApiException as e:
    print("Exception when calling ClientCertificatesApi->grid_client_certificates_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Client certificate ID | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_client_certificates_id_get**
> ClientCertificateGetPostPutResponse grid_client_certificates_id_get(id)

Retrieves a single client certificate

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
api_instance = swagger_client.ClientCertificatesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Client certificate ID

try:
    # Retrieves a single client certificate
    api_response = api_instance.grid_client_certificates_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientCertificatesApi->grid_client_certificates_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Client certificate ID | 

### Return type

[**ClientCertificateGetPostPutResponse**](ClientCertificateGetPostPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_client_certificates_id_put**
> ClientCertificateGetPostPutResponse grid_client_certificates_id_put(body, id)

Replaces a single client certificate

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
api_instance = swagger_client.ClientCertificatesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClientCertificate() # ClientCertificate | The new client certificate configuration
id = 'id_example' # str | Client certificate ID

try:
    # Replaces a single client certificate
    api_response = api_instance.grid_client_certificates_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientCertificatesApi->grid_client_certificates_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientCertificate**](ClientCertificate.md)| The new client certificate configuration | 
 **id** | **str**| Client certificate ID | 

### Return type

[**ClientCertificateGetPostPutResponse**](ClientCertificateGetPostPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_client_certificates_post**
> ClientCertificateGetPostPutResponse grid_client_certificates_post(body)

Creates a client certificate

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
api_instance = swagger_client.ClientCertificatesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClientCertificate() # ClientCertificate | 

try:
    # Creates a client certificate
    api_response = api_instance.grid_client_certificates_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientCertificatesApi->grid_client_certificates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientCertificate**](ClientCertificate.md)|  | 

### Return type

[**ClientCertificateGetPostPutResponse**](ClientCertificateGetPostPutResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

