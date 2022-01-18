# NodeExpanded

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hardware** | [**Hardware**](Hardware.md) |  | [optional] 
**progress** | [**Progress**](Progress.md) |  | [optional] 
**current_cassandra_data** | **int** | The number of bytes of Cassandra data currently on the new Storage Node. This number and the Estimated Cassandra Data Load are used to calculate the progress of the Cassandra data streaming stage during an expansion of an existing site.  | [optional] 
**estimated_cassandra_data** | **int** | The total number of bytes of Cassandra data expected for the new Storage Node. This number and the Current Cassandra Data Load are used to calculate the progress of the Cassandra data streaming stage during an expansion of an existing site.  | [optional] 
**site_cassandra_data** | **int** | The total number of bytes of Cassandra data in the same site at the start of the expansion. This number is used to calculate the Estimated Cassandra Data Load when data streaming begins during an expansion of an existing site.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

