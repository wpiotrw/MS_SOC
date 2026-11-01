---
layout: Conceptual
title: Microsoft Purview Data owner policies concepts | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/concept-policies-data-owner
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Understand Microsoft Purview Data owner policies
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: vlrodrig
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: concept-article
ms.date: 2025-02-24T00:00:00.0000000Z
locale: en-us
document_id: 5d50047e-4676-72d9-da6e-084f2df8e2d3
document_version_independent_id: 5d50047e-4676-72d9-da6e-084f2df8e2d3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/concept-policies-data-owner.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/concept-policies-data-owner
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/concept-policies-data-owner.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 37078018-c098-b8d0-02d3-695abcff6596
---

# Microsoft Purview Data owner policies concepts | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

This article discusses concepts related to managing read or modify access to assets in your data estate from within the Microsoft Purview governance portal.

Note

This capability does not offer access control for Microsoft Purview itself. Granting access to Microsoft Purview internal roles is described in [Access control in Microsoft Purview](../data-gov-classic-permissions). This capability is used to grant data plane access, i.e., access to the data itself in data systems like Azure Storage. It does not allow you to grant control plane access. Control plane access provides visibility and ability manage resources in your subscription. You can manage control plane access via [Identity and Access Management (IAM)](/en-us/azure/active-directory/fundamentals/introduction-identity-access-management)

## Overview

Access policies in Microsoft Purview enable you to manage access to different data systems across your entire data estate. For example:

A user needs read access to an Azure Storage account that has been registered in Microsoft Purview. You can grant this access directly in Microsoft Purview by creating a data access policy through the **Data policy** app in the Microsoft Purview governance portal.

Data owner policies can be enforced only on data systems that have been enabled for policy enforcement in Microsoft Purview i.e., with the **Data policy enforcement** option turned on in data source registration.

## Concepts

### Data owner policy

A **Data owner policy** is a named set of policy statements. When a policy is published to one or more data systems under Microsoft Purview’s governance, it's then enforced by them. A policy definition includes a policy name, description, and a list of one or more policy statements.

Note

Currently only a single policy statement is supported per policy.

### Policy statement

A **policy statement** is a human readable instruction that dictates how the data source should handle a specific data access operation. The policy statement comprises **Effect**, **Action, Data Resource** and **Subject**.

#### Action

An **action** is the operation being permitted or denied as part of this policy. For example: Read or Modify. These high-level logical actions map to one (or more) data actions in the data system where they are enforced.

#### Effect

The **effect** indicates what should be outcome if there is a match on the Data resource and Subject of the policy statement. Currently, the only supported value is **Allow**.

#### Data resource

The **data resource** is the fully qualified data asset path to the object the policy statement applies. It conforms to the following format:

*/subscription/&lt;subscription-id&gt;/resourcegroups/&lt;resource-group-name&gt;/providers/&lt;provider-name&gt;/&lt;data-asset-path&gt;*

Azure Storage data-asset-path format:

*Microsoft.Storage/storageAccounts/&lt;account-name&gt;/blobservice/default/containers/&lt;container-name&gt;*

Azure SQL DB data-asset-path format:

*Microsoft.Sql/servers/&lt;server-name&gt;*

#### Subject

It is a list of the end-user identities from Microsoft Entra ID for whom this policy statement is applicable. Each identity can be a service principal, an individual user, a group, or a managed service identity (MSI).

### Example

Allow Read on Data Asset: */subscription/finance/resourcegroups/prod/providers/Microsoft.Storage/storageAccounts/finDataLake/blobservice/default/containers/FinData to group Finance-analyst*

In the above policy statement, the effect is *Allow*, the action is *Read*, the data resource is Azure Storage container *FinData*, and the subject is Microsoft Entra group *Finance-analyst*. If any user that belongs to this group attempts to read data from the storage container *FinData*, the request will be allowed.

### Hierarchical enforcement of policies

The data resource specified in a policy statement is hierarchical by default. This means that the policy statement applies to the data object itself and to **all** the children objects contained by the data object. For example, a policy statement on Azure Storage container applies to all the blobs contained within it.

### Policy combining algorithm

A data source combines all the applicable local policies with all policies from Microsoft Purview and provides a consolidated decision when a user tries to access an asset. The combining strategy picks the most restrictive policy.

For example, let’s assume two different policies on an Azure Storage container *FinData* as follows,

Policy 1 - *Allow Read on Data Asset /subscription/…./containers/FinData to group Finance-analyst*

Policy 2 - *Deny Read on Data Asset /subscription/…./containers/FinData to group Finance-contractors*

Then let’s assume that user ‘user1’, who is part of two groups: *Finance-analyst* and *Finance-contractors*, executes a call to the blob read API. Since both policies will be applicable, Azure Storage will choose the most restrictive one, which is *Deny* of *Read*. Thus, the access request will be denied.

## Policy publishing

A newly created policy exists in the draft mode state, only visible in Microsoft Purview. The act of publishing initiates enforcement of a policy in the specified data systems. It's an asynchronous action that can take between 5 minutes and 2 hours to be effective, depending on the data source type. For more information, consult the Data owner policies how-to guides related to each data source type.

A policy published to a data source could contain policy statements that refer to a different data source. Such references will be ignored since the asset in question does not exist in the data source where the policy is applied.