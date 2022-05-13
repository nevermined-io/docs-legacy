
All function calls are currently implemented without side effects

## Functions
### __ProvenanceRegistry_init
```solidity
  function __ProvenanceRegistry_init(
  ) internal
```




### __ProvenanceRegistry_init_unchained
```solidity
  function __ProvenanceRegistry_init_unchained(
  ) internal
```




### createProvenanceEntry
```solidity
  function createProvenanceEntry(
    bytes32 _provId,
    bytes32 _did,
    bytes32 _relatedDid,
    address _agentId,
    bytes32 _activityId,
    address _agentInvolvedId,
    enum ProvenanceRegistry.ProvenanceMethod _method,
    address _createdBy,
    bytes _signatureDelegate
  ) internal returns (bool)
```
create an event in the Provenance store

access modifiers and storage pointer should be implemented in ProvenanceRegistry

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_provId` | bytes32 | refers to provenance event identifier
|`_did` | bytes32 | refers to decentralized identifier (a byte32 length ID)
|`_relatedDid` | bytes32 | refers to decentralized identifier (a byte32 length ID) of a related entity
|`_agentId` | address | refers to address of the agent creating the provenance record
|`_activityId` | bytes32 | refers to activity
|`_agentInvolvedId` | address | refers to address of the agent involved with the provenance record     
|`_method` | enum ProvenanceRegistry.ProvenanceMethod | refers to the W3C Provenance method
|`_createdBy` | address | refers to address of the agent triggering the activity
|`_signatureDelegate` | bytes | refers to the digital signature provided by the did delegate.

### _wasGeneratedBy
```solidity
  function _wasGeneratedBy(
    bytes32 _provId,
    bytes32 _did,
    address _agentId,
    bytes32 _activityId,
    string _attributes
  ) internal returns (bool)
```
Implements the W3C PROV Generation action



#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_provId` | bytes32 | unique identifier referring to the provenance entry     
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID) of the entity created
|`_agentId` | address | refers to address of the agent creating the provenance record
|`_activityId` | bytes32 | refers to activity
|`_attributes` | string | refers to the provenance attributes

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`the`| bytes32 | number of the new provenance size
### _used
```solidity
  function _used(
    bytes32 _provId,
    bytes32 _did,
    address _agentId,
    bytes32 _activityId,
    bytes _signatureUsing,
    string _attributes
  ) internal returns (bool success)
```
Implements the W3C PROV Usage action



#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_provId` | bytes32 | unique identifier referring to the provenance entry     
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID) of the entity created
|`_agentId` | address | refers to address of the agent creating the provenance record
|`_activityId` | bytes32 | refers to activity
|`_signatureUsing` | bytes | refers to the digital signature provided by the agent using the _did     
|`_attributes` | string | refers to the provenance attributes

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`success`| bytes32 | true if the action was properly registered
### _wasDerivedFrom
```solidity
  function _wasDerivedFrom(
    bytes32 _provId,
    bytes32 _newEntityDid,
    bytes32 _usedEntityDid,
    address _agentId,
    bytes32 _activityId,
    string _attributes
  ) internal returns (bool success)
```
Implements the W3C PROV Derivation action



#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_provId` | bytes32 | unique identifier referring to the provenance entry     
|`_newEntityDid` | bytes32 | refers to decentralized identifier (a bytes32 length ID) of the entity created
|`_usedEntityDid` | bytes32 | refers to decentralized identifier (a bytes32 length ID) of the entity used to derive the new did
|`_agentId` | address | refers to address of the agent creating the provenance record
|`_activityId` | bytes32 | refers to activity
|`_attributes` | string | refers to the provenance attributes

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`success`| bytes32 | true if the action was properly registered
### _wasAssociatedWith
```solidity
  function _wasAssociatedWith(
    bytes32 _provId,
    bytes32 _did,
    address _agentId,
    bytes32 _activityId,
    string _attributes
  ) internal returns (bool success)
```
Implements the W3C PROV Association action



#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_provId` | bytes32 | unique identifier referring to the provenance entry     
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID) of the entity
|`_agentId` | address | refers to address of the agent creating the provenance record
|`_activityId` | bytes32 | refers to activity
|`_attributes` | string | refers to the provenance attributes

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`success`| bytes32 | true if the action was properly registered
### _actedOnBehalf
```solidity
  function _actedOnBehalf(
    bytes32 _provId,
    bytes32 _did,
    address _delegateAgentId,
    address _responsibleAgentId,
    bytes32 _activityId,
    bytes _signatureDelegate,
    string _attributes
  ) internal returns (bool success)
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
## Events
### ProvenanceAttributeRegistered
```solidity
  event ProvenanceAttributeRegistered(
  )
```
Provenance Events


### WasGeneratedBy
```solidity
  event WasGeneratedBy(
  )
```



### Used
```solidity
  event Used(
  )
```



### WasDerivedFrom
```solidity
  event WasDerivedFrom(
  )
```



### WasAssociatedWith
```solidity
  event WasAssociatedWith(
  )
```



### ActedOnBehalf
```solidity
  event ActedOnBehalf(
  )
```



