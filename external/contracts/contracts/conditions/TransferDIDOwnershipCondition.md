
Implementation of condition allowing to transfer the ownership
     between the original owner and a receiver


## Functions
### initialize
```solidity
  function initialize(
    address _owner,
    address _conditionStoreManagerAddress,
    address _didRegistryAddress
  ) external
```
initialize init the contract with the following parameters

this function is called only once during the contract
      initialization.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_owner` | address | contract's owner account address
|`_conditionStoreManagerAddress` | address | condition store manager address    
|`_didRegistryAddress` | address | DID Registry address

### hashValues
```solidity
  function hashValues(
    bytes32 _did,
    address _receiver
  ) public returns (bytes32)
```
hashValues generates the hash of condition inputs 
       with the following parameters


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to the DID in which secret store will issue the decryption keys
|`_receiver` | address | is the address of the granted user or the DID provider

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`bytes32`| bytes32 | hash of all these values
### fulfill
```solidity
  function fulfill(
    bytes32 _agreementId,
    bytes32 _did,
    address _receiver
  ) public returns (enum ConditionStoreLibrary.ConditionState)
```
fulfill the transfer DID ownership condition

only DID owner or DID provider can call this
      method. Fulfill method transfer full ownership permissions 
      to to _receiver address. 
      When true then fulfill the condition

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_agreementId` | bytes32 | agreement identifier
|`_did` | bytes32 | refers to the DID in which secret store will issue the decryption keys
|`_receiver` | address | is the address of the granted user

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`condition`| bytes32 | state (Fulfilled/Aborted)
## Events
### Fulfilled
```solidity
  event Fulfilled(
  )
```



