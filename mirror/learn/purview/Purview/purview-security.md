---
layout: Conceptual
title: Microsoft Purview data security solutions | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/purview-security
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use this article to learn more about Microsoft Purview data security solutions.
keywords: Microsoft 365, Microsoft Purview, security, solutions
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-05-01T00:00:00.0000000Z
audience: ITPro
ms.topic: overview
ms.service: purview
search.appverid:
- MET150
ms.collection:
- purview-compliance
- essentials-get-started
- essentials-security
locale: en-us
document_id: 0e514ca3-644a-ec04-eedb-e101f8b1ede8
document_version_independent_id: 0e514ca3-644a-ec04-eedb-e101f8b1ede8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/purview-security.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purview-security
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/purview-security.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: f86c35ae-bcc4-1472-09e8-12c0da210002
---

# Microsoft Purview data security solutions | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

[Microsoft Purview](/en-us/purview/purview) data security solutions help you manage and monitor your data and protect information. This article helps you learn about Microsoft Purview data security solutions and quickly get started with deploying these solutions to meet specific security needs for your organization.

## Protect sensitive data across clouds, apps, and devices

Your information protection strategy should be driven by your business needs, but every organization has a requirement to protect some or all of its data. Use the capabilities from [Microsoft Purview Information Protection](information-protection) (formerly Microsoft Information Protection) to help you discover, classify, protect, and govern sensitive information wherever it lives or travels.

### Know your data

Your organization likely has information residing across the Microsoft 365 services, other cloud services, and on-premises. Identifying which items are sensitive and gaining visibility into how they're being used is central to your information protection practice. Microsoft Purview includes:

- [Sensitive information types](sensitive-information-type-learn-about) to identify sensitive items by using built-in or custom regular expressions, or a function.
- [Trainable classifiers](classifier-learn-about) to identify sensitive items by using examples of the data you're interested in rather than identifying elements in the item.
- [Data classification](data-classification-overview) provides a graphical identification of items in your organization that have a sensitivity label, a retention label, or have been classified and the actions your users are taking on them

### Protect your data

There are many capabilities that you can use from the Microsoft Purview Information Protection solution to help protect your data, wherever it's stored and however it's accessed. However, sensitivity labels are the foundational capability that both provide protection actions and interact with other Purview solutions and capabilities.

Sensitivity labels provide users and admins with visibility into the sensitivity of the data that they're using, and the labels themselves can apply protection actions that include encryption, access restrictions, and visual markings. For more information about the range of labeling scenarios supported, see the [Common scenarios for sensitivity labels](get-started-with-sensitivity-labels#common-scenarios-for-sensitivity-labels) section from the getting started documentation. For more information about sensitivity labels, see [Learn about sensitivity labels](sensitivity-labels).

#### Encrypt your data and control your encryption keys

[Encryption](encryption) is an important part of your information protection strategy. The encryption process encodes your data (referred to as plaintext) into ciphertext. Unlike plaintext, ciphertext can't be used by people or computers unless and until the ciphertext is decrypted. Decryption requires an encryption key that only authorized users have. Encryption helps ensure that only authorized recipients can decrypt your content.

[Microsoft Purview Double Key Encryption](double-key-encryption) helps secure your most sensitive data that is subject to the strictest protection requirements. [Microsoft Purview Customer Key](customer-key-overview) helps you meet regulatory or compliance obligations for controlling root keys. You explicitly authorize Microsoft 365 services to use your encryption keys to provide value added cloud services, such as eDiscovery, anti-malware, anti-spam, search indexing, and so on.

### Prevent data loss

Unintentional sharing of sensitive items can cause financial harm to your organization and may result in a violation of laws and regulations. [Microsoft Purview Data Loss Prevention](dlp-learn-about-dlp) can help protect your organization against unintentional or accidental sharing of sensitive information both inside and outside of your organization. In a data loss prevention policy, you:

- Define the sensitive information you want to monitor for, like financial, health, medical, and privacy data.
- Where to monitor, like Microsoft 365 services or Windows and macOS devices.
- The conditions that must be matched for a policy to be applied to an item, like items containing credit card, driver's license, or social security numbers.
- The actions to take when a match is found, like audit, block the activity, and block the activity with override.

## Address your data security objectives with Data Security Posture Management

[Microsoft Data Security Posture Management (DSPM)](data-security-posture-management-learn-about) helps you discover, protect, and investigate sensitive data risks across your digital estate. Unifying other Microsoft Purview solutions by focusing on data security objectives with remediation plans that have guided workflows and reports, DSPM provides visibility and control for both traditional applications and AI apps and agents, regardless of where sensitive data resides.

## Analyze and respond to data security incidents with Data Security Investigations

[Microsoft Purview Data Security Investigations](data-security-investigations) helps cybersecurity teams in your organization harness generative artificial intelligence (AI) to analyze and respond to data security incidents, risky insiders, and data breaches. Investigations help you quickly identify risks from sensitive data exposure and more effectively collaborate with your partner teams to remediate the issues and simplify tasks that traditionally are time consuming and complex.

## Detect and act on risk activities with Insider Risk Management

[Microsoft Purview Insider Risk Management](insider-risk-management) uses the full breadth of service and 3rd-party indicators to help you quickly identify, triage, and act on risky user activity in your organization. By using logs from Microsoft 365 and Microsoft Graph, insider risk management allows you to define specific policies to identify risk indicators. After identifying risky activities, you can take action to mitigate these risks.

## Restrict communication and collaboration between users with Information Barriers

[Microsoft Purview Information Barriers (IB)](information-barriers) is a compliance solution that allows you to restrict two-way communication and collaboration between groups and users in Microsoft Teams, SharePoint, and OneDrive. Often used in highly regulated industries, IB can help to avoid conflicts of interest and safeguard internal information between users and organizational areas.

## Limit access to sensitive data with Privileged Access Management

Having standing access by some users to sensitive information or critical network configuration settings in Microsoft Exchange is a potential pathway for compromised accounts or internal threat activities. [Microsoft Purview Privileged Access Management](privileged-access-management) helps protect your organization from breaches and helps to meet compliance best practices by limiting standing access to sensitive data or access to critical configuration settings. Instead of administrators having constant access, just-in-time access rules are implemented for tasks that need elevated permissions.