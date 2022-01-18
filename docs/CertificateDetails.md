# CertificateDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | distinguished name of this certificate&#x27;s entity | 
**issuer** | **str** | distinguished name of the entity that signed and issued this certificate | 
**serial_number** | **str** | unique certificate serial number assigned by the CA | 
**not_before** | **str** | start of validity period | 
**not_after** | **str** | end of validity period | 
**subject_alt_names** | **list[str]** | identities in addition to or in place of the identity in the subject field | [optional] 
**finger_prints** | [**CertificateFingerPrints**](CertificateFingerPrints.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

