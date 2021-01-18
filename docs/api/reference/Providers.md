# Providers API Reference

In Nevermined a data publisher can delegate to other users identified
 with their key material, to interact in their behalf.
 This is useful for users who don't want to run Nevermined infrastructure and delegate
 that to other entities.

This module allows to manage the providers that can interact with data publisher assets.

## Add a new provider to an asset

Allows to associate a new provider to an existing asset. Parameters:

* `did` the id of the document where we are gonna associate the provider
* `providerAddress` the public address of the provider
* `account` the public address of the account executing this action

Example:

```java
add("did:nv:1234", 0xaabb, 0xccdd)
```

## Remove a provider of an asset

Allows to de-associate a provider of an asset. Parameters:

* `did` the id of the document where we are gonna de-associate the provider
* `providerAddress` the public address of the provider
* `account` the public address of the account executing this action

Example:

```java
remove("did:nv:1234", 0xaabb, 0xccdd)
```


## List the providers associated to an asset

Returns a list with the public addresses of the providers associated to an asset . Parameters:

* `did` the id of the document

Example:

```java
list("did:nv:1234")
```
