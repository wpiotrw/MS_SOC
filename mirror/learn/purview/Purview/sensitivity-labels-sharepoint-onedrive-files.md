---
layout: Conceptual
title: Enable sensitivity labels for files in SharePoint and OneDrive | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sensitivity-labels-sharepoint-onedrive-files
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
audience: Admin
ms.topic: how-to
ms.date: 2026-10-14T00:00:00.0000000Z
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
- SPO_Content
search.appverid:
- MOE150
- MET150
description: Administrators can enable sensitivity label support for Word, Excel, PowerPoint, and PDF files in SharePoint and OneDrive.
ms.custom: sfi-ga-blocked, msecd-doc-authoring-1030
ai-usage: ai-assisted
locale: en-us
document_id: 96fedf23-2f39-3282-c100-44e002f318af
document_version_independent_id: 96fedf23-2f39-3282-c100-44e002f318af
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sensitivity-labels-sharepoint-onedrive-files.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sensitivity-labels-sharepoint-onedrive-files
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sensitivity-labels-sharepoint-onedrive-files.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/64b65f6c-101f-411a-9b83-9f577fab52d0
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://authoring-docs-microsoft.poolparty.biz/devrel/1a667fd1-8145-4b11-af0f-9f5de205a6e5
platformId: 7c44350d-0235-3a94-7224-b71cff737f28
---

# Enable sensitivity labels for files in SharePoint and OneDrive | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Enable built-in labeling for [supported Office files](sensitivity-labels-office-apps#office-file-types-supported) and [PDF files](sensitivity-labels-office-apps#pdf-support) in SharePoint and OneDrive so that users can apply your [sensitivity labels](sensitivity-labels) in Office for the web. When this feature is enabled, users see the **Sensitivity** button on the ribbon so they can apply labels, and see any applied label name on the status bar.

Users can also see and apply sensitivity labels without having to first open the files, by using the details pane in SharePoint and OneDrive. This labeling method is also available from the **Files** tab in Microsoft Teams.

Enabling this feature also results in SharePoint and OneDrive being able to process the contents of Office files and optionally, PDF documents that have been encrypted by using a sensitivity label. The label can be applied in Office for the web, or in Office desktop apps and uploaded or saved in SharePoint and OneDrive. Until you enable this feature, these services can't process encrypted files, which means that coauthoring, eDiscovery, data loss prevention, search, and other collaborative features won't work for these files.

After you enable sensitivity labels for these files in SharePoint and OneDrive, for new and changed files that have a sensitivity label that applies encryption with a cloud-based key (and doesn't use [Double Key Encryption](double-key-encryption)):

- For Word, Excel, and PowerPoint files, and uploaded [PDF files](sensitivity-labels-office-apps#pdf-support), SharePoint and OneDrive recognize the label and can now process the contents of the encrypted file.
- When users download or access these files from SharePoint or OneDrive, the sensitivity label and any encryption settings from the label are enforced and remain with the file, wherever it's stored. Ensure you provide user guidance to use only labels to protect documents. For more information, see [Information Rights Management (IRM) options and sensitivity labels](sensitivity-labels-office-apps#information-rights-management-irm-options-and-sensitivity-labels).
- When users upload labeled and encrypted files to SharePoint or OneDrive, they must have at least [View usage rights](rights-management-usage-rights#usage-rights-and-descriptions) to those files. For example, they can open the files outside SharePoint. If they don't have this minimum usage right, the upload is successful but the service doesn't recognize the label and can't process the file contents.
- Use Office for the web (Word, Excel, PowerPoint) to open and edit Office files that have sensitivity labels that apply encryption. The permissions that were assigned with the encryption are enforced. You can also use [auto-labeling](apply-sensitivity-label-automatically) for these documents.
- External users can access documents that are labeled with encryption by using guest accounts. For more information, see [Support for external users and labeled content](sensitivity-labels-office-apps#support-for-external-users-and-labeled-content).
- eDiscovery supports full-text search for these files and data loss prevention (DLP) policies support content in these files.

Note

If encryption has been applied with an on-premises key (a key management topology often referred to as "hold your own key" or HYOK), or by using [Double Key Encryption](double-key-encryption), the service behavior for processing the file contents doesn't change. So for these files, coauthoring, eDiscovery, data loss prevention, search, and other collaborative features won't work.

The SharePoint and OneDrive behavior also doesn't change for existing files in these locations that are labeled with encryption using a single Azure-based key. For these files to benefit from the new capabilities after you enable sensitivity labels for Office files in SharePoint and OneDrive, the files must be either downloaded and uploaded again, or edited.

After you enable sensitivity labels for Office files in SharePoint and OneDrive, three new [audit events](audit-log-activities#sensitivity-label-activities) are available for monitoring sensitivity labels that are applied to documents in SharePoint and OneDrive:

- **Applied sensitivity label to file**
- **Changed sensitivity label applied to file**
- **Removed sensitivity label from file**

You can disable sensitivity labels for Office files in SharePoint and OneDrive (opt-out) at any time.

If you're currently protecting documents in SharePoint by using SharePoint Information Rights Management (IRM), be sure to check the SharePoint Information Rights Management (IRM) and sensitivity labels section on this page.

## Requirements

These new capabilities work with [sensitivity labels](sensitivity-labels) only.

Use the OneDrive sync app version 19.002.0121.0008 or later on Windows, and version 19.002.0107.0008 or later on macOS. Both these versions were released January 28, 2019. For more information, see the [OneDrive release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0). After you enable sensitivity labels for SharePoint and OneDrive, users who run an older version of the sync app see a prompt to update it.

## Supported file types

After you enable sensitivity labels for SharePoint and OneDrive, the following Office file types support sensitivity labeling scenarios.

Applying a sensitivity label in Office for the web or in SharePoint:

- **Word**: .docx, .docm
- **Excel**: .xlsx, .xlsm, .xlsb
- **PowerPoint**: .pptx, .ppsx

Uploading a labeled Office document, and then extracting and displaying that sensitivity label:

- **Word**: .doc, .docx, .docm, .dot, .dotx, .dotm
- **Excel**: .xls, .xlt, .xla, .xlc, .xlm, .xlw, .xlsx, .xltx, .xlsm, .xltm, .xlam, .xlsb
- **PowerPoint**: .ppt, .pot, .pps, .ppa, .pptx, .ppsx, .ppsxm, .potx, .ppam, .pptm, .potm, .ppsm

### Video support (MP4 files and Clipchamp projects)

Enable sensitivity label support for MP4 files by using the SharePoint Online PowerShell setting `EnableSensitivityLabelForVideoFiles`. The same setting also controls labeling for Clipchamp projects after the update described in that subsection reaches your tenant.

MP4 files support manually applying sensitivity labels, but can't be labeled automatically or by default. Additionally, MP4 files can [automatically inherit a sensitivity label from a Teams meeting](sensitivity-labels-meetings#policy-settings-meetings).

To turn on support for MP4 video files, use the [Set-SPOTenant](/en-us/powershell/module/sharepoint-online/set-spotenant) cmdlet with the *EnableSensitivityLabelForVideoFiles* parameter:

```PowerShell
 Set-SPOTenant -EnableSensitivityLabelForVideoFiles $true
```

For Microsoft 365 Multi-Geo, you must connect to each of your geo-locations and run the command separately.

When MP4 files have a sensitivity label that applies encryption, they can't be downloaded. All labeled MP4 files support playback in SharePoint, Teams, and Clipchamp.

Sensitivity labels that apply encryption must be configured with the [Assign permissions now](encryption-sensitivity-labels#assign-permissions-now) option, rather than user-defined permissions.

#### Clipchamp projects

In Clipchamp, a project's sensitivity label can restrict actions in the editor and be inherited by an exported MP4.

An update extends `EnableSensitivityLabelForVideoFiles` to Clipchamp project labeling and label inheritance on MP4 exports. Check your tenant's current value, then review the before-and-after behavior below to understand the effect on your organization.

[Connect to SharePoint Online PowerShell](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online) and run:

```PowerShell
Get-SPOTenant | Select-Object EnableSensitivityLabelForVideoFiles
```

Note

The update announced in Message Center post MC1454399 is rolling out worldwide from mid-September 2026, with completion expected in mid-October 2026. The schedule doesn't confirm availability for an individual tenant.

**Before the change reaches your tenant**, `EnableSensitivityLabelForVideoFiles` controls MP4 labeling support in SharePoint and OneDrive, but not project labeling in the Clipchamp editor. Even when the setting is `$false`, Clipchamp can apply your organization's default sensitivity label and pass a project's label to an MP4 export.

**After the change reaches your tenant**, `EnableSensitivityLabelForVideoFiles` also controls sensitivity label behavior for `.clipchamp` projects:

| Setting and project state after rollout | Project labels and imported media | New MP4 exports |
| --- | --- | --- |
| `$true` | Your organization's default label policy applies. Supported label changes and imports are subject to label, protection, and permission checks. | Inherit the project's label, if one is applied. |
| `$false`, project is unlabeled | No default label or label changes; the picker is hidden. Importing supported protected or non-protected labeled media requires acknowledgment that neither the project nor its export inherits the source label. | Don't inherit a label from the project. |
| `$false`, project already has a valid label | The existing label and restrictions remain, but label changes are blocked. Imports retain the same checks as for `$true`, but imports that require a project label upgrade are blocked. | Don't inherit the project's label or restrictions from that label. Clipchamp warns before exporting without the label. |

Users still need permission to access and use source media and to export the project. After the change reaches a tenant with the setting at `$false`, users can share or download new, unlabeled MP4 exports from Clipchamp, subject to other permissions and policies. Existing project restrictions and previously exported MP4 files are unchanged.

If your organization requires labels on Clipchamp projects and their exports, use `$true` and review the applicable default label policy. The setting applies across the tenant, or the connected geo-location in a Multi-Geo organization; review its effect before changing it.

For supported label changes, import prompts, and sharing restrictions in Clipchamp, see [How sensitivity labels work in Clipchamp](https://support.microsoft.com/clipchamp/clipchamp-sensitivity-labels).

### Adding support for PDF

You can enable support for PDFs for the following scenarios:

- Applying a sensitivity label in Office for the web
- Uploading a labeled document, and then extracting and displaying that sensitivity label
- Search, eDiscovery, and data loss prevention
- [Auto-labeling policies](apply-sensitivity-label-automatically#how-to-configure-auto-labeling-policies-for-sharepoint-onedrive-and-exchange) and [default sensitivity labels for SharePoint document libraries](sensitivity-labels-sharepoint-default-label)

Sensitivity labels don't support signed PDFs.

Important

Enabling PDF support can increase the number of files that get automatically labeled by existing auto-labeling policies. The limit is 500,000 automatically labeled SharePoint and OneDrive files per tenant per day, across all auto-labeling policies.

To turn on support from the Microsoft Purview portal:

- [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Information Protection** &gt; **Sensitivity labels** &gt; **Policies** &gt; **Auto-labeling policies**

    Then, if you see a message **Protect PDFs with Auto-labeling**, select this banner to confirm you want to turn on PDF protection for files in SharePoint and OneDrive.

Alternatively, you can turn on PDF support by using PowerShell. Use the [Set-SPOTenant](/en-us/powershell/module/sharepoint-online/set-spotenant) cmdlet with the *EnableSensitivityLabelforPDF* parameter:

```PowerShell
Set-SPOTenant -EnableSensitivityLabelforPDF $true
```

This PDF parameter requires a minimum version of 16.0.24211.12000 for the [SharePoint Online Management Shell](https://www.microsoft.com/en-us/download/details.aspx?id=35588). For more information about how to install this PowerShell module or run the cmdlets, see the [section on this page to enable support for sensitivity labels](sensitivity-labels-sharepoint-onedrive-files#use-powershell-to-enable-support-for-sensitivity-labels).

For Microsoft 365 Multi-Geo: Similarly to the instructions to run the PowerShell command to enable support for sensitivity labels, you must connect to each of your geo-locations, and then run the command to enable support for PDFs.

## Support for labels configured for user-defined permissions

User-defined permissions refers to an encryption configuration and the setting **Let users assign permissions when they apply the label** and the checkbox **In Word, PowerPoint, and Excel, prompt users to specify permissions** is selected.

After you've enabled sensitivity labels for SharePoint and OneDrive, content labeled with user-defined permissions can be inspected for search, data loss prevention, and eDiscovery. This functionality applies to only newly uploaded and edited files.

The following actions support labels configured for user-defined permissions:

- When a document is labeled with user-defined permissions and uploaded to SharePoint or OneDrive, these services can now process the document so that it can be opened and edited in Office for the web, and the label name is displayed in the **Sensitivity** column.
- Labels with this configuration are displayed in Office for the web. Before users select these labels to specify users and permissions, or change the label applied, make sure you've [enabled co-authoring for files encrypted with sensitivity labels](sensitivity-labels-coauthoring).

To support AutoSave and co-authoring for these encrypted files by using a desktop app, [co-authoring for files encrypted with sensitivity labels](sensitivity-labels-coauthoring) must first be enabled.

This functionality comes with the following change in behavior for encryption:

- If an existing file that's labeled with user-defined permissions is relabeled with a sensitivity label that doesn't apply encryption, the original encryption is removed rather than preserved. For more information, see [What happens to existing encryption when a label's applied](encryption-sensitivity-labels#what-happens-to-existing-encryption-when-a-labels-applied).

## Limitations

- SharePoint and OneDrive can't process some files that are labeled and encrypted from Office desktop apps when these files contain Power Query data, data stored by custom add-ins, or custom XML parts such as Cover Page Properties, content type schemas, custom Document Information Panel, and Custom XSN. This limitation also applies to files that include a [bibliography](https://support.microsoft.com/en-us/office/create-a-bibliography-citations-and-references-17686589-4824-4940-9c69-342c289fa2a5), and to files that have a [Document ID](https://support.microsoft.com/office/enable-and-configure-unique-document-ids-ea7fee86-bd6f-4cc8-9365-8086e794c984) added when they're uploaded.

    For these files, either apply a label without encryption so that users can later open them in Office for the web, or instruct users to open the files in their desktop apps. Files that are labeled and encrypted only in Office for the web aren't affected.
- SharePoint and OneDrive don't support sensitivity labels if you applied the labels before enabling these services for sensitivity labels. The labels aren't recognized and if the labels applied encryption, the contents aren't processed. For the labels and encryption to be supported by SharePoint and OneDrive, download these files and then upload them to their original location.
- SharePoint and OneDrive can't process encrypted files when the label that applied the encryption has either of the following [configurations for encryption](encryption-sensitivity-labels#configure-encryption-settings):

    - **User access to content expires** is set to a value other than **Never**.
    - **Double Key Encryption** is selected.

        For labels with either of these encryption configurations, the labels aren't displayed to users in Office for the web. If they're parent labels, this means that users don't see that label's sublabels, even if the sublabels aren't configured to apply encryption.

        Additionally, the new capabilities can't be used with labeled documents that already have these encryption settings. For example, these documents aren't returned in search results, even if they're updated.
- SharePoint and OneDrive can't read or apply sensitivity labels when the document is password-protected.
- SharePoint and OneDrive prevents downloading MP4 files with sensitivity labels that apply encryption. If these files have labels that don't apply encryption, they can be downloaded but the labeling information is lost.
- For performance reasons, when you upload or save a document to SharePoint and the file's label doesn't apply encryption, the **Sensitivity** column in the document library can take a while to display the label name. Factor in this delay if you use scripts or automation that depend on the label name in this column.
- If a document is labeled while it's [checked out in SharePoint](https://support.microsoft.com/office/check-out-check-in-or-discard-changes-to-files-in-a-library-7e2c12a9-a874-4393-9511-1378a700f6de), the **Sensitivity** column in the document library doesn't display the label name until the document is checked in and next opened in SharePoint.
- If a labeled and encrypted document is downloaded from SharePoint or OneDrive by an app or service that uses a service principal name, and then uploaded again with a label that applies different encryption settings, the upload fails. An example scenario is Microsoft Defender for Cloud Apps changes a sensitivity label on a file from **Confidential** to **Highly Confidential**, or from **Confidential** to **General**.

    The upload doesn't fail if the app or service first runs the [Unlock-SPOSensitivityLabelEncryptedFile](/en-us/powershell/module/sharepoint-online/unlock-sposensitivitylabelencryptedFile) cmdlet, as explained in the Remove encryption for a labeled document section. Or, before the upload, the original file is deleted, or the file name is changed.
- Users might experience delays in being able to open encrypted documents in the following Save As scenario: With a desktop version of Office, a user chooses Save As for a document that has a sensitivity label that applies encryption. The user selects SharePoint or OneDrive for the location, and then immediately tries to open that document in Office for the web. If the service is still processing the encryption, the user sees a message that the document must be opened in their desktop app. If they try again in a couple of minutes, the document successfully opens in Office for the web.
- For encrypted documents, printing, downloading, exporting, and creating a copy aren't supported in Office for the web.
- For encrypted documents in Office for the web, [screen captures aren't prevented](azure-rights-management-learn-about#can-rights-management-prevent-screen-captures). However, when documents are labeled and encrypted, and the **Copy**[usage right](rights-management-usage-rights) isn't granted, Office for the web prevents copying to clipboard in the same way as desktop apps prevent this action.
- By default, Office desktop apps and mobile apps don't support co-authoring for files that are labeled with encryption. These apps continue to open labeled and encrypted files in exclusive editing mode. To change the default behavior, see [Enable co-authoring for files encrypted with sensitivity labels](sensitivity-labels-coauthoring).
- If an admin changes settings for a published label that's already applied to files downloaded to users' sync client, users might be unable to save changes they make to the file in their OneDrive Sync folder. This scenario applies to files that are labeled with encryption, and also when the label change is from a label that didn't apply encryption to a label that does apply encryption. Users see a [red circle with a white cross icon error](https://support.office.com/article/what-do-the-onedrive-icons-mean-11143026-8000-44f8-aaa9-67c985aa49b3), and they're asked to save new changes as a separate copy. Instead, they can close and reopen the file, or use Office for the web.
- Sensitivity labels that are configured for [automatic labeling](apply-sensitivity-label-automatically#how-to-configure-auto-labeling-for-office-apps) are supported for Office for the web when the label settings for conditions are for sensitive information types only. Automatic labeling isn't supported for Office for the web when the conditions include trainable classifiers.
- Users can experience save problems after going offline or into a sleep mode when instead of using Office for the web, they use the desktop and mobile apps for Word, Excel, or PowerPoint. For these users, when they resume their Office app session and try to save changes, they see an upload failure message with an option to save a copy instead of saving the original file.
- Documents that are encrypted in the following ways can't be opened in Office for the web:

    - Encryption that uses an on-premises key ("hold your own key" or HYOK)
    - Encryption that was applied by using [Double Key Encryption](double-key-encryption)
    - Encryption that was applied independently from a label, for example, by directly applying a Rights Management protection template.
- Labels configured for [other languages](create-sensitivity-labels#additional-label-settings-with-security--compliance-powershell) aren't supported and display the original language only.
- If you delete a label that's been applied to a document in SharePoint or OneDrive, rather than remove the label from the applicable label policy, the document when downloaded isn't labeled or encrypted. In comparison, if the labeled document is stored outside SharePoint or OneDrive, the document remains encrypted if the label is deleted. Although you might delete labels during a testing phase, it's very rare to delete a label in a production environment.
- When a labeled and encrypted Office file larger than 12 MB is copied or moved to a different site, SharePoint can no longer process this file. As a result, the **Sensitivity** column doesn't display the label name and users can't open the file using Office for the web. Users can successfully open the file when they use an Office client app.
- In the following scenario, users from an external tenant can't open files protected with a user-defined permissions sensitivity label in Office for the web. The same limitation also applies when users open the file from SharePoint or OneDrive with Microsoft Office desktop applications.

    - A user (UserA) from an external tenant (fabrikam) is invited as a guest user to the contoso tenant.
    - The sensitivity label applied to the file grants permissions to a group in the external fabrikam tenant, and UserA is a member of that group.
    - The file is uploaded to SharePoint in the contoso tenant, and UserA attempts to open the file in Office for the web.

    To allow an external tenant user to open a file protected with a user-defined permissions sensitivity label, use one of the following methods:

    - Grant permissions directly to the external user in the sensitivity label.
    - Add the external user to a group in the contoso tenant, and grant permissions to that contoso tenant group in the sensitivity label.

## How to enable sensitivity labels for SharePoint and OneDrive (opt-in)

Note

Enabling sensitivity labels for SharePoint and OneDrive automatically enables [sensitivity labels for Loop components and pages](sensitivity-labels-loop). However, enabling sensitivity labels for OneNote requires an additional step that uses PowerShell.

You can enable the new capabilities by using the Microsoft Purview portal, or by using PowerShell. See the following sections for instructions.

As with all tenant-level configuration changes for SharePoint and OneDrive, it takes about 15 minutes for the change to take effect.

### Use the portal to enable support for sensitivity labels

This option is the easiest way to enable sensitivity labels for SharePoint and OneDrive. You must sign in as a global administrator for your tenant.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Information Protection** &gt; **Sensitivity labels**.
2. If you see a message to turn on the ability to process content in Office online files, select **Turn on now**:

    ![Turn on now button to enable sensitivity labels for Office Online.](media/sensitivity-labels-turn-on-banner.png)

    The command runs immediately and when the page is next refreshed, you no longer see the message or button.

Note

If you have Microsoft 365 Multi-Geo, you must use PowerShell to enable these capabilities for all your geo-locations. See the next section for details.

### Use PowerShell to enable support for sensitivity labels

As an alternative to using the Microsoft Purview portal, you can enable support for sensitivity labels by using the [Set-SPOTenant](/en-us/powershell/module/sharepoint-online/set-spotenant) cmdlet from SharePoint Online PowerShell. The same Set-SPOTenant cmdlet can then be run again to enable sensitivity labels for OneDrive.

If you have Microsoft 365 Multi-Geo, you must use PowerShell to enable this support for all your geo-locations.

#### Prepare the SharePoint Online Management Shell

Before you run the PowerShell command to enable sensitivity labels for Office files in SharePoint and OneDrive, ensure that you're running SharePoint Online Management Shell version 16.0.19418.12000 or later. To additionally support sensitivity labels for OneNote, you need SharePoint Online Management Shell version 16.0.26914.12004 or later. If you already have the latest version, you can skip to next procedure to run the PowerShell command.

1. If you installed a previous version of the SharePoint Online Management Shell from the PowerShell gallery, update the module by running the following cmdlet.

    ```PowerShell
    Update-Module -Name Microsoft.Online.SharePoint.PowerShell
    ```
2. Alternatively, if you have installed a previous version of the SharePoint Online Management Shell from the Microsoft Download Center, you can also go to **Add or remove programs** and uninstall the SharePoint Online Management Shell.
3. In a web browser, go to the Download Center page and [Download the latest SharePoint Online Management Shell](https://www.microsoft.com/en-us/download/details.aspx?id=35588).
4. Select your language and then select **Download**.
5. Choose between the x64 and x86 .msi file. Download the x64 file if you run the 64-bit version of Windows or the x86 file if you run the 32-bit version. If you don't know, see [Which version of Windows operating system am I running?](https://support.microsoft.com/help/13443/windows-which-operating-system)
6. After you download the file, run the file and follow the steps in the Setup configuration.

#### Run the PowerShell command to enable support for sensitivity labels

To enable the new capabilities, use the [Set-SPOTenant](/en-us/powershell/module/sharepoint-online/set-spotenant) cmdlet with the *EnableAIPIntegration* parameter:

1. Using a work or school account that has SharePoint admin privileges in Microsoft 365, connect to SharePoint. To learn how, see [Getting started with SharePoint Online Management Shell](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

    Note

    If you have Microsoft 365 Multi-Geo, use the -Url parameter with [Connect-SPOService](/en-us/powershell/module/sharepoint-online/connect-sposervice), and specify the SharePoint Online Administration Center site URL for one of your geo-locations.
2. Run the following command and press **Y** to confirm:

    ```PowerShell
    Set-SPOTenant -EnableAIPIntegration $true
    ```
3. For Microsoft 365 Multi-Geo: Repeat steps 1 and 2 for each of your remaining geo-locations.
4. If you want to additionally enable sensitivity labels for OneNote (supported at the [section level](https://support.microsoft.com/office/create-a-new-section-43356c5d-05c0-4a6b-990a-58ed45eef34a)), run *Set-SPOTenant* again, but use the following command:

    ```PowerShell
    Set-SPOTenant -EnableSensitivityLabelforOneNote $true
    ```

    For Microsoft 365 Multi-Geo, repeat this step for each of your remaining geo-location.

## Publishing and changing sensitivity labels

When you use sensitivity labels with SharePoint and OneDrive, keep in mind that you need to allow for replication time when you publish new sensitivity labels or update existing sensitivity labels. This replication time is especially important for new labels that apply encryption.

For example, you create and publish a new sensitivity label that applies encryption and it very quickly appears in a user's desktop app. The user applies this label to a document and then uploads it to SharePoint or OneDrive. If the label replication hasn't completed for the service, the new capabilities aren't applied to that document on upload. As a result, the document isn't returned in search or for eDiscovery, and the document can't be opened in Office for the web.

For more information about the timing of labels, see [When to expect new labels and changes to take effect](create-sensitivity-labels#when-to-expect-new-labels-and-changes-to-take-effect).

As a safeguard, publish new labels to just a few test users first, wait for at least one hour, and then verify the label behavior on SharePoint and OneDrive. Wait at least a day before you make the label available to more users by either adding more users to the existing label policy, or adding the label to an existing label policy for your standard users. By the time your standard users see the label, it has already synchronized to SharePoint and OneDrive.

## SharePoint Information Rights Management (IRM) and sensitivity labels

[SharePoint Information Rights Management (IRM)](set-up-irm-in-sp-admin-center) is an older technology to protect files at the list and library level by applying encryption and restrictions when users download files. This older protection technology is designed to prevent unauthorized users from opening the file while it's outside SharePoint.

In comparison, sensitivity labels provide the protection settings of visual markings (headers, footers, watermarks) in addition to encryption. The encryption settings support the full range of [usage rights](rights-management-usage-rights) to restrict what users can do with the content, and the same sensitivity labels are supported for [many scenarios](get-started-with-sensitivity-labels#common-scenarios-for-sensitivity-labels). Using the same protection method with consistent settings across workloads and apps results in a consistent protection strategy.

However, you can use both protection solutions together and the behavior is as follows:

- If you upload a file with a sensitivity label that applies encryption, SharePoint can't process the content of these files so coauthoring, eDiscovery, DLP, and search aren't supported for these files.
- If you label a file using Office for the web, any encryption settings from the label are enforced. For these files, coauthoring, eDiscovery, DLP, and search are supported.
- If you download a file that's labeled by using Office for the web, the label is retained and any encryption settings from the label are enforced rather than the IRM restriction settings.
- If you download an Office or PDF file that isn't encrypted with a sensitivity label, IRM settings are applied.
- If you enabled any of the additional IRM library settings, which include preventing users from uploading documents that don't support IRM, these settings are enforced.

With this behavior, you can be assured that all Office and PDF files are protected from unauthorized access if they're downloaded, even if they aren't labeled. However, labeled files that are uploaded don't benefit from the new capabilities.

## Search for documents by sensitivity label

Use the managed property **InformationProtectionLabelId** to find all documents in SharePoint or OneDrive that have a specific sensitivity label. Use the following syntax: `InformationProtectionLabelId:<GUID>`

For example, to search for all documents that are labeled as "Confidential" and that label has a GUID of `8faca7b8-8d20-48a3-8ea2-0f96310a848e`, type the following text in the search box:

```
InformationProtectionLabelId:8faca7b8-8d20-48a3-8ea2-0f96310a848e
```

Search can't find labeled documents in a compressed file, such as a .zip file.

To get the GUIDs for your sensitivity labels, use the [Get-Label](/en-us/powershell/module/exchange/get-label) cmdlet:

1. First, [connect to Office 365 Security & Compliance PowerShell](/en-us/powershell/exchange/office-365-scc/connect-to-scc-powershell/connect-to-scc-powershell).

    For example, in a PowerShell session that you run as administrator, sign in by using a compliance administrator account.
2. Then run the following command:

    ```powershell
    Get-Label |ft Name, Guid
    ```

For more information about using managed properties, see [Manage the search schema in SharePoint](/en-us/sharepoint/manage-search-schema).

## Remove encryption for a labeled document

There might be rare occasions when a SharePoint administrator needs to remove encryption from a document stored in SharePoint. Any user who has the [Rights Management usage right](rights-management-usage-rights#usage-rights-and-descriptions) of Export or Full Control assigned to them for that document can remove encryption that was applied by the Azure Rights Management service from Microsoft Purview Information Protection. For example, users with either of these usage rights can replace a label that applies encryption with a label without encryption. A [super user](encryption-super-users) could also download the file and save a local copy without the encryption.

As an alternative, a [SharePoint admin](/en-us/sharepoint/sharepoint-admin-role) can run the [Unlock-SPOSensitivityLabelEncryptedFile](/en-us/powershell/module/sharepoint-online/unlock-sposensitivitylabelencryptedFile) cmdlet, which removes both the sensitivity label and the encryption. This cmdlet runs even if the admin doesn't have access permissions to the site or file, or if the Azure Rights Management service is unavailable.

For example:

```powershell
Unlock-SPOSensitivityLabelEncryptedFile -FileUrl "https://contoso.com/sites/Marketing/Shared Documents/Doc1.docx" -JustificationText "Need to decrypt this file"
```

Requirements:

- SharePoint Online Management Shell version 16.0.20616.12000 or later.
- The encryption is applied by a sensitivity label with admin-defined encryption settings (the [Assign permissions now](encryption-sensitivity-labels#assign-permissions-now) label settings). [Double Key Encryption](encryption-sensitivity-labels#double-key-encryption) isn't supported for this cmdlet.

The justification text is added to the [audit event](audit-log-activities#sensitivity-label-activities) of **Removed sensitivity label from file**, and the decryption action is also recorded in the [usage logging for the Azure Rights Management service](rights-management-usage-logging).

## How to disable sensitivity labels for SharePoint and OneDrive (opt-out)

After you disable these new capabilities, SharePoint and OneDrive can't process newly labeled and encrypted files. As a result, coauthoring, eDiscovery, data loss prevention, search, and other collaborative features won't work for these files. However, these capabilities continue to be supported for files that were labeled and encrypted before you disabled sensitivity labels.

This mixed protection state can result in higher administrative overheads with help desk incidents to investigate the inconsistent behavior. It might also be a problem for compliance requirements.

To better understand the behavior of labeled files before and after disabling sensitivity labels for SharePoint and OneDrive, use the **Label behavior** tab.

# [Disable instructions](#tab/disable-instructions)
To disable these new capabilities, you must use PowerShell. By using the SharePoint Online Management Shell and the [Set-SPOTenant](/en-us/powershell/module/sharepoint-online/set-spotenant) cmdlet, specify the same *EnableAIPIntegration* parameter as described in the Use PowerShell to enable support for sensitivity labels section. But this time, set the parameter value to false and press **Y** to confirm:

```PowerShell
Set-SPOTenant -EnableAIPIntegration $false
```

If you have Microsoft 365 Multi-Geo, you must run this command for each of your geo-locations.

# [Label behavior](#tab/disable-considerations)
After you disable sensitivity labels for files in SharePoint and OneDrive, the following behaviors apply for files that have sensitivity labels applied:

| Scenario | Label applied before disabling | Label applied after disabling |
| --- | --- | --- |
| **Label visibility** | The label name remains visible, for example in the **Sensitivity** column, but you can't change or remove the label. | No label name displayed. |
| **Label encryption settings** | Encryption settings are honored and the file remains protected by the label. | Because the encrypted content can't be processed, the encryption settings can't be applied by SharePoint and OneDrive. |
| **Office for the web** | View and edit remains supported if the user has encryption permissions from the label. However, changes in these permissions won't be picked up. | Not supported for labeled and encrypted files. |
| **Search, eDiscovery, DLP** | Supported for labeled and encrypted files. | Not supported for labeled and encrypted files. |
| **Coauthoring** | Supported for labeled and encrypted files. | Not supported for labeled and encrypted files. |

If you use [SharePoint IRM](set-up-irm-in-sp-admin-center) as your alternative protection method, the behavior for files labeled and encrypted before you disable sensitivity labels for files in SharePoint and OneDrive remains the same as documented in SharePoint Information Rights Management (IRM) and sensitivity labels.

To restore consistent behavior, re-enable support for sensitivity labels and re-upload or re-label affected files.

---