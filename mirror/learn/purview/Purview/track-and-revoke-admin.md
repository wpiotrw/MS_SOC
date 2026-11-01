---
layout: Conceptual
title: Track and revoke document access | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/track-and-revoke-admin
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords: 
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-encryption
ms.collection:
- purview-compliance
description: Learn how administrators can track document access for protected documents, as well as revoke access if needed.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: c48cc17d-071f-a2db-823d-b833ec6320ea
document_version_independent_id: c48cc17d-071f-a2db-823d-b833ec6320ea
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/track-and-revoke-admin.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: track-and-revoke-admin
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/track-and-revoke-admin.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/19e6356c-ba1e-4d22-9557-6222c183f04d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/01e6eca5-e701-4cd9-a21f-56c9258f473e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 233943f2-8536-d9e3-3ff4-bfd76c2ae5ad
---

# Track and revoke document access | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Document tracking provides information for administrators about when a protected document was accessed. If necessary, both admins and users can revoke document access for tracked documents.

A document must be registered for tracking before an admin can track access details, including successful access events and denied attempts, and revoke access if needed. For minimum versions of Office apps that support file registration the next time they're opened, see Requirements.

Note

Track and revoke features are supported for Office file types only.

## Requirements

Use the [capabilities table](sensitivity-labels-versions#sensitivity-label-capabilities-in-word-excel-and-powerpoint) and the row **Document tracking and revocation** to identify the minimum versions of Word, Excel, and PowerPoint that automatically register label-protected local Office documents (if not already registered) the next time they're opened.

PowerShell cmdlets in this article use the [AIPService](/en-us/powershell/module/aipservice) PowerShell module, which you can install from the [PowerShell Gallery](https://www.powershellgallery.com/packages/AIPService). You must run [Connect-AipService](/en-us/powershell/module/aipservice/connect-aipservice) to connect to your tenant before you run any of the documented cmdlets.

## Limitations

The following limitations apply to track and revoke features:

- Password-protected documents aren't supported by track and revoke features.
- If you attach multiple documents to an email, and then protect the email and send it, each of the attachments gets the same ContentID value. This ContentID value will be returned only with the first file that had been opened. Searching for the other attachments won't return the ContentID value required to get tracking data.

    Additionally, revoking access for one of the attachments also revokes access for the other attachments in the same protected email.
- Documents protected with admin-defined permissions that are uploaded to SharePoint or OneDrive lose their **ContentID** value, and access can't be tracked or revoked.
- If a user downloads a file protected with admin-defined permissions from SharePoint or OneDrive, a new **ContentID** is applied to the document. Using the original **ContentID** value to track data won't include any access performed for the user's downloaded file. Additionally, revoking access based on the original **ContentID** value won't revoke access for any of the downloaded files.

    If administrators have access to the downloaded files, they can use PowerShell to identify a document's **ContentID** for track and revoke actions.

## Track document access

Admins can track access for protected documents via PowerShell using the **ContentID** generated for the protected document during registration.

**To view document access details**:

Use the following cmdlets to find details for the document you want to track:

1. Find the **ContentID** value for the document you want to track.

    Use the [Get-AipServiceDocumentLog](/en-us/powershell/module/aipservice/get-aipservicedocumentlog) cmdlet to search for a document using the filename or the email address of the user who applied protection.

    For example;

    ```PowerShell
    Get-AipServiceDocumentLog -ContentName "test.docx" -Owner "alice@contoso.com" -FromTime "12/01/2020 00:00:00" -ToTime "12/31/2020 23:59:59"
    ```

    This command returns the **ContentID** for all matching, protected documents that are registered for tracking.

    Note

    Protected documents are registered for tracking when they're first opened in an Office app that supports file registration. If this command does not return the ContentID for your protected file, open it in a supported Office app. For minimum supported versions, see Office apps that support file registration.
2. Use the [Get-AipServiceTrackingLog](/en-us/powershell/module/aipservice/get-aipservicetrackinglog) cmdlet with your document's **ContentID** to return your tracking data.

    For example:

    ```PowerShell
    Get-AipServiceTrackingLog -ContentId c03bf90c-6e40-4f3f-9ba0-2bcd77524b87
    ```

    Tracking data is returned, including emails of users who attempted access, whether access was granted or denied, the time and date of the attempt, and the domain and location where the access attempt originated.

## Revoke document access from PowerShell

Admins can revoke access for any protected document stored in their local content shares, using the [Set-AIPServiceDocumentRevoked](/en-us/powershell/module/aipservice/set-aipservicedocumentrevoked) cmdlet.

Note

If [offline access](encryption-sensitivity-labels#assign-permissions-now) is allowed, users will continue to be able to access the documents that have been revoked until the offline policy period expires.

1. Find the **ContentID** value for the document you want to revoke access for.

    Use the [Get-AipServiceDocumentLog](/en-us/powershell/module/aipservice/get-aipservicedocumentlog) cmdlet to search for a document using the filename or the email address of the user who applied protection.

    For example:

    ```PowerShell
    Get-AipServiceDocumentLog -ContentName "test.docx" -Owner "alice@contoso.com" -FromTime "12/01/2020 00:00:00" -ToTime "12/31/2020 23:59:59"
    ```

    The data returned includes the ContentID value for your document.

    Tip

    Only documents that have been protected and registered for tracking have a **ContentID** value. If your document has no **ContentID**, open it in a supported Office app. For minimum supported versions, see Office apps that support file registration.
2. Use the [Set-AIPServiceDocumentRevoked](/en-us/powershell/module/aipservice/set-aipservicedocumentrevoked) with your document's ContentID to revoke access.

    For example:

    ```PowerShell
    Set-AipServiceDocumentRevoked -ContentId 0e421e6d-ea17-4fdb-8f01-93a3e71333b8 -IssuerName testIssuer
    ```

By using the **Sensitivity** menu in their Office apps, users can also revoke access for any documents that they protected.

### Restore access

If you've accidentally revoked access to a specific document, use the same **ContentID** value with the [Clear-AipServiceDocumentRevoked](/en-us/powershell/module/aipservice/clear-aipservicedocumentrevoked) cmdlet to remove the revoked status so that authorized users can access the document again. Specify the same **IssuerName** value that was used when the document was revoked.

For example:

```PowerShell
Clear-AipServiceDocumentRevoked -ContentId   0e421e6d-ea17-4fdb-8f01-93a3e71333b8 -IssuerName testIssuer
```

Document access is granted to the user you defined in the **IssuerName** parameter.

## Turn off track and revoke features for your tenant

If you need to turn off track and revoke features for your tenant, such as for privacy requirements in your organization or region, run the [Disable-AipServiceDocumentTrackingFeature](/en-us/powershell/module/aipservice/disable-aipservicedocumenttrackingfeature) cmdlet.

Document tracking and options to revoke access are turned off for your tenant:

- Opening protected documents no longer registers the documents for track and revoke.
- Access logs aren't stored when protected documents that are already registered are opened. Access logs that were stored before turning off these features are still available.
- Admins won't be able to track or revoke access via PowerShell, and although end-users still see the **Revoke** menu option in their Office apps, the site displays a message that tracking and revocation has been disabled by their administrator.

If you need to turn track and revoke back on, run the [Enable-AipServiceDocumentTrackingFeature](/en-us/powershell/module/aipservice/enable-aipservicedocumenttrackingfeature) cmdlet.

## Remove the track and revoke options from the Sensitivity menu

If you need to remove the Track & Revoke button from the Sensitivity menu on Office clients, use PowerShell advanced settings with the [Set-LabelPolicy](/en-us/powershell/module/exchange/set-labelpolicy) cmdlet.

The following example disables revoke support in the client UI by setting the `EnableRevokeGuiSupport` advanced setting to `False` in the global label policy:

```PowerShell
Set-LabelPolicy -Identity Global -AdvancedSettings @{EnableRevokeGuiSupport="False"}
```

## End user instructions for Office apps

See [Track and revoke access to your files](https://support.microsoft.com/office/track-and-revoke-access-to-your-files-1de9a543-c2df-44b6-9464-396b23018f96).