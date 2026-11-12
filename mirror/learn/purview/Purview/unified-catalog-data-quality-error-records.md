---
layout: Conceptual
title: Data quality error records of rule exception in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-error-records
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Browse and remediate data quality issues in Microsoft Purview Unified Catalog by correcting the error records.
locale: en-us
document_id: 2bf99a2f-82ca-e6e7-e856-3f7f1aabb99a
document_version_independent_id: 2bf99a2f-82ca-e6e7-e856-3f7f1aabb99a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-error-records.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-error-records
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-error-records.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e7cd09c2-9e9a-4f0d-b160-c15783f45b1f
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1d337399-0ca4-4b4c-acef-8df37820e018
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 0daea221-6e3d-6a93-8011-1b39f56d6d0f
---

# Data quality error records of rule exception in Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

When you perform data quality checks in Microsoft Purview Unified Catalog, you can configure and publish data quality error records for rule exceptions. By using this setup, you can review and remediate these records directly in your managed storage.

For cloud data sources, you can store and manage data quality error records in Microsoft Fabric Lakehouse or Azure Data Lake Storage Gen2. For on-premises data sources, you can create an error records database in Oracle or SQL Server to store and manage data quality error records.

By using this feature, Microsoft Purview Data Quality users can identify, analyze, and address data quality problems. It helps ensure data accuracy, completeness, consistency, timeliness, and validity across systems and use cases.

## Architecture

To publish data quality error records for rule exceptions, you need to set up your managed storage in Microsoft Purview. The Data Governance Administrator for your organization is responsible for configuring the storage details on the Microsoft Purview administration page. The Data Quality Steward can enable the toggle either from the Data Quality Manage console or the data quality overview page at **Unified Catalog** &gt; **Health management** &gt; **Data quality**.

[![dq error record architecture](media/how-to-configure-and-run-data-quality-scan/dq-error-records-architecture.png)](media/how-to-configure-and-run-data-quality-scan/dq-error-records-architecture.png#lightbox)

## Configuration storage location

- In Unified Catalog, go to **Health management** &gt; **Data quality**.
- Select a governance domain from the list to open its details page.
- Select **Manage**, then select **Settings**.
- Select **Azure Region** from the dropdown list of all supported Azure regions.
- After selecting the Azure region, select **New** to configure storage details.
- Select **Storage Type**: Fabric or Data Lake Storage Gen2.
- Enter the **Location URL**.
- If you select **Fabric** as the storage type, enter the **Workspace ID** and **Lakehouse ID**. Grant contributor access to Microsoft Purview Manage Service Identity (MSI) to your Fabric workspace.
- If you select **Azure Data Lake Storage Gen2**as the storage type, enter following details:
    - Add **Azure subscription**. To find your Azure subscription name, go to `portal.azure.com`.
    - Add **Resource**. To find the resource name, select **Home** &gt; select **Resource** from the **Resource list**.
    - Add **Container** name. To find the container name, select **Data Lake Storage** from the overview page in `portal.azure.com`
    - Add **Folder Path**. This is optional information.
    - Grant Storage Blob Data Contributor access to Microsoft Purview Manage Service Identity (MSI) to your Data Lake Storage Gen2 container.
- Test the connection.
- Save the configuration.
- You can **Save as draft** if you don't have all the required information so that you won't lose what you've entered.

Compute is a prerequisite for private endpoint or virtual network storage setup. For private endpoint approval request, select **Enable managed V-Net** checkbox. An approval request is sent to your Azure portal, which you must approve to enable virtual network access. This process is similar to setting up a Data Quality connection. You must deploy the compute in the same Azure region as the storage account.

If you configure your Fabric tenant to run on a virtual network or in private link, select the **Enable managed V-NET** checkbox on the **Configure Storage** page. Then add the Private Link Resource ID as listed here:

/subscriptions/07d669d6-83f2-4f15-8b5b 4a4b31a7050e/resourceGroups/pdgbugbashfabricvnet/providers/Microsoft.PowerBI/priva teLinkServicesForPowerBI/fabricvnetpl.

To set up compute for virtual networks, see [Set up data quality for managed virtual networks](unified-catalog-data-quality-managed-virtual-networks). To set up and use private link for your Fabric tenant, follow the instructions to [set up the private link for the Fabric tenant](/en-us/fabric/security/security-private-links-use) before configuring data quality virtual network connection and compute allocation.

Note

- Supported cloud data sources for Data Quality error records are: Azure SQL, Azure SQL MI, Azure Data Lake Storage G2, Azure Databricks, Microsoft Fabric, Azure Synapse, and Google BigQuery.
- Supported on-premises data sources for error records are: Oracle and SQL Server.
- If your data products include assets from multiple Azure regions, you must create a region-specific data quality error records folder for each region to meet data residency requirements. Microsoft Purview Data Quality doesn't copy data between Azure regions.
- If you already created a storage location without specifying an Azure region, you must update it to include the region. Data quality failed/error records won't publish until a region is provided.
- If you configure multiple region-specific folders for storing data quality failed/error records, Microsoft Purview Data Quality automatically routes the error records to the correct regional folder during the scan.
- If you're using virtual networks, you can't test the connection. The **Test Connection** tab is disabled.
- You can use error sink behind virtual networks only if you're also running the job in a virtual network connection. If not, error row publishing is skipped.
- For a non-virtual network source connection to Azure Databricks Unity Catalog, Snowflake, Google BigQuery, Azure Synapse Analytics, on-premises Oracle Database, Fabric, and Azure SQL MI database, you need to set up error sink in the Microsoft Purview account region, not the data asset region.
- For virtual network sources and all other types of non-virtual network sources, the error sink region has to match the asset region.

**Data quality error records storage setting for non-virtual network storage - Fabric**: [![Data quality error record setting](media/how-to-configure-and-run-data-quality-scan/dq-error-records-setting.png)](media/how-to-configure-and-run-data-quality-scan/dq-error-records-setting.png#lightbox)

**Data quality error records storage setting for virtual storage - Fabric**: [![Data quality error record setting for virtual network storage](media/how-to-configure-and-run-data-quality-scan/dq-error-records-setting-vnet.png)](media/how-to-configure-and-run-data-quality-scan/dq-error-records-setting-vnet.png#lightbox)

**Data quality error records storage setting for non-virtual storage - AdlsG2**: [![Data quality error record setting Azure Data Lake Storage Gen2](media/how-to-configure-and-run-data-quality-scan/dq-error-records-setting-adlsg2.png)](media/how-to-configure-and-run-data-quality-scan/dq-error-records-setting-adlsg2.png#lightbox)

**Data quality error records storage setting for virtual network storage - AdlsG2**: [![Data quality error record setting for virtual network storage Azure Data Lake Storage Gen2](media/how-to-configure-and-run-data-quality-scan/dq-error-records-setting-vnet-adlsg2.png)](media/how-to-configure-and-run-data-quality-scan/dq-error-records-setting-vnet-adlsg2.png#lightbox)

Caution

- If you don't have storage and a connection set up to store data quality error records in the asset region (as mentioned in the preceding section), the data quality scan job still succeeds, but error row publishing is skipped.
- After configuring the storage and connection, you can enable the data quality error record feature either by going to **Health management** &gt; **Data quality** &gt; **Manage** &gt; **Settings** for the selected governance domain, or from the Data Quality overview page for a data asset.
- To analyze the published erroneous records, use the latest versions of Spark (&gt;= 3.xx) on Synapse or Databricks.
- Error sink configurations in a **published** state will only be used for error sink output, *not* in a **draft** state. If the configuration is in a draft state, the system skips error row publishing to the configured storage.

## Data quality error detection

To detect data quality errors in your data, configure and set up a data quality scan. Select the data asset and configure rules for the critical columns that need a Data Quality measurement. You can use out-of-the-box rules, create custom rules, or use the rule suggestion feature to recommend rules for a data quality scan. For more information, see [data quality rules](unified-catalog-data-quality-rules).

## Enable error recording

To get error records, enable the capture and storage of error records for every data quality job run by following these steps:

1. Follow the instructions to [start a data quality scan on a data asset](unified-catalog-data-quality-scan#run-a-data-quality-scan).
2. After selecting **Run quality scan** on the data asset's page, turn on the toggle for **Enable publishing of failed rows**.

[![activate error record feature from data asset page](media/how-to-configure-and-run-data-quality-scan/activate-error-record-feature.png)](media/how-to-configure-and-run-data-quality-scan/activate-error-record-feature.png#lightbox)

You can also enable error recording for all data assets with data quality rules associated with data products in a **governance domain** level by following these steps:

- In Unified Catalog, go to **Health management** &gt; **Data quality**.
- Select a governance domain from the list to open its details page.
- Select **Manage**, then select **Settings**.
- Turn on the toggle for **Enable publishing of failed rows**.

## Set up schedule to run

Set up the schedule to run your data quality job and publish the error records into the configured storage. For more information, see [configure and run data quality scans](unified-catalog-data-quality-scan).

Though you can run data quality scans on an ad-hoc basis by selecting **Run quality scan** on a data asset page, in production scenarios it's likely that the source data is constantly updated. Regularly monitor data quality to detect any problems. Automating the scanning process helps you manage regular updates of quality scans.

## Check the error records in the configured storage

1. Find the location of the published error rows from the data quality overview page.
2. Select **View Scan report**, in the top-right corner just below the **Latest quality score**.
3. Go to the path shown in your Data Lake Storage Gen2 or Fabric Lakehouse folder, as seen in the following example:

[![error records in adlsG2](media/how-to-configure-and-run-data-quality-scan/error-records-in-adlsg2.png)](media/how-to-configure-and-run-data-quality-scan/error-records-in-adlsg2.png#lightbox)

#### Data Lake Storage Gen2 folder hierarchy

Data Lake Storage Gen2 container (for example, folder name is DEH):

1. DataQualityAuditExtract
2. Governance domain (BusinessDomain)
3. DataProduct
4. DataAsset
5. RunDate
6. RunId
7. Purview DQRunId
8. Error record file

#### Read data quality error records from Data Lake Storage Gen2

Use a Synapse or Databricks notebook to read data from Data Lake Storage Gen2 container by using this PySpark script:

```Python

#For complete error records of all jobs run on the asset
path = "abfss://TestWSPDGBB@onelake.dfs.fabric.microsoft.com/TestSelfServeLakehouse.Lakehouse/Files/SelfServeFolder/DataQualityAuditExtracts/BusinessDomain_577b8e54-e534-478d-bbc6-19a3221fc71e/DataProduct_a04c82a2-2372-4b9e-9e0a-4dfd8959ee85/DataAsset_4b2b2644-c94a-447f-9b2e-32961ac0170b"
df = spark.read.format("delta").load(path)
display(df)

#For All Runs on a particular Date
path = "abfss://TestWSPDGBB@onelake.dfs.fabric.microsoft.com/TestSelfServeLakehouse.Lakehouse/Files/SelfServeFolder/DataQualityAuditExtracts/BusinessDomain_577b8e54-e534-478d-bbc6-19a3221fc71e/DataProduct_a04c82a2-2372-4b9e-9e0a-4dfd8959ee85/DataAsset_4b2b2644-c94a-447f-9b2e-32961ac0170b"
df = spark.read.format("delta").load(path).where("_purviewDQRunDate = '2025-08-06'")
display(df)

#For a Specific run
path = "abfss://TestWSPDGBB@onelake.dfs.fabric.microsoft.com/TestSelfServeLakehouse.Lakehouse/Files/SelfServeFolder/DataQualityAuditExtracts/BusinessDomain_577b8e54-e534-478d-bbc6-19a3221fc71e/DataProduct_a04c82a2-2372-4b9e-9e0a-4dfd8959ee85/DataAsset_4b2b2644-c94a-447f-9b2e-32961ac0170b"
df = spark.read.format("delta").load(path).where("_purviewDQRunId = '647b8a8f-7140-4158-9914-9c2409a5ec67'")
display(df)

#For a specific rule of the run
path = "abfss://TestWSPDGBB@onelake.dfs.fabric.microsoft.com/TestSelfServeLakehouse.Lakehouse/Files/SelfServeFolder/DataQualityAuditExtracts/BusinessDomain_577b8e54-e534-478d-bbc6-19a3221fc71e/DataProduct_a04c82a2-2372-4b9e-9e0a-4dfd8959ee85/DataAsset_4b2b2644-c94a-447f-9b2e-32961ac0170b"
df = spark.read.format("delta").load(path).where("_purviewDQRunId = '647b8a8f-7140-4158-9914-9c2409a5ec67' AND _purviewDQRuleId = '32d57f8d-87dc-4862-90c9-c3bcad1051ad'")
display(df) 

#For a specific rule across all runs
path = "abfss://TestWSPDGBB@onelake.dfs.fabric.microsoft.com/TestSelfServeLakehouse.Lakehouse/Files/SelfServeFolder/DataQualityAuditExtracts/BusinessDomain_577b8e54-e534-478d-bbc6-19a3221fc71e/DataProduct_a04c82a2-2372-4b9e-9e0a-4dfd8959ee85/DataAsset_4b2b2644-c94a-447f-9b2e-32961ac0170b"
df = spark.read.format("delta").load(path).where(" _purviewDQRuleId = '32d57f8d-87dc-4862-90c9-c3bcad1051ad'")
display(df) 

#For comparing two runs
path = "abfss://TestWSPDGBB@onelake.dfs.fabric.microsoft.com/TestSelfServeLakehouse.Lakehouse/Files/SelfServeFolder/DataQualityAuditExtracts/BusinessDomain_577b8e54-e534-478d-bbc6-19a3221fc71e/DataProduct_a04c82a2-2372-4b9e-9e0a-4dfd8959ee85/DataAsset_4b2b2644-c94a-447f-9b2e-32961ac0170b"
df = spark.read.format("delta").load(path).where("_purviewDQRunId = '647b8a8f-7140-4158-9914-9c2409a5ec67' OR _purviewDQRunId = 'a508f960-254c-4eb1-9097-03307402475b'")
display(df) 

```

**Example dataset:**

[![error records sample](media/how-to-configure-and-run-data-quality-scan/error-records-sample.png)](media/how-to-configure-and-run-data-quality-scan/error-records-sample.png#lightbox)

#### Read error records from Fabric Lakehouse

1. Go to the path shown in your Lakehouse, and browse all fail records published to Fabric Lakehouse.
2. Create a shortcut from Delta Parquet to Delta Table. Or you can use a Delta Parquet file to create a dashboard of your data quality error records, as seen in this example:

[![error records published in Lakehouse](media/how-to-configure-and-run-data-quality-scan/error-records-in-fabric-lakehouse.png)](media/how-to-configure-and-run-data-quality-scan/error-records-in-fabric-lakehouse.png#lightbox)

Use a notebook to create a shortcut table of failed data asset records. See the notebook script.

## Output data model

You can view failed records at the level of a governed data asset. For each new assessment run that succeeds on the data asset, the process adds a new set of failed records for each rule evaluation to the failed records table.

**Format**: Delta

**Output schema**: Each row of output contains all the columns of an input data asset row that failed a rule evaluation, along with a set of metadata columns that you can use to identify and analyze the failed row.

**Primary key**: Composite key of input data asset columns + \_purviewDQRunId + \_purviewDQRuleId

| **Metadata columns** | **Data type** | **Description** |
| --- | --- | --- |
| \_purviewDQRunId | string | A GUID that represents the Run ID of the assessment scan available to the user at the time of run. Also, a Delta partition-column. |
| \_purviewDQRunDate | string | The run date in YYYY-MM-DD format. Also, a Delta partition-column. |
| \_purviewDQRuleId | string | The quality Rule ID that corresponds to the failed rule. Also, a Delta partition-column. |
| \_purviewDQRuleName | string | The Rule Name at the time of job run. |
| \_purviewDQRuleType | string | The Rule type (for example: UniqueCheck, NotNull, Regex). |
| \_purviewDQGovernanceDomainId | string | The governance domain ID of the data asset that you ran. |
| \_purviewDQDataProductId | string | The data product of the data asset that you ran. |
| \_purviewDQDataAssetId | string | The data asset ID. |
| \_purviewDQRunSubmitTimestamp | string | The exact timestamps of the run submit time in the default UTC time-zone per the ISO format. |

## Create a Power BI dashboard for your data quality error records

Use the Business Domain ID to link data products and their associated data assets for reporting data quality error records.

- One business domain can link to multiple data products.
- Each data product can link to multiple data assets.
- Each data asset can have multiple rules.
- Each rule can generate multiple error records.

This image illustrates a data model to create a basic report of your data quality error record:

[![error records reporting datamodel](media/how-to-configure-and-run-data-quality-scan/datamodel.png)](media/how-to-configure-and-run-data-quality-scan/datamodel.png#lightbox)

This image illustrates a sample report created with the data model shown in the preceding image:

[![error records sample report](media/how-to-configure-and-run-data-quality-scan/sample-report.png)](media/how-to-configure-and-run-data-quality-scan/sample-report.png#lightbox)

## Limitations

- 100,000 failed records are published per rule for each run.
- Datasets up to 100 million rows with up to 40 rules have been benchmarked.
- As data is stored in organizations' managed storage, the organization owns role-based access control for the data. Microsoft publishes data quality error rows to an organization's storage based on the organization's consent.

Note

Failed rows can't be accessed by selecting the URL. For security reasons, direct browsing of the error record database through the URL isn't supported.

Example URL: `https://onelake.dfs.fabric.microsoft.com/xxxxxxx-4xxx-88aa-xxxe22db3d5/babea959-fxxxxxxxxx-d2efe0716593/Files/xxxx1/DataQualityAuditExtracts/BusinessDomain_xxxx-xxxx-ccc9-92c2-1554a93dd2af/DataProduct_abc33xxxxyu-28ec-4186-01fg-591c0420e677/DataAsset_xxxxx-583a-49ee-abd6-6543464654e4ss`

## Script to create shortcut

You can automate the creation of table shortcuts from data quality audit extracts failed row data by using this script in a Fabric notebook. After creating the shortcut tables, your error records for new job runs on the asset shortcut table automatically refresh in Fabric.

```Python

# NEW Script to automate the creation of table shortcuts from Data Quality audit extracts failed row data.

# Update these three values for your Fabric Workspace ID, Lakehouse ID and Purview BYOC Self-serve store path
workspaceId = "f28dc1c8-360c-4788-9f46-e69853b1c40d" #Example: f28dc1c8-360c-4788-9f46-e69853b1c40d
lakehouseId = "77d6df6b-64ab-4628-985f-9365591a85a8" #Example: 77d6df6b-64ab-4628-985f-9365591a85a8
dataqualityauditPath = "Files/SelfServeFolder/DataQualityAuditExtracts" #Example: "Files/DEH2/DataQualityAuditExtracts"

#Use for lakehouses with Lakehouse-Schema (Public preview feature)
DestinationShortcutUri = f"abfss://{workspaceId}@onelake.dfs.fabric.microsoft.com/{lakehouseId}/Tables/DataQualityAuditExtracts" 

#Use for lakehouses without Lakehouse-Schema
#DestinationShortcutUri = f"abfss://{workspaceId}@onelake.dfs.fabric.microsoft.com/{lakehouseId}/Tables" 

import sempy.fabric as fabric
from sempy.fabric.exceptions import FabricHTTPException
import fnmatch
import re
import os
from collections import deque

SourceUri = f"abfss://{workspaceId}@onelake.dfs.fabric.microsoft.com/{lakehouseId}/{dataqualityauditPath}"

request_headers = {
            "Authorization": "Bearer " + mssparkutils.credentials.getToken("pbi"),
            "Content-Type": "application/json"
        }
print(request_headers)

def is_delta_table(uri: str):
    #print("Checking for uri:" + uri)
    delta_log_path = os.path.join(uri, "_delta_log")
    return mssparkutils.fs.exists(delta_log_path)

def extract_onelake_https_uri_components(uri):
    pattern = re.compile(r"abfss://([^@]+)@[^/]+/([^/]+)/(.*)")
    match = pattern.search(uri)
    if match:
        workspace_id, item_id, path = match.groups()
        return workspace_id, item_id, path
    else:
        return None, None, None

def is_valid_onelake_uri(uri: str) -> bool:
    workspace_id, item_id, path = extract_onelake_https_uri_components(uri)
    if "abfss://" not in uri or workspace_id is None or item_id is None or path is None:
        return False
    return True

def get_onelake_shorcut(workspace_id: str, item_id: str, path: str, name: str):
    shortcut_uri = (
        f"v1/workspaces/{workspace_id}/items/{item_id}/shortcuts/{path}/{name}"
    )
    result = client.get(shortcut_uri).json()
    return result

def get_last_path_segment(uri: str):
    path = uri.split("/")  # Split the entire URI by '/'
    return path[-1] if path else None

def create_onelake_shorcut(SourceUri: str, dest_uri: str, result: list):
    src_workspace_id, src_item_id, src_path = extract_onelake_https_uri_components(
        SourceUri
    )

    dest_workspace_id, dest_item_id, dest_path = extract_onelake_https_uri_components(
        dest_uri
    )

    name = get_last_path_segment(SourceUri)
    dest_uri_joined = os.path.join(dest_uri, name)

    # If the destination path already exists, return without creating shortcut
    if mssparkutils.fs.exists(dest_uri_joined):
        print(f"Table already exists: {dest_uri_joined}")
        result.append(dest_uri_joined)
        return None

    request_body = {
        "name": name,
        "path": dest_path,
        "target": {
            "oneLake": {
                "itemId": src_item_id,
                "path": src_path,
                "workspaceId": src_workspace_id,
            }
        },
    }
    #print(request_body)

    shortcut_uri = f"v1/workspaces/{dest_workspace_id}/items/{dest_item_id}/shortcuts"
    print(f"Creating shortcut: {shortcut_uri}/{name}..")
    try:
        client.post(shortcut_uri, json=request_body, headers=request_headers)
    except FabricHTTPException as e:
        print(e)
        print(e.error_reason)
        return None

    return get_onelake_shorcut(dest_workspace_id, dest_item_id, dest_path, name)

client = fabric.FabricRestClient()

queue = deque([SourceUri])
result = []

while queue:
    current_uri = queue.popleft()

    #print(current_uri)
    
    if  is_delta_table(os.path.join("", current_uri)):
        #print(current_uri)
        shortcut = create_onelake_shorcut(os.path.join("", current_uri), DestinationShortcutUri, result)
        if shortcut is not None:
            result.append(shortcut)
        continue;
    
    # List subitems in the current folder
    subitems = mssparkutils.fs.ls(current_uri)   
    for item in subitems:
        if item.isDir:
            queue.append(item.path)   

print(f"{len(result)}" + " error record shortcut tables present in the lakehouse: ")
for item in result:
    print(item)    

```

## Error records for on-premises data sources

Data quality error records for [on‑premises data sources](unified-catalog-data-quality-on-premises-data-sources) are stored within the corresponding on‑premises Oracle or SQL Server databases. Users must define a designated error database where data quality failed records will be stored. For each supported on‑premises data source, users are required to create an error database in the same environment. For example, if users are performing data quality assessments on an Oracle database, they must create an Oracle error database to store the resulting failed or error records. Similarly, if users are assessing data quality on a SQL Server database, they must create a SQL Server database to store the corresponding data quality failed records.

### Example of Oracle database data quality error records setup

#### Error record table naming convention

**Table Name Format**

`PURVIEW_ERRORRECORD_<SCHEMA>_<ASSET_NAME>`

**Example**

- Schema: ORACLENEW\_DATAGOV
- Asset / Table Name: EMPLOYEE\_DETAILS\_ERRORRECORD

**Final table name:**

PURVIEW\_ERRORRECORD\_ORACLENEW\_DATAGOV\_EMPLOYEE\_DETAILS\_ERRORRECORD

This convention ensures:

- Clear traceability to the source schema
- Easy identification of error-record tables
- Alignment with Purview data governance standards

#### Data load scenarios

**Scenario 1: First-Time Load (Table Creation)**

- Table, columns, and indexes are created during the first execution
- Records inserted: 1,000,000
- Rules applied: 1

**Timestamps:**

- CreatedAt: 01/28/2026 07:37:55 PM
- LastModifiedAt: 01/28/2026 07:41:34 PM

**Scenario 2: Load on existing table**

- Table already exists
- Only data insertion occurs
- Records inserted: 1,000,000
- Rules applied: 1

**Timestamps:**

- CreatedAt: 01/28/2026 07:33:19 PM
- LastModifiedAt: 01/28/2026 07:36:54 PM

#### Failure recovery and restart logic

- If data insertion fails, the process resumes from the last successfully inserted record.
- Previously inserted records aren't duplicated.

This ensures:

- Idempotent behavior
- No data loss
- Minimal reprocessing

#### Querying error record tables

Source Table: MANUFACTURERS Error Record Table: PURVIEW\_ERRORRECORD\_DBO\_MANUFACTURERS

**Sample query**

```
SELECT TOP 5 *
FROM PURVIEW_ERRORRECORD_DBO_MANUFACTURERS WITH (NOLOCK)
WHERE _PurviewJobId = 'c7f7c92e-9a36-46c5-86bc-bc3c595d5ddd';
```

This query retrieves error records associated with a specific Microsoft Purview job execution.

#### SQL Server performance metrics

1 Million Record Insert Performance

**Execution time:**

- CreatedAt: 01/29/2026 04:45:05 PM
- LastModifiedAt: 01/29/2026 04:54:14 PM

Total Time Taken: ~9 minutes

This demonstrates efficient bulk insertion using parallel processing.

Note

- Proper Oracle and SQL Server permissions should be configured for data governance operations.
- Use standardized naming convention for error record tables.
- Large-scale inserts should be optimized using parallel batching.
- Enabling failure recovery ensures safe restart without duplication.