
Implementation of a Mintable DID Registry.

## Functions
### initialize
```solidity
  function initialize(
    address _owner
  ) public
```

DIDRegistry Initializer
     Initialize Ownable. Only on contract creation.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_owner` | address | refers to the owner of the contract.

### registerMintableDID
```solidity
  function registerMintableDID(
    bytes32 _didSeed,
    bytes32 _checksum,
    address[] _providers,
    string _url,
    uint256 _cap,
    uint8 _royalties,
    bytes32 _activityId,
    string _attributes
  ) public returns (uint256 size)
```
Register a Mintable DID.


The first attribute of a DID registered sets the DID owner.
     Subsequent updates record _checksum and update info.


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_didSeed` | bytes32 | refers to decentralized identifier seed (a bytes32 length ID).
|`_checksum` | bytes32 | includes a one-way HASH calculated using the DDO content.
|`_providers` | address[] | list of addresses that can act as an asset provider     
|`_url` | string | refers to the url resolving the DID into a DID Document (DDO), limited to 2048 bytes.
|`_cap` | uint256 | refers to the mint cap
|`_royalties` | uint8 | refers to the royalties to reward to the DID creator in the secondary market
|`_activityId` | bytes32 | refers to activity
|`_attributes` | string | refers to the provenance attributes     

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`size`| bytes32 | refers to the size of the registry after the register action.
### enableAndMintDidNft
```solidity
  function enableAndMintDidNft(
    bytes32 _did,
    uint256 _cap,
    uint8 _royalties,
    bool _preMint
  ) public returns (bool success)
```
enableDidNft creates the initial setup of NFTs minting and royalties distribution.
After this initial setup, this data can't be changed anymore for the DID given, even for the owner of the DID.
The reason of this is to avoid minting additional NFTs after the initial agreement, what could affect the 
valuation of NFTs of a DID already created.
      

update the DID registry providers list by adding the mintCap and royalties configuration

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a byte32 length ID)
|`_cap` | uint256 | refers to the mint cap
|`_royalties` | uint8 | refers to the royalties to reward to the DID creator in the secondary market
|`_preMint` | bool | if is true mint directly the amount capped tokens and lock in the _lockAddress

### mint
```solidity
  function mint(
    bytes32 _did,
    uint256 _amount
  ) public
```
Mints a NFT associated to the DID


Because ERC-1155 uses uint256 and DID's are bytes32, there is a conversion between both
     Only the DID owner can mint NFTs associated to the DID


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID).
|`_amount` | uint256 | amount to mint

### burn
```solidity
  function burn(
    bytes32 _did,
    uint256 _amount
  ) public
```
Burns NFTs associated to the DID


Because ERC-1155 uses uint256 and DID's are bytes32, there is a conversion between both
     Only the DID owner can burn NFTs associated to the DID


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_did` | bytes32 | refers to decentralized identifier (a bytes32 length ID).
|`_amount` | uint256 | amount to burn

