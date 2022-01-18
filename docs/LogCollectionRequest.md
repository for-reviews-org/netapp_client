# LogCollectionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passphrase** | **str** | provisioning passphrase | 
**nodes** | **list[str]** | list of target grid node UUIDs (To find a node ID (UUID), use the health/topology API. Alternatively, go to the Nodes page and select the node, or look in the /etc/node_id file.) | 
**notes** | **str** | a message to send to technical support | [optional] 
**range_start** | **datetime** | log collection start time | 
**range_end** | **datetime** | log collection end time | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

