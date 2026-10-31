---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft 365 for business security best practices - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-security-best-practices?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- CSH
ms.author: vpattnaik
author: vpattnai
manager: dansimp
audience: Admin
ms.topic: reference
ms.service: m365-core
ms.subservice: security
ms.date: 2025-08-14T00:00:00.0000000Z
ms.localizationpriority: medium
ms.collection:
- highpri
- m365-security
- tier2
- ContentEnagagementFY23
- essentials-security
- trust-pod
search.appverid:
- BCS160
- MET150
- MOE150
description: Learn best practices to protect your data using Microsoft 365 Business Basic, Standard, or Premium. Protect devices, email, files, and accounts.
ms.custom: security
locale: en-us
document_id: 6368ffef-d605-5982-1321-980ff56804c6
document_version_independent_id: 6368ffef-d605-5982-1321-980ff56804c6
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/security-and-compliance/m365b-security-best-practices.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/security-and-compliance/m365b-security-best-practices
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/security-and-compliance/m365b-security-best-practices.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/82f69bd7-5cb0-4163-9fd6-9103bb1a8352
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f003597a-dab2-429a-8639-1d2acd9c0371
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: d095ea79-3c55-1fd0-b0a0-d0215fb9280e
---

# Microsoft 365 for business security best practices - Microsoft 365 admin | Microsoft Learn

Tip

**This article is for small and medium sized businesses with up to 300 users**.

If you're looking for information for enterprise organizations, see [Deploy ransomware protection for your Microsoft 365 organization](/en-us/previous-versions/microsoft-365/solutions/ransomware-protection-microsoft-365).

If you're a Microsoft partner, see [Resources for Microsoft partners working with small and medium-sized businesses](/en-us/defender-business/mdb-partners).

Microsoft 365 for business, which includes Microsoft 365 Business Basic, Microsoft 365 Business Standard, and Microsoft 365 Business Premium, includes anti-phishing, anti-spam, and anti-malware protection for email. Microsoft 365 Business Premium includes even more security capabilities, such as advanced cybersecurity protection for:

- Devices (computers, tablets, and phones; also known as *endpoints*)
- Email & collaboration content (for example, Office documents)
- Data (encryption, sensitivity labels, and Data Loss Prevention or DLP)

This article describes the top 10 ways to secure your business data with Microsoft 365 for business. For more information about what each plan includes, see [Microsoft 365 for Businesses](https://www.microsoft.com/microsoft-365/business).

## Top 10 ways to secure your business data

[![Diagram listing the top 10 ways to secure business data with Microsoft 365 for business.](../../media/top-10-ways-to-secure-data.png)](../../media/top-10-ways-to-secure-data.png#lightbox)

The following table summarizes how to secure your data using Microsoft 365 for business.

| Best practices and capabilities | BusinessBasic | BusinessStandard | BusinessPremium |
| --- | --- | --- | --- |
| **1. Use multi-factor authentication** (MFA), also known as two-step verification: |  |  |  |
| [Security defaults](set-up-multi-factor-authentication#manage-security-defaults) is on by default and is suitable for most organizations. | ✔ | ✔ | ✔ |
| Use [Conditional Access](set-up-multi-factor-authentication#manage-conditional-access-policies) for more stringent requirements. |  |  | ✔ |
| **2. Protect admin accounts**. See [Admin account security in Microsoft 365 for business](m365b-account-security-admins). | ✔ | ✔ | ✔ |
| **3. Use preset security policies**. See [Preset security policies in cloud organizations](/en-us/defender-office-365/preset-security-policies) and [Determine your threat policy strategy](/en-us/defender-office-365/mdo-deployment-guide#determine-your-threat-policy-strategy). |  |  |  |
| [Built-in security features for all cloud mailboxes](/en-us/defender-office-365/eop-about). Includes: Anti-spam, anti-malware, and anti-phishing (spoof) protection. | ✔ | ✔ | ✔ |
| [Microsoft Defender for Office 365 Plan 1](/en-us/defender-office-365/mdo-about#defender-for-office-365-plan-1-capabilities) protection. Includes: Extra anti-phishing protection features (impersonation protection and anti-phishing thresholds), Safe Links (email, Office apps, and Microsoft Teams), and Safe Attachments (email and files in SharePoint, OneDrive, and Microsoft Teams) |  |  | ✔ |
| **4. Protect all devices** that access company data, including personal and company devices: |  |  |  |
| [Basic Mobility and Security](m365b-devices-basic-mobility-security-overview) (provides mobile device management or MDM) | ✔ | ✔ | ✔ |
| [Microsoft Intune Plan 1](m365bp-devices-enrollment) (provides MDM *and* mobile app management or MAM) |  |  | ✔ |
| [Device protection policies in Microsoft Defender for Business and Microsoft Intune](m365bp-devices-protection) |  |  | ✔ |
| **5. Use email securely** |  |  |  |
| [Protect yourself against phishing and other attacks](m365b-users-phishing-spam-malware). | ✔ | ✔ | ✔ |
| Use [Microsoft Purview Message Encryption](/en-us/purview/email-encryption) automatically with [Exchange mail flow rules](/en-us/purview/define-mail-flow-rules-to-encrypt-email) (also known as transport rules) or [manually](https://support.microsoft.com/office/eaa43495-9bbb-4fca-922a-df90dee51980). [Custom branding](/en-us/purview/add-your-organization-brand-to-encrypted-messages) is also available. |  |  | ✔ |
| Use [Microsoft Purview Data Loss Prevention](/en-us/purview/dlp-create-deploy-policy) to safeguard company data. |  |  | ✔ |
| Use [Sensitivity labels](/en-us/purview/get-started-with-sensitivity-labels) to mark email messages as sensitive, confidential, etc. |  |  | ✔ |
| **6. Work together in Microsoft Teams** |  |  |  |
| Use [Microsoft Teams](/en-us/microsoft-365/business-premium/create-teams-for-collaboration) for communication, collaboration, and sharing | ✔ | ✔ | ✔ |
| Get time of click protection for URLs and files in Teams messages with [Safe Links for Microsoft Teams](/en-us/defender-office-365/safe-links-about#safe-links-settings-for-microsoft-teams) and [Safe Attachments for SharePoint, OneDrive, and Microsoft Teams](/en-us/defender-office-365/safe-attachments-for-spo-odfb-teams-about). |  |  | ✔ |
| Allow/block [URLs](/en-us/defender-office-365/tenant-allow-block-list-urls-configure) and [files](/en-us/defender-office-365/tenant-allow-block-list-files-configure) inside Teams using the Tenant Allow/Block List. |  |  | ✔ |
| Use [sensitivity labels for meetings](/en-us/purview/sensitivity-labels-meetings) to protect calendar items, Teams meetings, and chat. |  |  | ✔ |
| Use [Microsoft Purview Data Loss Prevention in Microsoft Teams](/en-us/purview/dlp-teams-default-policy) to safeguard company data. |  |  | ✔ |
| **7. Set file sharing settings** |  |  |  |
| [Safe Links](/en-us/defender-office-365/safe-links-about) and [Safe Attachments](/en-us/defender-office-365/safe-attachments-for-spo-odfb-teams-about) for SharePoint and OneDrive |  |  | ✔ |
| Use [Sensitivity labels](/en-us/purview/get-started-with-sensitivity-labels) to mark items as sensitive, confidential, etc. |  |  | ✔ |
| Use [Microsoft Purview Data Loss Prevention](/en-us/purview/dlp-create-deploy-policy) to safeguard company data. |  |  | ✔ |
| **8. Use Microsoft 365 Apps** |  |  |  |
| Use [Outlook and web/mobile versions of Microsoft 365 Apps](https://support.microsoft.com/topic/microsoft-365-mobile-apps-0ffcba82-380f-43dd-ab96-dbac0894b542) for all users | ✔ | ✔ | ✔ |
| Install [Microsoft 365 Apps](/en-us/microsoft-365/business-premium/m365bp-users-install-m365-apps) on user devices. |  | ✔ | ✔ |
| Use the [User quick setup guide](https://support.microsoft.com/office/7f34c318-e772-46a5-8c0a-ab86661542d1) to help users get set up and running. | ✔ | ✔ | ✔ |
| **9. Manage calendar sharing** |  |  |  |
| [Outlook](../setup/setup-outlook) for email and calendars. | ✔ | ✔ | ✔ |
| [Microsoft Purview Data Loss Prevention](/en-us/purview/dlp-create-deploy-policy) to safeguard company data. |  |  | ✔ |
| **10. Maintain your environment**: See [Maintain your environment](m365bp-security-monitor). | ✔ | ✔ | ✔ |

For more information about what each plan includes, see [Microsoft 365 for Businesses](https://www.microsoft.com/microsoft-365/business).