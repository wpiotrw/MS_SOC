---
layout: Conceptual
title: Microsoft Purview account merge best practices | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-best-practices-account-merge
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2024-09-12T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Find best practices for Microsoft Purview account merge.
locale: en-us
document_id: 5e543f62-7451-2346-12e7-55c2dfd23840
document_version_independent_id: 5e543f62-7451-2346-12e7-55c2dfd23840
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-best-practices-account-merge.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-best-practices-account-merge
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-best-practices-account-merge.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 8e19a2d2-df5b-d26b-1e53-f871bfefaa02
---

# Microsoft Purview account merge best practices | Microsoft Learn

## Background

Microsoft Purview represents the next step towards unifying your organization's governance, policy, compliance, risk, and security. If you started using Microsoft Purview data governance with the classic experience, upgrading to the new experience is necessary to obtain the full set of capabilities and enhancements. For organizations with multiple accounts, this upgrade process involves merging existing accounts.

Merging Microsoft Purview accounts involves consolidating resources, configurations, and data governance policies from multiple accounts into a single, unified account. This process requires careful planning and consideration to ensure data integrity, security, and compliance.

It's recommended to follow this guide if you have more than one Microsoft Purview account under the classic experience.

## Pre-merge assessment

- Conduct a thorough assessment to obtain the total number of Microsoft Purview accounts in your tenant, and the purpose of each account to identify which account to promote as primary. This account will be converted into your default domain in the new experience.
- Evaluate the remaining accounts to detect and resolve potential conflicts, such as duplicate resources or incompatible configurations.
- Currently, you can only have up to five domains (one default domain and four custom domains) inside the new experience. If your organization has more than five accounts in the classic mode, you need to select only five accounts to upgrade and retire the remaining accounts. For example, if your organization has multiple nonproduction accounts, you can consider merging one account into a custom domain and retire remaining accounts without using the merge tool. This process may include a combination of using the merge tool and manually migrating resources from other classic accounts under a nonprod account.
- Review Microsoft Purview limitations to reduce the risk of failure during the merge and ensure the unified experience has the capacity to merge resources.
- Evaluate resources in each account to determine what needs to be merged or can be excluded during the migration.
- Run the merge tool in assess mode to identify and resolve any issues before the merge, considering that the merge is a one-time irreversible process.

## Conflict resolution

- Develop a strategy for resolving conflicts, such as renaming resources or excluding certain types from the merge. Handle name conflicts and consider the option to exclude certain object types.

### What to do if conflicts happen

Use the following guidelines if conflicts are raised during the Microsoft Purview account merge process:

1. Identify Conflicts: During the premerge assessment, run the merge tool in assess mode to identify potential conflicts. This generates a list of conflicts that need to be resolved before proceeding with the merge. Conflicts may raise due any of these issues:

    - Conflicts may arise due to duplicate resources, such as assets, or glossary terms. For example, if two accounts have the same custom type definition name, you need to choose one and delete the other.
    - Conflicts could also occur due to incompatible configurations between accounts. This could include differences in data source configurations. For example, Advanced Resource Set feature may be turned on in the merging account but it's off in the primary account.
2. Resolve Conflicts:

    - If there are duplicate resources, consider renaming them to avoid conflicts. For example, you can rename conflicting assets or glossary term to ensure they have unique names across accounts.
        - You may choose to exclude certain types of resources from the merge if they're not essential or if they cause conflicts. This can help streamline the merge process and reduce the risk of errors.
        - For conflicts that can't be resolved automatically, manually delete the conflicting resources before proceeding with the merge. This ensures that only the necessary and nonconflicting resources are merged.
3. Re-Run Assessments:

    - After resolving conflicts, rerun the merge tool in assess mode to ensure that all issues are addressed. This step helps validate that the merge can proceed without further conflicts.
4. Execute the Merge:

    - Run merge tool in assess mode until all conflicts are resolved.
    - Once all conflicts are resolved, proceed with the merge by following the step-by-step process outlined in the execution phase. This includes running assessments, performing prechecks, and executing the merge.

## Perform the merge

- Consider the merge as a one-time process and irreversible.
- Make sure no major changes are happening in data map in the secondary account during the merge process.
- Follow a step-by-step process for the merge, starting with a precheck, running assessments, and then executing the merge.

## Post-merge review

- After merge completion, conduct a review to ensure all resources are correctly integrated and that there are no outstanding issues.
- Manually migrate resources that weren't moved.
- Remove classic accounts that are merged.
- Review domains and collections roles to ensure proper role assignments are in place. Remove unnecessary roles that were added due to the merge process or assign the roles to lower-level collections when possible.