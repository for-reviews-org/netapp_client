# swagger_client.MetricsApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_metric_labels_label_values_get**](MetricsApi.md#grid_metric_labels_label_values_get) | **GET** /grid/metric-labels/{label}/values | Lists the values for a metric label
[**grid_metric_names_get**](MetricsApi.md#grid_metric_names_get) | **GET** /grid/metric-names | Lists all available metric names
[**grid_metric_query_get**](MetricsApi.md#grid_metric_query_get) | **GET** /grid/metric-query | Performs an instant metric query at a single point in time
[**grid_metric_query_range_get**](MetricsApi.md#grid_metric_query_range_get) | **GET** /grid/metric-query-range | Performs a metric query over a range of time

# **grid_metric_labels_label_values_get**
> MetricsLabelsGetResponse grid_metric_labels_label_values_get(label)

Lists the values for a metric label

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
api_instance = swagger_client.MetricsApi(swagger_client.ApiClient(configuration))
label = 'label_example' # str | label name

try:
    # Lists the values for a metric label
    api_response = api_instance.grid_metric_labels_label_values_get(label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->grid_metric_labels_label_values_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| label name | 

### Return type

[**MetricsLabelsGetResponse**](MetricsLabelsGetResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_metric_names_get**
> MetricsNamesGetResponse grid_metric_names_get()

Lists all available metric names

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
api_instance = swagger_client.MetricsApi(swagger_client.ApiClient(configuration))

try:
    # Lists all available metric names
    api_response = api_instance.grid_metric_names_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->grid_metric_names_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MetricsNamesGetResponse**](MetricsNamesGetResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_metric_query_get**
> MetricsDataGetResponse grid_metric_query_get(query, time=time, timeout=timeout)

Performs an instant metric query at a single point in time

The format of metric queries is controlled by Prometheus. See https://prometheus.io/docs/querying/basics 

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
api_instance = swagger_client.MetricsApi(swagger_client.ApiClient(configuration))
query = 'storagegrid_storage_utilization_usable_space_bytes{job=\"ldr\"}' # str | Prometheus query string (default to storagegrid_storage_utilization_usable_space_bytes{job="ldr"})
time = '2013-10-20T19:20:30+01:00' # datetime | query start, default current time (date-time) (optional)
timeout = '120s' # str | timeout (duration) (optional) (default to 120s)

try:
    # Performs an instant metric query at a single point in time
    api_response = api_instance.grid_metric_query_get(query, time=time, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->grid_metric_query_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Prometheus query string | [default to storagegrid_storage_utilization_usable_space_bytes{job&#x3D;&quot;ldr&quot;}]
 **time** | **datetime**| query start, default current time (date-time) | [optional] 
 **timeout** | **str**| timeout (duration) | [optional] [default to 120s]

### Return type

[**MetricsDataGetResponse**](MetricsDataGetResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_metric_query_range_get**
> MetricsDataGetResponse grid_metric_query_range_get(query, start, end, step, timeout=timeout)

Performs a metric query over a range of time

The format of metric queries is controlled by Prometheus. See https://prometheus.io/docs/querying/basics 

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
api_instance = swagger_client.MetricsApi(swagger_client.ApiClient(configuration))
query = 'storagegrid_storage_utilization_usable_space_bytes{job=\"ldr\"}' # str | Prometheus query string (default to storagegrid_storage_utilization_usable_space_bytes{job="ldr"})
start = '2017-01-01T00:00Z' # datetime | query start (date-time) (default to 2017-01-01T00:00Z)
end = '2017-01-01T00:02Z' # datetime | query end (date-time) (default to 2017-01-01T00:02Z)
step = '2m' # str | step width (duration) (default to 2m)
timeout = '120s' # str | timeout (duration) (optional) (default to 120s)

try:
    # Performs a metric query over a range of time
    api_response = api_instance.grid_metric_query_range_get(query, start, end, step, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->grid_metric_query_range_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Prometheus query string | [default to storagegrid_storage_utilization_usable_space_bytes{job&#x3D;&quot;ldr&quot;}]
 **start** | **datetime**| query start (date-time) | [default to 2017-01-01T00:00Z]
 **end** | **datetime**| query end (date-time) | [default to 2017-01-01T00:02Z]
 **step** | **str**| step width (duration) | [default to 2m]
 **timeout** | **str**| timeout (duration) | [optional] [default to 120s]

### Return type

[**MetricsDataGetResponse**](MetricsDataGetResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

