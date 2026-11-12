---
layout: Conceptual
title: Asset curation approval workflow | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-workflow-asset-curation
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article describes how to create and manage workflows to approve data asset curation in Microsoft Purview.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: sidnotha
ms.service: purview
ms.subservice: purview-data-map-classic
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: template-how-to, msecd-doc-authoring-1030
locale: en-us
document_id: f7a44644-be26-50db-cf74-84c0458a0585
document_version_independent_id: f7a44644-be26-50db-cf74-84c0458a0585
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-workflow-asset-curation.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-workflow-asset-curation
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-workflow-asset-curation.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: a41a3c53-2676-7e84-6fac-4cd7969b8044
---

# Asset curation approval workflow | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

This guide will take you through the creation and management of approval workflows for asset curation.

## Create and enable a new approval workflow for asset curation

1. Sign in to the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/) and select the Management center. You'll see three new icons in the table of contents.

    ![Screenshot showing the management center left menu with the new workflow section highlighted.](../media/how-to-workflow-asset-curation/workflow-section.png)
2. To create new workflows, select **Authoring** in the workflow section. This will take you to the workflow authoring experiences.

    ![Screenshot showing the authoring workflows page, showing a list of all workflows.](../media/how-to-workflow-asset-curation/workflow-authoring-experience.png)

    Note

    If the authoring tab is greyed out, you don't have the permissions to be able to author workflows. You'll need the [workflow admin role](../data-gov-classic-permissions).
3. To create a new workflow, select the **+New** button.

    ![Screenshot showing the authoring workflows page, with the plus sign New button highlighted.](../media/how-to-workflow-asset-curation/workflow-authoring-select-new.png)
4. To create **Approval workflows for asset curation** Select **Data Catalog** and select **Continue**

    ![Screenshot showing the new workflows menu, with Data Catalog selected.](../media/how-to-workflow-asset-curation/select-data-catalog.png)
5. In the next screen, you'll see all the templates provided by Microsoft Purview to create a workflow. Select the template using which you want to start your authoring experiences and select **Continue**. Each of these templates specifies the kind of action that will trigger the workflow. In the screenshot below we've selected **Update asset attributes** to create approval workflow for asset updates.

    [![Screenshot showing the new data catalog workflow menu, showing template options, with the Continue button selected.](../media/how-to-workflow-asset-curation/update-asset-attributes-continue.png)](../media/how-to-workflow-asset-curation/update-asset-attributes-continue.png#lightbox)
6. Next, enter a workflow name and optionally add a description. Then select **Continue**.

    ![Screenshot showing the new data catalog workflow menu with a name entered into the name textbox.](../media/how-to-workflow-asset-curation/name-and-continue.png)
7. You'll now be presented with a canvas where the selected template is loaded by default.

    [![Screenshot showing the workflow authoring canvas, with the selected template workflow populated in the central workspace.](../media/how-to-workflow-asset-curation/workflow-authoring-canvas-inline.png)](../media/how-to-workflow-asset-curation/workflow-authoring-canvas-inline.png#lightbox)
8. The default template can be used as it is by populating the approver's email address in **Start and Wait for approval** Connector.

    [![Screenshot showing the workflow authoring canvas, with the start and wait for an approval step opened, and the Assigned to textbox highlighted.](../media/how-to-workflow-asset-curation/add-approver-email-inline.png)](../media/how-to-workflow-asset-curation/add-approver-email-inline.png#lightbox)

    The default template has the following steps:

    1. Trigger when an asset is updated. The update can be done in overview, schema or contacts tab.
    2. Approval connector that specifies a user or group that will be contacted to approve the request.
    3. Condition to check approval status
        - If approved:
            1. Update the asset in Purview data catalog.
            2. Send an email to requestor that their request is approved, and asset update operation is successful.
        - If rejected:
            1. Send email to requestor that their asset update request is denied.
9. You can also modify the template by adding more connectors to suit your organizational needs. Add a new step to the end of the template by selecting the **New step** button. Add steps between any already existing steps by selecting the arrow icon between any steps.

    [![Screenshot showing the workflow authoring canvas, with a plus sign button highlighted on the arrow between the two top steps, and the Next Step button highlighted at the bottom of the workspace.](../media/how-to-workflow-asset-curation/modify-template-inline.png)](../media/how-to-workflow-asset-curation/modify-template-inline.png#lightbox)
10. Once you're done defining a workflow, you need to bind the workflow to a collection hierarchy path. The binding implies that this workflow is triggered only for update operation on data assets in that collection. A workflow can be bound to only one hierarchy path. To bind a workflow or to apply a scope to a workflow, you need to select ‘Apply workflow’. Select the scopes you want this workflow to be associated with and select **OK**.

    [![Screenshot showing the new data catalog workflow menu with the Apply Workflow button highlighted at the top of the workspace.](../media/how-to-workflow-asset-curation/select-apply-workflow.png)](../media/how-to-workflow-asset-curation/select-apply-workflow.png#lightbox)

    [![Screenshot showing the apply workflow window, showing a list of items that the workflow can be applied to. At the bottom of the window, the O K button is selected.](../media/how-to-workflow-asset-curation/select-okay.png)](../media/how-to-workflow-asset-curation/select-okay.png#lightbox)

    Note

    The Microsoft Purview workflow engine will always resolve to the closest workflow that the collection hierarchy path is associated with. In case a direct binding is not found, it will traverse up in the tree to find the workflow associated with the closest parent in the collection tree.
11. By default, the workflow will be enabled. To disable, toggle the Enable button in the top menu.
12. Finally select **Save and close** to create and the workflow.

    [![Screenshot showing the workflow authoring page, showing the newly created workflow listed among all other workflows.](../media/how-to-workflow-asset-curation/workflow-enabled.png)](../media/how-to-workflow-asset-curation/workflow-enabled.png#lightbox)

## Edit an existing workflow

To modify an existing workflow, select the workflow and then select **Edit** in the top menu. You'll then be presented with the canvas containing workflow definition. Modify the workflow and select **Save** to commit changes.

[![Screenshot showing the workflow authoring page, with the Edit button highlighted in the top menu.](../media/how-to-workflow-asset-curation/select-edit.png)](../media/how-to-workflow-asset-curation/select-edit.png#lightbox)

## Disable a workflow

To disable a workflow, select the workflow and then select **Disable** in the top menu. You can also disable the workflow by selecting **Edit** and changing the enable toggle in workflow canvas.

[![Screenshot showing the workflow authoring page, with the Disable button highlighted in the top menu.](../media/how-to-workflow-asset-curation/select-disable.png)](../media/how-to-workflow-asset-curation/select-disable.png#lightbox)

## Delete a workflow

To delete a workflow, select the workflow and then select **Delete** in the top menu.

[![Screenshot showing the workflow authoring page, with the Delete button highlighted in the top menu.](../media/how-to-workflow-asset-curation/select-delete.png)](../media/how-to-workflow-asset-curation/select-delete.png#lightbox)

## Limitations for asset curation with approval workflow enabled

- Lineage updates are directly stored in Purview data catalog without any approvals.