---
layout: Conceptual
title: Use the hold report in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-hold-report
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use the hold report in eDiscovery to display information about the holds associated with all eDiscovery cases in your organization.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-02T00:00:00.0000000Z
audience: Admin
ms.topic: article
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
locale: en-us
document_id: 92890fee-b0db-0b21-4930-135cc1cb68c6
document_version_independent_id: 92890fee-b0db-0b21-4930-135cc1cb68c6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-hold-report.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-hold-report
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-hold-report.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 49c7f9ea-6e3c-7c10-6fec-ae3c866420c5
---

# Use the hold report in eDiscovery | Microsoft Learn

The hold report (preview) in eDiscovery lets users with *eDiscovery Administrator* or *eDiscovery Manager (preview)* permissions access a built-in report with information on all holds associated with eDiscovery cases in the Microsoft Purview portal. This report includes eDiscovery holds associated with eDiscovery cases. The hold report shows the data locations and reports on all hold policies within the tenant. It lists all locations that are part of those hold policies, whether enabled or disabled.

Important

The hold report is in public preview and provides a tenant-wide summary of hold policies for all eDiscovery cases. The report syncs policy and location status no more than once every seven days, so the information shown might not reflect recent changes to your hold policies. For the current status of a specific hold policy and its locations, go to the hold policy details page in the Microsoft Purview eDiscovery case. For more information, see [Manage holds in eDiscovery](edisc-hold-manage).

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Step 1: Verify your subscription and permissions

- Your organization must have an [organization subscription](edisc-get-started) that supports premium eDiscovery features to generate and access the hold report.
- Users accessing the hold report must be assigned the *eDiscovery Administrator* or *eDiscovery Manager (preview)* role. All eDiscovery Administrators and eDiscovery Managers in your organization can view the Hold Report. eDiscovery Managers can only view hold reports related to the cases they are a member of. For more information about eDiscovery permissions and the eDiscovery Administrator and eDiscovery Manager roles, see [Assign eDiscovery permissions](edisc-permissions).

## Step 2: View the hold report

1. Go to **eDiscovery** &gt; **Dashboards** &gt; **Hold report (preview)** to view your hold report.
2. Sort, filter, group by, and customize columns to customize your hold report.
3. Download the hold report to a .csv file for further analysis. The entire report is downloaded regardless of any filtering or grouping option you apply to the report. You can also [use a PowerShell script to create a hold report](edisc-hold-report-script) for automated reporting.

The item count at the top of the hold report is the total count of locations within the hold policies in the tenant. If the same location is placed on hold under different policies, the same location appears multiple times in the report under the respective case and hold policy and contributes to multiple item counts.

When you search the report, only the **Case name** and **Location** columns are searched. For example, if you search for the keyword *Test*, the search only returns items that are associated with a case or location that contains the word Test.

## Default hold report columns

- **Case Name**: Name of the case that the hold policy is associated with. If the case name changes and you update the hold policy associated with the case, the report immediately reflects the case name change for the associated row. When a full sync of the report occurs (currently every three to seven days), the case name also updates.
- **Hold name**: Name of the Hold Policy that contains the associated locations.
- **Last modified**: The date when the eDiscovery hold policy was last updated.
- **Location**: The Exchange mailbox or SharePoint site in the hold policy. If this field displays *None*, it indicates that the hold policy has no active locations within it. Any previous locations that were part of the policy are released from hold and removed from the policy.
- **Location error**: Displays the error message associated with the location within the hold policy. If this field displays *None*, it indicates that the associated location doesn't have errors, even if it's part of a *Partially Applied/Released* policy.
- **Location type**: Indicates if the location is a SharePoint site or Exchange mailbox.
- **Policy status**: The following policy status values are available:

    - *Applied successfully*: Indicates the location of the hold policy is turned on (enabled), a rule is enabled for the policy, and the policy is applied successfully. This status means the location is placed on hold.
    - *Applying*: Indicates that the hold policy that the location is part of is set to be turned on (enabled) and is in progress to apply holds to the locations in it. This job is an asynchronous job, which means some locations might be placed on hold while others might still be in progress. Wait for the hold job to complete checking the final status.
    - *Applied Partially*: – Indicates that the hold policy that the location is part of is set to be turned on (enabled) and has some locations where the hold might not be applied. Check the ‘Location error’ column. If the associated result is ‘None’ then the location is placed on hold. If there's an associated error, then the location isn't placed on hold and the error message is displayed here. Check the hold policy for more details to remediate and retry the hold.
    - *Released successfully*: Indicates that the hold policy that the location is part of is set to be turned off (disabled) and has completed successfully. This status means the associated location is successfully released from hold.
    - *Releasing*: Indicates that the hold policy that the location is part of is set to be turned off (disabled) and is in progress to release holds from the locations in it. This job is an asynchronous job, which means some locations might be removed from hold while others might still be in progress. Wait for the hold job to complete checking the final status.
    - *Released partially*: Indicates that the hold policy that the location is part of is set to be turned off (disabled) and has some locations where the hold might not be released. Check the ‘Location error’ column. If the associated result is ‘None’ then the location is successfully released from hold. If there's an associated error, then the location isn't removed from hold and the error message is displayed here. Check the hold policy for more details to remediate and retry the action.
    - *Policy failed*: Indicates that the policy is set up incorrectly. The policy doesn't have a rule or was set up with rule set as disabled. These policies aren't enforced even if the policy status is successful. To ensure these policies are enforced, create a rule and resync the policy. For more information, see [New-CaseHoldRule](/en-us/powershell/module/exchange/new-caseholdrule).

Note

If you delete a user account while an eDiscovery hold is active on the mailbox, the mailbox becomes an inactive mailbox. The hold report continues to show the location and hold status. If the location shows an error after you delete the account, this error might indicate that the hold isn't yet in place because you delete the account before the system applies it, or that the mailbox transition is still processing. To confirm that the hold is in place before you delete the account, see [Identify Exchange mailbox hold types in eDiscovery](edisc-hold-types-mailboxes).

## Other available hold report columns

- **Case type**: Indicates if the case is an eDiscovery or eDiscovery case with premium features.
- **Case status**: Shows the status of case. Values are *Active*, *Closing*, *Closed with error*, *Pending delete*, or *Closed*. If the case status changes and you update a hold policy associated with the case, the report immediately reflects the case status change for the associated row. When a full sync of the report occurs (currently every three to seven days), all case status changes are also updated.
- **Policy created by**: Shows the user that created the initial hold policy.
- **Policy last modified by**: Shows the user that last modified the hold policy.
- **Policy last modified**: Shows the last date that the policy was updated on. This date is the policy update date and doesn't necessarily match the date the location was placed on or released from hold.
- **Report last fetched**: Displays the date and time stamp of the latest fetch of policy status and location information by the report for the specific policy.
- **Policy created date**: Shows the first date that the policy was created on. This date is the policy creation date and doesn't necessarily match the date the location was placed on or released from hold.
- **Hold ID**: The unique ID of the hold policy.
- **Case ID**: The unique ID of the case associated with the hold policy.
- **Rule query**: Displays any content match query that is applied to the policy. If there's no content match query applied to the policy, this field is empty.
- **Rule ID**: The unique ID for the rule associated with the hold policy. This status is useful for sending information to Microsoft when reporting any hold errors. If there's no rule associated with the policy, *Rule not available* is displayed in this field. Policies where a rule isn't available aren't set up correctly and not enforced. Create rules and resync the policy. For more information, see [New-CaseHoldRule](/en-us/powershell/module/exchange/new-caseholdrule).