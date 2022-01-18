# Node

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | a unique identifier for the node (automatically assigned when the node is created) | 
**site** | **str** | the id of the site to which the node is assigned | 
**name** | **str** | the name of the node (must be a valid hostname) | 
**ntp_role** | **str** | the NTP role assigned to the node, or null to determine automatically | [optional] 
**has_adc** | **bool** | whether the grid node has an ADC (Administrative Domain Controller) service, or null to determine automatically; at least three Storage Nodes per site must contain an ADC service  | [optional] 
**type** | **str** | the node type | 
**is_primary_admin** | **bool** | whether this Admin Node is the primary Admin Node, or null if this node is not an Admin Node; immutable  | [optional] 
**configured** | **bool** | whether required properties for this node have been configured and the node has been added to a site  | 
**networks** | [**NodeNetworks**](NodeNetworks.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

