---
layout: Conceptual
title: Scan data sources in Microsoft Purview Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-scan-data-sources
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2024-06-13T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to scan registered data sources in the Microsoft Purview Data Map.
locale: en-us
document_id: 641fadab-5d52-8945-901a-baf0285eeabe
document_version_independent_id: 641fadab-5d52-8945-901a-baf0285eeabe
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-scan-data-sources.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-scan-data-sources
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-scan-data-sources.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: a4767f23-a02d-1e54-3b12-6c5ecc38c6ba
---

# Scan data sources in Microsoft Purview Data Map | Microsoft Learn

In Microsoft Purview, after you [register your data source](data-map-data-sources-register-manage#register-a-new-source), you can scan your source to capture technical metadata, extract schema, and apply classifications to your data.

- For more information about scanning, see [Scans and ingestion in Data Map](data-map-scan-ingestion).
- Review [scanning best practices](data-map-scanning-best-practices).

In this article, you learn the basic steps for scanning any data source.

Tip

Each source has its own instructions and prerequisites for scanning. For the most complete scanning instructions, select your source from the [supported sources list](data-map-data-sources) and review its scanning instructions.

## Prerequisites

Review the list of [sources that are available to register and scan in Microsoft Purview](data-map-data-sources).

Before you can scan your data source, complete these steps:

1. [Register your data source](data-map-data-sources-register-manage#register-a-new-source). This step essentially gives Microsoft Purview the address of your data source and maps it to a [collection or domain](data-map-domains-collections-manage) in Data Map.
2. Consider your network and [choose the right integration runtime configuration for your scenario](data-map-integration-runtime-choose).
3. Consider what credentials you use to connect to your source. All [source pages](data-map-data-sources) have a **Scan** section that includes details about what authentication types are available.

## Create a scan

In the following steps, use [Azure Blob Storage](register-scan-azure-blob-storage-source) as an example, and authenticate by using the Microsoft Purview Managed Identity.

Important

These steps describe how to create a scan. For source-specific prerequisites and scanning instructions, see [Data sources that connect to Data Map](data-map-data-sources).

1. Open the Microsoft Purview portal and go to **Data Map** &gt; **Data sources**. You can view your registered sources in either a map or table view.

    Tip

    If your Data Map has a large number of registered sources, the table view might perform better.
2. Find your source and select **New Scan**.
3. Enter a **Name** for the scan.
4. For **Credential**, select your authentication method.
5. Choose the current domain, collection, or a subcollection for the scan. The collection or domain you choose is where the scan stores the discovered metadata.

    Note

    The scan is always in the same domain as the registered source, but you can select a subcollection.
6. Select **Test connection**. If the connection is successful, select **Continue**. See troubleshooting if the connection isn't successful.
7. Depending on the source, you can scope your scan to a specific subset of data. For Azure Blob Storage, select folders and subfolders by choosing the appropriate items in the list.

    ![Screenshot showing the scope your scan window with files and folders selected.](media/scan-data-sources/register-blob-scope-scan.png)
8. Select a scan rule set. The scan rule set contains the kinds of [data classifications](data-map-classification) your scan checks. You can choose the system default (which contains all classifications available for the source), existing custom rule sets made by others in your organization, or [create a new rule set inline](data-map-scan-rule-set).

    Note

    You can only select the credentials and scan rule sets associated with the domain where you registered your source.
9. Choose your scan trigger. You can set up a schedule or run the scan once. Learn more about the supported schedule options.
10. Review your scan and select **Save and run**.

## Schedule a scan

When you set up the scan, choose to run it once or on demand, or set up a recurring schedule. You can configure the following schedule options:

- **Time zone**: Select the time zone you'd like to align your scan schedule with. If the time zone you select observes daylight savings, the trigger autoadjusts for the difference.
- **Recurrence**: Select a **daily**, **weekly**, or **monthly**scan recurrence.
    - **Daily recurrence**: Set recurrence to every X days, and specify the scan start time of the day.
    - **Weekly recurrence**: Set recurrence to every X weeks, select one or multiple days of the week, and specify the scan start time of the day.
    - **Monthly recurrence**: Set recurrence to every X months, choose between by month days or by weekdays, select one or multiple days or weekdays of the month, and specify the scan start time of the day.
- **Start recurrence at**: Set when the scan schedule begins.
- **Specify recurrence end date** (optional): If you want to stop the scan after a certain amount of time, enable this option by selecting the check box and provide an end date.

![Screenshot of the set a scan trigger page.](media/scan-data-sources/register-blob-scan-trigger.png)

## View a scan

Depending on the amount of data in your data source, a scan can take some time to run. Here's how you can check on progress and see results when the scan is complete.

1. You can view your scan from the collection, domain, or from the source itself.
2. To view from the collection or domain, go to your *Collection* or *Domain* in Data Map and select **Scans**.

    ![Screenshot of the collection page with the scans button highlighted.](media/scan-data-sources/select-scans.png)
3. Select your scan name to see details.

    ![Screenshot of the scans in the collection list with the most recent scan name highlighted.](media/scan-data-sources/select-scan-name.png)
4. Or, you can go directly to the *data source* in its *Collection* or *Domain* and select **View Details** to check the status of the scan.

    ![Screenshot of Data Map with a source's view details button highlighted.](media/scan-data-sources/register-blob-view-scan.png)
5. The scan details show the progress of the scan in the **Last run status** and the number of assets *scanned* and *classified*.

    ![Screenshot of a source detail page, with the assets and scans highlighted.](media/scan-data-sources/register-blob-scan-details.png)
6. The **Last run status** updates to **In progress** and then **Completed** once the entire scan runs successfully.

    ![Screenshot of a source detail page with a scan showing an in progress status.](media/scan-data-sources/register-blob-scan-in-progress.png)

    ![Screenshot of a source detail page with a scan showing a completed status.](media/scan-data-sources/register-blob-scan-completed.png)

## Manage a scan

After a scan finishes, you can manage it or run it again.

1. Select the **Scan name** from either the collections list or the source page to manage the scan.

    ![Screenshot of a source details page with the scan name link highlighted.](media/scan-data-sources/register-blob-manage-scan.png)
2. You can run the scan again, edit the scan, or delete the scan.

    ![Screenshot of a manage scan page with the run, edit, and delete buttons highlighted.](media/scan-data-sources/register-blob-manage-scan-options.png)
3. You can run a full scan, which scans all the content in your scope. Some sources also have an **Incremental scan** option. An **Incremental scan** scans only those resources that are updated since the last scan. Check the **supported capabilities** table in your source page to see if incremental scan is available for your source after the first scan.

    ![Screenshot of the run scan now button showing the full and incremental scan options.](media/scan-data-sources/register-blob-full-inc-scan.png)

## Troubleshooting

Setting up the connection for your scan can be complex, since it's a custom set up for your network and your credentials.

If you can't connect to your source, follow these steps:

1. Review your [source page](data-map-data-sources) prerequisites to make sure you didn't miss anything.
2. Review your authentication option in the **Scan** section of your source page to confirm you set up the authentication method correctly.
3. Review [troubleshoot connections](troubleshoot-connections).
4. [Create a support request](/en-us/azure/azure-portal/supportability/how-to-create-azure-support-request#go-to-help--support-from-the-global-header), so the support team can help you troubleshoot your specific environment.