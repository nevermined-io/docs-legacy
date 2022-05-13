
Implementation of the Lock Payment Condition
This condition allows to lock payment for multiple receivers taking
into account the royalties to be paid to the original creators in a secondary market.

## Functions
### initialize
```solidity
  function initialize(
    address _owner,
    address _conditionStoreManagerAddress,
    address _didRegistryAddress
  ) external
```
initialize init the contract with the following parameters

this function is called only once during the contract initialization.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_owner` | address | contract's owner account address
|`_conditionStoreManagerAddress` | address | condition store manager address
|`_didRegistryAddress` | address | DID Registry address

### hashValues
```solidity
  function hashValues(
    bytes32 _did,
    address _rewardAddress,
    address _tokenAddress,
    uint256[] _amounts,
    address[] _receivers
  ) public returns (bytes32)
```
hashValues generates the hash of condition inputs 
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
    address payable _rewardAddress,
    address _tokenAddress,
    uint256[] _amounts,
    address[] _receivers
  ) external returns (enum ConditionStoreLibrary.ConditionState)
```
fulfill requires valid token transfer in order 
          to lock the amount of tokens based on the SEA


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_agreementId` | bytes32 | the agreement identifier
|`_did` | bytes32 | the asset decentralized identifier
|`_rewardAddress` | address payable | the contract address where the reward is locked
|`_tokenAddress` | address | the ERC20 contract address to use during the lock payment. 
|`_amounts` | uint256[] | token amounts to be locked/released
|`_receivers` | address[] | receiver's addresses

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`condition`| bytes32 | state
### _transferERC20
```solidity
  function _transferERC20(
    address _rewardAddress,
    address _tokenAddress,
    uint256 _amount
  ) internal
```
_transferERC20 transfer ERC20 tokens 

Will throw if transfer fails
#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_rewardAddress` | address | the address to receive the tokens
|`_tokenAddress` | address | the ERC20 contract address to use during the payment
|`_amount` | uint256 | token amount to be locked/released


### _transferETH
```solidity
  function _transferETH(
    address payable _rewardAddress,
    uint256 _amount
  ) internal
```
_transferETH transfer ETH 


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_rewardAddress` | address payable | the address to receive the ETH
|`_amount` | uint256 | ETH amount to be locked/released

## Events
### Fulfilled
```solidity
  event Fulfilled(
  )
```



