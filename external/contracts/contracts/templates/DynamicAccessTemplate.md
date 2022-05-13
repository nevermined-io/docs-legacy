
Implementation of Agreement Template
This is a dynamic template that allows to setup flexible conditions depending 
on the use case.


## Functions
### initialize
```solidity
  function initialize(
    address _owner,
    address _agreementStoreManagerAddress,
    address _didRegistryAddress
  ) external
```
initialize init the 
      contract with the following parameters.

this function is called only once during the contract
      initialization. It initializes the ownable feature, and 
      set push the required condition types including 
      access secret store, lock reward and escrow reward conditions.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_owner` | address | contract's owner account address
|`_agreementStoreManagerAddress` | address | agreement store manager contract address
|`_didRegistryAddress` | address | DID registry contract address

### addTemplateCondition
```solidity
  function addTemplateCondition(
    address _conditionAddress
  ) external returns (uint256 length)
```
addTemplateCondition adds a new condition to the template


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_conditionAddress` | address | condition contract address

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`length`| address | conditionTypes array size
### removeLastTemplateCondition
```solidity
  function removeLastTemplateCondition(
  ) external returns (address[])
```
removeLastTemplateCondition removes last condition added to the template



#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`conditionTypes`|  | existing in the array
