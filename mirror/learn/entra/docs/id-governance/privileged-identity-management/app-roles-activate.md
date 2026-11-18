---
layout: Conceptual
title: Activate app roles in PIM (preview) - Microsoft Entra ID Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/app-roles-activate
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: kenwith
ms.author: kenwith
ms.service: entra-id-governance
ms.subservice: privileged-identity-management
manager: dougeby
description: Learn how to activate and deactivate app roles, view request status, and cancel pending requests in Microsoft Entra Privileged Identity Management.
ms.topic: how-to
ms.date: 2026-10-29T00:00:00.0000000Z
ms.custom: pim, msecd-doc-authoring-1031
ai-usage: ai-generated
locale: en-us
document_id: 0f9110f0-bcba-113e-12f4-353dea850228
document_version_independent_id: 0f9110f0-bcba-113e-12f4-353dea850228
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/id-governance/privileged-identity-management/app-roles-activate.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: id-governance/privileged-identity-management/app-roles-activate
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/id-governance/privileged-identity-management/app-roles-activate.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac4b7417-d4c2-43d4-94bf-f22fa1416b34
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68876bab-7da4-4e70-b295-395b3a255a1f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 24da1e26-dea7-2d2c-546b-eead44a2edbd
---

# Activate app roles in PIM (preview) - Microsoft Entra ID Governance | Microsoft Learn

Microsoft Entra Privileged Identity Management (PIM) for app roles is in preview. Follow the steps in this article to activate an eligible app role, view or cancel a pending request, and deactivate a role when you finish your work.

## Prerequisites

- A Microsoft Entra ID Governance license.
- An eligible app role assignment, either assigned directly or through a group. For information about assignments, see [Assign app roles in PIM](app-roles-assign).

## Activate a role

When you need to take on an app role, you can request activation by using the **My roles** navigation option in PIM. The [app role's settings](app-roles-settings) determine the requirements for activation.

If your eligibility comes from a group's eligible app role assignment, you activate the role for yourself. Your activation doesn't activate the role for the whole group or its other members.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
2. Browse to **ID Governance** &gt; **Privileged Identity Management** &gt; **App Roles (Preview)**, and select the application.
3. Select **My roles** &gt; **Eligible assignments**, and review the list of app roles that you're eligible to activate.
4. Select **Activate** for the eligible assignment you want to activate.
5. Depending on the application's role settings, you might be asked to provide multifactor authentication or another form of credential. Follow the instructions to complete the required verification.
6. On the **Activate** tab, select **Custom activation start time** if you need to schedule activation. Enter **Start time** and select the time zone.
7. Set **Duration (hours)** using the slider or numeric field, within the maximum configured for the role.
8. Depending on the application's role settings, justification for activation might be required. If needed, provide the justification in **Reason (max 500 characters)**.
9. Select **Activate** to submit the request.
10. Review the request status.

    The **Status** tab shows progress through request processing, validation, and completion. Wait for the stages to finish. The status panel indicates that the PIM page refreshes automatically after completion.

If the [role requires approval](app-roles-approval-workflow) to activate, use **Pending requests** to view the status of your request while it awaits review. The request list shows **Pending approval** for a request awaiting a decision.

After activation, select **My roles** &gt; **Active assignments** to review your active app roles. An activated assignment shows **Activated** in the **State** column and its **End time**.

Before using the activated role in the application, the application must obtain a new token. Follow the application's sign-in instructions if another sign-in is needed, and then perform the tasks that require the role. The PIM page's automatic refresh doesn't replace token acquisition by the application.

## View the status of your requests

You can view the status of your pending activation requests. Check the status when your requests require another person's approval.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
2. Browse to **ID Governance** &gt; **Privileged Identity Management** &gt; **App Roles (Preview)**, and select the application.
3. Select **Pending requests**.
4. Review the list of requests, including the reason and status for each request.

To review your assignments rather than pending requests, select **My roles**. Use the **Eligible assignments**, **Active assignments**, and **Expired assignments** tabs to view the corresponding assignments for the application.

## Cancel a pending request

If you no longer need to activate a role that requires approval, you can cancel the pending request.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
2. Browse to **ID Governance** &gt; **Privileged Identity Management** &gt; **App Roles (Preview)**, and select the application.
3. Select **Pending requests**.
4. For the request that you want to cancel, select **Cancel**.

To activate the role after canceling the pending request, submit a new activation request.

## Deactivate a role

If you no longer need an activated app role assignment, you can deactivate it before the activation expires.

Important

Deactivation or expiration doesn't automatically invalidate already-issued tokens or existing application sessions. Application access can persist according to token lifetime and the application's session and authorization behavior. Ending an activation in PIM isn't a guarantee of immediate access removal in the application.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
2. Browse to **ID Governance** &gt; **Privileged Identity Management** &gt; **App Roles (Preview)**, and select the application.
3. Select **My roles** &gt; **Active assignments**.
4. Find the assignment with **State** set to **Activated** that you want to deactivate, and select **Deactivate**.
5. In the **Deactivate** panel, review **Resource name**, **Role**, **Scope**, **Member**, **Start time**, and **End time** to confirm the activation.
6. Select **Deactivate** to submit the request, or **Cancel** to close the panel without submitting.

    Note

    If PIM reports **Deactivate role failed** because the active duration is too short and the minimum required is five minutes, wait until the activation has been active for at least five minutes before retrying. A failed deactivation doesn't end the activation.
7. Review the result, and then check **Active assignments** to verify that the activation has ended. If PIM reports a failure, don't treat the request as a completed deactivation.

Deactivation ends the activation, not your eligible assignment. You can request activation again while your eligible assignment remains valid.