---
layout: Conceptual
title: Workflow dynamic content | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-use-workflow-dynamic-content
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article describes how to use dynamic content to create expressions with built-in variables and functions in Microsoft Purview workflows.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: zeinam
ms.service: purview
ms.subservice: purview-data-map-classic
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom:
- template-how-to
- sfi-image-nochange
- msecd-doc-authoring-1030
locale: en-us
document_id: fe936dec-c8ef-e0db-405b-18ce65faa9cf
document_version_independent_id: fe936dec-c8ef-e0db-405b-18ce65faa9cf
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-use-workflow-dynamic-content.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-use-workflow-dynamic-content
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-use-workflow-dynamic-content.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: c3d92e9b-2230-f413-5966-eed8351868c9
---

# Workflow dynamic content | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

You can use dynamic content inside Microsoft Purview workflows to associate certain variables in the workflow or add other expressions to process these values.

When you add dynamic content to your workflows, you're building expressions from provided building blocks that reference and process information in your workflow so you can get the values you need in real-time.

In the dynamic content menu, the available options are built-in variables and expressions. Built-in variables represent values coming to the workflow from the items that triggered it. Expressions are formulas built from functions and variables that can process values in-workflow.

## Built-in variables

The following variables are available for a workflow connector in Microsoft Purview:

| Prerequisite connector | Built-in variable | Functionality | Type | Possible values |
| --- | --- | --- | --- | --- |
| When data access request is submitted  When asset update request is submitted | Workflow.Requestor | The ID of the requestor of the workflow | *string* |  |
|  | Asset.Name | The name of the asset | *string* |  |
|  | Asset.Description | The description of the asset | *string* or *null* |  |
|  | Asset.Type | The type of the asset | *string* |  |
|  | Asset.Fully Qualified Name | The fully qualified name of the asset | *string* |  |
|  | Asset.Owner | The IDs of the data owners of the asset | *array* of *string*s |  |
|  | Asset.Classification | The display names of classifications of the asset | *array* of *string*s |  |
|  | Asset.Schema.Classification | The display names of classifications applied to a column in the asset schema | *array* of *string*s |  |
|  | Asset.Is Certified | The indicator of whether the asset meets your organization's quality standards and can be regarded as reliable | *boolean* | `true` or `false` |
| When data access request is submitted | Workflow.Request Recipient | The ID of the request recipient of the workflow | *string* |  |
| Start and wait for an approval | Approval.Outcome | The outcome of the approval | *string* | `'Approved'` or `'Rejected'` |
|  | Approval.Assigned To | The IDs of the approvers | *array* of *string*s |  |
|  | Approval.Comments | The names of the approvers and their comments | *string* |  |
| Check data source registration for data use governance | Data Use Governance | The result of the data use governance check | *boolean* | `true` or `false` |
| When term creation request is submitted | Workflow.Requestor | The ID of the requestor of the workflow | *string* |  |
|  | Term.Name | The name of the term | *string* |  |
|  | Term.Formal Name | The formal name of the term | *string* |  |
|  | Term.Definition | The definition of the term | *string* |  |
|  | Term.Experts | The IDs of the experts of the term | *array* of *string*s |  |
|  | Term.Stewards | The IDs of the stewards of the term | *array* of *string*s |  |
|  | Term.Parent.Name | The name of parent term if exists | *string* |  |
|  | Term.Parent.Formal Name | The formal name of parent term if exists | *string* |  |
| When term update request is submitted  When term deletion request is submitted | Workflow.Requestor | The requestor of the workflow | *string* |  |
|  | Term.Name | The name of the term | *string* |  |
|  | Term.Formal Name | The formal name of the term | *string* |  |
|  | Term.Definition | The definition of the term | *string* or *null* |  |
|  | Term.Experts | The IDs of the experts of the term | *array* of *string*s |  |
|  | Term.Stewards | The IDs of the stewards of the term | *array* of *string*s |  |
|  | Term.Parent.Name | The name of parent term if exists | *string* |  |
|  | Term.Parent.Formal Name | The formal name of parent term if exists | *string* |  |
|  | Term.Created By | The ID of the creator of the term | *string* |  |
|  | Term.Last Updated By | The ID of the last updater of the term | *string* |  |
| When term import request is submitted | Workflow.Requestor | The ID of the requestor of the workflow | *string* |  |
|  | Import File.Name | The name of the file to import | *string* |  |
| Http | Http.Body | HTTP response body | *object* or *string* |  |
|  | Http.Headers | HTTP response headers | *object* |  |
|  | Http.Status Code | HTTP status code | *string* |  |
| Apply to each | Item | The current item of Apply to Each action | Any |  |
| Until | Index | The current iteration index of Until action | *integer* |  |
| Create record  Delete record  Get record  Update record | Result | The result of ServiceNow action | *object* |  |
| Get record types  List records | Result | The result of ServiceNow action | *array* of *object*s |  |

## Expressions

Workflow definitions in Microsoft Purview allow you to use functions in your expressions to process values in your workflows.

To find functions based on their general purpose, review the following tables. Or, for detailed information about each function, see the alphabetical list.

When you're building a workflow and want to add a function to your expressions, follow these steps:

1. Select the value you're going to edit.
2. Select the **Add dynamic content** button that appears underneath the textbox.
3. Select the **Expressions** tab in the dynamic content window and scroll to select your value.
4. Update your expression and select **OK** to add it.

![Screenshot showing a workflow text field with Use dynamic content highlighted and the expressions tab shown.](../media/how-to-use-workflow-dynamic-content/use-expressions.png)

### Considerations

- Function parameters are evaluated from left to right.
- Functions that appear inline with plain text require enclosing curly braces ({}) to use the expression's interpolated format instead. This format helps avoid parsing problems. If your function expression doesn't appear inline with plain text, no curly braces are necessary.

    The following example shows the correct and incorrect syntax:

    **Correct**: `"<text>/@{<function-name>('<parameter-name>')}/<text>"`

    **Incorrect**: `"<text>/@<function-name>('<parameter-name>')/<text>"`
- Functions may have overloads, which are multiple versions of a function with the same name but different ways of doing a task, depending on the input you give them.

The following sections organize functions based on their general purpose, or you can browse these functions in alphabetical order.

## String functions

To work with strings, you can use these string functions and also some collection functions. String functions work only on strings.

| String function | Task |
| --- | --- |
| endsWith | Check whether a string ends with the specified substring. |
| startsWith | Check whether a string starts with a specific substring. |

## Collection functions

To work with collections, generally arrays, strings, and sometimes, dictionaries, you can use these collection functions.

| Collection function | Task |
| --- | --- |
| contains | Check whether a collection has a specific item. |
| length | Return the number of items in a collection, or the length of a string. |

## Logical comparison functions

To work with conditions, compare values and expression results, or evaluate various kinds of logic, you can use these logical comparison functions. For the full reference about each function, see the alphabetical list.

| Logical comparison function | Task |
| --- | --- |
| not | Check whether an expression is false. Return true when the expression is false, or return false when true. |
| and | Check whether all expressions are true. Return true when all expressions are true, or return false when at least one expression is false. |
| or | Check whether at least one expression is true. Return true when at least one expression is true, or return false when all are false. |
| equals | Check whether both values are equivalent. |
| greater | Check whether the first value is greater than the second value. |
| greaterOrEquals | Check whether the first value is greater than or equal to the second value. |
| less | Check whether the first value is less than the second value. |
| lessOrEquals | Check whether the first value is less than or equal to the second value. |

## User functions

To work with users, their relationships with other users and groups, and the resources they access for example their mails, calendars, files, administrative roles, group memberships. For the full reference about each function, see the alphabetical list.

| User function | Task |
| --- | --- |
| getUserName | Get the name of the user. |
| getManager | Get the ID of the user's manager. |
| memberOfGroup | Check whether the user is a member of the group. |

## Conversion functions

To change a value's type or format, you can use these conversion functions. For the full reference about each function, see the alphabetical list.

| Conversion function | Task |
| --- | --- |
| createArray | Return an array from any number of inputs. |
| createObject | Return an empty object. |
| string | Return the string version for a value. |
| int | Try to convert the input value into an integer number. |
| float | Try to convert the input value into a float number. |
| bool | Try to convert the input value into a boolean value. |
| object | Try to convert the input value into an object. |
| array | Try to convert the input value into an array. |
| nullOrElse | Give a default value to a nullable value. |

## All functions — alphabetical list

### and

Check whether all expressions are true. Return true when all expressions are true, or return false when at least one expression is false.

| Parameter | Type | Description |
| --- | --- | --- |
| value | *boolean* | The first expression to check |
| values... | *boolean* | The rest expressions to check |

| Return value type | Description |
| --- | --- |
| *boolean* | Return true when all expressions are true. Return false when at least one expression is false. |

*Examples*

These examples check whether the specified expressions are false:

```
and(equals(1, 1), equals(2, 2))
and(equals(1, 1), equals(1, 2))
and(equals(1, 2))
```

And returns these results:

- First example: Both expressions are true, so returns `true`.
- Second example: One expression is false, so returns `false`.
- Third example: The expression is false, so returns `false`.

### array

This function tries to convert the input value into an array. It is used to cast the value from a broader type to *array*. To create an array from items, see createArray.

| Parameter | Type | Description |
| --- | --- | --- |
| value | Any | The value to convert |

| Return value type | Description |
| --- | --- |
| *array* | The converted array value |

*Example*

This example asserts **Item** of an "Apply to each" action to be of *array* type:

```
array(items('Appy to each'))
```

### bool

This function tries to convert the input value into a boolean value. It is used to cast the value from a broader type to *boolean*.

| Parameter | Type | Description |
| --- | --- | --- |
| value | Any | The value to convert |

| Return value type | Description |
| --- | --- |
| *boolean* | The converted boolean value |

*Example*

This example asserts **Item** of an "Apply to each" action to be of *boolean* type:

```
bool(items('Appy to each'))
```

### contains

Check whether a collection has a specific item. Return true when the item is found, or return false when not found.

#### Overload 1: A *string* to find a substring

This overload is case-sensitive.

| Parameter | Type | Description |
| --- | --- | --- |
| collection | *string* | The string to check |
| value | *string* | The substring to find |

| Return value type | Description |
| --- | --- |
| *boolean* | Return true when the substring is found. Return false when not found. |

#### Overload 2: A *array* to find a value

| Parameter | Type | Description |
| --- | --- | --- |
| collection | *array* | The collection to check |
| value | Any | The item to find |

| Return value type | Description |
| --- | --- |
| *boolean* | Return true when the item is found. Return false when not found. |

*Example 1*

This example checks the string "hello world" for the substring "world" and returns `true`:

```
contains('hello world', 'world')
```

*Example 2*

This example checks the variable **Asset.Owner** for the item equal to the variable **Workflow.Requestor**:

```
contains(runInput()['asset']['dataOwner'], runInput()['requestor'])
```

### createArray

Return an array from any number of inputs. This function doesn't require the input values to be of a same type.

| Parameter | Type | Description |
| --- | --- | --- |
| values... | Any | Values to create the array. |

| Return value type | Description |
| --- | --- |
| *array* | The array created from all the input items |

*Examples*

These examples create an array from inputs:

```
createArray('h', 'e', 'l', 'l', 'o')
createArray(true, null)
createArray()
```

### createObject

Return an empty object.

| Return value type | Description |
| --- | --- |
| *object* | An empty object |

*Example*

This example creates an array from inputs, and returns {}.

```
createObject()
```

### endsWith

Check whether a string ends with a specific substring. Return true when the substring is found, or return false when not found. This function is case-sensitive.

| Parameter | Type | Description |
| --- | --- | --- |
| text | *string* | The string to check |
| searchText | *string* | The ending substring to find |

| Return value type | Description |
| --- | --- |
| *boolean* | Return true when the ending substring is found. Return false when not found. |

*Example 1*

This example checks whether the "hello world" string ends with the "world" string:

```
endsWith('hello world', 'world')
```

And returns this result: `true`

*Example 2*

This example checks whether the "hello world" string ends with the "universe" string:

```
endsWith('hello world', 'universe')
```

And returns this result: `false`

### equals

Check whether both values, expressions, or objects are equivalent. Return true when both are equivalent, or return false when they're not equivalent.

| Parameter | Type | Description |
| --- | --- | --- |
| value | Any | The values, expressions, or objects to compare |
| compareTo | Any | The comparison values, expressions, or objects |

| Return value type | Description |
| --- | --- |
| *boolean* | Return true when both are equivalent. Return false when not equivalent. |

*Examples*

These examples check whether the specified inputs are equivalent.

```
equals(true, 1)
equals('abc', 'abcd')
```

And returns these results:

- First example: Both values are equivalent, so the function returns `true`.
- Second example: Both values aren't equivalent, so the function returns `false`.

### float

This function tries to convert the input value into a float number. It is used to cast the value from a broader type to *float*.

| Parameter | Type | Description |
| --- | --- | --- |
| value | Any | The value to convert |

| Return value type | Description |
| --- | --- |
| *float* | The converted float value |

*Example*

This example asserts **Item** of an "Apply to each" action to be of *float* type:

```
float(items('Appy to each'))
```

### getManager

Get the ID of the user's manager in Microsoft Entra ID.

#### Overload 1: Get for a single user

| Parameter | Type | Description |
| --- | --- | --- |
| userId | *string* | The ID of the input user |

| Return value type | Description |
| --- | --- |
| *string* or *null* | The ID of the input user's manager or null if not exist |

#### Overload 2: Get for multiple users

| Parameter | Type | Description |
| --- | --- | --- |
| userId | *array* | The IDs of the input users |

| Return value type | Description |
| --- | --- |
| *array* | The union of IDs of the input users' managers |

*Examples*

These examples get the manager(s) of the input user(s):

```
getManager(runInput()['requestor'])
getManager(runInput()['term']['stewards'])
```

- First example: The input parameter is a string, so returns the ID of the manager of **Workflow.Requestor**
- Second example: the input parameter is an array, so returns the union set of IDs of managers of **Term.Stewards**.

### getUserName

Get the name of the user in Microsoft Entra ID.

#### Overload 1: Get for a single user

| Parameter | Type | Description |
| --- | --- | --- |
| userId | *string* | The ID of the input user |

| Return value type | Description |
| --- | --- |
| *string* | The name of the input user |

#### Overload 2: Get for multiple users

| Parameter | Type | Description |
| --- | --- | --- |
| userId | *array* | The IDs of the input users |

| Return value type | Description |
| --- | --- |
| *array* | The names of the input users |

*Examples*

These examples get the name(s) of the input user(s):

```
getUserName(runInput()['requestor'])
getUserName(runInput()['term']['stewards'])
```

- First example: The input parameter is a string, so returns the name of **Workflow.Requestor**
- Second example: The input parameter is an array, so returns an array of names of **Term.Stewards**.

### greater

Check whether the first value is greater than the second value. Return true when the first value is more, or return false when less.

#### Overload 1: Compare numbers

| Parameter | Type | Description |
| --- | --- | --- |
| value | *integer* or *float* | The first value to check whether greater than the second value |
| compareTo | *integer* or *float* | The comparison value |

| Return value type | Description |
| --- | --- |
| *boolean* | Return true when the first value is greater than the second value. Return false when the first value is equal to or less than the second value. |

#### Overload 2: Compare strings

| Parameter | Type | Description |
| --- | --- | --- |
| value | *string* | The first value to check whether greater than the second value |
| compareTo | *string* | The comparison value |

| Return value type | Description |
| --- | --- |
| *boolean* | Return true when the first value is greater than the second value. Return false when the first value is equal to or less than the second value. |

*Examples*

These examples check whether the first value is greater than the second value:

```
greater(10, 5)
greater('apple', 'banana')
```

And return these results:

- First example: `true`
- Second example: `false`

### greaterOrEquals

Check whether the first value is greater than or equal to the second value. Return true when the first value is greater or equal, or return false when the first value is less.

#### Overload 1: Compare numbers

| Parameter | Type | Description |
| --- | --- | --- |
| value | *integer* or *float* | The first value to check whether greater than or equal to the second value |
| compareTo | *integer* or *float* | The comparison value |

| Return value type | Description |
| --- | --- |
| *boolean* | Return true when the first value is greater than or equal to the second value. Return false when the first value is less than the second value. |

#### Overload 2: Compare strings

| Parameter | Type | Description |
| --- | --- | --- |
| value | *string* | The first value to check whether greater than or equal to the second value |
| compareTo | *string* | The comparison value |

| Return value type | Description |
| --- | --- |
| *boolean* | Return true when the first value is greater than or equal to the second value. Return false when the first value is less than the second value. |

*Examples*

These examples check whether the first value is greater or equal than the second value:

```
greaterOrEquals(5, 5)
greaterOrEquals('apple', 'banana')
```

And return these results:

- First example: `true`
- Second example: `false`

### int

This function tries to convert the input value into an integer number. It is used to cast the value from a broader type to *integer*.

| Parameter | Type | Description |
| --- | --- | --- |
| value | Any | The value to convert |

| Return value type | Description |
| --- | --- |
| *integer* | The converted integer value |

*Example*

This example asserts **Item** of an "Apply to each" action to be of *integer* type:

```
int(items('Appy to each'))
```

### length

Return the number of items in a collection, or the length of a string.

| Parameter | Type | Description |
| --- | --- | --- |
| value | *string* or *array* | The string or the collection with the items to count |

| Return value type | Description |
| --- | --- |
| *boolean* | The number of items in the collection or the length of the string |

*Examples*

These examples count the number of items in these collections:

```
length('abcd')
length(createArray(0, 1, 2, 3))
```

And both return this result: `4`

### less

Check whether the first value is less than the second value. Return true when the first value is less, or return false when the first value is more.

#### Overload 1: Compare numbers

| Parameter | Type | Description |
| --- | --- | --- |
| value | *integer* or *float* | The first value to check whether less than the second value |
| compareTo | *integer* or *float* | The comparison value |

| Return value type | Description |
| --- | --- |
| *boolean* | Return true when the first value is less than the second value. Return false when the first value is equal to or greater than the second value. |

#### Overload 2: Compare strings

| Parameter | Type | Description |
| --- | --- | --- |
| value | *string* | The first value to check whether greater than the second value |
| compareTo | *string* | The comparison value |

| Return value type | Description |
| --- | --- |
| *boolean* | Return true when the first value is less than the second value. Return false when the first value is equal to or greater than the second value. |

*Examples*

These examples check whether the first value is less than the second value.

```
less(5, 10)
less('banana', 'apple')
```

And return these results:

- First example: `true`
- Second example: `false`

### lessOrEquals

Check whether the first value is less than or equal to the second value. Return true when the first value is less than or equal, or return false when the first value is more.

#### Overload 1: Compare numbers

| Parameter | Type | Description |
| --- | --- | --- |
| value | *integer* or *float* | The first value to check whether less than or equal to the second value |
| compareTo | *integer* or *float* | The comparison value |

| Return value type | Description |
| --- | --- |
| *boolean* | Return true when the first value is less than or equal to the second value. Return false when the first value is greater than the second value. |

#### Overload 2: Compare strings

| Parameter | Type | Description |
| --- | --- | --- |
| value | *string* | The first value to check whether less than or equal to the second value |
| compareTo | *string* | The comparison value |

| Return value type | Description |
| --- | --- |
| *boolean* | Return true when the first value is less than or equal to the second value. Return false when the first value is greater than the second value. |

*Examples*

These examples check whether the first value is less or equal than the second value.

```
lessOrEquals(10, 10)
lessOrEquals('apply', 'apple')
```

And return these results:

- First example: `true`
- Second example: `false`

### memberOfGroup

Check whether the user is a member of the group in Microsoft Entra ID. Group ID can be found on Microsoft Entra group management page.

| Parameter | Type | Description |
| --- | --- | --- |
| userId | *string* | The ID of the input user |
| groupId | *string* | The ID of the group to check |

| Return value type | Description |
| --- | --- |
| *boolean* | Return true when the user is a member of the group. Return false when the user is not a member of the group or the group doesn't exist. |

*Example*

This example check whether **Workflow.Requestor** is a member of the specified group:

```
memberOfGroup(runInput()['requestor'], '00000000-0000-0000-0000-111111111111')
```

### not

Check whether an expression is false. Return true when the expression is false, or return false when true.

| Parameter | Type | Description |
| --- | --- | --- |
| value | *boolean* | The expression to check |

| Return value type | Description |
| --- | --- |
| *boolean* | Return true when the expression is false. Return false when the expression is true. |

*Examples*

These examples check whether the specified expressions are false:

```
not(equals(1, 2))
not(equals(1, 1))
```

And return these results:

- First example: The expression is false, so the function returns `true`.
- Second example: The expression is true, so the function returns `false`.

### nullOrElse

Give a default value to a nullable value. Return a non-nullable value.

#### Overload 1: String version

| Parameter | Type | Description |
| --- | --- | --- |
| value | *string* or *null* | The nullable value |
| defaultValue | *string* | The fallback value |

| Return value type | Description |
| --- | --- |
| *string* | Return the input value if it is not null. Return the default value if the input value is null. |

#### Overload 2: Integer version

| Parameter | Type | Description |
| --- | --- | --- |
| value | *integer* or *null* | The nullable value |
| defaultValue | *integer* | The fallback value |

| Return value type | Description |
| --- | --- |
| *integer* | Return the input value if it is not null. Return the default value if the input value is null. |

#### Overload 3: Float version

| Parameter | Type | Description |
| --- | --- | --- |
| value | *float* or *null* | The nullable value |
| defaultValue | *float* | The fallback value |

| Return value type | Description |
| --- | --- |
| *float* | Return the input value if it is not null. Return the default value if the input value is null. |

#### Overload 4: Boolean version

| Parameter | Type | Description |
| --- | --- | --- |
| value | *boolean* or *null* | The nullable value |
| defaultValue | *boolean* | The fallback value |

| Return value type | Description |
| --- | --- |
| *boolean* | Return the input value if it is not null. Return the default value if the input value is null. |

#### Overload 5: Array version

| Parameter | Type | Description |
| --- | --- | --- |
| value | *array* or *null* | The nullable value |
| defaultValue | *array* | The fallback value |

| Return value type | Description |
| --- | --- |
| *array* | Return the input value if it is not null. Return the default value if the input value is null. |

#### Overload 6: Object version

| Parameter | Type | Description |
| --- | --- | --- |
| value | *object* or *null* | The nullable value |
| defaultValue | *object* | The fallback value |

| Return value type | Description |
| --- | --- |
| *object* | Return the input value if it is not null. Return the default value if the input value is null. |

*Example*

This example gives the nullable variable **Term.Definition** a default value `'Empty'`:

```
nullOrElse(runInput()['term']['definition'], 'Empty')
```

### object

This function tries to convert the input value into an object value. It is used to cast the value from a broader type to *object*.

| Parameter | Type | Description |
| --- | --- | --- |
| value | Any | The value to convert |

| Return value type | Description |
| --- | --- |
| *boolean* | The converted object value |

*Example*

This example asserts **Item** of an "Apply to each" action to be of *object* type:

```
object(items('Appy to each'))
```

### or

Check whether at least one expression is true. Return true when at least one expression is true, or return false when all are false.

| Parameter | Type | Description |
| --- | --- | --- |
| value | *boolean* | The first expression to check |
| values... | *boolean* | The rest expressions to check |

| Return value type | Description |
| --- | --- |
| *boolean* | Return true when at least one expression is true. Return false when all expressions are false. |

*Examples*

These examples check whether at least one expression is true:

```
or(equals(1, 1), equals(1, 2))
or(equals(1, 2), equals(1, 3))
or(equals(1, 2))
```

And return these results:

- First example: At least one expression is true, so the function returns `true`.
- Second example: Both expressions are false, so the function returns `false`.
- Third example: The expression is false, so the function returns `false`.

### startsWith

Check whether a string starts with a specific substring. Return true when the substring is found, or return false when not found. This function is case-sensitive.

| Parameter | Type | Description |
| --- | --- | --- |
| text | *string* | The string to check |
| searchText | *string* | The starting substring to find |

| Return value type | Description |
| --- | --- |
| *boolean* | Return true when the starting substring is found. Return false when not found. |

*Example 1*

This example checks whether the "hello world" string starts with the "hello" substring:

```
startsWith('hello world', 'hello')
```

And returns this result: `true`

*Example 2*

This example checks whether the "hello world" string starts with the "greetings" substring:

```
startsWith('hello world', 'greetings')
```

And returns this result: `false`

### string

This function returns the string version of the value.

| Parameter | Type | Description |
| --- | --- | --- |
| value | Any | The value to convert |

| Return value type | Description |
| --- | --- |
| *string* | The string version for the specified value. If the value parameter is null, this value is returned as an empty string ("") value. |

*Examples*

These examples convert the input value into a string:

```
string('abc')
string(true)
string(createArray())
```

And return these results:

- First example: The input value is a string, so returns an identity value `'abc'`.
- Second example: String version of boolean values are capitalized, so the function returns `'True'`.
- Third example: Arrays or objects are converted to JSON form, so the function returns `'[]'`.