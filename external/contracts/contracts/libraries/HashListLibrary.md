
Implementation of the basic functionality of list of hash values.
This library allows other contracts to build and maintain lists
and also preserves the privacy of the data by accepting only hashed 
content (bytes32 based data type)

## Functions
### add
```solidity
  function add(
    struct HashListLibrary.List _self,
    bytes32 value
  ) public returns (bool)
```

add index an element then add it to a list

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct HashListLibrary.List | is a pointer to list in the storage
|`value` | bytes32 | is a bytes32 value

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| struct HashListLibrary.List | if value is added successfully
### add
```solidity
  function add(
    struct HashListLibrary.List _self,
    bytes32[] values
  ) public returns (bool)
```

put an array of elements without indexing
     this meant to save gas in case of large arrays

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct HashListLibrary.List | is a pointer to list in the storage
|`values` | bytes32[] | is an array of elements value

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| struct HashListLibrary.List | if values are added successfully
### update
```solidity
  function update(
    struct HashListLibrary.List _self,
    bytes32 oldValue,
    bytes32 newValue
  ) public returns (bool)
```

update the value with a new value and maintain indices

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct HashListLibrary.List | is a pointer to list in the storage
|`oldValue` | bytes32 | is an element value in a list
|`newValue` | bytes32 | new value

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| struct HashListLibrary.List | if value is updated successfully
### remove
```solidity
  function remove(
    struct HashListLibrary.List _self,
    bytes32 value
  ) public returns (bool)
```

remove value from a list, updates indices, and list size 

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct HashListLibrary.List | is a pointer to list in the storage
|`value` | bytes32 | is an element value in a list

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| struct HashListLibrary.List | if value is removed successfully
### get
```solidity
  function get(
    struct HashListLibrary.List _self,
    uint256 index
  ) public returns (bytes32)
```

has value by index 

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct HashListLibrary.List | is a pointer to list in the storage
|`index` | uint256 | is where is value is stored in the list

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`the`| struct HashListLibrary.List | value if exists
### index
```solidity
  function index(
    struct HashListLibrary.List _self,
    uint256 from,
    uint256 to
  ) public returns (bool)
```

index is used to map each element value to its index on the list 

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct HashListLibrary.List | is a pointer to list in the storage
|`from` | uint256 | index is where to 'from' indexing in the list
|`to` | uint256 | index is where to stop indexing

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| struct HashListLibrary.List | if the sub list is indexed
### setOwner
```solidity
  function setOwner(
  ) public
```

setOwner set list owner
param _owner owner address


### indexOf
```solidity
  function indexOf(
    struct HashListLibrary.List _self,
    bytes32 value
  ) public returns (uint256)
```

indexOf gets the index of a value in a list

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct HashListLibrary.List | is a pointer to list in the storage
|`value` | bytes32 | is element value in list

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`value`| struct HashListLibrary.List | index in list
### isIndexed
```solidity
  function isIndexed(
    struct HashListLibrary.List _self
  ) public returns (bool)
```

isIndexed checks if the list is indexed

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct HashListLibrary.List | is a pointer to list in the storage

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| struct HashListLibrary.List | if the list is indexed
### all
```solidity
  function all(
    struct HashListLibrary.List _self
  ) public returns (bytes32[])
```

all returns all list elements

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct HashListLibrary.List | is a pointer to list in the storage

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`all`| struct HashListLibrary.List | list elements
### has
```solidity
  function has(
    struct HashListLibrary.List _self,
    bytes32 value
  ) public returns (bool)
```

size returns the list size

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct HashListLibrary.List | is a pointer to list in the storage
|`value` | bytes32 | is element value in list

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| struct HashListLibrary.List | if the value exists
### size
```solidity
  function size(
    struct HashListLibrary.List _self
  ) public returns (uint256)
```

size gets the list size

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct HashListLibrary.List | is a pointer to list in the storage

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`total`| struct HashListLibrary.List | length of the list
### ownedBy
```solidity
  function ownedBy(
    struct HashListLibrary.List _self
  ) public returns (address)
```

ownedBy gets the list owner

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct HashListLibrary.List | is a pointer to list in the storage

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`list`| struct HashListLibrary.List | owner
