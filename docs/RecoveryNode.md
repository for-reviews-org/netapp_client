# RecoveryNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | a unique identifier for the node (automatically assigned when the node is created) | 
**site** | **str** | the id of the site to which the node is assigned | [optional] 
**name** | **str** | the name of the node (must be a valid hostname) | 
**ntp_role** | **str** | the NTP role assigned to the node, or null to determine automatically | [optional] 
**has_adc** | **bool** | whether the grid node has an ADC (Administrative Domain Controller) service, or null to determine automatically; at least three Storage Nodes per site must contain an ADC service  | [optional] 
**type** | **str** | the node type | 
**is_primary_admin** | **bool** | whether this Admin Node is the primary Admin Node, or null if this node is not an Admin Node; immutable  | [optional] 
**configured** | **bool** | whether required properties for this node have been configured and the node has been added to a site  | 
**networks** | [**NodeNetworks**](NodeNetworks.md) |  | 
**hardware** | [**Hardware**](Hardware.md) |  | 
**progress** | [**Progress**](Progress.md) |  | 
**current_cassandra_data** | **int** | The number of bytes of Cassandra data currently on the new Storage Node. This number and the Estimated Cassandra Data Load are used to calculate the progress of the Cassandra data streaming stage during an expansion of an existing site.  | [optional] 
**estimated_cassandra_data** | **int** | The total number of bytes of Cassandra data expected for the new Storage Node. This number and the Current Cassandra Data Load are used to calculate the progress of the Cassandra data streaming stage during an expansion of an existing site.  | [optional] 
**site_cassandra_data** | **int** | The total number of bytes of Cassandra data in the same site at the start of the expansion. This number is used to calculate the Estimated Cassandra Data Load when data streaming begins during an expansion of an existing site.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

