


## Functions
### initialize
```solidity
  function initialize(
    address _tokenAddress,
    address _owner
  ) external
```

Dispenser Initializer

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_tokenAddress` | address | The deployed contract address of an ERC20
|`_owner` | address | The owner of the Dispenser
Runs only on initial contract creation.

### requestTokens
```solidity
  function requestTokens(
    uint256 amount
  ) external returns (bool tokensTransferred)
```

user can request some tokens for testing

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`amount` | uint256 | the amount of tokens to be requested

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`tokensTransferred`| uint256 | Boolean indication of tokens are requested
### setMinPeriod
```solidity
  function setMinPeriod(
    uint256 period
  ) external
```

the Owner can set the min period for token requests

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`period` | uint256 | the min amount of time before next request

### setMaxAmount
```solidity
  function setMaxAmount(
    uint256 amount
  ) external
```

the Owner can set the max amount for token requests

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`amount` | uint256 | the max amount of tokens that can be requested

### setMaxMintAmount
```solidity
  function setMaxMintAmount(
    uint256 amount
  ) external
```

the Owner can set the max amount for token requests

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`amount` | uint256 | the max amount of tokens that can be requested

## Events
### RequestFrequencyExceeded
```solidity
  event RequestFrequencyExceeded(
  )
```



### RequestLimitExceeded
```solidity
  event RequestLimitExceeded(
  )
```



