
Implementation of the Template Store Manager.
     Templates are blueprints for modular SEAs. When creating an Agreement, 
     a templateId defines the condition and reward types that are instantiated 
     in the ConditionStore. This contract manages the life cycle 
     of the template ( Propose --> Approve --> Revoke ).


## Functions
### initialize
```solidity
  function initialize(
    address _owner
  ) public
```

initialize TemplateStoreManager Initializer
     Initializes Ownable. Only on contract creation.

#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_owner` | address | refers to the owner of the contract

### proposeTemplate
```solidity
  function proposeTemplate(
    address _id
  ) external returns (uint256 size)
```
proposeTemplate proposes a new template


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | address | unique template identifier which is basically
       the template contract address

### approveTemplate
```solidity
  function approveTemplate(
    address _id
  ) external
```
approveTemplate approves a template


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | address | unique template identifier which is basically
       the template contract address. Only template store
       manager owner (i.e OPNF) can approve this template.

### revokeTemplate
```solidity
  function revokeTemplate(
    address _id
  ) external
```
revokeTemplate revoke a template


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | address | unique template identifier which is basically
       the template contract address. Only template store
       manager owner (i.e OPNF) or template owner
       can revoke this template.

### getTemplate
```solidity
  function getTemplate(
    address _id
  ) external returns (enum TemplateStoreLibrary.TemplateState state, address owner, address lastUpdatedBy, uint256 blockNumberUpdated)
```
getTemplate get more information about a template


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | address | unique template identifier which is basically
       the template contract address.

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`state`| address | template status
|`owner`|  | template owner
|`lastUpdatedBy`|  | last updated by
|`blockNumberUpdated`|  | last updated at.
### getTemplateListSize
```solidity
  function getTemplateListSize(
  ) external returns (uint256 size)
```
getTemplateListSize number of templates



#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`size`|  | number of templates
### isTemplateApproved
```solidity
  function isTemplateApproved(
    address _id
  ) external returns (bool)
```
isTemplateApproved check whether the template is approved


#### Parameters:
| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_id` | address | unique template identifier which is basically
       the template contract address.

#### Return Values:
| Name                           | Type          | Description                                                                  |
| :----------------------------- | :------------ | :--------------------------------------------------------------------------- |
|`true`| address | if the template is approved
