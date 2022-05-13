


## Functions
### registerAttribute
```solidity
  function registerAttribute(
    bytes32 _didSeed,
    bytes32 _checksum,
    address[] _url
  ) public returns (uint256 size)
```
registerAttribute is called only by DID owner.

this function registers DID attributes

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_didSeed` | bytes32 | refers to decentralized identifier (a byte32 length ID)
|`_checksum` | bytes32 | includes a one-way HASH calculated using the DDO content    
|`_url` | address[] | refers to the attribute value

