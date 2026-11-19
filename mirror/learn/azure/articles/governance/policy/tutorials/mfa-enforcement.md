---
layout: Conceptual
title: 'Tutorial: Self-enforce MFA through Azure Policy - Azure Policy | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/policy/tutorials/mfa-enforcement
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/228/azure-policy
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/675ae472-f324-ec11-b6e6-000d3a4f0da0
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
author: nehakulkarni
learn_banner_products:
- azure
ms.author: nehakulkarni
ms.service: azure-policy
description: Learn how to gather audit events or enforce MFA enforcement on your environment
ms.date: 2026-11-18T00:00:00.0000000Z
ms.topic: how-to
locale: en-us
document_id: fe117bf8-b9ea-0395-46e5-7bff0d9461f5
document_version_independent_id: 4273bd15-f806-7b49-d61d-2eb94741f03b
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/policy/tutorials/mfa-enforcement.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/policy/tutorials/mfa-enforcement
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/policy/tutorials/mfa-enforcement.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/eea02214-631d-404a-92d1-5a3357c32a26
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f42c31d7-eed9-43b7-9757-54caffb53cdc
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
platformId: 11443ea1-7f70-b6d7-1f0a-fcac11a021c7
---

# Tutorial: Self-enforce MFA through Azure Policy - Azure Policy | Microsoft Learn

[Azure Policy](../overview) is a powerful governance tool that allows you to prepare your organization for [upcoming enforcement of multifactor authentication (MFA) across Azure clients](https://aka.ms/mfaforazure). This guide walks you through the process of applying Azure Policy assignments to self-enforce multifactor authentication across your organization.

## Apply Azure Policy enforcement through Azure portal

### 1. Sign into Azure portal

Navigate to the [Azure portal](https://www.portal.azure.com)

### 2. Access Azure Policy Service

Select Policy under Azure services. If you don't see it, type 'Policy' in the search bar at the top and select it from the results.

[![Screenshot of Azure Policy Assignment View.](../media/multifactor-enforcement/policy-overview.png)](../media/multifactor-enforcement/policy-overview.png#lightbox)

### 3. Choose the Scope for Assignment

1. Click 'Assignments' in the left pane of the Policy dashboard.
2. Click 'Assign policy' at the top of the assignments page.
3. Click 'Select scope' in the Scope section.
4. Select the appropriate resource group, subscription, or management group where you want to apply the policy.
5. Click 'Select' to confirm your choice.

### 4. Configure Selectors for gradual rollout of policy enforcement

Note

To enable safe rollout of policy enforcement, we recommend using [Azure Policy’s resource selectors](/en-us/azure/governance/policy/concepts/assignment-structure#resource-selectors) to gradually rollout policy enforcement across your resources.

1. Click 'Expand' on the 'Resource Selectors' section of the Basics tab.
2. Click 'Add a resource selector'

    [![Screenshot of Azure Policy Assignment Creation View.](../media/multifactor-enforcement/policy-resource-selectors.png)](../media/multifactor-enforcement/policy-resource-selectors.png#lightbox)
3. Add a name for your selector
4. Toggle resourceLocation to enable it.
5. Pick a few low-risk regions that you’d like to enforce on. The policy assignment will evaluate Azure resources in those regions.
6. You can update this assignment later to add more regions by adding more resourceLocation selectors or updating the existing resourceLocation selector to add more regions.

[![Screenshot of Azure Policy Selector Creation View.](../media/multifactor-enforcement/resource-selector-creation.png)](../media/multifactor-enforcement/resource-selector-creation.png#lightbox)

### 5. Select a Policy Definition

1. Click on Policy definition under 'Basics'.
2. Browse or search for the multifactor policy definition – there are 2 of them. Pick one for now:
    - [Users must authenticate with multi-factor authentication to delete resources](https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetail.ReactView/id/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2Fdb4a9d17-db75-4f46-9fcb-9f9526604417/version/1.0.0-preview/scopes/%5B%22%2Fsubscriptions%2F12015272-f077-4945-81de-a5f607d067e1%22%2C%22%2Fsubscriptions%2F0ba674a6-9fde-43b4-8370-a7e16fdf0641%22%5D/contextRender/).
    - [Users must authenticate with multi-factor authentication to create or update resources](https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetail.ReactView/id/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F4e6c27d5-a6ee-49cf-b2b4-d8fe90fa2b8b/version/1.0.0-preview/scopes/%5B%22%2Fsubscriptions%2F12015272-f077-4945-81de-a5f607d067e1%22%2C%22%2Fsubscriptions%2F0ba674a6-9fde-43b4-8370-a7e16fdf0641%22%5D/contextRender/).
3. Select the policy definition from the list.

[![Screenshot of Azure Policy Definition Search View.](../media/multifactor-enforcement/policy-definition-selection.png)](../media/multifactor-enforcement/policy-definition-selection.png#lightbox)

### 6. Configure More Assignment Details

1. Under 'Basics', enter a name for your policy assignment. Optionally, you may add a description to help others understand the purpose of this assignment.
2. Under 'Basics', enforcement mode should be set to enabled (this mode is set by default, no action needed).
3. Go to the 'Parameters' tab. Uncheck 'only show parameters that require input or review'. The parameter value should be at the preselected value 'AuditAction' or 'Audit' (depending on the definition chosen in step 4).
4. Under the 'Non-compliance messages' tab, configure a custom message that any user sees if they're blocked from deleting a resource because of this enforcement:

*Sample Text: To resolve this error, set up MFA at aka.ms/setupMFA. If you set up MFA and are still receiving this error, reach out to your Entra administrator to restore your Azure security default.*

[![Screenshot of Azure Policy Message Tab.](../media/multifactor-enforcement/noncompliance-message.png)](../media/multifactor-enforcement/noncompliance-message.png#lightbox)

### 7. Review and Create Assignment

1. Review your selections and settings on the 'Review + create' tab.
2. If everything looks correct, click 'Create' to apply the policy assignment.

### 8. Roll out the policy assignment to all regions

1. Update the policy assignment selector to evaluate resources in other regions.
2. Repeat this step until the policy assignment is evaluating resources in all regions.

### 9. Verify existence of the policy assignment

1. Under the 'Assignments' tab, confirm that the policy assignment was successfully created.
2. You can use the search bar and scope bar to easily filter.

[![Screenshot of Azure Policy Assignment List View.](../media/multifactor-enforcement/assignment-list.png)](../media/multifactor-enforcement/assignment-list.png#lightbox)

Note

Azure Policy assignments that evaluate multifactor enforcement don't provide compliance. To get audit events for your policy assignment without enforcement, see **Audit mode** in the following section.

## Update the policy assignment to enforcement

You can enable enforcement by updating the 'Effect' of the policy assignment.

1. Go to the policy assignment under [Policy Assignments](https://portal.azure.com/?subscriptionId=617eb244-7791-4c21-98c5-77f840a7e4ef#view/Microsoft_Azure_Policy/PolicyMenuBlade/%7E/Overview/scope/%2Fsubscriptions%2F617eb244-7791-4c21-98c5-77f840a7e4ef). Click 'Edit assignment'.
2. In the 'Basics' tab, you’ll see 'Overrides'. Click expand.
3. Click 'Add a policy effect override'
4. In the drop-down menu, update the `Override Value` to 'DenyAction' or 'Deny' (depending on the policy definition chosen at Step 4).
5. For `Selected Resources`, pick a few low-risk regions that you’d like to enforce on. The policy assignment will only evaluate Azure resources in those regions. [![Screenshot of Azure Policy Overrides Creation.](../media/multifactor-enforcement/overrides-example.png)](../media/multifactor-enforcement/overrides-example.png#lightbox)
6. Click 'Review + save', then 'Create'.
7. Once you have confirmed no unexpected impact, you may update the existing override to add other regions.

## Audit Mode

Discover audit events in your activity log when this policy assignment is applied in audit mode. Each event represents a resource create, update or delete that was performed by a user who did not authenticate with MFA.

You can view activity Log events in Azure portal and other supported clients. Here's a sample query that can be used in CLI:

```bash
az monitor activity-log list \
  --query "[?operationName.value=='Microsoft.Authorization/policies/audit/action'].{ResourceId: resourceId, Policies: properties.policies}" \
  --output json | \
jq -r '"ResourceName\tResourceId\tPolicyDefinitionDisplayName", (.[] as $event | ($event.Policies | fromjson[] | "\($event.ResourceId | split("/") | last)\t\($event.ResourceId)\t\(.policyDefinitionDisplayName)"))' | \
column -t -s $'\t'
```

You can also use the Azure portal to pull log events. Here's a sample query:

```kusto
AzureActivity
| where CategoryValue == "Policy"
| extend p = parse_json(Properties)
| extend policies = parse_json(tostring(p.policies))
| mv-expand policies
| where tostring(policies.policyDefinitionId) == "/providers/Microsoft.Authorization/policyDefinitions/4e6c27d5-a6ee-49cf-b2b4-d8fe90fa2b8b"
| project TimeGenerated, ResourceId, OperationNameValue, PolicyDefinitionId = tostring(policies.policyDefinitionId), PolicyAssignmentId = tostring(policies.policyAssignmentId)
```

Note

Audit events are seen only in Activity Logs with the Policy compliance list showing always 0 resources. This policy identifies non-compliant requests, not resources, which is why the resource compliance list is empty.

## Enforcement Mode

Discover deny events in your activity log when this policy assignment is applied in enforcement mode. Each deny event represents a resource create, update or delete that was attempted by a user who did not authenticate with MFA.

The next section shows the experience from some select clients when the policy assignment is applied in enforcement mode and a user account attempts to create, update, or delete a resource without being authenticated with MFA.

Note

In preview timeframe, the error messages displayed to the user may differ depending on the client and command being run.

### Azure portal

When you attempt to perform a create, update, or delete operation without an MFA-authenticated token, Azure portal may return:

[![Screenshot of Azure portal view.](../media/multifactor-enforcement/portal-enforcement.png)](../media/multifactor-enforcement/portal-enforcement.png#lightbox)

### Azure CLI

When you attempt to perform a create, update, or delete operation without an MFA-authenticated token, Azure CLI may return:

[![Screenshot of Azure CLI View When User Gets Blocked By Policy.](../media/multifactor-enforcement/cli-sample.png)](../media/multifactor-enforcement/cli-sample.png#lightbox)

### Azure PowerShell

When you attempt to perform a create, update, or delete operation without an MFA-authenticated token, Azure PowerShell may return:

[![Screenshot of Azure PowerShell View When User Gets Blocked By Policy.](../media/multifactor-enforcement/powershell-sample.png)](../media/multifactor-enforcement/powershell-sample.png#lightbox)