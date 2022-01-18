# Replicated

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_id** | **str** | One or more storage pools where object data is saved, specified as comma-separated values. Either poolId or cloudStoragePoolId is required. | [optional] 
**temporary_pool_id** | **str** | Temporary locations are deprecated and should not be used for new ILM rules. If you select the Strict ingest behavior, the temporary location is ignored. | [optional] 
**cloud_storage_pool_id** | **str** | Cloud Storage Pool where object data is saved. Cloud Storage Pools cannot be used in the same placement as a storage pool. Either poolId or cloudStoragePoolId is required. | [optional] 
**copies** | **int** | number of replicated copies | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

