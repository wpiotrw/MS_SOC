---
layout: Conceptual
title: Learn about inactive mailboxes | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/inactive-mailboxes-in-office-365
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-08-05T00:00:00.0000000Z
audience: Admin
ms.topic: overview
ms.service: purview
ms.subservice: purview-mailboxes
ms.collection:
- purview-compliance
- m365copilot
search.appverid:
- MOE150
- MET150
ms.assetid: 1fbd74e8-7a60-4157-afe8-fe79f05d2038
ms.custom:
- seo-marvel-apr2020
description: Learn how to retain mailbox content for former employees by turning the mailbox into an inactive mailbox.
locale: en-us
document_id: 7964f5c8-e34c-15ac-947f-45ae150e7788
document_version_independent_id: 7964f5c8-e34c-15ac-947f-45ae150e7788
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/inactive-mailboxes-in-office-365.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: inactive-mailboxes-in-office-365
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/inactive-mailboxes-in-office-365.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: a388ae08-a316-99f0-655e-ec0b7bae7138
---

# Learn about inactive mailboxes | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Your organization might need to retain former employees' email after they leave the organization. Depending on your organization's retention requirements, you might need to retain mailbox content for a few months or years after employment ends, or you might need to retain mailbox content indefinitely. Regardless of how long you need to retain email, you can create inactive mailboxes to retain the mailbox of former employees.

## What are inactive mailboxes?

An inactive mailbox is a type of soft-deleted mailbox used to retain a former employee's email after they leave your organization.

When an employee leaves your organization (or goes on an extended leave of absence), you can remove their Microsoft 365 account. The employee's mailbox data is retained for 30 days after the account is removed. During this period, you can still recover the mailbox data by undeleting the account. After 30 days, the data is permanently removed.

But if a hold is applied to the mailbox prior to deleting the Microsoft 365 account, the mailbox will be converted into an inactive mailbox. The following sections contain information about holds that can be applied with Microsoft 365 retention and eDiscovery holds.

Inactive mailboxes are useful when your organization needs to retain mailbox content of former employees for regulatory or other reasons. While any type of hold listed in this document will force a mailbox to be made inactive when a user object is deleted, we recommend doing this by applying a Microsoft 365 retention policy or retention labels, confirm the hold is applied, and then remove the corresponding Microsoft 365 account. At that point, the contents of the inactive mailbox are retained for the duration of the retention period specified before the user account was deleted. You can still recover the corresponding user account for a 30-day period, however after 30 days, the mailbox is retained in Microsoft 365 as an inactive mailbox until the retention policy or retention labels are removed.

Important

As we mentioned previously, we recommend you use Microsoft 365 retention to create an inactive mailbox:

- In-Place Holds in the Exchange admin center are now retired. As of July 1, 2020, new In-Place Holds were unable to be created in Exchange Online. As of October 1, 2020, the hold duration of in-place holds could no longer be changed. Any inactive mailbox that has an In-Place Hold applied can only be deleted by removing the In-Place Hold. Existing inactive mailboxes that are on In-Place Hold will continue to be preserved until the hold is removed. For more information about In-Place Holds retirement, see [Retirement of legacy eDiscovery tools](ediscovery-legacy-retirement).
- [Litigation hold](/en-us/exchange/policy-and-compliance/holds/litigation-holds) remains supported as an alternative method to retain content in a mailbox and make it inactive after a user account is deleted. However, as an older technology, we recommend you use Microsoft 365 retention instead.

When there are multiple holds on the same content, the [principle of retention apply](retention#the-principles-of-retention-or-what-takes-precedence) and the content is retained for the longest period.

### Confirming a hold is applied to a mailbox

Whether you apply a Microsoft 365 retention policy, retention labels, eDiscovery hold, Litigation hold, or have an existing In-Place Hold, you can confirm the hold is successfully applied to the mailbox by using PowerShell. If you've recently configured the hold, you might need to wait until it's applied to the mailbox.

To prevent accidental or unintentional deletion, we recommend you confirm the hold before you delete the user account. If the hold isn't applied, the mailbox won't be converted into an inactive mailbox.

For instructions, see [How to identify the type of hold placed on an Exchange Online mailbox](ediscovery-identify-a-hold-on-an-exchange-online-mailbox).

A hold can also be applied automatically: after you remove a hold from a mailbox, Microsoft 365 applies a *delay hold* so that content isn't purged immediately. A mailbox with a delay hold is still treated as being on hold, so it stays an inactive mailbox until the delay hold is removed or expires. For more information, see [Managing mailboxes on delay hold](ediscovery-identify-a-hold-on-an-exchange-online-mailbox#managing-mailboxes-on-delay-hold) and [Remove a delay hold from an inactive mailbox](delete-an-inactive-mailbox#remove-a-delay-hold-from-an-inactive-mailbox).

## Inactive mailboxes and Microsoft 365 retention

If a Microsoft 365 retention policy is applied to a mailbox, or one or more email items in a mailbox have a retention label applied, and then the Microsoft 365 user account is deleted, the mailbox will be converted into an inactive mailbox. For the inactive mailbox to be created:

- The retention settings must be configured to [retain content, or retain and then delete content](retention-settings#settings-for-retaining-and-deleting-content). If the retention action is configured to only delete content, the mailbox won't become inactive when the user account is deleted. For inactive mailboxes, we recommend using the retain and then delete option.
- The retention settings must be applied to a [retention location](retention-settings#locations) that is associated with an Exchange mailbox:

    - Exchange email
    - Microsoft 365 Groups
    - Skype for Business
    - Exchange public folders
    - Teams channel messages
    - Teams chats and Copilot interactions
    - Teams private channel messages
    - Viva Engage community messages
    - Viva Engage user messages

For more information about Microsoft retention, see [Learn about retention policies and retention labels](retention).

If Microsoft 365 retention is used to create an inactive mailbox, the retention settings from the retention policy or retention labels continue to apply to the inactive mailbox. This means if the retention settings are configured to retain and then delete content, items will be moved to the Recoverable Items folder when the retention duration expires, and then eventually purged from the inactive mailbox. If the retention settings aren't configured to delete items, then items that haven't been permanently deleted by the user (before the mailbox was made inactive) will not be moved to the Recoverable Items folder and will be retained indefinitely after the mailbox becomes inactive.

Tip

You can use the *ComplianceTagHoldApplied* property to identify whether a mailbox has items that have one or more retention labels applied to retain, or retain and then delete content. For more information, see [Identifying mailboxes on hold because a retention label has been applied to a folder or item](ediscovery-identify-a-hold-on-an-exchange-online-mailbox#identifying-mailboxes-on-hold-because-a-retention-label-has-been-applied-to-a-folder-or-item).

### Using adaptive policy scopes to manage retention of inactive mailboxes

With [adaptive policy scopes](purview-adaptive-scopes#advantages-of-using-adaptive-scopes), you can apply retention settings specifically to inactive mailboxes. Benefits of this configuration include:

- You can meet your organization's regulations or policies that require different retention periods for active employees and former employees.
- You can configure the retention settings to retain mailbox content for only as long as necessary to meet your organization's requirement for former employees.
- You can quickly identify the policy for retention that's assigned to inactive mailboxes in your organization, which makes it easier to change the retention settings if necessary.
- It's easier to permanently delete an inactive mailbox because you can remove it from the policy by [configuring the adaptive scope](purview-adaptive-scopes#configure-adaptive-scopes) to exclude it, based on attributes or properties of the inactive mailbox. Otherwise, you must use [Exchange Online PowerShell](delete-an-inactive-mailbox#remove-an-inactive-mailbox-from-a-retention-policy) before [deleting the mailbox](delete-an-inactive-mailbox#before-you-delete-an-inactive-mailbox).

Note

Depending on the configuration of your adaptive policy scope, inactive mailboxes might or might not be included. To specifically target or to exclude inactive mailboxes from an adaptive policy scope, see [configuration information for Exchange email and Exchange public folders](retention-settings#locations).

### Using static policy scopes and inactive mailboxes

If you don't use [adaptive policy scopes and instead use a static scope](retention#adaptive-or-static-policy-scopes-for-retention) with Microsoft 365 retention, consider the following:

- Static policy scopes include inactive mailboxes when you use the default **All mailboxes** configuration but aren't supported for [specific inclusions or exclusions](retention-settings#a-policy-with-specific-inclusions-or-exclusions). However, if you include or exclude a recipient that has an active mailbox at the time the policy is applied and the mailbox later goes inactive, the retention settings continue to be applied or excluded. In this scenario, [specific inclusion and exclusion limits](retention-limits) still apply.

    Note

    This also means that any new Microsoft 365 retention settings using a static scope that is applied to the default selection of **All mailboxes** will automatically include all existing inactive mailboxes.
- If you change the default selection of **All mailboxes** to include specific recipients, retention settings for the policy will no longer apply to any inactive mailboxes, which now become eligible for automatic deletion.
- If you want to release a retention policy that's applied to an inactive mailbox, see [Releasing a policy for retention](retention#releasing-a-policy-for-retention).

Caution

When you use Microsoft 365 retention to make a mailbox inactive, do not change or remove the user principal name (UPN) for the mailbox before you delete the corresponding user account. Additionally, do not change the primary SMTP address (that's derived from the UPN) or remove this email address from the list of secondary SMTP addresses associated with the mailbox before making the mailbox inactive.

If you change the UPN or email addresses (that were assigned to the mailbox at the time the retention settings were applied) and then delete the user account to make the mailbox inactive, you won't be able to delete the inactive mailbox if you no longer need to retain it. That's because you can't remove the inactive mailbox from the policy by using a UPN or email address (to identify the inactive mailbox) that's different from the ones that existed when the retention settings were initially applied to the mailbox. For more information about deleting inactive mailboxes, see [Delete an inactive mailbox in Office 365](delete-an-inactive-mailbox).

## Inactive mailboxes and eDiscovery case holds

If a hold that's associated with an [eDiscovery case](edisc-cases-manage) is placed on a mailbox and then the mailbox or the user's account is deleted, the mailbox becomes an inactive mailbox. However, don't use eDiscovery case holds to make a mailbox inactive. That's because eDiscovery cases are intended for specific, time-bound cases related to a legal issue. At some point, a legal case probably ends, the holds associated with the case are removed, and the eDiscovery case is closed. In fact, if a hold that's placed on an inactive mailbox is associated with an eDiscovery case, and then the hold is released or the eDiscovery case is closed (or deleted), the inactive mailbox is permanently deleted. Also, you can't create a time-based eDiscovery hold. This condition means that content in an inactive mailbox is retained forever or until the hold is removed and the inactive mailbox is deleted. Therefore, use Microsoft 365 retention for inactive mailboxes.

Important

When a mailbox with an [active eDiscovery hold](edisc-hold-manage) is deleted, the mailbox content is preserved as an inactive mailbox. The content remains searchable and exportable in eDiscovery for as long as the hold or associated case remains active.

For more information about the differences between eDiscovery holds and Microsoft 365 retention, see [When to use retention policies and retention labels or eDiscovery holds](retention#when-to-use-retention-policies-and-retention-labels-or-ediscovery-holds).

## Inactive mailboxes and auto-expanding archives

An inactive mailbox that's configured with an auto-expanding archive can't be recovered or restored. If, for compliance reasons, you need to recover data from an inactive mailbox with an auto-expanding archive, use content search to export the data from the mailbox. This action is supported for eDiscovery purposes only, and can't be used as a backup solution. For instructions to use search for the recovery of data for eDiscovery, see [Create a search for a case in eDiscovery](edisc-search-query)

## Inactive mailboxes and Exchange MRM retention policies

Applying an Exchange retention policy (the messaging records management, or MRM, feature in Exchange Online) does not create an inactive mailbox when the user account is deleted.

However, if this MRM retention policy was applied to a mailbox before it went inactive, any deletion policies (MRM retention tags configured with a **Delete** action) will continue to be processed on the inactive mailbox. That means items that are tagged with an MRM deletion policy will be moved to the [Recoverable Items folder](/en-us/exchange/security-and-compliance/recoverable-items-folder/recoverable-items-folder) when the retention period expires. Those items are purged from the inactive mailbox when the hold duration expires. If a hold duration isn't specified for the inactive mailbox, items in the Recover Items folder will be retained indefinitely.

Conversely, any archive policies (MRM retention tags configured with a **MoveToArchive** action) that are included in the MRM retention policy assigned to an inactive mailbox are ignored. That means items in an inactive mailbox that are tagged with an archive policy remain in the primary mailbox when the retention period expires. They're not moved to the archive mailbox or to the Recoverable Items folder in the archive mailbox. They will be retained indefinitely.