
Implementation of the Nft Holder Condition

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
  ) public returns (bytes32)
```




### fulfill
```solidity
  function fulfill(
  ) external returns (enum ConditionStoreLibrary.ConditionState)
```




