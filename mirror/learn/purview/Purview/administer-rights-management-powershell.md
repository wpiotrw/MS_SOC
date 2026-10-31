---
layout: Conceptual
title: Administering the Azure Rights Management service by using PowerShell | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/administer-rights-management-powershell
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
description: Learn how you can use the PowerShell module for the Azure Rights Management service from Microsoft Purview Information Protection, to administer this encryption service for your tenant.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: b387f5ad-6f80-ba51-3cd8-37d9114d91f5
document_version_independent_id: b387f5ad-6f80-ba51-3cd8-37d9114d91f5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/administer-rights-management-powershell.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: administer-rights-management-powershell
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/administer-rights-management-powershell.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 0476dc72-b7bb-440c-141f-33ab9f189c77
---

# Administering the Azure Rights Management service by using PowerShell | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

PowerShell is required to manually activate the Azure Rights Management encryption service, and you also need PowerShell for some advanced configurations. Some configurations can be done from the Microsoft Purview portal, however, you might prefer to use PowerShell for more efficient command-line control and scripting.

The following table lists some of the advanced configuration scenarios that use PowerShell. When the configuration can also be completed without using PowerShell, this information is also included in the table.

For a complete list of the available cmdlets for this module, with more information about each one, see [AIPService](/en-us/powershell/azure/aip/overview#aipservice).

To install this PowerShell module, see [Install the AIPService PowerShell module for the Azure Right Management service](/en-us/azure/information-protection/install-powershell).

Tip

In addition to this service-side PowerShell module, the Microsoft Purview Information Protection client installs a supplemental PowerShell module, [PurviewInformationProtection](/en-us/powershell/azure/aip/overview#purviewinformationprotection).

This client module supports labeling and encrypting multiple files so that, for example, you can bulk-protect all files in a folder. For more information, see [Set up the information protection client using PowerShell](/en-us/powershell/azure/aip/setup-information-protection-client-powershell).

## Cmdlets grouped by administration task

The following table groups common administration tasks by the cmdlets used to complete them.

| If you need to… | …use the following cmdlets |
| --- | --- |
| Migrate from on-premises Rights Management (AD RMS or Windows RMS) to the Azure Rights Management service from Microsoft Purview Information Protection. | [Import-AipServiceTpd](/en-us/powershell/module/aipservice/import-aipservicetpd)[Set-AipServiceKeyProperties](/en-us/powershell/module/aipservice/set-aipservicekeyproperties) |
| Connect to or disconnect from the Rights Management service for your organization. | [Connect-AipService](/en-us/powershell/module/aipservice/connect-aipservice)[Disconnect-AipServiceService](/en-us/powershell/module/aipservice/disconnect-aipservice) |
| Generate and manage your own root key for the Azure Rights Management service – the bring your own key (BYOK) scenario. | [Set-AipServiceKeyProperties](/en-us/powershell/module/aipservice/set-aipservicekeyproperties)[Use-AipServiceKeyVaultKey](/en-us/powershell/module/aipservice/use-aipservicekeyvaultkey)[Get-AipServiceKeys](/en-us/powershell/module/aipservice/get-aipservicekeys) |
| Activate or deactivate the Azure Rights Management service for your organization. | [Enable-AipService](/en-us/powershell/module/aipservice/enable-aipservice)[Disable-AipService](/en-us/powershell/module/aipservice/disable-aipservice) |
| Configure onboarding controls for a phased deployment of the Azure Rights Management service. | [Get-AipServiceOnboardingControlPolicy](/en-us/powershell/module/aipservice/get-aipserviceonboardingcontrolpolicy)[Set-AipServiceOnboardingControlPolicy](/en-us/powershell/module/aipservice/set-aipserviceonboardingcontrolpolicy) |
| Create and manage Rights Management templates for your organization. | [Add-AipServiceTemplate](/en-us/powershell/module/aipservice/add-aipservicetemplate)[Export-AipServiceTemplate](/en-us/powershell/module/aipservice/export-aipservicetemplate)[Get-AipServiceTemplate](/en-us/powershell/module/aipservice/get-aipservicetemplate)[Get-AipServiceTemplateProperty](/en-us/powershell/module/aipservice/get-aipservicetemplateproperty)[Import-AipServiceTemplate](/en-us/powershell/module/aipservice/import-aipservicetemplate)[New-AipServiceRightsDefinition](/en-us/powershell/module/aipservice/new-aipservicerightsdefinition)[Remove-AipServiceTemplate](/en-us/powershell/module/aipservice/remove-aipservicetemplate)[Set-AipServiceTemplateProperty](/en-us/powershell/module/aipservice/set-aipservicetemplateproperty) |
| Configure the maximum number of days that content that your organization encrypts can be accessed without an internet connection (the use license validity period). | [Get-AipServiceMaxUseLicenseValidityTime](/en-us/powershell/module/aipservice/get-aipservicemaxuselicensevaliditytime)[Set-AipServiceMaxUseLicenseValidityTime](/en-us/powershell/module/aipservice/set-aipservicemaxuselicensevaliditytime) |
| Manage the super user feature of the Azure Rights Management service for your organization. | [Enable-AipServiceSuperUserFeature](/en-us/powershell/module/aipservice/enable-aipservicesuperuserfeature)[Disable-AipServiceSuperUserFeature](/en-us/powershell/module/aipservice/disable-aipservicesuperuserfeature)[Add-AipServiceSuperUser](/en-us/powershell/module/aipservice/add-aipservicesuperuser)[Get-AipServiceSuperUser](/en-us/powershell/module/aipservice/get-aipservicesuperuser)[Remove-AipServiceSuperUser](/en-us/powershell/module/aipservice/remove-aipservicesuperuser)[Set-AAipServiceSuperUserGroup](/en-us/powershell/module/aipservice/set-aipservicesuperusergroup)[Get-AipServiceSuperUserGroup](/en-us/powershell/module/aipservice/get-aipservicesuperusergroup)[Clear-AipServiceSuperUserGroup](/en-us/powershell/module/aipservice/clear-aipservicesuperusergroup) |
| Manage users and groups who are authorized to administer the Azure Rights Management service for your organization. | [Add-Aip-ServiceRoleBasedAdministrator](/en-us/powershell/module/aipservice/add-aipservicerolebasedadministrator)[Get-Aip-ServiceRoleBasedAdministrator](/en-us/powershell/module/aipservice/get-aipservicerolebasedadministrator)[Remove-Aip-ServiceRoleBasedAdministrator](/en-us/powershell/module/aipservice/remove-aipservicerolebasedadministrator) |
| Get a log of the Azure Rights Management service administrative tasks for your organization. | [Get-AipServiceAdminLog](/en-us/powershell/module/aipservice/get-aipserviceadminlog) |
| Log and analyze usage logging for the Azure Rights Management service. | [Get-AipServiceUserLog](/en-us/powershell/module/aipservice/get-aipserviceuserlog) |
| Display the current configuration of the Azure Rights Management service for your organization. | [Get-AipServiceConfiguration](/en-us/powershell/module/aipservice/get-aipserviceconfiguration) |
| Migrate your organization from the Azure Rights Management service to an on-premises AD RMS deployment. | [Set-AipServiceMigrationUrl](/en-us/powershell/module/aipservice/set-aipservicemigrationurl)[Get-AipServiceMigrationUrl](/en-us/powershell/module/aipservice/get-aipservicemigrationurl) |
| Manage the legacy document tracking site for rights-protected documents | [Disable-AipServiceDocumentTrackingFeature](/en-us/powershell/module/aipservice/disable-aipservicedocumenttrackingfeature)[Enable-AipServiceDocumentTrackingFeature](/en-us/powershell/module/aipservice/enable-aipservicedocumenttrackingfeature)[Get-AipServiceDocumentTrackingFeature](/en-us/powershell/module/aipservice/get-aipservicedocumenttrackingfeature)[Set-AipServiceDoNotTrackUserGroup](/en-us/powershell/module/aipservice/set-aipservicedonottrackusergroup)[Clear-AipServiceDoNotTrackUserGroup](/en-us/powershell/module/aipservice/Clear-AipServiceDoNotTrackUserGroup)[Get-AipServiceDoNotTrackUserGroup](/en-us/powershell/module/aipservice/get-AipServiceDoNotTrackUserGroup)[Get-AipServiceTrackingLog](/en-us/powershell/module/aipservice/Get-AipServiceTrackingLog)[Get-AipServiceDocumentLog](/en-us/powershell/module/aipservice/Get-AipServiceDocumentLog) |