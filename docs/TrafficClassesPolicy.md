# TrafficClassesPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for the policy | 
**description** | **str** | A description of the policy | [optional] 
**matchers** | [**list[TrafficClassMatcher]**](TrafficClassMatcher.md) | The set of parameters to match. The traffic class will match requests where _ANY_ of these matchers match. _Note:_ One of each matcher type can be specified. | [optional] 
**limits** | [**list[TrafficClassLimit]**](TrafficClassLimit.md) | Optional limits to impose on client requests matched by this traffic class. _Note:_ One of each matcher type can be specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

