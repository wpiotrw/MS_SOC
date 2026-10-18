---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Troubleshooting Microsoft 365 support integration with ServiceNow - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/servicenow-troubleshooting?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2025-04-28T00:00:00.0000000Z
audience: Admin
ms.topic: troubleshooting-general
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_TOC
- operations-pod
ms.custom: AdminSurgePortfolio
ROBOTS: NOINDEX, NOFOLLOW
search.appverid:
- MET150
description: Scoped Certified application installation and configuration guide for ServiceNow.
locale: en-us
document_id: 9b7429b1-8300-c90e-ee52-39ef2584d103
document_version_independent_id: 9b7429b1-8300-c90e-ee52-39ef2584d103
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/servicenow-troubleshooting.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/servicenow-troubleshooting
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/servicenow-troubleshooting.md
platformId: 88ec0e3a-4cb6-c391-9d9b-873f9f77298f
---

# Troubleshooting Microsoft 365 support integration with ServiceNow - Microsoft 365 admin | Microsoft Learn

Important

Microsoft 365 support integration with ServiceNow is retired, and the service will be completely shut down on May 30, 2025. If you installed the integration, take necessary steps to remove it before May 30, 2025.

| # | Problem | Diagnostics action |
| --- | --- | --- |
| 1 | Can't see **Microsoft 365 support** tab | Verify the current view and **System Logs** &gt; **All** with filter x\_mioms\_m365\_assit |
| 2 | Select **Microsoft recommended solutions** but get error "Please contact your ServiceNow admin and ask them to complete the setup steps for the app." | Check the error message on top of the form and **System Logs** &gt; **All** with filter x\_mioms\_m365\_assit |
| 3 | Select **Microsoft recommended solutions** but get error "Please contact your ServiceNow admin and ask them to complete the final set up step for the app." | Check the error message on top of the form and **System Logs** &gt; **All** with filter x\_mioms\_m365\_assit |
| 4 | Type the problem in search box and select **Microsoft recommended solutions** but get error "Please contact your ServiceNow admin and ask them to complete the setup steps for the app." | Check the error message on top of the form and **System Logs** &gt; **All** with filter x\_mioms\_m365\_assit |
| 5 | Type problem in search box and select **Microsoft recommended solutions** but get error "Please contact your ServiceNow admin and ask them to complete the final set up step for the app." | Check the error message on top of the form and **System Logs** &gt; **All** with filter x\_mioms\_m365\_assit |
| 6 | Select **Contact Microsoft support**, but get the error "Please contact your ServiceNow admin and ask them to complete the setup steps for the app." | Check the error message on top of the form and **System Logs** &gt; **All** with filter x\_mioms\_m365\_assit |
| 7 | Select **Contact Microsoft support**, but get the error "Please contact your ServiceNow admin and ask them to complete the final set up step for the app." | Check the error message on top of the form and **System Logs** &gt; **All** with filter x\_mioms\_m365\_assit |
| 8 | Select **Contact Microsoft support** but get the error "{EmailAddress} is not a valid Microsoft 365 admin account. You need Microsoft 365 admin privileges to open a service request. In the app, link the admin account." | Check the error message on top of the form and **System Logs** &gt; **All** with filter x\_mioms\_m365\_assit |
| 9 | Select **Microsoft recommended solutions** but nothing shows up | Check **System Logs - Outbound HTTP logs** with filter login.microsoftonline.com and connector.rave.microsoft.com |
| 10 | Select **Microsoft recommended solutions** but get error "Please contact app support." | Check the error message on top of the form and **System Logs** &gt; **All** with filter x\_mioms\_m365\_assit |
| 11 | Type problem in search box and select **Microsoft recommended solutions** but nothing shows up | Check **System Logs - Outbound HTTP logs** with filter login.microsoftonline.com and connector.rave.microsoft.com |
| 12 | Type problem in search box and select **Microsoft recommended solutions** but get error "Please contact app support." | Check the error message on top of the form and **System Logs** &gt; **All** with filter x\_mioms\_m365\_assit |
| 13 | User selects **Contact Microsoft support**, but nothing happens | Check **System Logs - Outbound HTTP logs** with filter login.microsoftonline.com and connector.rave.microsoft.com |
| 14 | Can't see Microsoft recommended solution after reopening the incident | Check **System Logs** &gt; **All** with filter x\_mioms\_m365\_assit |
| 15 | Can't see Microsoft cases when reopening the incident that was transferred to Microsoft support | Check **System Logs** &gt; **All** with filter x\_mioms\_m365\_assit |
| 16 | Can't save ticket details, get error "Unable to save ticket details. Please contact App support." | Check the error message on top of form |