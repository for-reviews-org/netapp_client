# LogCollectionStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the name of the maintenance procedure | 
**in_progress** | **bool** | true if a log collection procedure is in progress | 
**error** | **str** | an error message if a problem has occurred, otherwise null | [optional] 
**start_time** | **datetime** | the date and time when the log collection procedure was started | [optional] 
**end_time** | **datetime** | the date and time when the log collection procedure completed | [optional] 
**file_name** | **str** | the name of the log collection file, or null if not ready to download | [optional] 
**nodes** | [**list[SingleNodeStatus]**](SingleNodeStatus.md) | status of the log collection on each grid node | [optional] 
**notes** | **str** | a message to send to technical support | [optional] 
**range_start** | **datetime** | log collection start time | [optional] 
**range_end** | **datetime** | log collection end time | [optional] 
**percentage** | **int** | the total progress percentage for the procedure | [optional] 
**user** | [**InitiatingUser**](InitiatingUser.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

