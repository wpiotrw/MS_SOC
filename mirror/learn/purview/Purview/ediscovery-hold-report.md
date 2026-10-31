---
layout: Conceptual
title: Hold report in eDiscovery (Premium) (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-hold-report
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use the hold report in eDiscovery (Premium) to display information about the holds associated with all eDiscovery cases in your organization.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection: M365-security-compliance
search.appverid:
- MOE150
- MET150
locale: en-us
document_id: 2913d59c-6852-9c20-ba82-1e63e2e173e0
document_version_independent_id: 2913d59c-6852-9c20-ba82-1e63e2e173e0
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-hold-report.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-hold-report
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-hold-report.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 3b6ebff2-8d39-3fdb-ad1b-5e2406178025
---

# Hold report in eDiscovery (Premium) (preview) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

The hold report in eDiscovery (Premium) lets users with *eDiscovery Administrator* or *eDiscovery Manager (preview)* permissions access a built-in report with information on all holds associated with eDiscovery cases in the Microsoft Purview portal. This report includes eDiscovery holds associated with eDiscovery (Standard) and eDiscovery (Premium) cases. The hold report currently doesn't show custodian association for each data source, but will show the location.

The hold report is a report on all hold policies within the tenant and lists all locations that are part of those hold policies (whether enabled or disabled). Holds from eDiscovery (Standard) cases are identified by the **Standard** value in the **Case type** column. You can use the **Case type** group option to group the eDiscovery holds from eDiscovery (Standard) cases.

## Step 1: Verify your subscription and permissions

- Your organization must have an [organization subscription](ediscovery-premium-get-started) that supports eDiscovery (Premium) to generate and access the hold report.
- Users accessing the hold report must be assigned the *eDiscovery Administrator* or *eDiscovery Manager (preview)* role. All eDiscovery Administrators and eDiscovery Managers in your organization can access it on the **Hold report (preview)** tab in **Reports** section of eDiscovery (Premium). eDiscovery Managers (preview) can only view hold reports which are related to the cases they are a member of. For more information about eDiscovery permissions and the eDiscovery Administrator and eDiscovery Manager roles, see [Assign eDiscovery permissions](ediscovery-assign-permissions).

## Step 2: View the hold report

1. Go to **eDiscovery** &gt; **Premium** &gt; **Reports** &gt; **Hold report (preview)** to view your hold report.
2. Sort, filter, group by, and customize columns to customize your hold report.
3. Download the hold report to CSV file for further analysis. The entire report is downloaded regardless of any filtering or grouping option applied to the report.

The item count at the top of the hold report is total count of locations within the hold policies in the tenant. If the same location is placed on hold under different policies, then the same location is displayed multiple times in the report under the respective case and hold policy and contribute to multiple item counts.

When you search the report, only the **Case name** and **Location** columns are searched. For example, if you search for the keyword *Test*, the search only returns items that are associated with a case or location that contains the word Test.

## Default hold report columns

- **Case Name**: Name of the case that the hold policy is associated with. If the case name changed and a hold policy associated with the case is also updated, the case name change for the associated row is immediately reflected in the report. When a full sync of the report occurs (currently every 3 to 7 days), the case name is also updated.
- **Hold name**: Name of the Hold Policy that contains the associated locations.
- **Last modified**: The date when the eDiscovery hold policy was last updated.
- **Location**: The exchange mailbox or SharePoint site in the hold policy. If this field displays *None*, it indicates that the hold policy has no active locations within it. Any previous locations that were part of the policy are released from hold and removed from the policy.
- **Location error**: Displays the error message associated with the location within the hold policy. If this field displays *None*, it indicates that associated location doesn't have errors, even if it's part of a *Partially Applied/Released* policy.
- **Location type**: Indicates if the location is a SharePoint site or Exchange mailbox.
- **Policy status**: The following policy status values are available:

    - *Applied successfully*: Indicates the location of the hold policy is turned on (enabled), a rule is enabled for the policy and the policy is applied successfully. This status means the location is placed on hold.
    - *Applying*: Indicates that the hold policy that the location is part of is set to be turned on (enabled) and is in progress to apply holds to the locations in it. This job is an asynchronous job, which means some locations may have been placed on hold while others may still be in progress. Wait for the hold job to complete checking the final status.
    - *Applied Partially*: – Indicates that the hold policy that the location is part of is set to be turned on (enabled) and has some locations where the hold may haven't applied. Check the ‘Location error’ column. If the associated result is ‘None’ then the location is placed on hold. If there's an associated error, then the location isn't placed on hold and the error message is displayed here. Check the hold policy for more details to remediate and retry the hold.
    - *Released successfully*: Indicates that the hold policy that the location is part of is set to be turned off (disabled) and has completed successfully. This status means the associated location is successfully released from hold.
    - *Releasing*: Indicates that the hold policy that the location is part of is set to be turned off (disabled) and is in progress to release holds from the locations in it. This job is an asynchronous job, which means some locations may have been removed from hold while others may still be in progress. Wait for the hold job to complete checking the final status.

        Note

        System default policies (Custodian/NCDS) can only turned off by closing the case. The locations within these policies can still be removed from hold in an active case by releasing them from the data source.
    - *Released partially*: Indicates that the hold policy that the location is part of is set to be turned off (disabled) and has some locations where the hold may haven't released. Check the ‘Location error’ column. If the associated result is ‘None’ then the location is successfully released from hold. If there's an associated error, then the location isn't removed from hold and the error message is displayed here. Check the hold policy for more details to remediate and retry the action.
    - *Policy failed*: Indicates that the policy is set up incorrectly. The policy doesn't have a rule or was set up with rule set as disabled. These policies won't be enforced even if the policy status is successful. To ensure these policies are enforced, create a rule and resync the policy. For more information, see [New-CaseHoldRule](/en-us/powershell/module/exchange/new-caseholdrule).

## Other available hold report columns

- **Case type**: Indicates if the case is an eDiscovery (Standard) or eDiscovery (Premium case).
- **Case status**: Shows the status of case. Values are *Active*, *Closing*, *Closed with error*, *Pending delete*, or *Closed*. If the case status changed and a hold policy associated with the case is also updated, the case status change for the associated row is immediately reflected in the report. When a full sync of the report occurs (currently every 3 to 7 days), all case status changes are also updated.
- **Policy created by**: Shows the user that created the initial hold policy.
- **Policy last modified by**: Shows the user that last modified the hold policy.
- **Policy last modified**: Shows the last date that the policy was updated on. This date is the policy update date and doesn't necessarily match the date the location was placed on/released from hold.
- **Report last fetched**: Displays the date and time stamp of the latest fetch of policy status and location information by the report for the specific policy.
- **Policy created date**: Shows the first date that the policy was created on. This date is the policy creation date and doesn't necessarily match the date the location was placed on/released from hold.
- **Hold ID**: The unique ID of the hold policy.
- **Case ID**: The unique ID of the case associated with the hold policy.
- **Rule query**: This displays any content match query that is applied to the policy. If there's no content match query applied to the policy, this field is empty.
- **Rule ID**: The unique ID for the rule associated with the hold policy. This status is useful for sending information to Microsoft when reporting any hold errors. If there's no rule associated with the policy, *Rule not available* is displayed in this field. Policies where a rule isn't available aren't set up correctly and not enforced. Create rules and resync the policy. For more information, see [New-CaseHoldRule](/en-us/powershell/module/exchange/new-caseholdrule).