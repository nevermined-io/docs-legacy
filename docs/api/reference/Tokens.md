# Tokens API Reference

Nevermined is a solution that uses a blockchain network to execute part of it's business logic using Smart Contracts.
Nevermined uses a Ethereum (EVM) based blockchain network. So for executing transactions in existing networks is necessary to pay of that execution.
In each network, you’ll need ETH to pay for gas, and `Nevermined` token for purchasing Nevermined assets (`access` and `compute`).

Nevermined can be deployed in any EVM based network (permissioned or not). In each of these networks ETH and Nevermined tokens can have a real value.

The Tokens API Reference describe the functionalities for Nevermined token requests and token transfers.

## Request Nevermined Tokens

Allows to request Nevermined tokens to the Dispenser. This functionality only will work in **test networks** where the Nevermined token doesn't have a real value.
In other production networks it will be necessary to contact the governance entity running Nevermined. Parameters:

* `account` the public address of the account receiving the Nevermined tokens
* `amount` the amount of Nevermined tokens to receive

Example:

```java
request(0xaabb, 5)
```

## Transfer Nevermined Tokens

Allows to transfer Nevermined tokens between accounts. Parameters:

* `receiver_account` the public address of the account receiving the Nevermined tokens
* `amount` the amount of Nevermined tokens to transfer
* `sender_account` the public address of the account transferring the Nevermined tokens

Example:

```java
transfer(0xaabb, 3, 0xccdd)
```
