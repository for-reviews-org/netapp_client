# AlertNotificationReceiverPostRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | the type of notification receiver | 
**enable** | **bool** | whether alert notifications are sent to this receiver | [default to True]
**smtp_host** | **str** | the IP address or hostname of the SMTP server | 
**smtp_port** | **int** | the port to use to communicate with the SMTP server | 
**username** | **str** | the username to use to authenticate with the SMTP server | [optional] 
**password** | **str** | the password to use to authenticate with the SMTP server. Obfuscated in responses. | [optional] 
**from_email** | **str** | the email address that will appear in the From field of alert notification emails | 
**to_emails** | **list[str]** | the email addresses to send alert notifications to | 
**minimum_severity** | **str** | the minimum severity level for alert notifications. For example, \&quot;major\&quot; will not send notifications for minor alerts, but will send notifications for major or critical alerts. | 
**ca_cert** | **str** | if TLS is required, the CA certificate that will be used to verify the identity of the SMTP server | [optional] 
**client_cert** | **str** | if a client certificate is required to verify the identity of the Admin Node, the PEM-encoded certificate to send to the SMTP server. A CA certificate must also be provided | [optional] 
**client_key** | **str** | the PEM-encoded private key for the client certificate. Obfuscated in responses. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

