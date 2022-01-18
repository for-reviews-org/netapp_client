# ObjectMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | a unique identifier for the object | 
**version_id** | **str** | the object version ID. Objects that are not versioned have a null version ID | [optional] 
**account_id** | **str** | the ID of the Tenant Account that uploaded the object. Objects uploaded by anonymous users have a null account ID  | [optional] 
**name** | **str** | the name of the object, including any prefixes but excluding the bucket or container name  | 
**container** | **str** | the name of the Swift container or S3 bucket that contains the object | 
**object_size_bytes** | **int** | the original object size in bytes | 
**disk_size_bytes** | **int** | the amount of disk space consumed by the object; not available if segmented object | [optional] 
**creation_time** | **datetime** | date and time when the object was uploaded | 
**modified_time** | **datetime** | date and time when the object was last modified | 
**last_access_time** | **datetime** | date and time when the object was last accessed. To use this option, updates to Last Access Time must be enabled for the S3 bucket or Swift container  | 
**user_metadata** | **dict(str, list[str])** | key-value pairs for any user-defined metadata applied to the object. | [optional] 
**tags** | **dict(str, str)** | key-value pairs for any tags applied to the object | [optional] 
**locations** | [**list[ObjectMetadataLocation]**](ObjectMetadataLocation.md) | how and where the object is stored | 
**segmentation** | [**ObjectMetadataSegmentation**](ObjectMetadataSegmentation.md) |  | 
**encrypted** | **bool** | object is encrypted | [default to False]
**raw** | **object** | all object metadata in the unprocessed internal storage format | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

