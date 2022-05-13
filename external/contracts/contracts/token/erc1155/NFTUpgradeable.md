

Implementation of the basic standard multi-token.
See https://eips.ethereum.org/EIPS/eip-1155
Originally based on code by Enjin: https://github.com/enjin/erc-1155

_Available since v3.1._

## Functions
### __NFTUpgradeable_init
```solidity
  function __NFTUpgradeable_init(
  ) internal
```

See {_setURI}.


### __ERC1155_init_unchained
```solidity
  function __ERC1155_init_unchained(
  ) internal
```




### uri
```solidity
  function uri(
  ) external returns (string)
```

See {IERC1155MetadataURI-uri}.

This implementation returns the same URI for *all* token types. It relies
on the token type ID substitution mechanism
https://eips.ethereum.org/EIPS/eip-1155#metadata[defined in the EIP].

Clients calling this function must replace the `\{id\}` substring with the
actual token type ID.


### burn
```solidity
  function burn(
  ) public
```




### burnBatch
```solidity
  function burnBatch(
  ) public
```




### balanceOf
```solidity
  function balanceOf(
  ) public returns (uint256)
```

See {IERC1155-balanceOf}.

Requirements:

- `account` cannot be the zero address.


### balanceOf
```solidity
  function balanceOf(
  ) external returns (uint256)
```

Returns the amount of tokens of token type `id` owned by `account`.

Requirements:

- `account` cannot be the zero address.


### balanceOfBatch
```solidity
  function balanceOfBatch(
  ) public returns (uint256[])
```

See {IERC1155-balanceOfBatch}.

Requirements:

- `accounts` and `ids` must have the same length.


### setApprovalForAll
```solidity
  function setApprovalForAll(
  ) public
```

See {IERC1155-setApprovalForAll}.


### setProxyApproval
```solidity
  function setProxyApproval(
  ) public
```




### isApprovedForAll
```solidity
  function isApprovedForAll(
  ) public returns (bool)
```

See {IERC1155-isApprovedForAll}.


### isHolder
```solidity
  function isHolder(
  ) public returns (bool)
```




### safeTransferFrom
```solidity
  function safeTransferFrom(
  ) public
```

See {IERC1155-safeTransferFrom}.


### safeBatchTransferFrom
```solidity
  function safeBatchTransferFrom(
  ) public
```

See {IERC1155-safeBatchTransferFrom}.


### _mint
```solidity
  function _mint(
  ) internal
```

Creates `amount` tokens of token type `id`, and assigns them to `account`.

Emits a {TransferSingle} event.

Requirements:

- `account` cannot be the zero address.
- If `to` refers to a smart contract, it must implement {IERC1155Receiver-onERC1155Received} and return the
acceptance magic value.


### _mintBatch
```solidity
  function _mintBatch(
  ) internal
```

xref:ROOT:erc1155.adoc#batch-operations[Batched] version of {_mint}.

Requirements:

- `ids` and `amounts` must have the same length.
- If `to` refers to a smart contract, it must implement {IERC1155Receiver-onERC1155BatchReceived} and return the
acceptance magic value.


### _burn
```solidity
  function _burn(
  ) internal
```

Destroys `amount` tokens of token type `id` from `account`

Requirements:

- `account` cannot be the zero address.
- `account` must have at least `amount` tokens of token type `id`.


### _burnBatch
```solidity
  function _burnBatch(
  ) internal
```

xref:ROOT:erc1155.adoc#batch-operations[Batched] version of {_burn}.

Requirements:

- `ids` and `amounts` must have the same length.


### _beforeTokenTransfer
```solidity
  function _beforeTokenTransfer(
  ) internal
```

Hook that is called before any token transfer. This includes minting
and burning, as well as batched variants.

The same hook is called on both single and batched variants. For single
transfers, the length of the `id` and `amount` arrays will be 1.

Calling conditions (for each `id` and `amount` pair):

- When `from` and `to` are both non-zero, `amount` of ``from``'s tokens
of token type `id` will be  transferred to `to`.
- When `from` is zero, `amount` tokens of token type `id` will be minted
for `to`.
- when `to` is zero, `amount` of ``from``'s tokens of token type `id`
will be burned.
- `from` and `to` are never both zero.
- `ids` and `amounts` have the same, non-zero length.

To learn more about hooks, head to xref:ROOT:extending-contracts.adoc#using-hooks[Using Hooks].


## Events
### ProxyApproval
```solidity
  event ProxyApproval(
  )
```
Event for recording proxy approvals.


