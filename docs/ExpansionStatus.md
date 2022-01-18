# ExpansionStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the name of the maintenance procedure | 
**in_progress** | **bool** | true if an expansion procedure is currently being configured or is running | 
**error** | **str** | an error message if a problem has occurred, otherwise null | 
**configured** | **bool** | whether the expansion procedure has been configured | 
**provision** | [**ProvisioningStatus**](ProvisioningStatus.md) |  | 
**start_time** | **datetime** | the date and time when the expansion procedure was started | [optional] 
**end_time** | **datetime** | the date and time when the expansion procedure completed | [optional] 
**user** | [**InitiatingUser2**](InitiatingUser2.md) |  | [optional] 
**stages** | [**list[ExpansionStageState]**](ExpansionStageState.md) | state of each overall stage of the expansion procedure | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

