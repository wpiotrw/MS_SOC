---
layout: Conceptual
title: Types of Containers - FSLogix | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/fslogix/concepts-container-types
uhfHeaderId: MSDocsHeader-FSLogix
breadcrumb_path: /fslogix/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://aka.ms/avdideas
ms.service: fslogix
description: Technical overview for the various FSLogix containers
author: msft-jasonparker
ms.author: japarker
ms.topic: article
ms.date: 2025-08-26T00:00:00.0000000Z
ms.custom: template-concept
locale: en-us
document_id: d297fd90-e75b-7362-7d55-4e3691497644
document_version_independent_id: d297fd90-e75b-7362-7d55-4e3691497644
original_content_git_url: https://github.com/MicrosoftDocs/fslogix-docs-pr/blob/live/fslogix-docs/concepts-container-types.md
site_name: Docs
depot_name: MSDN.fslogix-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.fslogix-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: concepts-container-types
moniker_range_name: 
monikers: []
item_type: Content
source_path: fslogix-docs/concepts-container-types.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57ef615f-6bf1-4904-b6dc-96bb1d32c7e9
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1aea571c-6f95-42f8-b87e-c4d3aaf4bd7d
platformId: 9803805c-e834-dee2-1d57-6f61bbd38adc
---

# Types of Containers - FSLogix | Microsoft Learn

Important

An upcoming change to Windows, included in the April 2026 Windows Server update, the default Kerberos encryption type is changing from RC4 to AES-SHA1.

File shares hosting FSLogix containers that aren't upgraded to AES-SHA1 might have access issues after this change is applied. To avoid disruption, complete the upgrade to AES-SHA1 before installing the update.

Customers who have already upgraded to AES-SHA1 aren't affected.

For more information, see the FSLogix blog: [Action required: Windows Kerberos hardening (RC4) may affect FSLogix profiles on SMB storage](https://techcommunity.microsoft.com/blog/fslogix-blog/action-required-windows-kerberos-hardening-rc4-may-affect-fslogix-profiles-on-sm/4506378).

FSLogix has two (2) primary [container](concepts-fslogix-terminology) types, which can be implemented as part of your profile management solution. As outlined in our [terminology](concepts-fslogix-terminology) page, FSLogix containers are the virtual hard disk (VHD(x)) files, which hold all of the data for the given container type.

Note

Cloud Cache isn't a type of container, but it is an optional configuration for profile and ODFC container types. For more information, see [Cloud Cache overview](concepts-fslogix-cloud-cache).

## Profile container

A [profile](concepts-fslogix-terminology) container is the most common container used in an FSLogix solution. A profile container is all the data related to a user's profile, which is directly stored in the VHD(x). A Windows user profile is typically stored in `C:\Users\%username%`. Nearly all the files and folders found under this location would be included in an FSLogix profile container. Some data in a users profile shouldn't or can't be roamed which can be found in the exclusion list.

For users familiar with managing profiles, the function of the profile container may be compared to Microsoft User Profile Disk (UPD), Microsoft roaming profiles, or Citrix User Profile Management (UPM). Although the function is similar, the underlying method and technology is different, resulting in key FSLogix [capabilities](overview-what-is-fslogix#key-capabilities).

Note

Unless otherwise configured, the profile container will hold all profile and ODFC content in the same VHD(x) file. ***This is the recommended configuration.***

### Profile excluded content

There's two ways FSLogix excludes profile content from a user's VHD(x) container.

#### Redirection based exclusions

Profile content that can't be stored inside the user's VHD(x) container is [redirected](concepts-fslogix-terminology) from the native profile path to a new folder in the `C:\Users` path. This folder is prefixed with `local_` and combined with the user's SAM account name (for example, `C:\Users\local_%username%`). The local redirect is created to prevent issues with applications or processes that need access to this data in the event the remote [storage provider](concepts-fslogix-terminology) is unavailable. During sign out, the `C:\Users\local_%username%` folder is deleted.

FSLogix automatically redirects the following paths to the `C:\Users\local_%username%` path:

- `%userprofile%\AppData\Roaming\Microsoft\Protect`
- `%userprofile%\AppData\Roaming\Microsoft\Credentials`
- `%userprofile%\AppData\Local\Microsoft\Credentials`
- `%userprofile%\AppData\Local\Microsoft\Office\16.0\OfficeFileCache`

#### Deletion based exclusions

Profile content that isn't designed to be roamed between virtual machines is deleted from the user's VHD(x) container when the user is signed out. These deletion based exclusions are implemented based on the recommendations of the product teams which are responsible for the content.

##### Nonroamable application data (MSIX)

- `AppData\Local\Packages\*\AC`
- `AppData\Local\Packages\*\SystemAppData`
- `AppData\Local\Packages\*\LocalCache`
- `AppData\Local\Packages\*\TempState`
- `AppData\Local\Packages\*\AppData`

^**Reference:**[ApplicationData Class (Windows.Storage) - Windows apps](/en-us/uwp/api/windows.storage.applicationdata#remarks)^

##### Nonroamable identity data

Roaming this data through the [`RoamIdentity`](reference-configuration-settings?tabs=profiles#roamidentity) setting is **not recommended**.

- `AppData\Local\Packages\Microsoft.AAD.BrokerPlugin_cw5n1h2txyewy`
- `AppData\Local\Packages\Microsoft.Windows.CloudExperienceHost_cw5n1h2txyewy`
- `AppData\Local\Microsoft\TokenBroker`
- `AppData\Local\Microsoft\OneAuth`
- `AppData\Local\Microsoft\IdentityCache`
- `HKEY_CURRENT_USER\SOFTWARE\Microsoft\IdentityCRL`
- `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\AAD`
- `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows NT\CurrentVersion\WorkplaceJoin`
- `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows NT\CurrentVersion\TokenBroker`

^**Reference:**[Device identity and desktop virtualization](/en-us/entra/identity/devices/howto-device-identity-virtual-desktop-infrastructure#non-persistent-vdi)^

## ODFC container

An [ODFC](concepts-fslogix-terminology) container is a container type, which is focused on storing profile content that is unique to Microsoft Office applications^1^. The ODFC container is most commonly implemented in conjunction other roaming profile solutions^2^.

^1 Office data includes, but is not limited to Office apps, OneDrive, Teams, SharePoint, and OneNote.^^2 Traditional roaming profiles, Citrix User Profile Management, VMware Dynamic Environment Manager, or similar. ^

Important

When using ODFC containers with other profile roaming solutions, be sure the other solutions are configured to [exclude the ODFC data](tutorial-configure-odfc-containers#exclusions-for-third-party-roaming-profiles).

A default ODFC container configuration includes the following data:

- Office Activation
- Outlook
- Outlook personalization
- SharePoint
- OneDrive
- Skype for Business (legacy support)

Most data contained in the ODFC container is sourced from other remote systems and is easily replaced should the ODFC container become corrupted or deleted. For example, Outlook data files are generated from remote e-mail servers (for example, Microsoft 365). The list of applications that can be included are found in the [ODFC reference](reference-configuration-settings?tabs=odfc#tabpanel_1_odfc) article.

Note

ODFC containers are an [optional](overview-faq#do-i-need-to-use-the-odfc-container-when-using-microsoft-365-applications) configuration.

## When to use Profile and ODFC containers

Profile and ODFC containers should be used together when:

- Discretion is wanted in the storage location for Office data vs. other profile data.
- Provides isolation from data loss or corruption in one of the containers^3^.
- Used as a mechanism to specify which Office components have their data included in the container^4^.
- Allows organizations to have different container sizes to accommodate specific workloads or data synced from OneDrive^5^.

^3 ODFC container is not backed up or replicated to alternate locations since the data is recoverable from the source.^^4 Not available when using a single container configuration.^^5 Configure 10 GB profile container with a 50 GB ODFC container.^