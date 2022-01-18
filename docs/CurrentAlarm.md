# CurrentAlarm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | the Node ID or OID of the alarm source | 
**severity** | **str** | severity level of the alarm | 
**attribute_code** | **str** | the four-character code for the alarm source attribute | 
**attribute_index** | **int** | multi-value attributes use the index to indicate which value triggered the alarm, starting at 1 | 
**trigger_value** | **str** | the attribute value at the time the alarm was triggered | 
**trigger_time** | **datetime** | the date and time when the alarm was triggered | 
**acknowledge_time** | **datetime** | the date and time when the alarm was acknowledged, or null if not acknowledged | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

