


## Functions
### getCurrentBlockNumber
```solidity
  function getCurrentBlockNumber(
  ) external returns (uint256)
```
getCurrentBlockNumber get block number



#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`the`|  | current block number
### isContract
```solidity
  function isContract(
  ) public returns (bool)
```

isContract detect whether the address is 
         is a contract address or externally owned account


#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| address | if it is a contract address
### provenanceSignatureIsCorrect
```solidity
  function provenanceSignatureIsCorrect(
    address _agentId,
    bytes32 _hash,
    bytes _signature
  ) public returns (bool)
```


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_agentId` | address | The address of the agent
|`_hash` | bytes32 | bytes32 message, the hash is the signed message. What is recovered is the signer address.
|`_signature` | bytes | Signatures provided by the agent

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| address | if the signature correspond to the agent address
### calculateTotalAmount
```solidity
  function calculateTotalAmount(
  ) public returns (uint256)
```

Sum the total amount given an uint array


#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`the`| uint256[] | total amount
