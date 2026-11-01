---
layout: Conceptual
title: Get started with privileged access management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/privileged-access-management-configuration
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Microsoft Purview privileged access management helps you control and audit elevated permissions in Microsoft 365. Follow our guide to get started now.
keywords: Microsoft 365, Microsoft Purview, compliance, privileged access management
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2023-08-20T00:00:00.0000000Z
audience: Admin
ms.topic: overview
ms.service: purview
ms.subservice: purview-privileged-access-management
search.appverid:
- MET150
ms.collection:
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- highpri
ms.custom:
- Ent_Solutions
- seo-marvel-apr2020
- admindeeplinkMAC
ms.assetid: 
ai-usage: ai-assisted
locale: en-us
document_id: fd2b58bc-14e8-c26a-2705-4e1eebeb5c86
document_version_independent_id: fd2b58bc-14e8-c26a-2705-4e1eebeb5c86
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/privileged-access-management-configuration.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: privileged-access-management-configuration
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/privileged-access-management-configuration.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 5af3fbfa-bdf3-ec99-4659-9b63dd94d2b7
---

# Get started with privileged access management | Microsoft Learn

This article guides you through enabling and configuring privileged access management in your organization. You can use either the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) or Exchange Management PowerShell to manage and use privileged access.

## Before you begin

Before you get started with privileged access management, confirm your [Microsoft 365 subscription](https://www.microsoft.com/microsoft-365/compare-all-microsoft-365-plans) and any add-ons.

To access and use privileged access management, your organization must have supporting subscriptions or add-ons. For more information, see the [subscription requirements](https://aka.ms/M365EnterprisePlans) for privileged access management.

If you don't have an existing Microsoft 365 Enterprise E5 plan and want to try privileged access management, you can [add Microsoft 365](/en-us/microsoft-365/commerce/try-or-buy-microsoft-365) to your existing Microsoft 365 subscription or [sign up for a trial](https://www.microsoft.com/microsoft-365/enterprise) of Microsoft 365 Enterprise E5.

## Enable and configure privileged access management

Complete the following steps to set up and use privileged access in your organization:

- [Step 1: Create an approver's group](privileged-access-management-configuration#step1)

    Before you start using privileged access, determine who needs approval authority for incoming requests for access to elevated and privileged tasks. Any user who is part of the Approvers' group can approve access requests. Enable this group by creating a mail-enabled security group in Microsoft 365.
- [Step 2: Enable privileged access](privileged-access-management-configuration#step2)

    Explicitly enable privileged access in Microsoft 365 with the default approver group, including a set of system accounts that you want to exclude from the privileged access management access control.
- [Step 3: Create an access policy](privileged-access-management-configuration#step3)

    Define specific approval requirements scoped at individual tasks by creating an approval policy. The approval type options are **Auto** or **Manual**.
- [Step 4: Submit and approve privileged access requests](privileged-access-management-configuration#step4)

    After you enable privileged access, it requires approvals for any task that has an associated approval policy defined. For tasks included in an approval policy, users must request and be granted access approval to have permissions necessary to execute the task.

After approval is granted, the requesting user can execute the intended task. Privileged access authorizes and executes the task on behalf of the user. The approval remains valid for the requested duration (the default duration is four hours), during which the requester can execute the intended task multiple times. All such executions are logged and made available for security and compliance auditing.

Note

To use Exchange Management PowerShell to enable and configure privileged access, follow the steps in [Connect to Exchange Online PowerShell using Multi-Factor authentication](/en-us/powershell/exchange/connect-to-exchange-online-powershell#connect-to-exchange-online-powershell-using-mfa) to connect to Exchange Online PowerShell with your Microsoft 365 credentials. You don't need to enable multi-factor authentication for your organization to use the steps to enable privileged access while connecting to Exchange Online PowerShell. Connecting with multi-factor authentication creates an auth token that privileged access uses for signing your requests.

## Step 1: Create an approver's group

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) with credentials for an admin account in your organization.
2. In the admin center, go to [**Groups**](https://go.microsoft.com/fwlink/p/?linkid=2052855) &gt; **Add a group**.
3. Select **mail-enabled security group** and then enter the **Name**, **Group email address**, and **Description** for the new group.
4. Save the group. It might take a few minutes for the group to be fully configured and to appear in the Microsoft 365 admin center.
5. Select the new approvers group and select **edit** to add users to the group.
6. Save the group.

## Step 2: Enable privileged access

### In the Microsoft 365 admin center

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) with credentials for an admin account in your organization.
2. In the admin center, go to **Settings** &gt; **Org Settings** &gt; [**Security & Privacy**](https://go.microsoft.com/fwlink/p/?linkid=2072756) &gt; **Privileged access**.
3. Turn on **Require approvals for privileged tasks**.
4. Assign the approvers group you created in Step 1 as the **Default approvers group**.
5. **Save** and **Close**.

### In Exchange Management PowerShell

To enable privileged access and assign the approver group, run the following command in Exchange Online PowerShell:

```PowerShell
Enable-ElevatedAccessControl -AdminGroup '<default approver group>' -SystemAccounts @('<systemAccountUPN1>','<systemAccountUPN2>')
```

Example:

```PowerShell
Enable-ElevatedAccessControl -AdminGroup 'pamapprovers@fabrikam.onmicrosoft.com' -SystemAccounts @('sys1@fabrikamorg.onmicrosoft.com', 'sys2@fabrikamorg.onmicrosoft.com')
```

Note

The system accounts feature ensures that certain automations within your organizations work without privileged access. However, make such exclusions exceptional and regularly approve and audit those allowed.

## Step 3: Create an access policy

You can create and configure up to 30 privileged access policies for your organization.

### In the Microsoft 365 admin center

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) with credentials for an admin account in your organization.
2. In the Admin Center, go to **Settings** &gt; **Org Settings** &gt; [**Security & Privacy**](https://go.microsoft.com/fwlink/p/?linkid=2072756)\*\* &gt; **Privileged access**.
3. Select **Manage access policies and requests**.
4. Select **Configure policies** and select **Add a policy**.
5. From the drop-down fields, select the appropriate values for your organization:

    - **Policy type**: Task, Role, or Role Group
    - **Policy scope**: Exchange
    - **Policy name**: Select from the available policies
    - **Approval type**: Manual or Auto
    - **Approval group**: Select the approvers group created in Step 1
6. Select **Create** and then **Close**. It might take a few minutes for the policy to be fully configured and enabled.

### In Exchange Management PowerShell

To create and define an approval policy, run the following command in Exchange Online PowerShell:

```PowerShell
New-ElevatedAccessApprovalPolicy -Task 'Exchange\<exchange management cmdlet name>' -ApprovalType <Manual, Auto> -ApproverGroup '<default/custom approver group>'
```

Example:

```PowerShell
New-ElevatedAccessApprovalPolicy -Task 'Exchange\New-MoveRequest' -ApprovalType Manual -ApproverGroup 'mbmanagers@fabrikamorg.onmicrosoft.com'
```

## Step 4: Submit or approve privileged access requests

### Request elevation authorization to execute privileged tasks

Requests for privileged access are valid for up to 24 hours after submission. If approvers don't approve or deny the request within 24 hours, the request expires and access isn't granted.

#### In the Microsoft 365 Admin Center

1. Sign in to the [Microsoft 365 Admin Center](https://go.microsoft.com/fwlink/p/?linkid=2024339) with your credentials.
2. In the Admin Center, go to **Settings** &gt; **Org Settings** &gt; [**Security & Privacy**](https://go.microsoft.com/fwlink/p/?linkid=2072756)\*\* &gt; **Privileged access**.
3. Select **Manage access policies and requests**.
4. Select **New request**. From the drop-down fields, select the appropriate values for your organization:

    - **Request type**: Task, Role, or Role Group
    - **Request scope**: Exchange
    - **Request for**: Select from the available policies
    - **Duration (hours)**: Number of hours of requested access. You can request any number of hours.
    - **Comments**: Text field for comments related to your access request
5. Select **Save** and then **Close**. The system sends your request to the approver group by email.

#### In Exchange Management PowerShell

Run the following command in Exchange Online PowerShell to create and submit an approval request to the approver group:

```PowerShell
New-ElevatedAccessRequest -Task 'Exchange\<exchange management cmdlet name>' -Reason '<appropriate reason>' -DurationHours <duration in hours>
```

Example:

```PowerShell
New-ElevatedAccessRequest -Task 'Exchange\New-MoveRequest' -Reason 'Attempting to fix the user mailbox error' -DurationHours 4
```

### View status of elevation requests

After you create an approval request, you can check the status of the elevation request in the admin center or in Exchange Management PowerShell by using the associated request ID.

#### In the Microsoft 365 admin center

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) with your credentials.
2. In the admin center, go to **Settings** &gt; **Org Settings** &gt; [**Security & Privacy**](https://go.microsoft.com/fwlink/p/?linkid=2072756) &gt; **Privileged access**.
3. Select **Manage access policies and requests**.
4. Select **View** to filter submitted requests by **Pending**, **Approved**, **Denied**, or **Customer Lockbox** status.

#### In Exchange Management PowerShell

Run the following command in Exchange Online PowerShell to view an approval request status for a specific request ID:

```PowerShell
Get-ElevatedAccessRequest -Identity <request ID> | select RequestStatus
```

Example:

```PowerShell
Get-ElevatedAccessRequest -Identity 28560ed0-419d-4cc3-8f5b-603911cbd450 | select RequestStatus
```

### Approving an elevation authorization request

When you create an approval request, members of the relevant approver group receive an email notification. They can approve the request by using the request ID. The requestor receives an email notification when you approve or deny the request.

#### In the Microsoft 365 admin center

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) with your credentials.
2. In the admin center, go to **Settings** &gt; **Org Settings** &gt; [**Security & Privacy**](https://go.microsoft.com/fwlink/p/?linkid=2072756) &gt; **Privileged access**.
3. Select **Manage access policies and requests**.
4. Select a listed request to view the details and take action on the request.
5. Select **Approve** to approve the request or select **Deny** to deny the request. You can revoke access for previously approved requests by selecting **Revoke**.

#### In Exchange Management PowerShell

To approve an elevation authorization request, run the following command in Exchange Online PowerShell:

```PowerShell
Approve-ElevatedAccessRequest -RequestId <request id> -Comment '<approval comment>'
```

Example:

```PowerShell
Approve-ElevatedAccessRequest -RequestId a4bc1bdf-00a1-42b4-be65-b6c63d6be279 -Comment '<approval comment>'
```

To deny an elevation authorization request, run the following command in Exchange Online PowerShell:

```PowerShell
Deny-ElevatedAccessRequest -RequestId <request id> -Comment '<denial comment>'
```

Example:

```PowerShell
Deny-ElevatedAccessRequest -RequestId a4bc1bdf-00a1-42b4-be65-b6c63d6be279 -Comment '<denial comment>'
```

## Delete a privileged access policy in Microsoft 365

If your organization no longer needs a privileged access policy, you can delete it.

### In the Microsoft 365 admin center

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) with credentials for an admin account in your organization.
2. In the admin center, go to **Settings** &gt; **Org Settings** &gt; [**Security & Privacy**](https://go.microsoft.com/fwlink/p/?linkid=2072756) &gt; **Privileged access**.
3. Select **Manage access policies and requests**.
4. Select **Configure policies**.
5. Select the policy you want to delete, and then select **Remove Policy**.
6. Select **Close**.

### In Exchange Management PowerShell

To delete a privileged access policy, run the following command in Exchange Online PowerShell:

```PowerShell
Remove-ElevatedAccessApprovalPolicy -Identity <identity GUID of the policy you want to delete>
```

## Disable privileged access in Microsoft 365

If needed, you can disable privileged access management for your organization. Disabling privileged access doesn't delete any associated approval policies or approver groups.

### In the Microsoft 365 admin center

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) with credentials for an admin account in your organization.
2. In the Admin Center, go to **Settings** &gt; **Org Settings** &gt; [**Security & Privacy**](https://go.microsoft.com/fwlink/p/?linkid=2072756)\*\* &gt; **Privileged access**.
3. Turn on **Require approvals for privileged access**.

### In Exchange Management PowerShell

To disable privileged access, run the following command in Exchange Online PowerShell:

```PowerShell
Disable-ElevatedAccessControl
```