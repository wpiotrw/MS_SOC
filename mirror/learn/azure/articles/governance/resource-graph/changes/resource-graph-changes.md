---
layout: Conceptual
title: Analyze changes to your Azure resources with Change Analysis - Azure Resource Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/resource-graph/changes/resource-graph-changes
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/133/azure
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
author: kgremban
learn_banner_products:
- azure
ms.author: kgremban
ms.service: azure-resource-graph
description: Learn to use the Azure Resource Graph Change Analysis tool to explore and analyze changes in your resources.
ms.date: 2025-10-23T00:00:00.0000000Z
ms.topic: concept-article
locale: en-us
document_id: 1db95e37-240f-746a-b12c-26f803ad5dbf
document_version_independent_id: 68a8f69e-518a-7e2d-4abf-4dfb42eb659c
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/resource-graph/changes/resource-graph-changes.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/resource-graph/changes/resource-graph-changes
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/resource-graph/changes/resource-graph-changes.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3928677-9b71-43a6-875f-004dc4f98b65
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6bbc70ca-58b2-4c69-8249-28ec92c08029
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: f3973511-0510-5f52-684a-b1203465b41d
---

# Analyze changes to your Azure resources with Change Analysis - Azure Resource Graph | Microsoft Learn

Resources change through the course of daily use, reconfiguration, and even redeployment. While most change is by design, sometimes it can break your application. With the power of Azure Resource Graph, you can find when a resource changed due to a [control plane operation](../../../azure-resource-manager/management/control-plane-and-data-plane) sent to the Azure Resource Manager URL.

Change Analysis goes beyond standard monitoring solutions, alerting you to live site issues, outages, or component failures and explaining the causes behind them.

## How it works

Change Analysis ingests data into Resource Graph for queries and to power the portal experience. Change Analysis data can be accessed using:

- The `POST Microsoft.ResourceGraph/resources` API *(preferred)* for querying across tenants and subscriptions.
- The following APIs *(under a specific scope, such as `LIST` changes and snapshots for a specific virtual machine):*
    - `GET/LIST Microsoft.Resources/Changes`
    - `GET/LIST Microsoft.Resources/Snapshots`

When a resource is created, updated, or deleted via the Azure Resource Manager control plane, Resource Graph uses its [Change Actor functionality](get-resource-changes) to identify the changes.

Note

Currently, Azure Resource Graph doesn't:

- Observe changes made to a resource's data plane API, such as writing data to a table in a storage account.
- Support file and configuration changes over App Service.

## Change Analysis in the portal

Change Analysis experiences across the Azure portal are powered using the Azure Resource Graph [`Microsoft.ResourceGraph/resources` API](/en-us/rest/api/azureresourcegraph/resourcegraph/resources/resources). You can query this API for changes made to many of the Azure resources you interact with, including App Services (`Microsoft.Web/sites`) or Virtual Machines (`Microsoft.Compute/virtualMachines`).

The Azure Resource Graph Change Analysis portal experience provides:

- An onboarding-free experience, giving all subscriptions and resources access to change history.
- Tenant-wide querying, rather than select subscriptions.
- Change history summaries aggregated into cards at the top of the new Resource Graph Change Analysis.
- More extensive filtering capabilities.
- Improved accuracy and relevance of *changed by* information, using *Change Actor* functionality.

[Learn how to view the new Change Analysis experience in the portal.](view-resource-changes)

## Supported resource types

Change Analysis supports changes to resource types from the following Resource Graph tables:

- [`resources`](../reference/supported-tables-resources#resources)
- [`resourcecontainers`](../reference/supported-tables-resources#resourcecontainers)
- [`healthresources`](../reference/supported-tables-resources#healthresources)

You can compose and join tables to project change data any way you want.

## Data retention

Changes are queryable for 14 days. For longer retention, you can [integrate your Resource Graph query with Azure Logic Apps](../tutorials/logic-app-calling-arg) and manually export query results to any of the Azure data stores like [Log Analytics](/en-us/azure/azure-monitor/logs/log-analytics-overview) for your desired retention.

## Cost

You can use Azure Resource Graph Change Analysis at no extra cost.

## Send feedback for more data

Submit feedback via [the Change Analysis experience](view-resource-changes) in the Azure portal.