---
layout: Conceptual
title: FSLogix Release Notes - FSLogix | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/fslogix/overview-release-notes
uhfHeaderId: MSDocsHeader-FSLogix
breadcrumb_path: /fslogix/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://aka.ms/avdideas
ms.service: fslogix
description: Provides a list of updates, changes, and fixes in FSLogix official releases.
author: msft-jasonparker
ms.author: japarker
ms.topic: overview
ms.date: 2025-08-26T00:00:00.0000000Z
ms.custom: template-overview
locale: en-us
document_id: 3c140ca1-20a5-7766-a04d-d1cac53f1466
document_version_independent_id: 3c140ca1-20a5-7766-a04d-d1cac53f1466
original_content_git_url: https://github.com/MicrosoftDocs/fslogix-docs-pr/blob/live/fslogix-docs/overview-release-notes.md
site_name: Docs
depot_name: MSDN.fslogix-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.fslogix-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: overview-release-notes
moniker_range_name: 
monikers: []
item_type: Content
source_path: fslogix-docs/overview-release-notes.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57ef615f-6bf1-4904-b6dc-96bb1d32c7e9
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1aea571c-6f95-42f8-b87e-c4d3aaf4bd7d
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
2PlusCloud:
- Azure
- Power
- M365
__autotagging_hash:
- 9FB3C3A7E8DD74EE36C2E724D8AB79D3478EAA773839FBA4ED1DF3E6D69913F3
platformId: c5c471dc-6f0b-aada-2bfc-9efa65a84ac3
---

# FSLogix Release Notes - FSLogix | Microsoft Learn

Important

An upcoming change to Windows, included in the April 2026 Windows Server update, the default Kerberos encryption type is changing from RC4 to AES-SHA1.

File shares hosting FSLogix containers that aren't upgraded to AES-SHA1 might have access issues after this change is applied. To avoid disruption, complete the upgrade to AES-SHA1 before installing the update.

Customers who have already upgraded to AES-SHA1 aren't affected.

For more information, see the FSLogix blog: [Action required: Windows Kerberos hardening (RC4) may affect FSLogix profiles on SMB storage](https://techcommunity.microsoft.com/blog/fslogix-blog/action-required-windows-kerberos-hardening-rc4-may-affect-fslogix-profiles-on-sm/4506378).

These releases follow a pattern of internal testing (self-host), early access, and general availability (GA). You can opt into early access by joining the [Microsoft Management Customer Connection Program](https://aka.ms/joinCCP). When necessary, a critical update might be released quickly following a GA release.

Important

Customers are required to install and use the [latest version](https://aka.ms/fslogix-latest). For more information, see [FSLogix product support](troubleshooting-fslogix-product-support).

## FSLogix 26.08

- **Version:** 3.26.826.17182
- **Date published:** August 31, 2026

### Summary

This release provides a set of security, stability, and data-protection fixes. New background Cloud Kerberos ticket refresh for Microsoft Entra-joined devices.

### What's new

- **Cloud Kerberos ticket refresh:** FSLogix now refreshes users' Cloud Kerberos ticket in the background during a session, and on VHD reconnect/reattach, keeping authentication to Entra Kerberos-backed storage such as Azure Files valid throughout long sessions and after resume. This avoids reconnect and storage-access failures that previously required the user to sign out and back in.

Note

This feature does not change the current 10 hour ticket lifetime of the Cloud Kerberos ticket. This feature provides mitigation for long running sessions (&gt; 10 hours) until a long term solution can be implemented.

### Fixed issues

- Addressed several security vulnerabilities in the FSLogix driver and service, including an elevation of privilege and kernel memory-safety issues.
- Fixed a driver crash that could occur during redirection setup when a container filename allocation failed.
- Fixed an issue where unlinking OneDrive during a session could lead to data loss.
- Fixed an issue where OneDrive cloud-only placeholder files could be corrupted during container mirror-back, causing sync errors or a sync client crash loop.
- Fixed multiple issues that could cause a bugcheck (Stop Codes: 0x139, 0x50, and APC\_INDEX\_MISMATCH).
- Fixed a deadlock that could cause long sign-out delays when [`CleanupInvalidSessions`](reference-configuration-settings?tabs=profiles#cleanupinvalidsessions) was enabled with ODFC containers.
- Fixed an issue where a locked or unresponsive container could block all sign-ins and sign-outs on a host until reboot, and improved retry handling for locked container files.
- Fixed an issue where a stuck storage provider could hang sign-out and leave containers attached.
- Fixed an issue where OneDrive files could remain in a pending-delete state even when [`IncludeOneDrive`](reference-configuration-settings?tabs=odfc#includeonedrive) was disabled.
- Fixed two identity data exclusion issues that could remove certificates from the user's Personal store or prevent OneDrive/Entra sign-in.

### File information

Download the following package and follow the [installation instructions](how-to-install-fslogix)

- [Download FSLogix 26.08 (3.26.826.17182)](https://download.microsoft.com/download/ae6d2014-e692-45fa-a88b-ee552567cdc1/FSLogix_26.08.zip)

## FSLogix 26.01 CU1 (critical update)

- **Version:** 3.26.126.19110
- **Date published:** February 10, 2026

### Summary

This is a critical update to the 26.01 release.

### What's new

- This version doesn't have any new features or functionality.

### Fixed issues

- Fixed an issue that prevented ODFC VHD(x) containers from creating or mounting when [`CleanupInvalidSessions`](reference-configuration-settings?tabs=profiles#cleanupinvalidsessions) was enabled.

Note

This only affects configurations using both Profiles and ODFC.

### File information

Download the following package and follow the [installation instructions](how-to-install-fslogix)

- [Download FSLogix 26.01 CU1 (3.26.126.19110)](https://download.microsoft.com/download/e9eed5b4-83ff-4b93-bf87-765509e6fd85/FSLogix_26.01_CU1.zip)

## FSLogix 26.01

- **Version:** 3.26.102.18413
- **Date published:** January 13, 2026

### Summary

This release provides a set of updates and fixes.

### What's new

- This version doesn't have any new features or functionality.

### Fixed issues

- Updated the default identity exclusions as defined in [Device identity and desktop virtualization | Microsoft Learn](/en-us/entra/identity/devices/howto-device-identity-virtual-desktop-infrastructure#microsofts-guidance).
- Fixed the registry exclusions.
- Fixed logging when a user is excluded using local exclude groups.
- Fixed FRX.exe copy-profile utility.
- Updated default redirections in Outlook for Windows.
- Fixed an issue where a disk may not detach correctly after a compact operation.
- Fixed a potential logon hang when a profile does not unload successfully during a timeout operation (&lt; 30 sec).
- Fixed extended status of SupportedSize for VHD compact operations.
- Fixed an issue where package registration could fail due to missing authentication context.

### File information

Download the following package and follow the [installation instructions](how-to-install-fslogix)

- [Download FSLogix 26.01 (3.26.102.18413)](https://download.microsoft.com/download/60d5e1c8-aacf-41c3-b215-2ca57876d064/FSLogix_26.01.zip)

## FSLogix 25.09

- **Version:** 3.25.822.19044
- **Date published:** September 9, 2025

### Summary

This release provides a set of updates and fixes.

### What's new

- Added new exclusions to our [profile deletion exclusions](concepts-container-types#deletion-based-exclusions).

### Fixed issues

- Fixed an issue where a redirection removed prior to sign out resulted in a bugcheck E3 or 24 (Stop Code: 0xE3, 0x24).
- Removed a driver feature flag that indicated support for `QUERY_OPEN` when it didn't exist in the driver.
- Fixed an issue where a single item in the redirected Recycle Bin would display the incorrect name when emptied.
- Fixed an issue when creating an application rule for [specify value](concepts-fslogix-apps-rule-editor-rule-sets#specify-value-rule), the wrong UI was displayed.

### File information

Download the following package and follow the [installation instructions](how-to-install-fslogix)

- [Download FSLogix 25.09 (3.25.822.19044)](https://download.microsoft.com/download/8fc0f8ba-e928-4aa7-8b85-f6655b6a15ab/FSLogix_25.09.zip)

## FSLogix 25.06

- **Version:** 3.25.626.21064
- **Date published:** July 8, 2025

### Summary

This release provides compatibility and support for [Microsoft Outlook for Windows](/en-us/microsoft-365-apps/outlook/get-started/virtualized-desktop-infrastructure) (MSIX version).

### What's new

- Support, data roaming, and application registration for [Microsoft Outlook for Windows](/en-us/microsoft-365-apps/outlook/get-started/virtualized-desktop-infrastructure)(MSIX version).
    - Enabled special handling for the registration of the MSIX package family in both Profiles and ODFC.
    - Supports redirections of the application data for ODFC containers.
    - Allows coexistence between classic and Outlook for Windows under a [single configuration setting](reference-configuration-settings?tabs=odfc#includeoutlook).

### Fixed issues

- Fixed an issue where FSLogix attempted to look up a user token before it was initialized during profile load.

### File information

Download the following package and follow the [installation instructions](how-to-install-fslogix)

- [Download FSLogix 25.06 (3.25.626.21064)](https://download.microsoft.com/download/a7599f72-a0b3-49a1-9ece-2f54f6557ee1/FSLogix_25.06.zip)

## FSLogix 25.04

- **Version:** 3.25.401.15305
- **Date published:** April 8, 2025

### Summary

This release provides updates to address five known issues introduced in 25.02.

### Fixed issues

- FSLogix containers don't detach and prevent users from signing into a new session.
- FSLogix Rules don't apply to users as expected.
- FRXShell rule fails clean-up and prevents all user sign ins.
- After signing in, user receives an error message that the Recycle Bin is corrupted.
- Searchindexer.exe (frx\_usermode\_x64.dll) crashing in Windows Server 2016.

### File information

Download the following package and follow the [installation instructions](how-to-install-fslogix)

- [Download FSLogix 25.04 (3.25.401.15305)](https://download.microsoft.com/download/38803434-6d52-4668-b9a4-4d9bcf07248e/FSLogix_25.04.zip)

## FSLogix 25.02

- **Version:** 3.25.202.4223
- **Date published:** February 11, 2025

### Summary

This release is a change in versioning and release structure. This update to v3 introduces a versioning that is date / time formatted and based on when the product was created. While not feature packed, we made significant updates and improvements to enhance overall stability. Additionally, this release retired various features from the product and no longer supports 32-bit operating systems.

### What's new

- Major version change (2 → 3) and updated how FSLogix release names and build versions are defined. In future releases, major releases will increment the major version from 3 to 4 to 5, etc.
    - **Example:**
        - **Release name:** 25.02
        - **Build version:** 3.25.202.4223 (3.YY.MMDD.HHMMS, *Single digit months don't have a leading 0*)
- Cloud Cache no longer assumes some failure states are a bad configuration and now allows customers to test and validate their configurations for redundancy through any method they choose.
- [Microsoft.FSLogix PowerShell module](utilities/powershell/microsoft-fslogix) used for Cloud Cache investigation and troubleshooting.
- When `RedirXMLSourceFolder` is removed or 'not configured' in Group Policy, the redirections.xml file is now removed from within the user's profile container at the next sign-in.

### Fixed issues

- LocalCache and TempState folders for MSIX packages are now properly cleaned up during sign out.
- Fixed an issue related to symlink reparse points affecting App-V and other components that have similar calls.
- VHD disk compaction for differencing disks now works the same as disks without a differencing disk.

    Note

    Compaction results are based on each disk and what space is able to be reclaimed during the optimization.
- ADMX templates were updated to allow settings that are enabled by default to be disabled.
- Sign-in and sign out optimizations to ensure MSIX settings are properly handled before and after the Windows shell events.

    Note

    This optimization is most notable when reviewing text logs.

    ```output
    ===== Begin Session: Post Profiles Logon
    ===== End Session: Post Profiles Logon
    ===== Begin Session: Pre Profiles Logoff
    ===== End Session: Pre Profiles Logoff
    ```

### Feature retirement

- [Support for Windows Server 2012 R2](troubleshooting-fslogix-product-support#server-operating-systems)
- [Support for 32-bit operating systems](troubleshooting-fslogix-product-support#operating-system-bit-architecture)
- [Cloud Cache CcdMaxCacheSizeInMBs (limited cache)](reference-configuration-settings?tabs=ccd#ccdmaxcachesizeinmbs-retired)
- Profiles Configuration Tool
- [App Container Rules](concepts-fslogix-apps-rule-editor-rule-sets#app-container-vhd-rule-retired)
- Internet Explorer browser plug-in
- [Application Rule Set license reporting](how-to-configure-rule-set-per-device-licensing#licensing-reports-retired)
- [Java Rule Editor and Java Rules](how-to-install-fslogix#install-fslogix-apps-rule-editor-and-java-rule-editor-retired)
- [FRXTray utility](reference-service-drivers-components#fslogix-profile-status-retired-frxtrayexe)

### File information

Download the following package and follow the [installation instructions](how-to-install-fslogix)

- [Download FSLogix 25.02 (3.25.202.4223)](https://download.microsoft.com/download/0d30db30-2d48-4640-a56c-3a1502fcb29a/FSLogix_25.02.zip)

## FSLogix 2210 hotfix 4

- **Version:** 2.9.8884.27471
- **Date published:** May 14, 2024

### Summary

This is a hotfix release to address known issues and other identified bugs. In addition, this release brings back the capability to roam a user's Group Policy state which provides asynchronous policy processing.

Important

This version provides a comprehensive set of changes to support new Microsoft Teams in virtual desktop environments.

### What's new

2210 hotfix 4 includes the following updates:

- Group Policy processing can now occur asynchronously for users during sign-in.
- MSIX folders under `%LocalAppData%\Packages\<package-name>\` are automatically created when an ODFC container is created (*new or reset container*).
- Teams data located in `%LocalAppData%\Publishers\8wekyb3d8bbwe\TeamsSharedConfig` will roam with the ODFC container.

### Fixed issues

2210 hotfix 4 includes the following fixed issues:

- Windows Server 2019 would sometimes fail to query the provisioned AppX applications for the user during sign out.
- [MSIX folders that shouldn't be backed up](troubleshooting-appx-issues#nonroamable-folders-not-backed-up) would be removed during sign out instead of only removing the contents of those folders.
- New Microsoft Teams crashes or fails to start in Windows Server 2019.
- New Microsoft Teams would display an error during launch with `The parameter is incorrect`.
- New Microsoft Teams would display an error during launch with `Invalid function`.
- New Microsoft Teams wouldn't on-demand register during sign-in when using the ODFC container.
- New Microsoft Teams wouldn't on-demand register during profile creation and wouldn't register during future sign-ins, despite being installed.
- User-based Group Policy settings would persist in the user's profile after the policy setting was removed or set to disabled.

### File information

Download the following package and follow the [installation instructions](how-to-install-fslogix)

- [Download FSLogix 2210 hotfix 4 (2.9.8884.27471)](https://download.microsoft.com/download/e/c/4/ec4b55b3-d2f3-4610-aebd-56478eb0d582/FSLogix_Apps_2.9.8884.27471.zip)