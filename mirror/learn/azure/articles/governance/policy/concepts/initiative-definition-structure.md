---
layout: Conceptual
title: Details of the initiative definition structure - Azure Policy | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/policy/concepts/initiative-definition-structure
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/228/azure-policy
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/675ae472-f324-ec11-b6e6-000d3a4f0da0
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
author: kgremban
learn_banner_products:
- azure
ms.author: kgremban
ms.service: azure-policy
description: Describes how policy initiative definitions are used to group policy definitions for deployment to Azure resources in your organization.
ms.date: 2025-03-04T00:00:00.0000000Z
ms.topic: reference
locale: en-us
document_id: 68937d84-5e47-4f20-7ad7-33ec3f883a07
document_version_independent_id: 89515485-857e-6f4e-8488-3a7765f86176
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/policy/concepts/initiative-definition-structure.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/policy/concepts/initiative-definition-structure
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/policy/concepts/initiative-definition-structure.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/eea02214-631d-404a-92d1-5a3357c32a26
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f42c31d7-eed9-43b7-9757-54caffb53cdc
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: c67b7fb4-4dec-0872-2252-fb93d20be44c
---

# Details of the initiative definition structure - Azure Policy | Microsoft Learn

Initiatives enable you to group several related policy definitions to simplify assignments and management because you work with a group as a single item. For example, you can group related tagging policy definitions into a single initiative. Rather than assigning each policy individually, you apply the initiative.

You use JSON to create a policy initiative definition. The policy initiative definition contains elements for:

- display name
- description
- metadata
- version
- parameters
- policy definitions
- policy groups (this property is part of the [Regulatory Compliance (Preview) feature](regulatory-compliance))

The following example illustrates how to create an initiative for handling two tags: `costCenter` and `productName`. It uses two built-in policies to apply the default tag value.

```json
{
    "properties": {
        "displayName": "Billing Tags Policy",
        "policyType": "Custom",
        "description": "Specify cost Center tag and product name tag",
        "version" : "1.0.0",
        "metadata": {
            "version": "1.0.0",
            "category": "Tags"
        },
        "parameters": {
            "costCenterValue": {
                "type": "String",
                "metadata": {
                    "description": "required value for Cost Center tag"
                },
                "defaultValue": "DefaultCostCenter"
            },
            "productNameValue": {
                "type": "String",
                "metadata": {
                    "description": "required value for product Name tag"
                },
                "defaultValue": "DefaultProduct"
            }
        },
        "policyDefinitions": [{
                "policyDefinitionId": "/providers/Microsoft.Authorization/policyDefinitions/1e30110a-5ceb-460c-a204-c1c3969c6d62",
                "definitionVersion": "1.*.*",
                "parameters": {
                    "tagName": {
                        "value": "costCenter"
                    },
                    "tagValue": {
                        "value": "[parameters('costCenterValue')]"
                    }
                }
            },
            {
                "policyDefinitionId": "/providers/Microsoft.Authorization/policyDefinitions/2a0e14a6-b0a6-4fab-991a-187a4f81c498",
                "parameters": {
                    "tagName": {
                        "value": "costCenter"
                    },
                    "tagValue": {
                        "value": "[parameters('costCenterValue')]"
                    }
                }
            },
            {
                "policyDefinitionId": "/providers/Microsoft.Authorization/policyDefinitions/1e30110a-5ceb-460c-a204-c1c3969c6d62",
                "parameters": {
                    "tagName": {
                        "value": "productName"
                    },
                    "tagValue": {
                        "value": "[parameters('productNameValue')]"
                    }
                }
            },
            {
                "policyDefinitionId": "/providers/Microsoft.Authorization/policyDefinitions/2a0e14a6-b0a6-4fab-991a-187a4f81c498",
                "parameters": {
                    "tagName": {
                        "value": "productName"
                    },
                    "tagValue": {
                        "value": "[parameters('productNameValue')]"
                    }
                }
            }
        ]
    }
}
```

Azure Policy built-ins and patterns are at [Azure Policy samples](/en-us/azure/governance/policy/samples/index).

## Metadata

The optional `metadata` property stores information about the policy initiative definition. Customers can define any properties and values useful to their organization in `metadata`. However, there are some *common* properties used by Azure Policy and in built-ins.

### Common metadata properties

- `version` (string): Tracks details about the version of the contents of a policy initiative definition. For built-ins, this metadata version follows the version property of the built-in. It's recommended to use the version property over this metadata version.
- `category` (string): Determines under which category in the Azure portal the policy definition is displayed.

    Note

    For a [Regulatory Compliance](regulatory-compliance) initiative, the `category` must be **Regulatory Compliance**.
- `preview` (boolean): True or false flag for if the policy initiative definition is *preview*.
- `deprecated` (boolean): True or false flag for if the policy initiative definition has been marked as *deprecated*.

## Version

Both built-in and custom policy initiatives can host multiple versions with the same `definitionID`. If no version number is specified, all experiences will show the latest version of the definition. To see a specific version, it must be specified in API, SDK or UI. To reference a specific version of a definition within an assignment, see [definition version within assignment](assignment-structure#policy-definition-id-and-version).

Custom initiative versioning is in public preview. During preview, each custom initiative can hold up to four versions.

The Azure Policy service uses `version`, `preview`, and `deprecated` properties to convey state and level of change to a policy definition or initiative. The format of `version` is: `{Major}.{Minor}.{Patch}`. When a policy definition is in preview state, the suffix *preview* is appended to the `version` property and treated as a **boolean**. When a policy definition is deprecated, the deprecation is captured as a boolean in the definition's metadata using `"deprecated": "true"`.

- Major Version (example: 2.0.0): introduce breaking changes such as major rule logic changes, removing parameters, adding an enforcement effect by default.
- Minor Version (example: 2.1.0): introduce changes such as minor rule logic changes, adding new parameter allowed values, change to role definitionIds, adding or removing definitions within an initiative.
- Patch Version (example: 2.1.4): introduce string or metadata changes and break glass security scenarios (rare).

Initiatives are versioned, and specific versions of policy definitions can be referenced within built-in or custom initiatives as well. For more information, see reference definition and versions.

For more information about Azure Policy versions for built-ins, see [Built-in versioning](https://github.com/Azure/azure-policy/blob/master/built-in-policies/README.md). To learn more about what it means for a policy to be *deprecated* or in *preview*, see [Preview and deprecated policies](https://github.com/Azure/azure-policy/blob/master/built-in-policies/README.md#preview-and-deprecated-policies).

## Parameters

Parameters help simplify your policy management by reducing the number of policy definitions. Think of parameters like the fields on a form - `name`, `address`, `city`, `state`. These parameters always stay the same, however their values change based on the individual filling out the form. Parameters work the same way when building policy initiatives. By including parameters in a policy initiative definition, you can reuse that parameter in the included policies.

Note

Once an initiative is assigned, initiative level parameters can't be altered. Due to this, the recommendation is to set a **defaultValue** when defining the parameter.

### Parameter properties

A parameter has the following properties that are used in the policy initiative definition:

- `name`: The name of your parameter. Used by the `parameters` deployment function within the policy rule. For more information, see using a parameter value.
- `type`: Determines if the parameter is a **string**, **array**, **object**, **boolean**, **integer**, **float**, or **datetime**.
- `metadata`: Defines subproperties primarily used by the Azure portal to display user-friendly information:
    - `description`: (Optional) The explanation of what the parameter is used for. Can be used to provide examples of acceptable values.
    - `displayName`: The friendly name shown in the portal for the parameter.
    - `strongType`: (Optional) Used when assigning the policy definition through the portal. Provides a context aware list. For more information, see strongType.
- `defaultValue`: (Optional) Sets the value of the parameter in an assignment if no value is given.
- `allowedValues`: (Optional) Provides an array of values that the parameter accepts during assignment.

As an example, you could define a policy initiative definition to limit the locations of resources in the various included policy definitions. A parameter for that policy initiative definition could be **allowedLocations**. The parameter is then available to each included policy definition and defined during assignment of the policy initiative.

```json
"parameters": {
    "init_allowedLocations": {
        "type": "array",
        "metadata": {
            "description": "The list of allowed locations for resources.",
            "displayName": "Allowed locations",
            "strongType": "location"
        },
        "defaultValue": [ "westus2" ],
        "allowedValues": [
            "eastus2",
            "westus2",
            "westus"
        ]
    }
}
```

### Passing a parameter value to a policy definition

You declare which initiative parameters you pass to which included policy definitions in the policyDefinitions array of the initiative definition. While the parameter name can be the same, using different names in the initiatives than in the policy definitions simplifies code readability.

For example, the **init\_allowedLocations** initiative parameter defined previously can be passed to several included policy definitions and their parameters, **sql\_locations** and **vm\_locations**, like this:

```json
"policyDefinitions": [
    {
        "policyDefinitionId": "/providers/Microsoft.Authorization/policyDefinitions/0ec8fc28-d5b7-4603-8fec-39044f00a92b",
        "policyDefinitionReferenceId": "allowedLocationsSQL",
        "parameters": {
            "sql_locations": {
                "value": "[parameters('init_allowedLocations')]"
            }
        }
    },
    {
        "policyDefinitionId": "/providers/Microsoft.Authorization/policyDefinitions/aa09bd0f-aa5f-4343-b6ab-a33a6a6304f3",
        "policyDefinitionReferenceId": "allowedLocationsVMs",
        "parameters": {
            "vm_locations": {
                "value": "[parameters('init_allowedLocations')]"
            }
        }
    }
]
```

This sample references the **init\_allowedLocations** parameter that was demonstrated in parameter properties.

### strongType

Within the `metadata` property, you can use **strongType** to provide a multiselect list of options within the Azure portal. **strongType** can be a supported *resource type* or an allowed value. To determine whether a *resource type* is valid for **strongType**, use [Get-AzResourceProvider](/en-us/powershell/module/az.resources/get-azresourceprovider).

Some resource types not returned by **Get-AzResourceProvider** are supported. Those resource types are:

- `Microsoft.RecoveryServices/vaults/backupPolicies`

The non-resource type allowed values for **strongType** are:

- `location`
- `resourceTypes`
- `storageSkus`
- `vmSKUs`
- `existingResourceGroups`

## Policy definitions

The `policyDefinitions` portion of the initiative definition is an *array* of which existing policy definitions are included in the initiative. As mentioned in Passing a parameter value to a policy definition, this property is where initiative parameters are passed to the policy definition.

### Policy definition properties

Each *array* element that represents a policy definition has the following properties:

- `policyDefinitionId` (string): The ID of the custom or built-in policy definition to include.
- `policyDefinitionReferenceId` (string): A short name for the included policy definition.
- `parameters`: (Optional) The name/value pairs for passing an initiative parameter to the included policy definition as a property in that policy definition. For more information, see Parameters.
- `definitionVersion` : (Optional) The version of the policy definition to refer to. If none is specified, it refers to the latest major version at assignment time and autoingests any minor updates. For more information, see [definition version](definition-structure-basics#version)
- `groupNames` (array of strings): (Optional) The group the policy definition is a member of. For more information, see Policy groups.

Here's an example of `policyDefinitions` that has two included policy definitions that are each passed the same initiative parameter:

```json
"policyDefinitions": [
    {
        "policyDefinitionId": "/providers/Microsoft.Authorization/policyDefinitions/0ec8fc28-d5b7-4603-8fec-39044f00a92b",
        "policyDefinitionReferenceId": "allowedLocationsSQL",
        "definitionVersion": "1.2.*",
        "parameters": {
            "sql_locations": {
                "value": "[parameters('init_allowedLocations')]"
            }
        }
    },
    {
        "policyDefinitionId": "/providers/Microsoft.Authorization/policyDefinitions/aa09bd0f-aa5f-4343-b6ab-a33a6a6304f3",
        "policyDefinitionReferenceId": "allowedLocationsVMs",
        "parameters": {
            "vm_locations": {
                "value": "[parameters('init_allowedLocations')]"
            }
        }
    }
]
```

## Policy definition groups

Policy definitions in an initiative definition can be grouped and categorized. Azure Policy's [Regulatory Compliance](regulatory-compliance) (preview) feature uses this property to group definitions into **controls** and **compliance domains**. This information is defined in the `policyDefinitionGroups`*array* property. More grouping details may be found in a **policyMetadata** object created by Microsoft. For information, see metadata objects.

### Policy definition groups parameters

Each *array* element in `policyDefinitionGroups` must have both of the following properties:

- `name` (string) [required]: The short name for the **group**. In Regulatory Compliance, the **control**. The value of this property is used by `groupNames` in `policyDefinitions`.
- `category` (string): The hierarchy the group belongs to. In Regulatory Compliance, the **compliance domain** of the control.
- `displayName` (string): The friendly name for the **group** or **control**. Used by the portal.
- `description` (string): A description of what the **group** or **control** covers.
- `additionalMetadataId` (string): The location of the policyMetadata object that has additional details about the **control** and **compliance domain**.

    Note

    Customers may point to an existing policyMetadata object. However, these objects are *read-only* and only created by Microsoft.

An example of the `policyDefinitionGroups` property from the NIST built-in initiative definition looks like this:

```json
"policyDefinitionGroups": [
    {
        "name": "NIST_SP_800-53_R4_AC-1",
        "additionalMetadataId": "/providers/Microsoft.PolicyInsights/policyMetadata/NIST_SP_800-53_R4_AC-1"
    }
]
```

### Metadata objects

Regulatory Compliance built-ins created by Microsoft have additional information about each control. This information is:

- Displayed in the Azure portal on the overview of a **control** on a Regulatory Compliance initiative.
- Available via REST API. See the `Microsoft.PolicyInsights` resource provider and the [policyMetadata operation group](/en-us/rest/api/policyinsights/policy-metadata/get-resource).
- Available via Azure CLI. See the [az policy metadata](/en-us/cli/azure/policy/metadata) command.

Important

Metadata objects for Regulatory Compliance are *read-only* and can't be created by customers.

The metadata for a policy grouping has the following information in the `properties` node:

- `metadataId`: The **Control ID** the grouping relates to.
- `category` (required): The **compliance domain** the **control** belongs to.
- `title` (required): The friendly name of the **Control ID**.
- `owner` (required): Identifies who has responsibility for the control in Azure: *Customer*, *Microsoft*, *Shared*.
- `description`: Additional information about the control.
- `requirements`: Details about responsibility of the implementation of the control.
- `additionalContentUrl`: A link to more information about the control. This property is typically a link to the section of documentation that covers this control in the compliance standard.

Below is an example of the **policyMetadata** object. This example metadata belongs to the *NIST SP 800-53 R4 AC-1* control.

```json
{
  "properties": {
    "metadataId": "NIST SP 800-53 R4 AC-1",
    "category": "Access Control",
    "title": "Access Control Policy and Procedures",
    "owner": "Shared",
    "description": "**The organization:**    \na. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]:  \n1. An access control policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and  \n2. Procedures to facilitate the implementation of the access control policy and associated access controls; and  \n
\nb. Reviews and updates the current:  \n1. Access control policy [Assignment: organization-defined frequency]; and  \n2. Access control procedures [Assignment: organization-defined frequency].",
    "requirements": "**a.**  The customer is responsible for developing, documenting, and disseminating access control policies and procedures. The customer access control policies and procedures address access to all customer-deployed resources and customer system access (e.g., access to customer-deployed virtual machines, access to customer-built applications).  \n**b.**  The customer is responsible for reviewing and updating access control policies and procedures in accordance with FedRAMP requirements.",
    "additionalContentUrl": "https://nvd.nist.gov/800-53/Rev4/control/AC-1"
  },
  "id": "/providers/Microsoft.PolicyInsights/policyMetadata/NIST_SP_800-53_R4_AC-1",
  "name": "NIST_SP_800-53_R4_AC-1",
  "type": "Microsoft.PolicyInsights/policyMetadata"
}
```