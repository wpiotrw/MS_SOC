---
layout: Conceptual
title: View resource changes in the Azure portal - Azure Resource Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/resource-graph/changes/view-resource-changes
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
description: View resource changes with Azure Resource Graph Change Analysis in the Azure portal.
ms.date: 2025-10-28T00:00:00.0000000Z
ms.topic: how-to
ms.custom: sfi-image-nochange
locale: en-us
document_id: 7b899f10-6e93-04c1-4750-d2982319506e
document_version_independent_id: ed7b8b61-2eea-54a1-6e58-af93f4c51355
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/resource-graph/changes/view-resource-changes.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/resource-graph/changes/view-resource-changes
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/resource-graph/changes/view-resource-changes.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3928677-9b71-43a6-875f-004dc4f98b65
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6bbc70ca-58b2-4c69-8249-28ec92c08029
platformId: 35cbabb3-4634-f674-6b9a-8300d5b641e0
---

# View resource changes in the Azure portal - Azure Resource Graph | Microsoft Learn

Change Analysis provides data for various management and troubleshooting scenarios, helping you understand which changes to your application caused which breaking issues. In addition to [querying Resource Graph for resource changes](get-resource-changes), you can also view all changes to your applications via the Azure portal.

In this guide, you learn where to find Change Analysis in the portal and how to view, filter, and query changes.

## Access Change Analysis screens

Change Analysis automatically collects snapshots of change data for all Azure resources, without needing to limit to a specific subscription or service. To view change data, search for and select **Change Analysis** in the Azure portal search bar.

![Screenshot of searching for Change Analysis in the Azure portal.](media/view-resource-changes/search-change-analysis.png)

![Screenshot of the Change Analysis page.](media/view-resource-changes/change-analysis-page.png)

## Filter and sort Change Analysis results

You can use the filters and sorting categories in the Azure portal to weed out results unnecessary to your project.

### Filter

Use any of the filters available at the top of **Change Analysis** to narrow down the change history results to your specific needs.

![Screenshot of the filters available for Change Analysis that help narrow down the Change Analysis results.](media/view-resource-changes/changes-filter.png)

| Filter | Description |
| --- | --- |
| Subscription | This filter is in-sync with the Azure portal subscription selector. It supports multiple-subscription selection. |
| Resource group | Select the resource group to scope to all resources within that group. By default, all resource groups are selected. |
| Time span | Limit results to resources changed within a certain time range. |
| Change types | Types of changes made to resources. |
| Resource types | Select **Add filter** to add this filter. Search for resources by their resource type, like virtual machine. |
| Resource names | Select **Add filter** to add this filter. Filter results based on their resource name. |
| Correlation IDs | Select **Add filter** to add this filter. Filter resource results by [the operation's unique identifier](../../../expressroute/get-correlation-id). |
| Changed by types | Select **Add filter** to add a tag filter. Filter resource changes based on the descriptor of who made the change. |
| Client types | Select **Add filter** to add this filter. Filter results based on how the change is initiated and performed. |
| Operations | Select **Add filter** to add this filter. Filter resources based on [their resource provider operations](../../../role-based-access-control/resource-provider-operations). |
| Changed by | Select **Add filter** to add a tag filter. Filter the resource changes by who made the change. |

### Sort

In **Change Analysis**, you can organize the results into groups using the **Group by...** drop-down menu.

![Screenshot of the drop-down for selecting how to group Change Analysis results.](media/view-resource-changes/change-grouping.png)

| Group by... | Description |
| --- | --- |
| None | Set to this grouping by default and applies no group settings. |
| Subscription | Sorts the resources into their respective subscriptions. |
| Resource Group | Groups resources based on their resource group. |
| Resource Type | Groups resources based on their Azure service type. |
| Change Type | Organizes resources based on the collected change type. Values include *Create*, *Update*, and *Delete*. |
| Client Type | Sorts by how the change is initiated and performed. Values include *CLI* and *ARM template*. |
| Changed By | Groups resource changes by who made the change. Values include user email ID or subscription ID. |
| Changed By Type | Groups resource changes based on the descriptor of who made the change. Values include *User*, *Application*. |
| Operation | Groups resources based on [their resource provider operations](../../../role-based-access-control/resource-provider-operations). |
| Correlation ID | Organizes the resource changes by [the operation's unique identifier](../../../expressroute/get-correlation-id). |

### Edit columns

You can add and remove columns, or change the column order in the Change Analysis results. In **Change Analysis** select **Manage view** &gt; **Edit columns**.

![Screenshot of the drop-down for selecting the option for editing columns for the results.](media/view-resource-changes/manage-results-view.png)

In the **Edit columns** pane, make your changes and then select **Save** to apply.

![Screenshot of the Edit columns pane options.](media/view-resource-changes/edit-columns-pane.png)

#### Add a column

Click **+ Add column** and select a column property from the dropdown in the new column field.

![Screenshot of the drop-down for selecting a new column.](media/view-resource-changes/select-new-column.png)

#### Delete a column

To delete a column, select the trash can icon.

![Screenshot of the trash can icon to delete a column.](media/view-resource-changes/delete-column.png)

#### Reorder columns

Change the column order by either dragging and dropping a field, or selecting a column and clicking **Move up** and **Move down**.

![Screenshot of selecting a column to move up or down in the order.](media/view-resource-changes/reorder-columns.png)

#### Reset to default

Select **Reset to defaults** to revert your changes.

![Screenshot of where to reset to the default column settings.](media/view-resource-changes/reset-columns-default.png)