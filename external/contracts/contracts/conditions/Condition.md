
Implementation of the Condition

     Each condition has a validation function that returns either FULFILLED, 
     ABORTED or UNFULFILLED. When a condition is successfully solved, we call 
     it FULFILLED. If a condition cannot be FULFILLED anymore due to a timeout 
     or other types of counter-proofs, the condition is ABORTED. UNFULFILLED 
     values imply that a condition has not been provably FULFILLED or ABORTED. 
     All initialized conditions start out as UNFULFILLED.

## Functions
### generateId
```solidity
  function generateId(
    bytes32 _agreementId,
    bytes32 _valueHash
  ) public returns (bytes32)
```
generateId condition Id from the following 
      parameters


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_agreementId` | bytes32 | SEA agreement ID
|`_valueHash` | bytes32 | hash of all the condition input values

### fulfill
```solidity
  function fulfill(
    bytes32 _id,
    enum ConditionStoreLibrary.ConditionState _newState
  ) internal returns (enum ConditionStoreLibrary.ConditionState)
```
fulfill set the condition state to Fulfill | Abort


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | bytes32 | condition identifier
|`_newState` | enum ConditionStoreLibrary.ConditionState | new condition state (Fulfill/Abort)

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`the`| bytes32 | updated condition state
### abortByTimeOut
```solidity
  function abortByTimeOut(
    bytes32 _id
  ) external returns (enum ConditionStoreLibrary.ConditionState)
```
abortByTimeOut set condition state to Aborted 
        if the condition is timed out


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | bytes32 | condition identifier

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`the`| bytes32 | updated condition state
