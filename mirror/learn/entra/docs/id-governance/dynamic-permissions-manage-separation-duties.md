---
layout: Conceptual
title: Manage separation of duties for dynamic permissions - Microsoft Entra ID Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/id-governance/dynamic-permissions-manage-separation-duties
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: OWinfreyATL
ms.author: owinfrey
ms.service: entra-id-governance
manager: dougeby
description: Learn how to import, update, enable, disable, and delete separation of duties rules for dynamic permissions in Microsoft Entra ID Governance.
ms.topic: how-to
ms.date: 2026-11-14T00:00:00.0000000Z
ms.custom: msecd-doc-authoring-1032
ai-usage: ai-generated
locale: en-us
document_id: 12697388-b6ef-585a-51fa-a5de577b107f
document_version_independent_id: 12697388-b6ef-585a-51fa-a5de577b107f
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/id-governance/dynamic-permissions-manage-separation-duties.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: id-governance/dynamic-permissions-manage-separation-duties
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/id-governance/dynamic-permissions-manage-separation-duties.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68cb9039-df60-49b0-8ef8-89ad96497f63
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac4b7417-d4c2-43d4-94bf-f22fa1416b34
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/725b6df3-93e8-472d-834e-e7e0d2953d35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68876bab-7da4-4e70-b295-395b3a255a1f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: ec24a8bf-4876-d7fe-e6f7-8ec80a94f4de
---

# Manage separation of duties for dynamic permissions - Microsoft Entra ID Governance | Microsoft Learn

As an Identity Governance Administrator, you can manage separation of duties rules for dynamic permissions in Microsoft Entra ID Governance.

Note

With separation of duties in the dynamic permissions preview, organizations can define rules using the authorization models and constructs of their applications and resources. These preview capabilities are separate from the generally available [separation of duties capabilities for access packages](entitlement-management-access-package-incompatible) in entitlement management.

This article explains how to import, update, enable, disable, and delete rules, and where to view the impacted agent non-human identities.

## Prerequisites

Dynamic permissions is in preview and capabilities are subject to change. Licensing requirements for dynamic permissions have not yet been announced. During preview, dynamic permissions for agent identities requires one of the following license plans:

- **Microsoft 365 E7**, which includes Agent 365 and Microsoft Entra Suite.

Have a resource already set up that supports separation of duties. If you're getting started, see [Tutorial: Mitigate permission risk of agents in Snowflake with Microsoft Entra dynamic permissions](tutorial-dynamic-permissions-prevent-excessive-permissions).

## View separation of duties rule details

To view the details of a separation of duties rule, follow these steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Identity Governance Administrator](../identity/role-based-access-control/permissions-reference#identity-governance-administrator).
2. Browse to **ID Governance** &gt; **Dynamic permissions (preview)** &gt; **Separation of duties**.

    [![Screenshot of two separation of duties rules for a catalog, showing their descriptions, resources, and enabled status.](media/dynamic-permissions-manage-separation-duties/view-separation-of-duties-rules.png)](media/dynamic-permissions-manage-separation-duties/view-separation-of-duties-rules.png#lightbox)
3. Select the name of the rule.

    [![Screenshot of a separation of duties rule showing its Object ID and the two sets of conflicting Snowflake account roles.](media/dynamic-permissions-manage-separation-duties/view-separation-of-duties-rule-details.png)](media/dynamic-permissions-manage-separation-duties/view-separation-of-duties-rule-details.png#lightbox)

## Import separation of duties rules

To import separation of duties rules from a CSV file, follow these steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Identity Governance Administrator](../identity/role-based-access-control/permissions-reference#identity-governance-administrator).
2. Browse to **ID Governance** &gt; **Dynamic permissions (preview)** &gt; **Separation of duties**.
3. Select **Import rules**.

    [![Screenshot of the Separation of duties page with Import rules highlighted to add rules to the selected catalog.](media/dynamic-permissions-manage-separation-duties/import-separation-of-duties-rules.png)](media/dynamic-permissions-manage-separation-duties/import-separation-of-duties-rules.png#lightbox)
4. Select **Download template** to get the CSV template.
5. Update the CSV template with your separation of duties rules. For Snowflake examples, see CSV examples for Snowflake.
6. Select **Choose file**, and then select the CSV file to upload it.
7. Confirm the import message, which summarizes how many rules will be created or updated. If validation reports errors, correct the CSV file and upload it again.
8. Select **Review and import**.
9. Confirm the list of rules to be imported.
10. Select **Import**.
11. Review the import results. If all rules were imported successfully, select **Return to rules**.

### CSV examples for Snowflake

The examples define two rules for illustrative custom Snowflake account roles. Replace the resource identifier and role names with values from your environment.

- `PermissionSet1` and `PermissionSet2`: Use the exact names of the Snowflake account roles that an identity must not hold together.
- `ResourceOriginId`: Use the resource's `originId` returned by the Microsoft Graph [List resources API](/en-us/graph/api/accesspackagecatalog-list-resources?tabs=http), not its `id`. Alternatively, use the exact display name of the resource in the catalog.
- `Status`: Use `active` to enable the rule or `inactive` to disable it.
- `incompatiblePermissionSetId`: Leave this value empty to create a rule. To update an existing rule, use its **Object ID**. To find this value, select the rule name on the **Separation of duties** page to open the rule details.

The following CSV uses a resource origin ID to create an enabled finance rule and a disabled masking rule:

```csv
Name,Description,ResourceOriginId,PermissionSet1,PermissionSet2,Status,incompatiblePermissionSetId
"Separate finance data changes and auditing","Prevent the same identity from modifying finance data and independently auditing that data.","a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1","FINANCE_DATA_WRITER","FINANCE_AUDITOR","active",""
"Separate masking administration and sensitive data access","Prevent the same identity from managing masking policies and reading the sensitive data those policies protect.","a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1","MASKING_POLICY_ADMIN","SENSITIVE_DATA_READER","inactive",""
```

Alternatively, the following CSV defines the same rules using the resource's exact display name in the catalog:

```csv
Name,Description,ResourceOriginId,PermissionSet1,PermissionSet2,Status,incompatiblePermissionSetId
"Separate finance data changes and auditing","Prevent the same identity from modifying finance data and independently auditing that data.","Snowflake for Microsoft Entra ID","FINANCE_DATA_WRITER","FINANCE_AUDITOR","active",""
"Separate masking administration and sensitive data access","Prevent the same identity from managing masking policies and reading the sensitive data those policies protect.","Snowflake for Microsoft Entra ID","MASKING_POLICY_ADMIN","SENSITIVE_DATA_READER","inactive",""
```

## Update separation of duties rules

To change which roles a separation of duties rule declares incompatible, use Import separation of duties rules. Set `incompatiblePermissionSetId` in the CSV file to the rule's **Object ID**, shown when you select the rule name to view its details.

To update a rule's name, description, or enabled status, follow these steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Identity Governance Administrator](../identity/role-based-access-control/permissions-reference#identity-governance-administrator).
2. Browse to **ID Governance** &gt; **Dynamic permissions (preview)** &gt; **Separation of duties**.
3. Select the name of the rule you want to update.
4. Select **Edit**.
5. Update the name, description, or enabled status.
6. Select **Next**.
7. Select **Review and save**.
8. Select **Save changes**.

## Enable, disable, or delete separation of duties rules

To enable, disable, or delete separation of duties rules, follow these steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Identity Governance Administrator](../identity/role-based-access-control/permissions-reference#identity-governance-administrator).
2. Browse to **ID Governance** &gt; **Dynamic permissions (preview)** &gt; **Separation of duties**.
3. Select the checkbox for the rule you want to enable, disable, or delete.
4. Select **Enable selected**, **Disable selected**, or **Delete selected**.

## View separation of duties conflicts

When identities hold permissions that conflict with enabled separation of duties rules, the conflicts appear in **Detections**. For more information, see [view detections and remediations (Preview)](dynamic-permissions-review-detections-remediations).