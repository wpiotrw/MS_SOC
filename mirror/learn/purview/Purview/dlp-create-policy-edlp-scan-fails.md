---
layout: Conceptual
title: Help protect files that Endpoint Data Loss Prevention fails to scan | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-create-policy-edlp-scan-fails
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- highpri
- tier1
- M365-security-compliance
- m365solution-mip
- m365initiative-compliance
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1014
search.appverid:
- MET150
description: Create a DLP policy that helps protect files that Endpoint Data Loss Prevention fails to scan.
ai-usage: ai-assisted
locale: en-us
document_id: d4d29bad-ba17-0b47-e13c-7b5b5b4a2e83
document_version_independent_id: d4d29bad-ba17-0b47-e13c-7b5b5b4a2e83
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-create-policy-edlp-scan-fails.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-create-policy-edlp-scan-fails
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-create-policy-edlp-scan-fails.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/486161dc-fa28-4625-9b1c-1a21d690bc8d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/5dd28c86-729c-4723-ab5a-57e26fcec2a8
platformId: 8503ed24-3397-26ef-dd3a-1a9ef4b765ae
---

# Help protect files that Endpoint Data Loss Prevention fails to scan | Microsoft Learn

This article uses the process you learned in [Design a data loss prevention policy](dlp-policy-design#design-a-data-loss-prevention-policy) to show you how to create a Microsoft Purview Data Loss Prevention (DLP) policy that helps protect files on supported Windows and macOS devices where the scanning process fails. Work through this scenario in your test environment to familiarize yourself with the policy creation UI.

Note

Applying controls to supported files that fail scanning is currently in preview.

Use this scenario when you want to apply Audit, Block, or Block with override controls on user activities for files that are on the [Monitored files](/en-us/purview/endpoint-dlp-learn-about) list but fail to be scanned by Endpoint DLP.

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important policy design. [This article](dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

## Prerequisites and assumptions

This scenario requires that you already have devices onboarded and reporting into activity explorer. If you haven't onboarded devices yet, see [Get started with Endpoint data loss prevention](endpoint-dlp-getting-started).

Important

This feature only supports following action types:

- Upload to a restricted cloud service domain
- Copy to a removable USB device
- Copy to a network share
- Print

## Policy intent statement and mapping

*Sometimes scanning fails for files that endpoint DLP supports. There might be sensitive information in those files, but we don't know. When scanning fails for a file on any of our onboarded devices, we want to prevent users from copying that file to a USB device or to a network share.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “When scanning fails for a file on any of our onboarded devices ...” | - Administrative scope: **Full directory**- Where to monitor: **Enteprise applications & devices**, **Devices**-Scope: **Allusers, groups, devices, device groups**- Conditions: **Document could not be scanned** |
| "...we want to prevent users from copying that file to a USB device or to a network share." | - Action : select **audit or restrict activities on devices**- clear **Upload to a restriced cloud service domain or access from an unallowed browser**- select **Apply restrictions to specific activity**- select **Copy to a removable USB device**, and **Block with override**- select **Copy to a network share** and **Block with override** clear **Copy to clipboard**, **Print**, **Copy or move using unallowed Bluetooth app**, and **Copy or move using RDP** |

When you configure the conditions, the summary looks like this:

![Policy conditions for match summary for scenario 3.](media/create-deploy-policy-scenario-3-summary.png)

## Steps to configure policy actions

Perform the following steps to configure the policy actions for this scenario.

Important

For the purposes of this policy creation procedure, leave the policy turned off. Change the policy activation settings when you deploy the policy.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open **Data Loss Prevention** &gt; **Policies**.
3. Select **Create policy**.
4. Select **Enterprise applications & devices**.
5. Select the **Custom** from the **Categories** then **Custom policy** template from **Regulations**.
6. Name your new policy and provide a description.
7. Select **Full directory** under **Admin units**.
8. Scope the location to **Devices** only.
9. Create a rule where:
    1. In **Conditions**:
        1. Select **Document could not be scanned**
    2. In **Actions**:
        1. Select **Audit or restrict activities on devices**.
        2. Clear **Upload to a restriced cloud service domain or access from an unallowed browser**
        3. Select **Apply restrictions to specific activity**
        4. Select **Copy to a removable USB device**, and **Block with override**
        5. Select **Copy to a network share**, and **Block with override**
        6. Clear **Copy to clipboard**, **Print**, **Copy or move using unallowed Bluetooth app**, and **Copy or move using RDP**
10. **Save**.
11. Choose **Turn on the policy immediately**. Choose **Next**.
12. Review your settings and choose **Submit**.