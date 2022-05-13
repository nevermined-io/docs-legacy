


## Functions
### hashValues
```solidity
  function hashValues(
    bytes32 _did,
    address _nftReceiver,
    address _nftAmount,
    uint256 _lockCondition
  ) external returns (bytes32)
```
hashValues generates the hash of condition inputs 
       with the following parameters


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to the DID in which secret store will issue the decryption keys
|`_nftReceiver` | address | is the address of the granted user or the DID provider
|`_nftAmount` | address | amount of NFTs to transfer   
|`_lockCondition` | uint256 | lock condition identifier    

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`bytes32`| bytes32 | hash of all these values
### fulfill
```solidity
  function fulfill(
    bytes32 _agreementId,
    bytes32 _did,
    address _nftReceiver,
    uint256 _nftAmount,
    bytes32 _lockPaymentCondition
  ) external returns (enum ConditionStoreLibrary.ConditionState)
```
fulfill the transfer NFT condition

Fulfill method transfer a certain amount of NFTs 
      to the _nftReceiver address. 
      When true then fulfill the condition

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_agreementId` | bytes32 | agreement identifier
|`_did` | bytes32 | refers to the DID in which secret store will issue the decryption keys
|`_nftReceiver` | address | is the address of the account to receive the NFT
|`_nftAmount` | uint256 | amount of NFTs to transfer  
|`_lockPaymentCondition` | bytes32 | lock payment condition identifier

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



