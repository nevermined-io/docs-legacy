# Nevermined Assets API

Every entity object in Nevermined is encapsulated in an **asset**. Typically the abstract things like datasets, algorithms, services, workflows, etc. But technically can abstract any entity with services provided by an user to the rest network under some conditions. Any asset has 2 main components:

- A Decentralized Identifier or DID. A unique id that reference the asset. This is recorded on-chain when the asset is registered in a Nevermined network
- Metadata. A DID Document describing the asset and the services (access, compute, etc.) associated to that asset. This is recorded off-chain.

An on-chain DID can be used to resolve the metadata associated to it.
You can find more information about the implementation of the SEAs and the services associated to Nevermined assets in the [access Spec](../../architecture/specs/access/README.md) and the [compute Spec](../../architecture/specs/compute/README.md).

## Assets Management

### Create an asset

It registers a new asset on Nevermined. It Creates a new DID, registering it on-chain through `DIDRegistry` contract and off-chain in Metadata.
Parameters:

* `metadata` the metadata describing the asset (full [metadata specification](../../architecture/specs/metadata/README.md))
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

It registers a new asset on Nevermined with a [compute service](../../architecture/specs/compute/README.md) associated to it. This function creates a new DID, registering it on-chain through `DIDRegistry` contract and off-chain in Metadata.
Parameters:

* `metadata` the metadata describing the asset (full [metadata specification](../../architecture/specs/metadata/README.md))
* `publisherAccount` Public address of the account publishing the asset
* `providers` List of public addresses that can act on behalf of the asset publisher, typically for providing some services like access associated to it
* `authorization` Type of encryption used to validate authorization (`PSK_RSA`, `PSK_ECDSA`, `SecretStore`)
* `activityId` Provenance identifier of the activity doing the creation action
* `attributes` Optional attributes associated with the provenance creation

Example:

```java
createCompute("{ddo metadata}", 0xaabb, [0xccdd], "PSK_RSA", "creation", "+ attributes")
```


### Order an asset

This function orders an Asset represented by a DID. It implies to initialize a Service Agreement on-chain between publisher and consumer.
For lower level details you can take a look at [access Specs](../../architecture/specs/access/README.md).

As a result of an `order` the function will return an `agreementId`. This unique identifier about the Service Agreement just created can be used for further consumption of the access or compute service associated to it.

Parameters:

* `did` Identifier of the asset to order
* `index` The service index of the agreement in the DDO to order
* `consumerAccount` The Public address of the consumer account executing the order

Example:

```java
order("did:nv:1234", 0, 0xaabb)
```

### Download assets

This function downloads an Asset previously ordered (using the `order` function).

Parameters:

* `agreementId` Identifier of the service agreement between the consumer and the publisher
* `did` Identifier of the asset to download
* `index` The service index to the `access` service in the DDO to download
* `path` Destination folder where the asset files will be downloaded

Example:

```java
download("8594385934", "did:nv:1234", 0, 0xaabb, "/path/to/destination")
```

### Execute

This function executes a compute service of an Asset previously ordered (using the `order` function).

Parameters:

* `agreementId` Identifier of the service agreement between the consumer and the publisher
* `did` Identifier of the asset to execute
* `index` The service index to the `compute` service in the DDO to execute
* `workflowDid` Identifier of the compute workflow to execute

Example:

```java
execute("8594385934", "did:nv:1234", 0, 0xaabb, "did:nv:ccdd")
```


### Transfer asset ownership

It transfer the on-chain ownership of one asset from the original owner to a different account.

Parameters:

* `did` Identifier of the asset to execute
* `newAccountOwner` The Public address of account belonging to the new owner

Example:

```java
transferOwnership("did:nv:1234", 0xddee)
```


## Fetch assets associated information

This functions allow retrieve information related with assets. Assets information can be in two different places:

* On-chain. As part of the assets registry (`DIDRegistry`). There is stored the `did` and the url resolving to the `did document` or `ddo`.
* Off-chain. As part of marketplaces, the metadata api services keep all the metadata information (in `ddo` format)

### Resolve a DID into a DDO

A Nevermined network is composed by only one source of truth, the decentralized logic and storage provided by the blockchain and the Smart Contracts. A part of that, the network can be composed by many different marketplaces or metada repositories. This function resolves a `did` existing in the unique source of truth (blockchain) into the `ddo` (metadata) that can be stored in any of the multiple metadata servers existing in a Nevermined network deployment.

This function will return the metadata of an asset in DDO format. More information about the contents of this document can be found in the [metadata specification](../../architecture/specs/metadata/README.md) page.

Parameters:

* `did` Identifier of the asset to resolve in a DDO that is off-chain

Example:

```java
resolve("did:nv:1234")
```

### Search for assets

This function search in a metadata api instance  all the DDO that match the search criteria. This function will return a list of assets metadata matching the criteria.
Parameters:

* `text` the search query
* `sort` Key or list of keys to sort the result
* `offset` Number of records per page
* `page` Page showed

Example:

```java
search("weather in Berlin", "price", 0, 1)
```


### Get assets owned by an account

This function retrieves the list of assets owned by an account.
Parameters:

* `account` The Public address of account owning assets

Example:

```java
ownerAssets(0xaabb)
```


### Get assets purchased by an account

This function retrieves the list of assets purchased by an account.
Parameters:

* `account` The Public address of account that purchased the assets

Example:

```java
consumerAssets(0xaabb)
```


### Get the computation logs of a workflow execution

When a user triggers a compute execution via the `execute` function, this execution is scheduled and de-attached of the api method triggering it.
This function returns the logs generated during the execution of the multiple stages of a workflow in the data publisher infrastructure.
This function requires the `executionId` and `agreementId` for getting the logs. Parameters:

* `agreementId` Identifier of the service agreement between the consumer and the publisher
* `executionId` Identifier of the execution related with the agreement executed
* `account` The Public address of account used to execute the computation

Example:

```java
computeLogs("8974328", "ababacc", 0xaabb)
```


### compute status

When a user triggers a compute execution via the `execute` function, this execution is scheduled and de-attached of the api method triggering it.
This function returns status of the jobs executed in the data publisher infrastructure.
This function requires the `executionId` and `agreementId` for getting the logs. Parameters:

* `agreementId` Identifier of the service agreement between the consumer and the publisher
* `executionId` Identifier of the execution related with the agreement executed
* `account` The Public address of account used to execute the computation

Example:

```java
computeStatus("8974328", "ababacc", 0xaabb)
```


## Non-Fungible Tokens (NFTs) associated to assets

A Decentralized Identifier (DID) that digitally represents some physical stuff, aligns quite well with the concept of a Non-Fungible Token (NFT).
The implication is that, if you are an asset owner in Nevermined, you can mint NFTs associated with your DID and distribute them amongst your customers or users.

### Mint a NFT associated to an asset

This function allows to a DID owner to mint NFTs associated to the DID. Parameters:

* `did` Identifier of the asset where the NFTs will be minted
* `amount` the amount of NFTs to mint associated to the DID

Example:

```java
mint("did:nv:1234", 5)
```

### Burn NFTs associated to an asset

This function allows to burn existing NFTs associated to a DID. Parameters:

* `did` Identifier of the asset where the NFTs will be burned
* `amount` the amount of NFTs to burn associated to the DID

Example:

```java
burn("did:nv:1234", 1)
```


### Transfer NFTs associated to an asset

This function allows to transfer NFTs associated to a DID between accounts. Parameters:

* `did` Identifier of the asset where the NFTs will be burned
* `account` Public address of the account where the NFTs will be transferred
* `amount` the amount of NFTs to burn associated to the DID

Example:

```java
transfer("did:nv:1234", 0xabab, 2)
```

### Get NFTs balance associated to an asset

This function allows to get the NFTs balance of an account for a DID. Parameters:

* `account` Public address of the account
* `did` Identifier of the asset with NFTs associated

Example:

```java
balance(0xabab, "did:nv:1234")
```
