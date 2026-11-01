---
layout: Conceptual
title: Manage workflow runs | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-workflow-manage-runs
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article outlines how to manage workflow runs.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.service: purview
ms.subservice: purview-data-map-classic
ms.topic: how-to
ms.date: 2025-02-26T00:00:00.0000000Z
ms.custom: template-how-to
locale: en-us
document_id: 553c858c-1c4d-75cb-df5e-78107dc688e6
document_version_independent_id: 553c858c-1c4d-75cb-df5e-78107dc688e6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-workflow-manage-runs.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-workflow-manage-runs
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-workflow-manage-runs.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/3f837592-9b7c-422c-82fa-3523042264d7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/f37b967c-efb8-47e1-9b0d-0ab7670e3db4
platformId: c1d8b3ec-e23d-35aa-b53a-4dd4c193bada
---

# Manage workflow runs | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

This article outlines how to manage workflows that are already running.

1. To view workflow runs you triggered, sign in to the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/), select the Management center, and select **Workflow runs**.

    ![Screenshot of the management menu in the Microsoft Purview governance portal. The Workflow runs tab is highlighted.](../media/how-to-workflow-manage-runs/select-workflow-runs.png)
2. You'll be presented with the list of workflow runs and their statuses.

    ![Screenshot of the workflow runs page, showing a list of all workflow runs, their status, and their run IDs.](../media/how-to-workflow-manage-runs/workflow-runs.png)
3. You can filter the results by using workflow name, status, or time.

    ![Screenshot of the workflow runs page, with the keyword, name, status, and time filters highlighted above the list of workflows.](../media/how-to-workflow-manage-runs/filters.png)
4. Select a workflow name to see the details of the workflow run.
5. This will present a window that shows all the actions that are completed, actions that are in-progress, and the next action for that workflow run.

    ![Screenshot of the workflow runs page, with an example workflow name selected, and the workflow details page overlaid, showing workflow run, submission time, run ID, status, and a list of all steps in the request timeline.](../media/how-to-workflow-manage-runs/workflow-details.png)
6. You can select any of the actions in the request timeline to see the specific status and sub steps details.

    ![Screenshot of the workflow runs page, with the workflow details page overlaid. Some workflow run actions in the request timeline have been expanded to show more information and sub steps.](../media/how-to-workflow-manage-runs/select-stages.png)
7. You can cancel a running workflow by selecting **Cancel workflow run**.

    [![Screenshot of the workflow runs page, with the workflow details page overlaid and cancel button to cancel the workflow run.](../media/how-to-workflow-manage-runs/cancel-workflows-inline.png)](../media/how-to-workflow-manage-runs/cancel-workflows.png#lightbox)

    Note

    You can only cancel workflows that are in progress.