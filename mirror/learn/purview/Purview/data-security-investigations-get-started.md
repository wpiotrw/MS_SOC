---
layout: Conceptual
title: Get started with Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-get-started
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use Data Security Investigations to identify, investigate, and mitigate data risks. Follow step-by-step guidance to improve your data security.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-11T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-security-investigations
ms.collection:
- purview-compliance
- data-security-investigations
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: 40f2cb8c-e26d-9843-db0b-4b98adad8db8
document_version_independent_id: 40f2cb8c-e26d-9843-db0b-4b98adad8db8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-get-started.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-get-started
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-get-started.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 47d0f217-942d-5ad6-f20a-5983358662d0
---

# Get started with Data Security Investigations | Microsoft Learn

Use Data Security Investigations to identify, investigate, and mitigate data risk either reactively when an incident occurs or proactively to improve data security hygiene for your organization. Complete the following steps in the [workflow](data-security-investigations-workflow) to set up prerequisites and configure Data Security Investigations.

For more information about how Data Security Investigations can help you with security incidents in your organization, see [Learn about Data Security Investigations](data-security-investigations).

## Step 1: Read and agree to terms

The first time you access Data Security Investigations in the Microsoft Purview portal, you must read and agree to the terms of the [Privacy Statement](https://www.microsoft.com/privacy/privacystatement).

Confirm that you accept the terms and select **Get started**.

## Step 2: Configure permissions

To allow users to access Data Security Investigations tools in the [Microsoft Purview portal](purview-portal), assign the users the appropriate permissions. The easiest way to assign roles is to use the setup task or add the user the appropriate role group on the **Role groups** page in the Microsoft Purview portal.

Members of the *Compliance Administrator* and *Organization Management* role groups automatically have Data Security Investigations administrative and contributor access. Members of the *Data Security Management* and *Insider Risk Management* role groups automatically have contributor access. For more information about access levels, see [Additional role groups with Data Security Investigations access](data-security-investigations-permissions#additional-role-groups-with-data-security-investigations-access).

Important

To configure the AI capacity for Data Security Investigations, you must be a member of the *Data Security Investigations Admins* role group.

For step-by-step guidance, see [Assign permissions in Data Security Investigations](data-security-investigations-permissions).

## Step 3: Configure billing and usage

To get started with Data Security Investigations, configure billing and usage settings for data storage and AI analysis features. Data Security Investigations uses a payment model based on how much data you add to investigations and how much AI capacity you use for analysis of that data.

For step-by-step guidance, see [Billing models in Data Security Investigations](data-security-investigations-billing).

If you plan to enable [proactive AI insights from Data Security Posture Management (DSPM)](data-security-investigations-investigation#enable-proactive-ai-insights-from-dspm), configure billing before enabling the toggle because the auto-created investigation incurs storage and AI costs immediately.

Tip

After setup completes, all users with Data Security Investigations roles receive a notification through the Microsoft Purview Notification Center and email confirming the solution is ready. For more information, see [Email and portal notifications](data-security-investigations-workflow#email-and-portal-notifications).

## Step 4: Create an investigation

To get started with Data Security Investigations, you must create an investigation and configure investigation settings.

You can create investigations in several ways. Choose from the following methods to create a new investigation:

- From a [Microsoft Defender XDR](data-security-investigations-investigation#create-an-investigation-from-defender-xdr) incident.
- From an [Insider Risk Management](data-security-investigations-investigation#create-an-investigation-from-insider-risk-management) case.
- From [Data Security Posture Management](data-security-investigations-investigation#create-an-investigation-from-data-security-posture-management) insights.
- Manually using the [full draft mode](data-security-investigations-investigation#create-an-investigation-using-full-draft-mode).

The user who creates the investigation is automatically added as a member. Members of the investigation can access the investigation in the Microsoft Purview portal and perform Data Security Investigations tasks.

To configure user access and permissions for specific investigations, see [Configure investigation access and permission settings in Data Security Investigations](data-security-investigations-settings-access-permissions).

## Step 5: Search and evaluate results

After creating an investigation, use [search tools](data-security-investigations-search) to identify content such as email, documents, and instant messaging conversations in your organization that are relevant to a data security incident.

Tip

Refining and narrowing searches to key areas of your investigation is an iterative process. Narrow the results as much as possible before adding data items to the investigation scope. Use filters to identify non-relevant items, select the items, and mark the items as excluded.

Search tools allow you to:

- Define custom [data sources](data-security-investigations-search#data-sources)
- Create custom searches with the [query builder](data-security-investigations-search#query-builder)
- View [scope](data-security-investigations-search#scope-dashboard) and [sample](data-security-investigations-search#samples-dashboard) dashboards for search result items

## Step 6: Add items to an investigation scope

After you add data items from your search queries to the [scope](data-security-investigations-scope#access-the-investigation-scope) of the investigation, the system automatically vectorizes items for AI analysis.

You can group and view items in the investigation scope, including file [detail views](data-security-investigations-scope-views) for each data item. After [automatic vectorization](data-security-investigations-scope#automatic-vectorization) completes, you can use AI-powered tools for advanced analysis.

## Step 7: Investigate items

Use generative AI processing to help you quickly identify and review data items in the investigation scope. These tools help you decide which items need closer examination and if they should be added to the mitigation plan.

- [Vector search](data-security-investigations-ai#vector-search)
- [Categorization](data-security-investigations-ai#categorization)
- [Examination](data-security-investigations-ai#examination)

## Step 8: Take mitigation actions

Create detailed examinations and review risk examinations and recommendations for items in the investigation scope:

- [Review mitigation recommendations](data-security-investigations-mitigation)
- [Review credentials examinations](data-security-investigations-credentials)
- [Review risk examinations](data-security-investigations-risks)
- [Review personal data examinations](data-security-investigations-personal-data)
- [Use the mitigation plan](data-security-investigations-mitigation-actions)