---
layout: Conceptual
title: Overview of restoring a Cloud PC to a previous state with Windows 365 Enterprise | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/restore-overview
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn about restoring a Cloud PC to a previous state with Windows 365 Enterprise.
keywords: 
author: ErikjeMS
ms.author: aradinger
manager: dougeby
ms.date: 2025-04-17T00:00:00.0000000Z
ms.topic: concept-article
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: docoombs
ms.suite: ems
search.appverid: MET150
ms.custom: 
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: ad9f0543-be75-98f3-743c-bf6814f77663
document_version_independent_id: ad9f0543-be75-98f3-743c-bf6814f77663
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/restore-overview.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/restore-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/restore-overview.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: e7023cb1-ce14-25ba-7e40-cae200fa9579
---

# Overview of restoring a Cloud PC to a previous state with Windows 365 Enterprise | Microsoft Learn

Point-in-time restore lets an administrator restore a Cloud PC to the exact state it was at an earlier point in time. You can [create new or edit settings](restore-configure) to automatically create restore points at regular intervals for groups of Cloud PCs. You can also create on-demand restore points for specific times. Admins can also give users permission to restore their own Cloud PCs.

## Restore point options

There are three different ways to [set restore points](restore-configure):

- Short-term restore points
- Long-term restore points
- On-demand manual restore points

Each type of restore point can be [restored](restore-single-cloud-pc) in the same way.

### Short-term restore points

You can choose to set short-term restore points every 4, 6, 12, 16, or 24 hours. Each Cloud PC in the assigned groups has 10 short-term restore points saved at the intervals that you define in the user setting. For example, if you chose four hour intervals, each assigned Cloud PC has 10 restore points spread out every four hours over the last 40 hours.

### Long-term restore points

In addition to the configurable short-term restore points, there are also four long-term restore points that aren't configurable. These long-term restore points are saved every seven days.

### On-demand manual restore point

Manual restore points let administrators [create a restore point](create-manual-restore-point) whenever they want, for both a single Cloud PC and groups of Cloud PCs (using bulk actions).

Among other uses, on-demand manual restore points are useful:

- For creating a backup before taking management actions.
- During employee off-boarding with sharing a restore point.

Only administrators can create a manual restore point, and each Cloud PC can have only one manual restore point at a time.

### Expiration of restore points

For short- and long-term restore points, as time passes and a new restore point is added, the oldest restore point is removed.

Each Cloud PC can have one manual restore point. If you create another manual restore point for a Cloud PC that already has a manual restore point, the existing restore point is overwritten by the new restore point. If not overwritten, a manual restore point expires in approximately 28 days. Manual restore points have an expiration date that shows when they were created.

## Recovering Cloud PCs Deprovisioned due to License Expiration

For Windows 365 Enterprise Cloud PCs that have been deprovisioned due to Windows 365 Enterprise license expiration, a retention snapshot is saved. This does not include Cloud PCs that were deprovisioned when a license was removed from the user. If you follow the prerequisites, you can recover the Cloud PC to the point right before it was deprovisioned.

To follow the prerequisites for Cloud PC recovery, please:

- Ensure that expired [Windows 365 licenses](https://www.microsoft.com/en-us/windows-365/enterprise/all-pricing) are renewed. They must be of the same SKU.
- Ensure that the provisioning policy of the deprovisioned Cloud PC still exists.
- Ensure that the assignments with the right users is assigned to the provisioning policy.
- Ensure the end users still exist, are still assigned to the same Entra ID groups as before or the ones included in the policy assignments.

As long as the prerequisites above are met, once a license is renewed, a new Cloud PC should be provisioned for any of the end users that lost their Cloud PCs. Once the Cloud PCs have been successfully provisioned, you can individually restore the Cloud PCs using their retention snapshots effectively recovering the lost Cloud PC. Retention snapshots are available for 28 days after creation. The remaining retention period is displayed next to each snapshot in the restore point list. Restores from retention snapshots can take longer than standard restores because the snapshots are stored in archived storage.

To recover old Cloud PC :

- Go to [Intune](https://intune.microsoft.com/#home) -&gt; select **Devices** -&gt; select **All Cloud PCs** under **"Manage Windows365 Cloud PCs"**.
- Select the newly provisioned Cloud PC.
- Select the Restore option under the Cloud PC overview section.

![Restore_button](media/restore-overview/restore-button.png)

- If the new Cloud PC is deployed in the same region as the old CPC, you will see the retention snapshot with the remaining retention period displayed next to it.

![RetentionSnapshot](media/restore-overview/retentionsnapshot.png)

- Select the retention snapshot and click on **Restore** to restore the old CPC.

## Risks and results of restoring a Cloud PC

Cloud PCs have same risks as all Windows PCs when performing a full disk restore. These risks and results include:

- All changes made to the Cloud PC between the saved restore point and when the restore is started will be lost. This lost information includes all data, documents, installed applications, configurations, downloads, and other changes. External data stored in cloud services, like OneDrive, won't be lost.
- Various applications, agents and tools also use rolling passwords, secrets, certificates, and keys. If any of these credentials are updated between the current time and the restore point, the associated service or application will be impacted.
- The chances of data loss and automated machine account password updates increase with longer time gaps between the selected restore point and the current time.

## Best practices

- To minimize data loss and the risk of a rolling password conflict, choose a restore point that is as close as possible to the current time.
- After a restoration is complete, the user should immediately sign into their Cloud PC to verify that they can successfully connect. If a user can't connect, or experiences unexpected behavior, try a second restoration to a different restore point that is more recent. On rare occasions, you may need to reprovision/reset a Cloud PC if all restore points have obsolete rolling credentials.

## Unhealthy restore point

When viewing the restore point list for a Cloud PC, Windows 365 notes any unhealthy snapshots with the triangle symbol icon (![Image of unhealthy restore point warning icon](media/restore-overview/triangle.png)). Unhealthy snapshot have a low probability of successfully restoring the Cloud PC. This advisory status doesn’t block using the snapshot for any actions (like export, restore, share).

## Disaster recovery

When a restore is started, the virtual infrastructure used for the Cloud PC remains the same. If the infrastructure is unavailable, but appropriate alternate infrastructure is available in the same Azure region, then the Cloud PC is automatically placed in the available infrastructure. This automation makes sure, for a disaster recovery scenario in an Azure zone, that the Cloud PC is resilient through recovery to a different Zone in the region. The recovery to an alternate infrastructure is automatic. There's nothing required of the administrator or user other than to start the restore.