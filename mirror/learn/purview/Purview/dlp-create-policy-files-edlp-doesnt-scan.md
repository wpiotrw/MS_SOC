---
layout: Conceptual
title: Help protect files that Endpoint Data Loss Prevention doesn't scan | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-create-policy-files-edlp-doesnt-scan
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
description: Create a Microsoft Purview DLP policy to apply audit or block controls to file types not monitored by Endpoint DLP, with optional file extension exclusions.
ai-usage: ai-assisted
locale: en-us
document_id: 52ae4755-3a82-4ee6-222f-7320eaad27c0
document_version_independent_id: 52ae4755-3a82-4ee6-222f-7320eaad27c0
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-create-policy-files-edlp-doesnt-scan.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-create-policy-files-edlp-doesnt-scan
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-create-policy-files-edlp-doesnt-scan.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/486161dc-fa28-4625-9b1c-1a21d690bc8d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/5dd28c86-729c-4723-ab5a-57e26fcec2a8
platformId: 8bf68d52-43b2-9b57-1c8c-b597ea310296
---

# Help protect files that Endpoint Data Loss Prevention doesn't scan | Microsoft Learn

This article uses the process you learned in [Design a data loss prevention policy](dlp-policy-design#design-a-data-loss-prevention-policy) to show you how to create a Microsoft Purview Data Loss Prevention (DLP) policy that helps protect files that Endpoint DLP doesn't support. Work through these scenarios in your test environment to familiarize yourself with the policy creation UI.

Apply controls to all unsupported files, is in *preview*.

Use the "Apply controls to all unsupported files" scenario to apply Audit, Block, or Block with override controls on user activities for files that aren't on the [Monitored files](/en-us/purview/endpoint-dlp-learn-about) list without enumerating all the file extensions through the **File extension is** condition. Use the **Apply restrictions to only unsupported file extensions** configuration to create a blanket policy to place controls on files like .mp3, .wav, and .dat.

Caution

The ability to apply controls to all files is a powerful capability. If you implement this capability without proper caution, the policy might have unintended consequences. Test this policy in a nonproduction environment before deploying it to your production environment. The unsupported-files policy example also shows how you can (optionally) exclude specific file extensions from the scope of the policy.

Important

When you select the **Audit or restrict activities on devices** action in the policy configuration **Actions**, the **Apply restrictions to only unsupported file extensions** shows up. **Apply restrictions to only unsupported file extensions** configuration option ***DOES NOT*** support scoping by **Device and device groups** in the policy location setting.

These actions are supported:

- Upload to a restricted cloud service domain
- Copy to a removable USB device
- Copy to a network share
- Print

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important policy design. [This article](dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

## Policy intent statement and mapping

*There are many types of files that endpoint DLP doesn't scan, more than we can track. We don't know if there is sensitive information in those files, and so we want to have a checkpoint in place before our user try to copy those files to a USB device or to a network share. We don't want to disrupt users workflow for the **abc** file type which is well known to us and poses no threat of data leakage.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “There are many types of files that endpoint DLP doesn't scan,...” | - Administrative scope: **Full directory**- Where to monitor: **Enterprise applications & devices**, **Devices**- Scope: **Allusers, groups, devices, device groups** |
| "...We don't want to disrupt users workflow for the **abc** file type which is well known to us and poses no threat of data leakage." | - Endpoint settings: create a Unsupported file extension exclusions list and add the file extension **abc** to the list. |
| "...more than we can track. We don't know if there is sensitive information in those files, and so we want to have a checkpoint in place before they try to copy those files to a USB device or to a network share..." | - Conditions for a match: **Document could not be scanned** action : select **audit or restrict activities on devices**- clear **Upload to a restriced cloud service domain or access from an unallowed browser**- select **Apply restrictions to specific activity**- select **Copy to a removable USB device**, and **Block with override**- select **Copy to a network share and Block with override**- clear **Copy to clipboard**, **Print**, **Copy or move using unallowed Bluetooth app**, and **Copy or move using RDP**- select **file could not be scanned**. - select **apply restrictions to only unsupported file extensions**. |

Important

The difference between the **Apply restrictions to only unsupported file extensions** option and the **File extension is** condition is:

- Endpoint DLP scans content for **File extension is** condition. For example, you see **Sensitive info type** value on the event or alert; on the other hand, the **Apply restrictions to only unsupported file extensions** option doesn't scan file content.
- **File extension is** condition triggering content scanning might consume higher machine resource, like CPU and memory, and might cause application performance issue for some file types.

## Steps to add a file type to unsupported file extension exclusions

Use the **Unsupported file extension exclusions** setting to exclude file extensions from the policy.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com)
2. Open **Settings** &gt; **Data Loss Prevention** &gt; **Endpoint DLP settings** &gt; **Unsupported file extension exclusions**.
3. Select **Add file extensions**.
4. Provide extensions.
5. Select **Save**.
6. Close the item.

## Steps to configure policy actions

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open **Data Loss Prevention** &gt; **Policies**.
3. Select **Enterprise applications & devices**.
4. Select **Create policy** and select the **Custom** from the **Categories** then **Custom policy** template from **Regulations**.
5. Name your new policy and provide a description.
6. Select **Full directory** under **Admin units**.
7. Scope the location to **Devices** only.
8. Create a rule where:
    1. In **Conditions**:
        1. Select **Document could not be scanned**.
    2. In **Actions**:
        1. Select **Audit or restrict activities on devices**.
        2. Clear **Upload to a restriced cloud service domain or access from an unallowed browser**.
        3. Select **Apply restrictions to specific activity**.
        4. Select **Copy to a removable USB device**, and **Block with override**.
        5. Select **Copy to a network share**, and **Block with override**.
        6. Clear **Copy to clipboard**, **Print**, **Copy or move using unallowed Bluetooth app**, and **Copy or move using RDP**.
        7. Select **Apply restrictions to only unsupported file extensions**.
9. **Save**.
10. Choose **Turn on the policy immediately**. Choose **Next**.
11. Review your settings and choose **Submit**.

Important

You can't use **Document could not be scanned** together with other conditions in the "Apply controls to all unsupported files" scenario.