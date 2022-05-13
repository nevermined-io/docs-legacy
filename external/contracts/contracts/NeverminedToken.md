
Implementation of a Test Token.
     Test Token is an ERC20 token only for testing purposes

## Functions
### initialize
```solidity
  function initialize(
    address _owner,
    address payable _initialMinter
  ) public
```

NeverminedToken Initializer
     Runs only on initial contract creation.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_owner` | address | refers to the owner of the contract
|`_initialMinter` | address payable | is the first token minter added

### _beforeTokenTransfer
```solidity
  function _beforeTokenTransfer(
  ) internal
```

See {ERC20-_beforeTokenTransfer}.

Requirements:

- minted tokens must not cause the total supply to go over the cap.


### mint
```solidity
  function mint(
  ) external returns (bool)
```

Creates `amount` tokens and assigns them to `account`, increasing
the total supply.

Emits a {Transfer} event with `from` set to the zero address.

Requirements:

- `to` cannot be the zero address.


