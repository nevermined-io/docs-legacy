# MKT-API SPEC: Nevermined Marketplace API

```
shortname:      MKT-API
name:           Nevermined Marketplace API
type:           Standard
status:         Draft
version:        0.2
editor:         Aitor Argomaniz <aitor@nevermined.io>
contributors:   
```

Table of Contents
=================

* [MKT-API SPEC: Nevermined Marketplace API](#mkt-api-spec-nevermined-marketplace-api)
* [Table of Contents](#table-of-contents)
   * [Motivation](#motivation)
   * [Architecture](#architecture)
   * [Modules](#modules)
      * [Assets Management](#assets-management)
      * [Assets Search](#assets-search)
      * [Users Profiles](#users-profiles)
      * [Permissions](#permissions)
      * [Secondary Market](#secondary-market)
      * [NFTs Metadata](#nfts-metadata)
      * [User Generated Contents](#user-generated-contents)
      * [NFTs Drops](#nfts-drops)
      * [Bookmarks](#bookmarks)
      * [Marketplace Management](#marketplace-management)
      * [Multimedia](#multimedia)
      * [API Access Control](#api-access-control)
         * [Authentication](#authentication)
         * [Authorization](#authorization)
      * [Storage](#storage)
   * [Links](#links)


---

This SPEC introduces a new API that helps to build Marketplace environments on top of the Nevermined core protocol.

## Motivation

With this Specification we want to build the foundations of an API that can be used as reference to implement 
APIs exposing typical Marketplace functionalities.

Most of the Marketplaces (decentralized or not) expose some common functionalities around the assets they manage and 
their users. The intention of this API is to normalize a common set of this functionalities, allowing to build 
implementations providing this common functionalities.

With that objective in mind, the specification of this API should detail the following capabilities:

* Assets Management - Creation, Update, Deleting, etc. This is based in the existing [Metadata Spec](../metadata/README.md)
* Assets Search - Allowing the search and filtering of assets
* Users Profile - Allowing to create, update and delete users
* Secondary Market - Registering the negotiation of parties during a secondary market purchase
* NFTs Metadata - Recording the metadata associated to a NFT
* NFTs Drops - Management of NFT drops
* User Reviews - Allowing users to comment and rate marketplace contents
* Bookmarks - Allowing users to save bookmarks about different assets


## Architecture

## Modules

The API will provide the following functionalities.

### Assets Management

The Assets in a Nevermined ecosystem are represented via DDOs that are resolved via a Decentralized Identifier (DID). While the DIDs are 
unique identifiers stored on-chain, the metadata of an asset is represented by a DDO recorded in an external data storage (centralized or decentralized).
This DDO includes all the additional information describing an asset and the services attached to that asset (access, computation, etc.).

This module of the API allows the management of the assets information. The main functionalities provided are the following:

* Create a DDO of a new asset - `POST /api/v1/metadata/assets/ddo`
* Get the DDO of a particular asset - `GET /api/v1/metadata/assets/ddo/{did}`
* Update DDO of an existing asset - `PUT ​/api​/v1​/metadata​/assets​/ddo​/{did}`
* Delete an existing asset - `DELETE ​/api​/v1​/metadata​/assets​/ddo​/{did}`

The Creation, Update and Deletion of assets is authorized and **only the asset owner and/or the application admin** is allowed to do that action.

For more information about DID and/or DDO's please refer to the [DID SPEC: Decentralized Identifiers](../did/README.md) and 
[META SPEC: Metadata Ontology](../metadata/README.md).

### Assets Search

This module complements the previous one and provides search functionalities on top of the existing assets metadata. All the actions listed
here don't require user authorization:

* Get all asset IDs - `GET ​/api​/v1​/metadata​/assets`
* Get DDO of all assets - `GET ​/api​/v1​/metadata​/assets​/ddo`
* Get a list of DDOs that match with the given text - `GET ​/api​/v1​/metadata​/assets​/ddo​/query`
* Get a list of DDOs that match with the executed query - `POST ​/api​/v1​/metadata​/assets​/ddo​/query`


### Users Profiles

This module of the API allows the management of user profiles. The main functionalities provided are the following:

* Create a user profile - `POST /api/v1/metadata/profiles`
* Get the metadata of a user profile - `GET /api/v1/metadata/profiles/{userId}`
* Get the metadata of a user profile given an address - `GET /api/v1/metadata/profiles/address/{publicAddress}`
* Update the user profile - `PUT /api/v1/metadata/profiles/{userId}`
* Disable the user profile - `DELETE /api/v1/metadata/profiles/{userId}`

The Creation, Update and Deletion of profiles is authorized and **only the profile owner and/or the application admin** is allowed to do that action.

The model of this API is the following:

* `userId` - Unique identifier of the user
* `isListed` - Flag identifying if the user is listed in the marketplace. Possible values: `true` or `false`
* `state` - State of the user in the marketplace. Possible options: `disabled`, `unconfirmed`, `confirmed`
* `addresses` - The list of the addressed owned by the user. Addresses can't be shared between different users.
* `nickname` - The nickname of the user
* `name` - The name of the user (optional)
* `email` - The email of the user (optional)
* `url` - The url of the user (optional)
* `creationDate` - When the user information was created
* `updateDate` - When was the last time the user information was updated
* `additionalInformation` - List of additional key-value attributes with additional information

Here an example of the the permissions document:

```json
{
    "userId": "jifdwqejidqwa9okdasodkaso",
    "isListed": true,
    "state": "confirmed",
    "addresses": ["0x37BB53e3d293494DE59fBe1FF78500423dcFd43B"],
    "nickname": "john.doe",
    "name": "John Doe",
    "email": "john.doe@example.com",    
    "creationDate": "2019-01-01T19:73:24Z",
    "updateDate": "2019-01-01T19:73:24Z",
    "additionalInformation": {
        "profilePicture": "http://example.com/avatar.jpg",
        "linkedinProfile": "http://linkedin.com"
    }
}
```


### Permissions

This module of the API allows the management of user permissions in the marketplace via the usage of verifiable credentials. 
The main functionalities provided are the following:

* Create a permissions entry - `POST /api/v1/permissions`
* Get the information about a permissions entry - `GET /api/v1/permissions/{permissionId}`
* Get all the permissions of a user - `GET /api/v1/permissions/user/{userId}`
* Get all the permissions of a user of a specific type - `GET /api/v1/permissions/user/{userId}/{type}`
* Update the permissions entry - `PUT /api/v1/permissions/{permissionId}`
* Disable a permissions entry - `DELETE /api/v1/permissions/{permissionId}`

The Creation, Read, Update and Deletion of permissions is authorized and **only the application admin** is allowed to do that action.

The model of this API is the following:

* `id` - Unique identifier for the permissions entry
* `userId` - Unique identifier of the user
* `type` - The list of permissions owned hold by the user
* `issuer` - The account providing the permissions
* `holder` - The public address holding the permissions
* `issuanceDate` - When the permissions entry was created

Here an example of the the permissions document:

```json
{
    "permissionId": "98it403-295-43954-3s",
    "userId": "jifdwqejidqwa9okdasodkaso",
    "type": ["read", "update", "delete"],
    "issuer": "0x610D9314EDF2ced7681BA1633C33fdb8cF365a12",
    "holder": "0x37BB53e3d293494DE59fBe1FF78500423dcFd43B",
    "issuanceDate": "2019-01-01T19:73:24Z"   
}
```

For example when we want to provide a whitelisting functionality allowing to `mint` only to certain users, a specific `type` attribute could be created
in the user who will hold the minting permissions. Having that a client application could check if a specific user has `mint` permissions running the following query:

```
HTTP GET /api/v1/permissions/user/jifdwqejidqwa9okdasodkaso/mint
```

### Secondary Market

This module of the API allows the management of the Secondary Market transactions. The main functionalities provided are the following:

* Publish an asset in the secondary market - `POST /api/v1/agreement/secondary-market`
* Get details of an asset in the secondary market - `GET /api/v1/agreement/secondary-market/{id}`
* Update the details of an asset in the secondary market - `PUT /api/v1/agreement/secondary-market/{id}`
* Unpublish an asset in the secondary market - `DELETE /api/v1/agreement/secondary-market/{id}`
* Get a list of secondary market assets that match with the executed query - `POST ​/api​/v1​/agreement/secondary-market​/query`

The Creation, Update and Deletion of assets in the secondary market is authorized and **only the asset owner or the application admin** is allowed to do that action.

The model of this API is the following:

* `id` - Unique identifier for the entry
* `serviceAgreementId` - Service Agreement Id
* `did` - The identifier of the asset
* `seller` - The account selling the asset
* `buyer` - The account buying the asset
* `createdAt` - When the entry was published in the secondary market
* `price` - The price amount of the price in the secondary market
* `tokenAddress` - The token (Native or ERC20) used
* `dynamicPricingAddress` - Contract address if the pricing is defined as dynamic (auctions, etc). If is `0x0` the price is fixed and uses the `price` attribute



### NFTs Metadata

This module of the API allows the creation of metadata attached to a NFT. The main functionalities provided are the following:

* Create NFT Metadata of a new asset - `POST /api/v1/metadata/nft`
* Get the NFT Metadata of an asset - `GET /api/v1/metadata/nft/{did}`
* Update NFT Metadata of an asset - `PUT ​/api/v1/metadata/nft/{did}`
* Delete NFT Metadata - `DELETE ​/api/v1/metadata/nft/{did}`

The Marketplace API could use regular or inmutable storage for recording the NFT Metadata. If the storage is inmutable (IPFS, Filecoin, etc), the Update and Delete methods
will return a `HTTP 501 Not Implemented` error message will be returned.

The Creation, Update and Deletion of NFTs Metadata is authorized and **only the asset owner** is allowed to do that action.

The model of this API is the following:

* `did` - The identifier of the asset
* `image` - The URL to the image associated to the NFT
* `name` - Name of the asset
* `description` - Description of the asset
* `external_url` - URL to the asset in a Nevermined ecosystem
* `animation_url` - A URL to a multi-media attachment for the item
* `youtube_url` - A URL to a YouTube video
* `seller_fee_basis_points` - Royalties for selling the NFT through a marketplace out of Nevermined (i.e OpenSea)
* `fee_recipient` - Address of the user receiving the royalties


### User Generated Contents

This module of the API allows the management of User Generated Contents (UGC) like user reviews. The main functionalities provided are the following:

* Create a user review - `POST /api/v1/ugc/reviews`
* Get a user review - `GET /api/v1/ugc/reviews/{ugcId}`
* Get all the reviews associated to an asset - `GET /api/v1/ugc/asset/{did}`
* Update a review - `PUT /api/v1/ugc/reviews/{ugcId}`
* Unpublish a review - `DELETE /api/v1/ugc/reviews/{ugcId}`

The Creation, Update and Deletion of reviews is authorized and **only the review owner and/or the application admin** is allowed to do that action.

The model of this API is the following:

* `ugcId` - The identifier of the asset
* `did` - The identifier of the asset
* `owner` - The userId who created the review/rating
* `status` - Status of the UGC. Possible values: "publised", "unpublished", "deleted", "retired"
* `title` - Title of the comment
* `description` - Description given by the user
* `rate` - Number indicating the rating (flexible dependening to the marketplace). Examples: number between 1 and 5, 1 and 10, 0 and 100, etc.
* `createdAt` - When the UGC was created
* `updatedAt` - When the UGC was udpated
* `moderatedBy` - If the content was moderated, who applied that moderation

By default, only UGC reviews with the state set to "published" should be displayed/


### NFTs Drops

This module of the API allows the creation of metadata associated to NFT drops. Drops are an important event in NFT marketplaces where admins AND/OR whitelisted authors
can identify which NFTs are gonna be minted and when. The main functionalities provided are the following:

* Register a new NFT drop (admin or whitelisted author) - `POST /api/v1/metadata/drops`
* Search for listed drops - `GET /api/v1/metadata/drops`
* Get information about a drop - `GET /api/v1/metadata/drop/{did}`
* Update drop information - `PUT ​/api/v1/metadata/drop/{did}`
* Unlist a drop - `DELETE ​/api/v1/metadata/drop/{did}`

The Creation, Update and Deletion of a NFT Drop is authorized and **only the asset owner and/or the application admin** is allowed to do that action.



### Bookmarks

This module of the API allows users to bookmark marketplace contents. The main functionalities provided are the following:

* Create a bookmark entry - `POST /api/v1/ugc/bookmarks`
* Get a bookmark entry - `GET /api/v1/ugc/bookmarks/{bookmarkId}`
* Get all the user bookmarks - `GET /api/v1/ugc/bookmarks/{userId}`
* Update an existing bookmark - `PUT /api/v1/ugc/bookmarks/{bookmarkId}`
* Delete a bookmark - `DELETE /api/v1/ugc/bookmarks/{bookmarkId}`

The Creation, Update and Deletion of bookmarks is authorized and **only the bookmark owner** is allowed to do that action.

### Marketplace Management 

* Unpublish multiple assets
* Disable a user
* Disable user comments

### Multimedia

* URL Check - `GET /api/v1/files/check`
* Upload image - `POST /api/v1/files/image`
* Upload audio - `POST /api/v1/files/audio`

![Marketplace API Data Model](images/marketplace_api_data_model.png)

### API Access Control


The API will expose a `HTTP REST` interface using Json Web Tokens (JWT) for users authorization and authentication.

The API will use the following `JWT` attributes:

* Issuer (`iss`): the user address. For example: `0xa99d43d86a0758d5632313b8fa3972b6088a21bb`
* Subject (`sub`): the user address or the address of a delegate. For example: `0xa99d43d86a0758d5632313b8fa3972b6088a21bb`
* Issued at (`iat`): the date time of when the JWT token was issued
* Expiration (`exp`): the expiration date time of the JWT token

The API will define a TTL of a maximum of one hour duration.


#### Authentication

The client of the API will need to authenticate using `login` method. This method will require the client to provide to authenticate
the user. When the user is authenticated, the API will release a JWT allowing the user to interact with the different API modules.

![Marketplace API Access Control Flow](images/marketplace_api_access_control_flow.png)

The flow is the following:

1. The client sends a `HTTP GET /login` request providing the user address. Example:
```
HTTP GET /api/v1/docs/auth/login/0xa99d43d86a0758d5632313b8fa3972b6088a21bb
```

2. The server will return a unique challenge token to the user

3. The client will sign locally this challenge token using the local key material

4. The client will send a `HTTP POST /login` request providing the user address and the challenge token signed
```
HTTP POST /api/v1/docs/auth/login
address=0xa99d43d86a0758d5632313b8fa3972b6088a21bb
signature=90f8bf6a479f320ead074411a4b0e7944ea8c9c15932c5d68a1b539da0b0f8431d8e50e1a5b2b3bd4cfdcfc387a5ff85d7ef5fac429c4e0e4c1bfc36d4a99770b58f42924e126ece
```

5. If the server can authenticate the user, it will return a JWT token
```
  {
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzUxMiJ9.eyJzdWIiOiIweDkwZjhiZjZhNDc5ZjMyMGVhZDA3NDQxMWE0YjBlNzk0NGVhOGM5YzEiLCJleHAiOjE0OTY1MDUwNzQsIm5iZiI6MTQ5NjUwMzI3NCwiaXNzIjoiTmV1ZnVuZCIsImF1ZCI6IndlYjMiLCJpYXQiOjE0OTY1MDMyNzR9.AaOPxTqBV4iy6GVlAu8XfbmOsIoezKfYjkqZ0SZ_RW6E7qwW-tUwSq8fq-avJrLtmCzLOD2xO9T5esEiIykP3Z9SAKWrTkdo9RwGcqGfvAySurbVAiFgW4MZ9pf9cHcB6zRks53pPcq6X2yqaVzjw28N6kBRQRc23GrUFnEDK6P_t3Tv"
  }
```

6. The user should be able to renew the authentication token passing the `Authorization` header to the `/renew` method:
```
HTTP POST /api/v1/docs/auth/renew
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzUxMiJ9.eyJzdWIiOiIweDkwZjhiZjZhNDc5ZjMyMGVhZDA3NDQxMWE0YjBlNzk0NGVhOGM5YzEiLCJleHAiOjE0OTY1MDUwNzQsIm5iZiI6MTQ5NjUwMzI3NCwiaXNzIjoiTmV1ZnVuZCIsImF1ZCI6IndlYjMiLCJpYXQiOjE0OTY1MDMyNzR9.AaOPxTqBV4iy6GVlAu8XfbmOsIoezKfYjkqZ0SZ_RW6E7qwW-tUwSq8fq-avJrLtmCzLOD2xO9T5esEiIykP3Z9SAKWrTkdo9RwGcqGfvAySurbVAiFgW4MZ9pf9cHcB6zRks53pPcq6X2yqaVzjw28N6kBRQRc23GrUFnEDK6P_t3Tv
```


#### Authorization

Once the user is authenticated, the API will be able to authorize or not the user to perform different actions. Every document in the system has a 
reference to the original public address owning the document. Depending on the module, actions like updating or deleting will require different permissions.

All the documents stored into the database will have a `verifiableCredential` entry witht the `holder` attribute attached to the document. 
This attribute will allow to validate the owner of the metadata object and perform any authorization action.

For general permissions, the `Permissions` module will track what actions (described under the `type` attribute) are managed by each user.

The `admin` permissions can be added and are reserved for users with administrative permissions in the application.

### Storage

The storage of the data can use a standard database and/or an inmutable respository (IPFS, Filecoin, Arweave, ..) as a complement.

Different storage backends provide a different set of functionalities to the final user. From one side, regular or standard databases provide 
easy searching functionalities. In the other side, inmutable storage provide a level of trust on things like the assets metadata.

The usage of different storage backends or a combination of both will depend on the use case and/or the Marketplace API configuration.

All the documents stored in a regular database or search engine (like Elastic Search) will record the metadata in their current models are they are.
In the case this document has a mirror copy into a inmutable data store (like IPFS), the document will include a reference to 
this inmutable content via a full URL. This typically will be stored into the `proof.inmutableUrl` attribute.

For example if an Asset DDO has a copy into IPFS, it will include an attribute like this:

```json
"proof": {
    "type": "DDOIntegritySignature",
    "created": "2016-02-08T16:02:20Z",
    "creator": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
    "signatureValue": "0xc9eeb2b8106e…6abfdc5d1192641b",
    "inmutableUrl": "ipfs://QmPChd2hVbrJ6bfo3WBcTW4iZnpHm8TEzWkLHmLpXhF68A",
    "checksum": {
        "0": "0x52b5c93b82dd9e7ecc3d9fdf4755f7f69a54484941897dc517b4adfe3bbc3377",
        "1": "0x999999952b5c93b82dd9e7ecc3d9fdf4755f7f69a54484941897dc517b4adfe3"
    }    
}
```



## Links

* [Decentralized Identifiers SPEC](../did/README.md)
* [Metadata SPEC](../metadata/README.md)

