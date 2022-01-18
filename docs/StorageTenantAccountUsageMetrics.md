# StorageTenantAccountUsageMetrics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_time** | **datetime** | time when the usage data was calculated | 
**object_count** | **int** | number of objects under this Account | 
**data_bytes** | **int** | logical size in bytes of all objects under this Account | 
**buckets** | [**list[ContainerUsageMetrics]**](ContainerUsageMetrics.md) | per-container usage metrics (including S3 buckets) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

