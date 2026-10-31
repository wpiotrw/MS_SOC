---
layout: Conceptual
title: Import custodians to an eDiscovery (Premium) case | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-bulk-add-custodians
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use the bulk-import tool to quickly add multiple custodians and their associated data sources to a case in Microsoft Purview eDiscovery (Premium).
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
ms.custom: sfi-image-nochange
locale: en-us
document_id: 0056badf-abe0-2fe9-de63-619424e38005
document_version_independent_id: 0056badf-abe0-2fe9-de63-619424e38005
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-bulk-add-custodians.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-bulk-add-custodians
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-bulk-add-custodians.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: cfa9b74f-6bdc-9bb4-ff7a-93305e26c193
---

# Import custodians to an eDiscovery (Premium) case | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

For Microsoft Purview eDiscovery (Premium) cases that involve many custodians, you can import multiple custodians at once by using a CSV file that contains the information necessary to add them to a case. The import custodians tool will also validate the CSV file before the import job is created. This means you can fix any errors in the CSV file instead of having to wait until the import job is complete before learning there are errors that prevent a custodian from being added to the case.

## Before you import custodians

- You can import a maximum of 1,000 custodians (rows) per CSV file. Note that importing 1,000 custodians at the same time might result in timeout errors and some custodians might fail the import. To remediate this, repeat the import and the failed custodians should be imported. To avoid timeouts we recommend importing 200 custodians at a time.
- You can associate up to 500 data sources for each custodian.
- You can only import custodians that are part of your organization's Microsoft Entra ID.
- Each custodian must have a unique email address.
- To import an inactive mailbox as a custodian or to associate an inactive mailbox with another custodian, add a "." prefix to the email address of the inactive mailbox (for example, .sarad@contoso.onmmicrosoft.com).

## Import custodians

1. Open the eDiscovery (Premium) case and select the **Data sources** tab.
2. Select **Add data source** &gt; **Import custodians**.
3. On the **Get template** workflow page, select **Download the CSV template** to download a custodian template CSV file.

    ![Download a CSV template from Import custodians flyout page.](media/importcustodians1.png)
4. Add the custodial information to the CSV file and save it to your local computer. See the Custodian CSV file section for detailed information about the required properties in the CSV file.
5. After you've prepared the CSV file with the custodian information, go back to the **Data sources** tab, and select **Add data source** &gt; **Import custodians** again.
6. On the **Upload CSV file** workflow page, select **Upload csv file** and then upload the CSV file that contains the custodian information.

    After you upload the CSV file, the import workflow validates the CSV file. If any validation errors exist, the workflow displays an error banner with a link to view the errors.

    ![Validation error banner with link to more information.](media/importcustodians2.png)

    The error information identifies the row and column of the cell that contains the error, and suggests a remediation action. You have to fix any validation error and then reupload the fixed CSV file. The CSV file must be successfully validated before you can create the import custodian job.
7. Once the CSV file has been successfully validated, select **Next** and then select **Import** to start the import job.

After you start the import job, eDiscovery (Premium) does the following things:

- Creates a job named *Import custodians* on the **Jobs** tab of the case. You can select the *Import custodians* job on the **Jobs** tab to view the status and details of the import custodian job under the **Support information** section. For more information, see [Manage jobs](ediscovery-managing-jobs).
- Performs Advanced indexing of all data sources for each custodian.
- Places all custodian data sources on hold (if the **Is OnHold** property in the CSV file is set to TRUE)

When the import custodian job is complete, the custodians and their associated data sources are added to the **Data sources** page of the case.

## Custodian CSV file

After you download the CSV custodian template, you can add custodians and their data sources in each row. Be sure not to change the column names in the header row. Use the workload type and workload location columns to associate other data sources to a custodian.

| **Column name** | **Description** |
| --- | --- |
| **Custodian contactEmail** | The custodian's UPN email address. For example, sarad@contoso.onmicrosoft.com. |
| **Exchange Enabled** | TRUE/FALSE value to include or not include the custodian's mailbox. |
| **OneDrive Enabled** | TRUE/FALSE value to include or not include the custodian's OneDrive for Business account. |
| **Is OnHold** | TRUE/FALSE value to indicate whether to place the custodian data sources on hold. ^1^ |
| **Workload1 Type** | String value indicating the type of data source to associate with the custodian. Possible values include: - ExchangeMailbox - SharePointSite- TeamsMailbox^2^- Viva EngageMailbox^2^. The previous values for these workload types are case sensitive. The CSV file contains columns for three workload types and their corresponding workload locations. You can add a total of 500 workload types and locations. |
| **Workload1 Location** | Depending on your workload type, this would be the location of the data source. For example, the email address for an Exchange mailbox or the URL for a SharePoint site. |
|  |  |

Note

^1^ If you put more than 1,000 mailboxes or 100 sites on hold in a case, the system will automatically scale the eDiscovery hold as needed. This means the system automatically adds data locations to multiple hold policies, instead of adding them to a single policy. However, the limit of 10,000 case hold policies per organization still applies. For more information about hold limits, see [Limits in eDiscovery (Premium)](ediscovery-premium-limits#hold-limits).

^2^ When you include TeamsMailbox and Viva EngageMailbox workloads in the CSV file, the group site (TeamSite and Viva EngageSite) are automatically added by default. You don't need to specify TeamsSite and Viva EngageSite separately in the CSV file.

Here's an example of a CSV file with custodian information:

| **Custodian contactEmail** | **Exchange Enabled** | **OneDrive Enabled** | **Is OnHold** | **Workload1 Type** | **Workload1 Location** |
| --- | --- | --- | --- | --- | --- |
| robinc@contoso.onmicrosoft.com | TRUE | TRUE | TRUE | SharePointSite | `https://contoso.sharepoint.com` |
| pillarp@contoso.onmicrosoft.com | TRUE | TRUE | TRUE |  |  |
| johnj@contoso.onmicrosoft.com | TRUE | TRUE | TRUE |  |  |
| sarad@contoso.onmicrosoft.com | TRUE | TRUE | TRUE | ExchangeMailbox | .saradavis@contoso.onmicrosoft.com |
|  |  |  |  |  |  |

Note

As previously explained, add a "." prefix to the UPN address of an inactive mailbox to import an inactive mailbox as a custodian or to associate an inactive mailbox with another custodian.

## Retry hold action

Once a custodian is placed on hold, you can validate the status in the **Hold** column of the list page. If the hold status isn't equal to *True* (when hold is enabled) or *False* (when hold is disabled), you can multi-select the relevant custodians and select *Retry hold action* at the top of the page. *Retry hold action* is only available for custodial sources and when multiple custodians are selected. If *Retry hold action* is performed for data sources succesfully placed or released from hold, no action is triggered. For more information about managing holds, see [Manage holds in eDiscovery (Premium)](ediscovery-managing-holds).