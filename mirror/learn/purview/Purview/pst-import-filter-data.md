---
layout: Conceptual
title: Filter data when importing PST files | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/pst-import-filter-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to filter data using the intelligent import feature in the Microsoft 365 import service when you import PST files to Microsoft 365.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-06T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-exchange-legacy
ms.collection:
- purview-compliance
- import
search.appverid:
- MOE150
- MET150
ai-usage: ai-assisted
locale: en-us
document_id: 2cbe77aa-aa5c-bd31-3f48-be2016f531ac
document_version_independent_id: 2cbe77aa-aa5c-bd31-3f48-be2016f531ac
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/pst-import-filter-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: pst-import-filter-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/pst-import-filter-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 66d63c34-b030-88e9-98d0-5ba65290bb00
---

# Filter data when importing PST files | Microsoft Learn

Note

This article explains how to filter PST data during import. Before using this feature, create a PST import job by using [network upload](pst-import-network-upload) or [drive shipping](pst-import-drive-shipping). For an overview of the PST import process, including requirements and limits, see [Learn about importing PST files](pst-import-overview).

Use the new Intelligent Import feature in the Microsoft 365 Import service to filter the items in PST files that you import to the target mailboxes. Complete the following steps. it works:

- After you create and submit a PST import job, the process uploads PST files to an Azure storage area in the Microsoft cloud.
- Microsoft 365 analyzes the data in the PST files in a safe and secure manner. It identifies the age of the mailbox items and the different message types included in the PST files.
- When the analysis is complete and the data is ready to import, you can import all data in the PST files as is or trim the data by setting filters that control what data gets imported. For example, you can Select to:

    - Import only items of a certain age.
    - Import selected message types.
    - Exclude messages sent or received by specific people.
- After you configure the filter settings, Microsoft 365 imports only the data that meets the filtering criteria to the target mailboxes specified in the import job.

The following graphic shows the Intelligent Import process, and highlights the tasks you perform and the tasks performed by Microsoft 365.

![The Intelligent Import process in Microsoft 365.](media/f2ec309b-11f5-48f2-939c-a6ff72152d14.png)

## Create a PST Import job

- The steps in this article assume that you created a PST import job in the Microsoft 365 Import service by using network upload or drive shipping. For step-by-step instructions, see one of the following articles:

    - [Use network upload to import PST files to Microsoft 365](pst-import-network-upload)
    - [Use drive shipping to import PST files to Microsoft 365](pst-import-drive-shipping)
- After you create an import job by using network upload, the status for the import job on the Import page in the Microsoft Purview portal is set to **Analysis in progress**, which means that Microsoft 365 is analyzing the data in the PST files that you uploaded. Select **Refresh**![refresh.](media/165fb3ad-38a8-4dd9-9e76-296aefd96334.png) to update the status for the import job.
- For drive shipping import jobs, Microsoft 365 analyzes the data after Microsoft datacenter personnel receive your hard drive and upload the PST files to the Azure storage area for your organization.
- For answers to common questions about importing PST files, see [FAQ about importing PST files](pst-import-faq).

## Filter data that gets imported to mailboxes

After you create a PST import job, Complete the following steps to filter the data before you import it to Microsoft 365.

1. Go to the Microsoft Purview portal and sign in by using the credentials for an administrator account in your organization.
2. In the left pane of the Microsoft Purview portal, select **Data lifecycle management** &gt; **Microsoft 365** &gt; **Import**.

    The **Import** tab lists the import jobs for your organization. The **Analysis completed** value in the **Status** column indicates the import jobs that Microsoft 365 analyzed and are ready for you to import.

    ![Analysis complete status indicates Microsoft 365 has analyzed the data in PST files.](media/de5294f4-f0ba-4b92-a48a-a4b32b6da490.png)
3. Select the import job that you want to complete and select **Import to Microsoft 365**.

    A flyout page is displayed with information about the PST files and other information about the import job.
4. Select **Import to Microsoft 365**.

    The **Filter your data** page is displayed. It contains data insights about the data in the PST files for the import job, including information about the age of the data.

    ![The Filter your data page shows data insights of the PST files for the import job.](media/3b537ec0-25a4-45a4-96d5-a429e2a33128.png)
5. Based on whether you want to trim the data that's imported to Microsoft 365, under **Do you want to filter your data?**, do one of the following steps:

    1. Select **Yes, I want to filter it before importing** to trim the data that you import, and then select **Next**.

    The **Import data to Microsoft 365 page** is displayed with detailed data insights from the analysis that Microsoft 365 performed.

    ![Microsoft 365 displays detailed data insights from its analysis of the PST files.](media/4881205f-0288-4c32-a440-37e2160295f2.png)

    The graph on this page shows the amount of data that you import. It displays information about each message type found in the PST files. You can hover the cursor over each bar to display specific information about that message type. There's also a drop-down list with different age values based on the analysis of the PST files. When you select an age in the drop-down list, the graph is updated to show how much data is imported for the selected age.

    1. To configure addition filters to reduce the amount of data that's imported, select **More filtering options**.

    ![Configure the filters on the More options page to trim the data that's imported.](media/3f8d68c3-3fe2-4b4e-9488-b368b98fa9fe.png)

    You can configure these filters:

    - **Age** - Select an age so only items that are newer than the specified age are imported. See the More information section for a description about how Microsoft 365 determines the age buckets for the **Age** filter.
    - **Type** - This section shows all the message types that Microsoft 365 found in the PST files for the import job. You can clear a check box next to a message type that you want to exclude. You can't exclude the Other message type. See the More information section for a list of mailbox items that are included in the Other category.
    - **Users** - You can exclude messages that are sent or received by specific people. To exclude people who appear in the From: field, To: field, or the Cc: field of messages, select **Exclude users** next to that recipient type. Type the email address (SMTP address) of the person, select **Add**![New icon.](media/457cd93f-22c2-4571-9f83-1b129bcfb58e.gif) to add them to the list of excluded users for that recipient type, and then select **Save** to save the list of excluded users.

        Note

        Microsoft 365 doesn't show data insights that result from setting the **People** filter. However, if you set this filter to exclude messages sent or received by specific people, those messages are excluded during the actual import process.

    1. Select **Apply** in the **More filtering options** flyout page to save your filter settings.

    The data insights on the **Import data to Microsoft 365** page are updated based on your filter settings, including the total amount of data that you import based on the filter settings. A summary of the filter settings is also shown. You can select **Edit** next to a filter to change the setting if necessary.

    ![The data insights are updated based on your filter settings.](media/897e20fb-3b13-44c3-9d56-9f330750f2a3.png)

    1. Select **Next**.

    A status page is displayed showing your filter settings. Again, you can edit any of the filter settings.

    1. Select **Import data** to start the import. The total amount of data that you import is displayed.

    Or

    1. Select **No, I want to import everything** to import all data in the PST files to Microsoft 365, and then select **Next**.
    2. On the **Import data to Microsoft 365** page, select **Import data** to start the import. The total amount of data that will be imported is displayed.
6. On the **Import** tab, select **Refresh**![refresh.](media/165fb3ad-38a8-4dd9-9e76-296aefd96334.png). The **Status** column displays the status for the import job.
7. Select the import job to display more detailed information, such as the status for each PST file and the filter settings that you configured.

## More information

- How does Microsoft 365 determine the increments for the age filter? When Microsoft 365 analyzes a PST file, it looks at the sent or received timestamp of each item. If an item has both a sent and received timestamp, Microsoft 365 selects the oldest date. Then Microsoft 365 looks at the year value for that timestamp and compares it to the current date to determine the age of the item. The software uses these ages as the values in the drop-down list for the **Age** filter. For example, if a PST file has messages from 2016, 2015, and 2014, the values in the **Age** filter are **1 year**, **2 years**, and **3 years**.
- The following table lists the message types that the **Other** category includes in the **Type** filter on the **More options** flyout page (see Step 5b in the previous procedure). Currently, you can't exclude items in the **Other** category when you import PSTs to Microsoft 365.

    | Message class ID | Mailbox items that use this message class |
    | --- | --- |
    | IPM.Activity | Journal entries |
    | IPM.Document | Documents and files (not attached to an email message) |
    | IPM.File | (same as IPM.Document) |
    | IPM.Note.IMC.Notification | Reports sent by Internet Mail Connect, which is the Exchange Server gateway to the Internet |
    | IPM.Note.Microsoft.Fax | Fax messages |
    | IPM.Note.Rules.Oof.Template.Microsoft | Out-of-office autoreply messages |
    | IPM.Note.Rules.ReplyTemplate.Microsoft | Replies sent by an inbox rule |
    | IPM.OLE.Class | Exceptions for a recurring series |
    | IPM.Recall.Report | Message recall reports |
    | IPM.Remote | Remote mail messages |
    | IPM.Report | Item status reports |