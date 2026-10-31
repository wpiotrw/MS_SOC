---
layout: Conceptual
title: Microsoft Security Copilot experiences | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/experiences-security-copilot
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about the standalone and embedded Microsoft Security Copilot experiences.
ms.date: 2025-11-17T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: concept-article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: a39a7109-bb21-e9ff-0941-a61071151c30
document_version_independent_id: a39a7109-bb21-e9ff-0941-a61071151c30
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/experiences-security-copilot.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: experiences-security-copilot
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/experiences-security-copilot.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 368ac0e8-ae79-35c9-85c2-93431c368d06
---

# Microsoft Security Copilot experiences | Microsoft Learn

Security Copilot offers an immersive standalone experience and intuitive embedded experiences that are available in other Microsoft security products.

In addition to the standalone and embedded experiences, Security Copilot offers developer scenarios that enable you to build, test, publish, and integrate agents and plugins to meet unique security needs. These scenarios empower developers to streamline workflows, automate tasks, and extend Security Copilot’s capabilities across Microsoft security products.

This topic helps you:

- Identify the differences between standalone and embedded Security Copilot experiences
- Explore available embedded experiences across Microsoft security solutions
- Find guidance for hiding or showing the Copilot sidecar panel
- Understand developer scenarios such as building custom agents and automating workflows with Security Copilot

Watch the following video to learn more about the Security Copilot experiences:

## Standalone and embedded experiences

**Standalone experience** Security Copilot, accessed through https://securitycopilot.microsoft.com, is considered the **standalone** experience.

**Embedded experience** Accessing Security Copilot embedded experiences in other Microsoft security products is considered an **embedded** experience.

Important

Guidance on specific embedded experiences can be found in the documentation library of the corresponding service. For example, if you access a Microsoft Defender XDR embedded experience, then the corresponding documentation for that Security Copilot experience can be found in the Microsoft Defender XDR documentation. This ensures that you receive service-specific guidance wherever you access Security Copilot.

A feature common to all embedded experiences is the ability to hide or show the Copilot sidecar. The panel behavior persists per Copilot embedded experience, remembering that user's option. The embedded copilot functionality remains the same whether it's hidden or not, so closing the panel doesn't affect SCU consumption.

For example, to hide the Copilot in Microsoft Defender XDR experience, select the **X**. The incident summary will continue to generate in the background.

![Screenshot showing Copilot panel in embedded experience of Microsoft Defender XDR.](media/sidecar-embedded-experience.png)

To make the panel visible again, select the **Copilot** button.

## Embedded experiences

The following table lists the available embedded experiences.

| Product | Embedded experience |
| --- | --- |
| Azure Firewall | - [Enrich the threat profile of an IDPS signature beyond log information](/en-us/azure/firewall/firewall-copilot#enrich-the-threat-profile-of-an-idps-signature-beyond-log-information) - [Generate recommendations to secure your environment using Azure Firewall's IDPS feature](/en-us/azure/firewall/firewall-copilot#generate-recommendations-to-secure-your-environment-using-azure-firewalls-idps-feature)- [Look for a given IDPS signature across your tenant, subscription, or resource group](/en-us/azure/firewall/firewall-copilot#look-for-a-given-idps-signature-across-your-tenant-subscription-or-resource-group) - [Retrieve the top IDPS signature hits for an Azure Firewall](/en-us/azure/firewall/firewall-copilot#retrieve-the-top-idps-signature-hits-for-an-azure-firewall) |
| Microsoft Defender for Cloud | - [Analyze recommendations](/en-us/azure/defender-for-cloud/analyze-with-copilot) - [Delegate recommendations](/en-us/azure/defender-for-cloud/delegate-with-copilot) - [Remediate code](/en-us/azure/defender-for-cloud/remediate-code-with-copilot) - [Remediate recommendations](/en-us/azure/defender-for-cloud/remediate-with-copilot) - [Summarize recommendations](/en-us/azure/defender-for-cloud/summarize-with-copilot) |
| Microsoft Defender Threat Intelligence | - [Using Security Copilot for threat intelligence](/en-us/defender/threat-intelligence/using-copilot-threat-intelligence-defender-xdr) |
| Microsoft Defender XDR | - [Analyze files](/en-us/microsoft-365/security/defender/copilot-in-defender-file-analysis) - [Analyze scripts and codes](/en-us/microsoft-365/security/defender/security-copilot-m365d-script-analysis) - [Create incident reports](/en-us/microsoft-365/security/defender/security-copilot-m365d-create-incident-report)- [Generate KQL queries for hunting](/en-us/microsoft-365/security/defender/advanced-hunting-security-copilot)- [Summarize device information](/en-us/microsoft-365/security/defender/copilot-in-defender-device-summary) - [Summarize incidents](/en-us/microsoft-365/security/defender/security-copilot-m365d-incident-summary) - [Summarize identities](/en-us/defender-xdr/security-copilot-defender-identity-summary) - [Use guided response](/en-us/microsoft-365/security/defender/security-copilot-m365d-guided-response) |
| Microsoft Entra | - [Investigate app risk](/en-us/entra/fundamentals/copilot-security-entra-investigate-risky-apps) - [Investigate incidents](/en-us/entra/fundamentals/copilot-security-entra-investigate-incident) - [Investigate risky users](/en-us/entra/fundamentals/copilot-entra-risky-user-summarization) - [Manage lifecycle workflows](/en-us/entra/fundamentals/copilot-entra-lifecycle-workflow) |
| Microsoft Intune | - [Device query](/en-us/mem/intune/copilot/copilot-intune-overview#query-with-copilot-in-device-query)- [Policy and setting management](/en-us/mem/intune/copilot/copilot-intune-overview#policy-and-setting-management) - [Use Microsoft Copilot in Intune to troubleshoot devices](/en-us/mem/intune/copilot/copilot-devices) |
| Microsoft Purview | - [Investigate a Microsoft Purview Data Loss Prevention alert](/en-us/purview/dlp-alerts-dashboard-get-started#investigate-a-dlp-alert) - [Investigate insider risk management activities](/en-us/purview/insider-risk-management-activities)- [Summarize Communication Compliance messages by using Security Copilot](/en-us/purview/communication-compliance-investigate-remediate#summarize-a-message-by-using-microsoft-copilot-for-security) - [Summarize an eDiscovery message by using Security Copilot](/en-us/purview/ediscovery-view-documents-in-review-set#summarize-a-message-by-using-microsoft-copilot-for-security-preview) |
| Microsoft Sentinel | - [Summarize Microsoft Sentinel incidents with Security Copilot](/en-us/azure/sentinel/sentinel-security-copilot-incident-summary) |

## Developer scenarios

While Security Copilot offers immersive standalone and embedded experiences for end users, it also supports developer scenarios for organizations seeking to extend, automate, or integrate security workflows.

Developer scenarios empower you to:

- Build custom agents and plugins to automate security tasks
- Integrate Security Copilot with other Microsoft security products
- Build, publish, test and manage agents tailored to your organization's needs

Explore the [Security Copilot Developer content](/en-us/copilot/security/developer/).