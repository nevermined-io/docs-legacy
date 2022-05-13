
Implementation of NFT Sales Template

     The NFT Sales template supports an scenario where a NFT owner
     can sell that asset to a new Owner.
     Anyone (consumer/provider/publisher) can use this template in order
     to setup an agreement allowing a NFT owner to transfer the asset ownership
     after some payment. 
     The template is a composite of 3 basic conditions: 
     - Lock Payment Condition
     - Transfer NFT Condition
     - Escrow Reward Condition

     This scenario takes into account royalties for original creators in the secondary market.
     Once the agreement is created, the consumer after payment can request the transfer of the NFT
     from the current owner for a specific DID.

## Functions
### initialize
```solidity
  function initialize(
    address _owner,
    address _agreementStoreManagerAddress,
    address _lockPaymentConditionAddress,
    address _transferConditionAddress,
    address payable _escrowPaymentAddress
  ) external
```
initialize init the 
      contract with the following parameters.

this function is called only once during the contract
      initialization. It initializes the ownable feature, and 
      set push the required condition types including 
      access secret store, lock reward and escrow reward conditions.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_owner` | address | contract's owner account address
|`_agreementStoreManagerAddress` | address | agreement store manager contract address
|`_lockPaymentConditionAddress` | address | lock reward condition contract address
|`_transferConditionAddress` | address | transfer NFT condition contract address
|`_escrowPaymentAddress` | address payable | escrow reward condition contract address

