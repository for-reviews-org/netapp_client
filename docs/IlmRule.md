# IlmRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version** | **str** |  | 
**schema_version** | **str** | omitted for rules created prior to StorageGRID 10.3 | [optional] 
**display_name** | **str** | a representative and unique name for the ILM rule, immutable once the ILM rule is created | 
**description** | **str** | the description of the ILM rule | [optional] 
**active** | **bool** | when requested via include parameter, indicates whether or not the ILM rule is currently used in an active ILM policy | [optional] [default to False]
**proposed** | **bool** | when requested via include parameter, indicates whether or not the ILM rule is currently proposed for the active ILM policy | [optional] [default to False]
**permissions** | [**list[IlmRulePermissions]**](IlmRulePermissions.md) | when requested via include parameter, a list of allowed operations for this ILM rule | [optional] 
**compliance_compatible** | **bool** | when requested via include parameter, indicates whether the rule satisfies the requirements of a legacy compliant or S3 Object Lock bucket | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

