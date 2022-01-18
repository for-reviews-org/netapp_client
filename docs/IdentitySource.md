# IdentitySource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | a unique identifier for the identity source (automatically assigned when the identity source is configured) | 
**disable** | **bool** | whether the identity source will be used for authentication | [optional] [default to True]
**hostname** | **str** | the server hostname or IP address of the identity source | 
**port** | **int** | the port to use to connect to the identity source | 
**username** | **str** | the username to use to access the identity source | 
**password** | **str** | the password to use to access the identity source | 
**base_group_dn** | **str** | the fully qualified Distinguished Name (DN) of an LDAP subtree you want to search for groups | 
**base_user_dn** | **str** | the fully qualified Distinguished Name (DN) of an LDAP subtree you want to search for users | 
**ldap_service_type** | **str** | type of the LDAP service | 
**type** | **str** | type of the identity source | [optional] [default to 'ldap']
**ldap_user_id_attribute** | **str** | LDAP attribute that identifies the LDAP user who attempts authentication with unique name/login (only required when ldapServiceType is \&quot;Other\&quot;) | [optional] 
**ldap_user_uuid_attribute** | **str** | LDAP attribute that identifies the LDAP user&#x27;s permanent unique identity (only required when ldapServiceType is \&quot;Other\&quot;) | [optional] 
**ldap_group_id_attribute** | **str** | LDAP attribute that identifies the LDAP group of the user who attempts authentication (only required when ldapServiceType is \&quot;Other\&quot;) | [optional] 
**ldap_group_uuid_attribute** | **str** | LDAP attribute that identifies the LDAP group&#x27;s permanent unique identity (only required when ldapServiceType is \&quot;Other\&quot;) | [optional] 
**disable_tls** | **bool** | whether Transport Layer Security (TLS) is used to connect to the identity source server | [optional] [default to False]
**enable_ldaps** | **bool** | whether to use LDAPS instead of STARTTLS to connect to the identity source server. STARTTLS is the default and is recommended. | [optional] [default to False]
**ca_cert** | **str** | custom certificate to use to connect to the identity source server (if no custom certificate is supplied and TLS is enabled, the Operating System CA certificate will be used) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

