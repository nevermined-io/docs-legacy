# Agreements API Reference

Nevermined Service Execution Agreements (SEAs) (also called "Service Agreements" or "Agreements") are contracts between parties interacting in a transaction.
They provide the capacity of defining on-chain validation of conditions as a previous step of providing a service.

The most classical scenarios in Nevermined are Service Agreements allowing Data Sharing or Remote Computation. The SEAs are used here to facilitate:

- A publisher defining a service that is offered and what a the conditions to obtaining that service
- A consumer or user that needs to fulfill the publisher conditions to getting access to that service

You can find more information about the implementation of the SEAs in the [access Spec](../../architecture/specs/access/README.md) and the [compute Spec](../../architecture/specs/compute/README.md).

Every execution by an user of a service agreement can be referenced by the `agreementId`. That is a unique identifier of the agreement execution and it is used across this api reference document.


## Create a Service Agreement

Creates an on-chain Service Agreement instance. Parameters:

* `did` Identifier of the asset associated to the service agreement
* `index` The service index of the agreement in the DDO
* `agreementId` the unique identifier of the execution of an agreement
* `signature` the signature of the `agreementId` provided by the consumer of the agreement
* `consumerAccount` The Public address of the consumer account

Example:

```java
create("did:nv:1234", 0, "8181818", "fdfdfdfd", 0xaabb)
```

## Get the status of a Service Agreement

Get the status of a service agreement instance. Parameters:

* `agreementId` the unique identifier of the execution of an agreement

Example:

```java
status("8181818")
```

## Is a Service Agreement granted?

Return if a service agreement is granted. Parameters:

* `agreementId` the unique identifier of the execution of an agreement
* `did` Identifier of the asset associated to the service agreement
* `consumerAccount` The Public address of the consumer account

Example:

```java
isAccessGranted("8181818", "did:nv:1234", 0xaabb)
```
