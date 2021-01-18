# Nevermined API Reference

```
shortname: nevermined-api-spec
version: 1.0
status: Draft
date: December 2020
```

The goal of this doc is to help a developer build a version of the Nevermined API in any programming language.
Currently, the Nevermined API is defined for Object-Oriented languages such as JavaScript, Java, and Python (which are the three initial implementation languages).

## Modules

The SDKs are organized using the following modules:

* [Assets](Assets.md) - Managing of data assets on Nevermined networks
* [Accounts](Accounts.md) - Managing accounts
* [Agreements](Agreements.md) - Interacting with Service Exection Agreements
* [Conditions](Conditions.md) - Interacting with agreement conditions
* [Provenance](Provenance.md) - Tracking & retrieving data provenance
* [Tokens](Tokens.md) - Request and transfer Nevermined tokens
* [Providers](Providers.md) - Manage of asset providers
* [Secret Store](Secret-Store.md) - Encryption and Decryption secrets

### Assets

Exposes the API related with assets interaction (create, resolve, search, order, download, execute, etc.)

### Accounts

It allows to fetch information about Ethereum accounts and tokens balance

### Agreements

It allows to manage Service Execution Agreements and check their status

### Conditions

It allows to interact with the Smart Contracts related with Agreement Conditions
