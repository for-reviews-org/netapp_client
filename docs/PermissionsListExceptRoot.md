# PermissionsListExceptRoot

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alarm_acknowledgment** | **bool** | ability to acknowledge alarms | [optional] 
**manage_alerts** | **bool** | ability to manage silences, alert notifications, and alert rules | [optional] 
**other_grid_configuration** | **bool** | ability to access configuration pages not covered by other permissions | [optional] 
**grid_topology_page_configuration** | **bool** | ability to access Grid Topology configuration tabs and modify otherGridConfiguration pages | [optional] 
**tenant_accounts** | **bool** | ability to add, edit, or remove tenant accounts (The deprecated management API v1 also uses this permission to manage tenant group policies, reset Swift admin passwords, and manage root user S3 access keys.)  | [optional] 
**change_tenant_root_password** | **bool** | ability to reset the root user password for tenant accounts  | [optional] 
**maintenance** | **bool** | ability to perform maintenance procedures: software upgrade, expansion, decommission, and Recovery Package download; ability to configure DNS servers, NTP servers, grid license, domain names, server certificates, and audit; ability to collect logs; ability to list HA groups.  | [optional] 
**metrics_query** | **bool** | ability to perform custom Prometheus metrics queries  | [optional] 
**activate_features** | **bool** | ability to reactivate features that have been deactivated via the deactivated-features endpoints (This permission is provided for the option of deactivating it for security; the deactivated-features endpoints require rootAccess, so it is not useful to grant this permission to groups. Warning: this permission itself cannot be reactivated once deactivated, except by technical support.)  | [optional] [default to False]
**ilm** | **bool** | ability to add, edit, or set ILM policies, ILM rules, and EC profiles; ability to simulate ILM evaluation of objects on the grid  | [optional] 
**object_metadata** | **bool** | ability to look up object metadata for any object stored on the grid  | [optional] 
**storage_admin** | **bool** | ability to view and update settings in E-Series SANtricity System Manager from StorageGRID  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

