# Nevermined Assets API

Every entity object in Nevermined is encapsulated in an **asset**. Typically the abstract things like datasets, algorithms, services, workflows, etc. But technically can abstract any entity with services provided by an user to the rest network under some conditions. Any asset has 2 main components:

- A Decentralized Identifier or DID. A unique id that reference the asset. This is recorded on-chain when the asset is registered in a Nevermined network
- Metadata. A DID Document describing the asset and the services (access, compute, etc.) associated to that asset. This is recorded off-chain.

An on-chain DID can be used to resolve the metadata associated to it.
You can find more information about the implementation of the SEAs and the services associated to Nevermined assets in the [access Spec](../architecture/specs/access/README.md) and the [compute Spec](../architecture/specs/compute/README.md).

## Assets Management

### Create an asset

It registers a new asset on Nevermined. It Creates a new DID, registering it on-chain through `DIDRegistry` contract and off-chain in Metadata.
Parameters:

* `metadata` the metadata describing the asset (full [metadata specification](../architecture/spec/metadata/README.md))
* `publisherAccount` Public address of the account publishing the asset
* `providers` List of public addresses that can act on behalf of the asset publisher, typically for providing some services like access associated to it
* `authorization` Type of encryption used to validate authorization (`PSK_RSA`, `PSK_ECDSA`, `SecretStore`)
* `activityId` Provenance identifier of the activity doing the creation action
* `attributes` Optional attributes associated with the provenance creation

Example:

```java
create("{ddo metadata}", 0xaabb, [0xccdd], "PSK_RSA", "creation", "+ attributes")
```


### Create a compute service

### Download assets

### Order an asset

### ownerDownload

### Execute

### Transfer asset ownership


## Fetch assets associated information

### Resolve a DID into a DDO


### Search for assets

### Get assets published by an account

### Get assets purchased by an account

### compute logs

### compute status





## Non-Fungible Tokens (NFTs) associated to assets

### Mint a NFT associated to an asset


### Burn NFTs associated to an asset

### Transfer NFTs associated to an asset

### Get NFTs balance associated to an asset
