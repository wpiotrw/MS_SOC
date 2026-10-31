---
layout: Conceptual
title: Activating the Azure Rights Management encryption service from Microsoft Purview Information Protection | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/activate-rights-management-service
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
ms.reviewer: tommoser
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-encryption
ms.collection:
- purview-compliance
description: Learn how to activate the Azure Rights Management service to encrypt items such as documents and emails.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: b66afdf6-3e33-38da-a6e1-1559549cd181
document_version_independent_id: b66afdf6-3e33-38da-a6e1-1559549cd181
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/activate-rights-management-service.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: activate-rights-management-service
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/activate-rights-management-service.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: c2b0f94e-38a6-7ca9-60cd-284eaf1b2192
---

# Activating the Azure Rights Management encryption service from Microsoft Purview Information Protection | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

This article describes how administrators can activate the Azure Rights Management encryption service for [Microsoft Purview Information Protection](information-protection). When this encryption service is activated for your organization, administrators and users can start to protect important data by using apps and services that support this encryption solution. Administrators can also manage and monitor encrypted items that your organization owns.

The configuration information in this article is for administrators who are responsible for a service that applies to all users in an organization. If you are looking for user help and information to use the Rights Management functionality for a specific application or how to open a file or email that is rights-protected, use the help and guidance that accompanies your application.

## Automatic activation for the Azure Rights Management service

When you have a service plan that includes the Azure Rights Management service, you may not have to activate the service:

- **If your subscription that includes the Azure Rights Management service, Azure Information Protection (former name), or Microsoft Purview Information Protection was obtained towards the end of February 2018 or later**: The service is automatically activated for you. You do not have to activate the service unless you or another administrator for your organization deactivated the Azure Rights Management service.
- **If your subscription that includes the Azure Rights Management service, Azure Information Protection (former name), or Microsoft Purview Information Protection was obtained before or during February 2018**: Microsoft activates the Azure Rights Management service for these subscriptions if your tenant is using Exchange Online. For these subscriptions, the service will be activated for you unless you see that **AutomaticServiceUpdateEnabled** is set to **false** when you run [Get-IRMConfiguration](/en-us/powershell/module/exchange/encryption-and-certificates/get-irmconfiguration).

If neither of the listed scenarios apply to you, you must manually activate the Azure Rights Management service.

## How to activate or confirm the status of the encryption service

Important

Do not activate the Azure Rights Management service if you have Active Directory Rights Management Services (AD RMS) deployed for your organization. [Prepare your environment for AD RMS](/en-us/azure/information-protection/prepare-environment-adrms).

To activate the Azure Rights Management service, your organization must have a service plan that includes the Azure Rights Management service from Microsoft Purview Information Protection. For details about required service plans, see [Microsoft 365 licensing guidance for security & compliance](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance).

When the Azure Rights Management service is activated, all users in your organization can apply encryption to items such as documents and emails, and all users can open (consume) items that have been encrypted by this service. However, if you prefer, you can restrict who can apply this encryption, by using onboarding controls for a phased deployment. For more information, see the Configuring onboarding controls for a phased deployment section in this article.

### Activate the Azure Rights Management service via PowerShell

You must use PowerShell to activate the Azure Rights Management service. You can no longer activate or deactivate this service from admin portals.

1. Install the AIPService module to configure and manage the Azure Rights Management service. For instructions, see [Install the AIPService PowerShell module for the Azure Right Management service](/en-us/azure/information-protection/install-powershell).
2. Use the [Connect-AipService](/en-us/powershell/module/aipservice/connect-aipservice) cmdlet to connect your PowerShell session to the Azure Rights Management service. Run `Connect-AipService` and sign in with a [role that has permissions](/en-us/defender-office-365/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview) to activate the Azure Rights Management service for your tenant. For example, the compliance administrator role, or compliance data administrator role.
3. Run [Get-AipService](/en-us/powershell/module/aipservice/get-aipservice) to confirm whether the Azure Rights Management service is activated. A status of **Enabled** confirms activation; **Disabled** indicates that the service is deactivated.
4. To activate the service, run [Enable-AipService](/en-us/powershell/module/aipservice/enable-aipservice).

## Configuring onboarding controls for a phased deployment

If you don’t want all users to be able to encrypt documents and emails immediately by using the Azure Rights Management service, you can configure user onboarding controls by using the [Set-AipServiceOnboardingControlPolicy](/en-us/powershell/module/aipservice/set-aipserviceonboardingcontrolpolicy) PowerShell command. You can run this command before or after you activate the Azure Rights Management service.

For example, if you initially want only administrators in the “IT department” group (that has an object ID of aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb) to be able to protect content for testing purposes, use the following command:

```powershell
Set-AipServiceOnboardingControlPolicy -UseRmsUserLicense $False -SecurityGroupObjectId "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb"
```

For this configuration option, you must specify a group; you can't specify individual users. To get the object ID for the group, you can use the Microsoft Graph PowerShell—for example, for version 1.0 of the module, use the [Get-MgGroup](/en-us/powershell/module/microsoft.graph.groups/get-mggroup) command. Or, you can copy the **Object ID** value of the group from the Azure portal.

Alternatively, if you want to ensure that only users who are correctly licensed to use the Azure Rights Management service can protect content:

```powershell
Set-AipServiceOnboardingControlPolicy -UseRmsUserLicense $True
```

When you no longer need to use onboarding controls, whether you used the group or licensing option, run:

```powershell
Set-AipServiceOnboardingControlPolicy -UseRmsUserLicense $False
```

For more information about this cmdlet and additional examples, see the [Set-AipServiceOnboardingControlPolicy](/en-us/powershell/module/aipservice/set-aipserviceonboardingcontrolpolicy) help.

When you use these onboarding controls, all users in the organization can always consume encrypted content that has been protected by your subset of users, but they won’t be able to apply encryption themselves from client applications. Server-side applications, such as Exchange, can implement their own per-user controls to achieve the same result. For example, to prevent users from protecting emails in Outlook on the web, use [Set-OwaMailboxPolicy](/en-us/powershell/module/exchange/client-access/set-owamailboxpolicy) to set the *IRMEnabled* parameter to *$false*.