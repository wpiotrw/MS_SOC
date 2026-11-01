---
layout: Conceptual
title: How to build custom lineage in Microsoft Purview using REST APIs | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-purview-custom-lineage-api-user-guide
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article provides the steps to create custom lineage entries in Microsoft Purview with the REST APIs. You can use this guide to build custom lineage with the REST APIs, add new information, or stitch together existing lineage entries.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: jife
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.date: 2025-02-24T00:00:00.0000000Z
locale: en-us
document_id: 5adc2312-0d89-d7d6-66c1-66e66f6fbcff
document_version_independent_id: 5adc2312-0d89-d7d6-66c1-66e66f6fbcff
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-purview-custom-lineage-api-user-guide.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-purview-custom-lineage-api-user-guide
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-purview-custom-lineage-api-user-guide.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 592ba069-b7a6-c652-68ff-80166a774220
---

# How to build custom lineage in Microsoft Purview using REST APIs | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

This article provides the steps to create data lineage entries using the REST API in the Microsoft Purview Data Catalog. In scenarios where the automatically generated lineage in Microsoft Purview is incomplete or missing, lineage can be custom built either [manually in the Microsoft Purview portal](../data-gov-classic-lineage-user-guide#manual-lineage) or using the REST APIs. This article focuses on using REST APIs that can overcome manual lineage known limitations and provide more options.

## Background

The ability to show the lineage between datasets is one of Microsoft Purview's important platform features. Systems like Data Factory, Data Share, and Power BI capture the lineage of data as it moves. In certain situations, Microsoft Purview's automatically generated lineage is incomplete or missing for practical visualization and enterprise reporting purposes. In those scenarios, custom lineage reporting is supported by Apache Atlas hooks and the REST API.

Using the REST APIs to build custom lineage allows you to overcome some of manual lineage's limitations as described in the following articles:

- [Power BI lineage in Microsoft Purview](../data-map-lineage-power-bi)
- [Microsoft Purview manual lineage user guide](../data-gov-classic-lineage-user-guide#manual-lineage)
- [Lineage - known limitations](../data-gov-classic-lineage-user-guide#known-limitations)

The rest of this article explains the use of Microsoft Purview REST APIs to build and report custom lineage on Microsoft Purview.

## Prerequisites

- For step-by-step guidance on how to use the Purview Python SDK Packages, refer [Purview Python SDK Tutorial](../data-gov-python-sdk#install-the-python-packages) and [Exploring Purview’s REST API with Python](https://techcommunity.microsoft.com/t5/azure-architecture-blog/exploring-purview-s-rest-api-with-python/ba-p/2208058)
- For step-by-step guidance on how to use the [*Purview REST APIs*](/en-us/rest/api/purview/), refer [Purview Python SDK Tutorial](../data-gov-python-sdk#install-the-python-packages)

## Scenarios

There are two use cases when building custom lineage becomes necessary:

A. Create new entities created and link them with lineage

B. Link existing entities or lineage to another existing entity or lineage

### A. Create new entities and link them with lineage

As an example, lineage needs to be reported between entities A & B, but A & B don't exist currently.

To create the entities A & B, invoke the Microsoft Purview REST API: [*Entity - Bulk Create Or Update - REST API*](/en-us/rest/api/purview/datamapdataplane/entity/bulk-create-or-update?view=rest-purview-datamapdataplane-2023-09-01&amp;tabs=HTTP&amp;preserve-view=true)

```http
POST https://{accountname}.purview.azure.com/datamap/api/atlas/v2/entity/bulk?api-version=2023-09-01
```

```python
sample_entity_json = '{"entity": {"status": "ACTIVE","version": 0,"name": ENTITY_A"}.......{"entity": ........}}'
#Send POST JSON containing entities to be created
CreateOrUpdateEntitesUrl = 'https://<purview_account_name>.purview.azure.com/datamap/api/atlas/v2/entity/bulk'
EntitiesResponse = requests.post(CreateOrUpdateEntitesUrl, json = json.loads(sample_entity_json) ,headers=headers)
entitiesRes = json.loads(EntitiesResponse.text)
```

*API Response "201 Created" indicates entities are successfully created and their respective GUIDs are contained in the output JSON.*

Now that the entities A & B are created, move to step B to link the entities in the lineage chain using the same REST API.

### B. Link existing entities or lineage to another existing entity or lineage

- If the number of entities to be linked isn't time or resource intensive (for example, less than 20-30 entities), you can connect the lineage manually in the Microsoft Purview portal. Follow the [manual lineage user guide](../data-gov-classic-lineage-user-guide#manual-lineage) for steps to manually create lineage connections.
- If you have a high number of lineage connections to make, the process needs to be automated, or if manual lineage using the Microsoft Purview portal isn't feasible, proceed with the API process of linking and building custom lineage.

Custom Lineage JSON Payload:

Execute the *POST /entity/bulk*[*Entity - Bulk Create Or Update - REST API*](/en-us/rest/api/purview/datamapdataplane/entity/bulk-create-or-update?view=rest-purview-datamapdataplane-2023-09-01&amp;tabs=HTTP&amp;preserve-view=true) using the payload as illustrated:

```http
POST https://{accountname}.purview.azure.com/datamap/api/atlas/v2/entity/bulk?api-version=2023-09-01
```

```python
sample_entity_json = '{
  "entities": [
    {
      "status": "ACTIVE",
      "version": 1,
      "typeName": "Process",
      "attributes": {
        "inputs": [
          {
            "guid": "24558fd8-9cdc-47de-9310-56a58108bab0",
            “guid”: “27163581-9aca-212a-782a-213612639abc”
          }
        ],
        "outputs": [
          {
            "guid": "e33c694a-2c4f-4cae-8c27-06f6f6f60000"
          }
        ],
        "qualifiedName": "cassandra://query",
        "name": "query"
      }
    }
  ]
}'

#In this code snippet, we send the JSON as POST request containing the two GUIDs as input and "output" GUID as output. This creates lineage with 2 directional inputs and 1 directional output.
#Note: using the same API and SDK code you can create lineage with any number of inputs, any number of processes in between, any number of typedefs and any number of outputs.
#The API/SDK method is the most flexible and versatile menthod of creating lineage.
 
CreateLineageEntitesUrl = 'https://<purview_account_name>.purview.azure.com/datamap/api/atlas/v2/entity/bulk'
EntitiesResponse = requests.post(CreateLineageEntitesUrl, json = json.loads(sample_entity_json),headers=headers)
entitiesRes = json.loads(EntitiesResponse.text)
```

This JSON payload creates the custom lineage. It works for already existing assets whose GUIDs are supplied in the "inputs" JSON. For example "guid": "24558fd8-9cdc-47de-9310-56a58108bab0" and "27163581-9aca-212a-782a-213612639abc" refers to the directional input of the lineage and "guid": "e33c694a-2c4f-4cae-8c27-06f6f6f60000" refers to the directional output of the lineage, which was an existing asset automatically scanned by Purview. We just created the lineage between the two assets.

Note

If the assets don't exist already, you need to run Bulk Entity create API before this step to create those entities before creating the lineage relationship. The bulk entity creation process using the POST /entity/bulk API and Python code snippet is described in step A.

## Scenario Outcomes

API Response "201 Created" indicates successful lineage graph linkage creation and the created GUIDs are contained in the output JSON. Lineage appears in the Microsoft Purview portal:

- Scenario A: Custom built lineage from assets created via API:

    [![Screenshot showing Scenario A: Custom Built Lineage from assets created via API.](../media/how-to-custom-lineage-api/lineage-smaller.png)](../media/how-to-custom-lineage-api/lineage-smaller.png#lightbox)
- Scenario B: Custom built lineage from pre-existing assets linked via API.

    Note

    If the lineage is created from pre-existing entities, observe that the pre-existing lineage graph remains intact and the new linkage is created and displayed additionally.

    [![Screenshot showing Scenario B: Custom Built Lineage from pre-existing assets linked via API.](../media/how-to-custom-lineage-api/lineage-larger.png)](../media/how-to-custom-lineage-api/lineage-larger.png#lightbox)