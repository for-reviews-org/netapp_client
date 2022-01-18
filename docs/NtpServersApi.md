# swagger_client.NtpServersApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_ntp_servers_get**](NtpServersApi.md#grid_ntp_servers_get) | **GET** /grid/ntp-servers | Lists configured external NTP servers
[**grid_ntp_servers_update_post**](NtpServersApi.md#grid_ntp_servers_update_post) | **POST** /grid/ntp-servers/update | Change the external NTP servers used by the grid

# **grid_ntp_servers_get**
> GetNtpServersResponse grid_ntp_servers_get()

Lists configured external NTP servers

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
api_instance = swagger_client.NtpServersApi(swagger_client.ApiClient(configuration))

try:
    # Lists configured external NTP servers
    api_response = api_instance.grid_ntp_servers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NtpServersApi->grid_ntp_servers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNtpServersResponse**](GetNtpServersResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_ntp_servers_update_post**
> Response grid_ntp_servers_update_post(body, force_save=force_save)

Change the external NTP servers used by the grid

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
api_instance = swagger_client.NtpServersApi(swagger_client.ApiClient(configuration))
body = swagger_client.NtpChangeRequest() # NtpChangeRequest | 
force_save = true # bool | update the external NTP servers without connection testing (optional)

try:
    # Change the external NTP servers used by the grid
    api_response = api_instance.grid_ntp_servers_update_post(body, force_save=force_save)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NtpServersApi->grid_ntp_servers_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NtpChangeRequest**](NtpChangeRequest.md)|  | 
 **force_save** | **bool**| update the external NTP servers without connection testing | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

