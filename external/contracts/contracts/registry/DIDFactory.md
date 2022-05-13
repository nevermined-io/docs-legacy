
Implementation of the DID Registry.

## Functions
### initialize
```solidity
  function initialize(
    address _owner
  ) public
```

DIDRegistry Initializer
     Initialize Ownable. Only on contract creation.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_owner` | address | refers to the owner of the contract.

### setManager
```solidity
  function setManager(
  ) external
```
Sets the manager role. Should be the TransferCondition contract address



### registerAttribute
```solidity
  function registerAttribute(
    bytes32 _didSeed,
    bytes32 _checksum,
    address[] _url
  ) public returns (uint256 size)
```
Register DID attributes.


The first attribute of a DID registered sets the DID owner.
     Subsequent updates record _checksum and update info.


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_didSeed` | bytes32 | refers to decentralized identifier seed (a bytes32 length ID). 
|`_checksum` | bytes32 | includes a one-way HASH calculated using the DDO content.
|`_url` | address[] | refers to the attribute value, limited to 2048 bytes.

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`size`| bytes32 | refers to the size of the registry after the register action.
### registerDID
```solidity
  function registerDID(
    bytes32 _didSeed,
    bytes32 _checksum,
    address[] _providers,
    string _url,
    bytes32 _providers,
    string _activityId,
     _attributes
  ) public returns (uint256 size)
```
Register DID attributes.


The first attribute of a DID registered sets the DID owner.
     Subsequent updates record _checksum and update info.


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_didSeed` | bytes32 | refers to decentralized identifier seed (a bytes32 length ID). 
         The final DID will be calculated with the creator address using the `hashDID` function
|`_checksum` | bytes32 | includes a one-way HASH calculated using the DDO content.
|`_providers` | address[] | list of addresses that can act as an asset provider     
|`_url` | string | refers to the url resolving the DID into a DID Document (DDO), limited to 2048 bytes.
|`_providers` | bytes32 | list of DID providers addresses
|`_activityId` | string | refers to activity
|`_attributes` |  | refers to the provenance attributes     

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`size`| bytes32 | refers to the size of the registry after the register action.
### hashDID
```solidity
  function hashDID(
    bytes32 _didSeed,
    address _creator
  ) public returns (bytes32)
```
It generates a DID using as seed a bytes32 and the address of the DID creator


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_didSeed` | bytes32 | refers to DID Seed used as base to generate the final DID
|`_creator` | address | address of the creator of the DID     

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`the`| bytes32 | new DID created
### areRoyaltiesValid
```solidity
  function areRoyaltiesValid(
    bytes32 _did,
    uint256[] _amounts,
    address[] _receivers
  ) public returns (bool)
```
areRoyaltiesValid checks if for a given DID and rewards distribution, this allocate the  
original creator royalties properly


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a byte32 length ID)
|`_amounts` | uint256[] | refers to the amounts to reward
|`_receivers` | address[] | refers to the receivers of rewards

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| bytes32 | if the rewards distribution respect the original creator royalties
### wasGeneratedBy
```solidity
  function wasGeneratedBy(
  ) internal returns (bool)
```




### used
```solidity
  function used(
  ) public returns (bool success)
```




### wasDerivedFrom
```solidity
  function wasDerivedFrom(
  ) public returns (bool success)
```




### wasAssociatedWith
```solidity
  function wasAssociatedWith(
  ) public returns (bool success)
```




### actedOnBehalf
```solidity
  function actedOnBehalf(
    bytes32 _provId,
    bytes32 _did,
    address _delegateAgentId,
    address _responsibleAgentId,
    bytes32 _activityId,
    bytes _signatureDelegate,
    string _attributes
  ) public returns (bool success)
```
Implements the W3C PROV Delegation action
Each party involved in this method (_delegateAgentId & _responsibleAgentId) must provide a valid signature.
The content to sign is a representation of the footprint of the event (_did + _delegateAgentId + _responsibleAgentId + _activityId) 



#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_provId` | bytes32 | unique identifier referring to the provenance entry
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID) of the entity
|`_delegateAgentId` | address | refers to address acting on behalf of the provenance record
|`_responsibleAgentId` | address | refers to address responsible of the provenance record
|`_activityId` | bytes32 | refers to activity
|`_signatureDelegate` | bytes | refers to the digital signature provided by the did delegate.     
|`_attributes` | string | refers to the provenance attributes

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`success`| bytes32 | true if the action was properly registered
### addDIDProvider
```solidity
  function addDIDProvider(
    bytes32 _did,
    address _provider
  ) external
```
addDIDProvider add new DID provider.


it adds new DID provider to the providers list. A provider
     is any entity that can serve the registered asset

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID).
|`_provider` | address | provider's address.

### removeDIDProvider
```solidity
  function removeDIDProvider(
    bytes32 _did,
    address _provider
  ) external
```
removeDIDProvider delete an existing DID provider.


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID).
|`_provider` | address | provider's address.

### addDIDProvenanceDelegate
```solidity
  function addDIDProvenanceDelegate(
    bytes32 _did,
    address _delegate
  ) public
```
addDIDProvenanceDelegate add new DID provenance delegate.


it adds new DID provenance delegate to the delegates list. 
A delegate is any entity that interact with the provenance entries of one DID

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID).
|`_delegate` | address | delegates's address.

### removeDIDProvenanceDelegate
```solidity
  function removeDIDProvenanceDelegate(
    bytes32 _did,
    address _delegate
  ) external
```
removeDIDProvenanceDelegate delete an existing DID delegate.


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID).
|`_delegate` | address | delegate's address.

### transferDIDOwnership
```solidity
  function transferDIDOwnership(
    bytes32 _did,
    address _newOwner
  ) external
```
transferDIDOwnership transfer DID ownership


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID)
|`_newOwner` | address | new owner address

### transferDIDOwnershipManaged
```solidity
  function transferDIDOwnershipManaged(
    address _did,
    bytes32 _newOwner
  ) external
```
transferDIDOwnershipManaged transfer DID ownership


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | address | refers to decentralized identifier (a bytes32 length ID)
|`_newOwner` | bytes32 | new owner address

### _transferDIDOwnership
```solidity
  function _transferDIDOwnership(
  ) internal
```




### grantPermission
```solidity
  function grantPermission(
    bytes32 _did,
    address _grantee
  ) external
```

grantPermission grants access permission to grantee 

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID)
|`_grantee` | address | address

### revokePermission
```solidity
  function revokePermission(
    bytes32 _did,
    address _grantee
  ) external
```

revokePermission revokes access permission from grantee 

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID)
|`_grantee` | address | address

### getPermission
```solidity
  function getPermission(
    bytes32 _did,
    address _grantee
  ) external returns (bool)
```

getPermission gets access permission of a grantee

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID)
|`_grantee` | address | address

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| bytes32 | if grantee has access permission to a DID
### isDIDProvider
```solidity
  function isDIDProvider(
    bytes32 _did,
    address _provider
  ) public returns (bool)
```
isDIDProvider check whether a given DID provider exists


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID).
|`_provider` | address | provider's address.

### getDIDRegister
```solidity
  function getDIDRegister(
    bytes32 _did
  ) public returns (address owner, bytes32 lastChecksum, string url, address lastUpdatedBy, uint256 blockNumberUpdated, address[] providers, uint256 nftSupply, uint256 mintCap, uint256 royalties)
```


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID).

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`owner`| bytes32 | the did owner
|`lastChecksum`|  | 
|`url`|  | 
|`lastUpdatedBy`|  | 
|`blockNumberUpdated`|  | 

### getBlockNumberUpdated
```solidity
  function getBlockNumberUpdated(
    bytes32 _did
  ) public returns (uint256 blockNumberUpdated)
```


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID).

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`blockNumberUpdated`| bytes32 | last modified (update) block number of a DID.
### getDIDOwner
```solidity
  function getDIDOwner(
    bytes32 _did
  ) public returns (address didOwner)
```


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID).

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`didOwner`| bytes32 | the address of the DID owner.
### getDIDRegistrySize
```solidity
  function getDIDRegistrySize(
  ) public returns (uint256 size)
```



#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`size`|  | the length of the DID registry.
### getDIDRegisterIds
```solidity
  function getDIDRegisterIds(
  ) public returns (bytes32[])
```



#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`the`|  | list of items in the DID registry.
### _grantPermission
```solidity
  function _grantPermission(
    bytes32 _did,
    address _grantee
  ) internal
```

_grantPermission grants access permission to grantee 

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID)
|`_grantee` | address | address

### _revokePermission
```solidity
  function _revokePermission(
    bytes32 _did,
    address _grantee
  ) internal
```

_revokePermission revokes access permission from grantee 

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID)
|`_grantee` | address | address

### _getPermission
```solidity
  function _getPermission(
    bytes32 _did,
    address _grantee
  ) internal returns (bool)
```

_getPermission gets access permission of a grantee

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID)
|`_grantee` | address | address 

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| bytes32 | if grantee has access permission to a DID
### getProvenanceEntry
```solidity
  function getProvenanceEntry(
    bytes32 _provId
  ) public returns (bytes32 did, bytes32 relatedDid, address agentId, bytes32 activityId, address agentInvolvedId, uint8 method, address createdBy, uint256 blockNumberUpdated, bytes signature)
```
Fetch the complete provenance entry attributes


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_provId` | bytes32 | refers to the provenance identifier

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`did`| bytes32 | 
|`relatedDid`|  | 
|`activityId`|  | 
|`agentInvolvedId`|  | 
|`createdBy`|  | 
|`blockNumberUpdated`|  | 
|`signature`|  | 

### isDIDOwner
```solidity
  function isDIDOwner(
    address _address,
    bytes32 _did
  ) public returns (bool)
```
isDIDOwner check whether a given address is owner for a DID


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_address` | address | user address.
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID).

### isOwnerProviderOrDelegate
```solidity
  function isOwnerProviderOrDelegate(
    bytes32 _did
  ) public returns (bool)
```
isOwnerProviderOrDelegate check whether msg.sender is owner, provider or
delegate for a DID given


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID).

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`boolean`| bytes32 | true if yes
### isProvenanceDelegate
```solidity
  function isProvenanceDelegate(
    bytes32 _did,
    address _delegate
  ) public returns (bool)
```
isProvenanceDelegate check whether a given DID delegate exists


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID).
|`_delegate` | address | delegate's address.

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`boolean`| bytes32 | true if yes
### getProvenanceOwner
```solidity
  function getProvenanceOwner(
    bytes32 _did
  ) public returns (address provenanceOwner)
```


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID).

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`provenanceOwner`| bytes32 | the address of the Provenance owner.
## Events
### DIDAttributeRegistered
```solidity
  event DIDAttributeRegistered(
  )
```
DID Events


### DIDProviderRemoved
```solidity
  event DIDProviderRemoved(
  )
```



### DIDProviderAdded
```solidity
  event DIDProviderAdded(
  )
```



### DIDOwnershipTransferred
```solidity
  event DIDOwnershipTransferred(
  )
```



### DIDPermissionGranted
```solidity
  event DIDPermissionGranted(
  )
```



### DIDPermissionRevoked
```solidity
  event DIDPermissionRevoked(
  )
```



### DIDProvenanceDelegateRemoved
```solidity
  event DIDProvenanceDelegateRemoved(
  )
```



### DIDProvenanceDelegateAdded
```solidity
  event DIDProvenanceDelegateAdded(
  )
```



