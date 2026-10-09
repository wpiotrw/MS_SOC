---
layout: Conceptual
title: Add or delete custom device images for Windows 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/add-device-images
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how to add or delete custom device images for Windows 365.
keywords: 
author: ErikjeMS
ms.author: ivivano
manager: dougeby
ms.date: 2026-03-23T00:00:00.0000000Z
ms.topic: how-to
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: evas
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: 52efcec9-a315-2c4f-f9e3-edf32c0161d0
document_version_independent_id: 52efcec9-a315-2c4f-f9e3-edf32c0161d0
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/add-device-images.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/add-device-images
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/add-device-images.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ddab3cd8-636f-4a91-896e-1c23f399a6bd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f409bb5d-e203-40c5-9d95-0ee717231beb
platformId: a780688a-2a4f-233a-2595-7d8c99beb4fd
---

# Add or delete custom device images for Windows 365 | Microsoft Learn

If you want to use a custom device image, you can add it into your Azure subscription and then use it for provisioning Cloud PCs. You can use standard Marketplace gallery images or [create your own custom managed image](/en-us/azure/virtual-machines/windows/capture-image-resource). To convert, use the steps to [export an image version to a managed disk](/en-us/azure/virtual-machines/managed-disk-from-image-version) and then [create an image from a managed disk](/en-us/azure/virtual-machines/windows/capture-image-resource#create-an-image-from-a-snapshot-using-powershell).

- Images should not contain Azure Virtual Desktop components, including Remote Desktop Agent Boot Loader, Remote Desktop Services Infrastructure Agent, Remote Desktop Services Infrastructure Geneva Agent, and Remote Desktop Services SxS Network Stack. Additionally, you can't import Windows 10 and Windows 11 Multisession images into Windows 365.
- If deploying a virtual machine in Azure to create your customized managed image, you must select the 'Standard' security type when creating the virtual machine. Managed Images do not support [Trusted Launch virtual machines](/en-us/azure/virtual-machines/trusted-launch#unsupported-features). If you decide to import a custom image from an Azure Compute Gallery, you should choose an image that has Trusted Launch enabled on the image definition.
- Data disks attached to your custom image aren't supported in Windows 365.
- For information about support for Windows 11 custom device images, see [What's New for Windows 365 Enterprise](whats-new#support-for-windows-11).
- You can also use existing built-in [gallery images](device-images#gallery-images) without customization for a stream-lined experience.

## Add a custom device image from an Azure managed image

You can upload the custom image to the Windows 365 service by following these steps:

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431).
2. Select **Devices** &gt; **Provision Cloud PCs** &gt; **Custom images** &gt; **Add &gt; Managed image.**
3. In the **Add image** pane, provide the following information:

    - **Image name**: The name of the image you want to add. This name will show up in the list of Custom images in Intune.
    - **Image version**: A version number of the image with this format: Major(int).Minor(int).Patch(int) format. For example: 0.0.1, 1.5.13. This version will show up in the list of Custom images in Intune.
    - **Subscription**: Choose the Azure subscription where the image came from.
    - **Source Image**: Choose an image to add. The list will populate with all custom images from your chosen subscription that meet the prerequisites.
4. Select **Add** to add the image to your device image list.

After successfully uploading the image, you'll see the uploaded image when selecting an image to create a provisioning policy.

## Add a custom device image from an Azure Compute Gallery

Admins can also import custom images directly from an Azure Compute Gallery.

**Role/permissions required:**

[Compute Gallery Image Reader](/en-us/azure/role-based-access-control/built-in-roles/compute#compute-gallery-image-reader)

You can upload the custom image to the Windows 365 service by following these steps:

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431).
2. Select **Devices** &gt; **Provision Cloud PCs** &gt; **Custom images** &gt; **Add &gt; Azure Compute Gallery image**.

The admin will need to specify:

- **Image name:** The name of the image you want to add. This name will show up in the list of Custom images in Intune.
- **Image version:** A version number of the image with this format: Major(int).Minor(int).Patch(int) format. For example: 0.0.1, 1.5.13. This version will show up in the list of Custom images in Intune.
- **Subscription:** Choose the Azure subscription of the Azure Compute Gallery that contains the image.
- **Azure Compute Gallery:** Choose the name of the Azure Compute Gallery that contains the image.
- **Image definition:** Choose the image definition that contains the image. Note: this is populated automatically.
- **Image version:** Choose the image version that you want to upload.
- **Scope tag(s):** Adding a scope tag is optional.

Note that in order to import an Azure Compute Gallery image, the image definition should have the following options selected:

1. x64
2. Windows
3. Security type: Trusted Launch

## Delete a custom device image

You can delete a custom image from Windows 365 by following these steps:

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **Provision Cloud PCs** &gt; **Custom images**.
2. On the **Device images** page, select the check box next to the image &gt; **Delete**.
3. Select **Yes** on the confirmation pop up to permanently delete the image.

Device images being used in a provisioning policy can't be deleted. Delete the provisioning policy first and then the associated device image.