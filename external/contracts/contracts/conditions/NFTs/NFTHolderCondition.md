
Implementation of the Nft Holder Condition

## Functions
### initialize
```solidity
  function initialize(
    address _owner,
    address _conditionStoreManagerAddress,
    address _didRegistryAddress
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
|`_didRegistryAddress` | address | DIDRegistry address

### hashValues
```solidity
  function hashValues(
    bytes32 _did,
    address _holderAddress,
    uint256 _amount
  ) public returns (bytes32)
```
hashValues generates the hash of condition inputs 
       with the following parameters


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | the Decentralized Identifier of the asset
|`_holderAddress` | address | the address of the NFT holder
|`_amount` | uint256 | is the amount NFTs that need to be hold by the holder

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`bytes32`| bytes32 | hash of all these values
### hashValues
```solidity
  function hashValues(
  ) public returns (bytes32)
```




### fulfill
```solidity
  function fulfill(
    bytes32 _agreementId,
    bytes32 _did,
    address _holderAddress,
    uint256 _amount
  ) public returns (enum ConditionStoreLibrary.ConditionState)
```
fulfill requires a validation that holder has enough
      NFTs for a specific DID


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_agreementId` | bytes32 | SEA agreement identifier
|`_did` | bytes32 | the Decentralized Identifier of the asset    
|`_holderAddress` | address | the contract address where the reward is locked
|`_amount` | uint256 | is the amount of NFT to be hold

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`condition`| bytes32 | state
### fulfill
```solidity
  function fulfill(
  ) public returns (enum ConditionStoreLibrary.ConditionState)
```




