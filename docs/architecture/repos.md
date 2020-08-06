# Repositories

The complete description of the [architecture components](architecture/components.md) & licenses can be found [here](architecture/components.md).

A brief summary of some of them:

* [SMART CONTRACTS](https://github.com/keyko-io/nevermined-contracts) - Solidity Smart Contracts providing the Service
  Agreements business logic.
* [GATEWAY](https://github.com/keyko-io/nevermined-gateway) - Microservice to be executed by PUBLISHERS. It exposes an
  HTTP REST API permitting access to PUBLISHER assets or additional services such as computation.
* [METADATA-API](https://github.com/keyko-io/nevermined-metadata) - Microservice to be executed by MARKETPLACES.
  Facilitates   creating, updating, deleting and searching the asset metadata registered by the PUBLISHERS.
  This metadata is included as part of a DDO (see [DID SPEC](specs/did/README.md) and
  [METADATA SPEC](specs/metadata/README.md)) and also includes the services associated with the asset (consumption,
  computation, etc.).
* [SDK](sdk) - Software library encapsulating the Nevermined business logic. It's used to interact with all the
  components & APIs of the system. It's currently implemented in the following packages:
  - [nevermined-sdk-js](https://github.com/keyko-io/nevermined-sdk-js) - JavaScript version of the Nevermined SDK to be
    integrated with front-end applications.
  - [nevermined-sdk-py](https://github.com/keyko-io/nevermined-sdk-py) - Python version of the Nevermined SDK to be
    integrated with back-end applications. The primary users are data scientists.
  - [nevermined-sdk-java](https://github.com/keyko-io/nevermined-sdk-java) - Java version of the Nevermined SDK to be
    integrated with [JVM](https://en.wikipedia.org/wiki/Java_virtual_machine) applications. The primary users are
    data engineers.
* MARKETPLACE - Exposes a web interface allowing users to publish and purchase assets.
  It also facilitates the discovery of assets.
