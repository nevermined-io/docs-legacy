
Implementation of the Compute Execution Condition
     This condition is meant to be a signal in which triggers
     the execution of a compute service. The compute service is fully described
     in the associated DID document. The provider of the compute service will
     send this signal to its workers by fulfilling the condition where
     they are listening to the fulfilled event.

## Functions
### initialize
```solidity
  function initialize(
    address _owner,
    address _conditionStoreManagerAddress,
    address _agreementStoreManagerAddress
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
|`_agreementStoreManagerAddress` | address | agreement store manager address

### hashValues
```solidity
  function hashValues(
    bytes32 _did,
    address _computeConsumer
  ) public returns (bytes32)
```
hashValues generates the hash of condition inputs 
       with the following parameters


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | Decentralized Identifier (unique compute/asset resolver) describes the compute service
|`_computeConsumer` | address | is the consumer's address 

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`bytes32`| bytes32 | hash of all these values
### fulfill
```solidity
  function fulfill(
    bytes32 _agreementId,
    bytes32 _did,
    address _computeConsumer
  ) public returns (enum ConditionStoreLibrary.ConditionState)
```
fulfill compute execution condition

only the compute provider can fulfill this condition. By fulfilling this 
condition the compute provider will trigger the execution of 
the offered job/compute. The compute service is described in a DID document.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_agreementId` | bytes32 | agreement identifier
|`_did` | bytes32 | Decentralized Identifier (unique compute/asset resolver) describes the compute service
|`_computeConsumer` | address | is the consumer's address 

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`condition`| bytes32 | state (Fulfilled/Aborted)
### wasComputeTriggered
```solidity
  function wasComputeTriggered(
    bytes32 _did,
    address _computeConsumer
  ) public returns (bool)
```
wasComputeTriggered checks whether the compute is triggered or not.


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | Decentralized Identifier (unique compute/asset resolver) describes the compute service
|`_computeConsumer` | address | is the compute consumer's address

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| bytes32 | if the compute is triggered
## Events
### Fulfilled
```solidity
  event Fulfilled(
  )
```



