---
layout: Conceptual
title: Fine-tune exclusions in Insider Risk Management by creating detection groups and modifying built-in indicator variants (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-detection-groups
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about using the Detection groups setting (preview) in Microsoft Purview Insider Risk Management to create a variant of a built-in indicator.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: how-to
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
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
document_id: 4db56c32-59c1-7ce4-8d99-c714e6204e90
document_version_independent_id: 4db56c32-59c1-7ce4-8d99-c714e6204e90
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-settings-detection-groups.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-settings-detection-groups
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-settings-detection-groups.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 1451dfa8-a33e-7f03-91e2-e4c98681f612
---

# Fine-tune exclusions in Insider Risk Management by creating detection groups and modifying built-in indicator variants (preview) | Microsoft Learn

## Overview

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

You can exclude items from being scored by Insider Risk Management policies by using the [Global exclusions setting](insider-risk-management-settings-global-exclusions). These types of exclusions apply to every trigger and indicator for all policies that you create within a tenant. By using detection groups, you can modify a built-in global exclusion to make it specific for your organization's needs.

You can also use detection groups to modify the built-in insider risk indicators to tailor detections for different sets of users at the policy level. For example, to reduce the number of false positives for email activities, you might want to create a variant of the *Sending email with attachments to recipients outside the organization* built-in indicator to only detect email sent to personal domains.

## Process for creating and using detection groups

To use a detection group as part of a global exclusion, create the detection group as described in this article, then select it in the [Global exclusions settings](insider-risk-management-settings-global-exclusions).

Using a detection group to modify a built-in indicator includes the following steps:

1. Create the detection group as described in the Create a detection group section of this article. You select this detection group when you create the variant.
2. [Create the variant](insider-risk-management-settings-policy-indicators#create-a-variant-of-a-built-in-indicator).
3. [Use the variant in a new or existing policy](insider-risk-management-settings-policy-indicators#use-a-variant-in-a-policy).
4. [Review alerts related to the activities specified in the variant](insider-risk-management-settings-policy-indicators#investigate-insights-provided-by-variants).

## Create a detection group

A detection group helps you scope a built-in indicator or a global exclusion to focus on the high-value activities important to your organization.

### Detection types for policy indicators

Every policy indicator includes certain detection types that are applicable to that indicator. For example, for the *Sharing SharePoint files with people outside the organization* indicator, one of the detection types is *domains*. When you share a SharePoint file, you choose a domain to share the file with. Not all indicators have the same detection types. For example, *domains* is a detection type of the *Sharing SharePoint files with people outside the organization* indicator, but it's not a detection type of the *Creating or copying files to USB* indicator since it's not applicable in that case.

Insider Risk Management currently supports seven detection types:

- Domains
- File paths
- File types
- Keywords
- Sensitive info types
- SharePoint sites
- Trainable classifiers

Tip

When you create a detection group, you can see all the applicable indicators for a particular detection by selecting the **View applicable indicators** link in the introductory text for the group type.

Use the procedures in this section to create a detection group for each supported group type: domains, file paths, file types, keywords, sensitive info types, SharePoint sites, and trainable classifiers.

### Create a domains detection group

To create a domains detection group, complete these steps:

1. In Insider Risk Management settings, select **Detection groups**.
2. In the panel to the right, under **Type**, select **Domains**.
3. In the panel to the right, select **New domain group**.
4. In the **New domain group** pane, enter a name for the group (or accept the suggested name) and an optional description.
5. In the **Add domains** field, enter a domain, then press Enter. Continue adding more domains in the same way. To add a long list of domains, import them as a CSV file by selecting **Import domains from CSV file**. The domains you add appear at the bottom of the pane. You can create up to 10 domain detection groups, and each group can have up to 500 items.

    Note

    To specify multi-level subdomains for a root domain, select the **Include multi-level subdomains** checkbox, add a domain, then press Enter to add the domain to the list. Any subdomains included within that domain are included. Repeat the same process to add more domains, then select **Add domains** when you're done.

    Tip

    Use wildcards to help match variations of root domains or subdomains. For example, to specify `sales.wingtiptoys.com` and `support.wingtiptoys.com`, use the wildcard entry `*.wingtiptoys.com` to match these subdomains (and any other subdomain at the same level).
6. Select **Save**. You see a **Next steps** dialog box that advises you on the next step in the process, which includes using this detection group in a variant.

#### How the *Free public domains* domain group detects exfiltration of business data to personal email domains

The Domains detection group includes a special domain group called *Free public domains* that consists of a list of free email providers (such as `gmail.com` or `yahoo.com`) that users can use to create a personal email ID. This list automatically highlights exfiltration of business data to personal email domains for the email insight on the [**User activity** and **Activity explorer** tabs](insider-risk-management-activities). The insight lists the number of emails sent to free public domains by an in-scope user. The list also supports the algorithm that identifies email sent to self (sent to the in-scope user's personal email account). The email insight lists the number of emails sent to self.

![Insider Risk Management email highlights for personal email exfiltration](media/insider-risk-management-personal-email-exfiltration.png)

You can use this built-in domain group like any other domain group to create a variant of a built-in indicator for your policies. This domain group only applies to the *Sending email with attachments to recipients outside the organization* indicator. For more information, see [Create a variant of a built-in indicator](insider-risk-management-settings-policy-indicators#create-a-variant-of-a-built-in-indicator).

### Create a file paths detection group

To create a file paths detection group, complete these steps:

1. In Insider Risk Management settings, select **Detection groups**.
2. In the panel to the right, under **Type**, select **File paths**.
3. In the panel to the right, select **New file path group**.
4. In the **New file path group** pane, add a name for the group or accept the suggested name, and add a description (optional).
5. Select **Add file paths**, select the file paths, then select **Add**. You can create up to 10 file path detection groups and each group can have up to 500 items.
6. Select **Save**. You see a **Next steps** dialog box that advises you on the next step in the process, which includes using this detection group in a variant.

### Create a file types detection group

To create a file types detection group, complete these steps:

1. In Insider Risk Management settings, select **Detection groups**.
2. In the panel to the right, under **Type**, select **File types**.
3. In the panel to the right, select **New file type group**.
4. In the **New file type group** pane, add a name for the group or accept the suggested name, and add a description (optional).
5. In the **Add file type** field, enter a file extension, then press Enter. Continue adding more file extensions the same way. The extensions that you add are listed at the bottom of the pane. You can create up to 10 file types detection groups and each group can have up to 500 items.
6. Select **Save**. You see a **Next steps** dialog box that advises you on the next step in the process, which includes using this detection group in a variant.

### Create a keywords detection group

To create a keywords detection group, complete these steps:

1. In Insider Risk Management settings, select **Detection groups**.
2. In the panel to the right, under **Type**, select **Keywords**.
3. In the panel to the right, select **New keywords group**.
4. In the **New keywords group** pane, add a name for the group or accept the suggested name, and add a description (optional).
5. In the **Add keywords** field, enter a keyword, then press Enter. Repeat this process for each keyword you want to add. The keywords that you add are listed at the bottom of the pane. You can create up to 10 keywords detection groups and each group can have up to 500 items.
6. Select **Save**. You see a **Next steps** dialog box that advises you on the next step in the process, which includes using this detection group in a variant.

### Create a sensitive info types detection group

Note

The exclusion list of sensitive info types takes precedence over the [priority content](insider-risk-management-policies#prioritize-content-in-policies) list.

1. In Insider Risk Management settings, select **Detection groups**.
2. In the panel to the right, under **Type**, select **Sensitive info types**.
3. In the panel to the right, select **New sensitive info type group**.
4. In the **New sensitive info type group** pane, enter a name for the group or accept the suggested name. Optionally, add a description.
5. Select **Add sensitive info types**, select the sensitive info types, then select **Add**. Default SIT exclusions are not available for selection. You can create up to 10 sensitive info type groups, and each group can have up to 500 items.
6. Select **Save**. You see a **Next steps** dialog box that advises you on the next step in the process, which includes using this detection group in a variant.

### Create a SharePoint sites detection group

To create a SharePoint sites detection group, complete these steps:

1. In Insider Risk Management settings, select **Detection groups**.
2. In the panel to the right, under **Type**, select **SharePoint sites**.
3. In the panel to the right, select **New SharePoint site group**.
4. In the **New SharePoint site group** pane, enter a name for the group or accept the suggested name. Optionally, add a description.
5. Select **Add sites**, select the SharePoint sites, then select **Add**. You can create up to 10 SharePoint sites detection groups, and each group can have up to 500 items.
6. Select **Save**. You see a **Next steps** dialog box that advises you on the next step in the process, which includes using this detection group in a variant.

### Create a trainable classifier detection group

To create a trainable classifier detection group, complete these steps:

1. In Insider Risk Management settings, select **Detection groups**.
2. In the panel to the right, under **Type**, select **Trainable classifiers**.
3. In the panel to the right, select **New trainable classifiers group**.
4. In the **New trainable classifiers group** pane, enter a name for the group or accept the suggested name. Optionally, add a description.
5. Select **Add trainable classifiers**, select the trainable classifiers, then select **Add**. You can create up to 10 trainable classifier detection groups, and each group can have up to 500 items.
6. Select **Save**. You see a **Next steps** dialog box that advises you on the next step in the process, which includes using this detection group in a variant.