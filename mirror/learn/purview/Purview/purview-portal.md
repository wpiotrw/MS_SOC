---
layout: Conceptual
title: Learn about the Microsoft Purview portal | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/purview-portal
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Explore the Microsoft Purview portal's unified experience for data security, data governance, and risk and compliance. Learn how the portal helps you discover solutions, navigate features, and manage settings across your data estate.
ms.date: 2026-08-05T00:00:00.0000000Z
keywords: Microsoft Purview, compliance, governance, solutions
ms.author: chvukosw
author: chvukosw
manager: laurawi
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-portal
f1.keywords:
- NOCSH
search.appverid:
- MET150
ms.collection:
- purview-compliance
- essentials-get-started
ai-usage: ai-assisted
ms.custom: sfi-image-nochange, msecd-doc-authoring-1020
locale: en-us
document_id: cb9d18dc-5397-d02c-8f1b-7634c27d6729
document_version_independent_id: cb9d18dc-5397-d02c-8f1b-7634c27d6729
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/purview-portal.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purview-portal
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/purview-portal.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 0ba17cf2-992e-71dc-d869-e628e4f314ca
---

# Learn about the Microsoft Purview portal | Microsoft Learn

Microsoft Purview is a comprehensive set of solutions that helps you govern, protect, and manage data in your organization. The [Microsoft Purview portal](https://purview.microsoft.com) has a streamlined design and unified experience that helps you discover and access data security, data governance, and risk and compliance solutions for all your data, wherever it lives across your data estate. The unified experience streamlines navigation for all Purview solutions and provides a single-entry point for settings, search, and roles and permissions management.

## Get started with the portal

When you first navigate to and open the [Microsoft Purview portal](https://purview.microsoft.com), a welcome dialog appears that provides a brief overview of the new portal experience. After you agree to the terms and privacy conditions, select **Get started** to follow teaching bubbles that highlight key areas of the new portal experience.

![Screenshot of the Microsoft Purview portal welcome dialog showing the main starting point for accessing Purview features.](media/purview-portal-welcome.png)

Next, you see the new home page. The home page is your starting point for accessing all Microsoft Purview solutions, portal-wide settings, summary information about your data, and more.

![Screenshot of the Microsoft Purview portal home page displaying solution cards, compliance posture, and navigation options.](media/purview-portal.png)

## Relocated portal features

Some features and capabilities that you're familiar with when using the retired Microsoft Purview compliance portal and the [classic Microsoft Purview governance portal](legacy/use-microsoft-purview-governance-portal) are relocated or retired in the Microsoft Purview portal.

| Feature or capability | Summary of changes |
| --- | --- |
| Classification | Classification is renamed to *Classifiers* and moved to the left-navigation area for each solution. |
| Content Search | Content Search features are now included as core components in [eDiscovery](edisc). |
| Data asset search and browse | Data asset search and browse has moved to **Unified Catalog** &gt; **Discovery** &gt; **Data assets**. |
| Data Estate Insights | Data Estate Insights is renamed to *Reports* and moved to **Unified Catalog** &gt; **Health management** &gt; **Reports**. |
| Explorers | Explorers moved to the left-navigation area for each solution. |
| Glossary | The glossary moved to **Unified Catalog** &gt; **Discovery** &gt; **Enterprise glossary**. |
| Policies | Policies moved to the left-navigation area for each solution. |
| Privacy Risk Management | [Privacy Risk Management](/en-us/privacy/priva/risk-management) is available in the Microsoft Priva portal. |
| Reports | Reports moved to the left-navigation area for each solution. |
| Roles and scopes | Roles and scopes are located in **Settings**. |
| Settings | Settings are located in the global left-navigation or at the top command bar of the portal. Select **Settings** to configure global and solution-level setting options. |

## Permissions and subscriptions

Depending on your permissions and your Microsoft Purview subscription, you see different solutions, home page cards, and features in the portal. For example, if you have permissions and a supported subscription to access a specific data governance or risk and compliance solution (such as **Data Loss Prevention**, **Insider Risk Management**, and others), you see these solution cards on the home page. If you don't have permissions or a supported subscription, you don't see these solution cards on the home page.

Note

You can grant Microsoft Purview permissions through security group membership. If you use Microsoft Entra Privileged Identity Management (PIM) for just-in-time membership for security groups in Microsoft Purview role groups, it can take up to two hours after activation for eligible administrators to have effective permissions applied in Microsoft Purview. For more information about PIM, see [What is Microsoft Entra Privileged Identity Management](/en-us/entra/id-governance/privileged-identity-management/pim-configure).

For more information about permissions and role groups in Microsoft Purview, see:

- [Permissions in the Microsoft Purview portal](purview-permissions)
- [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview portals](/en-us/microsoft-365/security/office-365-security/scc-permissions?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json)

For more information about Microsoft Purview subscription requirements, see:

- [Purview compliance solution requirements](https://aka.ms/M365EnterprisePlans)
- [Purview governance solution plan requirements](data-governance-purview-portal)

## Global search

Use global search at the top of the portal to search for navigation, users, and resources across all your solutions and data estate. For terms you enter in the search bar, you see applicable results grouped by the following sections in the search results drop down:

- **Navigation**: Results for items associated with specific Microsoft Purview solutions and solution features.
- **Users**: Results for users included in your organization. When you select a user, you see user details, including email, role groups, and administrative units assigned. To view role groups for a user, you must have the *Role management* role assigned that isn't restricted to an [administrative unit](purview-admin-units).
- **Resources**: Results for helpful resources associated with the searched term.

To view the consolidated search results page, select the links to view all results at the bottom of any section listed in the search results drop down or select the **Search** arrow on the right side of the search bar. To filter the displayed results by section on the search results page, select the **All**, **Navigation**, **Users**, or **Resources** link at the top of the page. To view all results in each section, select **Show more**.

![Screenshot of Microsoft Purview portal search results grouped by navigation, users, and resources categories.](media/purview-portal-search-results.png)

The five most recently entered search terms are retained as quick links in the search bar for quick access to current results for these terms.

## Sections and cards

### Solution cards and the Solutions page

Solution cards on the portal home page allow you to quickly access and open the Microsoft Purview solutions that you have access to. You can't customize the displayed view for these cards.

![Screenshot of Microsoft Purview portal solution cards showing available solutions on the home page.](media/purview-portal-solution-cards.png)

To view and manage all solutions you have access to that aren't listed in the solution card list, select **View all solutions**. From the **Solutions** page, you can select solutions in the **Core** section to set up and configure app experiences across Microsoft Purview. You can also use the **Risk & Compliance**, **Data Governance**, and **Data Security** sections to directly view and manage specific Microsoft Purview solutions. Use the predefined filters to view solutions by area, or use the search box to find a specific solution by keyword. To explore learning materials (documentation, blogs, videos, and tutorials), select **Knowledge Center** in the **Resources** section.

![Screenshot of the Microsoft Purview portal solutions page showing core, risk and compliance, data governance, and data security sections.](media/purview-portal-solutions-page.png)

### Related portals

Access related portals and solutions to help you manage all aspects of data analytics, data privacy, user identity, and more in your organization. You can access the following management and resource portals by selecting **Solutions** &gt; **Related portals** in the left navigation:

- [Microsoft Defender](/en-us/defender/)
- [Microsoft Entra](/en-us/entra/fundamentals/whatis)
- [Microsoft Fabric](/en-us/fabric/get-started/microsoft-fabric-overview)
- [Microsoft Priva](/en-us/privacy/priva/priva-overview)
- [Microsoft Service Trust](/en-us/compliance/assurance/stp-get-started?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json)

### Compliance posture status

The **Compliance posture status** section includes cards that display summary information from the [Compliance Manager solution](compliance-manager) about your organization's compliance posture. The compliance posture percentages reflect progress toward completing the requirements of regulatory assessments. The **Posture breakdown** section highlights completion rates for your organization's top assessments and the services covered by the assessments. Select **Assess using Compliance Manager** or **Explore posture breakdown** to visit Compliance Manager, where you can view, add, and manage assessments.

![Screenshot of the Compliance posture status card in the Microsoft Purview portal showing assessment completion percentages and posture breakdown.](media/purview-portal-compliance-posture-status.png)

### Trials and recommendations

The **Trials and recommendations** card displays information and links to help you get started with trial solutions for specific Microsoft Purview solutions. Select **View all trials and recommendations** to discover more security and compliance capabilities in Microsoft Purview you can try for free.

![Screenshot of the Trials and recommendations card in the Microsoft Purview portal showing available trial solutions and recommended actions.](media/purview-portal-trials-recommendations.png)

### Knowledge Center

The **Knowledge Center** card highlights articles, product demos, tutorials, and other learning materials to help you succeed with Microsoft Purview. Select **Go to the Knowledge Center** to open the **Knowledge Center** page and view all available learning materials. Use the predefined filters to view knowledge center items by solution area, or use the search box to find a specific item by keyword.

![Screenshot of the Knowledge Center card in the Microsoft Purview portal showing articles, product demos, tutorials, and learning materials.](media/purview-portal-knowledge-center.png)

## New left navigation for solutions

When you select a Microsoft Purview solution in the portal, you see a solution-specific home page and a new left-navigation experience that lets you access all solution features, settings, and more. The new left-navigation displays links to the **Home**, **Solutions**, **Agents**, **Learn**, **Usage center**, and **Settings** pages for quick and easy access to these areas for managing solutions, learning more about Microsoft Purview, configuring solution settings, and more. Additionally, links to the five most recent Microsoft Purview solutions also display for quick access to these solutions.

![Screenshot of the Microsoft Purview portal left navigation showing links to Home, Solutions, Learn, Settings, and recent solutions.](media/purview-portal-left-navigation.png)

## Settings in the portal

Settings in the Microsoft Purview portal are now centralized in the portal. By selecting the **Settings** icon in the left navigation or at the top-right of the page, you can quickly manage solution and global portal-wide settings, no matter where you are in the portal.

![Screenshot of the Microsoft Purview portal settings pane showing centralized options for themes, language, time zone, password, and contact preferences.](media/purview-portal-settings.png)

To view and manage portal-wide settings, select options in the **Themes**, **Language and time zone**, **Password**, and **Contact preferences** sections.

To view and manage solution settings, select a solution. This action opens the settings page for the solution where you can update settings for the selected solution. From any solutions settings page, you can also select other Microsoft Purview solutions in the **Solution settings** area in the left navigation to view and update settings in these solutions. To view and manage account settings, select **Account**.

![Screenshot of the Microsoft Purview portal solution settings page showing configuration options for a selected solution.](media/purview-portal-solution-settings.png)

## Release notes and updates

View the latest release notes for Microsoft Purview solutions in a centralized location by selecting the **Release notes & updates** icon in the top right command bar. You can view [Message center](/en-us/microsoft-365/admin/manage/message-center?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json) announcements for solutions that give you a high-level overview of a planned update or change and how it might affect your users or organization. Select the associated **Learn more** link to view the announcement and more details on the Message Center.

Note

You must have the `microsoft.office365.messageCenter/messages/read` permission to view release notes in the Microsoft Purview portal. The [Message Center Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#message-center-reader), Global Reader, and Global Administrator roles include this permission. If you don't see an expected release note, check with your solution administrator or see [What's new in Microsoft Purview](whats-new).

## Help and support

Select the **Help** icon in the upper-right command bar to access specific help and support options for Microsoft Purview solutions:

- **Guided tours**: Start an integrated dialog-driven overview of key features and capabilities in the Microsoft Purview portal.
- **Knowledge Center**: Quickly access the Knowledge Center that contains highlighted articles, product demos, tutorials, and other learning materials to help you succeed with Microsoft Purview.
- **Need help?**: Select specific solution areas for self-help or share what you need help with so the right help and support can be provided.

For solution-specific help and support, select a specific solution in the drop-down field in the **Need help** section and select **Get help**. For example, if you need help with data loss prevention (DLP) policies, select *Data Loss Prevention*, and then select **Get help**. On the **Help** tab, enter the details for your help request.

![Screenshot of the Microsoft Purview portal help and support pane showing options for guided tours, Knowledge Center, and solution-specific help.](media/purview-portal-help-support.png)

Depending on your request, you see AI-generated guidance customized for your request and links to articles scoped to your request. If neither of these options helps resolve your questions, select **Contact support** to select email or telephone options to get support from a Microsoft agent.

Note

AI and article suggestions in help and support might not be available for some Microsoft Purview solutions. Check back frequently for updates about upcoming availability for these solutions in help and support.

## Submit feedback about the new portal

Select the **Feedback** icon in the upper-right command bar to provide your feedback to Microsoft about the new Microsoft Purview portal. Provide as much detail as you'd like, but don't include any private or sensitive information. After entering your feedback, select **Submit** to send your suggestions to Microsoft to help improve the portal experience.

## Get started with data governance solutions

Getting started with data governance solutions in the Microsoft Purview portal depends on your organization's current relationship with Microsoft Purview data governance solutions.

- If your organization didn't create a Microsoft Purview account in the Azure portal, read about the new experience for new customers.
- If your organization has Microsoft Purview accounts in the Azure portal, read about the new experience for existing data governance customers.

### New experience for new customers

If your organization doesn't have any Microsoft Purview accounts in any subscriptions under your Microsoft Entra tenant, you can get started with our governance solutions right away. Use the new [Microsoft Purview portal](https://purview.microsoft.com) to start your journey with the free version of Microsoft Purview.

#### Free version of Microsoft Purview data governance solutions

If you're new to Microsoft Purview data governance solutions, you can start in the [free version](data-governance-free-version) of Microsoft Purview. Because the free version has limited capabilities, use it only for initial evaluation, development, and test scenarios. To use the full capabilities of Microsoft Purview data governance, [upgrade to the enterprise version](data-governance-free-version-upgrade-to-enterprise).

Only a core subset of Microsoft Purview's governance solutions with limited capabilities are currently available in the free version:

- [Catalog](data-governance-free-version#catalog): Browse and search for your data assets.
- [Data Map history](data-map-history): A log of updates made to assets.

Currently, the free version of Microsoft Purview governance solutions supports these governance data sources using [live view](data-gov-live-view):

- Azure Blob Storage
- Azure Data Lake Storage Gen 2
- Azure SQL Database
- Azure subscriptions
- Microsoft Fabric

You can annotate and curate assets that are available via [live view](data-gov-live-view), or [use our APIs to create new entities](data-gov-api-create-assets).

Check out the [guide to getting started with the free version of Microsoft Purview data governance solutions](data-governance-free-version-get-started).

#### Enterprise version

When you [upgrade to the enterprise version of Microsoft Purview data governance](data-governance-free-version-upgrade-to-enterprise), you have access to all Microsoft Purview data governance features, including:

- [All data sources supported by Microsoft Purview data governance supported governance sources](data-map-data-sources): Manage data sources across your data estate.
- [Collections](data-map-collections-manage-classic): Manage fine grained access control for users across your environment.
- [Scanning](data-map-scan-data-sources): Gather your sources' technical metadata and lineage information.
- [Automatic classification](data-map-classification-apply-auto): Classify your data to identify important and sensitive information.
- [Data owner policies](concept-policies-data-owner): Govern data at the source from Microsoft Purview.
- [All reports](concept-policies-data-owner): Understand your data estate at a glance.
- [Workflows](concept-insights): Automate governance in your environment.

Learn more about [data governance in Microsoft Purview](data-governance-overview).

### New experience for existing data governance customers

The new experience enhances the current Microsoft Purview data governance experience. It doesn't affect the information already stored in your accounts or your ability to use the APIs. When you upgrade to the new experience, you automatically get the enterprise version of Microsoft Purview. The enterprise version has all the features you already use, plus these new features:

- [This new Microsoft Purview portal](purview-portal): the latest platform to manage your organization's data governance.
- [Live view](data-gov-live-view): view your Azure data assets in the Microsoft Purview Unified Catalog automatically and in real time with no need to register or set up a scan for the source.
- [Tenant-level administration](data-governance-roles-permissions): roles that give you the ability to delegate administration from the tenant level, while maintaining fine-grained access control options to limit permissions by role and collections. This feature gives your team flexibility when managing access and responsibilities.
- [Data Map history](data-map-history): a log of updates made to data assets, so you can audit changes in your Data Map.

For more information about the new experience, see [Guide to getting started with data governance in the new Microsoft Purview portal](data-governance-purview-portal#how-to-use-the-new-experience).