# Alert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the alert&#x27;s unique identifier | 
**name** | **str** | the name of the alert | 
**annotations** | **dict(str, str)** | additional informational properties about the alert | [optional] 
**inhibited** | **bool** | whether this alert is currently suppressed by another alert | 
**inhibited_by** | **list[str]** | the ids of other alerts currently suppressing this alert | [optional] 
**labels** | **dict(str, str)** | properties that classify the alert | 
**silenced** | **bool** | whether notifications for this alert are currently suppressed by an active silence | 
**silenced_by** | **list[str]** | silences currently suppressing the alert | [optional] 
**starts_at** | **datetime** | the time the alert was triggered | 
**status** | **str** | the status of the alert | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

