# PatchUserRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** | the human-readable name for the User (required for local Users and imported automatically for federated Users) | [optional] 
**member_of** | **list[str]** | Group memberships for this User (required for local Users and imported automatically for federated Users) | [optional] 
**disable** | **bool** | if true, the local User cannot sign in (does not apply to federated Users) | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

