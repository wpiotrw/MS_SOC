---
layout: Conceptual
title: Create and deploy a collection policy | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/collection-policies-create-deploy-policy
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.subservice: purview-collection-policies
ms.collection:
- highpri
- tier1
- M365-security-compliance
- m365solution-mip
- m365initiative-compliance
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1014
search.appverid:
- MET150
description: Learn common Microsoft Purview collection policy scenarios and how configuration options affect policy behavior. Follow guided examples to create and deploy collection policies.
ai-usage: ai-assisted
locale: en-us
document_id: 7f458185-7964-dd86-2e3d-b1bb118dabda
document_version_independent_id: 7f458185-7964-dd86-2e3d-b1bb118dabda
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/collection-policies-create-deploy-policy.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: collection-policies-create-deploy-policy
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/collection-policies-create-deploy-policy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: cd1edc60-a618-f39a-9cc7-f07cf85efc7d
---

# Create and deploy a collection policy | Microsoft Learn

There are many configuration options in a Microsoft Purview collection policy. Each option changes the policy's behavior. This article presents some common intent scenarios for policies that map to configuration options. Then it walks you through configuring those options. Once you familiarize yourself with the scenarios in this article, you'll have the foundational skills that you need to use the collection policy creation UX to create your own policies.

## Before you begin

If you're new to Microsoft Purview collection policies, here's a list of the core articles you should be familiar before.

- [Collection policies solution overview](collection-policies-solution-overview).
- [Collection policies policy reference](collection-policies-policy-reference)

### SKU/subscriptions licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

[Learn about Microsoft Purview billing models](purview-billing-models)

## Billing for collection policies

This feature uses pay-as-you-go billing or per-user licensing for Microsoft Purview capabilities or both. To help you understand and manage your usage, Microsoft Purview provides a **Usage center** in the Microsoft Purview portal. For more information, see [Manage pay-as-you-go and per-user licensing usage](purview-billing-usage). To learn more about Purview billing, see [Purview billing models.](purview-billing-models).

### Granular Roles and Role Groups

There are roles and role groups that you can use to fine tune your access controls.

Here's a list of applicable roles.

- DLP Compliance Management

To learn more, see [Permissions in the Microsoft Purview portal](purview-permissions).

Here's a list of applicable role groups.

- Organization Management
- Compliance Administrator
- Insider Risk Management Admin
- Information Protection Admins
- Data Security Viewers (read-only support)

## Policy creation scenarios

There are so many configuration options in the policy creation flow that it's not possible to cover every, or even most configurations. So this article covers the most common collection policy scenarios. Going through the following scenarios gives you hands-on experience across a broad range of configurations.

- Scenario 1 Detect sensitive data shared with unmanaged cloud apps via network

### Scenario 1 Detect sensitive data shared with unmanaged cloud apps via network

This scenario detects sensitive data shared with unmanaged cloud apps at the network level. Visibility into the network traffic is provided by an integrated Secure Access Service Edge (SASE) or non-Microsoft secure browser provider, so it requires the integration to be configured and enabled. The steps to configure and enable the integration are covered in this scenario.

Note

This is a hypothetical scenario with hypothetical values. It's only for illustrative purposes. You should substitute your own sensitive information types, sensitivity labels, distribution groups and users.

#### Scenario 1 prerequisites and assumptions

- You either have an existing relationship with one or more supported SASE or non-Microsoft secure browser providers or are interested in procuring one as part of your deployment. See the [Security Store in Microsoft Purview Data Loss Prevention](https://purview.microsoft.com/datalossprevention/securitystore) to understand which providers are supported.
- If you choose a non-Microsoft SASE or secure browser integration, you have [configured Microsoft Purview pay-as-you-go billing](purview-payg-subscription-based-enablement) for your Microsoft 365 tenant. Pay-as-you-go is not required for integration with Entra Global Secure Access. For more information, see [Learn about Microsoft Purview Network Data Security](dlp-network-data-security-learn#licensing).

Configuring network data security is a multi-phase process.

1. Setup Purview integration with one or more SASE providers.
2. Configure a collection policy to detect sensitive data shared with unmanaged cloud apps at the network level.
3. Viewing the network data security data

#### Scenario 1 policy intent statement and mapping

*We need to detect data that is sensitive to our organization in text or files shared by any user in the "US Sales" group through browsers, applications, add-ins, APIs, and more, with unmanaged cloud apps, such as ChatGPT, Dropbox, Slack, or Gmail.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| "We need to detect data that is sensitive to our organization" | - Data to detect: **All classifiers** excluding **All Full Names** and **All Physical Addresses** |
| "...in text or files..." | - Activities to detect: **Text sent to or shared with cloud or AI app** and **File uploaded to or shared with cloud or AI app** |
| "...shared by any user in the "US Sales" group through browsers, applications, add-ins, APIs, and more, with unmanaged cloud apps, such as ChatGPT, Dropbox, Slack, or Gmail..." | - Where to apply: **Unmanaged cloud apps: ChatGPT, Dropbox, Slack, Gmail**- Scope: **Include "US Sales" group** |

#### Steps to create policy for scenario 1

##### SASE provider integration

Perform the following steps to integrate a supported SASE or secure browser provider with Microsoft Purview:

1. In the [Microsoft Purview portal](https://purview.microsoft.com), open the **Data Loss Prevention** solution and choose **Security Store** in the left navigation bar.
2. Select **Get solution** for the SASE or non-Microsoft secure browser solution provider you want to integrate with.
3. Complete the steps required by the integration. The steps vary depending on the SASE provider you choose. For Entra Global Secure Access integration, see [Create content policies for network content filtering](/en-us/entra/global-secure-access/how-to-network-content-filtering).

##### Configure collection policy for network data security

Perform the following steps to create the collection policy for network data security:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open the **Data loss prevention** solution and navigate to **Classifiers** &gt; **Collection policies**.
3. Select **+ Create policy**.
4. Give the policy a **Name** and an optional **Description**. You can use the policy intent statement here.
5. Choose **Next**.
6. Select **+ Add condition** and choose **Content contains**.
7. Select **Classifiers** and then **Edit**.
8. In the **Scope for classifiers** flyout, check **Exclude classifiers** and then select **+ Exclude classifiers**.
9. In the **Choose Classifiers** flyout, select **All Full Names** and **All Physical Addresses** then select **Done**.
10. Select **Done** then select **Next**.

    Tip

    You can also add **Sensitivity labels** as a condition under **Content contains** to scope detection to items with specific sensitivity labels applied. For example, you can focus detection on items labeled as "Internal" or "Confidential" while excluding publicly labeled content. Sensitivity labels are only supported with browser and network cloud apps detection.
11. Select **+ Add activities**.
12. Select **Text sent to or shared with cloud or AI app** and **File uploaded to or shared with cloud or AI app**.
13. Select **Add** then **Next**.
14. Select **+ Add data source**.
15. Select the **Unmanaged cloud apps** tab.
16. Search for and select **ChatGPT**, **Dropbox**, **Slack**, and **Gmail** and select **Add**.
17. Select **Edit scope** on the **Unmanaged cloud apps** row.
18. Select the **Include only specific** option, and on the **Included** tab select **+ Add inclusions**.
19. Search for the **US Sales** group, select it, and select **Add**.
20. Select **Save and close** then select **Next**.
21. Leave the default option of **Don't capture content** and select **Next**.
22. Ensure **Network and non-Microsoft secure browsers** is enabled and select **Next**.
23. Ensure **Turn on** is enabled and select **Next**.
24. Review the policy settings and select **Create policy**.
25. Review the **Next steps** and select **Done**.

##### Viewing the network data security data

You can view network sensitive data matches in two Purview tools:

- [Activity explorer](data-classification-activity-explorer) in Data loss prevention
- [Data Security Posture Management (DSPM)](data-security-posture-management-learn-about#how-to-use-data-security-posture-management).

###### Activity explorer

Use the following steps to view network data security matches in Activity explorer:

1. Open the **Data loss prevention** solution and navigate to **Explorers** &gt; **Activity explorer**.
2. Select **+ Add filter** and choose **Enforcement plane**.
3. Click the **Enforcement plane** filter and select **Network**.
4. Select **Apply**.

###### DSPM

Use the following steps to review collection policy results in DSPM for AI:

1. Open the [DSPM](data-security-posture-management-learn-about#how-to-use-data-security-posture-management) solution.
2. Navigate to **Reports** to see high level reports and graphs breaking down the interactions detected by the collection policy.
3. Navigate to **Activity explorer** to see individual AI interactions and sensitive information detection events.

Note

Unless you've enabled content capture for AI interactions in the collection policy, only sensitive content matches will be available to view.