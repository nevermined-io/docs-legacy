
Implementation of Agreement Template

     Agreement template is a reference template where it
     has the ability to create agreements from whitelisted 
     template

## Functions
### createAgreement
```solidity
  function createAgreement(
    bytes32 _id,
    bytes32 _did,
    bytes32[] _conditionIds,
    uint256[] _timeLocks,
    uint256[] _timeOuts
  ) public returns (uint256 size)
```
createAgreement create new agreement


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | bytes32 | agreement unique identifier
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID).
|`_conditionIds` | bytes32[] | list of condition identifiers
|`_timeLocks` | uint256[] | list of time locks, each time lock will be assigned to the 
         same condition that has the same index
|`_timeOuts` | uint256[] | list of time outs, each time out will be assigned to the 
         same condition that has the same index

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`size`| bytes32 | the index of the created agreement
### getConditionTypes
```solidity
  function getConditionTypes(
  ) public returns (address[])
```
getConditionTypes gets the conditions addresses list

for the current template returns list of condition contracts 
     addresses


#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`list`|  | of conditions contract addresses
