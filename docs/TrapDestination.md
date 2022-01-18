# TrapDestination

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | SNMP trap destination type | 
**host** | **str** | SNMP trap destination host | 
**port** | **int** | SNMP trap destination port | [optional] 
**community** | **str** | SNMP trap destination community (cannot be used with usmUser). Cannot contain whitespace. | [optional] 
**usm_user** | **str** | USM user to send notification under (cannot be used with community). Cannot contain whitespace. | [optional] 
**protocol** | **str** | SNMP trap destination protocol | [optional] [default to 'udp']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

