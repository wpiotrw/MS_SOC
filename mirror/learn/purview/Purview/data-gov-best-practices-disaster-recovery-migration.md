---
layout: Conceptual
title: Disaster recovery and migration for Microsoft Purview data governance (classic) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-best-practices-disaster-recovery-migration
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2025-02-05T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to configure a disaster recovery environment for Microsoft Purview data governance (classic).
locale: en-us
document_id: 34e94633-9e3d-6ed4-4456-d1a76be8fb62
document_version_independent_id: 34e94633-9e3d-6ed4-4456-d1a76be8fb62
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-best-practices-disaster-recovery-migration.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-best-practices-disaster-recovery-migration
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-best-practices-disaster-recovery-migration.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 92fa3d26-59ef-12aa-33c5-a8639ff297a1
---

# Disaster recovery and migration for Microsoft Purview data governance (classic) | Microsoft Learn

This article provides guidance on backup and recovery strategy when your organization has classic Microsoft Purview governance solutions in production deployment. You can also use this general guideline to implement account migration. The scope of this article is to cover manual business continuity and disaster recovery (BCDR) methods, where you could automate using APIs.

Azure data center outages are rare, but can last anywhere from a few minutes to hours. Data Center outages can cause disruption to environments that are being relied on for data governance. By following the steps detailed in this article, you can continue to govern your data in the event of a data center outage for the primary region of your Microsoft Purview account.

Tip

Find more information about [reliability for Microsoft Purview](/en-us/azure/reliability/reliability-microsoft-purview).

## Achieve business continuity for Microsoft Purview

BCDR in a Microsoft Purview instance refers to the mechanisms, policies, and procedures that enable your business to protect data loss and continue operating in the face of disruption, particularly to its scanning, classic catalog, and classic insights tiers. This page explains how to configure a disaster recovery environment for Microsoft Purview.

Today, Microsoft Purview doesn't support automated BCDR. Until that support is added, you're responsible to take care of backup and restore activities. You can manually create a secondary Microsoft Purview account as a warm standby instance in another region.

The following steps summarize how you can achieve disaster recovery manually:

1. Once the primary Microsoft Purview account is created, create one or more secondary Microsoft Purview accounts in a separate region.

    Important

    Microsoft Purview currently supports a single Microsoft Purview instance per tenant. To create a second account for backup and disaster recovery, [contact support](https://azure.microsoft.com/support/create-ticket/)
2. All activities performed on the primary Microsoft Purview account must be carried out on the secondary Microsoft Purview accounts as well. This includes:

    - Maintain Account information
    - Create and maintain custom scan rule sets, classifications, and classification rules
    - Register and scan sources
    - Create and maintain collections along with the association of sources with the collections
    - Create and maintain credentials used while scanning
    - Curate data assets
    - Create and maintain glossary terms

Specific steps to create and maintain a disaster recovery account are provided later in the article. Before you follow them, read through the limitations and considerations.

## Limitations and considerations

As you create your manual BCDR plan, keep the following points in mind:

- You'll be charged for primary and secondary Microsoft Purview instances.
- The primary and secondary Microsoft Purview accounts can't be configured to the same Azure Data Factory, Azure Data Share and Synapse Analytics accounts, if applicable. As a result, the lineage from Azure Data Factory and Azure Data Share can't be seen in the secondary Microsoft Purview accounts. This limitation will be addressed when automated BCDR is supported.
- The integration runtimes are specific to a Microsoft Purview account. So, scans need to run in primary and secondary Microsoft Purview accounts in-parallel, multiple self-hosted integration runtimes must be maintained. This limitation will also be addressed when automated BCDR is supported.
- Parallel execution of scans from both primary and secondary Microsoft Purview accounts on the same source can affect the performance of the source. This can result in scan durations to vary across the Microsoft Purview accounts.
- It isn't advisable to back up "scanned" assets' details. You should only back up the curated data such as mapping of classifications and glossaries on assets. The only case when you need to back up assets' details is when you have [custom assets via custom `typeDef`](data-gov-api-custom-types).
- The backed-up asset count should be fewer than 100,000 assets. The main driver is that you have to use the search query API to get the assets, which have limitation of 100,000 assets returned. However, if you're able to segment the search query to get smaller number of assets per API call, it's possible to back up more than 100,000 assets.
- If you want to continuously "sync" assets between two accounts, there are other steps that won't be covered in detail in this article. You have to use [Microsoft Purview's Event Hubs to subscribe and create entities to another account](data-map-kafta-send-receive-events). However, Event Hubs only has Atlas information. Microsoft Purview has added other capabilities such as **glossaries** and **contacts** that won't be available via Event Hubs.

## Steps to achieve business continuity

### Create the new account

- **If your organization already has multiple Microsoft Purview accounts**, you can create a new Microsoft Purview account by following this guide instruction: [Quickstart: Create a Microsoft Purview account in the Azure portal](create-microsoft-purview-portal)
- **If your organization only has one tenant/organizational Microsoft Purview account**, to create an account for backup and recovery [contact support](https://azure.microsoft.com/support/create-ticket/).

Plan these configuration items that you can't change later:

- Account name
- Region
- Subscription
- Manage resource group name

### Migrate configuration items

Below steps are referring to [Microsoft Purview API documentation](/en-us/rest/api/purview/) so that you can programmatically stand up the backup account quickly:

| Task | Description |
| --- | --- |
| **Account information** | Maintain Account information by granting access for the admin and/or service principal to the account at root level |
| **Collections** | Create and maintain Collections along with the association of sources with the Collections. You can call [List Collections API](/en-us/rest/api/purview/accountdataplane/collections/list-collections) and then get specific details of each collection via [Get Collection API](/en-us/rest/api/purview/accountdataplane/collections/get-collection) |
| **Scan rule set** | Create and maintain custom scan rule sets. You need to call [List custom scan rule sets API](/en-us/rest/api/purview/scanningdataplane/scan-rulesets/list) and get details by calling [Get scan rule set API](/en-us/rest/api/purview/scanningdataplane/scan-rulesets/get) |
| **Manual classifications** | Get a list of all manual classifications by calling get classifications APIs and get details of each classification |
| **Resource set rule** | Create and maintain resource set rule. You can call the [Get resource set rule API](/en-us/rest/api/purview/accountdataplane/resource-set-rules/get-resource-set-rule) to get the rule details |
| **Data sources** | Call the [Get all data sources API](/en-us/rest/api/purview/scanningdataplane/scans/list-by-data-source) to list data sources with details. You also have to get the triggers by calling [Get trigger API](/en-us/rest/api/purview/scanningdataplane/triggers/get). There's also [Create data sources API](/en-us/rest/api/purview/scanningdataplane/data-sources/create-or-replace) if you need to re-create the sources in bulk in the new account. |
| **Credentials** | Create and maintain credentials used while scanning. There's no API to extract credentials, so this must be redone in the new account. |
| **Self-hosted integration runtime (SHIR)** | Get a list of SHIR and get updated keys from the new account then update the SHIRs. This must be done [manually inside the SHIRs' hosts](data-map-integration-runtime-self-hosted#create-a-self-hosted-integration-runtime). These need to be running before you create scans. |
| **ADF connections** | Currently an ADF can be connected to one Microsoft Purview at a time. You must disconnect ADF from failed Microsoft Purview account and reconnect it to the new account later. |

### Run scans

Important

Make sure your [self-hosted integration runtimes](data-map-integration-runtime-self-hosted) have been configured and are running and available before creating scans.

This will populate all assets with default `typedef`. There are several reasons to run the scans again vs. exporting the existing assets and importing to the new account:

- There's a limit of 100,000 assets returned from the search query to export assets.
- It's cumbersome to export assets with relationships.
- When you rerun the scans, you'll get all relationships and assets details up to date.
- Microsoft Purview comes out with new features regularly so you can benefit from other features when running new scans.

Running the scans is the most effective way to get all assets of data sources that Microsoft Purview is already supporting.

### Migrate custom typedefs and custom assets

If your organization [has created custom types in Microsoft Purview](data-gov-api-custom-types), you need to migrate those manually.

#### Custom typedefs

To identify all custom `typedef`, you can use the [get all type definitions API](/en-us/rest/api/purview/catalogdataplane/types/get-all-type-definitions). This will return each type. You need to identify the custom types in such format as `"serviceType": "<custom_typedef>"`

#### Custom assets

To export custom assets, you can search those custom assets and pass the proper custom `typedef` via the [discovery API](/en-us/rest/api/purview/catalogdataplane/discovery/query)

Note

There is a 100,000 return limit per search result. You might have to break the search query so that it won’t return more than 100,000 records.

There are several ways to scope down the search query to get a subset of assets:

- **Using `Keyword`**: Pass the parent FQN such as `Keyword: "<Parent String>/*"`
- **Using `Filter`**: Include `assetType` with the specific custom `typedef` in your search such as `"assetType": "<custom_typedef>"`

Here's an example of a search payload by customizing the `keywords` so that only assets in specific storage account (`exampleaccount`) are returned:

```json
{
  "keywords": "adl://exampleaccount.azuredatalakestore.net/*",
  "filter": {
    "and": [
      {
        "not": {
          "or": [
            {
              "attributeName": "size",
              "operator": "eq",
              "attributeValue": 0
            },
            {
              "attributeName": "fileSize",
              "operator": "eq",
              "attributeValue": 0
            }
          ]
        }
      },
      {
        "not": {
          "classification": "MICROSOFT.SYSTEM.TEMP_FILE"
        }
      },
      {
        "not": {
          "or": [
            {
              "entityType": "AtlasGlossaryTerm"
            },
            {
              "entityType": "AtlasGlossary"
            }
          ]
        }
      }
    ]
  },
  "limit": 10,
  "offset": 0,
  "facets": [
    {
      "facet": "assetType",
      "count": 0,
      "sort": {
        "count": "desc"
      }
    },
    {
      "facet": "classification",
      "count": 10,
      "sort": {
        "count": "desc"
      }
    },
    {
      "facet": "contactId",
      "count": 10,
      "sort": {
        "count": "desc"
      }
    },
    {
      "facet": "label",
      "count": 10,
      "sort": {
        "count": "desc"
      }
    },
    {
      "facet": "term",
      "count": 10,
      "sort": {
        "count": "desc"
      }
    }
  ]
}
```

The returned assets will have some key/pair value that you can extract details:

```json
{
    "referredEntities": {},
    "entity": {
    "typeName": "column",
    "attributes": {
        "owner": null,
        "qualifiedName": "adl://exampleaccount.azuredatalakestore.net/123/1/DP_TFS/CBT/Extensions/DTTP.targets#:xml/Project/Target/XmlPeek/@XmlInputPath",
        "name": "~XmlInputPath",
        "description": null,
        "type": "string"
    },
    "guid": "5cf8a9e5-c9fd-abe0-2e8c-d40024263dcb",
    "status": "ACTIVE",
    "createdBy": "ExampleCreator",
    "updatedBy": "ExampleUpdator",
    "createTime": 1553072455110,
    "updateTime": 1553072455110,
    "version": 0,
    "relationshipAttributes": {
        "schema": [],
        "inputToProcesses": [],
        "composeSchema": {
        "guid": "cc6652ae-dc6d-90c9-1899-252eabc0e929",
        "typeName": "tabular_schema",
        "displayText": "tabular_schema",
        "relationshipGuid": "5a4510d4-57d0-467c-888f-4b61df42702b",
        "relationshipStatus": "ACTIVE",
        "relationshipAttributes": {
            "typeName": "tabular_schema_columns"
        }
        },
        "meanings": [],
        "outputFromProcesses": [],
        "tabular_schema": null
    },
    "classifications": [
        {
        "typeName": "MICROSOFT.PERSONAL.EMAIL",
        "lastModifiedTS": "1",
        "entityGuid": "f6095442-f289-44cf-ae56-47f6f6f6000c",
        "entityStatus": "ACTIVE"
        }
    ],
    "contacts": {
        "Expert": [
        {
            "id": "30435ff9-9b96-44af-a5a9-e05c8b1ae2df",
            "info": "Example Expert Info"
        }
        ],
        "Owner": [
        {
            "id": "30435ff9-9b96-44af-a5a9-e05c8b1ae2df",
            "info": "Example Owner Info"
        }
        ]
    }
    }
}
```

Note

You need to migrate the term templates from `typedef` output as well.

When you re-create the custom entities, you might need to prepare the payload prior to sending to the API:

Note

The initial goal is to migrate all entities without any relationships or mappings. This will avoid potential errors.

- All `timestamp` value must be null such as `updateTime`, `updateTime`, and `lastModifiedTS`.
- The `guid` can't be regenerated exactly as before so you have to pass in a negative integer such as "-5000" to avoid error.
- The content of `relationshipAttributes` shouldn't be a part of the payload to avoid errors since it's possible that the `guids` aren't the same or haven't been created yet. You have to turn `relationshipAttributes` into an empty array prior to submitting the payload.

    - `meanings` contains all glossary mappings, which will be updated in bulk after the entities are created.
- Similarly, `classifications` needs to be an empty array as well when you submit the payload to create entities since you have to create classification mapping to bulk entities later using a different API.

### Migrate relationships

To complete the asset migration, you must remap the relationships. There are three tasks:

1. Call the [relationship API](/en-us/rest/api/purview/catalogdataplane/relationship/get) to get relationship information between entities by its `guid`
2. Prepare the relationship payload so that there's no hard reference to old `guids` in the old Microsoft Purview accounts. You need to update those `guids` to the new account's `guids`.
3. Finally, [create a new relationship between entities](data-gov-api-create-lineage-relationships)

### Migrate glossary terms

Note

Before migrating terms, you need to migrate the term templates. This step should be already covered in the custom `typedef` migration.

#### Using the Microsoft Purview governance portal

The quickest way to migrate glossary terms is to [export terms to a .csv file](how-to-import-export-glossary). You can do this using the Microsoft Purview governance portal.

#### Using Microsoft Purview API

To automate glossary migration, you first need to get the glossary `guid` (`glossaryGuid`) via [List Glossaries API](/en-us/rest/api/purview/catalogdataplane/glossary/list-glossaries). The `glossaryGuid` is the top/root level glossary `guid`.

The below sample response will provide the `guid` to use for subsequent API calls:

```json
"guid": "c018ddaf-7c21-4b37-a838-dae5f110c3d8"
```

Once you have the `glossaryGuid`, you can start to migrate the terms via two steps:

1. [Export Glossary Terms As .csv](/en-us/rest/api/purview/catalogdataplane/glossary/export-glossary-terms-as-csv)
2. [Import Glossary Terms Via .csv](/en-us/rest/api/purview/catalogdataplane/glossary/import-glossary-terms-via-csv)

### Assign classifications to assets

Note

The prerequisite for this step is to have all classifications available in the new account from Migrate configuration items step.

You must call the [discovery API](/en-us/rest/api/purview/catalogdataplane/discovery/query) to get the classification assignments to assets. This is applicable to all assets. If you've migrated the custom assets, the information about classification assignments is already available in `classifications` property. Another way to get classifications is to [list classification per `guid`](/en-us/rest/api/purview/catalogdataplane/entity/get-classifications) in the old account.

To assign classifications to assets, you need to [associate a classification to multiple entities in bulk](/en-us/rest/api/purview/catalogdataplane/entity/add-classification) via the API.

### Assign contacts to assets

If you have extracted asset information from previous steps, the contact details are available from the [discovery API](/en-us/rest/api/purview/catalogdataplane/discovery/query).

To assign contacts to assets, you need a list of `guids` and identify all `objectid` of the contacts. You can automate this process by iterating through all assets and reassign contacts to all assets using the [Create Or Update Entities API](/en-us/rest/api/purview/catalogdataplane/entity/create-or-update-entities).

## Related information

- [Microsoft Purview reliability documentation](/en-us/azure/reliability/reliability-microsoft-purview)
- [Business Continuity and Disaster Recovery](/en-us/azure/availability-zones/cross-region-replication-azure)
- [Build high availability into your BCDR strategy](/en-us/azure/architecture/solution-ideas/articles/build-high-availability-into-your-bcdr-strategy)
- [Azure status](https://azure.status.microsoft/status)