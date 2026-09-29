---
layout: Conceptual
title: KQL activity - Microsoft Fabric | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/fabric/data-factory/kql-activity
breadcrumb_path: /fabric/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Fabric
show_latex: false
feedback_system: Standard
feedback_help_link_url: https://community.fabric.microsoft.com/datafactory
feedback_help_link_type: ask-the-community
feedback_product_url: https://ideas.fabric.microsoft.com/?forum=ea587140-44f9-ed11-8849-000d3a4ef41d
ms.service: fabric
author: whhender
ms.author: whhender
ms.subservice: data-factory
search.app:
- fabric-datafactory-docs
description: Learn how to add a KQL activity to a pipeline and use it to connect to an Azure Data Explorer instance and run a query in Kusto Query Language (KQL).
ms.reviewer: abnarain
ms.topic: how-to
ms.custom: pipelines
ms.date: 2023-11-15T00:00:00.0000000Z
locale: en-us
document_id: 320b769d-0058-3907-a426-cfa9ebd5ee14
document_version_independent_id: 320b769d-0058-3907-a426-cfa9ebd5ee14
original_content_git_url: https://github.com/MicrosoftDocs/fabric-docs-pr/blob/live/docs/data-factory/kql-activity.md
site_name: Docs
depot_name: MSDN.fabric-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.fabric-docs/{branchName}{pdfName}
asset_id: data-factory/kql-activity
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/data-factory/kql-activity.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/26e1a60c-4ce1-41de-b2d1-e5f3b7e68e6e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e7cd09c2-9e9a-4f0d-b160-c15783f45b1f
- https://authoring-docs-microsoft.poolparty.biz/devrel/655f39c4-21c5-49d3-8367-a1f9c1a0b930
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad3bd485-5ca9-4865-afde-baec02586899
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1d337399-0ca4-4b4c-acef-8df37820e018
- https://authoring-docs-microsoft.poolparty.biz/devrel/d30b39f7-a405-488d-84ef-d6d5296ad372
platformId: fa166f67-2e70-f0ef-e19a-11f396ae614f
---

# KQL activity - Microsoft Fabric | Microsoft Learn

The KQL activity in Data Factory for Microsoft Fabric allows you to run a query in Kusto Query Language (KQL) against an Azure Data Explorer instance.

## Prerequisites

To get started, you must complete the following prerequisites:

- You must have access to a Microsoft Fabric tenant with a provisioned [capacity](/en-us/fabric/enterprise/plan-capacity). You can [try Fabric with a free trial](../fundamentals/fabric-trial).
- A Fabric [workspace](../fundamentals/create-workspaces) assigned to that capacity.

## Add a KQL activity to a pipeline with UI

To use a KQL activity in a pipeline, complete the following steps:

### Creating the activity

1. Create a new pipeline in your workspace.
2. Search for KQL in the pipeline **Activities** pane, and select it to add it to the pipeline canvas.

    Note

    You may need to expand the menu and scroll down to see the KQL activity as highlighted in the screenshot below.

    ![Screenshot of the Fabric UI with the Activities pane and KQL activity highlighted.](media/kql-activity/add-kql-activity-to-pipeline.png)
3. Select the new KQL activity on the pipeline editor canvas if it isn't already selected.

    ![Screenshot showing the General settings tab of the KQL activity.](media/kql-activity/kql-activity-general-settings.png)

Refer to the [**General** settings](activity-overview#general-settings) guidance to configure the **General** settings tab.

### KQL activity settings

1. Select the **Settings** tab, and then select your **KQL Database** connection from the dropdown, or create a new one. If you select a workspace data store you can use dynamic content to parameterize the database selection by selecting the **Add dynamic content** option that appears in the dropdown.
2. Then provide a KQL query to execute against the selected database for the **Command** property. You can use dynamic content in the query by selecting the **Add dynamic content** link that appears when the text box is selected.

    ![Screenshot showing the Settings tab of the KQL activity highlighting the Command property and showing where its Add dynamic content link appears.](media/kql-activity/kql-activity-settings.png)
3. Finally, specify a command timeout or leave the default timeout of 20 minutes. You can use dynamic content for this property too.

## Save and run or schedule the pipeline

The KQL activity might typically be used with other activities. After you configure any other activities required for your pipeline, you can save and run or schedule the pipeline.

Switch to the **Home** tab at the top of the pipeline editor and select the save button to save your pipeline. Select **Run** to run it directly or **Schedule** to schedule runs at specific times or intervals. For more information on pipeline runs, see: [schedule pipeline runs](pipeline-runs).

![Screenshot showing the Home tab in the pipeline editor with the tab name, Save, Run, and Schedule buttons highlighted.](includes/media/save-run-schedule-pipeline/save-run-schedule-pipeline.png)

After running, you can monitor the pipeline execution and view run history from the **Output** tab below the canvas.

## Known limitations

- **Cross‑workspace deployment limitation:** When a pipeline containing a KQL activity is deployed across workspaces using deployment pipelines, workspace‑specific linked service properties are not remapped and continue to reference the source workspace. This can cause pipeline runs in the target workspace to fail with UserErrorKustoReadFailed / EntityNotFoundException.

The workaround is to use workspace variables (Variable Library) for all workspace‑specific connection properties and reference them via endpointVariableLibrary, artifactIdVariableLibrary, and workspaceIdVariableLibrary.