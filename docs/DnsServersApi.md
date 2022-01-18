# swagger_client.DnsServersApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_dns_servers_get**](DnsServersApi.md#grid_dns_servers_get) | **GET** /grid/dns-servers | Lists configured external DNS servers
[**grid_dns_servers_put**](DnsServersApi.md#grid_dns_servers_put) | **PUT** /grid/dns-servers | Change the external DNS servers used by the grid

# **grid_dns_servers_get**
> GetDnsServersResponse grid_dns_servers_get()

Lists configured external DNS servers

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
api_instance = swagger_client.DnsServersApi(swagger_client.ApiClient(configuration))

try:
    # Lists configured external DNS servers
    api_response = api_instance.grid_dns_servers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsServersApi->grid_dns_servers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetDnsServersResponse**](GetDnsServersResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_dns_servers_put**
> GetDnsServersResponse grid_dns_servers_put(body)

Change the external DNS servers used by the grid

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
api_instance = swagger_client.DnsServersApi(swagger_client.ApiClient(configuration))
body = [swagger_client.DnsServer()] # list[DnsServer] | IP addresses of the external DNS servers

try:
    # Change the external DNS servers used by the grid
    api_response = api_instance.grid_dns_servers_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsServersApi->grid_dns_servers_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DnsServer]**](DnsServer.md)| IP addresses of the external DNS servers | 

### Return type

[**GetDnsServersResponse**](GetDnsServersResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

