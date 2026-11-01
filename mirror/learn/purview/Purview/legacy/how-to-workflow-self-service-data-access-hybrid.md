---
layout: Conceptual
title: Self-service hybrid data access workflows | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-workflow-self-service-data-access-hybrid
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article describes how to create and manage hybrid self-service data access workflows in Microsoft Purview.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: nayenama
ms.service: purview
ms.subservice: purview-data-map-classic
ms.topic: how-to
ms.date: 2025-02-26T00:00:00.0000000Z
ms.custom:
- template-how-to
- sfi-image-nochange
locale: en-us
document_id: 630745bd-dd5c-f297-02ba-dc0e6f99bd30
document_version_independent_id: 630745bd-dd5c-f297-02ba-dc0e6f99bd30
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-workflow-self-service-data-access-hybrid.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-workflow-self-service-data-access-hybrid
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-workflow-self-service-data-access-hybrid.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: bde9adc7-f96d-89ef-19e1-7c32e4912e8b
---

# Self-service hybrid data access workflows | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

You can use [workflows](../concept-workflow) to automate some business processes through Microsoft Purview. Self-service access workflows allow you to create a process for your users to request access to datasets they've discovered in Microsoft Purview.

Let's say your team has a new data analyst who will do some business reporting. You add that data analyst to your department's collection in Microsoft Purview. From there, they can browse through the data assets and read descriptions about the data that your department has available.

The data analyst notices that one of the Azure Data Lake Storage Gen2 accounts seems to have the exact data that they need to get started. Because a self-service access workflow has been set up for that resource, they can [request access](../how-to-request-access) to that Azure Data Lake Storage account from within Microsoft Purview.

![Screenshot of a data asset's overview page, with the button for requesting access highlighted.](../media/how-to-workflow-self-service-data-access-hybrid/request-access.png)

You can create these workflows for any of your resources across your data estate to automate the access request process. Workflows are assigned at the [collection](../data-governance-glossary) level, so they automate business processes along the same organizational lines as your permissions.

This guide shows you how to create and manage self-service access workflows in Microsoft Purview.

Note

To create or edit a workflow, you need the [workflow admin role](../data-gov-classic-permissions) in Microsoft Purview. You can also contact the workflow admin in your collection, or reach out to your collection administrator, for permissions.

## Create and enable the self-service access workflow

1. Sign in to [the Microsoft Purview governance portal](https://web.purview.azure.com/resource/) and select the management center. Three new icons appear in the table of contents.

    ![Screenshot that shows the management center menu with the new workflow section highlighted.](../media/how-to-workflow-self-service-data-access-hybrid/workflow-section.png)
2. To create new workflows, select **Authoring**. This step takes you to the workflow authoring experience.

    ![Screenshot that shows the page for authoring workflows and a list of all workflows.](../media/how-to-workflow-self-service-data-access-hybrid/workflow-authoring-experience.png)

    Note

    If the **Authoring** tab is unavailable, you don't have the permissions to author workflows. You need the [workflow admin role](../data-gov-classic-permissions).
3. To create a new self-service workflow, select the **+New** button.

    ![Screenshot that shows the page for authoring workflows, with the New button highlighted.](../media/how-to-workflow-self-service-data-access-hybrid/workflow-authoring-select-new.png)
4. You're presented with categories of workflows that you can create in Microsoft Purview. To create an access request workflow, select **Governance**, and then select **Continue**.

    ![Screenshot that shows the new workflow panel, with the Governance option selected.](../media/how-to-workflow-self-service-data-access-hybrid/select-governance.png)
5. The next screen shows all the templates that Microsoft Purview provides to create a self-service data access workflow. Select the **Data access request** template, and then select **Continue**.

    ![Screenshot that shows the new workflow panel, with the data access request template selected.](../media/how-to-workflow-self-service-data-access-hybrid/select-data-access-request.png)
6. Enter a workflow name, optionally add a description, and then select **Continue**.

    ![Screenshot that shows the name and description boxes for a new workflow.](../media/how-to-workflow-self-service-data-access-hybrid/name-and-continue.png)
7. You're presented with a canvas where the selected template is loaded by default.

    [![Screenshot that shows the workflow canvas with the selected template workflow steps displayed.](../media/how-to-workflow-self-service-data-access-hybrid/workflow-canvas-inline.png)](../media/how-to-workflow-self-service-data-access-hybrid/workflow-canvas-expanded.png#lightbox)

    The template has the following steps:

    1. Trigger when a data access request is made.
    2. Get an approval connector that specifies a user or group that will be contacted to approve the request.

    Assign data owners as approvers. Using the dynamic variable **Asset.Owner** as approvers in the approval connector will send approval requests to the data owners on the entity.

    Note

    Using the **Asset.Owner** variable might result in errors if an entity doesn't have a data owner.
8. If the condition to check approval status is approved, take the following steps:

    - If a data source is registered for [data policy enforcement](../how-to-enable-data-policy-enforcement)with the policy:
        1. Create a [self-service policy](../concept-self-service-data-access-policy).
        2. Send email to the requestor that confirms access.
    - If a data source isn't registered with the policy:
        1. Use a connector to assign [a task](../how-to-workflow-manage-requests-approvals#tasks) to a user or a Microsoft Entra group to manually provide access to the requestor.
        2. Send an email to requestor to explain that access is provided after the task is marked as complete.

    If the condition to check approval status is rejected, send an email to the requestor to say that the data access request is denied.
9. You can use the default template as it is by populating two fields:

    - Add an approver's email address or Microsoft Entra group in the **Start and wait for an approval** connector.
    - Add a user's email address or Microsoft Entra group in the **Create task and wait for task completion** connector to denote who is responsible for manually providing access if the source isn't registered with the policy.

    [![Screenshot that shows the workflow canvas with the connector for starting an approval and the connector for creating a task, along with the text boxes for assigning them.](../media/how-to-workflow-self-service-data-access-hybrid/required-fields-for-template-inline.png)](../media/how-to-workflow-self-service-data-access-hybrid/required-fields-for-template-expanded.png#lightbox)

    Note

    Configure the workflow to create self-service policies only for sources that the Microsoft Purview policy supports. To see what the policy supports, check the [documentation about data owner policies](../tutorial-data-owner-policies-storage).

    If the Microsoft Purview policy doesn't support your source, use the **Create task and wait for task completion** connector to assign [tasks](../how-to-workflow-manage-requests-approvals#tasks) to users or groups that can provide access.

    You can also modify the template by adding more connectors to suit your organizational needs.

    [![Screenshot that shows the workflow authoring canvas, with the button for adding a connector and the button for saving the new conditions.](../media/how-to-workflow-self-service-data-access-hybrid/more-connectors-inline.png)](../media/how-to-workflow-self-service-data-access-hybrid/more-connectors-expanded.png#lightbox)
10. After you define a workflow, you need to bind the workflow to a collection hierarchy path. The binding (or scoping) implies that this workflow is triggered only for data access requests in that collection.

    To bind a workflow or to apply a scope to a workflow, select **Apply workflow**. Select the scope that you want to associate with this workflow, and then select **OK**.

    ![Screenshot that shows the workflow workspace with a list of items on the menu for applying a workflow.](../media/how-to-workflow-self-service-data-access-hybrid/apply-workflow.png)

    Note

    The Microsoft Purview workflow engine will always resolve to the closest workflow that the collection hierarchy path is associated with. If the workflow engine doesn't find a direct binding, it will look for the workflow that's associated with the closest parent in the collection tree.
11. Make sure that the **Enable** toggle is on. The workflow should be enabled by default.
12. Select **Save and close** to create and enable the workflow.

    Your new workflow now appears in the list of workflows.

    ![Screenshot that shows the workflow authoring page with the newly created workflow listed among the other workflows.](../media/how-to-workflow-self-service-data-access-hybrid/completed-workflows.png)

## Edit an existing workflow

To modify an existing workflow, select the workflow, and then select the **Edit** button. You're presented with the canvas that contains the workflow definition. Modify the workflow, and then select **Save** to commit the changes.

![Screenshot that shows the workflow authoring page, with the Edit button highlighted on the top menu.](../media/how-to-workflow-self-service-data-access-hybrid/select-edit.png)

## Disable a workflow

To disable a workflow, select the workflow, and then select **Disable**.

![Screenshot that shows the workflow authoring page, with the Disable button highlighted on the top menu.](../media/how-to-workflow-self-service-data-access-hybrid/select-disable.png)

Another way is to select the workflow, select **Edit**, turn off the **Enable** toggle in the workflow canvas, and then select **Save and close**.

## Delete a workflow

To delete a workflow, select the workflow, and then select **Delete**.

![Screenshot that shows the workflow authoring page, with the Delete button highlighted on the top menu.](../media/how-to-workflow-self-service-data-access-hybrid/select-delete.png)