
Implementation of the Agreement Store.

     The agreement store generates conditions for an agreement template.
     Agreement templates must to be approved in the Template Store
     Each agreement is linked to the DID of an asset.

## Functions
### initialize
```solidity
  function initialize(
    address _owner,
    address _conditionStoreManagerAddress,
    address _templateStoreManagerAddress,
    address _didRegistryAddress
  ) public
```

initialize AgreementStoreManager Initializer
     Initializes Ownable. Only on contract creation.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_owner` | address | refers to the owner of the contract
|`_conditionStoreManagerAddress` | address | is the address of the connected condition store
|`_templateStoreManagerAddress` | address | is the address of the connected template store
|`_didRegistryAddress` | address | is the address of the connected DID Registry

### createAgreement
```solidity
  function createAgreement(
    bytes32 _id,
    bytes32 _did,
    address[] _conditionTypes,
    bytes32[] _conditionIds,
    uint256[] _timeLocks,
    uint256[] _timeOuts
  ) public returns (uint256 size)
```

Create a new agreement and associate the agreement created to the address originating the transaction.
     The agreement will create conditions of conditionType with conditionId.
     Only "approved" templates can access this function.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | bytes32 | is the ID of the new agreement. Must be unique.
|`_did` | bytes32 | is the bytes32 DID of the asset. The DID must be registered beforehand.
|`_conditionTypes` | address[] | is a list of addresses that point to Condition contracts.
|`_conditionIds` | bytes32[] | is a list of bytes32 content-addressed Condition IDs
|`_timeLocks` | uint256[] | is a list of uint time lock values associated to each Condition
|`_timeOuts` | uint256[] | is a list of uint time out values associated to each Condition

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`size`| bytes32 | the size of the agreement list after the create action.
### createAgreement
```solidity
  function createAgreement(
    bytes32 _id,
    bytes32 _did,
    address[] _conditionTypes,
    bytes32[] _conditionIds,
    uint256[] _timeLocks,
    uint256[] _timeOuts,
    address _creator
  ) public returns (uint256 size)
```

Create a new agreement.
     The agreement will create conditions of conditionType with conditionId.
     Only "approved" templates can access this function.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | bytes32 | is the ID of the new agreement. Must be unique.
|`_did` | bytes32 | is the bytes32 DID of the asset. The DID must be registered beforehand.
|`_conditionTypes` | address[] | is a list of addresses that point to Condition contracts.
|`_conditionIds` | bytes32[] | is a list of bytes32 content-addressed Condition IDs
|`_timeLocks` | uint256[] | is a list of uint time lock values associated to each Condition
|`_timeOuts` | uint256[] | is a list of uint time out values associated to each Condition
|`_creator` | address | address of the account associated as agreement and conditions creator

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`size`| bytes32 | the size of the agreement list after the create action.
### getAgreement
```solidity
  function getAgreement(
    bytes32 _id
  ) external returns (bytes32 did, address didOwner, address templateId, bytes32[] conditionIds, address lastUpdatedBy, uint256 blockNumberUpdated)
```

Get agreement with _id.
     The agreement will create conditions of conditionType with conditionId.
     Only "approved" templates can access this function.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | bytes32 | is the ID of the agreement.


### getAgreementDIDOwner
```solidity
  function getAgreementDIDOwner(
    bytes32 _id
  ) external returns (address didOwner)
```

get the DID owner for this agreement with _id.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | bytes32 | is the ID of the agreement.

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`didOwner`| bytes32 | the DID owner associated with agreement.did from the DID registry.
### isAgreementDIDOwner
```solidity
  function isAgreementDIDOwner(
    bytes32 _id,
    address _owner
  ) external returns (bool)
```

check the DID owner for this agreement with _id.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | bytes32 | is the ID of the agreement.
|`_owner` | address | is the DID owner

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`the`| bytes32 | DID owner associated with agreement.did from the DID registry.
### isAgreementDIDProvider
```solidity
  function isAgreementDIDProvider(
    bytes32 _id,
    address _provider
  ) external returns (bool)
```

isAgreementDIDProvider for a given agreement Id 
and address check whether a DID provider is associated with this agreement

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | bytes32 | is the ID of the agreement
|`_provider` | address | is the DID provider

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| bytes32 | if a DID provider is associated with the agreement ID
### getAgreementListSize
```solidity
  function getAgreementListSize(
  ) public returns (uint256 size)
```



#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`size`|  | the length of the agreement list.
### getAgreementIdsForDID
```solidity
  function getAgreementIdsForDID(
    bytes32 _did
  ) public returns (bytes32[])
```


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | is the bytes32 DID of the asset.

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`the`| bytes32 | agreement IDs for a given DID
### getAgreementIdsForTemplateId
```solidity
  function getAgreementIdsForTemplateId(
    address _templateId
  ) public returns (bytes32[])
```


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_templateId` | address | is the address of the agreement template.

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`the`| address | agreement IDs for a given DID
### getDIDRegistryAddress
```solidity
  function getDIDRegistryAddress(
  ) public returns (address)
```

getDIDRegistryAddress utility function 
used by other contracts or any EOA.


#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`the`|  | DIDRegistry address
