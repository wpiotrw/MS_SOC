---
layout: Conceptual
title: Use external APIs in Workflows | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-use-workflow-http-connector
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Work with external APIs using HTTP connector and Parse JSON in Microsoft Purview workflows.
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
document_id: 74193ccd-b22b-2b60-4770-4eca8c757b22
document_version_independent_id: 74193ccd-b22b-2b60-4770-4eca8c757b22
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-use-workflow-http-connector.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-use-workflow-http-connector
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-use-workflow-http-connector.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 5f2b7304-2c6e-1c9a-99e4-2c4e56cc7ed9
---

# Use external APIs in Workflows | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

You can use [workflows](../concept-workflow) to automate some business processes through Microsoft Purview, and the HTTP connector and parse JSON action allow you to integrate your workflows with external applications.

## HTTP connector

HTTP connectors use Representational State Transfer (REST) architecture, which allows Microsoft Purview workflows to interact directly with non-Microsoft applications using web requests.

HTTP connector is available in all workflow templates.

Note

To create or edit a workflow, you need the [workflow admin role](../data-gov-classic-permissions) in Microsoft Purview. You can also contact the workflow admin in your collection, or reach out to your collection administrator, for permissions.

1. To add an HTTP connector, select the **+** icon in the template where you want to add and select HTTP connector.

    ![Screenshot of how to add HTTP connector.](../media/how-to-use-workflow-http-connector/add-http-connector.png)
2. Once you select HTTP connector, fill the following parameters:

    1. **Host** - Request URL you want to call when this connector is executed.
    2. **Method** - Select one of the following methods. GET, PUT, PATCH, POST and DELETE. These methods correspond to create, read, update and delete operations.
    3. **Path** - Optionally you can enter request URL Path. You can use dynamic content for this parameter.
    4. **Headers** - Optionally, you can enter HTTP headers. HTTP headers let the client and the server pass additional information with an HTTP request or response
    5. **Queries** - Optionally, you can pass queries.
    6. **Body** - Optionally, you can pass HTTP body while invoking the URL
    7. **Authentication** - HTTP connector is integrated with your [Microsoft Purview credentials](../data-map-data-scan-credentials). Depending on the URL, you can invoke one of these three types:
        1. **None** (no authentication)
        2. **Basic authentication** - using a [basic authentication credential you've already created](../data-map-data-scan-credentials#create-a-new-credential).
        3. **Service principal** - using a [service principal credential you've already created](../data-map-service-principal), and an audience. [The audience will be the intended consumer of the access token](/en-us/entra/identity-platform/msal-client-application-configuration#application-audience). The Microsoft Purview audience for example: `https://purview.azure.net/.default` Make sure your service principal is authorized to call corresponding services, like ARM.

    ![Screenshot of how to add HTTP connector properties.](../media/how-to-use-workflow-http-connector/add-http-properties.png)
3. By default, secure settings are turned on for HTTP connectors. To turn OFF secure inputs and outputs select the ellipsis icon (**...**) to go to settings.

    ![Screenshot of how to add HTTP connector settings.](../media/how-to-use-workflow-http-connector/add-http-settings.png)
4. You're now presented with the settings for HTTP connector and you can turn secure inputs and outputs OFF.

    ![Screenshot of how to add HTTP connector secure input and outputs.](../media/how-to-use-workflow-http-connector/add-http-secure.png)

## Parse JSON action

The parse JSON action in workflows allows you to take an incoming JSON from HTTP (or any other action/connector), and parse the JSON to extract values for use in your workflow.

The parse JSON action is available in all workflows.

![Screenshot of the workflows parse JSON action, showing its parameters filled out with sample data.](../media/how-to-use-workflow-http-connector/parse-json-action.png)

The parse JSON action has two parameters:

- Content - a variable that should contain the JSON you want to parse.
- Schema - the schema of the incoming JSON, which allows the workflow to parse the incoming information. You can supply your own, or use the **Generate from sample** button. If you generate from a sample, you'll enter a sample JSON payload and a schema will be automatically generated for you.

Actions and connectors in the workflow after the parse JSON action will be able to use the values extracted from the JSON by selecting **Add dynamic content** for any parameters.

![Screenshot of another connector with values from the Parse JSON action added.](../media/how-to-use-workflow-http-connector/add-dynamic-content.png)