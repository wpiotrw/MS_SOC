---
layout: Conceptual
title: View admin logs for data connectors | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-connector-admin-logs
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to access and view admin logs for data connectors to get status information for the data imported by the connector.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-03-26T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-connectors
ms.collection:
- purview-compliance
- data-connectors
search.appverid:
- MOE150
- MET150
ai-usage: ai-assisted
ms.custom: sfi-image-nochange
locale: en-us
document_id: cc438406-f659-f981-eb0c-0d97f0a2cfd2
document_version_independent_id: cc438406-f659-f981-eb0c-0d97f0a2cfd2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-connector-admin-logs.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-connector-admin-logs
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-connector-admin-logs.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: 6026989a-3373-58f3-62f7-df45bcee0549
---

# View admin logs for data connectors | Microsoft Learn

After you create a data connector to import non-Microsoft data to Microsoft Purview, you can monitor the daily import status of the connector by downloading the admin logs for the data connector.

## Before you view admin logs

Important

We highly recommended that you review admin logs daily to ensure any data ingestion failures caused by erroneous data or service issues are detected early and remediated. Without daily monitoring, you could end up with irreversible loss of data.

Before you can view admin logs, make sure that you've confirmed the following:

- Auditing must be enabled for your organization to generate and view admin log for your organization. Auditing is enabled by default in Microsoft Purview. However, verify the auditing status of your organization. For instructions, see [Verify the auditing status for your organization](audit-log-enable-disable#verify-the-auditing-status-for-your-organization). If you need to enable auditing for your organization, see [Turn on auditing](audit-log-enable-disable#turn-on-auditing).
- After auditing is turned on, it could take up to 48 hours to generate admin logs for data connectors. Enable auditing before you create data connectors.
- After a data connector is created, it can take up to 72 hours to generate admin logs that contain import status summary.
- Admin logs are available for the previous seven days.

## Download admin logs for data connectors

To download admin logs for date connectors, complete the following steps:

1. Sign into the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select the **My connectors** tab and then select a data connector to display the fly out page, which contains information and properties about the data connector.
4. Under **Admin logs**, select the **Download log** link to open an admin log.

    ![Admins logs displayed on the data connector flyout page.](media/data-connector-admin-logs1.png)
5. View the following import status information in the admin log:

    - **Import completion time**: timestamp (in UTC) when connector completes import from data source and all the below events are computed/updated against the import.
    - **Items available from source**: count of items downloaded by Connector from data source.
    - **Items available for import**: count of items available for import by Connector after fanout. Fanout represents the act of writing a message to all associated participants (sender, receiver etc.).
    - **Items imported successfully**: count of items imported successfully by Connector into user mailboxes after fanout.
    - **Items partially imported**: count of items imported successfully by Connector into user mailboxes after fanout but had attachments dropped.
    - **Items skipped**: count of items skipped from being imported into user mailboxes after fanout due to it being duplicate items.
    - **Items failed**: count of items that failed to be imported into user mailboxes after fanout due to it errors (like user mapping, item size exceeded etc.). Event is logged once per user for user mapping failures.

    Note

    Items available for import should be a sum of items imported successfully, partially imported, skipped, and failed.

    - Summary of Failed item details:
        - **Item ID**: unique identifier of the item
        - **Source User ID**: user ID at source application
        - **Microsoft 365 User ID**: User Principal Name in Microsoft 365
        - **Failure Reason**: indicates the reason why the connector couldn't import the item

    Note

    If no items are imported on a particular day, the admin log contains the following message: `No items ingested on mm/dd/yyyy.`

## Reingesting data after failures

Reingesting of data after failures is supported if completed within 90 days. To reingest data, select the **Help** icon in the [Microsoft Purview portal](purview-portal) to open a support case. Be prepared to provide all relevant logs to help troubleshoot any issues more quickly.