---
layout: Conceptual
title: Use data connectors to import and archive third-party data in Microsoft 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-third-party-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to import and archive third-party data from social media platforms, instant messaging platforms, and document collaboration platforms to Microsoft 365 mailboxes.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-04T00:00:00.0000000Z
audience: Admin
ms.topic: overview
ms.service: purview
ms.subservice: purview-data-connectors
ms.collection:
- purview-compliance
- data-connectors
search.appverid:
- MOE150
- MET150
ai-usage: ai-assisted
locale: en-us
document_id: 970e71d0-4f67-71de-8605-d2695d5b0197
document_version_independent_id: 970e71d0-4f67-71de-8605-d2695d5b0197
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-third-party-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-third-party-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-third-party-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: d011e1b3-d7d5-486c-2186-f9345be7ef05
---

# Use data connectors to import and archive third-party data in Microsoft 365 | Microsoft Learn

Microsoft 365 lets administrators use data connectors to import and archive non-Microsoft, third-party data from social media platforms, instant messaging platforms, and document collaboration platforms, to mailboxes in your Microsoft 365 organization. One primary benefit of using data connectors to import and archive third-party data in Microsoft 365 is that you can apply various Microsoft Purview solutions to the data after you import it. This approach helps you ensure that your organization's non-Microsoft data complies with the regulations and standards that affect your organization.

This article describes the available third-party data connectors, the Microsoft Purview solutions that support imported third-party data, and how to provision a service principal for partner connectors.

## Third-party data connectors

The [Microsoft Purview portal](purview-portal) provides native third-party data connectors from Microsoft to import data from various data sources, such as LinkedIn, Instant Bloomberg, and Twitter. It also provides data connectors that support the Insider risk management solution.

In addition to these native data connectors, Microsoft works with the following partners to provide many more third-party data connectors in the Microsoft Purview portal. Your organization works with these partners to set up their archiving service before creating a corresponding data connector in the Microsoft Purview portal.

- TeleMessage
- 17a-4 LLC
- CellTrust

Important

All partner third-party data connector configurations require a provisioned [service principal](/en-us/entra/architecture/service-accounts-principal) for the partner application. This requirement isn't applicable for native Microsoft third-party data connector configurations.

To provision a service principal using PowerShell, see [Provision a service principal for partner third-party data connectors](archive-third-party-data#provision-a-service-principal-for-third-party-data-connectors).

The third-party data connectors described in this article (except for HR data and physical badging data that the Microsoft Purview Insider Risk Management solution uses) import into user mailboxes. The Microsoft Purview solutions that support third-party data apply to the user mailbox where the data is stored.

Important

All Veritas data connectors in Microsoft Purview were retired on June 30, 2024. Non-Veritas data connectors in your organization aren't affected by this change. Contact your Veritas account representative if you have questions about Veritas archiving services.

### Microsoft Purview data connectors

The following table lists the native third-party data connectors available in the Microsoft Purview portal. The table also summarizes the compliance solutions that you can apply after you import and archive third-party data in Microsoft 365. For a more detailed description of each compliance solution and how it supports third-party data, see the Overview of compliance solutions that support third-party data section.

Select the link in the **Third-party data** column to go to the step-by-step instructions for creating a connector for that data type.

| Third-party data | Litigation Hold | eDiscovery | Retention settings | Records management | Communication Compliance | Insider Risk Management |
| --- | --- | --- | --- | --- | --- | --- |
| [Anthropic Claude](manage-anthropic-data) |  |  |  |  |  |  |
| [Bloomberg Message](archive-bloomberg-message-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [ChatGPT Enterprise AI interactions](archive-chatgpt-interactions) |  | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |
| [Facebook](archive-facebook-data-with-sample-connector) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Generic EHR healthcare](import-healthcare-data) |  |  |  |  |  | ![Check mark.](media/check-mark.png) |
| [Human resources (HR)](import-hr-data) |  |  |  |  |  | ![Check mark.](media/check-mark.png) |
| [ICE Chat](archive-icechat-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Instant Bloomberg](archive-instant-bloomberg-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [LinkedIn](archive-linkedin-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |  |
| [Physical badging](import-physical-badging-data) |  |  |  |  |  | ![Check mark.](media/check-mark.png) |
| [Third-party insider risk detections (preview)](import-insider-risk-indicators) |  |  |  |  |  | ![Check mark.](media/check-mark.png) |
| [Twitter](archive-twitter-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |  |

### TeleMessage data connectors

Important

All partner third-party data connector configurations require a provisioned [service principal](/en-us/entra/architecture/service-accounts-principal) for the partner application. This requirement isn't applicable for native Microsoft third-party data connector configurations.

To provision a service principal using PowerShell, see [Provision a service principal for partner third-party data connectors](archive-third-party-data#provision-a-service-principal-for-third-party-data-connectors).

The following table lists the third-party data connectors available through the partnership with TeleMessage. The table also summarizes the compliance solutions you can apply to third-party data after you import and archive it in Microsoft 365. For more information about each compliance solution and how it supports third-party data, see the Overview of compliance solutions that support third-party data section.

Before you can archive third-party data in Microsoft 365, you need to work with TeleMessage to set up their archiving service for your organization. For more information, select the link in the **Third-party data** column to go to the step-by-step instructions for creating a connector for that data type.

You can also use TeleMessage data connectors in GCC environments in the Microsoft 365 US Government cloud. For more information, see the Data connectors in the US Government cloud section in this article.

| Third-party data | Litigation Hold | eDiscovery | Retention settings | Records management | Communication Compliance | Insider Risk Management |
| --- | --- | --- | --- | --- | --- | --- |
| [Android](archive-android-archiver-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [AT&T Network](archive-att-network-archiver-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Bell Network](archive-bell-network-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Enterprise Number](archive-enterprise-number-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Hong Kong CSL Network](archive-hk-csl-sms-mms-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [O2 Network](archive-o2-network-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Rogers Network](archive-rogers-network-archiver-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Signal](archive-signal-archiver-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [T-Mobile](archive-t-mobile-sms-mms-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Telegram](archive-telegram-archiver-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [TELUS Network](archive-telus-network-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Verizon Network](archive-verizon-network-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [WeChat](archive-wechat-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [WhatsApp](archive-whatsapp-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |

### 17a-4 data connectors

Important

All partner third-party data connector configurations require a provisioned [service principal](/en-us/entra/architecture/service-accounts-principal) for the partner application. This requirement isn't applicable for native Microsoft third-party data connector configurations.

To provision a service principal using PowerShell, see [Provision a service principal for partner third-party data connectors](archive-third-party-data#provision-a-service-principal-for-third-party-data-connectors).

The following table lists the third-party data connectors available through a partnership with 17a-4 LLC. The table also summarizes the compliance solutions you can apply to third-party data after you import and archive it in Microsoft 365. For a detailed description of each compliance solution and how it supports third-party data, see the Overview of compliance solutions that support third-party data section.

Before you can archive third-party data in Microsoft 365, you need to work with 17a-4 LLC to set up their archiving service (called *DataParser*) for your organization. For more information, select the link in the **Third-party data** column to go to the step-by-step instructions for creating a connector for that data type.

You can also use 17a-4 data connectors in GCC environments in the Microsoft 365 US Government cloud. For more information, see the Data connectors in the US Government cloud section in this article.

| Third-party data | Litigation Hold | eDiscovery | Retention settings | Records management | Communication Compliance | Insider Risk Management |
| --- | --- | --- | --- | --- | --- | --- |
| [BlackBerry](archive-17a-4-blackberry-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Bloomberg](archive-17a-4-bloomberg-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Cisco Jabber](archive-17a-4-cisco-jabber-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Cisco Webex](archive-17a-4-webex-teams-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [FactSet](archive-17a-4-factset-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Fuze](archive-17a-4-fuze-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [FX Connect](archive-17a-4-fxconnect-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [ICE Chat](archive-17a-4-ice-im-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [InvestEdge](archive-17a-4-investedge-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [LivePerson Conversational Cloud](archive-17a-4-liveperson-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Quip](archive-17a-4-quip-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Refinitiv Eikon Messenger](archive-17a-4-refinitiv-messenger-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [ServiceNow](archive-17a-4-servicenow-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Skype for Business Server](archive-17a-4-skype-for-business-server-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Slack](archive-17a-4-slack-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [SQL](archive-17a-4-sql-database-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Symphony](archive-17a-4-symphony-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |
| [Zoom](archive-17a-4-zoom-data) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |

### CellTrust data connectors

Important

All partner third-party data connector configurations require a provisioned [service principal](/en-us/entra/architecture/service-accounts-principal) for the partner application. This requirement isn't applicable for native Microsoft third-party data connector configurations.

To provision a service principal using PowerShell, see [Provision a service principal for partner third-party data connectors](archive-third-party-data#provision-a-service-principal-for-third-party-data-connectors).

The following table lists the third-party data connector available through a partnership with CellTrust. The table also summarizes the compliance solutions you can apply to third-party data after you import and archive it in Microsoft 365. For a more detailed description of each compliance solution and how it supports third-party data, see the Overview of compliance solutions that support third-party data section.

Before you can archive third-party data in Microsoft 365, you need to work with CellTrust to set up their archiving service, *CellTrust SL2*, for your organization. For more information, select the link in the **Third-party data** column to go to the step-by-step instructions for creating a CellTrust SL2 connector.

| Third-party data | Litigation Hold | eDiscovery | Retention settings | Records management | Communication Compliance | Insider Risk Management |
| --- | --- | --- | --- | --- | --- | --- |
| [CellTrust SL2](archive-data-from-celltrustsl2) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) | ![Check mark.](media/check-mark.png) |  |

The CellTrust SL2 data connector is also available in GCC environments in the Microsoft 365 US Government cloud. For more information, see the Data connectors in the US Government cloud section in this article.

### Provision a service principal for third-party data connectors

For partner third-party data connectors, you must configure a service principal. Before you begin, confirm the [Azure CLI](/en-us/cli/azure/install-azure-cli) is installed on your computer.

Complete the following steps to configure a service principal for your organization:

1. Open PowerShell and verify the Azure CLI installation:

    ```powershell
    az version
    ```
2. Sign in with the administrator account for your organization:

    ```powershell
    az login
    ```
3. Run the following cmdlet to create the service principal for your organization. Replace `<PartnerAppId>` with the application ID provided by the partner (TeleMessage, 17a-4 LLC, or CellTrust):

    ```powershell
    az ad sp create --id <PartnerAppId>
    ```

## Overview of Microsoft Purview solutions that support third-party data

The following sections describe how Microsoft Purview solutions help you manage imported third-party data, including Communication Compliance, eDiscovery, Insider Risk Management, Litigation Hold, Records management, and Retention settings.

### Communication Compliance

Use [Microsoft Purview Communication Compliance](communication-compliance) to examine third-party data to make sure it complies with your organization's data standards. You can detect, capture, and take remediation actions for inappropriate messages in your organization. For example, you can monitor the third-party data that you import for offensive language, sensitive information, and regulatory compliance.

### eDiscovery

[Microsoft Purview eDiscovery](edisc) is the primary legal investigation tool in Microsoft 365. Use eDiscovery to add custodians to a case, place a custodian's data on hold, and load a custodian's third-party data into a review set for further analysis such as themes and duplicate detection. After you load third-party data into a review set, you can query and filter it to a narrow result set. Use eDiscovery to manage third-party data that might be relevant to your organization's legal or internal investigations.

You can also use eDiscovery to search for and create query-based holds to preserve third-party data. To search for third-party data imported to user mailboxes, use the `kind:externaldata` property in your search query. To search for a specific type of third-party data, use the `itemclass:ipm.externaldata.<third-party data type>` mailbox property. For more information, see [Find content in mailboxes](edisc-search-mailboxes) and [Use Keyword Query Language to create search queries](edisc-keyword-query-language).

### Insider Risk Management

By using signals from third-party data, such as selective HR data, [Microsoft Purview Insider Risk Management](insider-risk-management) helps you minimize internal risks by detecting, investigating, and acting on risky activities in your organization. For example, data imported by the HR data connector is used as risk indicators to help detect departing user data theft. The healthcare data connector supports risk indicators for patient data misuse, and the third-party insider risk detections connector lets you extend detections to non-Microsoft workloads.

### Litigation Hold

Place a [Litigation Hold](/en-us/exchange/policy-and-compliance/holds/litigation-holds?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) on a user mailbox to retain third-party data. When you create a hold, specify a hold duration (also called a *time-based hold*) so that deleted and modified third-party data is retained for a specified period and then permanently deleted from the mailbox. Or retain content indefinitely (called an *infinite hold*) or until the Litigation Hold is removed.

### Records management

The [Microsoft Purview Records Management](records-management) solution lets you declare third-party data as a record. Users can manually apply a retention label that marks third-party data in their mailbox as a record. Or you can auto-apply retention labels by identifying sensitive information, keywords, or content types in third-party data.

### Retention settings

Apply a [retention policy](retention) to user mailboxes to retain and then delete third-party data (and other mailbox content) after the retention period expires. Use retention policies to delete third-party data of a certain age or [use retention labels to trigger a disposition review](disposition) when the retention period for third-party data expires.

## Data connectors in the US Government cloud

Some data connectors are available in the US Government cloud. The following tables show the specific government environments that support third-party data connectors. For more information about US Government clouds, see [Microsoft 365 US Government](/en-us/office365/servicedescriptions/office-365-platform-service-description/office-365-us-government/microsoft-365-government-how-to-buy?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

### Microsoft data connectors in the US Government cloud

The following table lists Microsoft data connectors available in US Government cloud environments.

| Data connector | GCC | GCC High | DoD |
| --- | --- | --- | --- |
| [Human resources (HR)](import-hr-data-us-government) | Yes | Yes | Yes |

### TeleMessage data connectors in the US Government cloud

The following table lists TeleMessage data connectors available in US Government cloud environments.

| Data connector | GCC | GCC High | DoD |
| --- | --- | --- | --- |
| Android Archiver | Yes | No | No |
| AT&T SMS/MMS Network Archiver | Yes | No | No |
| Bell SMS/MMS Network Archiver | Yes | No | No |
| Enterprise Number Archiver | Yes | No | No |
| O2 SMS and Voice Network Archiver | Yes | No | No |
| Rogers Network Archiver | Yes | No | No |
| Signal Archiver | Yes | No | No |
| Telegram Archiver | Yes | No | No |
| TELUS SMS Network Archiver | Yes | No | No |
| Verizon SMS/MMS Network Archiver | Yes | No | No |
| WeChat Archiver | Yes | No | No |
| WhatsApp Archiver | Yes | No | No |

### 17a-4 data connectors in the US Government cloud

The following table lists 17a-4 data connectors available in US Government cloud environments.

| Data connector | GCC | GCC High | DoD |
| --- | --- | --- | --- |
| BlackBerry DataParser | Yes | No | No |
| Bloomberg DataParser | Yes | No | No |
| Cisco Jabber DataParser | Yes | No | No |
| Cisco Webex DataParser | Yes | No | No |
| FactSet DataParser | Yes | No | No |
| Fuze DataParser | Yes | No | No |
| FX Connect DataParser | Yes | No | No |
| ICE DataParser | Yes | No | No |
| InvestEdge DataParser | Yes | No | No |
| LivePerson Conversational Cloud DataParser | Yes | No | No |
| Quip DataParser | Yes | No | No |
| Refinitiv Eikon Messenger DataParser | Yes | No | No |
| ServiceNow DataParser | Yes | No | No |
| Skype for Business Server DataParser | Yes | No | No |
| Slack DataParser | Yes | No | No |
| SQL DataParser | Yes | No | No |
| Symphony DataParser | Yes | No | No |
| Zoom DataParser | Yes | No | No |

### CellTrust data connectors in the US Government cloud

The following table lists CellTrust data connector availability in US Government cloud environments.

| Data connector | GCC | GCC High | DoD |
| --- | --- | --- | --- |
| CellTrust SL2 | Yes | No | No |