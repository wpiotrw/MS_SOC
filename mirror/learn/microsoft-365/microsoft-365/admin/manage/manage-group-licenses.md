---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Assign or unassign licenses to a group in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-group-licenses?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords: NOCSH
author: cmcatee-MSFT
ms.author: cmcatee
manager: scotv
ms.reviewer: shegu, jobailey
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-business
ms.subservice: m365-commerce-acquisition
ms.localizationpriority: medium
ms.collection:
- M365-subscription-management
- Adm_O365
ms.custom:
- commerce_licensing
- admindeeplinkMAC
- m365-groups
- user-accounts
search.appverid: MET150
description: Learn how to assign or unassign licenses to groups in the Microsoft 365 admin center.
ms.date: 2026-05-18T00:00:00.0000000Z
locale: en-us
document_id: 5ff73fa2-00b2-2cd8-93b0-8dd4504a638d
document_version_independent_id: 5ff73fa2-00b2-2cd8-93b0-8dd4504a638d
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/manage-group-licenses.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/manage-group-licenses
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/manage-group-licenses.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: dd547f68-e051-1b66-2aa0-dccf0218e5cb
---

# Assign or unassign licenses to a group in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn

If you have security groups, mail-enabled groups, or Microsoft 365 groups, you can assign or unassign licenses for those groups on the **Licenses** page in the Microsoft 365 admin center. We refer to this as *group-based licensing*.

Note

Some Microsoft services aren't available in all locations. Before a license can be assigned to a user, the administrator must specify the user's location setting. For group-based licensing, any users without a specific location inherit the location of the tenant. If you have users in multiple locations, set the user location as part of your user creation flow. For more information, see [Add users and assign licenses in Microsoft 365](assign-licenses-to-users).

## Before you begin

- You must be at least a Groups Administrator, License Administrator, or User Administrator to assign licenses.
- In addition to the steps described in this article, you can also use the Microsoft Graph PowerShell SDK to assign or unassign Microsoft 365 licenses to groups. For more information, see [Set-MgGroupLicense](/en-us/powershell/module/microsoft.graph.groups/set-mggrouplicense).
- Group-based licensing doesn't currently support nested groups (groups that contain other groups). If you assign licenses to a nested group, only users in the first-level group are assigned licenses.
- When you assign or modify licenses for a large group, like 100,000 users, it can affect performance. In certain high load situations, it might take a long time to process license changes for groups or membership changes to groups with existing licenses.

## Limitations of group-based licensing in the Microsoft 365 admin center

- You can assign licenses to a maximum of 20 groups at a time.
- When you select **Reprocess** to resolve issues with group license assignment, the feature attempts to reprocess licenses up to a maximum of 20 users at a time.
- The lists of users who were and who weren't successfully assigned licenses are paginated lists that display 999 users at a time. You must scroll to the bottom of the list to load the next set of users.

## Assign licenses to a group

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) as at least a License Administrator.
2. Go to the **Billing** &gt; [Licenses](https://go.microsoft.com/fwlink/p/?linkid=842264) page.
3. On the **Licenses** page, select **Assign licenses**.
4. In the side panel, search for the group that you want to assign licenses to, then select the name from the dropdown list.
5. Select the subscription that the assigned licenses should come from.
6. To assign or remove access to specific items, select **Turn apps and services on or off**.
7. When you're finished, select **Assign licenses**.

## Unassign licenses from a group

1. In the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339), go to **Billing** &gt; [Licenses](https://go.microsoft.com/fwlink/p/?linkid=842264).
2. Select the product that you want to unassign licenses for.
3. On the product details page, find the group in the list.
4. Select the three dots (more actions) on the group's row, and then select **Unassign**.
5. In the confirmation dialog, select **Unassign**.

## Move users between licensed groups

When you move a user from one licensed group to another, the order of operations matters. If you remove a user from a group before you add them to the new one, the user might experience a brief loss of access to licensed services while group-based licensing finishes processing the new assignment. However, you can prevent this temporary loss of access. To move a user between licensed groups without service interruption, use the following steps in this order:

1. **Add** the user to the destination group first.
2. **Confirm** the new license is applied on the user's **Licenses** page.
3. **Remove** the user from the original group.

    Note

    If you remove the user from the source group first, the user is unlicensed until group-based licensing finishes processing the new group's assignment. Processing time varies based on tenant size and current load. In large tenants or during high-load periods, the temporary loss of access can last longer than expected.

## Group-based licensing errors

Group-based licensing can produce errors in the background when Azure Active Directory tries to apply licenses to users through group membership. Unlike direct user license assignment, where errors appear immediately, group-based licensing records the failure on the user object and surfaces it later in the admin portal.

### View group-based licensing errors

If you receive any errors during license assignment, you can view them on the product details page.

1. In the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339), go to **Billing** &gt; [Licenses](https://go.microsoft.com/fwlink/p/?linkid=842264).
2. Select the product that you want to view licenses for.
3. Select the **Errors & issues** tab to see a list of users who have license assignment problems.
4. Select a user to inspect what type of error they encountered.

### Find group-based licensing errors

You can resolve common causes of group-based licensing errors.

#### Find all groups with license assignment errors

1. In the [Microsoft Entra][https://entra.microsoft.com/] admin center, select **Billing** &gt; **Licenses** &gt; **Overview**.
2. If any groups have licensing errors, an information box appears.
3. Select the box to see all groups with errors.
4. Open each group for details.

#### Find license assignment errors for users in a group

1. In the [Microsoft Entra][https://entra.microsoft.com/] admin center, select **Groups**.
2. Select a group from the list where one or more users has a licensing error. If users are in an error state, a notification appears.
3. Select the notification to view affected users.
4. Select a user to see error details.

### Resolve group-based licensing errors

There are common group-based licensing error types and fixes.

#### Problems and solutions

The following table provides common group-based and user-specific licensing issues, problems, and fixes.

| Issue | Problem | Fix |
| --- | --- | --- |
| Not enough licenses | There aren’t enough available licenses for one of the products assigned to the group. | Buy more licenses, remove unused direct assignments, or free licenses from other groups or users. |
| Conflicting service plans | A service plan in one product conflicts with a service plan already assigned to the user through another product.<br>**Example:**A user has **Office 365 E1** directly assigned, and then receives **Office 365 E3** through a group. Some plans overlap or conflict, such as:<br><br>- Exchange Online Plan 1<br>- Exchange Online Plan 2 | Disable one conflicting plan, remove the redundant direct license, or adjust the group license assignment. |
| Other products depend on this license | A license or service plan can’t be removed because another assigned product depends on it.<br>**Example:**Audio Conferencing depends on Skype for Business. If a group license containing Skype for Business is removed, but the user still has Audio Conferencing directly assigned, removal can fail or the inherited license can be converted to direct. | Ensure the dependent service is removed or reassigned before removing the prerequisite. |
| Usage location isn’t allowed | Some Microsoft services aren’t available in all countries or regions. A user’s **Usage location** is either missing or set to an unsupported location. | Complete the following actions:<br>- Set the correct usage location on the user.<br>- Remove users in unsupported locations from the licensed group.<br>- Ensure user location is populated during user creation.<br><br><br>If a user has no usage location, group-based licensing uses the tenant location. |
| Duplicate proxy addresses | Exchange Online licensing can fail if two users have the same proxy address. | Correct the duplicate proxy address, then reprocess the user or group license assignment. |
| Mail and ProxyAddresses attribute changes | Updating license assignment can trigger recalculation of the user’s mail and proxyAddresses attributes. | Review how proxy addresses are populated in Azure AD / Entra ID and correct the underlying source of the change. |
| LicenseAssignmentAttributeConcurrencyException in audit logs | A user may show LicenseAssignmentAttributeConcurrencyException when multiple groups try to assign the same license concurrently. | No action required. Azure AD retries processing and resolves the issue automatically. |
| More than one product license assigned to a group | If a group has multiple products assigned, Azure AD tries to apply all of them to each user. If one product fails because of insufficient licenses, conflicts, or dependency issues, the other products in that group might not be assigned either. | Inspect the affected users and determine which product caused the failure. |
| Licensed group is deleted | Before deleting a group, all licenses assigned to it must be removed. During removal, dependency or proxy address issues can block cleanup.<br>If a user has a direct license that depends on a service plan inherited from the group, Azure AD might convert the inherited license into a direct assignment so the dependent service keeps working.<br><br>**Example:**A group has Office 365 E3/E5 with Skype for Business enabled. Some users also have Audio Conferencing directly assigned. When the group is deleted, the E3/E5 license might be converted to direct assignment for those users because Audio Conferencing depends on Skype for Business. | Check affected users for direct assignment of license. |
| Products with prerequisites or add-ons | Some products are add-ons and require a prerequisite service plan.<br>**Example:** Microsoft Workplace Analytics requires one of the following plans:<br><br>- Exchange Online Plan 1<br>- Exchange Online Plan 2<br><br><br>If you assign the add-on alone to a group, licensing fails. | Assign the prerequisite and the add-on in the same group. For example:<br>- Office 365 E3 with only Exchange Online Plan 2 enabled<br>- Microsoft Workplace Analytics<br><br><br>This lets users receive the add-on without consuming extra full-suite licenses if they already receive E3 elsewhere. |

### Force license processing

After you update your group licensing, you might need to reprocess the licenses for your tenant. Use the following methods to reprocess the licensing for a group or a user.

#### Reprocess a group or user

Use this method to reprocess the group or user after you fix a group-level or user-specific issue.

1. In the [Microsoft 365](https://admin.microsoft.com/) admin center, select **Billing** &gt; **Licenses**.
2. Select the license product that has assignment problems.
3. Select **Errors & Issues**.
4. Review the groups and users with license assignment errors and correct the underlying issue.
5. Select the affected group or user and choose **Reprocess**.