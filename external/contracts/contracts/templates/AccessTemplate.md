
Implementation of Access Agreement Template

     Access template is use case specific template.
     Anyone (consumer/provider/publisher) can use this template in order
     to setup an on-chain SEA. The template is a composite of three basic
     conditions. Once the agreement is created, the consumer will lock an amount
     of tokens (as listed in the DID document - off-chain metadata) to the 
     the lock reward contract which in turn will fire an event. ON the other hand 
     the provider is listening to all the emitted events, the provider 
     will catch the event and grant permissions to the consumer through 
     secret store contract, the consumer now is able to download the data set
     by asking the off-chain component of secret store to decrypt the DID and 
     encrypt it using the consumer's public key. Then the secret store will 
     provide an on-chain proof that the consumer had access to the data set.
     Finally, the provider can call the escrow reward condition in order 
     to release the payment. Every condition has a time window (time lock and 
     time out). This implies that if the provider didn't grant the access to 
     the consumer through secret store within this time window, the consumer 
     can ask for refund.

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

