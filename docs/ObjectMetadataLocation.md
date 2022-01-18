# ObjectMetadataLocation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | the type of copy stored at this location | 
**node_id** | **str** | a unique identifier for the Grid Node (replicated only) | [optional] 
**disk_path** | **str** | full path to the disk location of the object (replicated only) | [optional] 
**profile_id** | **str** | a unique identifier for the Erasure Coding Profile (erasure coded only) | [optional] 
**fragments** | [**list[ObjectMetadataLocationFragment]**](ObjectMetadataLocationFragment.md) | the location of each erasure-coded fragment | [optional] 
**cloud_storage_pool_id** | **str** | The ID of the Cloud Storage Pool in which the object is stored | [optional] 
**cloud_storage_pool_object_key** | **str** | The key for the object in the Cloud Storage Pool | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

