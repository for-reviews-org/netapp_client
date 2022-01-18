# TrafficClassMatcher

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The attribute of the request to match. * &#x60;bucket&#x60; - The S3 bucket (or Swift container) being accessed * &#x60;bucket-regex&#x60; - A regular expression to evaluate against the S3 bucket (or Swift container) being accessed * &#x60;cidr&#x60; - Matches if the client request source IP is in the specified IPv4 CIDR (RFC4632) * &#x60;endpoint&#x60; - The UUID of the load balancer endpoint which the client is connecting to * &#x60;tenant&#x60; - Matches if the S3 bucket (or Swift container) is owned by the tenant account with this ID  | 
**inverse** | **bool** | If true, the matcher will apply for all requests that do not match __Warning:__ Creating an inverse matcher with more than 1 member will likely match all requests. Use with caution. | [optional] [default to False]
**members** | **list[str]** | A list of members to match on. The policy will match a request if _ANY_ of the elements listed match. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

