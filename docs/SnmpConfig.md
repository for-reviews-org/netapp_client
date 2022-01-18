# SnmpConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_snmp** | **bool** | Whether the SNMP agent is enabled | [optional] [default to False]
**community_strings** | **list[str]** | An array of SNMP community strings. Individual strings cannot contain whitespace. | [optional] 
**rousers** | **list[str]** | USM users allowed read-only access | [optional] 
**sys_location** | **str** | SNMP system location | [optional] 
**sys_contact** | **str** | SNMP system contact | [optional] 
**trapcommunity** | **str** | default trap community. Cannot contain whitespace. | [optional] 
**authtrapenable** | **int** | 1 - enable SNMP authentication traps, 2 - disable SNMP authentication traps (default) | [optional] 
**disable_notifications** | **bool** | Disable all SNMP notifications | [optional] [default to False]
**trap_destinations** | [**list[TrapDestination]**](TrapDestination.md) | SNMP trap destinations for V1, V2C, and Inform notifications | [optional] 
**agent_addresses** | [**list[AgentAddress]**](AgentAddress.md) | Local binding addresses for the SNMP agent. | [optional] 
**usm_users** | [**list[UsmUser]**](UsmUser.md) | USM user definitions | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

