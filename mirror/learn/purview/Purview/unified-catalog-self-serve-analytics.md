---
layout: Conceptual
title: Self-Serve Analytics in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-self-serve-analytics
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-06-23T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
ai-usage: ai-assisted
description: Get step-by-step instructions for using metadata in Microsoft Purview Unified Catalog for analytics and insights.
ms.custom: sfi-image-nochange, msecd-doc-authoring-1015
locale: en-us
document_id: 1509f59c-d8b2-e9e9-4145-c8428ce2d892
document_version_independent_id: 1509f59c-d8b2-e9e9-4145-c8428ce2d892
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-self-serve-analytics.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-self-serve-analytics
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-self-serve-analytics.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5c1f3bfc-fced-4ad1-b4e6-b7200832734d
- https://authoring-docs-microsoft.poolparty.biz/devrel/20ed8455-bc18-4537-87a4-83784e7b2a39
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5017978e-5a12-4c31-bdfd-1880eb1a780b
- https://authoring-docs-microsoft.poolparty.biz/devrel/9a7f703b-30bb-4d62-9eb4-97213f571849
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
platformId: 638ee4aa-7fd8-472e-7ec3-8983c86f5804
---

# Self-Serve Analytics in Unified Catalog | Microsoft Learn

Self-serve analytics and insights refer to data, tools, and platforms that enable business users to access, analyze, and generate insights from data independently. Microsoft Purview data governance publishes a domain model of metadata into Microsoft Fabric OneLake and Microsoft Azure Data Lake Storage Gen2, so you can analyze and generate insights by bringing your own tools and compute. Self-serve analytics of data governance metadata is valuable in driving continuous improvement of your data estate health management and fostering a data-driven culture across your organization by democratizing access to data estate insights and health management.

## Key components

- **Data Model:** 3NF Model with domains and dimensions details.
- **Metadata:**Data governance metadata that includes:
    - Governance domains
    - Data products
    - Data assets
    - Glossary terms
    - Subscription request
    - Data quality rules
    - Dimensions
    - Data quality facts (pass and fail counts)
    - Data health actions (including data quality actions)
    - And many more

## Benefits

- **Empowerment:** Empowers data practitioners, data product owners, data stewards, and analysts to explore data governance metadata and link metadata from various sources to derive insights.
- **Flexibility and efficiency:** You can create custom reports in addition to out-of-the-box reports in health management.
- **Agility:** Allows your organization to respond more swiftly to health management issues and remediation.
- **Cost-effective:** Reduces the need for setting up platforms and build tools. All data is available in OneLake and you can use available tools (Fabric semantic model, Power BI reporting, data flow, and notebook) in OneLake.

## Available reports (out-of-the-box)

Here are the available out-of-the-box reports. You can't customize these reports.

- [Classic assets](unified-catalog-reports-classic-assets) - an overview of assets by type and collection, and their curation status.
- [Classic catalog adoption](unified-catalog-reports-classic-catalog-adoption) - to understand at a glance how Unified Catalog is being used.
- [Classic classifications](unified-catalog-reports-classic-classifications) - an overview of assets classified and the types of classifications.
- [Classic data stewardship](unified-catalog-reports-classic-data-stewardship) - an overview of assets classified and the types of classifications.
- [Classic glossary](unified-catalog-reports-classic-glossary) - health and use of glossary terms.
- [Classic sensitivity labels](unified-catalog-reports-classic-sensitivity-labels) - an overview of assets that have sensitivity labels applied and the types of labels applied.
- [Data governance](unified-catalog-reports-data-governance) - The data governance health report allows your team to track your health progress at a glance, and identify areas that need more work.
- [Data quality health](unified-catalog-reports-data-quality-health) - Data quality dimensions and data quality rules performance reporting.

## Data model for self-serve analytics metadata

The 3NF domain model is part of the normalization process in relational database design. It ensures that the database is free of redundancy and update anomalies. A database schema is in the Third Normal Form if it meets the requirements of the First and Second Normal Forms and all its attributes are functionally dependent only on the primary key.

Use the 3NF domain model to structure data in a way that minimizes duplication and ensures data integrity. It focuses on breaking down data into smaller, related tables where each piece of information is stored only once.

**Characteristics:**

- Elimination of transitive dependencies: Nonkey attributes shouldn't depend on other nonkey attributes.
- Logical grouping: Data is logically grouped into domains based on its function or meaning.
- Entity-relationship diagrams (ERDs): Commonly used to represent 3NF domain models, showing how entities relate to each other.

| **Table name** | **What's stored in the table** | **Relationship keys** |
| --- | --- | --- |
| Access Policy Provisioning State | Information about provisioning state | ProvisioningStateId |
| Access Policy Resource Type | Access policy resource information | ResourceTypeId |
| Access Policy Set | Overall information about access policy, policy use case details, and where the policy is applied | AccessPolicySetId (UniqueId), ResourceTypeId (FK), ProvisioningStateId (FK) |
| Business Domain | Business domain (called **governance domain** in Unified Catalog) name, description, status, and ownership details | Parent Business Domain ID (FK), Created By User ID (FK), Last Modified By User ID (FK) |
| Classification | Data asset classification information | ClassificationId |
| Critical Data Column | Store glossary terms associated to data asset column in this field | Critical Data Column Id, Business Domain Id, Asset Id |
| Critical Data Element | Critical data elements of the data assets | Critical Data Element Id |
| Custom Access Use Case | Access use case information | AccessPolicySetId |
| Data Asset | Data asset name, description, and source information | DataAssetId (UniqueId), DataAssetTypeId (FK), CreatedByUserId (FK), LastModifiedByUserId (FK) |
| Data Asset Column | Data asset column name, column description, and references | DataAssetId (FK), ColumnId (Unique), DataAssetTypeId (FK), DataTypeId (FK), Created By User Id (FK), Last Modified By User Id (FK) |
| Data Asset Column Classification Assignment | Data classification assignment related reference keys | DataAssetId (FK), ColumnId (FK), ClassificationId (FK) |
| Data Asset Column Critical Data Element Assignment | Data asset column associating with critical data element | ColumnId |
| Data Asset Domain Assignment | Data asset governance domain assignment related information | DataAssetId (FK), BusinessDomainId (FK), AssignedByUserId (FK) |
| Data Asset Owner | Data asset owner information | DataAssetOwnerId |
| Data Asset Owner Assignment | Data asset owner assignment information | DataAssetId, DataAssetOwnerId |
| Data Asset Type Data Type | Data asset type information | DataTypeId (UniqueId), DataAssetTypeId (FK) |
| Data Product | Data product name, description, use cases, status, and other relevant information | DataProductId (UniqueId), DataProductTypeId (FK), DataProductStatusId (FK), UpdateFrequencyId (FK), CreatedByUserId (FK), LastUpdatedByUserId (FK) |
| Data Product Asset Assignment | Data product and data asset assignment information | DataProductId, DataAssetId |
| Data Product Business Domain Assignment | Data product and governance domain assignment information | DataProductId (FK), BusinessDomainId (FK), AssignedByUserId (FK) |
| Data Product Critical Data Element Assignment | Critical data element assignment to data product | DataProductId |
| Data Product Documentation | Data product documentation reference information is stored in this table. | DataProductId, DocumentationId |
| Data Product OKR Assignment | Assigned objectives and key results to data product | Data Product Id, Objective Id, Key Result Id |
| Data Product Owner | Data product owner information | DataProductId, DataProductOwnerId |
| Data Product Status | Data product status (like published or draft) related information | DataProductStatusId |
| Data Product Terms Of Use | Data product usage terms information | DataProductId, TermOfUsedId, DataAssetId |
| Data Product Type | The information about data product types, such as master, reference, or operational | DataProductTypeId |
| Data Product Update Frequency | The information about how often this data product's data are updated | UpdateFrequencyId |
| Data Quality Asset Rule Execution | Data quality scanning results, including custom rule column list and rule column IDs. | RuleId (FK), DataAssetId (FK), JobExecutionId (FK), RuleColumnList, RuleColumnIdList |
| Data Quality Job Execution | Data quality job execution status | JobExecutionId (UniqueId) |
| Data Quality Rule | Information about data quality rules | RuleId (UniqueId), RuleTypeId (FK), BusinessDomainId (FK), DataProductId (FK), DataAssetId (FK), JobTypeDisplayName (FK), RuleOriginDisplayName (FK), RuleTargetObjectType (FK), CreatedByUserId (FK), LastUpdatedByUserId (FK) |
| Data Quality Rule Column Execution | Information about data quality rules pass and fail count, data quality score at the column level, and data quality job execution details. Only out-of-the-box rule data are available. For custom rule column list and column ID list, see the Data Quality Asset Rule Execution table. | RuleId (FK), DataAssetId (FK), ColumnId (FK), JobExecutionId (FK) |
| Data Quality Rule Type | Data quality rule type and associated dimensions | RuleTypeId (UniqueId), DimensionDisplayName (FK) |
| Data Subscription Request | Information about data subscribers, policies applied, subscription request status, and other relevant information | SubscriberRequestId (UniqueId), SubscriberIdentityTypeDisplayName (FK), RequestorIdentityTypeDisplayName (FK), RequestorStatusDisplayName (FK) |
| Glossary Term | Information about glossary term, description, and overall status of the glossary term | GlossaryTermId (UniqueId), ParentGlossaryTermId (FK), CreatedByUserId (FK), LastModifiedByUserId (FK) |
| Glossary Term Business Domain Assignment | Information about glossary term governance domain assignment and statuses | GlossaryTermId (FK), BusinessDomainId (FK), AssignedByUserId (FK), GlossaryTermStatusId (FK), CreatedByUserId (FK), LastUpdatedByUserId (FK) |
| Glossary Term Critical Data Element Assignment | Associating glossary term with critical data element | GlossaryTermId |
| Glossary Term Data Product Assignment | Information about glossary term data product assignment | GlossaryTermId (FK), DataProductId (FK), AssignedByUserId (FK), GlossaryTermStatusId (FK), CreatedByUserId (FK), LastUpdatedByUserId (FK) |
| Health Action | Information about data governance and data quality actions | ActionId, TargetEntityId, CreatedByUserId |
| Health Action Finding Type | Data health actions **Finding Types** | FindingTypeId |
| Health Action Finding Sub Type | Data health actions **Finding Sub Types** | FindingSubTypeId, FindingTypeId |
| Health Action User Assignment | Data health actions **User Assignment** information | ActionId, AssignedToUserId |
| Key Result | Key result of data product objective, including details description | Key Result Id, Objective Id |
| Objective | Objective of the data product contains objective Id, objective description, and objective status | Objective Id |
| Policy Set Approver | Policy set and the approver information | SubscriberRequestId (FK), AccessPolicySetId (FK), ApproverUserId (FK) |
| Relationship | Information about source type and target information. The relationship of glossary terms association with assets and columns is available in this relationship table. | AccountId, SourceId, TargetId |

Note

- Business Domain is called **governance domain** in Unified Catalog, but it's still called **Business Domain** in the physical model in the database. The name difference doesn't affect the usage scenario described here for Business Domain.
- When you delete an asset from Data Map and later recreate it with the same name, the asset is treated as new and gets a new ID. As a result, the deleted asset is no longer valid for Data Quality rules column and column ID association. This scenario isn't currently supported. So, the `RuleColumnIdList` in the Data Quality Asset Rule Execution table stays blank for the deleted data asset in Data Map. You must run Data Quality scans again on the newly created data asset, even if the asset name and schema are identical to the deleted one.

This diagram shows the entity relationship for the domain model described in the data model table: [![Diagram that shows the entity relationship for the self-serve analytics domain model.](media/dg-self-serve-metadata-analytics/byoc-erd.png)](media/dg-self-serve-metadata-analytics/byoc-erd.png#lightbox)

## Subscribe Unified Catalog metadata to Fabric OneLake

Subscribe to Purview data governance metadata for analytics and get insights by following these steps:

1. In the [Purview portal](https://purview.microsoft.com), select **Settings**, then select **Unified Catalog**, then select **Solution integrations (preview)**.
2. Make sure that you have the Data Governance Administrator role (learn more about [roles and permissions](data-governance-roles-permissions)).
3. Select **Edit**.
4. Add **Storage type** and **Enable** the setup.
5. Add **Location URL** (example: `https://onelake.dfs.fabric.microsoft.com/workspace name/lakehouse name/Files/purviewmetadata`)
6. Select **Properties** to copy the URL.

    [![Screenshot that shows how to configure fabric url 1.](media/dg-self-serve-metadata-analytics/fabric-url-1.png)](media/dg-self-serve-metadata-analytics/fabric-url-1.png#lightbox)
7. Copy the URL from the **Properties** page.

    [![Screenshot that shows how to configure fabric url 2.](media/dg-self-serve-metadata-analytics/fabric-url-2.png)](media/dg-self-serve-metadata-analytics/fabric-url-2.png#lightbox)
8. Add the folder name at the end of the URL. For example, add `/DEH` to the copied URL, as shown in the previous screenshot.
9. Grant contributor access to Purview Managed Service Identity (MSI) for your Fabric workspace.
10. Test the connection.
11. Select **Save** to save the configuration and publish Purview metadata to your OneLake workspace.

## Enable managed V-NET

To enable or disable managed virtual network, follow these steps:

1. In the Purview portal, select **Settings**.
2. Under **Solution settings**, select Unified Catalog, and then select **Solution integrations (preview)**.
3. On **Configure storage**, select the **Enable managed V-NET** toggle to enable managed virtual network for your storage.

[![Screenshot that shows how to configure virtual network.](media/dg-self-serve-metadata-analytics/vnet-provisioning-self-serv.png)](media/dg-self-serve-metadata-analytics/vnet-provisioning-self-serv.png#lightbox)

1. Enter the **Target Resource ID**. For example, the target resource ID is: `/subscriptions/e2223ea4f73-6833-439d-b40e 615c78e2d8af/resourceGroups/vnettesting/providers/`. To copy a resource ID of your storage, select the JSON View of your storage and copy the JSON string.
2. Select **Update/Refresh MPE status** to see the update. The status changes from **Provisioning** to **Pending**.
3. You need to approve the MPE request in the Azure portal to complete the setup. After you approve the request, the MPE status changes from **Pending** to **Approved**.

[![Screenshot that shows how to approve vNet provisioning request.](media/dg-self-serve-metadata-analytics/approve-mpe-status.png)](media/dg-self-serve-metadata-analytics/approve-mpe-status.png#lightbox)

To disable the virtual network setup, select the **Enable managed V-NET** toggle to turn it off. If you disable it, you need to change non-virtual network storage endpoint.

### Remove a configured virtual network

To remove a managed virtual network setup, select **Delete MPE** on **Configure storage**. This action deletes the virtual network configuration and removes it from the **Configure storage** pane. The **Test connection** area reappears, which you can use to test a non-virtual network connection. **Test connection** is only enabled for non-virtual storage setup.

Note

Publishing Unified Catalog metadata to a Fabric workspace isn't supported in Fabric tenants with Managed Private Endpoints enabled. Use a Fabric tenant without Managed Private Endpoints to publish Unified Catalog metadata.

### Helpful information about virtual network setup

- Use the Location URL or Endpoint from virtual network storage when you enable managed virtual network to store Purview metadata.
- Use JSON View to copy **Target Resource ID** from your Azure portal to avoid using an incorrect resource group.
- If you deleted the configured virtual network, then make sure that you change the endpoint or Location URL to use non-virtual-network storage and test the connection for non-virtual-network storage.

Note

To store [data quality error records](unified-catalog-data-quality-error-records), create separate folder locations for each domain. This approach organizes and stores domain-specific data quality error records in dedicated folders. You must configure data quality error records storage separately. To create data quality error record storage, go to **Data Quality** &gt; **Manage** &gt; **Settings**, select an Azure region, and set up the storage connection. You can't use self-serve storage connection setup for data quality error records storage even if you use identical or same storage location.

## Create a semantic model in OneLake

In the context of data and analytics, a semantic model is a structured representation of data that defines the meaning, relationships, and rules within a specific domain. It provides a layer of abstraction that helps users understand and interact with complex data by making it more intuitive and accessible, especially in the context of business intelligence (Power BI) and analytics platforms.

You always need a semantic model before you can build any reports. Within the warehouse, you can add warehouse objects - tables or views - to your default Power BI semantic model. You can also add other semantic modeling properties, such as hierarchies and descriptions. Use these properties to create the Power BI semantic model's tables. You can also remove objects from the default Power BI semantic model.

To create a semantic model from the Data Governance metadata domain model:

1. Open the Lakehouse in your Fabric workspace.
2. Use a **shortcut** to create a shortcut of the domain model from OneLake and within OneLake.

    1. Select the **Tables** ellipsis button (...).
    2. Select **New Shortcut** and select OneLake from New Shortcut sources page.
    3. Select the **DomainModel** table to shortcut.

    [![Screenshot that shows how to publish to delta table via shortcut.](media/dg-self-serve-metadata-analytics/domain-dimension-models-shortcut.png)](media/dg-self-serve-metadata-analytics/domain-dimension-models-shortcut.png#lightbox)
3. Create a shortcut directly at the table level for all files, which eliminates duplicate records.

    [![Screenshot that shows how to create table level shortcut.](media/dg-self-serve-metadata-analytics/table-level-shortcut.png)](media/dg-self-serve-metadata-analytics/table-level-shortcut.png#lightbox)

After you publish all files to delta tables via shortcut, you can add the delta tables to semantic model.

1. Switch to SQL analytics endpoint page from the Lakehouse page.
2. Select **Reporting** from top left corner of the **SQL analytics endpoint** page.
3. Select **Manage default semantic model**.
4. Select the tables from dbo &gt; Tables that you want to add to the semantic model for reporting.

[![Screenshot that shows how to add table to semantic model manually.](media/dg-self-serve-metadata-analytics/add-table-to-semantic-model.png)](media/dg-self-serve-metadata-analytics/add-table-to-semantic-model.png#lightbox)

To add objects such as tables or views to the default Power BI semantic model, select **Automatically update semantic model**.

[![Screenshot that shows the self-serve analytics semantic model.](media/dg-self-serve-metadata-analytics/self-serve-analytics-semantic-model.png)](media/dg-self-serve-metadata-analytics/self-serve-analytics-semantic-model.png#lightbox)

Note

- You can right-click to add related tables to create a relationship.
- If you prefer not to subscribe Purview metadata for self-serve analytics, you can manually disable self-serve analytics (metadata subscription): go to Solution settings &gt; Unified Catalog &gt; Solution Integrations &gt; Self-serve analytics and select the toggle to disable it. You need the Data Governance Administrator role to enable and disable this feature.

## Subscribe to Purview catalog metadata to Data Lake Storage Gen2 storage

To subscribe to Purview's data governance metadata and publish it to your Data Lake Storage Gen2 storage for analytics and insights, follow these steps:

1. In the Purview portal, open **Unified Catalog**.
2. Select **Settings** in the left navigation. Under **Solution settings**, select **Unified Catalog**.
3. Select **Solution integration**, and then select **Edit**.
4. Select **Storage type** and **Enable** the setup.
5. Add **Location URL**. This URL needs to be the Data Lake Storage Gen2 path plus the container name, formatted as Data Lake Storage Gen2 endpoint + "/(container name)".

    1. Go to portal.azure.com.
        1. Select your Data Lake Storage Gen2 storage.
    2. Go to **Settings** &gt; **Endpoints** and select the primary endpoint of your Data Lake Storage Gen2 storage.
6. Grant **Storage Blob Data Contributor** access to Purview Managed Service Identity (MSI) for your Data Lake Storage Gen2 container.
7. Test the connection.

    [![Screenshot of the Data Lake Storage Gen2 subscription connection configuration.](media/dg-self-serve-metadata-analytics/dg-meta-subscription-adlsg2.png)](media/dg-self-serve-metadata-analytics/dg-meta-subscription-adlsg2.png#lightbox)
8. Select **Save** to save the configuration and publish the domain model to your Data Lake Storage Gen2 storage.

Note

To store [data quality error records](unified-catalog-data-quality-error-records), create separate folder locations for each domain. This approach organizes and stores domain-specific data quality error records in dedicated folders.

### Review published model and data

1. Open portal.azure.com.
2. Select your Data Lake Storage Gen2 storage.
3. Select the container that you added with the Data Lake Storage Gen2 endpoint in Purview.
4. Browse the list of Delta Parquet files published in the container.
5. Browse published model and metadata (see the following images).

    [![Screenshot that shows how to configure subscription connection in adlsg2 container.](media/dg-self-serve-metadata-analytics/adlsg2-storage-byoc-model.png)](media/dg-self-serve-metadata-analytics/adlsg2-storage-byoc-model.png#lightbox)

    [![Screenshot of the published domain model files in the Data Lake Storage Gen2 container.](media/dg-self-serve-metadata-analytics/adlsg2-storge-domain-files.png)](media/dg-self-serve-metadata-analytics/adlsg2-storge-domain-files.png#lightbox)

### Create a Power BI report

Power BI is natively integrated in the whole Fabric experience. This native integration includes a unique mode, called DirectLake, for accessing the data from the lakehouse to provide the most performant query and reporting experience. DirectLake is a groundbreaking new capability that allows you to analyze large semantic models in Power BI.

With DirectLake, you load parquet-formatted files directly from a data lake without needing to query a data warehouse or lakehouse endpoint, and without needing to import or duplicate data into a Power BI semantic model. DirectLake is a fast path to load the data from the data lake straight into the Power BI engine, ready for analysis.

In traditional DirectQuery mode, the Power BI engine directly queries the data from the source for each query execution, and the query performance depends on the data retrieval speed. DirectQuery eliminates the need to copy data, ensuring that any changes in the source are immediately reflected in query results.

For more information, see [how to create a Power BI report in Microsoft Fabric](/en-us/fabric/data-engineering/tutorial-lakehouse-build-report).

### Set up the schedule

Data Governance Administrators can set up the self-serve analytics metadata refreshing schedule by following these steps:

1. In the Purview portal, open **Unified Catalog**.
2. Select **Settings** in the left navigation. Under **Solution settings**, select **Unified Catalog**.
3. Select **Solution integration**, then select the scheduler icon.
4. On **Schedule self-serve analytics**, turn on the **Enabled** toggle, and set the start date, frequency, and end date.
5. Select **Save**.

### Job history

You can browse **Job history** by selecting the **Job history** icon on the self-serve analytics page. You can filter job status by Complete or Failed for a date range.

[![Screenshot that shows the list of job status.](media/dg-self-serve-metadata-analytics/self-serve-storage-job-history.png)](media/dg-self-serve-metadata-analytics/self-serve-storage-job-history.png#lightbox)

Important

- Purview MSI needs contributor access to your Fabric workspace if you're subscribing Purview metadata to publish into your Fabric workspace.
- Purview MSI needs **Storage Blob Data Contributor** access to your Data Lake Storage Gen2 if you're subscribing Purview metadata to publish into your Data Lake Storage Gen2 container.
- Standalone data assets with a Data Quality score aren't published for self-serve analytics. If you associate a standalone data asset with a data product and run Data Quality for it, Purview publishes the associated data asset's metadata for self-serve analytics.
- If a user deletes the Data Quality history for a data asset, the deleted history continues to exist in the self-serve analytics storage (Fabric and Data Lake Storage Gen2). Purview doesn't publish a delete indicator or deletion flag to self-serve analytics storage, making it impossible to distinguish deleted Data Quality scan history from active history records. As a result, consumers of the self-serve analytics data might continue to see historical Data Quality records even after they're deleted from the product experience.
- Purview only publishes governed assets data. Data assets associated with a data product are categorized as governed assets. Data Map assets that aren't governed won't appear in the self-serve analytics data asset table.
- The Catalog implements role-based access control (RBAC), ensuring that not all users can view all domains or data products. However, for self-serve analytics, Purview publishes all data, allowing anyone with access to this data to view the entire catalog. Access control for self-serve metadata depends on where the data is stored - either the Fabric workspace owner or the Data Lake Storage Gen2 storage owner can manage access.
- If you prefer not to subscribe Purview metadata for self-serve analytics, you can manually disable self-serve analytics (metadata subscription): go to Solution settings &gt; Unified Catalog &gt; Solution Integrations &gt; Self-serve analytics and select the toggle to disable it. You need the Data Governance Administrator role to enable and disable this feature.