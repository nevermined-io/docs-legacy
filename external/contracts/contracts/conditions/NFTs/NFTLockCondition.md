
Implementation of the NFT Lock Condition

## Functions
### initialize
```solidity
  function initialize(
    address _owner,
    address _conditionStoreManagerAddress,
    address _didRegistryAddress
  ) external
```
initialize init the  contract with the following parameters

this function is called only once during the contract
      initialization.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_owner` | address | contract's owner account address
|`_conditionStoreManagerAddress` | address | condition store manager address
|`_didRegistryAddress` | address | DIDRegistry contract address

### hashValues
```solidity
  function hashValues(
    bytes32 _did,
    address _rewardAddress,
    uint256 _amount
  ) public returns (bytes32)
```
hashValues generates the hash of condition inputs 
       with the following parameters


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | the DID of the asset with NFTs attached to lock    
|`_rewardAddress` | address | the final address to receive the NFTs
|`_amount` | uint256 | is the amount of the locked tokens

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`bytes32`| bytes32 | hash of all these values
### fulfill
```solidity
  function fulfill(
    bytes32 _agreementId,
    bytes32 _did,
    address _rewardAddress,
    uint256 _amount
  ) external returns (enum ConditionStoreLibrary.ConditionState)
```
fulfill requires valid NFT transfer in order 
          to lock the amount of DID NFTs based on the SEA


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_agreementId` | bytes32 | SEA agreement identifier
|`_did` | bytes32 | Asset Decentralized Identifier    
|`_rewardAddress` | address | the contract address where the reward is locked
|`_amount` | uint256 | is the amount of tokens to be transferred 

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`condition`| bytes32 | state
### onERC1155Received
```solidity
  function onERC1155Received(
  ) external returns (bytes4)
```




### onERC1155BatchReceived
```solidity
  function onERC1155BatchReceived(
  ) external returns (bytes4)
```




### supportsInterface
```solidity
  function supportsInterface(
  ) external returns (bool)
```




## Events
### Fulfilled
```solidity
  event Fulfilled(
  )
```



