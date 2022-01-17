# MKT-API SPEC: Nevermined Marketplace API

```
shortname:      MKT-API
name:           Nevermined Marketplace API
type:           Standard
status:         Draft
version:        0.1
editor:         Aitor Argomaniz <aitor@nevermined.io>
contributors:   
```

Table of Contents
=================




---

This SPEC introduces a new API that helps to build Marketplace environments on top of the Nevermined core protocol.

## Motivation

With this Specification we want to build the foundations of an API that can be used as reference to implement 
APIs exposing typical Marketplace functionalities.

Most of the Marketplaces (decentralized or not) expose some common functionalities around the assets the manage and 
their users. The intention of this API is to normalize a common set of this functionalities, allowing to build 
implementations providing this common functionalities.

With that objective in mind, the specification of this API should detail the following capabilities:

* Assets Management - Creation, Update, Deleting, etc. This is based in the existing [Metadata Spec](../metadata/README.md)
* Assets Search - Allowing the search and filtering of assets
* Users Profile - Allowing to create, update and delete users
* Secondary Market - Registering the negotiation of parties during a secondary market purchase
* NFTs Metadata - Recording the metadata associated to a NFT 
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
* Update the user profile - `PUT /api/v1/metadata/profiles/{userId}`
* Disable the user profile - `DELETE /api/v1/metadata/profiles/{userId}`

The Creation, Update and Deletion of profiles is authorized and **only the asset owner and/or the application admin** is allowed to do that action.


### Secondary Market

This module of the API allows the management of the Secondary Market transactions. The main functionalities provided are the following:

* Create a service agreement entry - `POST /api/v1/agreement/services`
* Get the a service agreement entry - `GET /api/v1/agreement/services/{serviceId}`
* Update a service agreement entry - `PUT /api/v1/agreement/services/{serviceId}`
* Disable a service agreement entry - `DELETE /api/v1/agreement/services/{serviceId}`

The Creation, Update and Deletion of service agreeemnts is authorized and **only the asset owner** is allowed to do that action.

### NFTs Metadata

This module of the API allows the creation of metadata attached to a NFT. The main functionalities provided are the following:

* Create NFT Metadata of a new asset - `POST /api/v1/metadata/nft`
* Get the NFT Metadata of an asset - `GET /api/v1/metadata/nft/{did}`
* Update NFT Metadata of an asset - `PUT ​/api/v1/metadata/nft/{did}`
* Delete NFT Metadata - `DELETE ​/api/v1/metadata/nft/{did}`

The Creation, Update and Deletion of NFTs Metadata is authorized and **only the asset owner** is allowed to do that action.


### User Reviews

This module of the API allows the management of User Generated Contents (UGC) like user reviews. The main functionalities provided are the following:

* Create a user review - `POST /api/v1/ugc/reviews`
* Get a user review - `GET /api/v1/ugc/reviews/{reviewId}`
* Get all the reviews associated to an asset - `GET /api/v1/ugc/asset/{did}`
* Update a review - `PUT /api/v1/ugc/reviews/{reviewId}`
* Unpublish a review - `DELETE /api/v1/ugc/reviews/{reviewId}`

The Creation, Update and Deletion of reviews is authorized and **only the review owner and/or the application admin** is allowed to do that action.

### Bookmarks

This module of the API allows users to bookmark marketplace contents. The main functionalities provided are the following:

* Create a bookmark entry - `POST /api/v1/ugc/bookmarks`
* Get a bookmark entry - `GET /api/v1/ugc/bookmarks/{bookmarkId}`
* Get all the user bookmarks - `GET /api/v1/ugc/bookmarks/{userId}`
* Update an existing bookmark - `PUT /api/v1/ugc/bookmarks/{bookmarkId}`
* Delete a bookmark - `DELETE /api/v1/ugc/bookmarks/{bookmarkId}`

The Creation, Update and Deletion of bookmarks is authorized and **only the bookmark owner** is allowed to do that action.

### Marketplace Management 

* Delete all the assets?
* Report a user
* Whitelisting

### Multimedia

* URL Check - `GET /api/v1/files/check`
* Upload image - `POST /api/v1/files/image`
* Upload audio - `POST /api/v1/files/image`


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
The flow is the following:

1. The client sends a `HTTP GET /login` request providing the user address. Example:
```
HTTP GET /api/v1/docs/auth/login/0xa99d43d86a0758d5632313b8fa3972b6088a21bb
```

1. The server will return a unique challenge token to the user

1. The client will sign locally this challenge token using the local key material

1. The client will send a `HTTP POST /login` request providing the user address and the challenge token signed
```
HTTP POST /api/v1/docs/auth/login
address=0xa99d43d86a0758d5632313b8fa3972b6088a21bb
signature=90f8bf6a479f320ead074411a4b0e7944ea8c9c15932c5d68a1b539da0b0f8431d8e50e1a5b2b3bd4cfdcfc387a5ff85d7ef5fac429c4e0e4c1bfc36d4a99770b58f42924e126ece
```

1. If the server can authenticate the user, it will return a JWT token
```
  {
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzUxMiJ9.eyJzdWIiOiIweDkwZjhiZjZhNDc5ZjMyMGVhZDA3NDQxMWE0YjBlNzk0NGVhOGM5YzEiLCJleHAiOjE0OTY1MDUwNzQsIm5iZiI6MTQ5NjUwMzI3NCwiaXNzIjoiTmV1ZnVuZCIsImF1ZCI6IndlYjMiLCJpYXQiOjE0OTY1MDMyNzR9.AaOPxTqBV4iy6GVlAu8XfbmOsIoezKfYjkqZ0SZ_RW6E7qwW-tUwSq8fq-avJrLtmCzLOD2xO9T5esEiIykP3Z9SAKWrTkdo9RwGcqGfvAySurbVAiFgW4MZ9pf9cHcB6zRks53pPcq6X2yqaVzjw28N6kBRQRc23GrUFnEDK6P_t3Tv"
  }
```

1. The user should be able to renew the authentication token passing the `Authorization` header to the `/renew` method:
```
HTTP POST /api/v1/docs/auth/renew
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzUxMiJ9.eyJzdWIiOiIweDkwZjhiZjZhNDc5ZjMyMGVhZDA3NDQxMWE0YjBlNzk0NGVhOGM5YzEiLCJleHAiOjE0OTY1MDUwNzQsIm5iZiI6MTQ5NjUwMzI3NCwiaXNzIjoiTmV1ZnVuZCIsImF1ZCI6IndlYjMiLCJpYXQiOjE0OTY1MDMyNzR9.AaOPxTqBV4iy6GVlAu8XfbmOsIoezKfYjkqZ0SZ_RW6E7qwW-tUwSq8fq-avJrLtmCzLOD2xO9T5esEiIykP3Z9SAKWrTkdo9RwGcqGfvAySurbVAiFgW4MZ9pf9cHcB6zRks53pPcq6X2yqaVzjw28N6kBRQRc23GrUFnEDK6P_t3Tv
```


#### Authorization

Once the user is authenticated, the API will be able to authorize or not the user to perform different actions. Every document in the system has a 
reference to the original public address owning the document. Depending on the module, actions like updating or deleting will require different permissions.

In the Modules section we will detail what authorization policies will be in place depending of each module.


### Storage

#### Database


#### Inmutable storage



## Links

* [Metadata SPEC](../metadata/README.md)

