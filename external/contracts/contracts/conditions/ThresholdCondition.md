
Implementation of the Threshold Condition

     Threshold condition acts as a filter for a set of input condition(s) in which sends 
     a signal whether to complete the flow execution or abort it. This type of conditions 
     works as intermediary conditions where they wire SEA conditions in order to support  
     more complex scenarios.

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
    bytes32[] inputConditions,
    uint256 threshold
  ) public returns (bytes32)
```
hashValues generates the hash of condition inputs 
       with the following parameters


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`inputConditions` | bytes32[] | array of input conditions IDs
|`threshold` | uint256 | the required number of fulfilled input conditions

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`bytes32`| bytes32[] | hash of all these values
### fulfill
```solidity
  function fulfill(
    bytes32 _agreementId,
    bytes32[] _inputConditions,
    uint256 threshold
  ) external returns (enum ConditionStoreLibrary.ConditionState)
```
fulfill threshold condition

the fulfill method check whether input conditions are
      fulfilled or not.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_agreementId` | bytes32 | agreement identifier
|`_inputConditions` | bytes32[] | array of input conditions IDs
|`threshold` | uint256 | the required number of fulfilled input conditions

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`condition`| bytes32 | state (Fulfilled/Aborted)
