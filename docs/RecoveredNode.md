# RecoveredNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | a unique identifier for the historical recovery (automatically assigned when the node is recovered) | 
**tempid** | **str** | the target node&#x27;s UUID | 
**name** | **str** | the name of the node (must be a valid hostname) | 
**serverip** | **str** | the grid network ip address for the node | 
**oid** | **str** | OID of a grid node | 
**starttime** | **datetime** | the date and time when the recovery procedure was started | 
**endtime** | **datetime** | the date and time when the recovery procedure completed | 
**state** | [**NodeState**](NodeState.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

