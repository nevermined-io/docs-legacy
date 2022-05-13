
Implementation of Epoch Library.
     For an arbitrary Epoch, this library manages the life
     cycle of an Epoch. Usually this library is used for 
     handling the time window between conditions in an agreement.
     For more information about Epoch checkout the below link
     https://github.com/oceanprotocol/OEPs/issues/119   
     TODO: update to the OEP link

## Functions
### create
```solidity
  function create(
    struct EpochLibrary.EpochList _self,
    bytes32 _timeLock,
    uint256 _timeOut
  ) internal
```
create creates new Epoch


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct EpochLibrary.EpochList | is the Epoch storage pointer
|`_timeLock` | bytes32 | value in block count (can not fulfill before)
|`_timeOut` | uint256 | value in block count (can not fulfill after)

### isTimedOut
```solidity
  function isTimedOut(
    struct EpochLibrary.EpochList _self
  ) external returns (bool)
```
isTimedOut means you cannot fulfill after


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct EpochLibrary.EpochList | is the Epoch storage pointer

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| struct EpochLibrary.EpochList | if the current block number is gt timeOut
### isTimeLocked
```solidity
  function isTimeLocked(
    struct EpochLibrary.EpochList _self
  ) external returns (bool)
```
isTimeLocked means you cannot fulfill before


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct EpochLibrary.EpochList | is the Epoch storage pointer

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| struct EpochLibrary.EpochList | if the current block number is gt timeLock
### getEpochTimeOut
```solidity
  function getEpochTimeOut(
    struct EpochLibrary.Epoch _self
  ) public returns (uint256)
```
getEpochTimeOut


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct EpochLibrary.Epoch | is the Epoch storage pointer

### getEpochTimeLock
```solidity
  function getEpochTimeLock(
    struct EpochLibrary.Epoch _self
  ) public returns (uint256)
```
getEpochTimeLock


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct EpochLibrary.Epoch | is the Epoch storage pointer

