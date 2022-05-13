
Implementation of the Escrow Payment Condition

     The Escrow payment is reward condition in which only 
     can release reward if lock and release conditions
     are fulfilled.

## Functions
### receive
```solidity
  function receive(
  ) external
```




### initialize
```solidity
  function initialize(
    address _owner,
    address _conditionStoreManagerAddress
  ) external
```
initialize init the 
      contract with the following parameters


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_owner` | address | contract's owner account address
|`_conditionStoreManagerAddress` | address | condition store manager address

### hashValues
```solidity
  function hashValues(
    bytes32 _did,
    uint256[] _amounts,
    address[] _receivers,
    address _lockPaymentAddress,
    address _tokenAddress,
    bytes32 _lockCondition,
    bytes32 _releaseCondition
  ) public returns (bytes32)
```
hashValues generates the hash of condition inputs 
       with the following parameters


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | asset decentralized identifier               
|`_amounts` | uint256[] | token amounts to be locked/released
|`_receivers` | address[] | receiver's addresses
|`_lockPaymentAddress` | address | lock payment contract address
|`_tokenAddress` | address | the ERC20 contract address to use during the payment 
|`_lockCondition` | bytes32 | lock condition identifier
|`_releaseCondition` | bytes32 | release condition identifier

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`bytes32`| bytes32 | hash of all these values
### hashValuesLockPayment
```solidity
  function hashValuesLockPayment(
    bytes32 _did,
    address _rewardAddress,
    address _tokenAddress,
    uint256[] _amounts,
    address[] _receivers
  ) public returns (bytes32)
```
hashValuesLockPayment generates the hash of condition inputs 
       with the following parameters


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | the asset decentralized identifier 
|`_rewardAddress` | address | the contract address where the reward is locked       
|`_tokenAddress` | address | the ERC20 contract address to use during the lock payment. 
       If the address is 0x0 means we won't use a ERC20 but ETH for payment     
|`_amounts` | uint256[] | token amounts to be locked/released
|`_receivers` | address[] | receiver's addresses

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`bytes32`| bytes32 | hash of all these values
### fulfill
```solidity
  function fulfill(
    bytes32 _agreementId,
    bytes32 _did,
    uint256[] _amounts,
    address[] _receivers,
    address _lockPaymentAddress,
    address _tokenAddress,
    bytes32 _lockCondition,
    bytes32 _releaseCondition
  ) external returns (enum ConditionStoreLibrary.ConditionState)
```
fulfill escrow reward condition

fulfill method checks whether the lock and 
     release conditions are fulfilled in order to 
     release/refund the reward to receiver/sender 
     respectively.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_agreementId` | bytes32 | agreement identifier
|`_did` | bytes32 | asset decentralized identifier          
|`_amounts` | uint256[] | token amounts to be locked/released
|`_receivers` | address[] | receiver's address
|`_lockPaymentAddress` | address | lock payment contract address
|`_tokenAddress` | address | the ERC20 contract address to use during the payment
|`_lockCondition` | bytes32 | lock condition identifier
|`_releaseCondition` | bytes32 | release condition identifier

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



### Received
```solidity
  event Received(
  )
```



