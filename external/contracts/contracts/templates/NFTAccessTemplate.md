
Implementation of NFT Access Template

     The NFT Access template is use case specific template.
     Anyone (consumer/provider/publisher) can use this template in order
     to setup an agreement allowing NFT holders to get access to Nevermined services. 
     The template is a composite of 2 basic conditions: 
     - NFT Holding Condition
     - Access Condition

     Once the agreement is created, the consumer can demonstrate is holding a NFT
     for a specific DID. If that's the case the Access condition can be fulfilled
     by the asset owner or provider and all the agreement is fulfilled.
     This can be used in scenarios where a data or services owner, can allow 
     users to get access to exclusive services only when they demonstrate the 
     are holding a specific number of NFTs of a DID.
     This is very useful in use cases like arts.

## Functions
### initialize
```solidity
  function initialize(
    address _owner,
    address _agreementStoreManagerAddress,
    address _nftHolderConditionAddress,
    address _accessConditionAddress
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
|`_nftHolderConditionAddress` | address | lock reward condition contract address
|`_accessConditionAddress` | address | access condition contract address

