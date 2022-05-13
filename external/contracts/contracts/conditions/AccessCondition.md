
Implementation of the Access Condition

     Access Secret Store Condition is special condition
     where a client or Parity secret store can encrypt/decrypt documents 
     based on the on-chain granted permissions. For a given DID 
     document, and agreement ID, the owner/provider of the DID 
     will fulfill the condition. Consequently secret store 
     will check whether the permission is granted for the consumer
     in order to encrypt/decrypt the document.

## Functions
### initialize
```solidity
  function initialize(
    address _owner,
    address _conditionStoreManagerAddress,
    address _agreementStoreManagerAddress
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
|`_agreementStoreManagerAddress` | address | agreement store manager address

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
### fulfill
```solidity
  function fulfill(
    bytes32 _agreementId,
    bytes32 _documentId,
    address _grantee
  ) public returns (enum ConditionStoreLibrary.ConditionState)
```
fulfill access secret store condition

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

### renouncePermission
```solidity
  function renouncePermission(
    address _grantee,
    bytes32 _documentId
  ) public
```
renouncePermission is called only by DID owner or provider


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
checkPermissions is called by Parity secret store


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_documentId` | address | refers to the DID in which secret store will issue the decryption keys
|`_grantee` | bytes32 | is the address of the granted user or the DID provider

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`permissionGranted`| address | true if the access was granted
## Events
### Fulfilled
```solidity
  event Fulfilled(
  )
```



