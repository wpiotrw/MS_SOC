---
layout: Conceptual
title: Use Preservation Lock to restrict changes to retention policies | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/retention-preservation-lock
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2024-06-10T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-records-management
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Use Preservation Lock with retention policies and retention label policies to help you meet regulatory requirements and safeguard against rogue administrators.
ms.custom: sfi-ga-nochange
locale: en-us
document_id: 8247d838-1610-a4ce-a8a4-a1eaa1e02c2c
document_version_independent_id: 8247d838-1610-a4ce-a8a4-a1eaa1e02c2c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/retention-preservation-lock.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: retention-preservation-lock
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/retention-preservation-lock.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 61fa9018-cc97-c3a7-6f72-6c8724093bda
---

# Use Preservation Lock to restrict changes to retention policies | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Important

Currently, [adaptive policy scopes](purview-adaptive-scopes#advantages-of-using-adaptive-scopes) don't support Preservation Lock.

Preservation Lock locks a retention policy or retention label policy so that no one—including a global admin—can turn off the policy, delete the policy, or make it less restrictive. This configuration might be needed for regulatory requirements and can help safeguard against rogue administrators.

When a retention policy is locked:

- No one can disable the policy or delete it
- Locations can be added but not removed
- You can extend the retention period but not decrease it

When a retention label policy is locked:

- No one can disable the policy or delete it
- Locations can be added but not removed
- Labels can be added but not removed

In summary, a locked policy can be increased or extended, but it can't be reduced or turned off.

Important

Before you lock a retention policy or retention label policy, it's critical that you understand the impact and confirm whether it's required for your organization. For example, it might be needed to meet regulatory requirements. Administrators won't be able to disable or delete these policies after the preservation lock is applied.

Configure Preservation Lock after you've created a [retention policy](create-retention-policies), or a retention label policy that you [publish](create-apply-retention-labels) and contains only labels that [mark items as regulatory records](records-management#records).

## How to lock a retention policy or retention label policy

You must use PowerShell if you need to use Preservation Lock. Because administrators can't disable or delete a policy for retention after this lock is applied, enabling this feature is not available in the UI to safeguard against accidental configuration.

All retention policies with any configuration support Preservation Lock. To apply Preservation Lock on a retention label policy, it must contain only labels that mark items as regulatory records.

1. [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).
2. Find the name of the policy that you want to lock by running [Get-RetentionCompliancePolicy](/en-us/powershell/module/exchange/get-retentioncompliancepolicy). For example:

    ![List of retention policies in PowerShell.](media/retention-policy-preservation-lock-get-retentioncompliancepolicy.png)
3. To place a Preservation Lock on your policy, run the [Set-RetentionCompliancePolicy](/en-us/powershell/module/exchange/set-retentioncompliancepolicy) cmdlet with the name of the policy, and the *RestrictiveRetention* parameter set to true:

    ```powershell
    Set-RetentionCompliancePolicy -Identity "<Name of Policy>" -RestrictiveRetention $true
    ```

    For example:

    ![RestrictiveRetention parameter in PowerShell.](media/retention-policy-preservation-lock-restrictiveretention.png)

    When prompted, read and acknowledge the restrictions that come with this configuration by entering **Y**:

    ![Prompt to confirm that you want to lock a retention policy in PowerShell.](media/retention-policy-preservation-lock-confirmation-prompt.png)

A Preservation Lock is now placed on the policy. To confirm, run `Get-RetentionCompliancePolicy` again, but specify the policy name and display the policy parameters:

```powershell
Get-RetentionCompliancePolicy -Identity "<Name of Policy>" |Fl
```

You should see **RestrictiveRetention** is set to **True**. For example:

![Locked policy with all parameters shown in PowerShell.](media/retention-policy-preservation-lock-locked-policy.png)