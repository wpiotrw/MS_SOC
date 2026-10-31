---
layout: Conceptual
title: Manage audit log retention policies | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-log-retention-policies
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discover how to create and customize audit log retention policies in Microsoft Purview to meet your organization's data retention needs.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-19T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-audit
ms.collection:
- purview-compliance
- audit
search.appverid:
- MOE150
- MET150
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: ad974e17-d2ee-f532-5a54-f745d9f53156
document_version_independent_id: ad974e17-d2ee-f532-5a54-f745d9f53156
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-log-retention-policies.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-log-retention-policies
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-log-retention-policies.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 044c9489-e80c-a1cd-af6d-35232fb0022c
---

# Manage audit log retention policies | Microsoft Learn

You can create and manage audit log retention policies in the [Microsoft Purview portal](purview-portal). Audit log retention policies are part of the new Microsoft Purview Audit (Premium) capabilities. An audit log retention policy lets you specify how long to retain audit logs in your organization. You can retain audit logs for up to 10 years. You can create policies based on the following criteria:

- All activities in one or more Microsoft services
- Specific activities in a Microsoft service performed by all users or by specific users
- A priority level that specifies which policy takes precedence if you have multiple policies in your organization

## Default audit log retention policy in Audit (Premium)

Audit (Premium) in Microsoft Purview provides a default audit log retention policy for all organizations. You can't modify this policy. It retains all Exchange Online, SharePoint, OneDrive, and Microsoft Entra audit records for one year. This default policy retains audit records that contain the value of **AzureActiveDirectory**, **Exchange**, **OneDrive**, and **SharePoint** for the **Workload** property (which is the service in which the activity occurred). Audit records for all other activities are retained for 180 days by default or you can change the retention to a different duration using a custom retention policy.

Note

The default audit log retention policy only applies to audit records for activity performed by users who are assigned an Office 365 or Microsoft 365 E5 license or have a Microsoft Purview Suite (formerly known as Microsoft 365 E5 Compliance) or E5 eDiscovery and Audit add-on license. If you have non-E5 users or guest users in your organization, their corresponding audit records are retained for 180 days.

The default retention period for audit records varies by license type and when the records were generated.

Important

The default retention period for Audit (Standard) changed from 90 days to 180 days. Audit (Standard) logs generated before October 17, 2023 are retained for 90 days. Audit (Standard) logs generated on or after October 17, 2023 follow the new default retention of 180 days.

## Before you create an audit log retention policy

- You need the *Organization Configuration* role in the Microsoft Purview portal to create or modify an audit retention policy.
- Your organization can have up to 50 audit log retention policies.
- To retain an audit log for longer than 180 days (and up to 1 year), the user who generates the audit log (by performing an audited activity) must have an Office 365 E5 or Microsoft 365 E5 license or a Microsoft Purview Suite (formerly known as Microsoft 365 E5 Compliance) or E5 eDiscovery and Audit add-on license. To retain audit logs for 10 years, the user who generates the audit log must also have a 10-year audit log retention add-on license in addition to an E5 license.

    Note

    If the user generating the audit log doesn't have the licenses required for the selected retention duration, data is retained according to the highest priority retention policy. This retention might be either the default retention policy for the user's license or the highest priority policy that matches the user and its record type.
- All custom audit log retention policies (created by your organization) take priority over the default retention policy. For example, if you create an audit log retention policy for Exchange mailbox activity that has a retention period that's shorter than one year, audit records for Exchange mailbox activities are retained for the shorter duration specified by the custom policy.
- The audit item lifetime for data is determined when you add it to the auditing pipeline and is based on the licensing defaults or applicable retention policies. Any changes to licensing or applicable retention policies change the expiration time of the audit data after updating. These changes don't update any previously committed items.

## Create an audit log retention policy

Complete the following steps to create an audit retention policy:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with a user account assigned the *Organization Configuration* role on the **Roles & scopes** page in the Microsoft Purview portal.
2. Select the **Audit** solution card. If the **Audit** solution card isn't displayed, select **View all solutions** and then select **Audit** from the **Core** section.
3. Select **Create audit retention policy**, and then complete the following fields on the flyout page:

    ![Screenshot of the New audit retention policy flyout page with fields for policy name, description, users, record type, duration, and priority.](media/new-audit-retention-policy.png)

    - **Policy name**: The name of the audit log retention policy. This name must be unique in your organization, and you can't change it after creating the policy.
    - **Description**: Optional, but helpful to provide information about the policy, such as the record type or workload, users specified in the policy, and the duration.
    - **Users:** Select one or more users to apply the policy to. If you leave this box blank, the policy applies to all users.
    - **Record type**: The audit record type the policy applies to. If you leave this property blank, the policy applies to all record types. You can select a single record type or multiple record types:
    - If you select a single record type, the **Activities** field is dynamically displayed. Use the drop-down list to select activities from the selected record type to apply the policy to. If you don't select specific activities, the policy applies to all activities of the selected record type.

        - If you select multiple record types, you don't have the ability to select activities. The policy applies to all activities of the selected record types.
        - **Duration:** The amount of time to retain the audit logs that meet the criteria of the policy. The available options are *7 Days*, *30 Days*, *6 Months*, *9 Months*, *1 Year*, *3 Years*, *5 Years*, and *7 Years*. Users with the 10-year Audit Log Retention add-on license can select a *10 Years* option.

    Important

    To retain audit logs for the 7 and 30 days duration options, you must have a Microsoft 365 Enterprise E5 subscription. To retain audit logs for the 3, 5, and 7 years duration options, you must be assigned to a 10-Year Audit Log Retention add-on license in addition to your Microsoft 365 Enterprise E5 subscription. For more information about Audit subscriptions and add-ons, see [Auditing solutions in Microsoft Purview](audit-solutions-overview#licensing-requirements)

    - **Priority**: This value determines the order in which audit log retention policies in your organization are processed. A lower value indicates a higher priority. Valid priorities are numerical values between **1** and **10000**. A value of **1** is the highest priority, and a value of **10000** is the lowest priority. For example, a policy with a value of **5** takes priority over a policy with a value of **10**. Any custom audit log retention policy takes priority over the default policy for your organization.
4. Select **Save** to create the new audit log retention policy.

The new policy appears in the list on the **Policies** page.

## Manage audit log retention policies in the Microsoft Purview portal

The **Audit retention policies** tab (also called the *dashboard*) lists audit log retention policies. You can use the dashboard to view, edit, and delete audit retention policies.

### View policies in the dashboard

The dashboard lists audit log retention policies. One advantage of viewing policies in the dashboard is that you can select the **Priority** column to list the policies in the priority order in which they're applied. A lower value indicates a higher priority.

![Screenshot of the Audit retention policies dashboard showing the Priority column used to sort policies by processing order.](media/auditlogretentiondashboardpriority.png)

You can also select a policy to display its settings on the flyout page.

Note

The dashboard doesn't display the default audit log retention policy for your organization.

### Edit policies in the dashboard

To edit a policy, select it to display the flyout page. You can modify one or more settings and then save your changes.

Important

If you use the *New-UnifiedAuditLogRetentionPolicy* cmdlet, you might create an audit log retention policy for record types or activities that aren't available in the **Create audit retention policy** tool in the dashboard. If the policy includes record types or activities that aren't available in the **Create audit retention policy** tool, you can't edit the policy (for example, change the retention duration or add and remove activities) from the **Audit retention policies** dashboard. You can only view and delete the policy in the Microsoft Purview portal. To edit the policy, you need to use the [Set-UnifiedAuditLogRetentionPolicy](/en-us/powershell/module/exchange/set-unifiedauditlogretentionpolicy) cmdlet in Security & Compliance PowerShell. A message is displayed at the top of the flyout page for policies that you need to edit by using PowerShell.

### Delete policies in the dashboard

To delete a policy, select the **Delete** icon and then confirm that you want to delete the policy. The policy is removed from the dashboard, but it might take up to 30 minutes for the policy to be removed from your organization.

## Create and manage audit log retention policies in PowerShell

You can also use Security & Compliance PowerShell to create and manage audit log retention policies. One reason to use PowerShell is to create a policy for a record type or activity that isn't available in the UI.

### Create an audit log retention policy in PowerShell

Complete the following steps to create an audit log retention policy in PowerShell:

1. [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).
2. Run the following command to create an audit log retention policy:

    ```powershell
    New-UnifiedAuditLogRetentionPolicy -Name "Microsoft Teams Audit Policy" -Description "One year retention policy for all Microsoft Teams activities" -RecordTypes MicrosoftTeams -RetentionDuration TenYears -Priority 100
    ```

    This example creates an audit log retention policy named "Microsoft Teams Audit Policy" with these settings:

    - A description of the policy.
    - Retains all Microsoft Teams activities (as defined by the *RecordType* parameter).
    - Retains Microsoft Teams audit logs for 10 years.
    - A priority of 100.

The following example creates an audit log retention policy that retains audit logs for the "User logged in" activity for six months for the user admin@contoso.onmicrosoft.com.

```powershell
New-UnifiedAuditLogRetentionPolicy -Name "SixMonth retention for admin logons" -RecordTypes AzureActiveDirectoryStsLogon -Operations UserLoggedIn -UserIds admin@contoso.onmicrosoft.com -RetentionDuration SixMonths -Priority 25
```

For more information, see [New-UnifiedAuditLogRetentionPolicy](/en-us/powershell/module/exchange/new-unifiedauditlogretentionpolicy).

### View policies in PowerShell

Use the [Get-UnifiedAuditLogRetentionPolicy](/en-us/powershell/module/exchange/get-unifiedauditlogretentionpolicy) cmdlet in Security & Compliance PowerShell to view audit log retention policies.

The following command displays the settings for all audit log retention policies in your organization. This command sorts the policies from the highest to lowest priority.

```powershell
Get-UnifiedAuditLogRetentionPolicy | Sort-Object -Property Priority -Descending | FL Priority,Name,Description,RecordTypes,Operations,UserIds,RetentionDuration
```

Note

The *Get-UnifiedAuditLogRetentionPolicy* cmdlet doesn't return the default audit log retention policy for your organization.

### Edit policies in PowerShell

Use the [Set-UnifiedAuditLogRetentionPolicy](/en-us/powershell/module/exchange/set-unifiedauditlogretentionpolicy) cmdlet in Security & Compliance PowerShell to edit an existing audit log retention policy.

### Delete policies in PowerShell

Use the [Remove-UnifiedAuditLogRetentionPolicy](/en-us/powershell/module/exchange/remove-unifiedauditlogretentionpolicy) cmdlet in Security & Compliance PowerShell to delete an audit log retention policy. It might take up to 30 minutes for the policy to be removed from your organization.