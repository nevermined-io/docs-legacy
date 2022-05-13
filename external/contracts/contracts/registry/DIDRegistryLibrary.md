
All function calls are currently implemented without side effects

## Functions
### update
```solidity
  function update(
    struct DIDRegistryLibrary.DIDRegisterList _self,
    bytes32 _did,
    bytes32 _checksum,
    string _url
  ) external returns (uint256 size)
```
update the DID store

access modifiers and storage pointer should be implemented in DIDRegistry

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct DIDRegistryLibrary.DIDRegisterList | refers to storage pointer
|`_did` | bytes32 | refers to decentralized identifier (a byte32 length ID)
|`_checksum` | bytes32 | includes a one-way HASH calculated using the DDO content
|`_url` | string | includes the url resolving to the DID Document (DDO)

### initializeNftConfig
```solidity
  function initializeNftConfig(
    struct DIDRegistryLibrary.DIDRegisterList _self,
    bytes32 _did,
    uint256 _cap,
    uint8 _royalties
  ) internal
```
initializeNftConfig creates the initial setup of NFTs minting and royalties distribution.
After this initial setup, this data can't be changed anymore for the DID given, even for the owner of the DID.
The reason of this is to avoid minting additional NFTs after the initial agreement, what could affect the 
valuation of NFTs of a DID already created. 

update the DID registry providers list by adding the mintCap and royalties configuration

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct DIDRegistryLibrary.DIDRegisterList | refers to storage pointer
|`_did` | bytes32 | refers to decentralized identifier (a byte32 length ID)
|`_cap` | uint256 | refers to the mint cap
|`_royalties` | uint8 | refers to the royalties to reward to the DID creator in the secondary market
       The royalties in secondary market for the creator should be between 0% >= x < 100%

### areRoyaltiesValid
```solidity
  function areRoyaltiesValid(
    struct DIDRegistryLibrary.DIDRegisterList _self,
    bytes32 _did,
    uint256[] _amounts,
    address[] _receivers
  ) internal returns (bool)
```
areRoyaltiesValid checks if for a given DID and rewards distribution, this allocate the  
original creator royalties properly


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct DIDRegistryLibrary.DIDRegisterList | refers to storage pointer
|`_did` | bytes32 | refers to decentralized identifier (a byte32 length ID)
|`_amounts` | uint256[] | refers to the amounts to reward
|`_receivers` | address[] | refers to the receivers of rewards

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| struct DIDRegistryLibrary.DIDRegisterList | if the rewards distribution respect the original creator royalties
### addProvider
```solidity
  function addProvider(
    struct DIDRegistryLibrary.DIDRegisterList _self,
    bytes32 _did,
    address provider
  ) internal
```
addProvider add provider to DID registry

update the DID registry providers list by adding a new provider

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct DIDRegistryLibrary.DIDRegisterList | refers to storage pointer
|`_did` | bytes32 | refers to decentralized identifier (a byte32 length ID)
|`provider` | address | the provider's address

### removeProvider
```solidity
  function removeProvider(
    struct DIDRegistryLibrary.DIDRegisterList _self,
    bytes32 _did,
    address _provider
  ) internal returns (bool)
```
removeProvider remove provider from DID registry

update the DID registry providers list by removing an existing provider

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct DIDRegistryLibrary.DIDRegisterList | refers to storage pointer
|`_did` | bytes32 | refers to decentralized identifier (a byte32 length ID)
|`_provider` | address | the provider's address

### updateDIDOwner
```solidity
  function updateDIDOwner(
    struct DIDRegistryLibrary.DIDRegisterList _self,
    bytes32 _did,
    address _newOwner
  ) internal
```
updateDIDOwner transfer DID ownership to a new owner


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct DIDRegistryLibrary.DIDRegisterList | refers to storage pointer
|`_did` | bytes32 | refers to decentralized identifier (a byte32 length ID)
|`_newOwner` | address | the new DID owner address

### isProvider
```solidity
  function isProvider(
    struct DIDRegistryLibrary.DIDRegisterList _self,
    bytes32 _did,
    address _provider
  ) public returns (bool)
```
isProvider check whether DID provider exists


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct DIDRegistryLibrary.DIDRegisterList | refers to storage pointer
|`_did` | bytes32 | refers to decentralized identifier (a byte32 length ID)
|`_provider` | address | the provider's address 

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| struct DIDRegistryLibrary.DIDRegisterList | if the provider already exists
### addDelegate
```solidity
  function addDelegate(
    struct DIDRegistryLibrary.DIDRegisterList _self,
    bytes32 _did,
    address delegate
  ) internal
```
addDelegate add delegate to DID registry

update the DID registry delegates list by adding a new delegate

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct DIDRegistryLibrary.DIDRegisterList | refers to storage pointer
|`_did` | bytes32 | refers to decentralized identifier (a byte32 length ID)
|`delegate` | address | the delegate's address

### removeDelegate
```solidity
  function removeDelegate(
    struct DIDRegistryLibrary.DIDRegisterList _self,
    bytes32 _did,
    address _delegate
  ) internal returns (bool)
```
removeDelegate remove delegate from DID registry

update the DID registry delegates list by removing an existing delegate

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct DIDRegistryLibrary.DIDRegisterList | refers to storage pointer
|`_did` | bytes32 | refers to decentralized identifier (a byte32 length ID)
|`_delegate` | address | the delegate's address

### isDelegate
```solidity
  function isDelegate(
    struct DIDRegistryLibrary.DIDRegisterList _self,
    bytes32 _did,
    address _delegate
  ) public returns (bool)
```
isDelegate check whether DID delegate exists


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct DIDRegistryLibrary.DIDRegisterList | refers to storage pointer
|`_did` | bytes32 | refers to decentralized identifier (a byte32 length ID)
|`_delegate` | address | the delegate's address 

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| struct DIDRegistryLibrary.DIDRegisterList | if the delegate already exists
