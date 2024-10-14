# CancelBatchOrder

Info of order to be cancelled
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_pair** | **str** | Order currency pair | 
**id** | **str** | Order ID or user custom ID. Custom ID are accepted only within 30 minutes after order creation | 
**account** | **str** | If cancelled order is cross margin order or is portfolio margin account&#39;s API key, this field must be set and can only be &#x60;cross_margin&#x60;If cancelled order is cross margin order, this field must be set and can only be &#x60;cross_margin&#x60; | [optional] 
**action_mode** | **str** | Processing Mode: When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result ACK: Asynchronous mode, only returns key order fields RESULT: No clearing information FULL: Full mode (default) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

