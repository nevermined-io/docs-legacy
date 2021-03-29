# Conditions API Reference

As part of the Service Execution Agreements (aka SEAs), Nevermined provide some functions to interact with these conditions.
Every execution by an user of a service agreement can be referenced by the `agreementId`. That is a unique identifier of the agreement execution and it is used across this api reference document.

## Grant Access

Grant access to an address for an specific Search Execution Agreement. Parameters:

* `agreementId` the unique identifier of the execution of an agreement
* `did` Identifier of the asset associated to the service agreement to grant the access
* `granteeAccount` Public address of the account to grant the access

Example:

```java
grantAccess("8181818", "did:nv:1234", 0xaabb)
```


## Grant Service Execution

Grant access to an address for an specific Search Execution Agreement. Parameters:

* `agreementId` the unique identifier of the execution of an agreement
* `did` Identifier of the asset associated to the service agreement to grant the access
* `granteeAccount` Public address of the account to grant the computation execution

Example:

```java
grantServiceExecution("8181818", "did:nv:1234", 0xaabb)
```


## Lock Reward

Lock the amount of token that are going to be paid for the asset. Parameters:

* `agreementId` the unique identifier of the execution of an agreement
* `amount` Amount of tokens to lock

Example:

```java
lockPayment("8181818", 10)
```


## Release Reward

Release the payment to the data publisher (access/compute/et) related with a service execution. Parameters:

* `agreementId` the unique identifier of the execution of an agreement
* `amount` Amount of tokens to release

Example:

```java
releaseReward("8181818", 10)
```


## Refund Reward

Refund the payment to the consumer. Parameters:

* `agreementId` the unique identifier of the execution of an agreement
* `amount` Amount of tokens to refund

Example:

```java
refundReward("8181818", 10)
```
