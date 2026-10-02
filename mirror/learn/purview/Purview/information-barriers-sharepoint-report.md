---
layout: Conceptual
title: Create an Information Barriers policy compliance report | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint-report
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.date: 2026-09-21T00:00:00.0000000Z
description: Learn how to find noncompliant sites after Information Barriers policies change.
ms.author: srmuppana
author: srmuppana
manager: dbolick
recommendations: true
ms.reviewer: nibandyo
audience: Admin
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: purview
ms.subservice: purview-information-barriers
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
ms.collection:
- purview-compliance
- M365-collaboration
ai-usage: ai-assisted
ms.custom: sfi-ga-nochange
locale: en-us
document_id: 9615f31a-ffee-626d-5375-ea0447bd2ca0
document_version_independent_id: 9615f31a-ffee-626d-5375-ea0447bd2ca0
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-barriers-sharepoint-report.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-barriers-sharepoint-report
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-barriers-sharepoint-report.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 7fb64938-82ae-be2d-9075-597faba93b8e
---

# Create an Information Barriers policy compliance report | Microsoft Learn

If a compliance administrator changes an existing Information Barriers policy, the change might affect the compatibility of segments already associated with a site.

For example, a policy might allow communication and collaboration between the Sales and Research segments. Later, the policy might not allow communication and collaboration between these segments. The segments are incompatible and shouldn't be associated with the same site.

By using the SharePoint Information Barriers policy compliance report, SharePoint administrators can view the list of sites that don't comply with existing policies. The report covers these sites:

- Microsoft 365 group-connected team sites that aren't connected to Microsoft Teams
- Communication sites
- Modern team sites that aren't connected to Microsoft 365 groups
- OneDrive
- User-owned SharePoint Embedded containers

The report displays the list of sites that don't comply with the existing policies that you recently updated. For each noncompliant site, it shows compatible segments, incompatible segments, and invalid segments (those segments that no longer exist).

If a OneDrive or user-owned SharePoint Embedded container doesn't comply, this report lets you update its segments to be compliant with the latest IB policies in your organization.

Note

You only need to run this report if you change Information Barriers policies. Depending on the number of sites in your organization, it can take a long time for this report to run.

## Run the report

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

1. You must use the latest version of the [SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251). If you installed a previous version of the SharePoint Online Management Shell, go to **Add or remove programs** and uninstall *SharePoint Online Management Shell*. Then, install the latest version. To learn more, see [Get started with SharePoint Online Management Shell](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
2. Connect to SharePoint Online as a [Global Administrator or SharePoint Administrator](/en-us/sharepoint/sharepoint-admin-role?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) in Microsoft 365. For more information, see [Getting started with SharePoint Online Management Shell](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).
3. Run the following command to build the report:

    ```PowerShell
    Start-SPOInformationBarriersPolicyComplianceReport
    ```

    Or, to automatically update any noncompliant OneDrive accounts when you build the report, run:

    ```PowerShell
    Start-SPOInformationBarriersPolicyComplianceReport -UpdateOneDriveSegments
    ```

    Or, to automatically update any noncompliant user-owned SharePoint Embedded containers when you build the report, run:

    ```PowerShell
    Start-SPOInformationBarriersPolicyComplianceReport -UpdateUserOwnedContainerSegments
    ```
4. Run the following command to view the status of the task:

    ```PowerShell
    Get-SPOInformationBarriersPolicyComplianceReport
    ```

    The command returns the following set of information:

    ```text
    State: Completed
    Id: beedfc3e-850c-4ca2-9ae0-7eacbe529d77
    StartTimeInUtc: 9/21/2026 1:11:32 AM
    CompleteTimeInUtc: 9/21/2026 1:11:33 AM
    QueuedTimeInUtc: 9/21/2026 1:07:11 AM
    UpdateOneDriveSegments: False
    UpdateUserOwnedContainerSegments: True
    ```
5. Run the following command to view the report:

    ```PowerShell
    Get-SPOInformationBarriersPolicyComplianceReport -reportid <ID>
    ```

    (Where *ID* is the report's ID from the previous step.)

    The command returns the following set of information for each site:

    ```text
    Content: {8d7c4a12-5f6e-4b8d-9a31-c7e2f4a9d6b5}
    HasNonCompliantSites: True
    State: Completed
    Id: beedfc3e-850c-4ca2-9ae0-7eacbe529d77
    StartTimeInUtc: 9/21/2026 1:11:32 AM
    CompleteTimeInUtc: 9/21/2026 1:11:33 AM
    QueuedTimeInUtc: 9/21/2026 1:07:11 AM
    UpdateOneDriveSegments: False
    UpdateUserOwnedContainerSegments: True
    ```

    The **Content** row lists the sites that aren't compliant. If all sites are compliant, the **Content** row is empty and **HasNonCompliantSites** is `False`.
6. Run the following command to view details about the noncompliant segments associated with each site:

    ```PowerShell
    $report = Get-SPOInformationBarriersPolicyComplianceReport -reportid <ID> $report.Content
    ```

    (Where *ID* is the report's ID from the previous step.)

    The command returns the following set of information for each site:

    ```text
    SiteId: 3ef21e8a-69d9-4bf0-a70f-0328e5a18087
    SiteUrl: https://contoso.sharepoint.com/sites/Research
    SiteType: Group
    ComplianceState: NonCompliant
    CurrentSegments: Sales, Research
    OriginalSegments: Sales, Research
    InvalidIBSegments:
    IncompatibleSegmentsPairs: <Sales, Research>
    FailedToBeProcessed: False
    ```

Note

For info about removing incompatible segments, see [Use Information Barriers with SharePoint](information-barriers-sharepoint#2-use-sharepoint-powershell-to-view-and-manage-information-segments-on-a-site). When you finish with a report, delete it by using `Remove-SPOInformationBarriersPolicyComplianceReport -reportid <>`.