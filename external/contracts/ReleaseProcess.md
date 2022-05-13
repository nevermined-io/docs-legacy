# Release Process

## Build a new version

The steps to build a new version are the following:

- Create a new local feature branch, e.g. `git checkout -b release/v0.2.5`
- Use the `bumpversion.sh` script to bump the project version. You can execute the script using {major|minor|patch} as first argument to bump the version accordingly:
  - To bump the patch version: `./bumpversion.sh patch`
  - To bump the minor version: `./bumpversion.sh minor`
  - To bump the major version: `./bumpversion.sh major`
- assuming we are on version `v0.2.4` and the desired version is `v0.2.5` `./bumpversion.sh patch` has to be run.

## Interact with networks

### Roles

We define four roles:

- `deployer`: represented as `accounts[0]`
- `upgrader`: represented as `accounts[1]`
- `upgraderWallet`: represented as the `upgrader` from `wallets.json`
- `ownerWallet`: represented as the `owner` from `wallets.json`

### Flags

- `--testnet` Deploys the Dispenser, the NeverminedToken and the contracts from `contracts.json`
- `--with-token` Deploys the NeverminedToken and the contracts from `contracts.json`

#### Deployer

Can be any account. It is used for deploying the initial proxy contracts and the logic contracts.

#### Upgrader

Has to be an `owner` of the `upgrader` multi sig wallet. It is used for issuing upgrade requests against the `upgrader` multi sig wallet.

#### UpgraderWallet

One instance of the multi sig wallet, defined as `upgrader`. This wallet will be assigned as zos admin and is required to do upgrades.

#### OwnerWallet

One instance of the multi sig wallet, defined as `owner`. This wallet will be assigned as the `owner` of all the contracts. It can be used to call specific functions in the contracts ie. change the configuration.

### Deploy & Upgrade

- run `yarn clean` to clean the work dir.
- run `yarn compile` to compile the contracts.

#### Rinkeby (Testnet)

- Copy the wallet file for `rinkeby`
  - `cp wallets_rinkeby.json wallets.json`
- run `export MNEMONIC=<your rinkeby mnemonic>`. You will find them in the password manager.

##### Deploy the whole application

- To deploy all contracts run `yarn deploy:rinkeby`

##### Deploy a single contracts

- To deploy a single contract you need to specify the contracts to deploy as a parameter to the deploy script: ie. `yarn deploy:rinkeby -- NeverminedToken Dispenser`will deploy `NeverminedToken` and `Dispenser`.

##### Upgrade the whole application

- To upgrade all contracts run `yarn upgrade:rinkeby`

##### Upgrade a single contract

- To upgrade a single contract run `yarn upgrade:rinkeby -- NeverminedToken`. For upgrading the `NeverminedToken` contract.

##### Persist artifacts

- Commit all changes in `artifacts/*.rinkeby.json`

#### Mumbai (PolygonTestnet)

- Copy the wallet file for `mumbai`
    - `cp wallets_mumbai.json wallets.json`
- run `export MNEMONIC=<your mumbai mnemonic>`. You will find them in the password manager.

##### Deploy the whole application

- To deploy all contracts run `yarn deploy:mumbai`

##### Deploy a single contracts

- To deploy a single contract you need to specify the contracts to deploy as a parameter to the deploy script: ie. `yarn deploy:mumbai -- NeverminedToken Dispenser`will deploy `NeverminedToken` and `Dispenser`.

##### Upgrade the whole application

- To upgrade all contracts run `yarn upgrade:mumbai`

##### Upgrade a single contract

- To upgrade a single contract run `yarn upgrade:mumbai -- NeverminedToken`. For upgrading the `NeverminedToken` contract.

##### Persist artifacts

- Commit all changes in `artifacts/*.mumbai.json`


#### Kovan (Testnet)

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

#### Approve upgrades

All upgrades of the contracts have to be approved by the `upgrader` wallet configured in the `wallets.json` file.

- go to https://wallet.gnosis.pm
- Load `upgrader` wallet
- Select an Ethereum Account that is an `owner` of the multi sig wallet, but not the one who issued the upgrade request. This can be done in the following ways:
  - Connect to a local Blockchain node that holds the private key.
  - Connect to MetaMask and select the owner account from the multi sig wallet.
  - Connect a hardware wallet like ledger or trezor.
- Select the transaction you want to confirm (the upgrade script will tell you which transactions have to be approved in which wallets)
- Click Confirm


## Document

### Contracts documentation

- Update the contracts documentation
- run `yarn doc:contracts`
- Commit the changes in `docs/contracts` folder

### Address Documentation

- Update the addresses in the `README.md`
- run `node ./scripts/contracts/get-addresses.js <network name>`

It will output the current proxy addresses in the `README` friendly format.

```text
| AccessCondition                   | v0.9.0 | 0x45DE141F8Efc355F1451a102FB6225F1EDd2921d |
| AgreementStoreManager             | v0.9.0 | 0x62f84700b1A0ea6Bfb505aDC3c0286B7944D247C |
| ConditionStoreManager             | v0.9.0 | 0x39b0AA775496C5ebf26f3B81C9ed1843f09eE466 |
| DIDRegistry                       | v0.9.0 | 0x4A0f7F763B1A7937aED21D63b2A78adc89c5Db23 |
| DIDRegistryLibrary                | v0.9.0 | 0x3B3504908Db36f5D5f07CD420ee2BBBbDfB674cF |
| Dispenser                         | v0.9.0 | 0x865396b7ddc58C693db7FCAD1168E3BD95Fe3368 |
....

```

- Copy this to the `README.md`

## Trigger CI

- Commit the missing changes to the feature branch.
- Tag the last commit with the new version number ie. `v0.2.5`
- Push the feature branch to GitHub.
- Make a pull request from the just-pushed branch to `develop` branch.
- Wait for all the tests to pass!
- Merge the pull request into the `develop` branch.

## Release and packages

The release itself is done by `github actions` based on the tagged commit.

It will deploy the following components:

- [npm](https://www.npmjs.com/package/@nevermined-io/contracts)
- [pypi](https://pypi.org/project/nevermined-contracts/)
- [maven](https://search.maven.org/artifact/io.keyko.nevermined/contracts)
- [docker](https://hub.docker.com/r/neverminedio/contracts)

The npm, pypi and maven packages contain the contract artifacts for the contracts already deployed in different networks
(such as `Production`, `Rinkeby`, `Mumbai`, `Testing`, or `Spree`).
The docker image generated contains the contracts and script ready to be used to deploy the contracts to a network.
It is used for deploying the contracts in the local network `Spree` in [nevermined-io/tools](https://github.com/nevermined-io/tools)

Once the new version is tagged and released, you can edit the `Releases` section of GitHub with the information and
changes about the new version (in the future, these will come from the changelog):

## Audit

To check or document that all transactions have been approved in the multi sig wallet you can run `yarn audit:rinkeby`
to get a list of all the current transactions and their current status.

```text
 Wallet: 0x24EB26D4042a2AB576E7E39b87c3f33f276AeF92

 Transaction ID: 64
 Destination: 0xfA16d26e9F4fffC6e40963B281a0bB08C31ed40C
 Contract: EscrowAccessSecretStoreTemplate
 Data is `upgradeTo` call: true
 Confirmed from: 0x7A13E1aD23546c9b804aDFd13e9AcB184EfCAF58
 Executed: false
```
