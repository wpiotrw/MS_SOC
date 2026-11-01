---
layout: Conceptual
title: Microsoft Purview Role Assignment Migrator | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/purview-role-assignment-migrator
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about synchronization of role assignments from Microsoft Purview to Microsoft Entra managed by the Microsoft Purview Role Assignment Migrator.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-10-23T00:00:00.0000000Z
ms.service: purview
ms.subservice: purview-permissions
audience: Admin
ms.topic: concept-article
ms.collection:
- purview-compliance
- essentials-manage
ms.custom:
- admindeeplinkCOMPLIANCE
ai-usage: ai-assisted
locale: en-us
document_id: 9e2ed92c-5f38-647c-5723-5ac3455b26e9
document_version_independent_id: 9e2ed92c-5f38-647c-5723-5ac3455b26e9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/purview-role-assignment-migrator.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purview-role-assignment-migrator
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/purview-role-assignment-migrator.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/439169bb-ca98-4939-bfdf-143f64c492d8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/27ece40b-27ae-490b-850a-e99fc3e2c052
platformId: bb23842e-9406-b13d-3246-327f090d30f3
---

# Microsoft Purview Role Assignment Migrator | Microsoft Learn

The **Microsoft Purview Role Assignment Migrator** is a Microsoft first-party enterprise application in Microsoft Entra ID that runs the background synchronization *from* Microsoft Purview role assignments *to* corresponding Entra roles. Microsoft 365 services use these Entra roles to verify that the administrator has the correct level of permissions before allowing long-running Microsoft Purview operations, such as content search and export, to proceed.

## Role mapping

The following table shows which Purview roles map to each of the following Entra roles. These Entra roles only grant the ability to run Purview operations. They don't expand existing Purview permissions or grant access to operations outside Purview.

| Purview roles | Mapped Entra role | Description |
| --- | --- | --- |
| Insider Risk Management Analysis  Insider Risk Management Investigation  Compliance Search  Export  Privacy Management Admin  Privacy Management Analysis  Privacy Management Investigation  Privacy Management Permanent Contribution  Privacy Management Temporary Contribution  Privacy Management Viewer  Data Security Investigation Reviewer | Purview Workload Content Reader | Allows Microsoft Purview operations to read content from Microsoft 365 services (for example, read a file in SharePoint). |
| Hold  Privacy Management Investigation  Data Security Investigation Investigator | Purview Workload Content Writer | Allows Microsoft Purview operations to read and write content to Microsoft 365 services (for example, store mail items in Exchange). |
| Search and Purge  Data Security Investigation Admin  Data Security Investigation Analyst | Purview Workload Content Administrator | Allows Microsoft Purview operations to read, write, and delete content in Microsoft 365 services (for example, purge messages in Microsoft Teams). |

If an administrator holds multiple Purview roles that map to different Entra roles, they receive the highest-privilege Entra role. The precedence order is: **Administrator &gt; Writer &gt; Reader**.

Note

The Purview Role Assignment Migrator manages the Purview Workload Content Reader, Purview Workload Content Writer, and Purview Workload Content Administrator Entra roles, and only the listed Purview roles synchronize to Entra. Don't assign the Entra roles in the Entra portal. These roles don't appear in the Microsoft Purview portal like the ones that are shown on the [settings](purview-permissions#microsoft-entra-roles-in-the-microsoft-purview-portal) page.

## Synchronization audit logs

The Purview Role Assignment Migrator works in two modes:

- **Initial bulk sync:** When the Purview Role Assignment Migrator first activates for your tenant, it syncs all existing Purview role assignments to Microsoft Entra in a single pass. This process generates a burst of activity in your Microsoft Entra audit logs.
- **Continuous sync:** All subsequent changes to Purview role memberships trigger synchronization to Microsoft Entra.

![Diagram of the Purview Role Assignment Migrator synchronizing Purview role assignments to Microsoft Entra roles.](media/purview-role-assignment-migrator.png)

Important

Keep the Purview Role Assignment Migrator enterprise application enabled in Microsoft Entra ID. The application ID is `7fe3d988-4f3b-4f33-83bd-1fb921a35ed2`. Disabling this app stops synchronization. New Purview role assignments don't propagate to Microsoft Entra, which can cause long-running Purview operations to fail authorization checks at runtime.

The Purview Role Assignment Migrator synchronization activity appears in Microsoft Entra audit logs with the display name **PurviewRoleAssignmentMigrator**. The **New Value** field for each log entry shows the Microsoft Entra role that was assigned.

You see two distinct patterns of activity:

| Activity pattern | When it occurs | Volume |
| --- | --- | --- |
| **Bulk sync** | Once, when the Purview Role Assignment Migrator first activates for your tenant | High — all existing Purview role assignments sync at once |
| **Continuous sync** | Ongoing, after each change to a Purview role membership | Low — proportional to the rate of Purview role changes in your tenant |

During the initial sync, administrators and affected users might also receive role-assignment emails, even if no Purview permissions have recently changed. Recipients depend on your [Microsoft Entra Privileged Identity Management (PIM) notification settings](/en-us/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings). Later role changes can also generate emails.

To verify an assignment or [an alert that a role was assigned outside of PIM](/en-us/entra/id-governance/privileged-identity-management/pim-how-to-configure-security-alerts), check the initiating application's ID, the mapped Entra role, and the corresponding Purview assignment. Don't rely on the display name alone or dismiss unexpected assignments.

Important

Don't assign users to these Microsoft Entra roles directly in Microsoft Entra ID. The Purview Role Assignment Migrator manages these assignments from Purview and can overwrite manual changes in Microsoft Entra during synchronization.

## Just-in-time access

The Purview Role Assignment Migrator follows your PIM policy for the corresponding Entra roles. When the policy requires an eligible or time-bound assignment, it applies that requirement. When the policy doesn't require eligibility or expiration, it creates **active assignments with no expiration**.

For just-in-time user access, we recommend assigning Purview permissions to [Microsoft Entra security groups](purview-permissions#add-users-or-groups-to-a-microsoft-purview-built-in-role-group) and using [PIM for Groups](/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups) to give users [eligible group membership](/en-us/entra/id-governance/privileged-identity-management/groups-assign-member-owner). The Purview Role Assignment Migrator synchronizes the group itself to the corresponding Entra role under that role's PIM policy; users activate time-bound membership to use the permissions provided through that group. Using PIM for Groups doesn't convert existing direct user assignments to eligible assignments.

Important

Size your just-in-time membership activation window on the security group to cover the full duration of your operations. If an activation expires while a long-running operation is still running, the operation might fail at its next runtime authorization check. For example, to identify how long your eDiscovery operations typically take, use [Process Manager in eDiscovery](edisc-process-managers) and set activation durations accordingly.

## Frequently asked questions

### Do these role assignments indicate an attack?

Synchronization by the Purview Role Assignment Migrator is expected Microsoft service activity. It doesn't, by itself, indicate compromise or a manual administrator role assignment. Before treating an event as expected, verify the following details:

| Detail | Expected value |
| --- | --- |
| Initiator | **PurviewRoleAssignmentMigrator** |
| Enterprise application ID | `7fe3d988-4f3b-4f33-83bd-1fb921a35ed2` |
| Assigned Entra role | **Purview Workload Content Reader**, **Purview Workload Content Writer**, or **Purview Workload Content Administrator** |

Also confirm that the Entra assignment matches the user's or group's existing Purview assignment. Don't rely on the display name alone. If any detail doesn't match, use your normal security investigation and incident response process.

### Does this grant new access?

No. The synchronized Entra role mirrors an existing Purview assignment and authorizes Purview operations only. It doesn't expand the user's or group's Purview permissions, grant other Microsoft Entra or Microsoft 365 administrative permissions, or provide independent access to Microsoft 365 content.

### Why did PIM generate an alert or an active assignment?

The Purview Role Assignment Migrator follows the PIM policy configured for the mapped Entra role, including requirements for eligible or time-bound assignments. If the policy doesn't require eligibility or expiration, the synchronized assignment is active with no expiration.

Administrators and affected users might receive PIM notifications about eligible, time-bound, or active assignments, including alerts that a role was assigned outside of PIM. After you verify the initiator, application ID, mapped role, and corresponding Purview assignment, these notifications are expected for the synchronized assignment.

### How can we use just-in-time access?

Assign Purview permissions to a security group and use PIM for Groups to provide eligible, time-bound user membership. The Purview Role Assignment Migrator synchronizes the group itself to the mapped Entra role. Users activate membership before starting an operation and must keep it active for the operation's full duration. For configuration links and activation guidance, see Just-in-time access.

Continue managing the underlying assignments in Purview, which remains the source of truth. Review and remove stale access, including assignments to disabled accounts. Using PIM for Groups doesn't remove existing direct user assignments.