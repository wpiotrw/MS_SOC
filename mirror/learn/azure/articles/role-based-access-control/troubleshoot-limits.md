---
layout: Conceptual
title: Troubleshoot Azure RBAC limits - Azure RBAC | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshoot-limits
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/189/azure-rbac/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
learn_banner_products:
- azure
description: Learn how to use Azure Resource Graph to reduce the number of Azure role assignments and Azure custom roles in Azure role-based access control (Azure RBAC).
author: rolyon
manager: pmwongera
ms.service: role-based-access-control
ms.topic: how-to
ms.date: 2025-10-15T00:00:00.0000000Z
ms.author: rolyon
ms.custom: sfi-image-nochange
locale: en-us
document_id: 158d81aa-bdea-a842-f7ba-fe4a07e4dd03
document_version_independent_id: a8a275ad-d164-8c17-883d-5619ead6b3b0
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/role-based-access-control/troubleshoot-limits.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: role-based-access-control/troubleshoot-limits
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/role-based-access-control/troubleshoot-limits.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: d271e074-0216-b756-ebed-65121ad67aa6
---

# Troubleshoot Azure RBAC limits - Azure RBAC | Microsoft Learn

This article describes some common solutions when you exceed the limits in Azure role-based access control (Azure RBAC).

## Prerequisites

- [Reader](built-in-roles#reader) role to run Azure Resource Graph queries.
- [Role Based Access Control Administrator](built-in-roles#role-based-access-control-administrator) role to add or remove role assignments.
- [User Access Administrator](built-in-roles#user-access-administrator) role to add role assignments, remove role assignments, or delete custom roles.
- [Groups Administrator](../active-directory/roles/permissions-reference#groups-administrator) or [User Administrator](../active-directory/roles/permissions-reference#user-administrator) role to create groups.

Note

The queries used in this article only return role assignments or custom roles that you have permissions to read. For example, if you only have permissions to read role assignments at resource group scope, role assignments at subscription scope aren't returned.

## Symptom - No more role assignments can be created

When you try to assign a role, you get the following error message:

`No more role assignments can be created (code: RoleAssignmentLimitExceeded)`

### Cause

Azure supports up to **5000** role assignments per subscription. This limit includes role assignments at the subscription, resource group, and resource scopes, but not at the management group scope. [Eligible role assignments](/en-us/azure/role-based-access-control/role-assignments-portal#step-6-select-assignment-type) and role assignments scheduled in the future do not count towards this limit. You should try to reduce the number of role assignments in the subscription.

Note

The **5000** role assignments limit per subscription is fixed and cannot be increased.

To get the number of role assignments, you can view the [chart on the Access control (IAM) page](/en-us/azure/role-based-access-control/role-assignments-list-portal#list-number-of-role-assignments) in the Azure portal. You can also use the following Azure PowerShell commands:

```azurepowershell
$scope = "/subscriptions/<subscriptionId>"
$ras = Get-AzRoleAssignment -Scope $scope | Where-Object {$_.scope.StartsWith($scope)}
$ras.Count
```

### Solution 1 - Replace principal-based role assignments with group-based role assignments

To reduce the number of role assignments in the subscription, add principals (users, service principals, and managed identities) to groups and assign roles to the groups instead. Follow these steps to identify where multiple role assignments for principals can be replaced with a single role assignment for a group.

1. Sign in to the [Azure portal](https://portal.azure.com) and open the Azure Resource Graph Explorer.
2. Select **Scope** and set the scope for the query.

    You typically set scope to **Directory** to query your entire tenant, but you can narrow the scope to particular subscriptions.

    [![Screenshot of Azure Resource Graph Explorer that shows Scope selection.](media/shared/resource-graph-scope.png)](media/shared/resource-graph-scope.png#lightbox)
3. Select **Set authorization scope** and set the authorization scope to **At, above and below** to query all resources at the specified scope.

    [![Screenshot of Azure Resource Graph Explorer that shows Set authorization scope pane.](media/shared/resource-graph-authorization-scope.png)](media/shared/resource-graph-authorization-scope.png#lightbox)
4. Run the following query to get the role assignments with the same role and at the same scope, but for different principals.

    This query checks active role assignments and doesn't consider eligible role assignments in [Microsoft Entra Privileged Identity Management](/en-us/entra/id-governance/privileged-identity-management/pim-resource-roles-assign-roles). To list eligible role assignments, you can use the Microsoft Entra admin center, PowerShell, or REST API. For more information, see [Get-AzRoleEligibilityScheduleInstance](/en-us/powershell/module/az.resources/get-azroleeligibilityscheduleinstance) or [Role Eligibility Schedule Instances - List For Scope](/en-us/rest/api/authorization/role-eligibility-schedule-instances/list-for-scope).

    If you are using [role assignment conditions](conditions-overview) or [delegating role assignment management with conditions](delegate-role-assignments-overview), you should use the Conditions query. Otherwise, use the Default query.

# [Default](#tab/default)
```kusto
    authorizationresources
    | where type =~ "microsoft.authorization/roleassignments"
    | where id startswith "/subscriptions"
    | extend RoleId = tolower(tostring(properties.roleDefinitionId))
    | join kind = leftouter (
      authorizationresources
      | where type =~ "microsoft.authorization/roledefinitions"
      | extend RoleDefinitionName = tostring(properties.roleName)
      | extend RoleId = tolower(id)
      | project RoleDefinitionName, RoleId
    ) on $left.RoleId == $right.RoleId
    | extend principalId = tostring(properties.principalId)
    | extend principal_to_ra = pack(principalId, id)
    | summarize count_ = count(), AllPrincipals = make_set(principal_to_ra) by RoleDefinitionId = RoleId, Scope = tolower(properties.scope), RoleDefinitionName
    | where count_ > 1
    | order by count_ desc
    ```

# [Conditions](#tab/conditions)
```kusto
    authorizationresources
    | where type =~ "microsoft.authorization/roleassignments"
    | where id startswith "/subscriptions"
    | extend RoleId = tolower(tostring(properties.roleDefinitionId))
    | extend condition = tostring(properties.condition)
    | join kind = leftouter (
      authorizationresources
      | where type =~ "microsoft.authorization/roledefinitions"
      | extend RoleDefinitionName = tostring(properties.roleName)
      | extend RoleId = tolower(id)
      | project RoleDefinitionName, RoleId
    ) on $left.RoleId == $right.RoleId
    | extend principalId = tostring(properties.principalId)
    | extend principal_to_ra = pack(principalId, id)
    | summarize count_ = count(), AllPrincipals = make_set(principal_to_ra) by RoleDefinitionId = RoleId, Scope = tolower(properties.scope), RoleDefinitionName, condition
    | where count_ > 1
    | order by count_ desc
    ```

---

    The following shows an example of the results. The **count\_** column is the number of principals assigned the same role and at the same scope. The count is sorted in descending order.

    [![Screenshot of Azure Resource Graph Explorer that shows role assignments with the same role and at the same scope, but for different principals.](media/troubleshoot-limits/authorization-same-role-scope.png)](media/troubleshoot-limits/authorization-same-role-scope.png#lightbox)
5. Identify a row where you want to replace the multiple role assignments with a single role assignment for a group.
6. In the row, select **See details** to open the **Details** pane.

    [![Screenshot of Details pane that shows role assignments with the same role and at the same scope, but for different principals.](media/troubleshoot-limits/authorization-same-role-scope-details.png)](media/troubleshoot-limits/authorization-same-role-scope-details.png#lightbox)

    | Column | Description |
    | --- | --- |
    | RoleDefinitionId | [ID](built-in-roles) of the currently assigned role. |
    | Scope | Scope for the role assignment, which will be a subscription, resource group, or resource. |
    | RoleDefinitionName | [Name](built-in-roles) of the currently assigned role. |
    | count\_ | Number of principals assigned the same role and at the same scope. |
    | AllPrincipals | List of principal IDs assigned the same role and at the same scope. |
7. Use **RoleDefinitionId**, **RoleDefinitionName**, and **Scope** to get the role and scope.
8. Use **AllPrincipals** to get the list of the principal IDs with the same role assignment.
9. Create a Microsoft Entra group. For more information, see [Manage Microsoft Entra groups and group membership](../active-directory/fundamentals/how-to-manage-groups).
10. Add the principals from **AllPrincipals** to the group.

    For information about how to add principals in bulk, see [Bulk add group members in Microsoft Entra ID](../active-directory/enterprise-users/groups-bulk-import-members).
11. Assign the role to the group you created at the same scope. For more information, see [Assign Azure roles using the Azure portal](/en-us/azure/role-based-access-control/role-assignments-portal).

    Now you can find and remove the principal-based role assignments.
12. Get the principal names from the principal IDs.

    - To use Azure portal, see [Add or update a user's profile information and settings](../active-directory/fundamentals/how-to-manage-user-profile-info).
    - To use PowerShell, see [Get-MgUser](/en-us/powershell/module/microsoft.graph.users/get-mguser?branch=main).
    - To use Azure CLI, see [az ad user show](/en-us/cli/azure/ad/user?branch=main#az-ad-user-show).
13. Open the **Access control (IAM)** page at the same scope as the role assignments.
14. Select the **Role assignments** tab.
15. To filter the role assignments, select the **Role** filter and then select the role name.
16. Find the principal-based role assignments.

    You should also see your group-based role assignment.

    [![Screenshot of Access control (IAM) page that shows role assignments with the same role and at the same scope, but for different principals.](media/troubleshoot-limits/role-assignments-filter-remove.png)](media/troubleshoot-limits/role-assignments-filter-remove.png#lightbox)
17. Select and remove the principal-based role assignments. For more information, see [Remove Azure role assignments](/en-us/azure/role-based-access-control/role-assignments-remove).

### Solution 2 - Remove redundant role assignments

To reduce the number of role assignments in the subscription, remove redundant role assignments. Follow these steps to identify where redundant role assignments at a lower scope can potentially be removed since a role assignment at a higher scope already grants access.

1. Sign in to the [Azure portal](https://portal.azure.com) and open the Azure Resource Graph Explorer.
2. Select **Scope** and set the scope for the query.

    You typically set scope to **Directory** to query your entire tenant, but you can narrow the scope to particular subscriptions.

    [![Screenshot of Azure Resource Graph Explorer that shows Scope selection.](media/shared/resource-graph-scope.png)](media/shared/resource-graph-scope.png#lightbox)
3. Select **Set authorization scope** and set the authorization scope to **At, above and below** to query all resources at the specified scope.

    [![Screenshot of Azure Resource Graph Explorer that shows Set authorization scope pane.](media/shared/resource-graph-authorization-scope.png)](media/shared/resource-graph-authorization-scope.png#lightbox)
4. Run the following query to get the role assignments with the same role and same principal, but at different scopes.

    This query checks active role assignments and doesn't consider eligible role assignments in [Microsoft Entra Privileged Identity Management](/en-us/entra/id-governance/privileged-identity-management/pim-resource-roles-assign-roles). To list eligible role assignments, you can use the Microsoft Entra admin center, PowerShell, or REST API. For more information, see [Get-AzRoleEligibilityScheduleInstance](/en-us/powershell/module/az.resources/get-azroleeligibilityscheduleinstance) or [Role Eligibility Schedule Instances - List For Scope](/en-us/rest/api/authorization/role-eligibility-schedule-instances/list-for-scope).

    If you are using [role assignment conditions](conditions-overview) or [delegating role assignment management with conditions](delegate-role-assignments-overview), you should use the Conditions query. Otherwise, use the Default query.

# [Default](#tab/default)
```kusto
    authorizationresources
    | where type =~ "microsoft.authorization/roleassignments"
    | where id startswith "/subscriptions"
    | extend RoleDefinitionId = tolower(tostring(properties.roleDefinitionId))
    | extend PrincipalId = tolower(properties.principalId)
    | extend RoleDefinitionId_PrincipalId = strcat(RoleDefinitionId, "_", PrincipalId)
    | join kind = leftouter (
      authorizationresources
      | where type =~ "microsoft.authorization/roledefinitions"
      | extend RoleDefinitionName = tostring(properties.roleName)
      | extend rdId = tolower(id)
      | project RoleDefinitionName, rdId
    ) on $left.RoleDefinitionId == $right.rdId
    | summarize count_ = count(), Scopes = make_set(tolower(properties.scope)) by RoleDefinitionId_PrincipalId,RoleDefinitionName
    | project RoleDefinitionId = split(RoleDefinitionId_PrincipalId, "_", 0)[0], RoleDefinitionName, PrincipalId = split(RoleDefinitionId_PrincipalId, "_", 1)[0], count_, Scopes
    | where count_ > 1
    | order by count_ desc
    ```

# [Conditions](#tab/conditions)
```kusto
    authorizationresources
    | where type =~ "microsoft.authorization/roleassignments"
    | where id startswith "/subscriptions"
    | extend RoleDefinitionId = tolower(tostring(properties.roleDefinitionId))
    | extend PrincipalId = tolower(properties.principalId)
    | extend RoleDefinitionId_PrincipalId = strcat(RoleDefinitionId, "_", PrincipalId)
    | extend condition = tostring(properties.condition)
    | join kind = leftouter (
      authorizationresources
      | where type =~ "microsoft.authorization/roledefinitions"
      | extend RoleDefinitionName = tostring(properties.roleName)
      | extend rdId = tolower(id)
      | project RoleDefinitionName, rdId
    ) on $left.RoleDefinitionId == $right.rdId
    | summarize count_ = count(), Scopes = make_set(tolower(properties.scope)) by RoleDefinitionId_PrincipalId,RoleDefinitionName, condition
    | project RoleDefinitionId = split(RoleDefinitionId_PrincipalId, "_", 0)[0], RoleDefinitionName, PrincipalId = split(RoleDefinitionId_PrincipalId, "_", 1)[0], count_, Scopes, condition
    | where count_ > 1
    | order by count_ desc
    ```

---

    The following shows an example of the results. The **count\_** column is the number of different scopes for role assignments with the same role and same principal. The count is sorted in descending order.

    [![Screenshot of Azure Resource Graph Explorer that shows role assignments for the same role and same principal, but at different scopes.](media/troubleshoot-limits/authorization-same-role-principal.png)](media/troubleshoot-limits/authorization-same-role-principal.png#lightbox)

    | Column | Description |
    | --- | --- |
    | RoleDefinitionId | [ID](built-in-roles) of the currently assigned role. |
    | RoleDefinitionName | [Name](built-in-roles) of the currently assigned role. |
    | PrincipalId | ID of the principal assigned the role. |
    | count\_ | Number of different scopes for role assignments with the same role and same principal. |
    | Scopes | Scopes for role assignments with the same role and same principal. |
5. Identify a row where you want to remove redundant role assignments.
6. In a row, select **See details** to open the **Details** pane.

    [![Screenshot of Details pane that shows role assignments for the same role and same principal, but at different scopes.](media/troubleshoot-limits/authorization-same-role-principal-details.png)](media/troubleshoot-limits/authorization-same-role-principal-details.png#lightbox)
7. Use **RoleDefinitionId**, **RoleDefinitionName**, and **PrincipalId** to get the role and principal ID.
8. Use **Scopes** to get the list of the scopes for the same role and same principal.
9. Determine which scope is required for the role assignment. The other role assignments can be removed.

    You should follow [best practices of least privilege](best-practices#only-grant-the-access-users-need) when determining which role assignments can be removed. The role assignment at the higher scope might be granting more access to the principal than what is needed. In that case, you should remove the role assignment with the higher scope. For example, a user might not need a Virtual Machine Contributor role assignment at subscription scope when a Virtual Machine Contributor role assignment at a lower resource group scope grants the required access.
10. Get the principal name from the principal ID.

    - To use Azure portal, see [Add or update a user's profile information and settings](../active-directory/fundamentals/how-to-manage-user-profile-info).
    - To use PowerShell, see [Get-MgUser](/en-us/powershell/module/microsoft.graph.users/get-mguser?branch=main).
    - To use Azure CLI, see [az ad user show](/en-us/cli/azure/ad/user?branch=main#az-ad-user-show).
11. Open the **Access control (IAM)** page at the scope for a role assignment you want to remove.
12. Select the **Role assignments** tab.
13. To filter the role assignments, select the **Role** filter and then select the role name.
14. Find the principal.
15. Select and remove the role assignment. For more information, see [Remove Azure role assignments](/en-us/azure/role-based-access-control/role-assignments-remove).

### Solution 3 - Replace multiple built-in role assignments with a custom role assignment

To reduce the number of role assignments in the subscription, replace multiple built-in role assignments with a single custom role assignment. Follow these steps to identify where multiple built-in role assignments can potentially be replaced.

1. Sign in to the [Azure portal](https://portal.azure.com) and open the Azure Resource Graph Explorer.
2. Select **Scope** and set the scope for the query.

    You typically set scope to **Directory** to query your entire tenant, but you can narrow the scope to particular subscriptions.

    [![Screenshot of Azure Resource Graph Explorer that shows Scope selection.](media/shared/resource-graph-scope.png)](media/shared/resource-graph-scope.png#lightbox)
3. Run the following query to get role assignments with the same principal and same scope, but with different built-in roles.

    This query checks active role assignments and doesn't consider eligible role assignments in [Microsoft Entra Privileged Identity Management](/en-us/entra/id-governance/privileged-identity-management/pim-resource-roles-assign-roles). To list eligible role assignments, you can use the Microsoft Entra admin center, PowerShell, or REST API. For more information, see [Get-AzRoleEligibilityScheduleInstance](/en-us/powershell/module/az.resources/get-azroleeligibilityscheduleinstance) or [Role Eligibility Schedule Instances - List For Scope](/en-us/rest/api/authorization/role-eligibility-schedule-instances/list-for-scope).

    If you are using [role assignment conditions](conditions-overview) or [delegating role assignment management with conditions](delegate-role-assignments-overview), you should use the Conditions query. Otherwise, use the Default query.

# [Default](#tab/default)
```kusto
    authorizationresources
    | where type =~ "microsoft.authorization/roleassignments"
    | where id startswith "/subscriptions"
    | extend PrincipalId = tostring(properties.principalId) 
    | extend Scope = tolower(properties.scope)
    | extend RoleDefinitionId = tolower(tostring(properties.roleDefinitionId))
    | join kind = leftouter (
      authorizationresources
      | where type =~ "microsoft.authorization/roledefinitions"
      | extend RoleName = tostring(properties.roleName)
      | extend RoleId = tolower(id)
      | extend RoleType = tostring(properties.type) 
      | where RoleType == "BuiltInRole"
      | extend RoleId_RoleName = pack(RoleId, RoleName)
    ) on $left.RoleDefinitionId == $right.RoleId
    | summarize count_ = count(), AllRD = make_set(RoleId_RoleName) by PrincipalId, Scope
    | where count_ > 1
    | order by count_ desc
    ```

# [Condition](#tab/conditions)
```kusto
    authorizationresources
    | where type =~ "microsoft.authorization/roleassignments"
    | where id startswith "/subscriptions"
    | extend PrincipalId = tostring(properties.principalId) 
    | extend Scope = tolower(properties.scope)
    | extend RoleDefinitionId = tolower(tostring(properties.roleDefinitionId))
    | extend condition = tostring(properties.condition)
    | join kind = leftouter (
      authorizationresources
      | where type =~ "microsoft.authorization/roledefinitions"
      | extend RoleName = tostring(properties.roleName)
      | extend RoleId = tolower(id)
      | extend RoleType = tostring(properties.type) 
      | where RoleType == "BuiltInRole"
      | extend RoleId_RoleName = pack(RoleId, RoleName)
    ) on $left.RoleDefinitionId == $right.RoleId
    | summarize count_ = count(), AllRD = make_set(RoleId_RoleName) by PrincipalId, Scope, condition
    | where count_ > 1
    | order by count_ desc
    ```

---

    The following shows an example of the results. The **count\_** column is the number of different built-in role assignments with the same principal and same scope. The count is sorted in descending order.

    [![Screenshot of Azure Resource Graph Explorer that shows role assignments for with the same principal and same scope.](media/troubleshoot-limits/authorization-same-principal-scope.png)](media/troubleshoot-limits/authorization-same-principal-scope.png#lightbox)

    | Column | Description |
    | --- | --- |
    | PrincipalId | ID of the principal assigned the built-in roles. |
    | Scope | Scope for built-in role assignments. |
    | count\_ | Number of built-in role assignments with the same principal and same scope. |
    | AllRD | ID and name of built-in roles. |
4. In a row, select **See details** to open the **Details** pane.

    [![Screenshot of Details pane that shows role assignments with the same principal and same scope.](media/troubleshoot-limits/authorization-same-principal-scope-details.png)](media/troubleshoot-limits/authorization-same-principal-scope-details.png#lightbox)
5. Use **AllRD** to see the built-in roles that can potentially be combined into a custom role.
6. List the actions and data actions for the built-in roles. For more information, see [List Azure role definitions](/en-us/azure/role-based-access-control/role-definitions-list) or [Azure built-in roles](built-in-roles).
7. Create a custom role that includes all the actions and data actions as the built-in roles. To make it easier to create the custom role, you can start by cloning one of the built-in roles. For more information, see [Create or update Azure custom roles using the Azure portal](custom-roles-portal).
8. Get the principal name from the principal ID.

    - To use Azure portal, see [Add or update a user's profile information and settings](../active-directory/fundamentals/how-to-manage-user-profile-info).
    - To use PowerShell, see [Get-MgUser](/en-us/powershell/module/microsoft.graph.users/get-mguser?branch=main).
    - To use Azure CLI, see [az ad user show](/en-us/cli/azure/ad/user?branch=main#az-ad-user-show).
9. Open the **Access control (IAM)** page at the same scope as the role assignments.
10. Assign the new custom role to the principal. For more information, see [Assign Azure roles using the Azure portal](/en-us/azure/role-based-access-control/role-assignments-portal).

    Now you can remove the built-in role assignments.
11. On the **Access control (IAM)** page at the same scope, select the **Role assignments** tab.
12. Find the principal and built-in role assignments.
13. Remove the built-in role assignments from the principal. For more information, see [Remove Azure role assignments](/en-us/azure/role-based-access-control/role-assignments-remove).

### Solution 4 - Make role assignments eligible

To reduce the number of role assignments in the subscription and you have Microsoft Entra ID P2, make role assignments eligible in [Microsoft Entra Privileged Identity Management](/en-us/entra/id-governance/privileged-identity-management/pim-resource-roles-assign-roles) instead of permanently assigned.

### Solution 5 - Add an additional subscription

Add an additional subscription.

## Symptom - No more role assignments can be created at management group scope

You're unable to assign a role at management group scope.

### Cause

Azure supports up to **500** role assignments per management group. This limit is different than the role assignments limit per subscription.

Note

The **500** role assignments limit per management group is fixed and cannot be increased.

### Solution

Try to reduce the number of role assignments in the management group. For possible options, see Symptom - No more role assignments can be created. For the queries to retrieve resources at the management group level, you'll need to make the following change to the queries:

Replace

`| where id startswith "/subscriptions"`

With

`| where id startswith "/providers/Microsoft.Management/managementGroups"`

## Symptom - No more role definitions can be created

When you try to create a new custom role, you get the following message:

`Role definition limit exceeded. No more role definitions can be created (code: RoleDefinitionLimitExceeded)`

### Cause

Azure supports up to **5000** custom roles in a directory. (For Microsoft Azure operated by 21Vianet, the limit is 2000 custom roles.)

### Solution

Follow these steps to find and delete unused Azure custom roles.

1. Sign in to the [Azure portal](https://portal.azure.com) and open the Azure Resource Graph Explorer.
2. Select **Scope** and set the scope to **Directory** for the query.

    [![Screenshot of Azure Resource Graph Explorer that shows Scope selection.](media/shared/resource-graph-scope.png)](media/shared/resource-graph-scope.png#lightbox)
3. Run the following query to get all custom roles that don't have any role assignments:

    This query checks active role assignments and doesn't consider eligible custom role assignments in [Microsoft Entra Privileged Identity Management](/en-us/entra/id-governance/privileged-identity-management/pim-resource-roles-assign-roles). To list eligible custom role assignments, you can use the Microsoft Entra admin center, PowerShell, or REST API. For more information, see [Get-AzRoleEligibilityScheduleInstance](/en-us/powershell/module/az.resources/get-azroleeligibilityscheduleinstance) or [Role Eligibility Schedule Instances - List For Scope](/en-us/rest/api/authorization/role-eligibility-schedule-instances/list-for-scope).

    ```kusto
    authorizationresources
    | where type =~ "microsoft.authorization/roledefinitions"
    | where tolower(properties.type) == "customrole"
    | extend rdId = tolower(id)
    | extend Scope = tolower(properties.assignableScopes)
    | join kind = leftouter (
    authorizationresources
      | where type =~ "microsoft.authorization/roleassignments"
      | extend RoleId = tolower(tostring(properties.roleDefinitionId))
      | summarize RoleAssignmentCount = count() by RoleId
    ) on $left.rdId == $right.RoleId
    | where isempty(RoleAssignmentCount)
    | project RoleDefinitionId = rdId, RoleDefinitionName = tostring(properties.roleName), Scope
    ```

    The following shows an example of the results:

    [![Screenshot of Azure Resource Graph Explorer that shows custom roles without role assignments.](media/troubleshoot-limits/authorization-unused-custom-roles.png)](media/troubleshoot-limits/authorization-unused-custom-roles.png#lightbox)

    | Column | Description |
    | --- | --- |
    | RoleDefinitionId | ID of the unused custom role. |
    | RoleDefinitionName | Name of the unused custom role. |
    | Scope | [Assignable scopes](role-definitions#assignablescopes) for the unused custom role. |
4. Open the scope (typically subscription) and then open the **Access control (IAM)** page.
5. Select the **Roles** tab to see a list of all the built-in and custom roles.
6. In the **Type** filter, select **CustomRole** to just see your custom roles.
7. Select the ellipsis (**...**) for the custom role you want to delete and then select **Delete**.

    [![Screenshot of a list of custom roles that can be selected for deletion.](media/shared/custom-roles-delete-menu.png)](media/shared/custom-roles-delete-menu.png#lightbox)