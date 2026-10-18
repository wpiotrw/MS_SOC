---
layout: FAQ
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft 365 Business Premium security - frequently asked questions | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365bp-security-faq?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
summary: >
  <div class="TIP">

  <p>Tip</p>

  <p>For frequently asked questions not related to security in Microsoft 365 Business Premium, see <a href="/microsoft-365/business-premium/microsoft-365-business-faqs">Microsoft 365 Business Premium frequently asked questions</a>.</p>

  </div>
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/help/4021566/windows-10-send-feedback-to-microsoft-with-feedback-hub-app
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: true
uhfHeaderId: MSDocsHeader-M365-IT
description: Find answers to the most frequently asked questions about security in Microsoft 365 Business Premium, a solution designed for small, and medium sized businesses (SMB) up to 300 users.
f1.keywords:
- NOCSH
ms.author: vpattnaik
author: vpattnai
manager: dansimp
ms.topic: how-to
ms.service: microsoft-365-security
ms.collection:
- tier2
- m365-security
- trust-pod
ms.date: 2025-09-15T00:00:00.0000000Z
ms.localizationpriority: medium
audience: microsoft-business
locale: en-us
document_id: d35f8006-63b2-9d32-d7bf-a9754523cea6
document_version_independent_id: d35f8006-63b2-9d32-d7bf-a9754523cea6
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/security-and-compliance/m365bp-security-faq.yml
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: faq
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/security-and-compliance/m365bp-security-faq
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/security-and-compliance/m365bp-security-faq.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/82f69bd7-5cb0-4163-9fd6-9103bb1a8352
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c671beaa-a830-4c9f-aceb-97379ee031ca
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f003597a-dab2-429a-8639-1d2acd9c0371
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/8921374c-4dbe-4ed0-b011-a39e18bfbd98
platformId: 2fad3345-5dec-7511-eb3a-57269d996755
---

# Microsoft 365 Business Premium security - frequently asked questions | Microsoft Learn

Tip

For frequently asked questions not related to security in Microsoft 365 Business Premium, see [Microsoft 365 Business Premium frequently asked questions](/en-us/microsoft-365/business-premium/microsoft-365-business-faqs).

## General

### How do I add the Microsoft Defender Suite to Microsoft 365 Business Premium?

Work with your [Microsoft partner](../manage/find-your-partner-or-reseller) or visit [Microsoft Security for Business](https://aka.ms/SMBSecurity).

### Does Microsoft 365 Business Premium with the Microsoft Defender Suite allow mixed licensing for endpoint security solutions?

Microsoft Defender for Business doesn't support mixed licensing, so a tenant with Defender for Business (which is included in Microsoft 365 Business Premium) along with Defender for Endpoint Plan 2 (which is included in Microsoft Defender Suite for Business Premium) defaults to the Defender for Business experience.

- 80 users are licensed for Business Premium (which includes Defender for Business).
- To those 80 users, you add 30 licenses of Microsoft Defender Suite (which includes Defender for Endpoint Plan 2).

The result is: all 80 users get the Defender for Business experience. To switch to the Defender for Endpoint Plan 2 experience, you need to do the following steps:

1. License all users for Defender for Endpoint Plan 2 using one of the following methods:
    - License all users with the standalone version of Defender for Endpoint Plan 2.
    - License all users with the Microsoft Defender Suite.
2. Contact Microsoft Support to request the switch for your organization.

For more information, see [Change your endpoint security subscription](/en-us/defender-business/mdb-manage-subscription).

### Is everyone in my organization required to have a Microsoft 365 Business Premium subscription?

No. However, the security and management benefits of Microsoft 365 Business Premium are available only to users with devices managed with a Business Premium subscription.

All businesses should seek to standardize their IT environment to help reduce maintenance and security costs over time. However, we recognize that small and medium-sized businesses often update their software when they upgrade their hardware over an extended time period.

Although you can deploy Microsoft 365 Business Premium to part of your organization, we recommend deploying Microsoft 365 Business Premium to all users for the best protection of sensitive business data and consistent collaboration experiences.

### How does Microsoft 365 Business Premium help support personal devices (also known as bring your own device or BYOD)?

Many small to medium-sized businesses don't provide company-owned mobile devices to users, yet users need to access company data when they're not in the office. Although using personal devices to access company data is common these days (in particular, email and calendar data), the practice increases the risk that business information could end up in the wrong hands.

Microsoft 365 Business Premium contains simple but powerful features that allow users to security access company data on their personal devices while preventing those devices from accessing, retaining, and/or sharing business information.

For more information, see the following articles:

- [Device and application management in Microsoft 365 Business Premium](m365bp-devices-enrollment)
- [Device and application protection in Microsoft 365 Business Premium](m365bp-devices-protection)

### How does Microsoft 365 Business Premium help protect PCs in my organization from malicious attacks?

PCs managed with Microsoft 365 Business Premium are protected by Microsoft Defender for Business, an endpoint security solution that's designed especially for small and medium-sized business (up to 300 users). With Defender for Business, the devices in your organization are better protected from ransomware, malware, phishing, and other threats.

### What if my Microsoft 365 Business Premium organization has some Microsoft Defender for Business servers licenses, and I want to switch all users to Microsoft Defender Suite?

You need to change your server plan to Microsoft Defender for Endpoint for servers or Microsoft Defender for Servers.

### Is Microsoft Defender Suite available as an add-on for Microsoft 365 Business Premium for Nonprofits?

Yes.

Microsoft Defender Suite is available as an add-on for the commercial and non-profit offerings of Microsoft 365 Business Premium.

## Deployment

### Does Microsoft 365 Business Premium include the full capabilities of Microsoft Intune?

Yes.

Microsoft 365 Business Premium subscribers are licensed to use full Intune capabilities for iOS, Android, Mac, and other cross-platform device management.

Features that aren't available in the simplified management experience in the Microsoft Defender portal are available in the Microsoft Intune portal. For example:

- Non-Microsoft app management
- Configuration of Wi-Fi profiles
- VPN certificates

### Does Microsoft Entra ID P1 come with Microsoft 365 Business Premium?

Yes.

Microsoft Entra ID P1 is included with Microsoft 365 Business Premium.

### Does Microsoft 365 Business Premium allow customers to manage Apple devices?

Yes.

Microsoft 365 Business Premium includes Intune and Defender for Business to help you securely manage iOS/iPadOS, and macOS devices.

### What is Windows Autopilot?

Windows Autopilot uses a supported version of Windows Semi-Annual Enterprise Channel to set up PCs with business critical apps, policies, and features (for example, BitLocker) before you give the PCs to users. Autopilot can also reset, repurpose, and recover Windows devices. For more information, see [Overview of Windows Autopilot](/en-us/autopilot/overview).

## Compatibility

### Can Microsoft 365 Business Premium customers use Microsoft Defender for Endpoint?

Yes.

Microsoft 365 Business Premium includes Microsoft Defender for Business, which is built on the capabilities of Defender for Endpoint to provide advanced security protection for devices.

However, you can add Defender for Endpoint Plan 1 or Plan 2 to your Microsoft 365 Business Premium subscription. For more information, see [Microsoft 365 guidance for security & compliance](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance).