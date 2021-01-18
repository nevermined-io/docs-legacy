# Provenance API Reference

Nevermined Smart Contracts implement the [W3C Provenance](https://www.w3.org/TR/prov-overview/) specification allowing to register on-chain all the provenance information, digital signatures and fingerprints allowing to make use of an open, transparent and unique source of truth for any data ecosystem where multiple parties need to collaborate in a common goal.

The complete Nevermined Provenance architecture can be found in the [Provenance Spec](architecture/specs/provenance/README.md#usage-used).

This module allows to register Provenance events associated to assets. Also allows to retrieve all the assets provenance track previously registered.

## Registering Provenance

All the provenance events are registered on-chain via the Provenance contract. All the individual provenance events have to be associated to a `Provenance ID`. This ID is a unique identifier that can be used later on to retrieve information about a specific event.

### Registering provenance generation

`Generation` is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
Nevermined encapsulate every entity to be managed using `Decentralized Identifiers (DID)` that are registered via the `DIDRegistry` Smart Contract.
This contract registers automatically the provenance generation event when an asset is created. So this function is not exposed as part of the API, but is referenced here for clarity.

You can find more details of this in the [Provenance Specs](architecture/specs/provenance/#generation-register-a-new-entity-generated-by-an-agent-wasgeneratedby)

### Registering provenance derivation

`Derivation` is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.
This function allows to register a provenance derivation event when a new asset is created as a result of some other asset. The function parameters are:

* `provenanceId` the Provenance ID
* `newEntityDid` Identifier of the new asset derived as a result of the activity
* `usedEntityDid` Identifier of the asset used for deriving a new asset as a result of the activity
* `agentId` Public address of the user/agent associated with the action
* `activityId` Identifier of the activity doing the derivation action
* `attributes` Optional attributes associated with the action

Example:

```java
wasDerivedFrom("999", "did:nv:1234", "did:nv:5678", 0xa1a1, "activity creating asset", "+ information")
```

You can find more details of this function in the [Provenance Specs](architecture/specs/provenance/#derivation-register-relationship-between-source-and-derived-entities-wasderivedfrom)


### Registering provenance utilization

`Usage` is the beginning of utilizing an entity by an activity. Before usage, the activity had not begun to utilize this entity and could not have been affected by the entity.
The function parameters are:

* `provenanceId` the Provenance ID
* `did` Identifier of the asset associated to the activity
* `agentId` Public address of the user/agent associated with the action
* `activityId` Identifier of the activity doing the usage action
* `attributes` Optional attributes associated with the action

Example:

```java
used("999", "did:nv:1234", 0xa1a1, "using activity", "additional information")
```

You can find more details of this function in the [Provenance Specs](architecture/specs/provenance/#usage-used)


### Registering provenance association

`Association` is an assignment of responsibility to an agent for an activity, indicating that the agent had a role in the activity.
This function allows to register a provenance association event to an asset. The function parameters are:

* `provenanceId` the Provenance ID
* `did` Identifier of the asset associated to the activity
* `agentId` Public address of the user/agent associated with the action
* `activityId` Identifier of the activity doing the association action
* `attributes` Optional attributes associated with the action

Example:

```java
wasAssociatedWith("999", "did:nv:1234", "ac1", "additional information")
```

You can find more details of this function in the [Provenance Specs](architecture/specs/provenance/#association-wasassociatedwith)


### Registering provenance delegation

`Delegation` is the assignment of authority and responsibility to an agent (by itself or by another agent) to carry out a specific activity as a delegate or representative, while the agent it acts on behalf of retains some responsibility for the outcome of the delegated work.
The function parameters are:

* `provenanceId` the Provenance ID
* `did` Identifier of the asset associated to the activity
* `delegateAgentId` Public address of the user/agent delegated by the `responsibleAgentId`
* `responsibleAgentId` Public address of the user/agent responsible of the `did`
* `activityId` Identifier of the activity doing the association action
* `signature` Signature of the `provenanceId` provided by the `delegatedAgentId`. This will work as proof of agreement between the delegate and the responsible about a specific provenance action.
* `attributes` Optional attributes associated with the action

Example:

```java
actedOnBehalf("999", "did:nv:1234", 0xa1a1, 0xb2b2, "ac1", "s1gnatureeeee", "additional information")
```

You can find more details of this function in the [Provenance Specs](architecture/specs/provenance/#delegation-actedonbehalfof)


## Retrieving Provenance information

### Search Provenance events related to an asset

When a new provenance event is recorded on-chain, an event is emitted including some information.
This function searches across all the `ProvenanceAttributeRegistered` events related with a specific DID. Parameters:

* `did` Identifier of the asset we are looking to search provenance events

Example:

```java
getDIDProvenanceEvents("did:nv:1234")
```

### Search Provenance events related to an asset

When a new provenance event is recorded on-chain, an event is emitted including some information.
This function searches for specific provenance events methods (`used`, `wasGeneratedBy`, etc.) given a DID. Parameters:

* `method` - Reference to the W3C Provenance method event we are going to search. This parameter is an `unsigned int` from `0` to `15`. See more here in the [Smart Contract implementation](https://github.com/nevermined-io/contracts/blob/master/contracts/registry/ProvenanceRegistry.sol#L58).
* `did` Identifier of the asset we are looking to search provenance events

Example:

```java
getProvenanceMethodEvents(0, "did:nv:1234")
```

### Get Provenance Entry

Get from the on-chain Provenance registry the information about one provenance event, given a provenance id.
Parameters:

* `provenanceId` Provenance Identifier

Example:

```java
getProvenanceEntry("049320943")
```

### Get Provenance Owner

Get from the on-chain Provenance registry the information about who create the provenance entry given a provenance id.
Parameters:

* `provenanceId` Provenance Identifier

Example:

```java
getProvenanceOwner("049320943")
```



## Managing Provenance Delegates

The provenance delegates are accounts that have the ability to register provenance events associated to an asset/entity (Decentralized Identifier - DID) on behalf of the owner.
This is helpful in some situations where a user creates a new asset, and later can delegate to a third party to make some actions on an asset and in extension to register provenance events associated to that.
The following functions describe how to manage the delegates regarding to DIDs.

### Add a provenance delegate to a DID

It associates a new user as a delegate to an existing DID. Parameters:

* `did` Identifier of the asset where the delegate will be added
* `delegatedAccount` Public address of the user associated as delegate to the `did`

Example:

```java
addDIDProvenanceDelegate("did:nv:1234", 0x1234)
```


### Remove a provenance delegate from a DID

It removes an existing delegate of a DID. Parameters:

* `did` Identifier of the asset where the delegate will be removed
* `delegatedAccount` Public address of the user to remove as delegate to the `did`

Example:

```java
removeDIDProvenanceDelegate("did:nv:1234", 0x1234)
```


### Is an user a provenance delegate?

Returns true or false if the user account provided is an existing delegate for an existing DID. Parameters:

* `did` Identifier of the asset
* `delegatedAccount` Public address of the user

Example:

```java
isProvenanceDelegate("did:nv:1234", 0x1234)
```
