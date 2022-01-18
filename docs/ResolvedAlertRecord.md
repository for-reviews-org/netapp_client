# ResolvedAlertRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **int** | Internal ID of the record | 
**name** | **str** | The unique name of the alert rule that triggered the alert | 
**instance** | **str** | The grid node on which this alert occurred | [optional] 
**severity** | **str** | The severity level of the alert | 
**event** | **str** | The type of the event | 
**labels** | [**ResolvedalertrecordLabels**](ResolvedalertrecordLabels.md) |  | 
**annotations** | **dict(str, str)** | Additional informational properties about the alert | 
**inhibited** | **bool** | Whether this alert has been suppressed by another alert for its entire lifespan | 
**status** | **str** | The status of the alert | 
**id** | **str** | The fingerprint of the alert&#x27;s labels | 
**start_time** | **datetime** | The time when the alert was triggered | 
**end_time** | **datetime** | The time when the alert was resolved | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

