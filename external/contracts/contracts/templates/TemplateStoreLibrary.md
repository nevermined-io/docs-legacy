
Implementation of the Template Store Library.
     
     Templates are blueprints for modular SEAs. When 
     creating an Agreement, a templateId defines the condition 
     and reward types that are instantiated in the ConditionStore.

## Functions
### propose
```solidity
  function propose(
    struct TemplateStoreLibrary.TemplateList _self,
    address _id
  ) internal returns (uint256 size)
```
propose new template


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct TemplateStoreLibrary.TemplateList | is the TemplateList storage pointer
|`_id` | address | proposed template contract address 

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`size`| struct TemplateStoreLibrary.TemplateList | which is the index of the proposed template
### approve
```solidity
  function approve(
    struct TemplateStoreLibrary.TemplateList _self,
    address _id
  ) internal
```
approve new template


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct TemplateStoreLibrary.TemplateList | is the TemplateList storage pointer
|`_id` | address | proposed template contract address

### revoke
```solidity
  function revoke(
    struct TemplateStoreLibrary.TemplateList _self,
    address _id
  ) internal
```
revoke new template


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_self` | struct TemplateStoreLibrary.TemplateList | is the TemplateList storage pointer
|`_id` | address | approved template contract address

