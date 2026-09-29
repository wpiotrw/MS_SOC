---
layout: Conceptual
title: Configure SharePoint with a sensitivity label to extend permissions to downloaded documents | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sensitivity-labels-sharepoint-extend-permissions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-02-23T00:00:00.0000000Z
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
description: Configure a SharePoint document library with a sensitivity label to extend existing permissions to documents that are downloaded, and protect files from being copied or moved.
locale: en-us
document_id: 7267b82b-0831-0980-7831-b32011310aa8
document_version_independent_id: 7267b82b-0831-0980-7831-b32011310aa8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sensitivity-labels-sharepoint-extend-permissions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sensitivity-labels-sharepoint-extend-permissions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sensitivity-labels-sharepoint-extend-permissions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 36fd6bb5-ab10-1957-19f0-1cf4714c7f23
---

# Configure SharePoint with a sensitivity label to extend permissions to downloaded documents | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

When SharePoint is [enabled for sensitivity labels](sensitivity-labels-sharepoint-onedrive-files), you can configure document libraries to extend the existing SharePoint site permissions to documents when they're downloaded from the library. Then, any previously unlabeled files from that library continue to be protected with the current SharePoint permissions for the user, even though the files have left the original SharePoint boundary.

For example, you select the **Confidential \ Trusted People** label as the sensitivity label to extend permissions for a document library. In that library, a site is configured to allow only read permissions to a specfiic group of users. A user from that group downloads a file from the site, and that file is now labeled as **Confidential \ Trusted People**. Even though the file is no longer in SharePoint, that user can still only view and not edit the content or remove the label. Only users with access to the file in SharePoint have access to the downloaded file. Users without access to the file in SharePoint won't be able to open that downloaded file, no matter where it's stored.

Additionally, the file has a just-in-time layer of protection because the user who downloaded the file also won't be able to open it under the following circumstances:

- Permissions for that user are removed from the file
- The file is deleted from the site
- The site is no longer active
- The file is moved to a different site

If the SharePoint permissions for the user are changed, those changes are reflected for the downloaded file.

When these labeled files are in the document library, they're also protected from copy and move actions:

- The files can't be copied to or moved to a different site.
- The files can be copied to or moved to a different document library within the same site only if the user has SharePoint permissions to create or delete lists.

The specified sensitivity label is applied to all files that are unlabeled, and to files that are labeled but the label configuration doesn't apply encryption. Files that are synchronized with OneDrive also get labeled.

For existing files that are labeled but not encrypted, a manually applied label is also replaced with the specified label. For a quick summary of the possible outcomes, see Will an existing label be overridden on this page.

Because unencrypted files can be relabeled, this labeling configuration is well-suited to organizations that are early in their labeling deployment and haven't yet labeled files in SharePoint sites by using other methods.

## Will an existing label be overridden?

Summary of outcomes:

| Existing label | Override with library label to extend permissions |
| --- | --- |
| Label applied using any methods (manual, automatic, default label from policy) and label configuration doesn't apply encryption, any priority | Yes |
| Label applied using any methods (manual, automatic, default label from policy) and label configuration does apply encryption, any priority | No |

## Requirements

- You've [created and published](create-sensitivity-labels) sensitivity labels, published to the users who will select the sensitivity label for a SharePoint document library. Labels require the following configuration:

    - The [label scope](sensitivity-labels#label-scopes) of **Files and other data assets**
    - Access control is selected with the encryption setting of **Let users assign permissions when they apply the label** and the checkbox **In Word, PowerPoint, and Excel, prompt users to specify permissions** is selected. This setting is sometimes referred to as "user-defined permissions."

        Note

        In this application of the label, users won't be prompted for permissions but their SharePoint permissions will be automatically applied when a file is downloaded, copied, or moved from the site.
- You've [enabled sensitivity labels for Office files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files). To check this status, you can run `(Get-SPOTenant).EnableAIPIntegration` from the [SharePoint Online Management Shell](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online) to confirm the value is set to **True**.
- Your tenant has been enabled for [co-authoring for files encrypted with sensitivity labels](sensitivity-labels-coauthoring).
- To support sensitivity labels for PDFs, you've [added support for PDFs in SharePoint](sensitivity-labels-sharepoint-onedrive-files#adding-support-for-pdf). To check this status, you can run `(Get-SPOTenant).EnableSensitivityLabelforPDF` from the [SharePoint Online Management Shell](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online) to confirm the value is set to **True**.
- Windows apps from Microsoft 365 Apps for enterprise that download files require a minimum version of 2402 from Current Channel, Monthly Enterprise Channel, or Semi-Annual Enterprise Channel.
- [SharePoint Information Rights Management (IRM) isn't enabled for the library](set-up-irm-in-sp-admin-center#irm-enable-sharepoint-document-libraries-and-lists). This older technology isn't compatible with using a sensitivity label for a SharePoint document library. If a library is enabled for IRM, you won't be able to select a sensitivity label.
- [Site admin permissions](/en-us/sharepoint/site-permissions#site-admins) are needed to apply and change the sensitivity label in SharePoint.
- Files must contain content to be labeled.

If you need to review a list of file types that are supported by sensitivity labels in SharePoint, see [Supported file types](sensitivity-labels-sharepoint-onedrive-files#supported-file-types).

## Mapping of SharePoint permissions to usage rights

Use the following table to understand how the SharePoint permissions for a user are extended to [rights management usage rights](rights-management-usage-rights#usage-rights-and-descriptions) and [permission levels](rights-management-usage-rights#usage-rights-and-descriptions) when a file is downloaded, or copied and moved outside the site.

| SharePoint permission | Usage rights applied | Permission levels |
| --- | --- | --- |
| **Owner** | Full control over the content, all permissions, and the sensitivity label applied: VIEW, EXTRACT, DOCEDIT, EDIT, EXPORT, COMMENT, PRINT, FORWARD, REPLY, REPLYALL, VIEWRIGHTSDATA, EDITRIGHTSDATA, OBJMODEL ^\*^, OWNER ^\*^ | Owner |
| **Edit** | Full control over the content but can't change the sensitivity label applied:  VIEW, EXTRACT, DOCEDIT, EDIT, EXPORT, COMMENT, PRINT, FORWARD, REPLY, REPLYALL, VIEWRIGHTSDATA | Editor |
| **Read** | Can view and copy the content but can't change the content or the sensitivity label applied:  VIEW, VIEWRIGHTSDATA, EXTRACT | No equivalent permission level, Viewer is the closest |

^\*^ Currently, these usage rights aren't applied and as a result, the user can change the sensitivity label, but can't remove it.

## Limitations

The following limitations apply when you use this configuration:

- Users can't manually apply sensitivity labels that aren't configured to apply encryption.
- Users won't be able to open downloaded files offline; they must be able to connect to the original site.
- Users won't be able to open downloaded files if the original SharePoint site, folder, or file is deleted.
- Files labeled with this configuration can't be moved or copied to another site.
- Files labeled with this configuration don't support the **Save As** option, and won't save with this option unless they are the minimum versions that include client-side improvements:

    - Windows: Version 2601+ in Current Channel and Monthly Enterprise Channel
    - macOS: Version 16.103+
    - iOS: Version 2.103+
    - Android: Version 16.0.19426+
- Files labeled with this configuration can only be moved or copied to another document library within the same site if users have SharePoint permissions to create or delete lists. The label isn't retained for the copied or moved file.
- This configuration can override a previously manually applied label if the label isn't configured to apply encryption.
- Files labeled with this configuration currently aren't displayed as labeled in [content explorer](data-classification-content-explorer).
- Microsoft 365 Copilot can reference the labeled files if users have SharePoint read permissions to them, but won't summarize these files. Because files can't be summarized, they also can't be used by Copilot to generate new content.

Note

As with all files that are encrypted with Azure Rights Management, a [super user](encryption-super-users) can open encrypted documents if that becomes necessary because the original location is no longer accessible.

## How to configure a SharePoint document library for a sensitivity label that extends permissions to downloaded documents

This configuration first requires that you enable the capability for the tenant by using PowerShell with the SharePoint Online Management Shell. Then, a new checkbox becomes available for document library settings.

### Run the PowerShell command to enable support to extend SharePoint permissions

Ensure that you're running SharePoint Online Management Shell version 16.0.25430.12000 or later.

To enable the new capabilities, use the [Set-SPOTenant](/en-us/powershell/module/sharepoint-online/set-spotenant) cmdlet with the *ExtendPermissionsToUnprotectedFiles* parameter:

1. Using a work or school account that has SharePoint admin privileges in Microsoft 365, connect to SharePoint. To learn how, see [Getting started with SharePoint Online Management Shell](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

    Note

    If you have Microsoft 365 Multi-Geo, use the -Url parameter with [Connect-SPOService](/en-us/powershell/module/sharepoint-online/connect-sposervice), and specify the SharePoint Online Administration Center site URL for one of your geo-locations.
2. Run the following command and press **Y** to confirm:

    ```PowerShell
    Set-SPOTenant -ExtendPermissionsToUnprotectedFiles $true
    ```

    If you see an error informing you that the feature isn't enabled, it's most likely because the rollout hasn't reached your tenant yet.
3. For Microsoft 365 Multi-Geo: Repeat steps 1 and 2 for each of your remaining geo-locations.

As with all tenant-level configuration changes for SharePoint, it takes about 15 minutes for the change to take effect.

### Configure SharePoint document libraries with a default label to extend permissions

For each SharePoint document library that you want to have this configuration, follow the instructions for [Add a sensitivity label to SharePoint document library](https://support.microsoft.com/office/54b1602b-db0a-4bcb-b9ac-5e20cbc28089), and select the checkbox **Extend protection on download, copy or move**:

![Extend permissions checkbox for SharePoint library default sensitivity label.](media/spo-extend-permissions.png)

You won't see this checkbox until the previous PowerShell command has completed.

After you've selected a sensitivity label that applies encryption with user-defined permissions, save the configuration.

Note

This feature is mutually exclusive with the option to select a [default sensitivity label for a SharePoint document library](sensitivity-labels-sharepoint-default-label) that supports sensitivity labels without encryption, and sensitivity labels that are configured with the option **Assign permissions now** (sometimes referred to as "admin-defined permissions").

The selected sensitivity label will be applied to all files that are unlabeled, and files that are labeled but the label configuration doesn't apply encryption. The **Sensitivity** column for the document library displays your selected label for existing, new, and edited files. Users see the selected label displayed when they open the file for editing but won't experience any changes in permissions as a result of the label.

After the library is configured with the sensitivity label, all existing files will be resynchronized if the library is synced via the OneDrive sync client. The resynchronization process can take a while and until it's complete, the extended protection won't be applied.

Important

In the SharePoint document library that you've configured for the sensitivity label, users can't remove the applied sensitivity label in their Office apps and can change it only if the replacement label applies encryption.

## Monitoring application of the sensitivity label that extends SharePoint permissions

Because this configuration extends the functionality of a default sensitivity label for a document library, you [monitor its configuration in the same way](sensitivity-labels-sharepoint-default-label#monitoring-application-of-library-default-sensitivity-labels). The sensitivity label GUID will identify the encryption configuration for user-defined permissions. There's no separate labeling auditing event for when a file is downloaded, copied, or moved.

## How to turn off this feature

If you want a specific SharePoint document library to no longer extend permissions with a sensitivity label, clear the **Extend protection on download, copy or move** checkbox as a SharePoint document library setting. Then:

- Files in the document library that were previously labeled with this configuration will revert to either their original label that didn't apply encryption, or unlabeled if that was their original status before the checkbox was selected.
- Files synchronized with OneDrive will be resynchronized and similarly revert to their previous label status. The resynchronization process can take a while and until it's complete, the extended protection will remain.
- Labeled files that are now downloaded retain their label.

If you want to turn off this feature at the tenant-level when it has been previously enabled and configured, first clear the **Extend protection on download, copy or move** checkbox from all document libraries where it's been selected. Then, use the same [Set-SPOTenant](/en-us/powershell/module/sharepoint-online/set-spotenant) cmdlet with the *ExtendPermissionsToUnprotectedFiles* parameter, but set the value to **false**. Then:

- The **Extend protection on download, copy or move** checkbox is no longer visible as a SharePoint document library setting.

If you turn off the feature at the tenant level without first clearing the checkbox for a document library, the configuration remains but without the checkbox to turn it off.

In this scenario, to turn off the configuration, run the PowerShell command to enable support to extend SharePoint permissions to display the checkbox again, so you can clear it. If you don't want to reenable support at the tenant level, contact [Microsoft Support](https://support.microsoft.com/microsoft-365) to talk you through PowerShell commands to remove the configuration for a specific document library.