---
layout: Conceptual
title: Manage hold policies for eDiscovery cases | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-hold-manage
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Create and manage hold policies for eDiscovery cases by placing holds on mailboxes, OneDrive sites, Teams, and Microsoft 365 groups to preserve relevant content.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-23T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom:
- msecd-doc-authoring-1014
- msecd-doc-authoring-1015
locale: en-us
document_id: 5807e82a-3d6c-15b9-ac25-b11f7aa85498
document_version_independent_id: 5807e82a-3d6c-15b9-ac25-b11f7aa85498
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-hold-manage.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-hold-manage
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-hold-manage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 57db1312-8145-6f18-b38d-36f24b4209dd
---

# Manage hold policies for eDiscovery cases | Microsoft Learn

Note

Active hold policies that you create in cases in the legacy eDiscovery experience are automatically migrated and available in the new Microsoft Purview eDiscovery experience. Review the [eDiscovery hold policy status report](edisc-hold-report) to check policy status and retry any policies that need attention.

Use eDiscovery to create hold policies that preserve content relevant to your cases. When you place content locations on hold, the content is held until you release the hold in the case, remove a specific data location, or delete the hold policy. You can place holds on data sources such as:

- User mailboxes and OneDrive sites.
- Microsoft Teams mailboxes and SharePoint and OneDrive sites.
- Microsoft 365 group mailboxes and SharePoint and OneDrive sites.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Hold policy dashboard

The **Hold policies** dashboard lists all the holds associated with a case. This dashboard lets you create hold policies, displays information about hold policies in the case, and lets you filter and group the hold policies. The **Hold policies** dashboard contains the following information and controls:

- **Name**: The name of the hold policy.
- **Created by**: The user that created the hold policy.
- **Last modified**: The date and time the hold policy was last modified. Select **Time zone** to switch between using local time and Coordinated Universal Time (UTC).
- **Hold policy Status**: The current status of the hold policy.

Select a hold policy to view the details, data sources, and condition and KeyQL filters.

To customize the columns display on the **Hold policies** dashboard, select **Customize columns** to choose the columns to display or drag and drop the columns in the list to reorder. To search for a specific hold policy, enter a keyword in the **Search** field. To download the list of hold policies and the column information, select **Download list** to create a .csv file containing this information.

## Hold policy states

The hold policy page shows the state of a hold next to the hold name. Hold policies have the following states:

- **Draft**: Displayed when you create a new policy but don't apply it. If you navigate away from the policy draft, you cancel the draft and lose all policy changes.
- **On**: The policy is applied and all locations in the policy are on hold. Select the **Details** tab to view location information.
- **Off**: The policy is off for a previously applied hold. All included locations aren't on hold.
- **In progress**: The hold policy is in the process of being applied or updated.
- **Pending deletion**: The hold policy is in the process of being deleted.

## Check for holds on a mailbox or site

Before you delete content, release a hold, or diagnose why a purge, site deletion, or storage cleanup isn't working as expected, identify every hold source that applies to the location. eDiscovery hold policies are only one of several hold sources. Microsoft Purview retention policies, retention labels, Litigation Hold, delay holds, and Single Item Recovery can independently preserve content, and any one of them is enough to keep items in the Recoverable Items folder or in the Preservation Hold Library.

### Symptoms that warrant a hold check

| Symptom | Most likely hold source |
| --- | --- |
| `New-ComplianceSearchAction -Purge -PurgeType HardDelete` succeeds but items remain in `\Recoverable Items\Purges` | Any hold or retention policy on the mailbox; delay hold; Single Item Recovery |
| You can't delete a SharePoint site or OneDrive site | eDiscovery hold; tenant-wide, site-, or group-scoped retention policy; delay hold |
| You can't delete a folder or document library | Site-scoped retention policy; Preservation Hold Library content |
| The Preservation Hold Library is consuming OneDrive storage and items aren't expiring | Retention policy or eDiscovery hold still applied to the OneDrive site |
| Mailbox shows as on hold even after you remove all known holds | Delay hold (`DelayHoldApplied` or `DelayReleaseHoldApplied`); retention label hold (`ComplianceTagHoldApplied`) |
| You can't permanently delete an inactive mailbox | A hold or retention policy is keeping the mailbox alive |

### Check for holds on a mailbox

Run the following cmdlets in [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell), in order. If any cmdlet returns a hold source, clear it before you attempt to delete content or remove the user from the location.

| # | Cmdlet | What it surfaces |
| --- | --- | --- |
| 1 | `Invoke-HoldRemovalAssistant -Identity <user>` | All applicable hold sources in a single call. Recommended first step. |
| 2 | `Get-OrganizationConfig \| FL InPlaceHolds` | Tenant-wide and organization-scoped retention policies. Entries with the `mbx`, `skp`, or `grp` prefix are mailbox-, Teams-, or group-scoped policies that surface at the organization level. |
| 3 | `Get-Mailbox <user> \| FL LitigationHoldEnabled,InPlaceHolds,ComplianceTagHoldApplied,SingleItemRecoveryEnabled` | Mailbox-scoped holds, retention label hold, and Single Item Recovery. |
| 4 | `Get-Mailbox <user> \| FL DelayHoldApplied,DelayReleaseHoldApplied` | Delay holds. A delay hold is automatically applied after a hold is removed and preserves items for up to 30 days. |

Use the following table to identify the hold source for each `InPlaceHolds` prefix that you see, and where to clear it.

| Prefix | Hold source | Where to clear it |
| --- | --- | --- |
| `mbx` | Microsoft Purview retention policy (mailbox-scoped) | Microsoft Purview portal: **Data lifecycle management** &gt; **Retention policies** &gt; exclude the mailbox |
| `skp` | Teams retention policy | Microsoft Purview portal: **Data lifecycle management** &gt; **Retention policies** (Teams) |
| `grp` | Microsoft 365 group retention policy | Microsoft Purview portal: **Data lifecycle management** &gt; **Retention policies** |
| `UniH` | eDiscovery case hold | Microsoft Purview portal: **eDiscovery** &gt; open the case &gt; **Hold policies** |
| `cld` | Cloud attachment hold | Microsoft Purview portal: **eDiscovery** &gt; open the case &gt; **Hold policies** |

For more detail on each hold type and how to identify the associated retention policy or case, see [Identify Exchange mailbox hold types in eDiscovery](edisc-hold-types-mailboxes).

### Check for holds on a SharePoint or OneDrive site

Run the following cmdlets, in order. If any cmdlet returns a hold source, clear it before you attempt to delete the site, the library, or content that's preserved in the Preservation Hold Library.

| # | Cmdlet | What it surfaces |
| --- | --- | --- |
| 1 | `Invoke-HoldRemovalAssistant -Identity <siteUrl-or-userUPN>` | All applicable hold sources in a single call. Recommended first step. |
| 2 | `Get-OrganizationConfig \| FL InPlaceHolds` | Tenant-wide retention policies. Entries with the `grp` prefix are group- or site-scoped policies. |
| 3 | `Get-RetentionCompliancePolicy \| Where-Object { $_.SharePointLocation -or $_.OneDriveLocation }` | Retention policies that target SharePoint sites or OneDrive accounts. |
| 4 | Delay hold on the site | Surfaced in the `Invoke-HoldRemovalAssistant` output. |

If the Preservation Hold Library (PHL) on a OneDrive site is consuming storage and items aren't draining, the most common cause is a retention policy or eDiscovery hold that still applies to the site. After you clear every hold source, the Managed Folder Assistant removes expired items from the PHL over time.

### Common misconceptions

- **"Setting MRM to True deletes items from the Purges folder."** The Managed Folder Assistant (MRM/MFA) enforces retention. It isn't a delete mechanism. The supported way to permanently delete items from the Recoverable Items folder is the HardDelete purge described in [Delete items in the Recoverable Items folder for mailboxes on hold in eDiscovery](edisc-hold-delete-recoverable-items), and that purge respects every hold source listed earlier in this section.
- **"I removed the Litigation Hold so I can delete the items now."** Wait up to 240 minutes for the change to apply, then check for a delay hold (`DelayHoldApplied` or `DelayReleaseHoldApplied`) before you attempt to delete content. A delay hold is automatically applied after a hold is removed.
- **"`LitigationHoldEnabled` is False, so the mailbox isn't on hold."** This check alone is insufficient. Also check `InPlaceHolds`, `ComplianceTagHoldApplied`, `DelayHoldApplied`, `DelayReleaseHoldApplied`, and `Get-OrganizationConfig | FL InPlaceHolds`.
- **"`Get-OrganizationConfig` returned an `mbx` entry, so the policy applies to the whole organization."** An `mbx`-prefixed entry that surfaces under `Get-OrganizationConfig` is a mailbox-scoped Microsoft Purview retention policy. To clear it, exclude the specific mailbox from the policy in the Microsoft Purview portal. It might take up to 24 hours for the exclusion to replicate.

## Create a hold policy

To create a new hold policy, see [Create holds in eDiscovery](edisc-hold-create).

## Edit a hold policy

You can edit the hold policy name, description, or the policy details (data sources, condition filters, and KeyQL filters) as applicable.

To edit the hold policy name or description, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, then select **Cases** in the left navigation.
3. Select a case, then select the **Hold policies** tab.
4. On the **Hold policies** dashboard, select the hold policy you want to edit.
5. Select the edit (pencil) icon next to the policy name.
6. Update the policy name or description, then select **Continue**.

To edit hold policy details, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, then select **Cases** in the left navigation.
3. Select a case, then select the **Hold policies** tab.
4. On the **Hold policies** dashboard, select the hold policy you want to edit.
5. On the **Hold policy** page for the selected policy, select the **Hold policy** tab.
6. Update data sources, condition filters, and KeyQL filters as applicable.
7. Select **Apply hold**.

Important

eDiscovery doesn't continuously monitor workload or location-level changes after a hold operation completes. If mailbox or site identities change (for example, UPN, SharePoint URL, or OneDrive URL changes), or if a hold is changed outside this policy workflow, update the hold policy data sources and then select **Apply hold** to restamp the policy.

## Retry a hold policy

A retry hold policy triggers the hold process to restamp all mailboxes and sites in the policy to enforce the hold. You might also encounter errors while placing a hold on data sources. For a list of possible errors, see Manage hold status errors.

Use **Retry policy** after location identity changes or external hold operations so that eDiscovery refreshes the policy state and per-location status.

To retry a hold policy, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, then select **Cases** in the left navigation.
3. Select a case, then select the **Hold policies** tab.
4. On the **Hold policies** dashboard, select the hold policy you want to retry.
5. On the **Hold policy** page for the selected policy, select **Policy actions** &gt; **Retry policy**.

## Turn off a hold policy

Turning off a hold policy might result in the permanent deletion of any content currently being preserved. It doesn't affect content preserved by other hold policies.

To turn off a hold policy, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, then select **Cases** in the left navigation.
3. Select a case, then select the **Hold policies** tab.
4. On the **Hold policies** dashboard, select the hold policy you want to turn off.
5. On the **Hold policy** page for the selected policy, select **Policy actions** &gt; **Turn off**.

## Turn on a hold policy

When you edit a policy, it doesn't affect content preserved by other hold policies.

To turn on a hold policy, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, then select **Cases** in the left navigation.
3. Select a case, then select the **Hold policies** tab.
4. On the **Hold policies** dashboard, select the hold policy you want to turn on.
5. On the **Hold policy** page for the selected policy, select **Policy actions** &gt; **Turn on**.

## Delete a hold policy

When you delete a hold policy, you remove all associated holds and release all sites and mailboxes. This action might result in permanent deletion of any content currently being preserved.

To delete a hold policy, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, then select **Cases** in the left navigation.
3. Select a case, then select the **Hold policies** tab.
4. On the **Hold policies** dashboard, select the hold policy you want to delete.
5. On the **Hold policy** page for the selected policy, select **Policy actions** &gt; **Delete policy**.
6. On the **Delete policy?** dialog, select **Yes, delete**.

## Manage hold status errors

You might encounter errors while placing a hold on data sources. The following table lists the errors that you might encounter and the recommended resolution.

| Hold error types | Description | Resolution |
| --- | --- | --- |
| Distribution group has too many members | The distribution group associated with the requested hold has more than 1,000 email addresses. Currently, a distribution group with more than 1,000 email addresses can't be expanded and placed on hold. | Add the individual email addresses as data sources or split the distribution group into groups with fewer than 1,000 email addresses. Then select **Policy actions** &gt; **Retry policy** in the hold policy to retry the hold application. |
| Invalid email address or URL | The location associated with the requested hold has an invalid email address or site URL. | Specify a valid email address or URL that exists within your organization. |
| Hold changed outside eDiscovery | The hold state for a location was changed outside this case policy workflow (for example, using `Invoke-HoldRemovalAction` in Security & Compliance PowerShell). | In eDiscovery, edit the hold policy so the intended locations are correct, then select **Apply hold** or **Policy actions** &gt; **Retry policy** to restamp and refresh status. |
| Mailbox not found | The mailbox associated with the requested hold isn't a valid mailbox. | Verify the email address and check that it's a valid Exchange Online mailbox. After you confirm the mailbox, edit the data source for the mailbox and then select **Policy actions** &gt; **Retry policy** in the hold policy to retry the hold application. |
| Policy deployment interrupted | A system error indicating a problem was encountered while applying the hold. | Select **Policy actions** &gt; **Retry policy** in the hold policy to retry the hold application. |
| Site inaccessible | The SharePoint location associated with the requested hold request isn't accessible and might be read only. | Contact your SharePoint site administrator to configure the site as writable. Then select **Policy actions** &gt; **Retry policy** in the hold policy to retry the hold application. |
| Site failed to apply hold | If the site URL changed for any reason (due to user UPN or tenant domain change), you must update the policy to include the site with the new name and URL. | Update the policy by removing the original site, then add the new site URL to the hold policy and reapply the hold. |
| Site not found | The SharePoint location associated with the requested hold might have been moved, deleted, or the site URL might not exist. | Check the site URL and confirm if the SharePoint site exists. After you confirm the site exists, edit the data source for the site and then select **Policy actions** &gt; **Retry policy** in the hold policy to retry the hold application. |

Hold policies have a *Site not found* error if the policy includes a location that had a UPN change due to change in status, departure policies, name change, or other circumstances. This error occurs when the hold is reapplied after these changes. The hold for site or mailbox can remain stamped on the original location identity, but the policy must be updated to include the new UPN or site URL for the policy to reflect the correct status and to support removal of holds.

After you add the new UPN or site URL to the policy, you can remove the prior SMTP UPN or site URL from the policy.

Important

To apply a hold to a SharePoint site, the site must have a title.

## Place a hold on Microsoft Teams and Microsoft 365 groups

Microsoft Teams is built on Microsoft 365 groups. Therefore, placing them on hold in eDiscovery is similar. Keep the following things in mind when placing Microsoft 365 groups and Microsoft Teams on hold:

- To place content located in Microsoft 365 groups and Microsoft Teams on hold, you need to specify the mailbox and SharePoint site that are associated with a group or team.
- Run the **Get-UnifiedGroup** cmdlet in Exchange Online to view properties for a Microsoft 365 group or Microsoft Team. This cmdlet is a good way to get the URL for the site that's associated with a Microsoft 365 group or a Microsoft Team. For example, the following command displays selected properties for a Microsoft 365 group named Senior Leadership Team:

    ```console
    Get-UnifiedGroup "Senior Leadership Team" | FL DisplayName,Alias,PrimarySmtpAddress,SharePointSiteUrl
    DisplayName            : Senior Leadership Team
    Alias                  : seniorleadershipteam
    PrimarySmtpAddress     : seniorleadershipteam@contoso.onmicrosoft.com
    SharePointSiteUrl      : https://contoso.sharepoint.com/sites/seniorleadershipteam
    ```

    Note

    To run the Get-UnifiedGroup cmdlet, you need to be assigned the View-Only Recipients role in Exchange Online or be a member of a role group that's assigned the View-Only Recipients role.
- When you search a user's mailbox, the search doesn't include any Microsoft 365 group or Microsoft Team that the user is a member of. Similarly, when you place a Microsoft 365 group or Microsoft Team hold, only the group mailbox and group site are placed on hold; the mailboxes and OneDrive sites of group members aren't placed on hold unless you explicitly add them to a case or place their data sources hold. Therefore, if you need to place a Microsoft 365 group or Microsoft Team on hold for a specific user, consider mapping the group site and group mailbox to the user. If the Microsoft 365 group or Microsoft Team isn't attributable to a single user, consider adding the source to a hold.
- To get a list of the members of a Microsoft 365 group or Microsoft Team, you can view the properties on the **Home** &gt; [**Groups page in the Microsoft 365 admin center**](https://go.microsoft.com/fwlink/p/?linkid=2052855). Alternatively, you can run the following command in Exchange Online PowerShell:

    ```powershell
    Get-UnifiedGroupLinks <group or team name> -LinkType Members | FL DisplayName,PrimarySmtpAddress
    ```

    Note

    To run the **Get-UnifiedGroupLinks** cmdlet, you need to be assigned the View-Only Recipients role in Exchange Online or be a member of a role group that's assigned the View-Only Recipients role.
- Channel conversations that are part of a Microsoft Teams channel are stored in the mailbox that's associated with the Team. Similarly, files that team members share in a channel are stored on the team's SharePoint site. Therefore, you need to place the Microsoft Team mailbox and SharePoint site on hold to retain conversations and files in a channel.
- Alternatively, conversations that are part of the Chat list in Microsoft Teams are stored in the mailbox of the users who participate in the chat. Files that a user shares in Chat conversations are stored in the OneDrive site of the user who shares the file. Therefore, you need to place the individual user mailboxes and OneDrive sites on hold to retain conversations and files in the Chat list.
- Every Microsoft Team or team channel contains a Wiki for note-taking and collaboration. The Wiki content is automatically saved to a file with a .mht format. This file is stored in the Teams Wiki Data document library on the team's SharePoint site. You can place the content in the Wiki on hold by placing the team's SharePoint site on hold.

    Note

    The capability to retain Wiki content for a Microsoft Team or team channel (when you place the team's SharePoint site on hold) was released on June 22, 2017. If a team site is on hold, the Wiki content is retained starting on that date. However, if a team site is on hold and the Wiki content was deleted before June 22, 2017, the Wiki content wasn't retained.