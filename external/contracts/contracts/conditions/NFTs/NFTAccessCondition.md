
Implementation of the Access Condition specific for NFTs

     NFT Access Condition is special condition used to give access 
     to a specific NFT related to a DID.

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
|`_didRegistryAddress` | address | DID registry address

### hashValues
```solidity
  function hashValues(
    bytes32 _documentId,
    address _grantee
  ) public returns (bytes32)
```
hashValues generates the hash of condition inputs 
       with the following parameters


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_documentId` | bytes32 | refers to the DID in which secret store will issue the decryption keys
|`_grantee` | address | is the address of the granted user or the DID provider

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
    bytes32 _documentId,
    address _grantee
  ) public returns (enum ConditionStoreLibrary.ConditionState)
```
fulfill NFT Access condition

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

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`condition`| bytes32 | state (Fulfilled/Aborted)
### fulfill
```solidity
  function fulfill(
    bytes32 _agreementId,
    bytes32 _documentId,
    address _grantee,
    address _contractAddress
  ) public returns (enum ConditionStoreLibrary.ConditionState)
```
fulfill NFT Access condition

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
|`_contractAddress` | address | is the contract address of the NFT implementation (ERC-1155 or ERC-721)

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`condition`| bytes32 | state (Fulfilled/Aborted)
### grantPermission
```solidity
  function grantPermission(
    address _grantee,
    bytes32 _documentId
  ) public
```
grantPermission is called only by DID owner or provider


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_grantee` | address | is the address of the granted user or the DID provider
|`_documentId` | bytes32 | refers to the DID in which secret store will issue the decryption keys

### checkPermissions
```solidity
  function checkPermissions(
    address _documentId,
    bytes32 _grantee
  ) external returns (bool permissionGranted)
```
checkPermissions is called to validate the permissions of user related to the NFT attached to an asset


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_documentId` | address | refers to the DID 
|`_grantee` | bytes32 | is the address of the granted user or the DID provider

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`permissionGranted`| address | true if the access was granted
