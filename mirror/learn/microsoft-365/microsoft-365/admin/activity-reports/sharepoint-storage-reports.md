---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: SharePoint Storage Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/sharepoint-storage-reports?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: cmcatee
author: cmcatee-MSFT
manager: scotv
ms.reviewer: hlu
audience: Admin
ms.topic: concept-article
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- M365-subscription-management
- Adm_O365
ms.custom:
- AdminTemplateSet
search.appverid:
- BCS160
- MST160
- MET150
- MOE150
ai-usage: ai-assisted
description: The SharePoint Storage report gives admins an overview of tenant usage, optimization tips, and growth trends. Discover how to view and interpret it today.
ms.date: 2026-06-11T00:00:00.0000000Z
locale: en-us
document_id: 97a609ae-db93-5282-f75a-8314ce273f92
document_version_independent_id: 97a609ae-db93-5282-f75a-8314ce273f92
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/sharepoint-storage-reports.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/sharepoint-storage-reports
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/sharepoint-storage-reports.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: fd33988c-29f6-7fa4-870f-5d6ac2b75eb2
---

# SharePoint Storage Report - Microsoft 365 admin | Microsoft Learn

The SharePoint Storage report provides an overview of your tenant's storage usage. It also offers suggestions for storage optimization and future proofing your organization's file growth capacity.

Use the SharePoint Storage report to quickly answer three admin questions:

- How much SharePoint storage is used, available, and allocated?
- How fast is storage growing over time?
- What actions should you take now to delay or plan additional storage purchase?

Note

This report is available to non-Education tenants. Education tenants should refer to their pooled storage report. For more information about viewing the pooled storage report, see [Pooled storage management](/en-us/microsoft-365/education/deploy/pooled-storage-management).

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the SharePoint Storage report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **SharePoint**.
5. On the report page, select the **Storage** tab.

## Interpret the SharePoint Storage report

This report refreshes every 48-72 hours. Banner notifications appear when SharePoint usage exceeds 80% of quota.

[![Screenshot of the SharePoint storage report   page.](../../media/usage-page.png)](../../media/usage-page.png#lightbox)

### Optimize your organization's SharePoint storage

Explore ways to manage your storage through setting file history limits, archiving inactive sites^1^, and creating site lifecycle management policies^1^. To increase SharePoint storage capacity, buy more storage in one-gigabyte increments. For more information about planning for SharePoint storage, see [SharePoint storage planning](/en-us/sharepoint/sharepoint-storage-planning).

^1^ Additional licensing charges might apply.

### Total usage

The **Total usage** chart shows the total storage used by your tenant, total storage quota, and available storage quota. For more information about SharePoint limits, see [SharePoint limits - Service Descriptions](/en-us/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits).

### Usage trend

The **Usage trend** report helps you understand your tenant's storage growth trend. Use the estimated future storage usage based on past usage to make informed decisions about when to buy more storage or whether to clean up usage.

Note

The historical trend represents usage across all sites and might slightly differ from the storage bar, which indicates tenant-level quota consumption.

### Featured resources

The **Featured resources** section provides information about options for managing storage, like [site storage limits](/en-us/sharepoint/manage-site-collection-storage-limits) and [version history limits](/en-us/sharepoint/document-library-version-history-limits). Consider using [Microsoft Graph Data connect](https://techcommunity.microsoft.com/blog/microsoft_graph_data_connect_for_sharepo/links-about-microsoft-graph-data-connect-for-sharepoint/4069045) for more in-depth SharePoint storage insights.

## Next actions

- [Plan storage growth](/en-us/sharepoint/sharepoint-storage-planning)
- [Set site storage limits](/en-us/sharepoint/manage-site-collection-storage-limits)
- [Set version history limits](/en-us/sharepoint/document-library-version-history-limits)