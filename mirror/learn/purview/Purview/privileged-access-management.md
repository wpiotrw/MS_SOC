---
layout: Conceptual
title: Learn about privileged access management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/privileged-access-management
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article provides an overview about privileged access management in Microsoft Purview, including answers to frequently asked questions (FAQs).
keywords: Microsoft 365, Microsoft Purview, compliance, privileged access management
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2025-01-01T00:00:00.0000000Z
audience: Admin
ms.topic: overview
f1.keywords:
- NOCSH
ms.service: purview
ms.subservice: purview-privileged-access-management
search.appverid:
- MET150
ms.collection:
- highpri
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- highpri
ms.custom:
- Ent_Solutions
- seo-marvel-apr2020
- sfi-ga-nochange
ai-usage: ai-assisted
locale: en-us
document_id: 17032c58-a57e-6440-07c7-ef47c77d8973
document_version_independent_id: 17032c58-a57e-6440-07c7-ef47c77d8973
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/privileged-access-management.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: privileged-access-management
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/privileged-access-management.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: ed471552-dd90-6037-21ac-91a90e5f3ea0
---

# Learn about privileged access management | Microsoft Learn

Microsoft Purview Privileged Access Management provides granular access control over privileged admin tasks in Microsoft 365. It helps protect your organization from breaches that use existing privileged admin accounts with standing access to sensitive data or access to critical configuration settings. Privileged access management requires users to request just-in-time access to complete elevated and privileged tasks through a highly scoped and time-bounded approval workflow. This configuration gives users just enough access to perform the task at hand, without risking exposure of sensitive data or critical configuration settings. When you enable privileged access management, your organization operates with zero standing privileges and provides a layer of defense against standing administrative access vulnerabilities.

For a quick overview of the integrated Customer Lockbox and privileged access management workflow, see this [Customer Lockbox and privileged access management video](https://go.microsoft.com/fwlink/?linkid=2066800).

## Layers of protection

Privileged access management complements other data and access feature protections within the Microsoft 365 security architecture. Including privileged access management as part of an integrated and layered approach to security provides a security model that maximizes protection of sensitive information and Microsoft 365 configuration settings. As shown in the diagram, privileged access management builds on the protection provided by native encryption of Microsoft 365 data and the role-based access control security model of Microsoft 365 services. When used with [Microsoft Entra Privileged Identity Management](/en-us/azure/active-directory/active-directory-privileged-identity-management-configure), these two features provide access control with just-in-time access at different scopes.

![Layered protection in Microsoft 365.](media/pam-layered-protection.png)

Privileged access management is defined and scoped at the **task** level, while Microsoft Entra Privileged Identity Management applies protection at the **role** level with the ability to execute multiple tasks. Microsoft Entra Privileged Identity Management primarily manages accesses for AD roles and role groups, while Microsoft Purview Privileged Access Management applies only at the task level.

- **Enable privileged access management while already using Microsoft Entra Privileged Identity Management:** Adding privileged access management provides another granular layer of protection and audit capabilities for privileged access to Microsoft 365 data.
- **Enable Microsoft Entra Privileged Identity Management while already using Microsoft Purview Privileged Access Management:** Adding Microsoft Entra Privileged Identity Management to Microsoft Purview Privileged Access Management can extend privileged access to data outside of Microsoft 365 that's primarily defined by user roles or identity.

## Privileged access management architecture and process flow

Each of the following process flows outlines the architecture of privileged access and how it interacts with the Microsoft 365 substrate, auditing, and the Exchange Management runspace.

### Step 1: Configure a privileged access policy

When you configure a privileged access policy with the [Microsoft 365 admin center](https://admin.microsoft.com) or the Exchange Management PowerShell, you define the policy and the privileged access feature processes and the policy attributes in the Microsoft 365 substrate. The system logs the activities in the audit log. The policy is now enabled and ready to handle incoming requests for approvals.

![Step 1: Policy creation.](media/pam-step1-policy-creation.jpg)

### Step 2: Access request

In the [Microsoft 365 admin center](https://admin.microsoft.com) or by using Exchange Management PowerShell, users can request access to elevated or privileged tasks. The privileged access feature sends the request to the Microsoft 365 substrate for processing against the configured privileged access policy and records the activity in the audit logs.

![Step 2: Access request.](media/pam-step2-access-request.jpg)

### Step 3: Access approval

The privileged access feature generates an approval request and sends a pending request notification to approvers by email. If approvers grant approval, the privileged access feature processes the privileged access request as an approval and makes the task ready to complete. If approvers deny the request, the privileged access feature blocks the task and grants no access to the requestor. The requestor receives an email message that notifies them of the request approval or denial.

![Step 3: Access approval.](media/pam-step3-access-approval.jpg)

### Step 4: Access processing

For an approved request, the Exchange Management runspace processes the task. The Microsoft 365 substrate checks the approval against the privileged access policy and processes it. The audit logs record all activity for the task.

![Step 4: Access processing.](media/pam-step4-access-processing.jpg)

## Frequently asked questions

### What SKUs can use privileged access in Microsoft 365?

You can use privileged access management with a wide selection of Microsoft 365 and Microsoft 365 subscriptions and add-ons. For details, see [Get started with privileged access management](privileged-access-management-configuration).

### When will privileged access management support Microsoft 365 workloads beyond Exchange?

For more information about the timeline for privileged access management support, see the [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap).

### My organization needs more than 30 privileged access policies. Will this limit be increased?

Yes, Microsoft is working on increasing the current limit of 30 privileged access policies per organization.

### Do I need to be a Global Admin to manage privileged access in Microsoft 365?

Yes, you need the *Global Admin* role assigned to accounts that manage privileged access in Microsoft 365. Users included in an approvers' group don't need to have the *Global Admin* or *Role Management* roles assigned to review and approve requests by using PowerShell. Users must have the *Exchange Administrator* role assigned to request, review, and approve privileged access requests in the Microsoft 365 admin center.

### How is privileged access management related to Customer Lockbox?

[Customer Lockbox](/en-us/office365/admin/manage/customer-lockbox-requests) provides access control for organizations when Microsoft accesses data. Privileged access management provides granular access control within an organization for all Microsoft 365 privileged tasks.

## Ready to get started?

Start [configuring your organization for privileged access management](privileged-access-management-configuration).

## Learn more

[Interactive guide: Monitor and control administrator tasks with privileged access management](https://content.cloudguides.com/guides/Privileged%20Access%20Management)