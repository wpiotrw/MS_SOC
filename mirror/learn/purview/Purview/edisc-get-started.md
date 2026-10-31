---
layout: Conceptual
title: Get started with eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-get-started
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about getting started with eDiscovery in the Microsoft Purview portal.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-01T00:00:00.0000000Z
audience: Admin
ms.topic: get-started
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: 4c6ddd4a-079e-caa5-e831-1e7b5a1ec351
document_version_independent_id: 4c6ddd4a-079e-caa5-e831-1e7b5a1ec351
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-get-started.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-get-started
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-get-started.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/a3955c7b-f5ee-420d-aff5-d7119738f38b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31948f4-2f38-404b-ac93-c3c8c5b3ae33
platformId: 708a635e-1e18-769e-7dc0-6a4323a1c867
---

# Get started with eDiscovery | Microsoft Learn

Use eDiscovery to identify, preserve, collect, review, analyze, and export content that's responsive to your organization's internal and external investigations. Complete the following steps in the [eDiscovery workflow](edisc-workflow) to set up prerequisites and configure eDiscovery.

Tip

Do you prefer an interactive configuration guide experience? Check out the [Getting started with Microsoft Purview eDiscovery](https://mslearn.cloudguides.com/guides/Get%20started%20with%20Microsoft%20Purview%20eDiscovery) guide.

For more information about how eDiscovery can help you with investigations in your organization, see [Learn about eDiscovery](edisc).

## Subscriptions and billing

Before getting started with eDiscovery, review the new billing model for how data storage charges are calculated and what is included with your enterprise subscription. Depending on the types of data included in your eDiscovery cases, different charges might apply.

For more information, see [Billing in eDiscovery](edisc-billing).

Both admins and users working with eDiscovery cases require a Microsoft 365 Enterprise E3 or E5 license. If an admin account doesn't also have a Microsoft SharePoint E3 license, some SharePoint capabilities might be limited. It is recommended that both admins and users are licensed appropriately. Additionally, if the admin account has any conditional access Entra policy some operations may be restricted, see [Troubleshoot sign-in problems with Conditional Access](/en-us/entra/identity/conditional-access/troubleshoot-conditional-access?toc=%2Fentra%2Fidentity%2Fconditional-access%2Fmonitoring-health%2Ftoc.json&amp;bc=%2Fentra%2Fidentity%2Fconditional-access%2Fmonitoring-health%2Fbreadcrumb%2FTOC.json) to troubleshoot policy issues.

## Step 1: Assign permissions

To use any of the eDiscovery-related tools in the Microsoft Purview portal, you must assign the appropriate permissions to users. The easiest way to assign roles is to add the user to the appropriate role group on the **Role groups** page in the [Microsoft Purview portal](purview-portal).

For step-by-step guidance, see [Assign permissions in eDiscovery](edisc-permissions#assign-ediscovery-permissions).

Tip

Do you prefer an interactive configuration guide experience? Check out the [Configure permissions and global settings](https://mslearn.cloudguides.com/guides/Configure%20permissions%20and%20global%20settings%20with%20Microsoft%20Purview%20eDiscovery) guide.

## Step 2: Verify that required eDiscovery apps are enabled, up to date, and configured correctly

eDiscovery requires the following Enterprise apps to be enabled in your Microsoft 365 or Microsoft Office 365 organization. If you don't enable these apps, you can't access all eDiscovery view, filter, and search features. These apps must be up to date and correctly configured. Make sure that *Enabled for users to sign-in* is selected.

| App | App ID |
| --- | --- |
| Built-in security add-on for on-premises mailboxes (formerly Exchange Online Protection) | 00000007-0000-0ff1-ce00-000000000000 |
| ComplianceWorkbenchApp | 92876b03-76a3-4da8-ad6a-0511ffdf8647 |
| MicrosoftPurviewEDiscovery | b26e684c-5068-4120-a679-64a5d2c909d9 |
| Office365Zoom | 0d38933a-0bbd-41ca-9ebd-28c4b5ba7cb7 |

To check your app status and configuration, complete the following steps:

1. Go to the [Microsoft Azure portal](https://portal.azure.com).
2. Go to or search for *Enterprise Applications*.
3. Filter the results for the apps listed in the previous table to review the status and configuration for each app.
4. In each application overview blade, go to **Manage** &gt; **Properties**.
5. Make sure that **Enabled for users to sign-in** property is set to *Yes*.

Note

The *MicrosoftPurviewEDiscovery* app provides support for exporting data through scripts when premium eDiscovery features are enabled. For more information about exporting data through scripts, see [Get caseOperation](/en-us/graph/api/security-caseoperation-get?view=graph-rest-1.0).

## Step 3: Configure settings

Depending on the needs of your organization and individual cases, you might need to review and configure global eDiscovery settings:

- **General**: Turn on or off [premium eDiscovery features](edisc-settings-general) for new cases.
- **Analytics**: Turn on [Attorney-client privilege detection](edisc-settings-analytics) within your working sets. If you turn on attorney-client privilege detection, the attorney-client privilege model runs on your data and helps flag documents likely to be privileged. This flag is based on the content and by comparing participants against a user-provided attorney list. This feature doesn't replace the need for privilege review, it's meant to help you get started.
- **Guest users**: Manage [guest access](edisc-settings-guest-users) to cases in your organization. Invitations to guests are sent after your approval.
- **Tag templates**: Tags help organize content in a review set to complete various workflows. Tags can be reused across multiple review sets and cases with [tag templates](edisc-settings-tag-templates). You can group tags by sections and allow single or multiple choice tagging.

## Step 4: Create a case

To start an investigation, you must [create a case](edisc-cases-manage#create-a-case) and configure case settings. The user who creates the case is automatically added as a member. Members of the case can access the case in the Microsoft Purview portal and perform eDiscovery tasks.

## Step 5: Create a search

After creating a new case, you're automatically directed to the **Searches** tab in the case and you're ready to [create a search](edisc-search-query#create-a-search-query) for the case. Searches help you find the items you want to collect for the case.

## Step 6: Review and refine search results

After the search query completes, you see the results displayed on the **Statistics** or **Sample** tabs (depending on the initial results type you chose) for the search. To view the results for the result type not chosen initially, select the applicable tab and you can generate results for the view.

For example, if you select **Statistics** as the search result type initially, but after the search is completed you'd like to view **Sample** results, you'd select the **Sample** tab and select **Generate sample results** and define sample view settings. Select **Run query** to generate the sample results.

For more information about working with search results, see [Review, evaluate, and refine search results in eDiscovery](edisc-search-results).

## Step 7: Take action on search results

After reviewing the items returned in the search query and refining your search as needed, you can take specific actions on selected items included in the search results.

### Add search results to a review set

When you're satisfied with the results of a search and you're ready to review and analyze those search results, add them to a review set in the case. [Review sets](edisc-features-components#review-sets) provide a static, known set of content that you can search, filter, tag, analyze, and take other actions on as part of your investigation. To add search result items to a review set, see [Add search results to a review set in eDiscovery](edisc-search-add-to-review-set).

### Export or download search results

Exporting and downloading search results helps internal and external partners stay current in your investigations. Download reports provide summary information for selected items in the search results in a .csv file. Exporting search results allows you to customize what items are included in the export, the types of items exported, the export format for item, and more. For more information about exporting search results, see [Export search results in eDiscovery](edisc-search-export).

### Download search results

To download the summary information for the search result items, complete the following steps:

1. On the **Statistics** or **Sample** tabs, select **Download reports**.
2. Save the .csv file to your local computer or network share.

### Export search results

To export information for items in the search results, select **Export** and complete the details needed for the item export. For step-by-step guidance, see [Export search results in eDiscovery](edisc-search-export).

### Create holds

Create holds to preserve content that might be relevant to an eDiscovery case. You can create holds at any time and they're not dependent on searches. For step-by-step guidance, see [Create holds in eDiscovery](edisc-hold-create).