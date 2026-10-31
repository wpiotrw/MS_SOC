---
layout: Conceptual
title: Legacy eDiscovery tools retired | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-legacy-retirement
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn more about the retirement of eDiscovery tools or functionality and features that are no longer available.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: reference
ms.service: purview
ms.subservice: purview-ediscovery
search.appverid:
- MET150
ms.collection:
- purview-compliance
- ediscovery
ms.custom: admindeeplinkCOMPLIANCE
locale: en-us
document_id: c4e98d14-39d1-5861-cbe9-e744c63d1f67
document_version_independent_id: c4e98d14-39d1-5861-cbe9-e744c63d1f67
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-legacy-retirement.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-legacy-retirement
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-legacy-retirement.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 5af08ddb-604d-b1a0-1e9a-cdea76c2d331
---

# Legacy eDiscovery tools retired | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Important

The functionality of the legacy eDiscovery tools described in this article has either been removed from the Microsoft 365 service or is still available, but no longer supported. Any functionality that's still available may be removed without notice. If you're still using any of these legacy tools, consider migrating to the eDiscovery tools in the Microsoft Purview portal or one of the alternatives described in this article.

Over the years, Microsoft has provided eDiscovery tools that let you search, preview, and export email content from Exchange Online. However, these tools no longer offer an effective way to search for non-Exchange content in other Microsoft 365 services, such as SharePoint and Microsoft 365 Groups.

To address this, Microsoft offers other eDiscovery tools that help you search for a wide variety of Microsoft 365 content. And we've been working hard to incorporate the most current and powerful eDiscovery functionality in the [Microsoft Purview portal](https://go.microsoft.com/fwlink/p/?linkid=2077149). This allows organizations to respond to legal, internal, and other document requests for content across many Microsoft 365 services, including Exchange Online.

As a result of this new and improved eDiscovery functionality in the Microsoft Purview portal, the following eDiscovery-related features and functionality related to searching for email content in Exchange Online and Microsoft 365 are retired:

- [In-Place eDiscovery](/en-us/exchange/security-and-compliance/in-place-ediscovery/in-place-ediscovery) and [In-Place Holds](/en-us/exchange/security-and-compliance/create-or-remove-in-place-holds) in the Exchange admin center.
- The Exchange Online PowerShell cmdlets that support In-Place eDiscovery and In-Place Holds (these cmdlets are collectively identified as \**-MailboxSearch* cmdlets). This includes the following cmdlets:

    - [New-MailboxSearch](/en-us/powershell/module/exchange/new-mailboxsearch)
    - [Start-MailboxSearch](/en-us/powershell/module/exchange/start-mailboxsearch)
    - [Stop-MailboxSearch](/en-us/powershell/module/exchange/stop-mailboxsearch)
    - [Set-MailboxSearch](/en-us/powershell/module/exchange/set-mailboxsearch)

    Note

    The [Remove-MailboxSearch](/en-us/powershell/module/exchange/remove-mailboxsearch) cmdlet will be available after the other \****-MailboxSearch*** cmdlets are retired so that you can use it to help in your transition to other eDiscovery and hold tools. However, after a certain date (cited below) Microsoft Support will no longer supports this cmdlet.
- The [Search-Mailbox](/en-us/powershell/module/exchange/search-mailbox) cmdlet in Exchange Online PowerShell.
- The following operations in the Exchange Web Services API:

    - [GetSearchableMailboxes](/en-us/exchange/client-developer/web-service-reference/getsearchablemailboxes-operation)
    - [SearchMailboxes](/en-us/exchange/client-developer/web-service-reference/searchmailboxes-operation)
    - [SetHoldOnMailboxes](/en-us/exchange/client-developer/web-service-reference/setholdonmailboxes-operation)
    - [GetHoldOnMailboxes](/en-us/exchange/client-developer/web-service-reference/getholdonmailboxes-operation)
- [Microsoft Purview eDiscovery (Premium) v1.0](ediscovery-overview), which is the first version of eDiscovery (Premium) that's accessed through a Microsoft Purview eDiscovery (Standard) case in the Microsoft Purview portal. The retirement of eDiscovery (Premium) v1.0 doesn't impact your ability to create and manage eDiscovery (Standard) cases.

Note

The eDiscovery functionality being retired only applies to cloud-based versions of Microsoft 365 and Office 365. eDiscovery functionality in on-premises versions of Exchange and SharePoint will still be supported until further notice.

The following sections in this article provide guidance about each feature being retired. This information including timelines and alternative tools that you can use instead of the retired tool.

## In-Place eDiscovery and In-Place Holds in the Exchange admin center

As per the original announcement on July 1, 2017, the In-Place eDiscovery & Hold functionality in the Exchange admin center (EAC) is being retired. The In-Place eDiscovery & Holds page in the EAC allowed you to search, hold, and export content from Exchange Online. In-Place eDiscovery also let you copy search results to a discovery mailbox so that you or other eDiscovery managers could review content and make it available for legal, regulatory, and public requests.

Because all of these capabilities (except for copying search results to a discovery mailbox) are now available in the content search, eDiscovery and eDiscovery (Premium) tools in the [Micrsoft Purview portal](purview-portal) (with improved functionality, reliability, and support for a wide range of Microsoft 365 services), we recommend that you start using these tools as soon as possible. To help you in the transition to these other eDiscovery tools, the table below lists the tools you can use instead of In-Place eDiscovery and In-Place Hold.

Note

When migrating mailboxes from on-premises Exchange to Exchange Online, you need to create new holds in the Microsoft Purview portal for mailboxes with holds to preserve the data. Legacy holds in on-premises Exchange organizations aren’t migrated.

### Scope of affected organizations

- Office 365 and Microsoft 365 Enterprise organizations
- Office 365 and Microsoft 365 Education organizations
- Office 365 and Microsoft 365 Government organizations; this includes GCC, GCC High, and DoD
- Office 365 and Microsoft 365 operated by 21Vianet (China)
- Office 365 and Microsoft 365 Germany

### Timeline for retirement

- July 1, 2020: You won't be able to create new searches and holds, but you can still run, edit, and delete existing searches at your own risk. Microsoft Support will no longer In-Place eDiscovery & Holds in the EAC.
- October 1, 2020: The In-Place eDiscovery & Holds functionality in the EAC was placed in a read-only mode. This means you'll only be able to remove existing searches and holds.

### Alternative tools

The following table describes other tools that you can use to replace the existing functionality that's being retired.

| Functionality | Alternative tool | Comments |
| --- | --- | --- |
| Search, export, and hold for legal purposes | eDiscovery (Standard) cases in the Microsoft Purview portal | Using the capabilities of eDiscovery (Standard) cases provide the functional parity to In-Place eDiscovery and In-Place Holds. This includes the following:<br><br>- Search scales to millions of locations<br>- Higher reliability for searching, exporting, and placing content on hold<br>- Searching for content in for Exchange Online, SharePoint, OneDrive, Skype for Business, Microsoft Teams, Viva Engage Groups, Microsoft 365 Groups, and other content stored in Office 365 applications |
| Hold for retention purposes | Retention policies in the Microsoft Purview portal | You can use Retention policies to retain content and, if desired, delete it after the retention period expires. Other capabilities include:<br><br>- Applying policies to your entire organization<br>- Applying policies to specific content locations such as Exchange Online, SharePoint, OneDrive, Skype for Business, Microsoft Teams, and Office 365 Groups<br>- Applying policies to specific users<br><br><br>For more information, see [Learn about retention policies and retention labels](retention). |
| Copy email search results to a discovery mailbox for review | Review sets in eDiscovery (Premium) v2.0 | Reviewing content in Microsoft 365 has never been easier. Review sets have many great capabilities to help reduce the amount of time and data needed to review, including:<br><br>- Perform fast search queries and filter content in a review set<br>- Analyze content in a review set; this includes email threading, near-duplicate detection, Themes analysis, and Predictive coding<br>- Tag documents in a review set<br>- Tagging suggestions to help identify attorney client privilege content<br><br><br>For more information, see [Overview of the eDiscovery (Premium) solution in Microsoft 365](ediscovery-overview).<br><br>Alternatively, you can export search results to PST files and then use Microsoft 365 Import service to import the PSTs to a discovery mailbox. For step-by-step instruction, see [Use network upload to import PST files to Office 365](pst-import-network-upload). |
| Copy messages from one mailbox to a different mailbox | [Assign permissions to a mailbox](/en-us/exchange/recipients-in-exchange-online/manage-permissions-for-recipients) | To give a person access to another user's email (such as when an employee leaves your organization and you need to give another person access to the former employee's email), we recommended that you assign that person permissions to access the former employee's mailbox. So instead of copying mailbox items to another user mailbox or a shared mailbox, just assign a user the permissions necessary to access the source mailbox. |
| Restore items from the Recoverable Items folder | [Restore-RecoverableItems](/en-us/powershell/module/exchange/Restore-RecoverableItems) | You can restore permanently deleted items (also known as *soft-deleted* items) in mailboxes, as long as the deleted item retention period for an item hasn't expired. For more information, see [Recoverable Items folder in Exchange Online](/en-us/Exchange/security-and-compliance/recoverable-items-folder/recoverable-items-folder). |

### FAQs about In-Place eDiscovery and In-Place Holds

**I use the copy search results functionality of In-Place eDiscovery & Holds in the EAC to copy search results to a discovery mailbox for review by attorneys. What options do I have now?**

There are two ways to replicate this functionality today. The first is to use [review sets in eDiscovery (Premium) v2.0](ediscovery-view-documents-in-review-set). Review sets have many of the same capabilities you see in a traditional review tool like fast search of documents, tagging, email threading, near duplicate grouping, themes analysis, and predictive coding. If you still want to use discovery mailboxes for review, the second option is to export search results to PST files and then import the PST files to a discovery mailbox by using the [PST import feature](pst-import-network-upload) in the Microsoft compliance center.

**How do I control which content locations (such as mailboxes or sites) that can an eDiscovery manager can search using the new tools?**

The Microsoft Purview portal also uses [compliance boundaries](ediscovery-set-up-compliance-boundaries) to control which content locations an eDiscovery Manager can search. Compliance boundaries are useful in government entities that need to stay within agency boundaries or multi-national corporations required to respect geographical boarders.

## \*-MailboxSearch cmdlets

As per the original notice announced on July 1, 2017 in the Exchange admin center, the In-Place eDiscovery & Hold functionality and the corresponding **\*-MailboxSearch** cmdlets are being retired. These cmdlets provide users the ability to search, hold, and export mailbox content for legal, regulatory, and public requests.

Because these capabilities are now available in the [Microsoft Purview portal](purview-portal) and Office 365 Security & Compliance PowerShell with improved performance and scalability, you should using these improved cmdlets. These cmdlets include [\*-ComplianceCase](/en-us/powershell/module/exchange/get-compliancecase), [\*-ComplianceSearch](/en-us/powershell/module/exchange/get-compliancesearch), [\*-CaseHoldPolicy](/en-us/powershell/module/exchange/get-caseholdpolicy), [\*-CaseHoldRule](/en-us/powershell/module/exchange/get-caseholdrule), and [\*-ComplianceSearchAction](/en-us/powershell/module/exchange/get-compliancesearchaction).

### Scope of affected organizations

- Office 365 and Microsoft 365 Enterprise organizations
- Office 365 and Microsoft 365 Education organizations
- Office 365 and Microsoft 365 Government organizations; this includes GCC, GCC High, and DoD
- Office 365 and Microsoft 365 operated by 21Vianet (China)
- Office 365 Germany

### Timeline

- July 1, 2020: You won't be able to use **New-MailboxSearch** to create new In-Place eDiscovery searches and In-Place Holds, but you can still use cmdlets to run, edit, and delete existing searches and holds at your own risk. Microsoft Support will no longer provide assistance for these types of searches and holds.
- October 1, 2020: The In-Place eDiscovery & Holds functionality in the EAC was placed in a read-only mode. You won't be able to use the **New-MailboxSearch**, **Start-MailboxSearch**, or **Set-MailboxSearch** cmdlets. You'll only be able to get and remove existing searches and holds.

### Alternative tools

The following table describes other tools that you can use to replace the existing functionality that's being retired.

| Functionality | Alternative tools | Comments |
| --- | --- | --- |
| Search and export | [\*-ComplianceSearch](/en-us/powershell/module/exchange/get-compliancesearch)<br><br>[\*-ComplianceSearchAction](/en-us/powershell/module/exchange/get-compliancesearchaction)<br><br>[\*-ComplianceCase](/en-us/powershell/module/exchange/get-compliancecase) | The ComplianceSearch and ComplianceSearchAction cmdlets work together to help you search and export content. You can create a new search and view the search estimate by using the **New-**, **Get-**, and **Start-ComplianceSearch** cmdlets. Then you can use the **New-ComplianceSearchAction** cmdlet to export the search results. You'll still have to use the eDiscovery (Standard) tool in the Microsoft Purview portal to download those search results to your local computer.<br><br>**Note:** If you use these cmdlets to create searches that aren't associated with an eDiscovery (Standard) case, these searches will be located on the **Content search** page in the Microsoft Purview portal. |
| Hold content in a mailbox | [\*-CaseHoldPolicy](/en-us/powershell/module/exchange/get-caseholdpolicy)<br><br>[\*-CaseHoldRule](/en-us/powershell/module/exchange/get-caseholdrule)<br><br>[\*-ComplianceCase](/en-us/powershell/module/exchange/get-compliancecase) | Holds in the Microsoft Purview portal must be associated with a ComplianceCase. First, create the compliance case, and then create a CaseHoldPolicy and a CaseHoldRule.<br><br>**Note:** Creating a CaseHoldPolicy without a creating CaseHoldRule will render the hold inoperable until the CaseHoldRule is created and associated to the CaseHoldPolicy. See the cmdlet documentation for more information. |
| Copy search results to a discovery mailbox | None | There's no direct replacement for this functionality because it does not provide access to all Microsoft 365 services. See the following FAQ below for alternative solutions. |
| Copy messages from one mailbox to a different mailbox | [Assign permissions to a mailbox](/en-us/exchange/recipients-in-exchange-online/manage-permissions-for-recipients) | To give a person access to another user's email (such as when an employee leaves your organization and you need to give another person access to the former employee's email), we recommended that you assign that person permissions to access the former employee's mailbox. So instead of copying mailbox items to another user mailbox or a shared mailbox, just assign a user permissions to access the source mailbox. |

### FAQs about \***-MailboxSearch** cmdlets

**We use Copy Search to export email messages or instant Messages for purposes other eDiscovery and legal investigations. What other options do we have after these cmdlets are retired?**

The [Microsoft Graph APIs](https://developer.microsoft.com/en-us/graph) provide a number of methods for extracting data for analysis and other purposes that are far more resilient and scalable than the using the **\*-MailboxSearch** cmdlets.

**After the cmdlets are retired, will I still be able to remove or retrieve searches?**

Yes, although we're removing the ability to create and modify searches, you'll still be able to use the **Remove-MailboxSearch** until further notice. However, the use of this cmdlet will be at your own risk after the retirement dates and Microsoft Support will no longer be able to provide assistance.

## Search-Mailbox cmdlet

The **Search-Mailbox** cmdlet in Exchange Online PowerShell has been retired as originally announced in a warning in the cmdlet output starting back in 2018. The **Search-Mailbox** cmdlet was originally used to search a user's mailbox and purge malicious content. We recommend that you start using the **New-ComplianceSearch** and **New-ComplianceSearchAction** cmdlets in Office 365 Security & Compliance PowerShell to search for and purge content. For a built-in security experience, the [&lt;Microsoft 365 security features](/en-us/microsoft-365/security/) provide robust threat protection for email and many other Microsoft services.

### Scope of affected organizations

- Office 365 and Microsoft 365 Enterprise organizations
- Office 365 and Microsoft 365 Education organizations
- Office 365 and Microsoft 365 Government organizations; this includes GCC, GCC High, and DoD
- Office 365 and Microsoft 365 operated by 21Vianet (China)
- Office 365 Germany

### Timeline

April, 2024: The **Search-Mailbox** cmdlet is no longer be available and Microsoft Support will no longer provide assistance.

### Alternative tools

The following table describes other tools that you can use to replace the existing functionality that's being retired.

| Functionality | Alternative tools | Comments |
| --- | --- | --- |
| Search a mailbox | [\*-ComplianceSearch](/en-us/powershell/module/exchange/get-compliancesearch)<br><br>[\*-ComplianceSearchAction](/en-us/powershell/module/exchange/get-compliancesearchaction) | The ComplianceSearch and ComplianceSearchAction cmdlets work together to help you search content. You can create a new search and view the search estimate by using the **New-**, **Get-**, and **Start-ComplianceSearch** cmdlets. |
| Delete bulk email from a mailbox | [Set up an archive and deletion policy for mailboxes](set-up-an-archive-and-deletion-policy-for-mailboxes) | Admins can create an archiving and deletion policy that automatically moves items to a user's archive mailbox and automatically deletes items from the mailbox. |
| Copy search results to a discovery mailbox |  | There's no direct replacement for this functionality because it does not provide access to all Microsoft 365 services. See the FAQs in the **\*-MailboxSearch cmdlets** section for alternative solutions. |
| Copy messages from one mailbox to a different mailbox | [Assign permissions to a mailbox](/en-us/exchange/recipients-in-exchange-online/manage-permissions-for-recipients) | To give a person access to another user's email (such as when an employee leaves your organization and you need to give another person access to the former employee's email), we recommended that you assign that person permissions to access the former employee's mailbox. So instead of copying mailbox items to another user mailbox or a shared mailbox, just assign a user permission to access the source mailbox. |
| Purge messages from a mailbox | [\*-ComplianceSearch](/en-us/powershell/module/exchange/get-compliancesearch)<br><br>[\*-ComplianceSearchAction](/en-us/powershell/module/exchange/get-compliancesearchaction) | The ComplianceSearch and ComplianceSearchAction cmdlets work together to help you search and purge content. You can create and run a search with **New-ComplianceSearch** and **New-ComplianceSearch** cmdlets, and then you can purge the content by using **New-ComplianceSearchAction -Purge -PurgeType** command. For more information, see [Search for and delete messages](ediscovery-search-for-and-delete-email-messages). |
| Purge messages from a mailbox | [Assign permissions to a mailbox](/en-us/exchange/recipients-in-exchange-online/manage-permissions-for-recipients) | To purge messages from a mailbox, assign an administrator permissions to access the employee's mailbox. Messages can be deleted and recycled as needed taking advantage of the built-in search and viewing capabilities in Outlook. |

## Exchange Web Services API operations

These operations in the Exchange Web Services API are used by the In-Place eDiscovery & Holds feature in the Exchange admin center and the corresponding **\*-MailboxSearch** cmdlets in Exchange Online PowerShell. They will also be retired as part of retiring the other legacy eDiscovery tools.

### Scope of affected organizations

- Office 365 and Microsoft 365 Enterprise organizations
- Office 365 and Microsoft 365 Education organizations
- Office 365 and Microsoft 365 Government organizations; this includes GCC, GCC High, and DoD
- Office 365 Germany

### Timeline

July 1, 2020: The GetSearchableMailboxes, SearchMailboxes, SetHoldOnMailboxes, and GetHoldOnMailboxes operations will no longer be available, and Microsoft Support will no longer provide assistance.

## eDiscovery (Premium) v1.0

eDiscovery (Premium) v1.0, which is the version of eDiscovery (Premium) available in an eDiscovery (Standard) case by selecting **Switch to eDiscovery (Premium)**, is being retired. Its functionality has been replaced by the new [eDiscovery (Premium) solution](ediscovery) in the Microsoft Purview portal.

To determine if your organization is using eDiscovery (Premium) v1.0:

1. Go to the Microsoft Purview portal, select **eDiscovery (Standard)**, and open an eDiscovery (Standard) case.
2. If you see **Switch to eDiscovery (Premium)**, selecting it takes you to the 1.0 version of eDiscovery (Premium), which is being retired. The ability to create and manage cases in eDiscovery (Standard) won't be affected. Only the ability to add and analyze case data in eDiscovery (Premium) v1.0 (by selecting **Switch to eDiscovery (Premium)**) is being retired.

The new eDiscovery (Premium) solution in Microsoft 365 (also known as *eDiscovery (Premium) v2.0*) provides all of the capabilities of the original solution, but now includes a custodian-based approach of identifying content in other Microsoft 365 services, collecting that content, and then adding it to a review set where reviewers can take advantage of fast search queries, tagging, and analytics features to help cull relevant documents. eDiscovery (Premium) now includes improved processing and native viewers for both Microsoft and non-Microsoft file types, a full list of file types is [here](ediscovery-supported-file-types) and supported metadata fields are [here](ediscovery-document-metadata-fields). Also, the new eDiscovery (Premium) solution provides a powerful custodian holds management feature that lets you apply holds to content in different services, notify users of the holds, and track custodian responses, all within an eDiscovery (Premium) case.

To access eDiscovery (Premium) v2.0:

Go to the Microsoft Purview portal, select **eDiscovery** &gt; [**Advanced**](https://go.microsoft.com/fwlink/p/?linkid=2174006), and open an eDiscovery (Standard) case.

At this time, we recommend that you begin to transition your eDiscovery workflow to the new eDiscovery (Premium) functionality. If necessary, you can archive your eDiscovery (Premium) 1.0 cases by exporting the content and storing it offline. Although you'll still be able to access eDiscovery (Premium) v1.0 in existing cases until December 31, 2020, Microsoft Support won't provide support after October 1, 2020. See the following timeline for more details.

### Scope of affected organizations

- Office 365 and Microsoft 365 Enterprise organizations
- Office 365 and Microsoft 365 Education organizations
- Office 365 and Microsoft 365 Government organizations; this includes GCC, GCC High, and DoD
- Office 365 Germany

### Timeline

- July 1, 2020: You won't be able to create new eDiscovery (Premium) v1.0 cases.
- October 1, 2020: You won't be able to add new data (Prepare search results for eDiscovery (Premium)) to any cases. You'll be able to continue working with data in existing cases at your own risk. Microsoft Support will no longer provide assistance.
- December 31, 2020: You won't be able to access eDiscovery (Premium) v1.0 cases.

### Alternative tools

The [eDiscovery (Premium) solution](ediscovery-overview) in the Microsoft Purview portal.