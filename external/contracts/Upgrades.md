# Upgrade Process

This documents explains in detail how [nevermined-contracts](https://github.com/nevermined-io/contracts) should be
deployed using zeppelinOS and how the contracts can be upgraded. The latest section describes the test procedure.

## Quickstart

The first step to work with `zos` is to install dependencies then initialize the project. Then compile contracts and add contracts to the project.
Finally push the contracts into the network and create the  upgradable instances. Once the contracts are deployed they can be tested and upgraded.
Also we change the proxy administrator to a MultiSignature wallet to approve upgrades.
We are going to use the [Nevermined Contract Tools](https://github.com/nevermined-io/contract-tools) in order to perform
any future deployments/upgrades.

## Details

Here we provide more details into each step of the initial deploy and the approach of upgradeability and governance.


## Roles

Before going into more details about the deployment. We should differentiate between different roles in the system which
govern the upgradeability in nevermined-contracts.

Roles are defined as follows:

```
deployer: represented as accounts[0]
upgrader: represented as accounts[1]
upgraderWallet: represented as the upgrader from wallets.json
ownerWallet: represented as the owner from wallets.json
```
- **Deployer**: Can be any account. It is used for deploying the initial `proxy contracts` and the `logic contracts`.

- **Upgrader**: Has to be an `owner` of the `upgrader` multi sig wallet. It is used for issuing upgrade requests against the upgrader multi sig wallet.

- **UpgraderWallet**: One instance of the multi sig wallet, defined as `upgrader`. This wallet will be assigned as zos admin and is required to do upgrades.

- **OwnerWallet**: One instance of the multi sig wallet, defined as `owner`. This wallet will be assigned as the owner of all the contracts. It can be used to call specific functions in the contracts ie. change the configuration.

## Deploy & Upgrade
`zos` does not support migrations, hence all the initial configuration should be performed with
[Nevermined Contract Tools](https://github.com/nevermined-io/contract-tools).
Contract constructors are ignored so the initial setup of the contract should be made in a
[`initialize`](https://docs.zeppelinos.org/docs/advanced.html#initializers-vs-constructors)
function that will be executed only once after the initial deployment.

### 1. Configuration

[Nevermined Contract Tools](https://github.com/nevermined-io/contract-tools) checks the `contracts.json` in order to
detect the current contracts that are going to be deployed:

```json
[
  "ConditionStoreManager",
  "TemplateStoreManager",
  "AgreementStoreManager",
  "SignCondition",
  "HashLockCondition",
  "LockRewardCondition",
  "NFTHolderCondition",
  "AccessCondition",
  "EscrowReward",
  "EscrowAccessSecretStoreTemplate",
  "NFTAccessTemplate",
  "DIDRegistry"
]
```

Moreover for each network, [Nevermined Contract Tools](https://github.com/nevermined-io/contract-tools) needs to detect
the roles and their addresses from a pre-defined wallets config file.
The following configuration should be an example for `wallets-<NETWORK_NAME>.json`:

```json
[
    {
        "name": "upgrader",
        "address": "0x24eb26d4042a2ab576e7e39b87c3f33f276aef92"
    },
    {
        "name": "owner",
        "address": "0xd02d68c62401472ce35ba3c7e505deae62db2b8b"
    }
]
```

### 2. Preparation

The following commands clean, install dependencies and compile the contracts:
```console
$ yarn clean #to clean the work dir
$ yarn #install dependencies
$ yarn compile #to compile the contracts
```

### 3. Deploy & Upgrade

The following steps shows how to perform contracts deployment and upgrade on `Rinkeby` and `Kovan` networks.
#### Nile

- Copy the wallet file for `rinkeby`
  - `cp wallets_rinkeby.json wallets.json`
- run `export MNEMONIC=<your staging mnemonic>`. You will find them in the password manager.

##### Deploy the whole application

- To deploy all contracts run `yarn deploy:rinkeby`

##### Deploy a single contracts

- To deploy a single contract you need to specify the contracts to deploy as a parameter to the deploy script:
  ie. `yarn deploy:rinkeby -- NeverminedToken Dispenser`will deploy `NeverminedToken` and `Dispenser`.

##### Upgrade the whole application

- To upgrade all contracts run `yarn upgrade:rinkeby`

##### Upgrade a single contract

- To upgrade a single contract run `yarn upgrade:rinkeby -- NeverminedToken`. For upgrading the `NeverminedToken` contract.

##### Persist artifacts

- Commit all changes in `artifacts/*.rinkeby.json`

#### Kovan

- Copy the wallet file for `kovan` > `cp wallets_kovan.json wallets.json`
- run `export MNEMONIC=<your kovan mnemonic>`. You will find them in the password manager.
- run `export INFURA_TOKEN=<your infura token>`. You will get it from `infura`.

##### Deploy the whole application

- To deploy all the contracts run `yarn deploy:kovan`

##### Deploy a single contracts

- To deploy a single contracts you need to specify the contracts to deploy as a parameter to the deploy script: ie. `yarn deploy:kovan -- NeverminedToken Dispenser` will deploy `NeverminedToken` and `Dispenser`.

##### Upgrade the whole application

- To upgrade all contracts run `yarn upgrade:kovan`

##### Upgrade a single contract

- To upgrade a single contract run `yarn upgrade:kovan -- NeverminedToken`. For upgrading the `NeverminedToken` contract.

##### Persist artifacts

- Commit all changes in `artifacts/*.kovan.json`

### 4. Approve Upgrade(s)

All upgrades of the contracts have to be approved by the `upgrader` wallet configured in the `wallets.json` file.

- go to https://wallet.gnosis.pm
- Load `upgrader` wallet
- Select an Ethereum Account that is an `owner` of the multi sig wallet, but not the one who issued the upgrade request. This can be done in the following ways:
  - Connect to a local Blockchain node that holds the private key.
  - Connect to MetaMask and select the owner account from the multi sig wallet.
  - Connect a hardware wallet like ledger or trezor.
- Select the transaction you want to confirm (the upgrade script will tell you which transactions have to be approved in which wallets)
- Click Confirm


### 5. Audit Contracts

To check or document that all transactions have been approved in the multi sig wallet you can run `yarn audit:rinkeby` to get a list of all the current transactions and their current status.

```text
 Wallet: 0x24EB26D4042a2AB576E7E39b87c3f33f276AeF92

 Transaction ID: 64
 Destination: 0xfA16d26e9F4fffC6e40963B281a0bB08C31ed40C
 Contract: EscrowAccessSecretStoreTemplate
 Data is `upgradeTo` call: true
 Confirmed from: 0x7A13E1aD23546c9b804aDFd13e9AcB184EfCAF58
 Executed: false
```

### 6. Documentation
- Update the addresses in the `README.md`
- run `node ./scripts/contracts/get-addresses.js <network name>`

It will output the current proxy addresses in the `README` friendly format.

```text
| AccessCondition        | v0.9.0 | 0x45DE141F8Efc355F1451a102FB6225F1EDd2921d |
| AgreementStoreManager             | v0.9.0 | 0x62f84700b1A0ea6Bfb505aDC3c0286B7944D247C |
| ConditionStoreManager             | v0.9.0 | 0x39b0AA775496C5ebf26f3B81C9ed1843f09eE466 |
| DIDRegistry                       | v0.9.0 | 0x4A0f7F763B1A7937aED21D63b2A78adc89c5Db23 |
| DIDRegistryLibrary                | v0.9.0 | 0x3B3504908Db36f5D5f07CD420ee2BBBbDfB674cF |
| Dispenser                         | v0.9.0 | 0x865396b7ddc58C693db7FCAD1168E3BD95Fe3368 |
....

```

- Copy this to the `README.md`
