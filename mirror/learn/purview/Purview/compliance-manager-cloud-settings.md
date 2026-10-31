---
layout: Conceptual
title: Configure cloud settings for use with Microsoft Purview Compliance Manager | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/compliance-manager-cloud-settings
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-07-01T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-compliance-manager
ms.collection:
- purview-compliance
- m365solution-compliancemanager
- m365initiative-compliance
search.appverid:
- MOE150
- MET150
description: Set up your Azure and other non-Microsoft services for using Microsoft Purview Compliance Manager to assess compliance across multiple cloud services.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: acd0b720-1ab3-da11-f1f2-5f6a73d5af2a
document_version_independent_id: acd0b720-1ab3-da11-f1f2-5f6a73d5af2a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/compliance-manager-cloud-settings.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: compliance-manager-cloud-settings
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/compliance-manager-cloud-settings.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/8e3fdb08-a059-4277-98f6-c0e21e940707
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/eab1aabc-e18c-405b-ac29-e35eb0b15e3b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/88291526-9c74-4f87-878c-de0a82134421
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/574d2eb1-e22a-49c0-b4eb-64e86dbeee6b
platformId: 720c1b00-3107-ad6b-e38e-2762ad27b49e
---

# Configure cloud settings for use with Microsoft Purview Compliance Manager | Microsoft Learn

## Setting up for multicloud support

Compliance Manager integrates with [Microsoft Defender for Cloud](/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) to provide multicloud support. Organizations must have at least one subscription within Microsoft Azure and then enable Defender for Cloud so that Compliance Manager can receive the necessary signals to monitor your cloud services. Once you have Defender for Cloud, you need to assign the relevant industry and regulatory standards to your subscriptions.

Depending on what your organization has already set up, use one of the following sections to get started:

- **You don't have Azure**: Activate Azure and create a subscription
- **You have Azure but don't have Defender for Cloud**: Enable Defender for Cloud on your Azure subscription
- **You have Defender for Cloud but haven't assigned standards**: Assign standards to your cloud service subscriptions

### Standards supported by Compliance Manager and Defender for Cloud

The standards or regulations listed below are supported across Defender for Cloud and Compliance Manager. Each standard is available to support Microsoft 365 in addition to the other cloud services listed in parentheses.

Tip

Defender for Cloud refers to “standards,” while Compliance Manager uses “regulations” to refer to the same thing.

- AWS Foundational Security Best Practices
- CIS 1.1.0 (GCP)
- CIS Microsoft Azure Foundations Benchmark v1.1.0 (Azure)
- CIS 1.2.0 (AWS, GCP)
- CIS Microsoft Azure Foundations Benchmark v1.3.0 (Azure)
- CIS Microsoft Azure Foundations Benchmark v1.4.0 (Azure)
- FedRAMP High (Azure)
- FedRAMP Moderate (Azure)
- ISO 27001 (Azure, GCP)
- NIST SP 800-171 Rev.2 (Azure)
- NIST SP 800-53 Rev.4 (Azure)
- NIST SP 800 53 Rev.5 (Azure, AWS, GCP)
- PCI DSS 3.2.1 (AWS, GCP)
- PCI DSS v4.0 (Azure)
- SOC 2 Type 2 (Azure)
- SWIFT CSP-CDCF v2022 (Azure)

## Activate Azure and create a subscription

Setting up a subscription within Microsoft Azure is a prerequisite for getting started with Defender for Cloud. If you don’t have a subscription, you can [sign up for an Azure free account](https://azure.microsoft.com/pricing/free-trial/).

## Enable Defender for Cloud

Visit [Quickstart: Set up Microsoft Defender for Cloud](/en-us/azure/defender-for-cloud/get-started). Follow the steps to enable Defender for Cloud on your Azure subscription and become familiar with the Defender for Cloud Overview page. Once you've enabled Defender for Cloud, follow the steps below to make sure you're set up for Compliance Manager integration.

Most setup functions require the user to hold the [Owner role in Azure](/en-us/azure/role-based-access-control/built-in-roles#owner). Get more details about [User roles and permissions for Defender for Cloud](/en-us/azure/defender-for-cloud/permissions).

### Confirm access to Defender for Cloud Regulatory compliance

1. Go to [Microsoft Defender for Cloud | Regulatory compliance](https://portal.azure.com/#view/Microsoft_Azure_Security/SecurityMenuBlade/%7E/22).
2. Validate that you see a dashboard like this: ![Screenshot of the Defender for Cloud regulatory compliance dashboard showing compliance status and standards.](media/compliance-manager-mdc-dashboard.png)
3. If you don’t see the dashboard above and instead see a notice about insufficient licensing, follow the prompts to activate an applicable Defender for Cloud plan. We recommend enabling one of the two plans: **Foundational CSPM** or **Defender CSPM** ([cloud security posture management plans](/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management)). You can manually select the plans by completing the following steps:

    1. In Defender for Cloud, select **Environment settings** on the left navigation.
    2. Select **Azure** from your list of environments. Expand the item underneath **Azure** to view the subscription, then select the subscription. You arrive at the **Defender plans** page.
    3. In the **Plan** column, find the rows for **Foundational CSPM** and **Defender CSPM**. In the **Status** row, select the **On** button for both plans.

### View available environments

1. In Defender for Cloud, select **Environment settings** on the left navigation.
2. View the available environments and subscriptions currently visible to MDC for your tenant. You may need to expand your management groups to view subscriptions, which you can do by selecting **Expand all** below the search bar. In addition to your Azure subscriptions, you'll also see any Google Cloud Platform (GCP) projects or Amazon Web Services (AWS) accounts connected to Defender for Cloud.
3. If you don't see an expected subscription and have already confirmed your Defender for Cloud licensing in the previous steps, check your current directory and subscription filters in your Azure [Portal settings](https://portal.azure.com/#settings/directory). In this view, you can adjust any subscription filters or switch to a different directory if one is available, and then return to the **Environment settings** view to check the results.
4. If you don't see an expected AWS or GCP environment, account, or project, proceed to the next step to set up the necessary connectors.

### Connect to your Amazon Web Services or Google Cloud Provider accounts (optional)

Follow these instructions if you have an Amazon Web Services (AWS) account or Google Cloud Platform (GCP) project that you want Compliance Manager to assess compliance posture, and you don’t already see those accounts or projects in your Azure Environment settings. When you complete this process, you can begin assigning standards to your connected AWS or GCP subscriptions within about an hour, though full data can take up to 24 hours to appear.

1. In Defender for Cloud, select **Environment settings** on the left navigation.
2. Select **Add environment** and choose either **Amazon Web Services** or **Google Cloud Platform**. ![Screenshot of the Defender for Cloud environment settings page with the Add environment option for connecting AWS or GCP accounts.](media/compliance-manager-mdc-environments.png)
3. Follow the wizard steps to complete the account setup. Connecting to the accounts requires admin permissions in the AWS or GCP accounts being used, and some configuration steps within AWS or GCP. These steps are detailed in the wizard.

    1. For a simple setup option, consider starting with just one account such as GCP. In the first step of **Account details**, at **Onboard**, select **Single account**. This option requires the least amount of configuration effort.

## Add standards to your subscriptions

Check the list of standards supported by Defender for Cloud and Compliance Manager to ensure your desired standard is supported. Then follow the steps below.

1. In Defender for Cloud, select **Environment settings** on the left navigation.
2. Your available environments and subscriptions are listed on the page. You may need to expand your management groups to view subscriptions, which you can do by selecting **Expand all** below the search bar. Find the subscription to which you want to add a standard.
3. On the row for the subscription, select the ellipses on the far right and select **Edit settings**. ![Screenshot of the Defender for Cloud environment settings page showing the Edit settings option for a subscription.](media/compliance-manager-mdc-subcription-settings.png)
4. On the left navigation, under **Policy settings**, select **Security policy**.
5. Browse the list of available standards under **Industry & regulatory standards**. You can view more standards by selecting the **Add more standards** button at the bottom of the list. Assign at least one of the supported standards listed below to your subscription by selecting **Enable** on the standard's row.