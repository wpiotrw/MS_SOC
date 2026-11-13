---
layout: Conceptual
title: Minimum versions for sensitivity labels in Microsoft 365 Apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sensitivity-labels-versions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
ms.reviewer: pefrem
manager: laurawi
ms.date: 2026-06-30T00:00:00.0000000Z
audience: Admin
ms.topic: reference
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
search.appverid:
- MOE150
description: Identify the minimum versions of Office apps that support specific capabilities for sensitivity labels from Microsoft Purview Information Protection.
locale: en-us
document_id: 0383a7eb-e0e8-220a-5816-446e3592ddb2
document_version_independent_id: 0383a7eb-e0e8-220a-5816-446e3592ddb2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sensitivity-labels-versions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sensitivity-labels-versions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sensitivity-labels-versions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/19e6356c-ba1e-4d22-9557-6222c183f04d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
- https://authoring-docs-microsoft.poolparty.biz/devrel/01e6eca5-e701-4cd9-a21f-56c9258f473e
2PlusCloud:
- M365
- Azure
- Power
platformId: 25cd4075-210c-8b56-d8f3-26ac184b9dfc
---

# Minimum versions for sensitivity labels in Microsoft 365 Apps | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

The capabilities tables on this page supplement [Manage sensitivity labels in Office apps](sensitivity-labels-office-apps) by listing the minimum Office version that introduced specific capabilities for sensitivity labels built in to Word, Excel, PowerPoint, and Outlook. Alternatively, the tabels indicate if the label capability is in public preview or not available.

For other apps that support sensitivity labels, check their documentation.

New versions of Office apps are made available at different times for different update channels. For Windows, you'll get the new capabilities earlier when you're on the Current Channel or Monthly Enterprise Channel, rather than Semi-Annual Enterprise Channel. The minimum version numbers can also be different from one update channel to the next. For more information, see [Overview of update channels for Microsoft 365 Apps](/en-us/deployoffice/overview-update-channels) and [Update history for Microsoft 365 Apps](/en-us/officeupdates/update-history-microsoft365-apps-by-date).

New capabilities that are in private preview aren't included in the tables but you might be able to join these previews by nominating your organization for the [Microsoft Information Protection private preview program](https://aka.ms/mip-preview).

Tip

When you compare the minimum versions in the tables with the versions you have, remember the common practice of release versions to omit leading zeros.

For example, you have version 4.2128.0 and read that 4.7.1+ is the minimum version. For easier comparison, read 4.7.1 (no leading zeros) as 4.**0007**.1 (and not 4.\*\* 7000\*\*.1). Your version of 4.2128.0 is higher than 4.0007.1; so, your version is supported.

## Sensitivity label capabilities in Word, Excel, and PowerPoint

The numbers listed are the minimum Office application versions required for each capability.

Note

For Windows and the Semi-Annual Enterprise Channel, the minimum supported version numbers might not yet be released. [Learn more](/en-us/officeupdates/update-history-microsoft365-apps-by-date#supported-versions).

| Capability | Windows | Mac | iOS | Android | Web |
| --- | --- | --- | --- | --- | --- |
| [Manually apply, change, or remove label](https://support.microsoft.com/office/apply-sensitivity-labels-to-your-files-and-email-in-office-2f96e7cd-d5a4-403b-8bd7-4cc636bae0f9) | Current Channel: 1910+  Monthly Enterprise Channel: 1910+  Semi-Annual Enterprise Channel: 2002+ | 16.21+ | 2.21+ | 16.0.11231+ | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files) |
| [Multi-language support](create-sensitivity-labels#additional-label-settings-with-security--compliance-powershell) | Current Channel: 1910+  Monthly Enterprise Channel: 1910+  Semi-Annual Enterprise Channel: 2002+ | 16.21+ | 2.21+ | 16.0.11231+ | Not available |
| [Apply a default label](sensitivity-labels#what-label-policies-can-do) to new documents | Current Channel: 1910+  Monthly Enterprise Channel: 1910+  Semi-Annual Enterprise Channel: 2002+ | 16.21+ | 2.21+ | 16.0.11231+ | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files) |
| [Apply a default label](sensitivity-labels#what-label-policies-can-do) to existing documents | Current Channel: 2208+  Monthly Enterprise Channel: 2207+  Semi-Annual Enterprise Channel: 2302+ | 16.63+ | Not available | Not available | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files) |
| [Require a justification to change a label](sensitivity-labels#what-label-policies-can-do) | Current Channel: 1910+  Monthly Enterprise Channel: 1910+  Semi-Annual Enterprise Channel: 2002+ | 16.21+ | 2.21+ | 16.0.11231+ | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files) |
| [Provide help link to a custom help page](sensitivity-labels#what-label-policies-can-do) | Current Channel: 1910+  Monthly Enterprise Channel: 1910+  Semi-Annual Enterprise Channel: 2002+ | 16.21+ | 2.21+ | 16.0.11231+ | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files) |
| [Mark the content](sensitivity-labels#what-sensitivity-labels-can-do) | Current Channel: 1910+  Monthly Enterprise Channel: 1910+  Semi-Annual Enterprise Channel: 2002+ | 16.21+ | 2.21+ | 16.0.11231+ | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files) |
| [Markings with variables](sensitivity-labels-office-apps#content-markings-with-variables) | Current Channel: 2010+  Monthly Enterprise Channel: 2010+  Semi-Annual Enterprise Channel: 2102+ | 16.42+ | 2.42+ | 16.0.13328+ | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files) |
| [Assign permissions now](encryption-sensitivity-labels#assign-permissions-now) | Current Channel: 1910+  Monthly Enterprise Channel: 1910+  Semi-Annual Enterprise Channel: 2002+ | 16.21+ | 2.21+ | 16.0.11231+ | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files) |
| [Let users assign permissions:  - Prompt users for custom permissions (users and groups)](encryption-sensitivity-labels#let-users-assign-permissions) | Current Channel: 2004+  Monthly Enterprise Channel: 2004+  Semi-Annual Enterprise Channel: 2008+ | 16.35+ | Not available | Not available | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files#support-for-labels-configured-for-user-defined-permissions) |
| [Let users assign permissions:  - Prompt users for custom permissions (users, groups, and organizations)](encryption-sensitivity-labels#support-for-organization-wide-custom-permissions) | Current Channel: 2212+  Monthly Enterprise Channel: 2302+  Semi-Annual Enterprise Channel: 2302+ | Not available | Not available | Not available | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files#support-for-labels-configured-for-user-defined-permissions) |
| [Audit label-related user activity](sensitivity-labels-office-apps#auditing-labeling-activities):  - Excludes encryption details | Current Channel: 2011+  Monthly Enterprise Channel: 2011+  Semi-Annual Enterprise Channel: 2108+ | 16.43+ | 2.46+ | 16.0.13628+ | Yes |
| [Audit label-related user activity](sensitivity-labels-office-apps#auditing-labeling-activities):  - Includes encryption details | Current Channel: 2301+  Monthly Enterprise Channel: 2302+  Semi-Annual Enterprise Channel: 2302+ | 16.70+ | 2.70+ | 16.0.16130+ | Not available |
| [Require users to apply a label to their email and documents](sensitivity-labels-office-apps#require-users-to-apply-a-label-to-their-email-and-documents) | Current Channel: 2101+  Monthly Enterprise Channel: 2101+  Semi-Annual Enterprise Channel: 2108+ | 16.45+ | 2.47+ | 16.0.13628+ | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files) |
| [Apply a sensitivity label to files automatically](apply-sensitivity-label-automatically) - Using sensitive info types | Current Channel: 2009+  Monthly Enterprise Channel: 2009+  Semi-Annual Enterprise Channel: 2102+ | 16.44+ | Not available | Not available | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files) |
| [Apply a sensitivity label to files automatically](apply-sensitivity-label-automatically) - Using trainable classifiers | Current Channel: 2105+  Monthly Enterprise Channel: 2105+  Semi-Annual Enterprise Channel: 2108+ | 16.49+ | Not available | Not available | Not available |
| [Support co-authoring and AutoSave](sensitivity-labels-coauthoring) for labeled and encrypted documents | Current Channel: 2107+  Monthly Enterprise Channel: 2107+  Semi-Annual Enterprise Channel: 2202+ | 16.51+ | 2.58+ | 16.0.14931+ | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files) |
| [PDF support](sensitivity-labels-office-apps#pdf-support) | Current Channel: 2208+  Monthly Enterprise Channel: 2209+  Semi-Annual Enterprise Channel: 2302+ | Not available | 2.82+ | 16.0.17224+ | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files) |
| [Sensitivity bar](sensitivity-labels-office-apps#sensitivity-bar) and [display label color](sensitivity-labels-office-apps#label-colors) | Current Channel: 2302+  Monthly Enterprise Channel: 2303+  Semi-Annual Enterprise Channel: 2302+ | 16.71+ | Not available | Not available | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files) |
| [Default sublabel for parent or group label](sensitivity-labels-office-apps#specify-a-default-sublabel-for-a-parent-label-or-label-group) | Current Channel: 2302+  Monthly Enterprise Channel: 2302+  Semi-Annual Enterprise Channel: 2302+ | Not available | Not available | Not available | Not available |
| [Scope labels to files or emails](sensitivity-labels-office-apps#scope-labels-to-just-files-or-emails) | Current Channel: 2301+  Monthly Enterprise Channel: 2302+  Semi-Annual Enterprise Channel: 2302+ | 16.70+ | 2.70+ | 16.0.16130+ | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files) |
| [Double Key Encryption (DKE)](encryption-sensitivity-labels#double-key-encryption) | Current Channel: 2307+  Monthly Enterprise Channel: 2309+  Semi-Annual Enterprise Channel: 2308+ | 16.85+ | 2.85+ | 16.0.18227+ | Not available |
| [Document tracking and revocation](track-and-revoke-admin) | Current Channel: 2402+  Monthly Enterprise Channel: 2402+  Semi-Annual Enterprise Channel: 2402+ | Not available | Not available | Not available | Not available |
| [Prevent some connected experiences that analyze content](sensitivity-labels-office-apps#prevent-connected-experiences-that-analyze-content) | Current Channel: 2406+  Monthly Enterprise Channel: 2406+  Semi-Annual Enterprise Channel: 2402+ | Not available | Not available | Not available | Not available |
| [Prevent all connected experiences that analyze content](sensitivity-labels-office-apps#prevent-connected-experiences-that-analyze-content) | Rolling out to Current Channel: 2606+  Rolling out to Monthly Enterprise Channel: 2606+ | Rolling out: 16.110+ | Rolling out: 2.111+ | Rolling out: 16.0.20026+ | Not available |
| [Dynamic watermarks](encryption-sensitivity-labels#dynamic-watermarks) - Encryption option: [Assign permissions now](encryption-sensitivity-labels#assign-permissions-now) | Current Channel: 2411+  Monthly Enterprise Channel: 2412+ | 16.94+ | 2.94+ | 16.0.18526+ | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files) |
| [Dynamic watermarks](encryption-sensitivity-labels#dynamic-watermarks) - Encryption option: [Let users assign permissions](encryption-sensitivity-labels#let-users-assign-permissions) | Current Channel: 2503+ | 16.96+ | 2.96+ | 16.0.18730+ | [Yes - opt-in](sensitivity-labels-sharepoint-onedrive-files) |

## Sensitivity label capabilities in Outlook

The numbers listed are the minimum Office application versions required for each capability.

Note

For Windows and the Semi-Annual Enterprise Channel, the minimum supported version numbers might not yet be released. [Learn more](/en-us/officeupdates/update-history-microsoft365-apps-by-date#supported-versions)

| Capability | Outlook for Windows | Outlook for Mac^\*\*\*^ | Outlook on iOS | Outlook on Android | Outlook on the web | New Outlook for Windows^\*^ |
| --- | --- | --- | --- | --- | --- | --- |
| Manually apply, change, or remove label  - [Files and emails](https://support.microsoft.com/office/apply-sensitivity-labels-to-your-files-and-email-in-office-2f96e7cd-d5a4-403b-8bd7-4cc636bae0f9) | Current Channel: 1910+  Monthly Enterprise Channel: 1910+  Semi-Annual Enterprise Channel: 2002+ | 16.21+ | 4.7.1+ | 4.0.39+ | Yes | Yes |
| Manually apply, change, or remove label  - [Calendar items](sensitivity-labels-meetings) | Current Channel: 2302+  Monthly Enterprise Channel: 2302+  Semi-Annual Enterprise Channel: 2402+ | 16.70+ ^\*\*^ | 4.2331.0+ | 4.2326.1+ | Yes | Yes |
| [Multi-language support](create-sensitivity-labels#additional-label-settings-with-security--compliance-powershell) | Current Channel: 1910+  Monthly Enterprise Channel: 1910+  Semi-Annual Enterprise Channel: 2002+ | 16.21+ | 4.7.1+ | 4.0.39+ | Yes | Yes |
| [Apply a default label](sensitivity-labels#what-label-policies-can-do) | Current Channel: 1910+  Monthly Enterprise Channel: 1910+  Semi-Annual Enterprise Channel: 2002+ | 16.21+ | 4.7.1+ | 4.0.39+ | Yes | Yes |
| [Require a justification to change a label](sensitivity-labels#what-label-policies-can-do) | Current Channel: 1910+  Monthly Enterprise Channel: 1910+  Semi-Annual Enterprise Channel: 2002+ | 16.21+ | 4.7.1+ | 4.0.39+ | Yes | Yes |
| [Provide help link to a custom help page](sensitivity-labels#what-label-policies-can-do) | Current Channel: 1910+  Monthly Enterprise Channel: 1910+  Semi-Annual Enterprise Channel: 2002+ | 16.21+ | 4.7.1+ | 4.0.39+ | Yes | Yes |
| [Mark the content](sensitivity-labels#what-sensitivity-labels-can-do) | Current Channel: 1910+  Monthly Enterprise Channel: 1910+  Semi-Annual Enterprise Channel: 2002+ | 16.21+ | 4.7.1+ | 4.0.39+ | Yes | Yes |
| [Content markings with variables](sensitivity-labels-office-apps#content-markings-with-variables) | Current Channel: 1910+  Monthly Enterprise Channel: 1910+  Semi-Annual Enterprise Channel: 2002+ | 16.21+ | 4.7.1+ | 4.0.39+ | Yes | Yes |
| [Assign permissions now](encryption-sensitivity-labels#assign-permissions-now) | Current Channel: 1910+  Monthly Enterprise Channel: 1910+  Semi-Annual Enterprise Channel: 2002+ | 16.21+ | 4.7.1+ | 4.0.39+ | Yes | Yes |
| [Let users assign permissions:  - Do Not Forward](encryption-sensitivity-labels#let-users-assign-permissions) | Current Channel: 1910+  Monthly Enterprise Channel: 1910+  Semi-Annual Enterprise Channel: 2002+ | 16.21+ | 4.7.1+ | 4.0.39+ | Yes | Yes |
| [Let users assign permissions:  - Encrypt-Only](encryption-sensitivity-labels#let-users-assign-permissions) | Current Channel: 2011+  Monthly Enterprise Channel: 2011+  Semi-Annual Enterprise Channel: 2108+ | 16.48+ ^\*\*^ | 4.2112.0+ | 4.2112.0+ | Yes | Yes |
| [Require users to apply a label to their email and documents](sensitivity-labels-office-apps#require-users-to-apply-a-label-to-their-email-and-documents) | Current Channel: 2101+  Monthly Enterprise Channel: 2101+  Semi-Annual Enterprise Channel: 2108+ | 16.43+ ^\*\*^ | 4.2111+ | 4.2111+ | Yes | Yes |
| [Audit label-related user activity](sensitivity-labels-office-apps#auditing-labeling-activities):  - Excludes encryption details | Current Channel: 2011+  Monthly Enterprise Channel: 2011+  Semi-Annual Enterprise Channel: 2108+ | 16.51+ ^\*\*^ | 4.2126+ | 4.2126+ | Yes | Yes |
| [Audit label-related user activity](sensitivity-labels-office-apps#auditing-labeling-activities):  - Includes encryption details | Current Channel: 2301+  Monthly Enterprise Channel: 2302+  Semi-Annual Enterprise Channel: 2302+ | 16.70+ ^\*\*^ | 4.2309+ | 4.2309+ | Not available | Not available |
| [Apply a sensitivity label to emails automatically](apply-sensitivity-label-automatically) - Using sensitive info types | Current Channel: 2009+  Monthly Enterprise Channel: 2009+  Semi-Annual Enterprise Channel: 2102+ | 16.44+ ^\*\*^ | Not available | Not available | Yes | Yes |
| [Apply a sensitivity label to emails automatically](apply-sensitivity-label-automatically) - Using trainable classifiers | Current Channel: 2105+  Monthly Enterprise Channel: 2105+  Semi-Annual Enterprise Channel: 2108+ | 16.49+ | Not available | Not available | Yes | Yes |
| [Different settings for default label and mandatory labeling](sensitivity-labels-office-apps#outlook-specific-options-for-default-label-and-mandatory-labeling) | Current Channel: 2105+  Monthly Enterprise Channel: 2105+  Semi-Annual Enterprise Channel: 2108+ | 16.43+ ^\*\*^ | 4.2111+ | 4.2111+ | Yes | Yes |
| [PDF support](sensitivity-labels-office-apps#pdf-support) | Current Channel: 2205+  Monthly Enterprise Channel: 2205+  Semi-Annual Enterprise Channel: 2302+ | Not available | Not available | Not available | Not available | Not available |
| [Apply S/MIME protection](sensitivity-labels-office-apps#configure-a-label-to-apply-smime-protection-in-outlook) | Current Channel: 2211+  Monthly Enterprise Channel: 2211+  Semi-Annual Enterprise Channel: 2302+ | 16.61+ ^\*\*^ | 4.2226+ | 4.2203+ | Yes | Yes |
| [Sensitivity bar](sensitivity-labels-office-apps#sensitivity-bar) | Current Channel: 2302+ Monthly Enterprise Channel: 2303+  Semi-Annual Enterprise Channel: 2302+ | Not available | 4.2316.0+ | 4.2316.0+ | Yes | Yes |
| [Display label color](sensitivity-labels-office-apps#label-colors) | Current Channel: 2302+  Monthly Enterprise Channel: 2303+  Semi-Annual Enterprise Channel: 2302+ | 16.71+ | 4.2316.0+ | 4.2316.0+ | Yes | Yes |
| [Default sublabel for parent or group label](sensitivity-labels-office-apps#specify-a-default-sublabel-for-a-parent-label-or-label-group) | Current Channel: 2302+  Monthly Enterprise Channel: 2302+  Semi-Annual Enterprise Channel: 2302+ | Not available | Not available | Not available | Not available | Not available |
| [Scope labels to files or emails](sensitivity-labels-office-apps#scope-labels-to-just-files-or-emails) | Current Channel: 2302+  Monthly Enterprise Channel: 2302+  Semi-Annual Enterprise Channel: 2302+ | 16.70+ ^\*\*^ | 4.2309+ | 4.2309+ | Yes | Yes |
| [Label inheritance from email attachments](sensitivity-labels-office-apps#configure-label-inheritance-from-email-attachments) | Current Channel: 2302+  Monthly Enterprise Channel: 2302+  Semi-Annual Enterprise Channel: 2302+ | Not available | Not available | Not available | Yes | Yes |
| [Double Key Encryption (DKE)](encryption-sensitivity-labels#double-key-encryption) | Current Channel: 2307+  Monthly Enterprise Channel: 2309+  Semi-Annual Enterprise Channel: 2308+ | Not available | Not available | Not available | Not available | Not available |
| [Prevent some connected experiences that analyze content](sensitivity-labels-office-apps#prevent-connected-experiences-that-analyze-content) | Current Channel: 2406+  Monthly Enterprise Channel: 2406+  Semi-Annual Enterprise Channel: 2402+ | Not available | Not available | Not available | Not available | Not available |

## Sensitivity label capabilities in OneNote

The numbers listed are the minimum OneNote application versions required for each capability.

Note

Tenant admins must opt in to enable sensitivity labels in OneNote within their tenants. [Learn more](sensitivity-labels-sharepoint-onedrive-files?tabs=disable-instructions#run-the-powershell-command-to-enable-support-for-sensitivity-labels)

| Capability | Windows | Mac | iOS | Android | Web |
| --- | --- | --- | --- | --- | --- |
| [Manually apply, change, or remove label](https://support.microsoft.com/office/apply-sensitivity-labels-to-your-files-and-email-in-office-2f96e7cd-d5a4-403b-8bd7-4cc636bae0f9) | Current Channel: 16.0.19426+  Monthly Enterprise Channel: 16.0.19426+ | 16.103+ | 16.103+ | 16.0.19426+ | Yes |
| [Multi-language support](create-sensitivity-labels#additional-label-settings-with-security--compliance-powershell) | Current Channel: 16.0.19426+  Monthly Enterprise Channel: 16.0.19426+ | 16.103+ | 16.103+ | 16.0.19426+ | Yes |
| [Apply a default label](sensitivity-labels#what-label-policies-can-do) to new documents | Not available | Not available | Not available | Not available | Not available |
| [Apply a default label](sensitivity-labels#what-label-policies-can-do) to existing documents | Not available | Not available | Not available | Not available | Not available |
| [Require a justification to change a label](sensitivity-labels#what-label-policies-can-do) | Current Channel: 16.0.19426+  Monthly Enterprise Channel: 16.0.19426+ | 16.103+ | 16.103+ | 16.0.19426+ | Yes |
| [Provide help link to a custom help page](sensitivity-labels#what-label-policies-can-do) | Current Channel: 16.0.19426+  Monthly Enterprise Channel: 16.0.19426+ | 16.103+ | 16.103+ | 16.0.19426+ | Yes |
| [Mark the content](sensitivity-labels#what-sensitivity-labels-can-do) | Current Channel: 16.0.19426+  Monthly Enterprise Channel: 16.0.19426+ | 16.103+ | 16.103+ | 16.0.19426+ | Yes |
| [Markings with variables](sensitivity-labels-office-apps#content-markings-with-variables) | Current Channel: 16.0.19426+  Monthly Enterprise Channel: 16.0.19426+ | 16.103+ | 16.103+ | 16.0.19426+ | Yes |
| [Assign permissions now](encryption-sensitivity-labels#assign-permissions-now) | Not available | Not available | Not available | Not available | Not available |
| Let users assign permissions:- [Prompt users for custom permissions (users and groups)](encryption-sensitivity-labels#let-users-assign-permissions) | Not available | Not available | Not available | Not available | Not available |
| Let users assign permissions:- [Prompt users for custom permissions (users, groups, and organizations)](encryption-sensitivity-labels#support-for-organization-wide-custom-permissions) | Not available | Not available | Not available | Not available | Not available |
| [Audit label-related user activity](sensitivity-labels-office-apps#auditing-labeling-activities):- Excludes encryption details | Current Channel: 16.0.19426+  Monthly Enterprise Channel: 16.0.19426+ | 16.103+ | 16.103+ | 16.0.19426+ | Yes |
| [Audit label-related user activity](sensitivity-labels-office-apps#auditing-labeling-activities):- Includes encryption details | Current Channel: 16.0.19426+  Monthly Enterprise Channel: 16.0.19426+ | 16.103+ | 16.103+ | 16.0.19426+ | Yes |
| [Require users to apply a label to their email and documents](sensitivity-labels-office-apps#require-users-to-apply-a-label-to-their-email-and-documents) | Not available | Not available | Not available | Not available | Not available |
| [Apply a sensitivity label to files automatically](apply-sensitivity-label-automatically)- Using sensitive info types | Not available | Not available | Not available | Not available | Not available |
| [Apply a sensitivity label to files automatically](apply-sensitivity-label-automatically)- Using trainable classifiers | Not available | Not available | Not available | Not available | Not available |
| [Support co-authoring and AutoSave](sensitivity-labels-coauthoring) for labeled and encrypted documents | Current Channel: 16.0.19426+  Monthly Enterprise Channel: 16.0.19426+ | 16.103+ | 16.103+ | 16.0.19426+ | Yes |
| [PDF support](sensitivity-labels-office-apps#pdf-support) | Current Channel: 16.0.19426+  Monthly Enterprise Channel: 16.0.19426+ | 16.103+ | 16.103+ | 16.0.19426+ | Not available |
| [Sensitivity bar](sensitivity-labels-office-apps#sensitivity-bar) and [display label color](sensitivity-labels-office-apps#label-colors) | Current Channel: 16.0.19426+  Monthly Enterprise Channel: 16.0.19426+ | 16.103+ | 16.103+ | 16.0.19426+ | Yes |
| [Default sublabel for parent label](sensitivity-labels-office-apps#specify-a-default-sublabel-for-a-parent-label-or-label-group) | Current Channel: 16.0.19426+  Monthly Enterprise Channel: 16.0.19426+ | 16.103+ | 16.103+ | 16.0.19426+ | Yes |
| [Scope labels to files or emails](sensitivity-labels-office-apps#scope-labels-to-just-files-or-emails) | Current Channel: 16.0.19426+  Monthly Enterprise Channel: 16.0.19426+ | 16.103+ | 16.103+ | 16.0.19426+ | Yes |
| [Double Key Encryption (DKE)](encryption-sensitivity-labels#double-key-encryption) | Not available | Not available | Not available | Not available | Not available |
| [Document tracking and revocation](track-and-revoke-admin) | Not available | Not available | Not available | Not available | Not available |
| [Prevent connected experiences that analyze content](sensitivity-labels-office-apps#prevent-connected-experiences-that-analyze-content) | Not available | Not available | Not available | Not available | Not available |
| [Dynamic watermarks](encryption-sensitivity-labels#dynamic-watermarks) | Not available | Not available | Not available | Not available | Not available |

**Footnotes:**

^\*^ For information about the new Outlook for Windows, see [Getting started with the new Outlook for Windows](https://support.microsoft.com/office/getting-started-with-the-new-outlook-for-windows-656bb8d9-5a60-49b2-a98b-ba7822bc7627)

^\*\*^ Requires the [new Outlook for Mac](https://support.microsoft.com/office/the-new-outlook-for-mac-6283be54-e74d-434e-babb-b70cefc77439)

^\*\*\*^ For Outlook for Mac, sensitivity labels for on-premises mailboxes require version 16.112 or later.

## Future releases

For information about new labeling capabilities that are planned for future releases, use the [Microsoft 365 roadmap](https://www.microsoft.com/microsoft-365/roadmap?filters=Microsoft%20Information%20Protection&amp;searchterms=label).