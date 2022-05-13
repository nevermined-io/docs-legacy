
Implementation of the Whitelisting Condition

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
    address _listAddress,
    bytes32 _item
  ) public returns (bytes32)
```
hashValues generates the hash of condition inputs 
       with the following parameters


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_listAddress` | address | list contract address
|`_item` | bytes32 | item in the list

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`bytes32`| address | hash of all these values
### fulfill
```solidity
  function fulfill(
    bytes32 _agreementId,
    address _listAddress,
    bytes32 _item
  ) public returns (enum ConditionStoreLibrary.ConditionState)
```
fulfill check whether address is whitelisted
in order to fulfill the condition. This method will be 
called by any one in this whitelist. 


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_agreementId` | bytes32 | SEA agreement identifier
|`_listAddress` | address | list contract address
|`_item` | bytes32 | item in the list

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`condition`| bytes32 | state
