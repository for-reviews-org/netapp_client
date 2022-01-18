# AlertSilencePostRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **datetime** | the time the silence will stop suppressing notifications | 
**comment** | **str** | a comment to describe the silence | [optional] 
**maximum_severity** | **str** | the maximum severity level for silences. For example, \&quot;major\&quot; will silence minor and major alerts, but will not silence critical alerts. | 
**matchers** | [**list[AlertSilenceMatcher]**](AlertSilenceMatcher.md) | Optionally, one or more name/value pairs used to match an alert&#x27;s labels. An alert is silenced if all specified name/value pairs match its labels. If no name/value pairs are specified, all alerts are silenced, based on the other filtering criteria. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

