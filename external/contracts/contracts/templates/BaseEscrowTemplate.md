


## Functions
### createAgreement
```solidity
  function createAgreement(
    bytes32 _id,
    bytes32 _did,
    bytes32[] _conditionIds,
    uint256[] _timeLocks,
    uint256[] _timeOuts,
    address _accessConsumer
  ) public returns (uint256 size)
```
createAgreement creates agreements through agreement template

this function initializes the agreement by setting the DID,
      conditions ID, timeouts, time locks and the consumer address.
      The DID provider/owner is automatically detected by the DID
      Registry

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | bytes32 | SEA agreement unique identifier
|`_did` | bytes32 | Decentralized Identifier (DID)
|`_conditionIds` | bytes32[] | conditions ID associated with the condition types
|`_timeLocks` | uint256[] | the starting point of the time window ,time lock is 
      in block number not seconds
|`_timeOuts` | uint256[] | the ending point of the time window ,time lock is 
      in block number not seconds
|`_accessConsumer` | address | consumer address

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`size`| bytes32 | the agreement index
### getAgreementData
```solidity
  function getAgreementData(
    bytes32 _id
  ) external returns (address accessConsumer, address accessProvider)
```
getAgreementData return the agreement Data


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | bytes32 | SEA agreement unique identifier

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`accessConsumer`| bytes32 | the agreement consumer
|`accessProvider`|  | the provider addresses
## Events
### AgreementCreated
```solidity
  event AgreementCreated(
  )
```



