# Software Development Kits (SDKs)

The SDKs, independently of their programming language, allow the interaction
with the multiple Nevermined components. The SDKs integrate:

- The Nevermined Smart Contracts, where is kept all the assets registry, token, service execution agreements, etc.
- The Metadata API, where is kept the metadata associated to assets (title, description, tags, etc).
- The Gateway, that is the component that make data and computation available via the integration with data repositories and compute apis
- The Faucet, an optional component that allow users to request Ether for paying on-chain transactions
- The Secret Store, an optional component existing in some Nevermined deploments, it allows multi-party encryption and decryption of secrets

## Language Implementations

There are different language implementations of the SDKs:

- [Nevermined SDK JS](https://github.com/nevermined-io/sdk-js) - JavaScript version of the Nevermined SDK to be
  integrated with front-end applications.
- [Nevermined SDK PY](https://github.com/nevermined-io/sdk-py) - Python version of the Nevermined SDK to be
  integrated with back-end applications. The primary users are data scientists.
- [Nevermined SDK JAVA](https://github.com/nevermined-io/sdk-java) - Java version of the Nevermined SDK to be
  integrated with [JVM](https://en.wikipedia.org/wiki/Java_virtual_machine) applications. The primary users are
  data engineers.

## SDK Documentation

- [Nevermined SDK JS Documentation](https://github.com/nevermined-io/sdk-js) - Javascript documentation is included as part of the project repository.
- [Nevermined SDK PY Documentation](https://github.com/nevermined-io/sdk-py/tree/master/docs) - Python documentation is included as part of the project repository.
- [Nevermined SDK JAVA Documentation](https://javadoc.io/doc/io.keyko.nevermined/api/latest/index.html) - The Java documentation is
  generated automatically using `javadoc`. All the documentation can be found in [javadoc.io](https://javadoc.io/doc/io.keyko.nevermined/api/latest/index.html).

## API Reference

All the SDKs implement the same Nevermined reference API. This can be found in the [Nevermined Reference API Document](../api/reference/api-reference-latest.md).

### Modules

The SDK implement different the following modules:

Modules       | Topic             | API reference         | SDK Implementation
--------------|-------------------|-----------------------|---------------------------
[Assets](../api/reference/Assets.md)        | Managing of data assets on Nevermined networks | [Assets API reference](../api/reference/api-reference-latest.md#) | [Javascript]() | [Python]() | [Java]()
[Accounts](../api/reference/Accounts.md)        | Managing accounts | [Accounts API reference](../api/reference/api-reference-latest.md#) | [Javascript]() | [Python]() | [Java]()
[Agreements](../api/reference/Agreements.md)        | Interacting with Service Exection Agreements | [Agreements API reference](../api/reference/api-reference-latest.md#) | [Javascript]() | [Python]() | [Java]()
[Conditions](../api/reference/Conditions.md)        | Interacting with agreement conditions | [Conditions API reference](../api/reference/api-reference-latest.md#) | [Javascript]() | [Python]() | [Java]()
[Provenance](../api/reference/Provenance.md)        | Tracking & retrieving data provenance | [Provenance API reference](../api/reference/api-reference-latest.md#) | [Javascript]() | [Python]() | [Java]()
[Tokens](../api/reference/Tokens.md)        |Request and transfer Nevermined tokens | [Tokens API reference](../api/reference/api-reference-latest.md#) | [Javascript]() | [Python]() | [Java]()
[Providers](../api/reference/Providers.md)        | Manage of asset providers | [Providers API reference](../api/reference/api-reference-latest.md#) | [Javascript]() | [Python]() | [Java]()
[Secret Store](../api/reference/Secret-Store.md)        | Encryption and Decryption secrets | [Secret Store API reference](../api/reference/api-reference-latest.md#) | [Javascript]() | [Python]() | [Java]()
