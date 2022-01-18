# swagger_client.ExpansionSitesApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_expansion_sites_get**](ExpansionSitesApi.md#grid_expansion_sites_get) | **GET** /grid/expansion/sites | Retrieves the list of existing and new sites (empty until expansion is started)
[**grid_expansion_sites_id_delete**](ExpansionSitesApi.md#grid_expansion_sites_id_delete) | **DELETE** /grid/expansion/sites/{id} | Deletes a site
[**grid_expansion_sites_id_get**](ExpansionSitesApi.md#grid_expansion_sites_id_get) | **GET** /grid/expansion/sites/{id} | Retrieves a site
[**grid_expansion_sites_id_put**](ExpansionSitesApi.md#grid_expansion_sites_id_put) | **PUT** /grid/expansion/sites/{id} | Updates the details of a site
[**grid_expansion_sites_post**](ExpansionSitesApi.md#grid_expansion_sites_post) | **POST** /grid/expansion/sites | Adds a new site

# **grid_expansion_sites_get**
> ListSitesResponse grid_expansion_sites_get()

Retrieves the list of existing and new sites (empty until expansion is started)

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
api_instance = swagger_client.ExpansionSitesApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the list of existing and new sites (empty until expansion is started)
    api_response = api_instance.grid_expansion_sites_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionSitesApi->grid_expansion_sites_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListSitesResponse**](ListSitesResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_expansion_sites_id_delete**
> grid_expansion_sites_id_delete(id)

Deletes a site

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
api_instance = swagger_client.ExpansionSitesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | site ID

try:
    # Deletes a site
    api_instance.grid_expansion_sites_id_delete(id)
except ApiException as e:
    print("Exception when calling ExpansionSitesApi->grid_expansion_sites_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| site ID | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_expansion_sites_id_get**
> GetSitesResponse grid_expansion_sites_id_get(id)

Retrieves a site

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
api_instance = swagger_client.ExpansionSitesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | site ID

try:
    # Retrieves a site
    api_response = api_instance.grid_expansion_sites_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionSitesApi->grid_expansion_sites_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| site ID | 

### Return type

[**GetSitesResponse**](GetSitesResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_expansion_sites_id_put**
> PostPutSitesResponse grid_expansion_sites_id_put(body, id)

Updates the details of a site

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
api_instance = swagger_client.ExpansionSitesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Site() # Site | 
id = 'id_example' # str | site ID

try:
    # Updates the details of a site
    api_response = api_instance.grid_expansion_sites_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionSitesApi->grid_expansion_sites_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Site**](Site.md)|  | 
 **id** | **str**| site ID | 

### Return type

[**PostPutSitesResponse**](PostPutSitesResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_expansion_sites_post**
> PostPutSitesResponse grid_expansion_sites_post(body)

Adds a new site

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
api_instance = swagger_client.ExpansionSitesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PostSiteRequest() # PostSiteRequest | 

try:
    # Adds a new site
    api_response = api_instance.grid_expansion_sites_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionSitesApi->grid_expansion_sites_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostSiteRequest**](PostSiteRequest.md)|  | 

### Return type

[**PostPutSitesResponse**](PostPutSitesResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

