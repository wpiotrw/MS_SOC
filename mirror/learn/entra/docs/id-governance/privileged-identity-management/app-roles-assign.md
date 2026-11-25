---
layout: Conceptual
title: Assign app roles in PIM (preview) - Microsoft Entra ID Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/app-roles-assign
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: kenwith
ms.author: kenwith
ms.service: entra-id-governance
ms.subservice: privileged-identity-management
manager: dougeby
description: Learn how to assign eligible and active app roles and update or remove assignments in Microsoft Entra Privileged Identity Management.
ms.topic: how-to
ms.date: 2026-11-16T00:00:00.0000000Z
ms.custom: pim, msecd-doc-authoring-1031
ai-usage: ai-generated
locale: en-us
document_id: efbb37b9-56e5-1839-2c95-ade79bf30a9c
document_version_independent_id: efbb37b9-56e5-1839-2c95-ade79bf30a9c
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/id-governance/privileged-identity-management/app-roles-assign.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: id-governance/privileged-identity-management/app-roles-assign
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/id-governance/privileged-identity-management/app-roles-assign.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 95bc45ee-ab1b-0aa4-0653-6ef995f0dfa5
---

# Assign app roles in PIM (preview) - Microsoft Entra ID Governance | Microsoft Learn

With Microsoft Entra Privileged Identity Management (PIM), you can create eligible and active app role assignments. PIM for app roles is in preview. This article shows you how to create, update, and remove app role assignments.

## Role assignment conditions

With Microsoft Entra PIM, assignees must activate an eligible app role assignment before they can use the role. The app role's settings control activation requirements and assignment duration.

App role assignments support the following assignees:

- **Eligible** assignments support users, groups, agents, and agent identities.
- **Active** assignments support users, groups, and workload identities.

You can create permanent or time-bound assignments, subject to the app role's settings.

Note

PIM for app roles (preview) requires a **Microsoft 365 E7** license plan to preview. Agents and agent identities can receive eligible app role assignments in preview. Capabilities are subject to change and licensing requirements have not yet been announced. Existing assignment-management permissions remain unchanged.

To create, update, or remove app role assignments in Microsoft Entra PIM, you must be an owner of the target service principal or have one of the following roles:

- **Directory Writers**.
- **Hybrid Identity Administrator**.
- **Identity Governance Administrator**.
- **Privileged Role Administrator**.
- **User Administrator**.
- **Application Administrator**.
- **Cloud Application Administrator**.
- **CSP Partner Admin Agent**.

## Assign a role

Follow these steps to create an eligible or active app role assignment. Before adding an assignment, review the role's [activation and assignment settings](app-roles-settings).

The application must already define the app role you want to assign. You can manage any enterprise application with app roles, including Microsoft and third-party applications. The application's registration doesn't have to be owned by your tenant. For background, see [PIM for app roles (preview)](concept-pim-for-app-roles).

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
2. Browse to **ID Governance** &gt; **Privileged Identity Management** &gt; **App Roles (Preview)**.
3. Select the application you want to manage. Use the application and object IDs in the application list to identify the intended application.
4. Under **Manage**, select **Roles** to see the list of app roles and their active and eligible assignment counts.
5. Select **Add assignments**.

    You can also start from the application's **Assignments** page.
6. On the **Membership** tab, review **Resource** to confirm the application. Under **Select role**, select the app role you want to assign.

    **Resource type** identifies the application as a service principal. It doesn't identify the type of assignee.
7. Under **Select member(s)**, select **No member selected** to open **Select a member or group**.
8. Use **Search** to find the target identity. Select the checkbox for the identity, and then select **Select**.
9. Select **Next** to continue to the **Setting** tab. Under **Assignment type**, select **Eligible** or **Active**. Privileged Identity Management provides two distinct assignment types:

    - *Eligible* assignments require the assignee to activate the role before using it. Depending on the role settings, activation might require additional actions such as multifactor authentication (MFA), a business justification, or approval from designated approvers.
    - *Active* assignments don't require the assignee to activate the role before using it.
10. Configure the assignment duration:

    - For a permanent eligible assignment, use **Permanently eligible**.
    - For a permanent active assignment, use **Permanently assigned**.
    - For a time-bound assignment, clear the corresponding permanent option and set **Assignment starts** and **Assignment ends**.
11. If you're creating an active assignment and the role settings require justification, enter the reason in **Enter justification**.
12. Review the role, assignee, assignment type, and schedule, and select **Assign**.
13. Return to the role's **Eligible assignments** or **Active assignments** tab to verify the new assignment.

For information about activating an eligible assignment, see [Activate app roles in PIM (preview)](app-roles-activate).

## Update or remove an existing role assignment

Follow these steps to update or remove an existing role assignment.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
2. Browse to **ID Governance** &gt; **Privileged Identity Management** &gt; **App Roles (Preview)**.
3. Select the application you want to manage.
4. Under **Manage**, select **Assignments**.
5. Use **Eligible assignments** and **Active assignments** to review existing assignments for the selected application. Use **Expired assignments** to review expired assignments.

    To review assignments for a single role instead, select **Roles**, and then select the role.
6. Find the eligible direct-user assignment you want to update or remove.
7. Select the action for the assignment:

    - To change the assignment, select **Update** to open **Membership settings**. Review **Assignment details** to confirm the application, role, and member. Update **Permanently eligible** or **Assignment ends** as needed, and then select **Save**.

        The panel also shows an **Assignment type** dropdown.

        PIM displays an **Updating role grant** notification while processing the update, followed by **Update role assignment request queued**. The queued notification acknowledges the request; it doesn't confirm that the assignment has finished updating.
    - To remove the assignment, select **Remove**. In the **Remove** confirmation, check the member and role, and select **Yes** to proceed or **No** to cancel.
8. Return to the assignment list and verify the result of your change. For an update, check that the assignment reflects the requested values rather than relying only on the queued notification.

The eligible direct-user assignment list also provides an **Extend** action. For information about extending or renewing an assignment, see [Extend or renew app role assignments in PIM (preview)](app-roles-renew-extend).