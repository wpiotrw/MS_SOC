---
layout: Conceptual
title: Workflows in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-workflows
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: nidought
ms.date: 2026-07-31T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.localizationpriority: medium
search.appverid:
- MET150
- MOE150
description: Learn how to create workflows in Microsoft Purview Unified Catalog to automate your business processes.
locale: en-us
document_id: 14f7e180-111d-04ab-2413-2c39bebb7a33
document_version_independent_id: 14f7e180-111d-04ab-2413-2c39bebb7a33
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-workflows.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-workflows
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-workflows.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/43093068-2dda-408b-b3fe-dfd705c84f78
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/e453d60d-ba7e-43bc-8028-ec38e6b62512
platformId: 85de0001-d353-e3e5-1ea0-1fb975ea17c0
---

# Workflows in Unified Catalog | Microsoft Learn

Workflows in Microsoft Purview Unified Catalog provide a centralized, automated way to manage approval scenarios, such as granting access to data products and publishing data products and glossary terms.

Workflows are automated, repeatable sets of actions or business processes that users can establish to streamline operations in their organization. The available workflows can automate the approval processes for requesting access to, and publishing, data products. Governance teams can use the workflows to automate their desired approval processes.

## Workflow types

You can set up customizable workflows in Unified Catalog for these processes:

- Granting access to data products
- Publishing data products and glossary terms

You set up these workflows directly within Unified Catalog. The setup process follows a similar process as the existing data product access request, but gives more options to customize. The new workflows go through a new requests and approvals tab, but with the same out-of-the-box options available for configuration.

Note

Access workflows can be applied to a governance domain or a single data product. Publication workflows can only apply to governance domains.

## Prerequisites

To create and manage workflows, users need to hold the **Governance Domain Creator** role for publication workflows, and the **Data Product Owner** role for data product access workflows. Learn more about [Unified Catalog roles](data-governance-roles-permissions#unified-catalog-roles).

## Data product access workflow

A data product access workflow allows you to manage [data product access requests](unified-catalog-data-product-access-policies) and generate approvals. A data product owner can only create a workflow for the data products in their governance domain.

If you previously created [workflows in the classic catalog experience](concept-workflow), you should update your workflow to the new experience by creating a new workflow for data access at the data product level. If you don't create a new workflow, your existing workflow continues to work.

For any new data products you create, you can only use the new workflow experience described in this article.

### Steps to create workflow

You can create workflows from either a data product's details page or from the **Workflows** page.

1. In Unified Catalog, start from either of these locations:

    - **From a data product**:

        1. Under **Catalog management**, select **Data products**, then select the data product you want to create a workflow for.
        2. On the data product's details page, select **Manage policies**.
        3. On the **Manage access policies** flyout pane, under **Approval requirements**, either add your approvers like you're used to **or** select **New Workflow** to edit the approver process. If you choose to use the approvers list in the flyout page, the workflow is automatically generated for you when you select **Save**.
    - **From the Workflows page**:

        1. Under **Process automation**, select **Workflows**.
2. Starting from either location in step 1, you arrive at the **Workflows** page. Select **New**.
3. In the **New workflow** flyout pane, enter a **Name** and an optional description.
4. At **Workflow category**, select **Data product access** from the list.
5. Select **Create**. A base template for the workflow opens, which is where you build your workflow.
6. At **Start and wait for an approval**:

    - Select an **Approval type**:
        - **Pending on all**: If there are multiple approvers for the access request, all approvers must approve the request.
        - **Pending on any**: Only one approver needs to approve the request.
    - The **Title** is automatically filled in as **Approval for data access request**.
    - At **Assigned to**, enter the user name.
7. At **Condition**, select the condition you want to apply, such as **and** or **or**, and set the approval outcome.
8. The **Condition** leads to **If yes** and **If no** outcomes. **If yes** results in the approval of the access request. **If no** results in the rejection of the access request. Within the **Yes** and **No** outcomes, you can add more actions to create extra layers based on conditions.
9. When you're done setting conditions, select **Set scope** at the top right of the page.
10. On the **Set scope** flyout pane, expand the list under the governance domains listed to view its data products. Select one data product or an entire domain of data products. Then select **Save**.

### Limitations

1. The current version doesn't support variables for contacts, metadata during the workflow, or email templates.
2. This set of workflows doesn't include external connectors.
3. You can only configure data product access workflows for a single data product or the whole governance domain of data products for the same list of approvers. You can't use these workflows for multiple data products or many domains.
4. If requests exist for a user on a data product in either workflow experience, the user can't create a new request. When you switch to the new workflow, remove all previously approved requests and have users recreate their requests if needed.
5. If the privacy approver is hard coded in a workflow, it won't prepopulate in the request form when filled in by the data consumer.
6. Security groups can be added for approvals, but someone from that group needs to manually approve the access request. This requirement applies for both the privacy approver and data product approver.
7. A security group added to be any approver must be email enabled to receive emails notification during workflow runs.
8. A group can be added to the access request if there are **zero** attestations on that data product. If attestations are required for a data product, only users and service principal requests are supported.
9. Data access workflows experience and APIs only support user principals. Service principals won't work in the workflow roles.

## Data product and glossary term publish workflow

A **Catalog curation** publish workflow lets you automate the [publishing of data products](unified-catalog-data-products-create-manage#publish-draft-and-expire) and [glossary terms](unified-catalog-glossary-terms-create-manage#publish-terms) for a specific governance domain. It enables governance domain data product owners and data stewards to collaborate more broadly during the drafting process but ensures a final review before publication to the catalog.

If you previously created [workflows in the classic catalog experience](concept-workflow), you can update your workflow to the new experience by creating a new workflow. If you don't create a new workflow, your existing workflow continues to work.

For any new data products and glossary terms you create, you can only use the new workflow experience described in this article.

### Steps to create workflow

1. In Unified Catalog, under **Process automation**, select **Workflows**. You arrive at the **Workflows** page.
2. Select **New**.
3. In the **New workflow** flyout pane, enter a **Name** and an optional description.
4. At **Workflow category**, select **Catalog curation** from the list.
5. At **Workflow type**, select **Data product publish** or **Term publish**.
6. Select **Create**. A base template for the workflow opens, which is where you build your workflow.
7. At **Start and wait for an approval**:

    - Select an **Approval type**:
        - **Pending on all**: If there are multiple approvers for publishing, all approvers must approve the publish.
        - **Pending on any**: Only one approver needs to approve the publish.
    - The **Title** is automatically filled in as **Approval for data product publish**.
    - At **Assigned to**, enter the user name XYZ.
8. At **Condition**, select the condition you want to apply, such as **and** or **or**, and set the approval outcome.
9. The **Condition** leads to **If yes** and **If no** outcomes. **If yes** results in publishing the data product. **If no** results in the data product remaining in a draft state. Within the **Yes** and **No** outcomes, you can add more actions to create extra layers based on conditions.
10. When you're done setting conditions, select **Set scope** at the top right of the page.
11. On the **Set scope** flyout pane, expand the list under the governance domains listed. Select one governance domain for the publication workflow. Then select **Save**.

## Adding actions

At the **If yes** and **If no** outcomes, add other actions to the workflow to build multiple levels and tiers based on the conditions. The available actions are:

- Start and wait for approval
- Condition
- Approve data subscription
- Complete data subscription
- Reject data subscription
- Send email notifications