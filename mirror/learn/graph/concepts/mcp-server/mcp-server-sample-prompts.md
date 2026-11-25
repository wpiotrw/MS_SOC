---
layout: Conceptual
title: Sample prompts for Microsoft MCP Server for IT Admins - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/mcp-server/mcp-server-sample-prompts
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: Licantrop0
ms.author: lucaspol
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: ent-mcp-server
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: how-to
description: Explore example natural language prompts that query and manage Microsoft Entra data with Microsoft MCP Server for IT Admins.
ms.date: 2026-11-17T00:00:00.0000000Z
locale: en-us
document_id: e648ba19-a497-b56f-7f7c-7f2edff14765
document_version_independent_id: e648ba19-a497-b56f-7f7c-7f2edff14765
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/mcp-server/mcp-server-sample-prompts.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: mcp-server/mcp-server-sample-prompts
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/mcp-server/mcp-server-sample-prompts.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 45c3e8ee-00e7-04e4-47f0-0eeb61078b14
---

# Sample prompts for Microsoft MCP Server for IT Admins - Microsoft Graph | Microsoft Learn

Microsoft MCP Server for IT Admins translates natural language questions and requests into Microsoft Graph API calls against your Microsoft Entra tenant. This article lists sample prompts by scenario. The prompts in Write actions change data in your tenant.

Tip

The MCP-enabled AI agent shows you the Microsoft Graph API calls it runs for each prompt. You can reuse these calls in your own scripts, applications, or automation workflows.

## Prerequisites

- Complete the setup in [Get started with Microsoft MCP Server for IT Admins](get-started).
- Your MCP client's app registration needs the three [required permissions](get-started#required-permissions), plus the Microsoft Graph delegated permissions that each prompt lists, with admin consent.
- The signed-in user needs the Microsoft Entra roles for each operation. The MCP server runs every request with that user's permissions.
- To show user names and emails in results, such as group members, owners, or role assignees, the app also needs `User.ReadBasic.All` or `User.Read.All`. Without it, Microsoft Graph returns only the object IDs of users.

## User management

### Count and list users

**Prompt:** "How many users are in my tenant?"

**What it does:** Returns the total count of users in your Microsoft Entra tenant.

**Required permission:**`User.ReadBasic.All`

**Prompt:** "List the first 10 users in my tenant"

**What it does:** Retrieves basic information about users including display name, user principal name, and email address.

**Required permission:**`User.ReadBasic.All`

**Prompt:** "Show me recently created users"

**What it does:** Lists users ordered by creation date, showing the most recently created accounts first.

**Required permission:**`User.Read.All`

**Prompt:** "How many guest users do we have?"

**What it does:** Counts external users (guests) in your tenant.

**Required permission:**`User.Read.All`

### User sign-in activity

**Prompt:** "Which users haven't signed in for the last 30 days?"

**What it does:** Identifies inactive user accounts based on sign-in activity data.

**Required permissions:**`User.Read.All`, `AuditLog.Read.All`

**Prompt:** "When did [user email] last sign in?"

**What it does:** Retrieves the most recent sign-in timestamp for a specific user.

**Required permissions:**`User.Read.All`, `AuditLog.Read.All`

**Prompt:** "Show me sign-in failures for [user email]"

**What it does:** Lists failed sign-in attempts for a specific user, including error details.

**Required permission:**`AuditLog.Read.All`

### User account status

**Prompt:** "List disabled user accounts"

**What it does:** Returns users where `accountEnabled` is set to false.

**Required permission:**`User.Read.All`

**Prompt:** "Show me recently deleted users"

**What it does:** Retrieves users from the directory's deleted items collection.

**Required permission:**`User.Read.All`

**Prompt:** "List users synced from on-premises Active Directory"

**What it does:** Identifies users where `onPremisesSyncEnabled` is true.

**Required permission:**`User.Read.All`

## Group management

### Count and list groups

**Prompt:** "How many groups are in my tenant?"

**What it does:** Returns the total count of groups.

**Required permission:**`GroupMember.Read.All`

**Prompt:** "List all security groups"

**What it does:** Retrieves groups where `securityEnabled` is true.

**Required permission:**`GroupMember.Read.All`

**Prompt:** "Show me cloud-only groups"

**What it does:** Lists groups that aren't synchronized from on-premises Active Directory.

**Required permission:**`GroupMember.Read.All`

**Prompt:** "Find groups without owners"

**What it does:** Identifies ownerless groups that may need attention.

**Required permission:**`GroupMember.Read.All`

### Group membership

**Prompt:** "List members of [group name]"

**What it does:** Retrieves all users who are members of the specified group.

**Required permission:**`GroupMember.Read.All`

**Prompt:** "Which groups is [user email] a member of?"

**What it does:** Lists all group memberships for a specific user.

**Required permissions:**`User.Read.All`, `GroupMember.Read.All`

**Prompt:** "Show me all groups provisioned for Microsoft Teams"

**What it does:** Lists Microsoft 365 groups that have Teams enabled.

**Required permission:**`GroupMember.Read.All`

## Application and service principal management

### List applications

**Prompt:** "How many applications are registered in my tenant?"

**What it does:** Counts both application registrations and service principals.

**Required permission:**`Application.Read.All`

**Prompt:** "List applications registered in my tenant"

**What it does:** Retrieves all application registrations with basic details.

**Required permission:**`Application.Read.All`

**Prompt:** "Show me applications from external publishers"

**What it does:** Lists service principals where the app owner organization differs from your tenant.

**Required permission:**`Application.Read.All`

### Application ownership and details

**Prompt:** "Which applications does [user email] own?"

**What it does:** Lists all applications and service principals owned by a specific user.

**Required permissions:**`User.Read.All`, `Application.Read.All`

**Prompt:** "Who owns [application name]?"

**What it does:** Retrieves the owner information for a specific application.

**Required permission:**`Application.Read.All`

## Security and compliance

### Multi-factor authentication (MFA)

**Prompt:** "Is MFA enabled for all administrators?"

**What it does:** Checks security defaults and Conditional Access policies that enforce MFA for admin roles.

**Required permission:**`Policy.Read.All`

**Prompt:** "Show me the MFA registration status for all users"

**What it does:** Lists which authentication methods users have registered and whether they're MFA-capable.

**Required permission:**`AuditLog.Read.All`

**Prompt:** "Which Conditional Access policies require MFA?"

**What it does:** Lists enabled Conditional Access policies that include MFA as a grant control.

**Required permission:**`Policy.Read.All`

**Prompt:** "Show me recent sign-ins that used MFA"

**What it does:** Retrieves sign-in logs where multi-factor authentication was required and completed.

**Required permission:**`AuditLog.Read.All`

### Conditional access policies

**Prompt:** "List all enabled Conditional Access policies"

**What it does:** Retrieves Conditional Access policies that are currently active.

**Required permission:**`Policy.Read.All`

**Prompt:** "What authentication contexts are defined in my tenant?"

**What it does:** Lists custom authentication context class references used in Conditional Access.

**Required permission:**`AuthenticationContext.Read.All`

### Risk and identity protection

**Prompt:** "Show me users flagged as risky"

**What it does:** Lists users with active risk detections from Microsoft Entra ID Protection.

**Required permission:**`IdentityRiskyUser.Read.All`

**Prompt:** "List recent identity risk events"

**What it does:** Retrieves recent risk detections such as anonymous IP usage, atypical travel, or leaked credentials.

**Required permission:**`IdentityRiskEvent.Read.All`

**Prompt:** "Show me risky service principals"

**What it does:** Lists service principals with suspicious activity detected.

**Required permission:**`IdentityRiskyServicePrincipal.Read.All`

### Audit and monitoring

**Prompt:** "Show me recent directory changes"

**What it does:** Retrieves recent audit log entries for directory modifications.

**Required permission:**`AuditLog.Read.All`

**Prompt:** "Who changed [user email]'s password?"

**What it does:** Finds audit log entries for password reset operations on a specific user.

**Required permission:**`AuditLog.Read.All`

**Prompt:** "List recent changes to [group name]"

**What it does:** Shows audit log entries for modifications to a specific group.

**Required permission:**`AuditLog.Read.All`

## License management

**Prompt:** "What licenses are available in my tenant?"

**What it does:** Lists all subscribed SKUs with their capability status.

**Required permission:**`LicenseAssignment.Read.All`

**Prompt:** "How many licenses are unassigned?"

**What it does:** Shows the difference between purchased and consumed licenses for each SKU.

**Required permission:**`LicenseAssignment.Read.All`

**Prompt:** "Which users have [license name] assigned?"

**What it does:** Lists users with a specific license SKU assigned.

**Required permissions:**`User.Read.All`, `LicenseAssignment.Read.All`

## Device management

**Prompt:** "How many devices are registered in my tenant?"

**What it does:** Counts all devices in Microsoft Entra.

**Required permission:**`Device.Read.All`

**Prompt:** "List all Windows devices"

**What it does:** Retrieves devices where the operating system is Windows.

**Required permission:**`Device.Read.All`

**Prompt:** "Show me devices that haven't checked in recently"

**What it does:** Identifies potentially inactive or orphaned device registrations.

**Required permission:**`Device.Read.All`

**Prompt:** "Which devices does [user email] own?"

**What it does:** Lists devices registered to a specific user.

**Required permissions:**`User.Read.All`, `Device.Read.All`

## Role assignments and privileged access

**Prompt:** "List all Global Administrators"

**What it does:** Shows users assigned to the Global Administrator role.

**Required permission:**`RoleManagement.Read.Directory`

**Prompt:** "Which roles is [user email] assigned to?"

**What it does:** Lists all directory role assignments for a specific user.

**Required permissions:**`User.Read.All`, `RoleManagement.Read.Directory`

**Prompt:** "Show me active Privileged Identity Management (PIM) assignments"

**What it does:** Lists time-bounded role assignments through PIM that are currently active.

**Required permission:**`RoleAssignmentSchedule.Read.Directory`

**Prompt:** "Who is eligible for the [role name] role?"

**What it does:** Shows users with eligible (not active) PIM assignments for a specific role.

**Required permissions:**`RoleEligibilitySchedule.Read.Directory`, `RoleManagement.Read.Directory`

## Administrative units

**Prompt:** "List all administrative units"

**What it does:** Retrieves all administrative units configured in your tenant.

**Required permission:**`AdministrativeUnit.Read.All`

**Prompt:** "Which users are in the [administrative unit name]?"

**What it does:** Lists members of a specific administrative unit.

**Required permission:**`AdministrativeUnit.Read.All`

**Prompt:** "Show me restricted management administrative units"

**What it does:** Lists administrative units with the restricted management feature enabled.

**Required permission:**`AdministrativeUnit.Read.All`

## Identity governance

### Access reviews

**Prompt:** "List all active access reviews"

**What it does:** Shows ongoing access reviews for groups, applications, or roles.

**Required permission:**`AccessReview.Read.All`

**Prompt:** "Which access reviews are overdue?"

**What it does:** Identifies access reviews that haven't been completed by their due date.

**Required permission:**`AccessReview.Read.All`

### Entitlement management

**Prompt:** "List all access packages"

**What it does:** Retrieves access packages configured for entitlement management.

**Required permission:**`EntitlementManagement.Read.All`

**Prompt:** "Show me pending access package requests"

**What it does:** Lists access package assignment requests awaiting approval.

**Required permission:**`EntitlementManagement.Read.All`

## Organization and domain information

**Prompt:** "What is my tenant ID?"

**What it does:** Retrieves your organization's tenant identifier.

**Required permission:**`User.Read` (one of the required permissions)

**Prompt:** "List all verified domains in my tenant"

**What it does:** Shows all domains associated with your organization and their verification status.

**Required permission:**`Domain.Read.All`

**Prompt:** "Show me my tenant's contact information"

**What it does:** Retrieves organization details including technical contacts.

**Required permission:**`Organization.Read.All`

## Reports and insights

**Prompt:** "Show me directory recommendations"

**What it does:** Lists Microsoft Entra recommendations for improving your tenant's security and configuration. This prompt uses the Microsoft Graph beta endpoint.

**Required permission:**`DirectoryRecommendations.Read.All`

**Prompt:** "What are the high-priority security recommendations?"

**What it does:** Filters recommendations by priority level. This prompt uses the Microsoft Graph beta endpoint.

**Required permission:**`DirectoryRecommendations.Read.All`

**Prompt:** "Show me recent audit log activity"

**What it does:** Retrieves recent directory audit log entries to monitor administrative actions and changes in your tenant.

**Required permission:**`AuditLog.Read.All`

## Synchronization and provisioning

**Prompt:** "Show me provisioning logs for [application name]"

**What it does:** Retrieves provisioning activity for automated user provisioning to applications.

**Required permissions:**`AuditLog.Read.All`, `Directory.Read.All`

**Prompt:** "Show me sync service audit logs"

**What it does:** Retrieves audit log entries for synchronization service activities.

**Required permission:**`AuditLog.Read.All`

**Prompt:** "Show me recent provisioning errors"

**What it does:** Identifies failed provisioning attempts with error details.

**Required permissions:**`AuditLog.Read.All`, `Directory.Read.All`

## Write actions

These prompts change data in your tenant. Before the MCP server calls Microsoft Graph, it asks you to confirm each change. Write actions work only in MCP clients that support elicitation on MCP protocol version 2026-07-28. For the list, see [Supported clients](get-started#supported-clients). Try these prompts on test accounts and groups before you use them on production objects. To find users and groups by name or email, the agent also needs read permissions such as `User.ReadBasic.All` and `Group.Read.All`. Before you confirm a change, check the object it targets in the confirmation prompt.

### Users

**Prompt:** "Create a user account for [display name] with the user principal name [user principal name]"

**What it does:** Creates a user account. The agent asks for required values that the prompt doesn't include, including an initial password. Your AI client might store the conversation, so don't type a password that you use elsewhere. Ask the agent to set a temporary password that the user must change at first sign-in.

**Required permission:**`User.Create`

**Required role:** User Administrator

**Prompt:** "Change the job title of [user email] to [job title]"

**What it does:** Updates a property on a user account.

**Required permission:**`User.ReadUpdate.All`

**Required role:** User Administrator

**Prompt:** "Disable the account for [user email]"

**What it does:** Sets `accountEnabled` to false so the user can't sign in.

**Required permissions:**`User.EnableDisableAccount.All`, `User.Read.All`

**Required role:** User Administrator for non-admin users. Disabling an administrator requires a higher role, such as Privileged Authentication Administrator.

### Groups

**Prompt:** "Add [user email] to [group name]"

**What it does:** Adds a user as a member of a group.

**Required permissions:**`GroupMember.ReadWrite.All`, `User.ReadBasic.All`

**Required role:** Groups Administrator, or owner of the group

To add members to a role-assignable group, the app also needs `RoleManagement.ReadWrite.Directory`, and the user needs at least the Privileged Role Administrator role.

**Prompt:** "Create a security group named [group name]"

**What it does:** Creates a security group.

**Required permission:**`Group.ReadWrite.All`

**Required role:** Groups Administrator

**Prompt:** "Delete the group [group name]"

**What it does:** Deletes a group.

**Required permission:**`Group.ReadWrite.All`

**Required role:** Groups Administrator

To delete a role-assignable group, the app also needs `RoleManagement.ReadWrite.Directory`, and the user must be the group's creator or have at least the Privileged Role Administrator role.

## Tips for effective prompts

- **Be specific**: Include user emails, group names, or other identifiers when asking about specific resources.
- **Use natural language**: You don't need to know Graph API syntax. Ask questions as you would ask a colleague.
- **Chain queries**: After getting results, you can ask follow-up questions like "Show me more details about the first user" or "When did they last sign in?"
- **Check the API calls**: Review the Microsoft Graph API calls that the MCP server generates, and reuse them in your own automation.
- **Combine scenarios**: Try multi-step questions like "List all inactive users who have licenses assigned and are not administrators."

## Scope

- Microsoft Entra data supports read and write prompts.
- Microsoft Intune data supports read prompts only, and the Intune reporting APIs aren't supported.
- Microsoft 365 APIs, such as mail, files, and Teams, aren't supported. For those, use [Work IQ MCP](/en-us/microsoft-365/copilot/extensibility/work-iq/mcp/overview).