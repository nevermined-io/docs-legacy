


## Functions
### hashValues
```solidity
  function hashValues(
    bytes32 _did,
    address _holderAddress,
    uint256 _amount,
    address _contractAddress
  ) external returns (bytes32)
```
hashValues generates the hash of condition inputs 
       with the following parameters


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | the Decentralized Identifier of the asset
|`_holderAddress` | address | the address of the NFT holder
|`_amount` | uint256 | is the amount NFTs that need to be hold by the holder
|`_contractAddress` | address | contract address holding the NFT (ERC-721) or the NFT Factory (ERC-1155)     

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`bytes32`| bytes32 | hash of all these values
### fulfill
```solidity
  function fulfill(
    bytes32 _agreementId,
    bytes32 _did,
    address _holderAddress,
    uint256 _amount,
    address _contractAddress
  ) external returns (enum ConditionStoreLibrary.ConditionState)
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
|`_contractAddress` | address | contract address holding the NFT (ERC-721) or the NFT Factory (ERC-1155)     

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`condition`| bytes32 | state
## Events
### Fulfilled
```solidity
  event Fulfilled(
  )
```



