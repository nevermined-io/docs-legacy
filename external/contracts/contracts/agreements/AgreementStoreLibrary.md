
Implementation of the Agreement Store Library.
     For more information: https://github.com/oceanprotocol/OEPs/issues/125    
     TODO: update the OEP link 
     The agreement store library holds the business logic
     in which manages the life cycle of SEA agreement, each 
     agreement is linked to the DID of an asset, template, and
     condition IDs.

## Functions
### create
```solidity
  function create(
    struct AgreementStoreLibrary.AgreementList _self,
    bytes32 _id,
    bytes32 _did,
    address _templateId,
    bytes32[] _conditionIds
  ) internal returns (uint256 size)
```

create new agreement
     checks whether the agreement Id exists, creates new agreement 
     instance, including the template, conditions and DID.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct AgreementStoreLibrary.AgreementList | is AgreementList storage pointer
|`_id` | bytes32 | agreement identifier
|`_did` | bytes32 | asset decentralized identifier
|`_templateId` | address | template identifier
|`_conditionIds` | bytes32[] | array of condition identifiers

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`size`| struct AgreementStoreLibrary.AgreementList | which is the index of the created agreement
