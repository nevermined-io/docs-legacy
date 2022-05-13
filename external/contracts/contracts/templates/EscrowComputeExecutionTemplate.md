
Implementation of a Compute Execution Agreement Template

     EscrowComputeExecutionTemplate is use case specific template.
     Anyone (consumer/provider/publisher) can use this template in order
     to setup an on-chain SEA. The template is a composite of three basic
     conditions. Once the agreement is created, the consumer will lock an amount
     of tokens (as listed in the DID document - off-chain metadata) to the 
     the lock reward contract which in turn will fire an event. ON the other hand 
     the provider is listening to all the emitted events, the provider 
     will catch the event and grant permissions to trigger a computation granting
     the execution via the ComputeExecutionCondition contract. 
     The consumer now is able to trigger that computation
     by asking the off-chain gateway to start the execution of a compute workflow.
     Finally, the provider can call the escrow reward condition in order 
     to release the payment. Every condition has a time window (time lock and 
     time out). This implies that if the provider didn't grant the execution to 
     the consumer within this time window, the consumer 
     can ask for refund.

## Functions
### initialize
```solidity
  function initialize(
    address _owner,
    address _agreementStoreManagerAddress,
    address _didRegistryAddress,
    address _computeExecutionConditionAddress,
    address _lockPaymentConditionAddress,
    address payable _escrowPaymentAddress
  ) external
```
initialize init the 
      contract with the following parameters.

this function is called only once during the contract
      initialization. It initializes the ownable feature, and 
      set push the required condition types including 
      service executor condition, lock reward and escrow reward conditions.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_owner` | address | contract's owner account address
|`_agreementStoreManagerAddress` | address | agreement store manager contract address
|`_didRegistryAddress` | address | DID registry contract address
|`_computeExecutionConditionAddress` | address | service executor condition contract address
|`_lockPaymentConditionAddress` | address | lock reward condition contract address
|`_escrowPaymentAddress` | address payable | escrow reward contract address

