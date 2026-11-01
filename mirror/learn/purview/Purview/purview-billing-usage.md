---
layout: Conceptual
title: Manage pay-as-you-go and per-user licensing usage | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/purview-billing-usage
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
description: Use the Microsoft Purview Usage center to understand and manage your pay-as-you-go and per-user licensing usage for Microsoft Purview capabilities.
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-11-14T00:00:00.0000000Z
ms.service: purview
ms.subservice: purview-portal
audience: ITPro
ms.topic: concept-article
ms.collection:
- tier1
- purview-compliance
- essentials-get-started
ms.custom:
- admindeeplinkCOMPLIANCE
- intro-overview
locale: en-us
document_id: aad16c7c-acb6-170a-cf7f-cda952631f63
document_version_independent_id: aad16c7c-acb6-170a-cf7f-cda952631f63
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/purview-billing-usage.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purview-billing-usage
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/purview-billing-usage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 05e51b88-7fde-9b06-4838-dc4eba689d0d
---

# Manage pay-as-you-go and per-user licensing usage | Microsoft Learn

Note

The Microsoft Purview **Usage center** feature is in preview.

Microsoft Purview solutions are licensed through the **Premium licensing model**, which is the per-seat model, the **pay-as-you-go billing model** model, or a combination of both. If you need to understand the billing models in Microsoft Purview, see [Learn about Microsoft Purview billing models](purview-billing-models).

The **Usage center** in the Microsoft Purview portal helps you understand and manage your usage for both billing models. You can view your pay-as-you-go billing usage and your per-user licensing usage for Microsoft Purview capabilities.

## Permissions

To access the **Usage center** &gt; **Pay-as-you-go** and **Usage center** &gt; **Premium usage** pages, the account you use must have one of the following roles:

- Global Reader
- Security Reader
- Global Admin

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## Pay-as-you-go usage

The **Usage center** provides detailed information on **Total Units Used** about your pay-as-you-go billing usage by feature and by workload. For definitions on the **Unit of Measure** see [Units of measure for pay-as-you-go capabilities](purview-billing-models#units-of-measure-for-pay-as-you-go-capabilities). The pay-as-you-go usage page also lets you toggle the features listed between paused and active states.

| Feature name | Pausable | Detailed report available |
| --- | --- | --- |
| Communication compliance Standard | Yes | Yes |
| Communication compliance Premium | Yes | Yes |
| Enterprise Data Management Basic | No | Yes |
| Enterprise Data Management Standard | No | Yes |
| Enterprise Data Management Advanced | No | Yes |
| Audit | Yes | Yes |
| Insider Risk Management | No | Yes |
| On-Demand Classification | Yes | Yes |
| Information Protection | Yes | Yes |
| Data lifecycle management | Yes | Yes |
| Data Catalogue Governed Assets | No | Yes |
| Data Security Investigations | No | No |
| In-transit protection of data to AI apps | No | Yes |
| In-transit protection of data at the network layer | No | Yes |
| eDiscovery | Yes | No |

## Premium usage model

The **Premium usage** model is useful for identifying underlicensing situations and under utilization of purchased licenses.

### Policy Scoping

Use the **Policy Scoping** card tells you how many unlicensed users are in scope of one or more Microsoft Purview premium features. This helps you identify potential under-licensing situations so you can optimize your licensing usage.

The **Policy Scoping** card shows three key metrics:

- Policy scoped users: The total number of users in scope of one or more Microsoft Purview premium features.
- Policy scope users with assigned licenses: The number of users in scope of one or more, which are licensed one or more of Microsoft Purview premium features.
- Policy scoped users without assigned licenses: The number of users in scope of one or more Microsoft Purview premium features, which aren't licensed for any of those features.

The unlicensed user metric is calculated like this:

**Policy scoped users** - **Policy scoped users with assigned licenses** = **Policy scoped users without assigned licenses**

### License Assignment

There may be users who are assigned licenses for Microsoft Purview premium features but aren't in scope of any of the features. So essentially, you're paying for usage of a feature, but not using the feature. The **License Assignment** card helps you identify these users so you can optimize your licensing usage.

The **License Assignment** card shows two key metrics:

- **License assigned users**: The number of users that are assigned Microsoft Purview Premium licenses.
- **License assigned users not under policy scope**: The number of users that are assigned Microsoft Purview Premium licenses but aren't in scope of any Microsoft Purview premium features.

The **License assigned users not under policy scope** metric is calculated like this:

**License assigned users** - **Policy scoped users with assigned licenses** = **License assigned users not under policy scope**