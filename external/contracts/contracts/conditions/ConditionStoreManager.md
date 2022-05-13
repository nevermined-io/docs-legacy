
Implementation of the Condition Store Manager.

     Condition store manager is responsible for enforcing the 
     the business logic behind creating/updating the condition state
     based on the assigned role to each party. Only specific type of
     contracts are allowed to call this contract, therefore there are 
     two types of roles, create role that in which is able to create conditions.
     The second role is the update role, which is can update the condition state.
     Also, it support delegating the roles to other contract(s)/account(s).

## Functions
### initialize
```solidity
  function initialize(
    address _owner
  ) public
```

initialize ConditionStoreManager Initializer
     Initialize Ownable. Only on contract creation, 

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_owner` | address | refers to the owner of the contract

### getCreateRole
```solidity
  function getCreateRole(
  ) external returns (address)
```

getCreateRole get the address of contract
     which has the create role


#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`create`|  | condition role address
### delegateCreateRole
```solidity
  function delegateCreateRole(
    address delegatee
  ) external
```

delegateCreateRole only owner can delegate the 
     create condition role to a different address

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`delegatee` | address | delegatee address

### delegateUpdateRole
```solidity
  function delegateUpdateRole(
    bytes32 delegatee
  ) external
```

delegateUpdateRole only owner can delegate 
     the update role to a different address for 
     specific condition Id which has the create role

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`delegatee` | bytes32 | delegatee address

### createCondition
```solidity
  function createCondition(
    bytes32 _id,
    address _typeRef
  ) external returns (uint256 size)
```

createCondition only called by create role address 
     the condition should use a valid condition contract 
     address, valid time lock and timeout. Moreover, it 
     enforce the condition state transition from 
     Uninitialized to Unfulfilled.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | bytes32 | unique condition identifier
|`_typeRef` | address | condition contract address

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`size`| bytes32 | the index of the created condition
### createCondition
```solidity
  function createCondition(
    bytes32 _id,
    address _typeRef,
    address _creator
  ) external returns (uint256 size)
```

createCondition only called by create role address 
     the condition should use a valid condition contract 
     address, valid time lock and timeout. Moreover, it 
     enforce the condition state transition from 
     Uninitialized to Unfulfilled.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | bytes32 | unique condition identifier
|`_typeRef` | address | condition contract address
|`_creator` | address | address of the condition creator    

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`size`| bytes32 | the index of the created condition
### createCondition
```solidity
  function createCondition(
    bytes32 _id,
    address _typeRef,
    uint256 _timeLock,
    uint256 _timeOut,
    address _creator
  ) public returns (uint256 size)
```

createCondition only called by create role address 
     the condition should use a valid condition contract 
     address, valid time lock and timeout. Moreover, it 
     enforce the condition state transition from 
     Uninitialized to Unfulfilled.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | bytes32 | unique condition identifier
|`_typeRef` | address | condition contract address
|`_timeLock` | uint256 | start of the time window
|`_timeOut` | uint256 | end of the time window
|`_creator` | address | address of the condition creator     

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`size`| bytes32 | the index of the created condition
### updateConditionState
```solidity
  function updateConditionState(
    bytes32 _id
  ) external returns (enum ConditionStoreLibrary.ConditionState)
```

updateConditionState only called by update role address. 
     It enforce the condition state transition to either 
     Fulfill or Aborted state

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | bytes32 | unique condition identifier

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`the`| bytes32 | current condition state
### getConditionListSize
```solidity
  function getConditionListSize(
  ) external returns (uint256 size)
```

getConditionListSize 


#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`size`|  | the length of the condition list
### getCondition
```solidity
  function getCondition(
  ) external returns (address typeRef, enum ConditionStoreLibrary.ConditionState state, uint256 timeLock, uint256 timeOut, uint256 blockNumber, address createdBy, address lastUpdatedBy, uint256 blockNumberUpdated)
```

getCondition  


#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`typeRef`| bytes32 | the type reference
|`state`|  | condition state
|`timeLock`|  | the time lock
|`timeOut`|  | time out
|`blockNumber`|  | block number
|`createdBy`|  | address
|`lastUpdatedBy`|  | address
|`blockNumberUpdated`|  | block number updated
### getConditionState
```solidity
  function getConditionState(
  ) external returns (enum ConditionStoreLibrary.ConditionState)
```

getConditionState  


#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`condition`| bytes32 | state
### getConditionTypeRef
```solidity
  function getConditionTypeRef(
  ) external returns (address)
```

getConditionTypeRef  


#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`condition`| bytes32 | typeRef
### getConditionCreatedBy
```solidity
  function getConditionCreatedBy(
  ) external returns (address)
```

getConditionCreatedBy  


#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`condition`| bytes32 | createdBy address
### isConditionTimeLocked
```solidity
  function isConditionTimeLocked(
  ) public returns (bool)
```

isConditionTimeLocked  


#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`whether`| bytes32 | the condition is timedLock ended
### isConditionTimedOut
```solidity
  function isConditionTimedOut(
  ) public returns (bool)
```

isConditionTimedOut  


#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`whether`| bytes32 | the condition is timed out
## Events
### ConditionCreated
```solidity
  event ConditionCreated(
  )
```



### ConditionUpdated
```solidity
  event ConditionUpdated(
  )
```



