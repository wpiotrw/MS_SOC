---
layout: Conceptual
title: Disable Purview Data Loss Prevention scanning for some supported files and apply controls | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-create-policy-disable-scan-supported-files
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
description: Create a DLP policy that disables scanning for specific supported file types and applies controls.
ai-usage: ai-assisted
locale: en-us
document_id: a157ff2f-9984-9438-4dfc-c3bae325d5ac
document_version_independent_id: a157ff2f-9984-9438-4dfc-c3bae325d5ac
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-create-policy-disable-scan-supported-files.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-create-policy-disable-scan-supported-files
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-create-policy-disable-scan-supported-files.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 97d5ab9a-c7a4-f824-c428-59b1dd25bbf5
---

# Disable Purview Data Loss Prevention scanning for some supported files and apply controls | Microsoft Learn

This article shows you how to create a Microsoft Purview data loss prevention (DLP) policy that disables scanning for selected supported file types and applies audit or restriction controls to those files, using the process described in [Design a data loss prevention policy](dlp-policy-design#design-a-data-loss-prevention-policy). Work through this scenario in your test environment to familiarize yourself with the policy creation UI.

Disable scanning for some supported files and apply controls is in *preview*.

Use the disable-classification configuration to save local resource consumption by disabling scanning of some file types on the [Monitored files](/en-us/purview/endpoint-dlp-learn-about) list. You can apply Audit, Block, or Block with override controls to those file types.

Important

This feature only supports the following action types:

- Upload to a restricted cloud service domain
- Copy to a removable USB device
- Copy to a network share
- Print

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important as policy design. [This article](dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

## Policy intent statement and mapping

*Bellows College needs to conserve resources on all our users Windows devices and cutting down on the scanning of files by DLP would be a big help. We have a list of file types that we know the contents of because they are auto generated. These file types are on the supported file types list. There's no need to scan these auto generated files, but we do want to prevent users from copying them to a USB device or to a network share. When they do try, we want to let them know, to educate them, that they are attempting a prohibited action.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “Bellows College needs to conserve resources on all our users Windows devices and cutting down on the scanning of files by DLP would be a big help...” | - Administrative scope: **Full directory**- Where to monitor: **Enterprise applications & devices**, **Devices**-Scope: **Allusers, groups, devices, device groups** |
| "...We have a list of file types that we know the contents of because they are auto generated. These file types are on the supported file types list. There's no need to scan these auto generated files..." | - Endpoint settings: create a **File extension group**- Disable classification |
| ...but we do want to prevent users from copying them to a USB device or to a network share... | - Conditions for a match: **Document could not be scanned** Action : select **audit or restrict activities on devices**- clear **Upload to a restriced cloud service domain or access from an unallowed browser**- select **Apply restrictions to specific activity**- select **Copy to a removable USB device**, &gt; **Block**- **Copy to a network share** &gt; **Block**- clear **Copy to clipboard**, **Print**, **Copy or move using unallowed Bluetooth app**, and **Copy or move using RDP**- select **file could not be scanned**. |
| "...When they do try, we want to let them know, to educate them, that they are attempting a prohibited action..." | - Use notifications to inform your users and help educate them on the proper use of sensitive info: **On**- Endpoint devices &gt; Show users a policy tip notification when an activity is restricted...: **selected**- Customize the notification: **selected** &gt; **Notication Title**: Bellows College IT don't copy files &gt; **Notification Content**: FYI, Bellows College data loss prevention policies don't let you copy that type of file to USB device or a network share |

## Create a File extension group

Select the appropriate tab for the portal you're using. To learn more about the Microsoft Purview portal, see [Microsoft Purview portal](/en-us/purview/purview-portal).

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open **Settings** &gt; **Data Loss Prevention** &gt; **Endpoint DLP settings** &gt; **File extension groups**.
3. Select **Create file extension group** and enter a **Group name**. In this scenario, we use `Student Class Registration file extensions`.
4. Enter the extensions.
5. Select **Save**.
6. Close the item.

## Disable classification

Use the **Disable classification** setting to exclude specific file extensions from Endpoint DLP classification.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open **Settings** &gt; **Data Loss Prevention** &gt; **Endpoint DLP settings** &gt; **Disable classification**.
3. Select **Add or edit file extensions**.
4. Enter the extensions.
5. Select **Save**.
6. Close the item.

## Configure policy actions

Perform the following steps to configure the policy actions for this scenario.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open **Data Loss Prevention** &gt; **Policies**.
3. Select **Create policy**.
4. Select **Enterprise applications & devices**.
5. Select **Custom** from the **Categories** then select **Custom policy** template from **Regulations**.
6. Name your new policy and provide a description.
7. Select **Full directory** under **Admin units**.
8. Scope the location to **Devices** only.
9. Create a rule where:
    1. In **Conditions**:
        1. **Document could not be scanned**.
    2. In **Actions**:
        1. Select: **Audit or restrict activities on devices**.
        2. Select: **Apply restrictions to specific activity**.
        3. Clear: **Copy to clipboard**.
        4. Select: **Copy to a removable USB device** &gt; **Block**.
        5. Select: **Copy to a network share** &gt; **Block**.
        6. Clear: **Print**.
        7. Clear: **Copy or move using unallowed Bluetooth app**.
        8. Clear: **Copy or move using RDP**.
        9. Clear: **Access by restricted apps**.
        10. Select: **Apply restrictions to only unsupported file extensions**.
        11. Select: **Add file extension group** and select `Student Class Registration file extensions`.
    3. **Save**.
10. Choose **Turn it on right away**. Choose **Next**.
11. Review your settings and choose **Submit**.

Important

You can't use the **Document could not be scanned** condition with other conditions in this policy scenario.