---
layout: Conceptual
title: Migrate parent sensitivity labels to sensitivity label groups | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/migrate-sensitivity-label-scheme
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-04-17T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
ms.custom: admindeeplinkCOMPLIANCE
search.appverid:
- MOE150
- MET150
description: Migrate your sensitivity label scheme to convert parent labels to label groups and benefit from better organization and reduced deployment complexity.
locale: en-us
document_id: b4beef66-0c11-c40f-67cc-9a4534730643
document_version_independent_id: b4beef66-0c11-c40f-67cc-9a4534730643
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/migrate-sensitivity-label-scheme.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: migrate-sensitivity-label-scheme
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/migrate-sensitivity-label-scheme.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 2f3cb889-f413-686e-770c-a977d7ba4950
---

# Migrate parent sensitivity labels to sensitivity label groups | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Note

Migration is automatic if you have a new tenant beginning October 1, 2025 or the migration of parent labels won't create a new sublabel with the same name because you have applicable parent labels. In both these cases, your sensitivity labels will automatically use the modern label scheme to benefit from better organization and reduced deployment complexity.

Previously, parent labels were used to organize [sensitivity labels](sensitivity-labels) in a two-tier hierarchy. To reduce complexity, their replacement, label groups, don't support settings other than name, description, color, and priority.

For more information about parent labels and label groups, see [Sublabels that use parent labels or label groups](sensitivity-labels#sublabels-that-use-parent-labels-or-label-groups).

To migrate your parent sensitivity labels to sensitivity label groups, use the [Microsoft Purview portal](purview-portal) if you see the information banner displayed in the following instructions.

Caution

Label migration is irreversible. We highly recommend that you first test the migration by using a test tenant that has the same sensitivity label configurations as your production tenant.

## Before you begin

First, make sure you have permissions to create and manage sensitivity labels. For more information, see [Permissions required to create and manage sensitivity labels](get-started-with-sensitivity-labels#permissions-required-to-create-and-manage-sensitivity-labels).

Then, understand the impact of parent labels that if applicable, will be migrated to a sublabel with the same name, in addition to a label group. If this scenario applies to you, you must decide whether you want to leave these new sublabels published after the migration, or you want to unpublish them:

- If you decide to unpublish these new sublabels, you can do this manually, or use PowerShell scripts to automatically unpublish them.
- If you leave these new sublabels published, decide whether you will need to edit them post migration and before users can select them.

This new sublabel creation ensures that all users and services that might have accessed the parent label as a standalone label will continue to be able to access it after the migration.

- It's configured for label actions that include encryption, content marking, auto-labeling, and PowerShell [advanced settings](/en-us/powershell/module/exchangepowershell/set-label#-advancedsettings).
- It's included in a different publishing policy from its sublabels.
- It has a different label scope from its sublabels in one or more of the following ways:
    - A sublabel is configured for a label scope that the parent label isn't configured for.
    - Within the same label policy, the parent label has one or more scopes that aren't configured for any of its sublabels.

The resulting sublabel that's created has the same name, label GUID, and settings as the original parent label. Without reconfiguration, this new sublabel will be available to select in a policy where previously it couldn't be selected as a parent label.

Note

Because label GUIDs are unique in your tenant, they are used by backend services and configurations to reliably identify a sensitivity label. For example, we recommend you [use the GUID rather than the label name to configure advanced settings](create-sensitivity-labels#powershell-tips-for-specifying-the-advanced-settings).

To ensure business continuity post migration, the new sublabel inherits the GUID from the applicable parent label, and the new label group is given a new GUID.

You can confirm whether you have applicable parent labels before the labels are migrated when you review the proposed new label scheme as part of the migration process. In the following example, the parent label **Confidential** is identified as an applicable parent label, with the result that a new sublabel of the same name will be created:

![Migration process showing an applicable parent label that will result in a new sublabel of the same name.](media/applicable-parent-label-example.png)

### PowerShell scripts for unpublishing sublabels from applicable parent labels

These PowerShell commands use [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).

**Script One:** Before the migration, run the following command to fetch all policies that publish parent labels.

```PowerShell
$parents = (Get-Label | ? { $_.ParentId -ne $null } | %{ echo $_.ParentId } | Sort-Object -Unique)
$parentLabels = ($parents | % { Get-Label -Identity $_.Guid })
$policyPublishingParent = @{}
$policies = Get-LabelPolicy; $parentLabels | % { $parent = $_.Name; $policies | ? { $_.Labels -contains $parent } | 
% { echo "$($_.Name) policy has published $parent"; $(If ($policyPublishingParent.Keys -notcontains $_.Name) { 
$policyPublishingParent[$_.Name] = @() }); $policyPublishingParent[$_.Name] += $parent } }
```

Don't close your PowerShell session but keep it open during the label migration.

**Script Two:** As soon as migration is complete, run the following script to unpublish the newly created sublabels from applicable parent labels:

```PowerShell
$policyPublishingParent.Keys | % { $policyToRemove = $_; $policyPublishingParent.Item($policyToRemove) | % { 
Set-LabelPolicy -Identity $policyToRemove -RemoveLabels $_ } 
```

## Migrate to the modern label scheme

Migration is gradually rolling out, so migrating your parent labels to label groups might not yet be available for your tenant.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Information Protection** &gt; **Sensitivity labels**
2. On the **Sensitivity labels** page, if you see an information banner **Migrate to the modern label scheme**, label migration is available to your tenant. From this banner, select **Get started** to start the migration:

    ![Information banner on the Sensitivity labels page to migrate to the modern label scheme.](media/sensitivity-labels-migration-bar.png)
3. On the **Migrate to the modern label scheme** flyout pane, you see a summary of your sensitivity labels before and after the migration. For more details, select the **Review new scheme** button at the bottom of the pane. For example:

    ![Label migration flyout pane from the Sensitivity labels page to migrate to the modern label scheme.](media/label-migration-pane.png)
4. The **New label scheme** page shows you how your migrated labels will look in the Microsoft Purview portal, with a folder icon next to what used to be parent labels. This page will also alert you to any naming conflicts that need to be resolved before the migration. For example, the **General** parent label has a sublabel that's also named **General**. All sublabels must have a unique name from their parent label.

    You can use the **Download** button to save a copy to a CSV file. The default name is NewLabelSchemecsv.csv.

    Important

    Even if you don't have alerts to resolve, use this opportunity to carefully review the labels and consider making changes to them before you migrate so you can remove or minimize the applicable parent labels that will create a new sublabel if they're not needed. After making changes, restart the migration and check the post-migration information again from this page.

    For example, you might have parent labels that you've never used as standalone labels, but are configured for encryption or content markings. Label actions are one of the reasons why migration creates a new sublabel that you might not need.
5. When you're ready to migrate your labels, select the **Migrate** button.

    Note

    If you have applicable parent labels that will create new sublabels and you decided to use a script to automatically unpublish them, run Script One before you select **Migrate**.

    The migration process doesn't take long, typically just a few minutes to an hour. However, as a precaution, allow up to 24 hours. While the migration is in progress, we don't recommend making any changes to the label configuration because those changes will likely be lost.

    When the migration is complete, the browser refreshes, and the new label scheme is displayed with a message to confirm that the migration is complete.

    Note

    If you have applicable parent labels that will create new sublabels and you decided to use a script to automatically unpublish them, now run Script Two.