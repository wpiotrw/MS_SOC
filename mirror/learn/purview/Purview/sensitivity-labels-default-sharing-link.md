---
layout: Conceptual
title: Use sensitivity labels to configure the default sharing link type | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sensitivity-labels-default-sharing-link
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2024-10-21T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
- SPO_Content
search.appverid:
- MOE150
- MET150
description: Use sensitivity labels to configure the default sharing link type for sites and documents in SharePoint and OneDrive.
locale: en-us
document_id: d0e0bd0b-b65a-4bb1-ffad-7e65cf700be9
document_version_independent_id: d0e0bd0b-b65a-4bb1-ffad-7e65cf700be9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sensitivity-labels-default-sharing-link.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sensitivity-labels-default-sharing-link
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sensitivity-labels-default-sharing-link.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 3a2a80ed-a399-f339-9291-e2818bfc3c47
---

# Use sensitivity labels to configure the default sharing link type | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

As an additional configuration to the settings you see in the Microsoft Purview portal for [sensitivity labels](sensitivity-labels), you can use these labels to configure settings for the default sharing link type for a SharePoint site or OneDrive account, and for individual documents. These settings are automatically selected, but not highly visible to users when they select the **Share** button in their Office apps. As an example:

![Example default sharing link dialog box.](media/default-sharing-link-example.png)

The default sharing link type sets the scope (who) and permissions (view or edit) that are automatically selected when users share files and folders. Although users can always override these default settings before sending the sharing link, the settings you choose provide a safe baseline. Typically, users don't change the settings before sharing.

At the site level (SharePoint site or OneDrive account), sensitivity labels provide a convenient alternative for setting the default sharing link type that can be configured for a site in the SharePoint admin center. For more information, see [Change the default link type for a site](/en-us/sharepoint/change-default-sharing-link) from the SharePoint documentation.

This site-level configuration works well for SharePoint sites that have documents all with the same level of sensitivity. But if sites contain some documents that have a higher level of sensitivity that require more restrictive settings, you can configure a sensitivity label with different settings for the default sharing link type, and then apply this label to documents.

In this scenario where the site has default sharing link type settings, and a document in that site has different default link type settings, the more restrictive scope settings will be applied at the time the user selects the sharing option for the document. For example:

- The default sharing link type for the site is scoped to anybody in your organization. A document in that site is labeled with the default sharing link type set to specific people. When a user shares that document, the default sharing link type selected will be scoped to specific people.
- The default sharing link type for the site is scoped to specific people, with edit permissions. A document in that site is labeled with the default sharing link type set to anybody in the organization, with view permissions. When a user shares that document, the default sharing link type selected will be scoped to specific people with edit permissions.

Configuring the default link type for documents might also be appropriate without the site-level setting. For example, although SharePoint sites are typically organized to host the same type of documents, that isn't the case for OneDrive accounts. Users typically save a wide range of files to OneDrive, often including a mix of personal and business documents. Setting a default link type for all documents for a user's OneDrive account is probably not practical, but individual documents can still benefit from these settings. For example:

- Documents labeled **Highly Confidential** have a default sharing link type that restricts sharing to specific people rather than anybody in the organization.
- Documents labeled **General** have a default sharing link type that restricts sharing to people in your organization.
- Documents labeled **Personal** have a default sharing link type that allows sharing to anyone with the link.

## Prerequisites

To apply the default sharing link type for sites, sensitivity labels must be enabled for containers. If this capability isn't yet enabled for your tenant, see [How to enable sensitivity labels for containers and synchronize labels](sensitivity-labels-teams-groups-sites#how-to-enable-sensitivity-labels-for-containers-and-synchronize-labels).

To apply the default sharing link type for documents in SharePoint and OneDrive, sensitivity labels must be enabled for these services. If this capability isn't yet enabled for your tenant, see [How to enable sensitivity labels for SharePoint and OneDrive (opt-in)](sensitivity-labels-sharepoint-onedrive-files#how-to-enable-sensitivity-labels-for-sharepoint-and-onedrive-opt-in).

In a PowerShell session, you must [connect to Security & Compliance PowerShell](/en-us/powershell/exchange/office-365-scc/connect-to-scc-powershell/connect-to-scc-powershell) to configure the settings for the default sharing link type.

Note

Although not required, it's easiest to first [create and configure sensitivity labels in the Microsoft Purview portal](create-sensitivity-labels), and then modify these labels with the settings that configure the default sharing link type.

## How to configure settings for the default sharing link type

The configuration settings for the default sharing link type use the PowerShell *AdvancedSettings* parameter with the [Set-Label](/en-us/powershell/module/exchange/set-label) and [New-Label](/en-us/powershell/module/exchange/new-labelpolicy) cmdlets from [Security & Compliance PowerShell](/en-us/powershell/exchange/scc-powershell):

- **DefaultSharingScope**: The available values are:

    - **SpecificPeople**: Sets the default sharing link to specific people (only the people the user specifies)
    - **Organization**: Sets the default sharing link for only people in your organization
    - **Anyone**: Sets the default sharing link to anyone with the link, which is equivalent to anonymous access
- **DefaultShareLinkPermission**: The available values are:

    - **View**: Sets the default link permission to view permissions
    - **Edit**: Sets the default link permission to edit permissions

These two settings and values are the equivalent of the parameters *DefaultSharingScope* and *DefaultShareLinkPermission* from the [Set-SPOSite](/en-us/powershell/module/sharepoint-online/set-sposite) cmdlet.

Another configuration for the default sharing link type is to use the **DefaultShareLinkToExistingAccess** advanced setting, which is the equivalent of the parameter *DefaultLinkToExistingAccess* from the [Set-SPOSite](/en-us/powershell/module/sharepoint-online/set-sposite) cmdlet. When you set this value to **True**, it overrides the other two advanced settings and their values.

PowerShell examples, where the sensitivity label GUID is **8faca7b8-8d20-48a3-8ea2-0f96310a848e**:

- To set the default sharing link type to SpecificPeople:

    ```powershell
    Set-Label -Identity 8faca7b8-8d20-48a3-8ea2-0f96310a848e -AdvancedSettings @{DefaultSharingScope="SpecificPeople"}
    ```
- To set the default sharing link type permissions to Edit:

    ```powershell
    Set-Label -Identity 8faca7b8-8d20-48a3-8ea2-0f96310a848e -AdvancedSettings @{DefaultShareLinkPermission="Edit"}
    ```
- To set the default sharing link type to people with existing access:

    ```powershell
    Set-Label -Identity 8faca7b8-8d20-48a3-8ea2-0f96310a848e -AdvancedSettings @{DefaultShareLinkToExistingAccess="True"}
    ```

For more help to specify PowerShell advanced settings, see [PowerShell tips for specifying the advanced settings](create-sensitivity-labels#powershell-tips-for-specifying-the-advanced-settings).

To configure the settings for the default sharing link type for a site, the [scope of the sensitivity label](sensitivity-labels#label-scopes) must include **Groups & sites** when you create the sensitivity label in the Microsoft Purview portal. After it's created, you see this displayed as **Site, UnifiedGroup** in the **Scope** column on the **Labels** page, and the PowerShell *ContentType* setting also displays this same value. For documents, the scope must include **Files & other data assets**, which displays as **File, Email**. Then:

- When the scope includes **Groups & sites**, you can apply the label to a site, which sets the default sharing link type for that site. For information how to apply a sensitivity label to a site, see [How to apply sensitivity labels to containers](sensitivity-labels-teams-groups-sites#how-to-apply-sensitivity-labels-to-containers).
- When the scope of the sensitivity label includes **Files & other data assets**, you can apply the label to documents, which sets the default sharing link type for that document. The label can be applied [manually](https://support.microsoft.com/office/apply-sensitivity-labels-to-your-files-and-email-in-office-2f96e7cd-d5a4-403b-8bd7-4cc636bae0f9) or [automatically](apply-sensitivity-label-automatically).

Tip

You can also specify that the label is the default sensitivity label to be applied for new sites or new documents, as a [label policy setting](sensitivity-labels#what-label-policies-can-do).