---
layout: Conceptual
title: Configure intelligent detections in Insider Risk Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-intelligent-detections
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Configure intelligent detections in Microsoft Purview Insider Risk Management to tune unusual download scoring, adjust alert severity distribution, import Defender for Endpoint alerts, and manage unallowed and third-party domains.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: how-to
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-25T00:00:00.0000000Z
audience: itpro
ms.collection:
- highpri
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- highpri
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 179b8e10-635c-eea3-a29c-8a903b93934a
document_version_independent_id: 179b8e10-635c-eea3-a29c-8a903b93934a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-settings-intelligent-detections.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-settings-intelligent-detections
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-settings-intelligent-detections.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/8b9ae643-2e85-42b8-beb2-eef4bae8c4bc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e047e27d-b5f3-43a8-b4b0-4f6dca95e7c9
platformId: 7438ad29-ef70-8bde-9136-675ed5765ba5
---

# Configure intelligent detections in Insider Risk Management | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Note

Global exclusions settings that the **Intelligent detections** setting previously included now appear in the [**Global exclusions (preview)** setting](insider-risk-management-settings-global-exclusions).

Use the **Intelligent detections** setting in Microsoft Purview Insider Risk Management to:

- Boost the score for unusual file download activities by entering a minimum number of daily events.
- Increase or decrease the volume and distribution of high, medium, and low alerts.
- Import and filter Defender for Endpoint alerts for activities used in policies created from Insider Risk Management templates.
- Specify unallowed domains to boost the risk score for potentially risky activity.
- Specify third-party domains to generate alerts for potentially risky download activity.

## File activity detection

Use this section to specify the number of daily events required to boost the risk score for download activity that's unusual for a user. For example, if you enter "25", and a user downloads 10 files on average over the previous 30 days, but a policy detects that they downloaded 20 files on one day, the score for that activity doesn't get boosted even though it's unusual for that user because the number of files they downloaded that day is less than 25.

## Configure alert volume levels

Insider risk policies assign a specific risk score to potentially risky activities they detect. This risk score determines the alert severity: low, medium, or high. By default, Insider Risk Management generates a certain number of low, medium, and high severity alerts. You can increase or decrease the volume of a specific level of alerts to suit your needs.

To adjust the volume of alerts for all Insider Risk Management policies, choose one of the following settings:

- **Fewer alerts**: You see all high-severity alerts, fewer medium-severity alerts, and no low-severity alerts. You might miss some true positives if you choose this setting.
- **Default volume**: You see all high-severity alerts and a balanced amount of medium-severity and low-severity alerts.
- **More alerts**: You see all medium-severity and high-severity alerts and most low-severity alerts. This setting might result in more false positives.

## Microsoft Defender for Endpoint alert statuses

Important

To import security violation alerts, you must configure Microsoft Defender for Endpoint in your organization and enable Defender for Endpoint for Insider Risk Management integration in the Defender Security Center. For more information on configuring Defender for Endpoint for Insider Risk Management integration, see [Configure advanced features in Defender for Endpoint](/en-us/windows/security/threat-protection/microsoft-defender-atp/advanced-features#share-endpoint-alerts-with-microsoft-compliance-center).

[Microsoft Defender for Endpoint](/en-us/windows/security/threat-protection/microsoft-defender-atp/microsoft-defender-advanced-threat-protection) is an enterprise endpoint security platform designed to help enterprise networks prevent, detect, investigate, and respond to advanced threats. To have better visibility of security violations in your organization, you can import and filter Defender for Endpoint alerts for activities used in policies created from Insider Risk Management security violation policy templates.

Depending on the types of signals you're interested in, you can choose to import alerts to Insider Risk Management based on the Defender for Endpoint alert triage status. You can define one or more of the following alert triage statuses in the global settings to import:

- Unknown
- New
- In progress
- Resolved

Alerts from Defender for Endpoint are imported daily. Depending on the triage status you choose, you might see multiple user activities for the same alert as the triage status changes in Defender for Endpoint.

For example, if you select *New*, *In progress*, and *Resolved* as the alert triage statuses to import, when a Microsoft Defender for Endpoint alert is generated and the status is *New*, an initial alert activity is imported for the user in Insider Risk Management. When the Defender for Endpoint triage status changes to *In progress*, a second activity for this alert is imported. When the final Defender for Endpoint triage status of *Resolved* is set, a third activity for this alert is imported. This functionality allows investigators to follow the progression of the Defender for Endpoint alerts and choose the level of visibility that their investigation requires.

## Configure unallowed and third-party domains

To boost your detections, specify unallowed and third-party domains:

- **Unallowed domains:** When you specify an unallowed domain, risk management activity that takes place with that domain has a higher risk score. Optionally, use it as a setting in policy triggers. For example, you might want to specify activities that involve sharing content with someone (such as sending email to someone with a gmail.com address) or activities that involve users downloading content to a device from an unallowed domain. You can add up to 500 unallowed domains.
- **Third-party domains:** If your organization uses third-party domains for business purposes (such as cloud storage), include them in the **Third-party domains** section to receive alerts for potentially risky activity related to the device indicator *Use a browser to download content from a third-party site*. You can add up to 500 third-party domains.

Tip

You can also specify [domains to exclude from being scored by Insider Risk Management policies](insider-risk-management-settings-global-exclusions).

### Add an unallowed domain

To add an unallowed domain to the Intelligent detections settings, perform the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page, and then select **Insider Risk Management** to go to the Insider Risk Management settings.
3. Under **Insider risk settings**, select **Intelligent detections**.
4. Scroll down to the **Unallowed domains** section, and then select **Add domains**.
5. Enter a domain.

    Tip

    To add multiple domains at once, import them as a CSV file by selecting **Import domains from CSV file** on the previous page.
6. To include all subdomains within the domain you entered, select the **Include multi-level subdomains** checkbox.

    Note

    Use wildcards to help match variations of root domains or subdomains. For example, to specify sales.wingtiptoys.com and support.wingtiptoys.com, use the wildcard entry "\*.wingtiptoys.com" to match these subdomains (and any other subdomain at the same level). To specify multi-level subdomains for a root domain, select the **Include multi-level subdomains** checkbox.
7. Press Enter. Repeat steps 5 and 6 for each additional domain that you want to add.
8. Select **Add domains**.

### Add a third-party domain

To add a third-party domain to the Intelligent detections settings, perform the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page, and then select **Insider Risk Management** to go to the Insider Risk Management settings.
3. Under **Insider risk settings**, select **Intelligent detections**.
4. Scroll down to the **Third-party domains** section, and then select **Add domains**.
5. Enter a domain.

    Tip

    To add multiple domains at once, import them as a CSV file by selecting **Import domains from CSV file** on the previous page.
6. To include all subdomains within the domain you entered, select the **Include multi-level subdomains** checkbox.

    Note

    Use wildcards to help match variations of root domains or subdomains. For example, to specify sales.wingtiptoys.com and support.wingtiptoys.com, use the wildcard entry "\*.wingtiptoys.com" to match these subdomains (and any other subdomain at the same level). To specify multi-level subdomains for a root domain, select the **Include multi-level subdomains** checkbox.
7. Press Enter. Repeat steps 5 and 6 for each additional domain that you want to add.
8. Select **Add domains**.