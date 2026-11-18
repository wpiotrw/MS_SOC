---
layout: Conceptual
title: Approve or deny app role requests in PIM (preview) - Microsoft Entra ID Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/app-roles-approval-workflow
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: kenwith
ms.author: kenwith
ms.service: entra-id-governance
ms.subservice: privileged-identity-management
manager: dougeby
description: Learn how to view, approve, and deny app role activation and assignment renewal or extension requests in Microsoft Entra Privileged Identity Management.
ms.topic: how-to
ms.date: 2026-10-29T00:00:00.0000000Z
ms.custom: pim, msecd-doc-authoring-1031
ai-usage: ai-generated
locale: en-us
document_id: 2dd21911-3a66-cc51-eadd-737d910bbb99
document_version_independent_id: 2dd21911-3a66-cc51-eadd-737d910bbb99
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/id-governance/privileged-identity-management/app-roles-approval-workflow.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: id-governance/privileged-identity-management/app-roles-approval-workflow
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/id-governance/privileged-identity-management/app-roles-approval-workflow.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: bb893bee-c43b-5fd3-28c1-4323ead37aa1
---

# Approve or deny app role requests in PIM (preview) - Microsoft Entra ID Governance | Microsoft Learn

Microsoft Entra Privileged Identity Management (PIM) for app roles is in preview. Follow the steps in this article to approve or deny requests for app role activation and assignment renewal or extension.

## Overview

Microsoft Entra Privileged Identity Management (PIM) enables you to configure app roles so that they require approval for activation, and choose users or groups from your Microsoft Entra organization as delegated approvers. Configure delegated approvers in the application's [role settings](app-roles-settings).

For activation requests, being designated as an approver in the app role's settings is sufficient to approve or deny requests. You don't need an additional administrative role.

For assignment extension and renewal requests, you must own the target service principal or have one of the administrative roles listed in [Permissions for app role assignments](app-roles-assign#permissions) to approve or deny requests.

For the requester's workflow, see [Activate app roles in PIM](app-roles-activate) and [Extend or renew app role assignments in PIM](app-roles-renew-extend).

## View pending requests

You can view requests pending your approval in Privileged Identity Management.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
2. Browse to **ID Governance** &gt; **Privileged Identity Management** &gt; **App Roles (Preview)**, and select the application.
3. Select **Approve requests**.

    In **Requests for role activations**, you see the activation requests pending your approval. **Requests to renew or extend role assignments** lists assignment extension and renewal requests.
4. Select **Refresh** in a request section to update its list.

If you can't find a request, check that you've selected the correct application and refresh both request sections.

## Approve requests

Follow these steps to approve a pending activation request.

1. In **Requests for role activations**, find and select the checkbox for the request that you want to approve. Select **Approve** to open the decision panel.

    Review **Request details**, including the role, requestor, resource, reason, and start and end times.
2. Enter your business justification in the required box showing **Enter the reason**.

    If the box is empty, the panel displays **Required fields are missing or invalid**, and **Submit** is unavailable.
3. Select **Submit** to approve the request.

    PIM shows **Approving** while processing the decision and **Request(s) approved successfully.** when approval succeeds.
4. After submitting the decision, select **Refresh** in **Requests for role activations** to check that the approved request is no longer listed.
5. To check the resulting PIM assignment state, open **Assignments** &gt; **Active assignments** and check for **Activated** in the **State** column for the user's app role.

An approval decision isn't confirmation that the application has started granting access. For activation status and the application-access considerations, see [Activate app roles in PIM](app-roles-activate).

## Deny requests

If a request doesn't meet your organization's access requirements, deny it and provide the business justification.

The following steps describe an activation request in **Requests for role activations**.

1. On the application's **Approve requests** page, select the checkbox for the request in **Requests for role activations**, and then select **Deny**.
2. In **Denying request(s)**, review **Request details** to confirm the request.
3. Enter your business justification in the required box showing **Enter the reason**.
4. Select **Submit** to deny the request.
5. Select **Refresh** in the request section to review the list after your decision.

## Workflow notifications

Here's some information about workflow notifications:

- Approvers are notified by email when a request for a role is pending their review. Email notifications include a direct link to the request, where the approver can approve or deny.
- Requests are resolved by the first approver who approves or denies.
- When an approver responds to the request, all approvers are notified of the action.
- Resource administrators are notified when an approved user becomes active in their role.

Note

A resource administrator who believes that an approved user shouldn't be active can remove the active role assignment in Privileged Identity Management. Although resource administrators aren't notified of pending requests unless they're an approver, they can view and cancel pending requests for all users by viewing pending requests in Privileged Identity Management.