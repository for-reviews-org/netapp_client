# PostAccountRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Optional. The password for the root user of the tenant account. If a password-related failure occurs, the tenant account root user cannot sign in. The response includes a metadata alert with additional details. | [optional] 
**grant_root_access_to_group** | **str** | Optional. Specify the uniqueName of an existing federated Grid Admin group. This group will be assigned the Root Access permission for the new tenant. If a group-related failure occurs, users cannot sign in to the new tenant account. The response includes a metadata alert with additional details. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

