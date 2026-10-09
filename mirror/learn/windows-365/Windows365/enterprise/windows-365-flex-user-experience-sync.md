---
layout: Conceptual
title: User Experience Sync for Windows 365 Flex in Shared mode | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/windows-365-flex-user-experience-sync
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn about User Experience Sync for Windows 365 Flex in Shared mode
keywords: 
author: msft-jasonparker
ms.author: japarker
manager: stulimat
ms.date: 2026-06-02T00:00:00.0000000Z
ms.topic: overview
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: stulimat, scottduf
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
ai-usage: ai-assisted
locale: en-us
document_id: ba358325-d6d5-40da-af2e-9717f7e70ce6
document_version_independent_id: ba358325-d6d5-40da-af2e-9717f7e70ce6
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/windows-365-flex-user-experience-sync.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/windows-365-flex-user-experience-sync
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/windows-365-flex-user-experience-sync.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 4642bd84-727b-406d-4881-216c3a2c21a9
---

# User Experience Sync for Windows 365 Flex in Shared mode | Microsoft Learn

## Overview

User Experience Sync is a feature for [Windows 365 Flex Cloud PCs in Shared mode](introduction-windows-365-flex#windows-365-flex-in-shared-mode) and [Windows 365 Cloud Apps](cloud-apps). This cloud-native solution delivers a seamless and consistent experience for users across Cloud PC and Cloud App sessions. Microsoft manages the infrastructure and platform, reducing complexity and cost compared to traditional solutions. This feature preserves Windows personalization, user settings (including accessibility), application settings, and application data. This ensures users have a consistent, productive experience every time they sign in to their Cloud PC or Cloud App.

Tip

User Experience Sync is an experience optimization feature for shared Cloud PCs and Cloud Apps. It's not designed to as a backup or disaster recovery solution for user data.

![Screenshot explaining the 'User Experience Sync' feature.](media/user-experience-sync/user-experience-sync.png)

^**Figure 1:** What is User Experience Sync^

The feature provides pooled user storage for each policy. When enabled, each user receives their own dedicated storage hosted in the Microsoft Cloud.

## Prerequisites

- [Windows 365 Flex license](windows-365-flex-license)
- Access to required [Windows 365](requirements-network) endpoints
- Intune management permissions

## How User Experience Sync works

User Experience Sync creates and attaches individual user storage to shared Cloud PCs. When a user signs in, their individual storage is attached, providing access to their settings, files, and application data. When they sign out, the user storage is detached and stored in the Microsoft Cloud to be used the next time they sign in.

The system automatically handles profile loading and storage management without requiring traditional profile management solutions.

## Enabling User Experience Sync

When [creating and assigning a provisioning policy](create-provisioning-policy), select **Enable user experience sync** in the configuration section. This reveals an option to choose the user storage size from five available options: 4 GB, 8 GB, 16 GB, 32 GB, and 64 GB.

### Creating new policies with User Experience Sync

Follow the standard [provisioning policy creation process](create-provisioning-policy) and ensure you select the **Enable user experience sync** checkbox during configuration.

![Screenshot that shows you have selected the 'Enable user experience sync' checkbox during configuration.](media/user-experience-sync/enable-user-experience-sync-create-flow.png)

^**Figure 2:** Enable user experience sync during policy creation^

### Enabling / disabling on existing policies

To enable or disable the feature on an existing provisioning policy:

Important

Enabling or disabling User Experience Sync requires the assignment to be removed and re-added. This will deprovision all Cloud PCs and provision new Cloud PCs.

1. **Remove** the current group assignment from the **Properties** tab
2. **Edit** the configuration section and toggle **Enable user experience sync**
3. **[Optional]** Select a user storage size (*enable only*)
4. **Update** the policy
5. **Re-add** the group assignment

## User storage

User Experience Sync provides a limited amount of pooled user storage that is included with your [Windows 365 Flex license](windows-365-flex-license). The storage limit is calculated using the size of the OS disk from the Cloud PC configuration and is multiplied by the number of Cloud PCs in the assignment.

### Storage limits

- Cloud PC size includes vCPU, Memory, and OS storage (e.g., 4vCPU/16GB/128GB)
- OS storage size × number of Cloud PCs = total pooled storage available (128 x 10 = 1.28 TB)

![Screenshot of pooled storage based on Cloud PC size and count.](media/user-experience-sync/user-experience-sync-user-storage-example.png)

^**Figure 3:** Storage calculation of pooled user storage based on Cloud PC size and count^

Important

Pooled storage is unique to each policy and assignment. Removing an assignment permanently deletes all user storage.

### Storage limits and quotas

- **Maximum storage per user**: Determined by selected size (4 GB - 64 GB)
- **Policy-level storage limits**: Based on Cloud PC count and OS storage size

Note

- **Exceeded limits**: New users can sign in with a temporary profile, but can't create user storage when pooled storage is [exceeded](/en-us/troubleshoot/windows-365/troubleshoot-user-experience-sync#exceeded-storage-conditions). Users with existing user storage can sign in with their personalized experience.
- **Exceeded tolerance period**: When the limit of the pooled storage has been [exceeded](/en-us/troubleshoot/windows-365/troubleshoot-user-experience-sync#exceeded-storage-conditions), there is a tolerance period of 7 days. After the tolerance period, the service will automatically delete individual user storage with the oldest last attach timestamp. Once the pooled storage is under the limit, the tolerance period is reset until the next exceeded limit event.

## Managing user storage

User Experience Sync provides comprehensive management capabilities for monitoring and administering user storage across your deployment.

### Accessing user storage management

To view and manage user storage:

1. Navigate to the **Microsoft Intune admin center**.
2. Go to **Devices** &gt; **Provision Cloud PCs** &gt; **Provisioning policies**.
3. Select your User Experience Sync enabled policy.
4. Click the **User Storage** tab.

### User storage overview

The User Storage tab provides a comprehensive view of your storage allocation:

- **Storage information**: Cloud PC size, count, and configured user storage size
- **Total pooled user storage**: Maximum available storage for the policy
- **Available pooled user storage**: Remaining storage capacity
- **Used pooled user storage**: Currently consumed storage
- **Individual user storage details**: Per-user storage size, state, and last attach timestamp

![Screenshot that shows the cloud PC storage's total, available, used, and per-user details.](media/user-experience-sync/user-storage-management.png)

^**Figure 4:** User Storage monitoring and management^

### Monitoring storage usage

#### Set up proactive monitoring

**Enable storage alerts**:

- Navigate to **Tenant administration** &gt; **Cloud PC Alerts**.
- Enable the **Windows 365 Flex Cloud PC User Experience Sync Storage Limits** alert rule.
- Configure notification settings for your admin team.

**Regular monitoring schedule**:

- Review storage utilization weekly.
- Monitor user storage growth patterns.
- Identify inactive user storage for potential cleanup.

#### Storage optimization policies

Configure Windows features to optimize storage usage:

**OneDrive redirection**:

- Apply [OneDrive Group Policy](/en-us/sharepoint/use-group-policy) settings
- Manage files on demand, known folder move and space limits.

**Browser data management**:

- Configure [Microsoft Edge policies](/en-us/intune/intune-service/configuration/settings-catalog-configure-edge)
- Manage cache and temporary data retention

**Storage Sense configuration**:

- Deploy [Storage Sense policies](/en-us/windows/configuration/storage/storage-sense?tabs=intune)
- Automate cleanup of temporary files, downloads, and cloud backed files (OneDrive)

### Managing individual user storage

#### Delete user storage

To remove individual user storage:

**Single user deletion**:

1. In the **User Storage** tab, locate the target user
2. Select the checkbox next to the user's storage.
3. Click **Delete** from the action bar.
4. Confirm the deletion in the dialog box.

**Bulk user deletion**:

1. Use checkboxes to select multiple users.
2. Click **Delete** from the action bar.
3. Review the selected users in the confirmation dialog.
4. Confirm the bulk deletion.

Warning

Deleting user storage permanently removes all user settings, files, and application data. This action cannot be undone.

#### When to delete user storage

Consider deleting user storage in these scenarios:

- **Inactive users**: Users who haven't accessed Cloud PCs for extended periods
- **Storage capacity management**: When approaching pooled storage limits
- **Troubleshooting**: Resolving persistent user profile issues

### What's stored

User storage contains all data from `C:\Users\%username%`, including:

- User settings and application data
- Registry files (`NTUSER.dat` and `USRCLASS.dat`)
- Personal files and folders

### What's excluded

Certain data types are automatically excluded because they can't be used across different devices:

#### Nonroamable application data

- `AppData\Local\Packages\*\AC`
- `AppData\Local\Packages\*\SystemAppData`
- `AppData\Local\Packages\*\LocalCache`
- `AppData\Local\Packages\*\TempState`
- `AppData\Local\Packages\*\AppData`

#### Nonroamable identity data

- `AppData\Local\Packages\Microsoft.AAD.BrokerPlugin_cw5n1h2txyewy`
- `AppData\Local\Packages\Microsoft.Windows.CloudExperienceHost_cw5n1h2txyewy`
- `AppData\Local\Microsoft\TokenBroker`
- `AppData\Local\Microsoft\OneAuth`
- `AppData\Local\Microsoft\IdentityCache`

^**References:**[ApplicationData Class (Windows.Storage)](/en-us/uwp/api/windows.storage.applicationdata#remarks) | [Device identity and desktop virtualization](/en-us/entra/identity/devices/howto-device-identity-virtual-desktop-infrastructure#non-persistent-vdi)^

Note

You can't customize the data that is excluded from storage. [OneDrive](/en-us/sharepoint/use-group-policy), [Edge](/en-us/intune/intune-service/configuration/settings-catalog-configure-edge), and [Storage Sense](/en-us/windows/configuration/storage/storage-sense?tabs=intune) for example, have policy settings that can be applied to devices in Windows 365 that affect how they store or clean up data.

## User experience

### First-time user setup

When a user first signs in to a Cloud PC or Cloud App with User Experience Sync enabled, the system automatically creates and attaches their personal storage and begins capturing their data.

### Sign-in process

1. User authenticates to Cloud PC or Cloud App

    - *Initial sign-in*:
        - New user storage is created
        - User settings and application data are redirected to the user storage
    - *Subsequent sign-ins*:
        - Existing user storage is attached
        - User settings and application data is loaded from previous session
2. User session begins with personalized environment
3. User experience is automatically maintained inside the individual user storage

### Application data persistence

Administrator or Intune installed applications will have their settings persist across sessions, providing a consistent user environment regardless of which Cloud PC the user connects to.

Note

User Experience Sync does not roam or persist user installed applications. Only the application data (settings and preferences) are stored.

## Frequently asked questions (FAQ)

**Q: Can I migrate existing FSLogix profiles to User Experience Sync?**

A: Direct migration isn't supported. Users will need to recreate their personalization when first using User Experience Sync.

**Q: What happens if a user exceeds their storage allocation?**

A: The user experience will be degraded with intermittent and potentially unknown behaviors. The user's storage can be deleted or the policy can be changed to a larger user storage size (*affects all users*).

**Q: Can I change storage size after enabling User Experience Sync?**

A: Yes, storage size is set when the feature is enabled and can be modified later.

**Q: Is User Experience Sync available for dedicated Cloud PCs?**

A: No, it's only available for Windows 365 Flex in Shared mode and Cloud Apps.

**Q: How does User Experience Sync compare to traditional profile solutions?**

A: User Experience Sync is designed to optimize the end user experience on share Cloud PCs and is a cloud-native solution.

## Related documentation

- [Windows 365 Flex overview](introduction-windows-365-flex)
- [Cloud Apps documentation](cloud-apps)
- [Creating provisioning policies](create-provisioning-policy)
- [Windows 365 Flex licensing](windows-365-flex-license)
- [Cloud PC size recommendations](cloud-pc-size-recommendations)