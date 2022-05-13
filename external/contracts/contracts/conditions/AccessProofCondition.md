
Implementation of the Access Condition with transfer proof.
The idea is that the hash of the decryption key is known before hand, and the key matching this hash
is passed from data provider to the buyer using this smart contract. Using ZK proof the key is kept
hidden from outsiders. For the protocol to work, both the provider and buyer need to have public keys
in the babyjub curve. To initiate the deal, buyer will pass the key hash and the public keys of participants.
The provider needs to pass the cipher text encrypted using MIMC (symmetric encryption). The secret key for MIMC
is computed using ECDH (requires one public key and one secret key for the curve). The hash function that is
used is Poseidon.

## Functions
### initialize
```solidity
  function initialize(
    address _owner,
    address _conditionStoreManagerAddress,
    address _agreementStoreManagerAddress,
    address _disputeManagerAddress
  ) external
```
initialize init the 
      contract with the following parameters

this function is called only once during the contract
      initialization.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_owner` | address | contract's owner account address
|`_conditionStoreManagerAddress` | address | condition store manager address
|`_agreementStoreManagerAddress` | address | agreement store manager address
|`_disputeManagerAddress` | address | dispute manager address

### hashValues
```solidity
  function hashValues(
    uint256 _origHash,
    uint256[2] _buyer,
    uint256[2] _provider
  ) public returns (bytes32)
```
hashValues generates the hash of condition inputs 
       with the following parameters


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_origHash` | uint256 | is the hash of the key
|`_buyer` | uint256[2] | buyer public key
|`_provider` | uint256[2] | provider public key

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`bytes32`| uint256 | hash of all these values
### fulfill
```solidity
  function fulfill(
    bytes32 _agreementId,
    uint256 _origHash,
    uint256[2] _buyer,
    uint256[2] _provider,
    uint256[2] _cipher,
    bytes _proof
  ) public returns (enum ConditionStoreLibrary.ConditionState)
```
fulfill key transfer

The key with hash _origHash is transferred to the _buyer from _provider.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_agreementId` | bytes32 | associated agreement
|`_origHash` | uint256 | is the hash of data to access
|`_buyer` | uint256[2] | buyer public key
|`_provider` | uint256[2] | provider public key
|`_cipher` | uint256[2] | encrypted version of the key
|`_proof` | bytes | SNARK proof that the cipher text can be decrypted by buyer to give the key with hash _origHash 

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`condition`| bytes32 | state (Fulfilled/Aborted)
## Events
### Fulfilled
```solidity
  event Fulfilled(
  )
```



