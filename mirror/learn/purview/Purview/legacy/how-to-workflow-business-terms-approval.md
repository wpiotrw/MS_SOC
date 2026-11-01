---
layout: Conceptual
title: Business terms approval workflow | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-workflow-business-terms-approval
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article describes how to create and manage workflows to approve business terms in Microsoft Purview.
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
document_id: fd9dea1b-fc3c-f125-29d4-07ea3e03554a
document_version_independent_id: fd9dea1b-fc3c-f125-29d4-07ea3e03554a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-workflow-business-terms-approval.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-workflow-business-terms-approval
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-workflow-business-terms-approval.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/3f837592-9b7c-422c-82fa-3523042264d7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/f37b967c-efb8-47e1-9b0d-0ab7670e3db4
platformId: 9e5f527d-2a50-7868-e7e0-f071dbe61ba8
---

# Business terms approval workflow | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

This guide will take you through the creation and management of approval workflows for business terms.

## Create and enable a new approval workflow for business terms

1. Sign in to the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/) and select the Management center. You'll see three new icons in the table of contents.

    ![Screenshot showing the management center left menu with the new workflow section highlighted.](../media/how-to-workflow-business-terms-approval/workflow-section.png)
2. To create new workflows, select **Authoring** in the workflow section. This will take you to the workflow authoring experiences.

    ![Screenshot showing the authoring workflows page, showing a list of all workflows.](../media/how-to-workflow-business-terms-approval/workflow-authoring-experience.png)

    Note

    If the authoring tab is greyed out, you don't have the permissions to be able to author workflows. You'll need the [workflow admin role](../data-gov-classic-permissions).
3. To create a new workflow, select **+New** button.

    ![Screenshot showing the authoring workflows page, with the + New button highlighted.](../media/how-to-workflow-business-terms-approval/workflow-authoring-select-new.png)
4. To create **Approval workflows for business terms** Select **Data Catalog** and select **Continue**

    ![Screenshot showing the new workflows menu, with Data Catalog selected.](../media/how-to-workflow-business-terms-approval/select-data-catalog.png)
5. In the next screen, you'll see all the templates provided by Microsoft Purview to create a workflow. Select the template using which you want to start your authoring experiences and select **Continue**. Each of these templates specifies the kind of action that will trigger the workflow. In the screenshot below we've selected **Create glossary term**. The four different templates available for business glossary are:

    - Create glossary term - when a term is created, approval will be requested.
    - Update glossary term - when a term is updated, approval will be requested.
    - Delete glossary term - when a term is deleted, approval will be requested.
    - Import terms - when terms are imported, approval will be requested.

    ![Screenshot showing the new data catalog workflow menu, showing template options, with the Continue button selected.](../media/how-to-workflow-business-terms-approval/create-glossary-term-select-continue.png)
6. Next, enter a workflow name and optionally add a description. Then select **Continue**.

    ![Screenshot showing the new data catalog workflow menu with a name entered into the name textbox.](../media/how-to-workflow-business-terms-approval/name-and-continue.png)
7. You'll now be presented with a canvas where the selected template is loaded by default.

    [![Screenshot showing the workflow authoring canvas, with the selected template workflow populated in the central workspace.](../media/how-to-workflow-business-terms-approval/workflow-authoring-canvas-inline.png)](../media/how-to-workflow-business-terms-approval/workflow-authoring-canvas-expanded.png#lightbox)
8. The default template can be used as it is by populating the approver's email address in **Start and Wait for approval** Connector.

    [![Screenshot showing the workflow authoring canvas, with the start and wait for an approval step opened, and the Assigned to textbox highlighted.](../media/how-to-workflow-business-terms-approval/add-approver-email-inline.png)](../media/how-to-workflow-business-terms-approval/add-approver-email-expanded.png#lightbox)

    The default template has the following steps:

    1. Trigger when a glossary term is created/updated/deleted/imported depending on the template selected.
    2. Approval connector that specifies a user or group that will be contacted to approve the request.
    3. Condition to check approval status
        - If approved:
            1. Create/update/delete/import the glossary term
            2. Send an email to requestor that their request is approved, and term CUD (create, update, delete) operation is successful.
        - If rejected:
            1. Send email to requestor that their request is denied.
9. You can also modify the template by adding more connectors to suit your organizational needs. Add a new step to the end of the template by selecting the **New step** button. Add steps between any already existing steps by selecting the arrow icon between any steps.

    [![Screenshot showing the workflow authoring canvas, with a + button highlighted on the arrow between the two top steps, and the Next Step button highlighted at the bottom of the workspace.](../media/how-to-workflow-business-terms-approval/modify-template-inline.png)](../media/how-to-workflow-business-terms-approval/modify-template-expanded.png#lightbox)
10. Once you're done defining a workflow, you need to bind the workflow to a glossary hierarchy path. The binding implies that this workflow is triggered only for CUD operations within the specified glossary hierarchy path. A workflow can be bound to only one hierarchy path. To bind a workflow or to apply a scope to a workflow, you need to select ‘Apply workflow’. Select the scopes you want this workflow to be associated with and select **OK**.

    ![Screenshot showing the new data catalog workflow menu with the Apply Workflow button highlighted at the top of the workspace.](../media/how-to-workflow-business-terms-approval/select-apply-workflow.png)

    ![Screenshot showing the apply workflow window, showing a list of items that the workflow can be applied to. At the bottom of the window, the O K button is selected.](../media/how-to-workflow-business-terms-approval/select-okay.png)

    Note

    - The Microsoft Purview workflow engine will always resolve to the closest workflow that the term hierarchy path is associated with. In case a direct binding is not found, it will traverse up in the tree to find the workflow associated with the closest parent in the glossary tree.
    - Import terms can only be bound to root glossary path as the .CSV can contain terms from different hierarchy paths.
11. By default, the workflow will be enabled. To disable, toggle the Enable button in the top menu.
12. Finally select **Save and close** to create the workflow.

## Edit an existing workflow

To modify an existing workflow, select the workflow and then select **Edit** in the top menu. You'll then be presented with the canvas containing workflow definition. Modify the workflow and select **Save** to commit changes.

![Screenshot showing the workflow authoring page, with the Edit button highlighted in the top menu.](../media/how-to-workflow-business-terms-approval/select-edit.png)

## Disable a workflow

To disable a workflow, select the workflow and then select **Disable** in the top menu. You can also disable the workflow by selecting **Edit** and changing the enable toggle in workflow canvas.

![Screenshot showing the workflow authoring page, with the Disable button highlighted in the top menu.](../media/how-to-workflow-business-terms-approval/select-disable.png)

## Delete a workflow

To delete a workflow, select the workflow and then select **Delete** in the top menu.

![Screenshot showing the workflow authoring page, with the Delete button highlighted in the top menu.](../media/how-to-workflow-business-terms-approval/select-delete.png)

## Limitations for business terms with approval workflow enabled

- Non-approved glossary terms aren't saved in Purview catalog.
- The behavior of tagging terms to assets/schemas is same as today. That is, previously created draft terms can be tagged to assets/schemas.