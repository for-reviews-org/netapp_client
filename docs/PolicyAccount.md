# PolicyAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_account_identity_source** | **bool** | whether the tenant account should configure its own identity source. If false, the tenant uses the grid-wide identity source. | [default to True]
**allow_platform_services** | **bool** | allows a tenant to use platform services features such as CloudMirror. These features send data to an external service that is specified using a StorageGRID endpoint. | [default to False]
**quota_object_bytes** | **int** | the maximum number of bytes available for this tenant&#x27;s objects. Represents a logical amount (object size), not a physical amount (size on disk). If null, an unlimited number of bytes is available. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

