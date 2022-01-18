# RecoveryStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the name of the maintenance procedure | 
**in_progress** | **bool** | true if an recovery procedure is currently running | 
**start_time** | **datetime** | the date and time when the recovery procedure was started | [optional] 
**user** | [**InitiatingUser1**](InitiatingUser1.md) |  | [optional] 
**node_in_recovery** | [**RecoveryNode**](RecoveryNode.md) |  | [optional] 
**recovered_nodes** | [**list[RecoveredNode]**](RecoveredNode.md) | list of all grid nodes that have been recovered | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

