# GetNtpServersResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **list[str]** | the list of IP addresses of the external NTP servers | 
**read_only** | **bool** | true if an NTP server list update is still in progress | [optional] 
**alerts** | [**list[NtpServersAlert]**](NtpServersAlert.md) | Only present when the current NTP configuration is in progress or the last configuration failed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

