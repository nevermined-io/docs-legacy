
Hash lists contract is a sample list contract in which uses 
     HashListLibrary.sol in order to store, retrieve, remove, and 
     update bytes32 values in hash lists.
     This is a reference implementation for IList interface. It is 
     used for whitelisting condition. Any entity can have its own 
     implementation of the interface in which could be used for the
     same condition.

## Functions
### initialize
```solidity
  function initialize(
    address _owner
  ) public
```

HashLists Initializer

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_owner` | address | The owner of the hash list
Runs only upon contract creation.

### hash
```solidity
  function hash(
    address account
  ) public returns (bytes32)
```

hash ethereum accounts

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`account` | address | Ethereum address

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`bytes32`| address | hash of the account
### add
```solidity
  function add(
    bytes32[] values
  ) external returns (bool)
```

put an array of elements without indexing
     this meant to save gas in case of large arrays

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`values` | bytes32[] | is an array of elements value

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| bytes32[] | if values are added successfully
### add
```solidity
  function add(
    bytes32 value
  ) external returns (bool)
```

add indexes an element then adds it to a list

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`value` | bytes32 | is a bytes32 value

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| bytes32 | if value is added successfully
### update
```solidity
  function update(
    bytes32 oldValue,
    bytes32 newValue
  ) external returns (bool)
```

update the value with a new value and maintain indices

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`oldValue` | bytes32 | is an element value in a list
|`newValue` | bytes32 | new value

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| bytes32 | if value is updated successfully
### index
```solidity
  function index(
    uint256 from,
    uint256 to
  ) external returns (bool)
```

index is used to map each element value to its index on the list 

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`from` | uint256 | index is where to 'from' indexing in the list
|`to` | uint256 | index is where to stop indexing

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| uint256 | if the sub list is indexed
### has
```solidity
  function has(
    bytes32 id,
    bytes32 value
  ) external returns (bool)
```

has checks whether a value is exist

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`id` | bytes32 | the list identifier (the hash of list owner's address)
|`value` | bytes32 | is element value in list

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| bytes32 | if the value exists
### has
```solidity
  function has(
    bytes32 value
  ) external returns (bool)
```

has checks whether a value is exist

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`value` | bytes32 | is element value in list

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| bytes32 | if the value exists
### remove
```solidity
  function remove(
    bytes32 value
  ) external returns (bool)
```

remove value from a list, updates indices, and list size 

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`value` | bytes32 | is an element value in a list

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| bytes32 | if value is removed successfully
### get
```solidity
  function get(
    bytes32 id,
    uint256 _index
  ) external returns (bytes32)
```

has value by index 

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`id` | bytes32 | the list identifier (the hash of list owner's address)
|`_index` | uint256 | is where is value is stored in the list

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`the`| bytes32 | value if exists
### size
```solidity
  function size(
    bytes32 id
  ) external returns (uint256)
```

size gets the list size

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`id` | bytes32 | the list identifier (the hash of list owner's address)

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`total`| bytes32 | length of the list
### all
```solidity
  function all(
    bytes32 id
  ) external returns (bytes32[])
```

all returns all list elements

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`id` | bytes32 | the list identifier (the hash of list owner's address)

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`all`| bytes32 | list elements
### indexOf
```solidity
  function indexOf(
    bytes32 id,
    bytes32 value
  ) external returns (uint256)
```

indexOf gets the index of a value in a list

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`id` | bytes32 | the list identifier (the hash of list owner's address)
|`value` | bytes32 | is element value in list

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`value`| bytes32 | index in list
### ownedBy
```solidity
  function ownedBy(
    bytes32 id
  ) external returns (address)
```

ownedBy gets the list owner

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`id` | bytes32 | the list identifier (the hash of list owner's address)

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`list`| bytes32 | owner
### isIndexed
```solidity
  function isIndexed(
    bytes32 id
  ) external returns (bool)
```

isIndexed checks if the list is indexed

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`id` | bytes32 | the list identifier (the hash of list owner's address)

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| bytes32 | if the list is indexed
