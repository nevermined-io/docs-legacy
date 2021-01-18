# Nevermined APIs

Nevermined offers different capabilities built on top of some [technical components](../architecture/components.md).
Each of team play a different role and allow their integration in different ways.

## Software Development Kits (SDK's)

The main entry point for using Nevermined are the Software Development Kits (SDKs).
SDK's are the software libraries encapsulating the Nevermined business logic. They are used to interact with all the
components & APIs of the system.

Nevermined provides 3 different Open Source implementation of SDK's allowing the integration and implementation of
complex use cases on top of the Nevermined Data Ecosystems.

- [Nevermined SDK JS](https://github.com/nevermined-io/sdk-js) - JavaScript version of the Nevermined SDK to be
  integrated with front-end applications.
- [Nevermined SDK PY](https://github.com/nevermined-io/sdk-py) - Python version of the Nevermined SDK to be
  integrated with back-end applications. The primary users are data scientists.
- [Nevermined SDK JAVA](https://github.com/nevermined-io/sdk-java) - Java version of the Nevermined SDK to be
  integrated with [JVM](https://en.wikipedia.org/wiki/Java_virtual_machine) applications. The primary users are
  data engineers.

All the three implementations are very similar from a design and interface point of view.
It means that beyond the language differences, the concepts and the way the API is exposed from a user point of view
is the same.

If you want to know more, you can explore the [Nevermined Reference API](../api/reference/api-reference-latest.md) and it's
implementation in the [SDKs API documentation](../api/SDK.md).


## Metadata API

The [Nevermined Metadata API](https://github.com/nevermined-io/metadata)
is an Open Source micro-service that allows to store Assets metadata in an
off-chain repository. It provides a plugins system allowing to persist the
Metadata in ElasticSearch or MongoDB. The Metadata API exposes the functionality
 for searching metadata using multiple filters and parameters.

The Metadata API is typically the backend used for Data Marketplaces or Data
Catalogs for storing all the Metadata of a specific domain related to a
Marketplace or Catalog .

The Metadata API is wrapped by the SDKs, so you don't need to integrate directly this API.

## Gateway

The [Nevermined Gateway](https://github.com/nevermined-io/gateway) is an
Open Source micro-service in the Nevermined ecosystem. The Gateway is the
technical component executed by Data/Compute Providers allowing them to provide
extended data services (e.g. storage and compute). The Nevermined Gateway, as
part of the Publisher ecosystem, includes the credentials to interact with the
infrastructure (initially cloud, but could be on-premise).

The Gateway API is wrapped by the SDKs, so you don't need to integrate directly this API.
