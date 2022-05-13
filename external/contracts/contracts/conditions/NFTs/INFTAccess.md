


## Functions
### hashValues
```solidity
  function hashValues(
    bytes32 _documentId,
    address _grantee,
    address _contractAddress
  ) external returns (bytes32)
```
hashValues generates the hash of condition inputs 
       with the following parameters


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_documentId` | bytes32 | refers to the DID in which secret store will issue the decryption keys
|`_grantee` | address | is the address of the granted user or the DID provider
|`_contractAddress` | address | contract address holding the NFT (ERC-721) or the NFT Factory (ERC-1155)

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`bytes32`| bytes32 | hash of all these values
### fulfill
```solidity
  function fulfill(
    bytes32 _agreementId,
    bytes32 _documentId,
    address _grantee,
    address _contractAddress
  ) external returns (enum ConditionStoreLibrary.ConditionState)
```
fulfill NFT Access conditions

only DID owner or DID provider can call this
      method. Fulfill method sets the permissions 
      for the granted consumer's address to true then
      fulfill the condition

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_agreementId` | bytes32 | agreement identifier
|`_documentId` | bytes32 | refers to the DID in which secret store will issue the decryption keys
|`_grantee` | address | is the address of the granted user or the DID provider
|`_contractAddress` | address | contract address holding the NFT (ERC-721) or the NFT Factory (ERC-1155)     

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



