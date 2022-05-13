
Implementation of the Condition Store Library.
     
     Condition is a key component in the service execution agreement. 
     This library holds the logic for creating and updating condition 
     Any Condition has only four state transitions starts with Uninitialized,
     Unfulfilled, Fulfilled, and Aborted. Condition state transition goes only 
     forward from Unintialized -> Unfulfilled -> {Fulfilled || Aborted}

## Functions
### create
```solidity
  function create(
    struct ConditionStoreLibrary.ConditionList _self,
    bytes32 _id,
    address _typeRef,
    address _creator
  ) internal returns (uint256 size)
```
create new condition

check whether the condition exists, assigns 
      condition type, condition state, last updated by, 
      and update at (which is the current block number)

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct ConditionStoreLibrary.ConditionList | is the ConditionList storage pointer
|`_id` | bytes32 | valid condition identifier
|`_typeRef` | address | condition contract address
|`_creator` | address | address of the condition creator

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`size`| struct ConditionStoreLibrary.ConditionList | is the condition index
### updateState
```solidity
  function updateState(
    struct ConditionStoreLibrary.ConditionList _self,
    bytes32 _id,
    enum ConditionStoreLibrary.ConditionState _newState
  ) internal
```
updateState update the condition state

check whether the condition state transition is right,
      assign the new state, update last updated by and
      updated at.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct ConditionStoreLibrary.ConditionList | is the ConditionList storage pointer
|`_id` | bytes32 | condition identifier
|`_newState` | enum ConditionStoreLibrary.ConditionState | the new state of the condition

