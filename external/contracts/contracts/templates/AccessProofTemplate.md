
Implementation of Access Agreement Template


## Functions
### initialize
```solidity
  function initialize(
    address _owner,
    address _agreementStoreManagerAddress,
    address _didRegistryAddress,
    address _accessConditionAddress,
    address _lockConditionAddress,
    address payable _escrowConditionAddress
  ) external
```
initialize init the 
      contract with the following parameters.

this function is called only once during the contract
      initialization. It initializes the ownable feature, and 
      set push the required condition types including 
      access , lock payment and escrow payment conditions.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_owner` | address | contract's owner account address
|`_agreementStoreManagerAddress` | address | agreement store manager contract address
|`_didRegistryAddress` | address | DID registry contract address
|`_accessConditionAddress` | address | access condition address
|`_lockConditionAddress` | address | lock reward condition contract address
|`_escrowConditionAddress` | address payable | escrow reward contract address

