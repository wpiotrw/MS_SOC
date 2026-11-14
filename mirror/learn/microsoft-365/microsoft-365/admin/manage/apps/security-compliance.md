---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Manage security and compliance for Microsoft Copilot Managed Runtime (preview) - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/apps/security-compliance?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn how to manage security and compliance for apps in Copilot Managed Runtime..
ms.date: 2026-11-13T00:00:00.0000000Z
author: Greggbarker-MS
ms.author: grbarker
manager: zoraz
ms.reviewer: mkaur
ms.topic: concept-article
ms.service: microsoft-365
ms.subservice: managed-apps-admin
ai-usage: ai-assisted
locale: en-us
document_id: c6ea3d1d-fe29-fa01-4ce0-7e8b2a58626e
document_version_independent_id: c6ea3d1d-fe29-fa01-4ce0-7e8b2a58626e
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/apps/security-compliance.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/apps/security-compliance
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/apps/security-compliance.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 73b58d05-d351-74f6-cc14-4d115972b17e
---

# Manage security and compliance for Microsoft Copilot Managed Runtime (preview) - Microsoft 365 admin | Microsoft Learn

[This article is prerelease documentation and is subject to change.]

This article covers security and compliance for Copilot Managed Runtime across the Power Platform admin center and the Microsoft 365 admin center. It explains how to apply data protection policies, configure access controls, and monitor compliance for Copilot Managed Runtime in your tenant.

Important

- This is a preview feature.
- These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?LinkId=2373139), and are available before an official release so that customers can get early access and provide feedback.

## Overview

Apps in Copilot Managed Runtime are line-of-business applications built with the Copilot Managed Runtime SDK. You configure security settings primarily in the **Microsoft 365 admin center**, with additional environment-level controls available in the **Power Platform admin center**.

This article focuses on security capabilities that are specific to apps in Copilot Managed Runtime. For general Power Platform security, see [Security overview](/en-us/power-platform/admin/security/security-overview).

## Prerequisites

To manage security settings for Copilot Managed Runtime, you need one of the following Microsoft Entra ID roles:

| Role | Access level |
| --- | --- |
| [Global Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) | Read and write |
| [Power Platform Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#power-platform-administrator) | Read and write |
| [AI Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#ai-reader) | Read-only access to Copilot Managed Runtime configuration and security settings |

The environment where you deploy apps built with Copilot Managed Runtime must be a [Managed Environment](/en-us/power-platform/admin/managed-environment-overview).

## Where to configure Copilot Managed Runtime

You can view and configure Copilot Managed Runtime in two admin centers:

| Admin center | What you can do |
| --- | --- |
| **Microsoft 365 admin center (MAC)** | Primary surface for Copilot Managed Runtime governance. View app inventory, configure sharing controls, manage app settings, and apply environment group rules. |
| **Power Platform admin center (PPAC)** | View environment groups, configure environment-level security settings, and manage advanced connector policies. |

Microsoft 365 admin center is the primary admin experience for Copilot Managed Runtime. Settings you configure in the Microsoft 365 admin center appear in the Power Platform admin center. Administrators can use either surface, but Copilot Managed Runtime-specific configuration starts in the Microsoft 365 admin center.

## Sharing controls

Configure sharing for apps in Copilot Managed Runtime at the environment group level. These controls are specific to Copilot Managed Runtime and operate separately from general Power Platform sharing settings.

To configure sharing for apps in Copilot Managed Runtime:

1. In the **Microsoft 365 admin center**, go to **Settings** &gt; **App settings**.
2. Go to the environment group rules.
3. Find the Copilot Managed Runtime sharing rule to set sharing limits.

Sharing controls let administrators restrict how broadly makers can share apps built with Copilot Managed Runtime within the organization. The sharing limit applies to all apps built with Copilot Managed Runtime within the environment group.

Note

Configure Copilot Managed Runtime sharing at the environment group level, not at the individual app or environment level. This setting is specific to Copilot Managed Runtime and doesn't affect sharing for other Power Platform resources in the same environment.

For more information about environment groups and governance configuration, see [Governance for Copilot Managed Runtime](/en-us/power-platform/admin/managed-governance).

## Control access with a security group

Apps in Copilot Managed Runtime use the security group associated with their environment to control access. Associate a Microsoft Entra security group with the environment to restrict who can run apps in that environment. The restriction applies automatically to all apps in the environment, so you don’t need to configure each app separately.

Environment access and app sharing are separate controls. To run an app, a user must be a member of the environment’s security group and have access to the app. Sharing an app doesn’t bypass the environment’s security group restriction. Adding a user to the security group doesn’t grant access to individual apps.

To associate a security group with an environment, follow these steps:

1. In the Power Platform admin center, select **Manage** &gt; **Environments**.
2. Select the environment, and then select **Edit**.
3. In **Edit details**, under **Security group**, select the edit icon.
4. Find and select the group, select **Done**, and then select **Save**.

Important

Before you associate a security group with an existing environment, review the group’s membership. Users who aren’t members of the group lose access to managed apps in the environment. To revoke a user’s environment access later, remove the user from the security group.

For more information about configuration, supported group types, and environment access requirements, see [Control user access to environments with security groups and licenses](/en-us/power-platform/admin/control-user-access).

## Content security policy (CSP)

Apps built with Copilot Managed Runtime enforce content security policy headers to protect against cross-site scripting and other injection attacks. Each app has its own CSP configuration, which the platform applies.

For the default directives and instructions to review and customize the policy, see [Content security policy](governance#content-security-policy).

## Advanced connector policies (ACP)

Advanced connector policies control which connectors and connector actions apps built with Copilot Managed Runtime can use. ACP applies to all resources in the environment, including apps, flows, and agents. Apps built with Copilot Managed Runtime don't require any extra configuration.

Policies configured for the environment or environment group apply automatically to apps built with Copilot Managed Runtime deployed there.

For details on configuring advanced connector policies, see [Advanced connector policies](/en-us/power-platform/admin/advanced-connector-policies).

## Audit app activities with Microsoft Purview

When Copilot Managed Runtime auditing is available in your environment, use Microsoft Purview Audit to investigate app creation, deployment, sharing, and access. Audit records help you identify who performed an activity, which app was affected, and when the activity occurred.

Audit records describe specific activities. For operational health metrics and alerts, use [Monitor the health of apps](/en-us/microsoft-365/admin/manage/apps/visibility-monitoring).

### Before you search

To search or export audit records, you need the **Audit Logs** or **View-Only Audit Logs** role in Microsoft Purview. The **Audit Manager** and **Audit Reader** role groups provide these permissions. The Copilot Managed Runtime administrator roles listed earlier in this article don't replace these Purview permissions.

Verify that your organization meets the Microsoft Purview Audit subscription requirements and that audit log search is turned on. For licensing, permissions, and setup instructions, see [Get started with auditing solutions](/en-us/purview/audit-get-started) and [Verify the auditing status for your organization](/en-us/purview/audit-log-enable-disable#verify-the-auditing-status-for-your-organization).

### App activities

Copilot Managed Runtime app events use the **Copilot** workload and the **CopilotManagedRuntime** record type (`519`).

The following table lists the activity display names and their operation names. Use the exact operation names when you search.

| Activity display name | Operation name | When the event is generated |
| --- | --- | --- |
| Changed a Copilot Managed Runtime App quarantine state | `AdminSetQuarantineStateCopilotManagedRuntimeApp` | An administrator changes the app's quarantine state, such as blocking or unblocking the app. |
| Created a Copilot Managed Runtime App | `CreatedCopilotManagedRuntimeApp` | An app is created. |
| Created a Copilot Managed Runtime App share link | `CreatedCopilotManagedRuntimeAppShareLink` | A share link is created for the app. |
| Deleted a Copilot Managed Runtime App | `DeletedCopilotManagedRuntimeApp` | An app is soft-deleted. |
| Deleted a Copilot Managed Runtime App share link | `DeletedCopilotManagedRuntimeAppShareLink` | A share link is deleted, revoking access through that link. |
| Deployed a Copilot Managed Runtime App | `DeployedCopilotManagedRuntimeApp` | An app build is deployed to a stage. |
| Downloaded Copilot Managed Runtime App content | `DownloadedCopilotManagedRuntimeAppContent` | An app content file is served through the runtime gateway. This activity can occur when a user opens an app; it doesn't necessarily mean the user explicitly downloaded a file. |
| Edited a Copilot Managed Runtime App permission | `EditedCopilotManagedRuntimeAppPermission` | An app role assignment is added or removed. The event identifies the recipient and the permission change. |
| Launched a Copilot Managed Runtime App | `LaunchedCopilotManagedRuntimeApp` | An app is launched. |
| Started a Copilot Managed Runtime App build | `StartedCopilotManagedRuntimeAppBuild` | A service-side app build is started. This event doesn't indicate that the build completed successfully. |
| Uploaded a Copilot Managed Runtime App build | `UploadedCopilotManagedRuntimeAppBuild` | An externally built app artifact is uploaded. This event doesn't indicate that the build was deployed. |

These events describe app activities, not every action a user performs inside an app. To investigate environment group and governance changes, see [View Power Platform admin activity logs in Microsoft Purview](/en-us/power-platform/admin/activity-logging-auditing/activity-logs-power-platform-admin#activity-category-environment-groups-and-rules).

### Search and export app events

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Solutions** &gt; **Audit**.
3. On the **Search** page, select the **Date and time range (UTC)** for the activities you want to investigate.
4. In **Activities - operations names**, enter one or more operation names from the table, separated by commas. For example, enter `CreatedCopilotManagedRuntimeApp,DeletedCopilotManagedRuntimeApp` to find app creation and deletion events.
5. To narrow the search by service, select **CopilotManagedRuntime** under **Record types**. You can also select **Copilot** under **Workloads**, but that workload includes activities beyond Copilot Managed Runtime.
6. Optionally, select **Users** to restrict the search to specific accounts. Leave this field blank to include all accounts.
7. Select **Search**. When the search job completes, open it and select an activity to view its details.
8. To download the results as a CSV file, select **Export**.

For more information about search filters, result details, and exports, see [Search the audit log](/en-us/purview/audit-search).

For programmatic access to audit records, see the [Office 365 Management Activity API reference](/en-us/office/office-365-management-api/office-365-management-activity-api-reference).

Note

Audit records aren't available immediately after an activity occurs. Microsoft doesn't guarantee a specific ingestion time. Retention depends on your organization's licensing and applicable audit retention policies. For details, see [Before you search the audit log](/en-us/purview/audit-search#before-you-search-the-audit-log) and [Manage audit log retention policies](/en-us/purview/audit-log-retention-policies).

### Understand event details

App events include activity, actor, app, and environment information. Some properties can be empty when the information isn't available for the operation. For example, project and repository identifiers depend on the app's source control metadata.

Use the following properties to correlate records for an app or investigate an activity:

| Property | Description |
| --- | --- |
| `copilotmanagedruntime.analytics.activity.id` | The unique identifier of the activity record. |
| `copilotmanagedruntime.analytics.activity.name` | The operation name from the app activities table. |
| `copilotmanagedruntime.analytics.operation.is_successful` | When the recorded operation succeeds. A successful build start doesn't establish that the build itself succeeded. |
| `copilotmanagedruntime.analytics.resource.app.id` | The identifier of the affected app. |
| `copilotmanagedruntime.analytics.resource.app.display_name` | The app's display name. |
| `copilotmanagedruntime.analytics.resource.environment.id` | The identifier of the app's environment. |
| `copilotmanagedruntime.analytics.resource.project.id` | The associated project identifier, when available. |
| `copilotmanagedruntime.analytics.resource.repository.id` | The associated repository identifier, when available. |
| `copilotmanagedruntime.analytics.resource.telemetry_correlation.id` | The correlation identifier for the request. |
| `enduser.principal_name` | The identity recorded for the caller. |
| `enduser.ip_address` | The caller's IP address, when available. |
| `user_agent.original` | The user agent associated with the request, when available. |

Additional properties depend on the activity. In the following table, property names are shown without the common `copilotmanagedruntime.analytics.resource.` prefix.

| Activity | Additional properties |
| --- | --- |
| Start or upload a build | `build.id` identifies the build. Service-side build start events also include `build.source`, with the value `ServerBuild`. |
| Deploy an app | `build.id` identifies the deployed build, and `stage.name` identifies the deployment stage. |
| Edit app permissions | `permission.change_type` is `Added` or `Removed`. `permission.principal.id`, `permission.principal.type`, and `permission.role` describe the recipient and role assignment. |
| Create or delete a share link | `share_link.id` identifies the link. |
| Change an app's blocked state | `quarantine.state` records the resulting quarantine state. |
| Download app content | `request.path` identifies the content path, and `appcontent.kind` records the content type. |