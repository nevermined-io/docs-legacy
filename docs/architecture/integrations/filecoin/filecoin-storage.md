# Integration of Filecoin as decentralized storage for Nevermined users

```
shortname:      FIL-STO
name:           Filecoin Storage Integration
type:           Standard
status:         Draft
version:        0.1
```




---


[Nevermined](https://nevermined.io/) is an Open Source solution developed by [Keyko](https://keyko.io/), offering the users the ability to build data sharing ecosystems where untrusted parties can share and monetize their data in a way that’s efficient, secure and privacy preserving. As data creation continues to proliferate, entities have the necessity of organising, understanding, using and sharing their data internally and externally. Nevermined provides Data Sharing and Data In-Situ Computation solutions that allow organizations to unlock data for a more insights-driven approach.

What we call a Data Ecosystem is an environment where independent organizations can cooperate with each other to publish, discover, and access data and the associated assets and services. Nevermined enables the usage of data without the members of these ecosystems having to lose control of their assets. One of the main principles of Nevermined is that Data Owners and Providers always keep control of their data. The solution is designed to be integrated with existing Big Data environments and allows for the execution of models or algorithms in-situ, or where the data resides. With Nevermined, the data never moves; instead the algorithms and models move to where the data sits.

Currently Nevermined integrated with the most popular centralized/cloud based storage providers (Amazon S3, Azure, etc.). This document details the integration of Nevermined with Filecoin allowing to:

- Use Filecoin as one of the options supported allowing Nevermined users to publish & share their data via Filecoin
- Facilitate access control & data monetization of Filecoin existing data
- Enable a decentralized storage solution where users don't need to upload their data to any existing centralized solution


![Nevermined & Filecoin High Level integration](images/integration-high-level.png)

## Value

The integration of Filecoin into Nevermined brings is valuable for Filecoin community because:

- Increase the usage of Filecoin network
- Provides utility to Filecoin network via integration with existing and mature Open Source software
- Filecoin doesn't provide a granular access control allowing the data owners or publishers to decided when, and from whom their data can be accessed
- Allows user using centralized data storage based on cloud providers to use Filecoin as alternative
- Nevermined is L2 solution, network independent, and can be deployed in public or private networks. Via this integration, Filecoin could be used in any Nevermined user deployment
- Nevermined provides compute to the data and provenance (based on W3C PROV) capabilities. Via the integration, the Filecoin community would be able to use high value capabilities on top of their data

## Integration Details

The integration of Filecoin as a fully supported storage provider require the modification and delivery of the following components:

* The [Nevermined Gateway](https://github.com/nevermined-io/gateway). This component is in charge of making available Nevermined users data. Before this integration the gateway supports different storage providers (Amazon S3, Azure, On Premise, etc.). This integration adds support to Filecoin as storage mechanism allowing to decrypt user urls and resolve Filecoin CIDs.
* The Nevermined SDKs. To facilitate user adoption, Nevermined support SDKs in 3 different programming languages:
  - [Javascript SDK](https://github.com/nevermined-io/sdk-js), to facilitate the integration of Nevermined in web interfaces and DApps
  - [Python SDK](https://github.com/nevermined-io/sdk-py), to facilitate the integration of Nevermined in data science tools
  It will deliver a modification of the 3 SDKs allowing to the users to publish in Nevermined Filecoin contents (CIDs)  
  - [Java SDK](https://github.com/nevermined-io/sdk-java), to facilitate the integration of Nevermined with existing industry big data solutions.
* [Marketplace](https://github.com/nevermined-io/marketplace). It's a frontend application where users can publish and share files. The intention is to modify this application to support data sharing of assets stored in the Filecoin network.

### User Flows

The final goal is to have a fully functional end to end integration, allowing for the registering of existing Filecoin assets into the Nevermined network:

![Registering of Filecoin assets into Nevermined](images/nvm-integration-publishing-flow.png)

After this publishing flow, it's intended to provide the downloading functionality (after access control) of Filecoin contents registered in the Nevermined network:

![Data Access of Filecoin assets existing into Nevermined](images/nvm-integration-downloading-flow.png)


### Architecture

The Nevermined architecture is evolved to integrate [Powergate](https://docs.filecoin.io/build/powergate/) as gateway for supporting Filecoin data store. That integration requires the following modifications:

#### SDKs

- The publishing flow of Nevermined assets allows to include CIDs as files
- The consumption flow of Nevermined assets integrates the gateway and work with assets including Filecoin files

The SDK will include in the Metadata files attribute a URL using the `cid` prefix. Example:

```json
"files": [
  {
    "url": "cid://QmW68jbcqSRtqSQb6xkukQ6tfonZGhu1VrZv9zAicNmovs",
    "index": 0,
    "checksum": "efb2c764274b745f5fc37f97c6b0e761",
    "contentLength": "4535431",
    "contentType": "text/csv",
    "encoding": "UTF-8",
    "compression": "zip"    
  }
]
```

In the case of a Filecoin asset, the CID included in the url field of the DDO can include the following information:

* CID Hash - Identifier of the content in the Filecoin network
* Powergate host - Hostname of the powergate node that can be used to fetch the file
* Powergate port - Port where is running the powergate service that can be used to fetch the file
* Powergate token - Token to use to fetch the file
* Deal Id - Identifier of the Deal that allow to pin the file to IPFS

Here some examples of Filecoin CIDs urls:

```text
cid://POWERGATE_TOKEN:DEAL_ID@POWERGATE_HOST:POWERGATE_PORT/CID_HASH
cid://POWERGATE_HOST:POWERGATE_PORT/CID_HASH
cid://POWERGATE_TOKEN:DEAL_ID@CID_HASH
cid://POWERGATE_TOKEN:@CID_HASH
cid://:DEAL_ID@CID_HASH
cid://CID_HASH
```

As in the regular [Nevermined Access flow](https://docs.nevermined.io/architecture/specs/access/) the URL will be encrypted for the client and decrypted during the consumption phase by the gateway.

See more about the [File Attributes](https://docs.nevermined.io/architecture/specs/metadata/#file-attributes) in the [Metadata Specs](https://docs.nevermined.io/architecture/specs/metadata/).


#### Gateway integration

- The Gateway supports the connectivity with the Filecoin network via Powergate. This behavior can be enabled/disabled from the Gateway via configuration.
- The Gateway support the usage of an existing Filecoin wallet.
- When a Nevermined asset is resolved and includes a CID, the gateway is capable of resolving that file and return it to the final user

The Filecoin connectivity is encapsulated in the [Filecoin Driver](https://github.com/nevermined-io/metadata-driver-filecoin).

#### Marketplace

- The visual publishing flow of Nevermined assets allow to include CIDs as files
- The consumption flow of Nevermined assets integrates the gateway and work with assets including Filecoin files
