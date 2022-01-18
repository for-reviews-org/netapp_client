# IlmRuleCommon

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingest_behavior** | **str** | how objects matching this rule are stored on ingest. &#x27;dual-commit&#x27; creates interim copies and applies the rule later. &#x27;strict&#x27; and &#x27;balanced&#x27; immediately create the copies specified in the rule’s day 0 instructions. &#x27;balanced&#x27; uses &#x27;dual-commit&#x27; if following the rule instructions is not possible. | [optional] [default to 'dual-commit']
**tenant_account_id** | **str** | One or more S3 or Swift tenant account IDs to which the ILM rule applies, specified as comma-separated values. If omitted, applies to all objects. | [optional] 
**bucket_filter** | [**BucketFilter**](BucketFilter.md) |  | [optional] 
**api** | [**IlmApi**](IlmApi.md) |  | [optional] 
**reference_time** | **str** | indicates the time from which the ILM rule is applied | [default to 'ingestTime']
**logical_operator** | **str** | logical operator connecting filter criterion. Mandatory if ILM rule has more than one filter | [optional] 
**filters** | [**list[IlmFilter]**](IlmFilter.md) | filtering criteria used to determine if the ILM rule shall be applied to the evaluated object. An ILM rule without filters applies to all objects | 
**placements** | [**list[IlmPlacement]**](IlmPlacement.md) | specifies where and how object data that matches the ILM rule is stored | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

