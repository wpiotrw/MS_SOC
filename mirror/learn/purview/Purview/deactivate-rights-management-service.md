---
layout: Conceptual
title: Deactivate the Azure Rights Management encryption service from Microsoft Purview Information Protection | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/deactivate-rights-management-service
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
ms.reviewer: tommoser
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-encryption
ms.collection:
- purview-compliance
description: Information and instructions if you no longer want to use the Azure Rights Management encryption service from Microsoft Purview Information Protection.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 44f62216-ff2d-2b37-d61d-f372d41cc1c9
document_version_independent_id: 44f62216-ff2d-2b37-d61d-f372d41cc1c9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/deactivate-rights-management-service.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: deactivate-rights-management-service
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/deactivate-rights-management-service.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: fc60a1fb-139f-5d49-7d3d-2917b4fa80ed
---

# Deactivate the Azure Rights Management encryption service from Microsoft Purview Information Protection | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

You're always in control of whether your organization protects content by using the Azure Rights Management encryption service from Microsoft Purview Information Protection. If you decide you no longer want to use this encryption service, you have the assurance that you won’t be locked out of content that was previously encrypted.

If you don’t need continued access to previously encrypted content, deactivate the Azure Rights Management encryption services and let your supporting subscription for this service expire. For example, this would be appropriate for when you have completed testing Microsoft Purview Information Protection before you deploy it in a production environment.

However, if you have deployed Microsoft Purview Information Protection in production and encrypted items by using the Azure Rights Management service, make sure that you have a copy of your Azure Rights Management service root key and suitable trusted publishing domain (TPD) before you deactivate the Azure Rights Management service. Make sure that you have a copy of your key and the TPD before your subscription expires to ensure that you can retain access to content that was encrypted by Azure Rights Management after the service is deactivated.

If you used the bring your own key solution (BYOK) where you generate and manage your own key in an HSM, you already have your Azure Rights Management root key. You'll also have a suitable TPD if you followed the instructions that [prepare for a future cloud exit](https://techcommunity.microsoft.com/t5/Azure-Information-Protection/How-to-prepare-an-Azure-Information-Protection-Cloud-Exit-plan/ba-p/382631). However, if your Azure Rights Management root key was managed by Microsoft (the default), see the instructions for exporting your root key in the [Manage the root key for your tenant's Azure Rights Management service](rights-management-tenant-key) article.

Tip

Even after your subscription expires, your tenant remains available for consuming encrypted content for an extended period. However, you will no longer be able to export your root key from the Azure Rights Management service.

When you have your Azure Rights Management service root key and the TPD, you can deploy Rights Management on premises (AD RMS) and import your Azure Rights Management root key as a trusted publishing domain (TPD). You then have the following options for decommissioning your Microsoft Purview Information Protection deployment:

| If this applies to you … | … do this: |
| --- | --- |
| You want all users to continue using Rights Management, but use an on-premises solution rather than using the Azure Rights Management service → | Redirect your clients to the on-premises deployment by using the **LicensingRedirection** registry key for Office apps. For instructions, see [Configure service discovery in the RMS client deployment notes](/en-us/azure/information-protection/rms-client/client-deployment-notes). |
| You want to stop using Rights Management technologies completely → | Grant a designated administrator [super user rights for Microsoft Purview encryption](encryption-super-users) and install the [Microsoft Purview Information Protection client](information-protection-client) for this user.This administrator can then use the PowerShell module from this client to bulk-decrypt files in folders that were encrypted by the Azure Rights Management service. Files revert to being unencrypted and can therefore be read without a Rights Management technology such as Microsoft Purview Information Protection or AD RMS. Because this PowerShell module can be used with both Microsoft Purview Information Protection and AD RMS, you have the choice of decrypting files before or after you deactivate the Azure Rights Management service, or a combination. |
| You can't identify all the files that were encrypted by the Azure Rights Management service. Or, you want all users to be able to automatically read any encrypted items that were missed → | Deploy a registry setting on all client computers by using the **LicensingRedirection** registry key for Office apps, as described in [Configure service discovery in the RMS client deployment notes](/en-us/azure/information-protection/rms-client/client-deployment-notes). |
| You want a controlled, manual recovery service for any files that were missed → | Grant designated users in a data recovery group [super user rights for Microsoft Purview encryption](encryption-super-users) and install the [Microsoft Purview Information Protection client](information-protection-client) for these users so that they can decrypt files when this action is requested by standard users.On all computers, deploy the registry setting to prevent users from encrypting new files by setting **DisableCreation** to **1**, as described in [Office registry settings for the DisableCreation policy](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd772637%28v=ws.10%29). |

For more information about the decommissioning options for your Microsoft Purview Information Protection deployment, see the following resources:

- For information about AD RMS and deployment references, see [Active Directory Rights Management Services Overview](/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831364%28v=ws.11%29).
- For instructions to import your Azure Rights Management service root key as a TPD file, see [Add a Trusted Publishing Domain](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc771460%28v=ws.11%29).
- To use PowerShell with the Microsoft Purview Information Protection client, see [Set up the information protection client using PowerShell](/en-us/powershell/azure/aip/setup-information-protection-client-powershell).

When you're ready to deactivate the Azure Rights Management encryption service, use the following instructions.

## Deactivate the Azure Rights Management service

You must use PowerShell to deactivate the Azure Rights Management service from Microsoft Purview Information Protection. You can no longer activate or deactivate this encryption service from admin portals.

Before you begin, ensure you have an account with permissions to manage the Azure Rights Management service, such as a Compliance Administrator or Compliance Data Administrator for your tenant.

1. Install the AIPService module, to configure and manage the Azure Rights Management service. For instructions, see [Install the AIPService PowerShell module for the Azure Right Management service](/en-us/azure/information-protection/install-powershell).
2. From a PowerShell session, run [Connect-AipService](/en-us/powershell/module/aipservice/connect-aipservice), and when prompted, provide the credentials for an account that has permissions to manage the Azure Rights Management service, such as a Compliance Administrator or Compliance Data Administrator for your tenant.
3. Run [Get-AipService](/en-us/powershell/module/aipservice/get-aipservice) to confirm the current status of the Azure Rights Management service. A status of **Enabled** confirms activation; **Disabled** indicates that the service is deactivated.
4. To deactivate the service, run [Disable-AipService](/en-us/powershell/module/aipservice/disable-aipservice).
5. Run [Get-AipService](/en-us/powershell/module/aipservice/get-aipservice) again to confirm the encryption service is now deactivated. This time, the status should display **Disabled**.
6. Run [Disconnect-AipService](/en-us/powershell/module/aipservice/disconnect-aipservice) to disconnect from the service, and close your PowerShell session.