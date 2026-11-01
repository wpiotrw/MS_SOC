---
layout: Conceptual
title: Enable co-authoring for encrypted documents | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sensitivity-labels-coauthoring
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
audience: Admin
ms.service: purview
ms.subservice: purview-information-protection
ms.date: 2026-01-14T00:00:00.0000000Z
ms.collection:
- purview-compliance
ms.topic: how-to
description: Turn on a setting that enables co-authoring and AutoSave in desktop apps for labeled and encrypted documents in SharePoint and OneDrive.
locale: en-us
document_id: 2207108d-7d98-9054-0cf0-c6bff6b40ad9
document_version_independent_id: 2207108d-7d98-9054-0cf0-c6bff6b40ad9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sensitivity-labels-coauthoring.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sensitivity-labels-coauthoring
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sensitivity-labels-coauthoring.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
2PlusCloud:
- M365
- Azure
- Power
__autotagging_hash:
- 42119BED1A1C4EB106D7F9D7FCB3B9C4DF3D2BAB12B3E2DDB608D27B588463E5
platformId: a5a0b2fd-5c13-67cc-8d72-4a758c20b08f
---

# Enable co-authoring for encrypted documents | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Enable the setting to support [co-authoring](https://support.office.com/article/ee1509b4-1f6e-401e-b04a-782d26f564a4) for Office desktop apps so that when documents are labeled and encrypted by [sensitivity labels](sensitivity-labels), multiple users can edit these documents at the same time.

Without this setting enabled for your tenant, users must check out an encrypted document stored in SharePoint or OneDrive when they use Office desktop apps. As a result, they can't collaborate in real time. Or, they must use Office for the web when [sensitivity labels are enabled for Office files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files).

In addition, enabling this functionality results in the [AutoSave](https://support.office.com/article/what-is-autosave-6d6bd723-ebfd-4e40-b5f6-ae6e8088f7a5) functionality being supported for these labeled and encrypted files.

For the release announcement, see the blog post [Co-authoring on Microsoft Information Protection encrypted documents is now generally available](https://techcommunity.microsoft.com/t5/security-compliance-and-identity/co-authoring-on-microsoft-information-protection-encrypted/ba-p/2693718).

## Metadata changes for sensitivity labels

Important

After you enable the setting for co-authoring, labeling information for unencrypted files is no longer saved in custom properties.

Don't enable this setting if you use any apps, services, scripts, or tools that read or write labeling metadata to the old location.

Before you enable the setting to support co-authoring for Office desktop apps, understand that this action changes the labeling metadata that Office files save and read.

The labeling metadata includes information that identifies your tenant and applied sensitivity label. The change that this setting makes is the metadata format and location for Word, Excel, and PowerPoint files. You don't need to take any action for encrypted files or emails because the metadata change for encrypted files is backward-compatible, and there are no changes for emails. However, you do need to be aware of the metadata changes for encrypted files that can be automatically upgraded but aren't backward-compatible.

This change affects both newly labeled files and already labeled files. When you use apps and services that support the co-authoring setting:

- For files that are newly labeled, only the new format and location is used for the labeling metadata.
- For files that are already labeled, the next time the file is opened and saved, if the file has metadata in the old format and location, that information is copied to the new format and location.

For more information about this metadata change, see the following resources:

- Blog post: [Upcoming Changes to Microsoft Information Protection Metadata Storage](https://techcommunity.microsoft.com/t5/microsoft-security-and/upcoming-changes-to-microsoft-information-protection-metadata/ba-p/1904418)
- Open Specifications: [2.6.3 LabelInfo versus Custom Document Properties](/en-us/openspecs/office_file_formats/ms-offcrypto/13939de6-c833-44ab-b213-e0088bf02341)

Because of these changes, don't enable this setting if your organization has any apps, services, scripts, or tools that read or write labeling metadata to the old location. If you enable this setting, some example consequences include:

- A document that is labeled appears to users as unlabeled.
- A document displays an out-of-date label to users.
- Co-authoring and AutoSave don't work for a labeled and encrypted document if another user has it open in a Office desktop app that doesn't support the new labeling metadata. Be aware that this scenario can also occur for users outside your organization if external users and invited guests have the file open.
- An Exchange Online mail flow rule that [identifies labels as custom properties in Office attachments](/en-us/azure/information-protection/configure-exo-rules#example-2-rule-that-applies-the-encrypt-only-option-to-emails-when-they-have-attachments-that-are-labeled-confidential--partners-and-these-emails-are-sent-outside-the-organization) fails to encrypt the email and attachment, or incorrectly encrypts them.

For a list of apps and services that support this setting and the changes to the labeling metadata, see the following section.

## Prerequisites

Make sure you understand the following prerequisites before you turn on this feature.

- To turn this capability on or off, you need at least the DLP Compliance Management or Information Protection Admin role. Alternative roles include the Security Administrator and Compliance Administrator roles.
- Sensitivity labels must be [enabled for Office files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files) for the tenant. If this feature isn't already enabled, it is automatically enabled when you select the setting to turn on co-authoring for files with sensitivity labels.
- Microsoft 365 Apps:

    - **Windows**: Minimum version 2107 from Current Channel or Monthly Enterprise Channel, or minimum version 2202 from Semi-Annual Enterprise Channel
    - **macOS**: Minimum version 16.51
    - **iOS**: Minimum version 2.58
    - **Android**: Minimum version 16.0.14931
- All apps, services, and operational tools in your tenant must support the new labeling metadata. If you use any of the following apps or services, check the minimum versions required:

    - **Microsoft Purview Information Protection client and scanner:**

        - Minimum version of 3.0 that you can install from the [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=53018), or minimum version of 2.12.62.0 for the older Azure Information Protection unified labeling client and scanner
    - **OneDrive sync app for Windows or macOS:**

        - Minimum version of 19.002.0121.0008
    - **Endpoint data loss prevention (Endpoint DLP):**

        - Windows 10 1809 with KB 4601383
        - Windows 10 1903 and 1909 with KB 4601380
        - Windows 10 2004 with KB 4601382
        - Windows versions later than Windows 10 2004 are supported without KB updates
    - **Apps and services that use the Microsoft Information Protection SDK:**

        - Minimum version of 1.7

Microsoft 365 services automatically support the new labeling metadata when you turn on this feature. For example:

- [Auto-labeling policies](apply-sensitivity-label-automatically#how-to-configure-auto-labeling-policies-for-sharepoint-onedrive-and-exchange)
- [DLP policies that use sensitivity labels as conditions](dlp-sensitivity-label-as-condition)
- [Microsoft Defender for Cloud Apps configured to apply sensitivity labels](/en-us/cloud-app-security/best-practices#discover-classify-label-and-protect-regulated-and-sensitive-data-stored-in-the-cloud)

## Limitations

Before you enable the tenant setting for co-authoring for files encrypted with sensitivity labels, make sure you understand the following limitations of this feature.

- Because of the labeling metadata changes, all apps, services, and operational tools in your tenant must support the new labeling metadata for a consistent and reliable labeling experience.

    Specific to Excel: Metadata for a sensitivity label that doesn't apply encryption can be deleted from a file if somebody edits and saves that file by using a version of Excel that doesn't support the metadata changes for sensitivity labels.
- Co-authoring and AutoSave aren't supported for Office documents that use the [label encryption configuration](encryption-sensitivity-labels#configure-encryption-settings)**User access to content expires** when it's set to a value other than **Never**, or **Double Key Encryption** is configured.

    Labels with these configurations do still display in Office apps. However, when users select these labels and nobody else is editing the document, they're warned that co-authoring and AutoSave won't be available. If somebody else is editing the document, users see a message that the labels can't be applied.
- Co-authoring and AutoSave are supported with [specific versions and limitations](sensitivity-labels-sharepoint-onedrive-files#support-for-labels-configured-for-user-defined-permissions) for sensitivity labels that are configured for user-defined permissions. This encryption configuration refers to the setting **Let users assign permissions when they apply the label** and the checkbox **In Word, PowerPoint, and Excel, prompt users to specify permissions** is selected.

## How to enable co-authoring for files with sensitivity labels

Caution

Enable this option only after you read and understand the metadata changes, prerequisites, limitations, and any known issues documented on this page.

For this configuration, use an account that has at least the DLP Compliance Management or Information Protection Admin role.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Settings** &gt; **Solution settings** &gt; **Information Protection** &gt; **Co-authoring for files with sensitivity labels**.
2. On the **Co-authoring for files with sensitivity labels** page, read the summary description, prerequisites, and what to expect.

    Then select **Turn on co-authoring for files with sensitivity labels**, and **Apply**:

    ![Option to turn on co-authoring for files with sensitivity labels.](media/co-authoring-tenant-option-for-sensitivity-labels.png)
3. Wait 24 hours for this setting to replicate across your environment before you use this new feature for co-authoring.

## If you need to disable this feature

Important

If you do need to disable this feature, for example, you've discovered some apps don't support the metadata changes and you can't immediately update these apps, be aware that labeling information can be lost.

After you enable co-authoring for files with sensitivity labels for your tenant, you can't disable this setting in the Microsoft Purview portal. This action is supported only by using PowerShell. This setting isn't one that you casually disable. Check and understand the prerequisites, consequences, and limitations before you enable the setting.

If you do disable this setting for your tenant:

- For apps and services that support the new labeling metadata, they now revert to the original metadata format and location when labels are read or saved.
- The new metadata format and location for Office documents that were used while the setting was enabled won't be copied to the original format and location. As a result, this labeling information for unencrypted Word, Excel, and PowerPoint files will be lost.
- Co-authoring and AutoSave no longer work in your tenant for labeled and encrypted documents.
- Sensitivity labels remain enabled for Office files in OneDrive and SharePoint.

### To disable co-authoring for your tenant

Use the [Set-PolicyConfig](/en-us/powershell/module/exchange/set-policyconfig) cmdlet with the *EnableLabelCoauth* parameter.

1. In a PowerShell session, [connect to Security & Compliance PowerShell](/en-us/powershell/exchange/office-365-scc/connect-to-scc-powershell/connect-to-scc-powershell).
2. Run the following command:

    ```PowerShell
    Set-PolicyConfig -EnableLabelCoauth:$false
    ```

The command completes without a prompt or confirmation.