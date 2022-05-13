
Implementation of the Sign Condition

## Functions
### initialize
```solidity
  function initialize(
    address _owner,
    address _conditionStoreManagerAddress
  ) external
```
initialize init the 
      contract with the following parameters

this function is called only once during the contract
      initialization.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_owner` | address | contract's owner account address
|`_conditionStoreManagerAddress` | address | condition store manager address

### hashValues
```solidity
  function hashValues(
    bytes32 _message,
    address _publicKey
  ) public returns (bytes32)
```
hashValues generates the hash of condition inputs 
       with the following parameters


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_message` | bytes32 | the message to be signed
|`_publicKey` | address | the public key of the signing address

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`bytes32`| bytes32 | hash of all these values
### fulfill
```solidity
  function fulfill(
    bytes32 _agreementId,
    bytes32 _message,
    address _publicKey,
    bytes _signature
  ) public returns (enum ConditionStoreLibrary.ConditionState)
```
fulfill validate the signed message and fulfill the condition


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_agreementId` | bytes32 | SEA agreement identifier
|`_message` | bytes32 | the message to be signed
|`_publicKey` | address | the public key of the signing address
|`_signature` | bytes | signature of the signed message using the public key

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`condition`| bytes32 | state
