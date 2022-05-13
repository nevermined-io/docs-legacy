# Nevermined Contracts Documentation

The Nevermined Contracts are organized in different modules. Each of them is intended to keep different Solidity
Smart Contracts code providing different building blocks or capabilities to implement the Nevermined Business Logic.

## Modules

### Registry

It allows the registration of assets into a Nevermined network. The entry point for that is the `DIDRegistry` contract.
It allows to

The different contracts involved in the `Registry` module are:

- [DID Registry](contracts/registry/DIDRegistry.md)
- [DID Factory](contracts/registry/DIDFactory.md)
- [NFT Upgradeable](contracts/token/erc1155/NFTUpgradeable.md)
- [DIDRegistry Library](contracts/registry/DIDRegistryLibrary.md)
- [Provenance Registry](contracts/registry/ProvenanceRegistry.md)

### Service Agreement Templates

This are the templates used for the **end users** to define use cases or user flows. They implement a pre-defined user
flow implementing a use case (like selling access to data). Every different service agreement template allows to create
instances of their type by the users with custimzed conditions.

The existing templates existing are:

- [Access Template](contracts/templates/AccessTemplate.md)
- [Compute Execution Template](contracts/templates/EscrowComputeExecutionTemplate.md)
- [DID Sales Template](contracts/templates/DIDSalesTemplate.md)
- [NFT Sales Template](contracts/templates/NFTSalesTemplate.md)
- [NFT Access Template](contracts/templates/NFTAccessTemplate.md)
- [Dynamic Access Template](contracts/templates/DynamicAccessTemplate.md)

A part of this, the agreements contracts module provide some internal components to manage the registering of service
agreements on-chain. This contracts typically don't need be instantiated directly by end-users:

- [Agreement Store Manager](contracts/agreements/AgreementStoreManager.md)
- [Agreement Store Library](contracts/agreements/AgreementStoreLibrary.md)


### Service Agreement Conditions

Are the different conditions allowing to the users of a flow to define the ground rules as part of an agreement.
Conditions typically have different parameters allowing to the users to define the specific conditions that someone
executing an agreement needs to fulfill.

The combination of templates and agreements allow the definition of complex scenarios where the users can interact and
transact regarding Nevermined digital assets.

The existing conditions ready to be used are:

- [Access Condition](contracts/conditions/AccessCondition.md)
- [Lock Payment Condition](contracts/conditions/LockPaymentCondition.md)
- [Rewards](#)
    - [Reward](contracts/conditions/rewards/Reward.md)
    - [Escrow Payment](contracts/conditions/rewards/EscrowPaymentCondition.md)
- [Compute Execution Condition](contracts/conditions/ComputeExecutionCondition.md)
- [Hash Lock Condition](contracts/conditions/HashLockCondition.md)
- [NFT Access Condition](contracts/conditions/NFTs/NFTAccessCondition.md)
- [NFT Holder Condition](contracts/conditions/NFTs/NFTHolderCondition.md)
- [NFT Lock Condition](contracts/conditions/NFTs/NFTLockCondition.md)
- [Transfer DID Ownership Condition](contracts/conditions/TransferDIDOwnershipCondition.md)
- [Transfer NFT Condition](contracts/conditions/NFTs/TransferNFTCondition.md)
- [Sign Condition](contracts/conditions/SignCondition.md)
- [Whitelisting Condition](contracts/conditions/WhitelistingCondition.md)
- [Threshold Condition](contracts/conditions/ThresholdCondition.md)

### Token

This are the contracts providing the following capabilities:

- [Nevermined Token](contracts/NeverminedToken.md) - A reference implementation of a `ERC20` token.
  This `NVM` token is provided as default token in a Nevermined deployment. The usage of this token is not necessary.
  A different `ERC20` can be used depending on the deployment of the network or the configuration of the service
  agreements. This allows to support payments in the `NVM` token, a different `ERC20` token or in `ETH`.
- [Dispenser](contracts/Dispenser.md) - It allows the distribution of `ERC20` tokens (typically `NVM` token) in a
  testnet. Because of that, the Dispenser contract **is not deployed in production or mainnet networks**.

### Libraries

- [EpochLibrary](contracts/libraries/EpochLibrary.md)
- [HashListLibrary](contracts/libraries/HashListLibrary.md)
- [Common](contracts/Common.md)
- [Hash List](contracts/HashLists.md)


### Contract Interfaces


- [IList](contracts/interfaces/IList.md)
- [ISecret Store](contracts/interfaces/ISecretStore.md)
- [ISecret Store Permission](contracts/interfaces/ISecretStorePermission.md)

### Template Libraries

Allow the registration and management of Service Agreement Templates. Typically are not necessary by users, that can
make use of the already pre-defined service agreement templates.

- [Template Store Manager](contracts/templates/TemplateStoreManager.md)
- [Template Store Library](contracts/templates/TemplateStoreLibrary.md)
- [Agreement Template](contracts/templates/AgreementTemplate.md)

### Condition Libraries

Internal libraries allowing the management and support of conditions.

- [Condition Store Manager](contracts/conditions/ConditionStoreManager.md)
- [Condition Store Library](contracts/conditions/ConditionStoreLibrary.md)
- [Condition Base Contract](contracts/conditions/Condition.md)

