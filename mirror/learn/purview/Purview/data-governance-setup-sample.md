---
layout: Conceptual
title: Sample setup walkthrough of Microsoft Purview Unified Catalog and Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-setup-sample
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: nidought
ms.date: 2025-02-19T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Follow a sample setup of Microsoft Purview Unified Catalog and Data Map to start building your data governance practice.
locale: en-us
document_id: ee14c439-1f48-7d56-34f3-bacb0192fe6c
document_version_independent_id: ee14c439-1f48-7d56-34f3-bacb0192fe6c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-setup-sample.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-setup-sample
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-setup-sample.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/8f37329d-5c2f-4d50-b9b8-aa5cf54dbffe
- https://authoring-docs-microsoft.poolparty.biz/devrel/655f39c4-21c5-49d3-8367-a1f9c1a0b930
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/e13db295-3de6-46d5-bcdf-8785a76e3843
- https://authoring-docs-microsoft.poolparty.biz/devrel/d30b39f7-a405-488d-84ef-d6d5296ad372
platformId: e6d055af-1472-f580-4ff7-904d1f9a340c
---

# Sample setup walkthrough of Microsoft Purview Unified Catalog and Data Map | Microsoft Learn

Microsoft Purview data governance, featuring Microsoft Purview Unified Catalog and Microsoft Purview Data Map, delivers comprehensive visibility, data confidence, and responsible innovation to help organizations achieve greater business value in the era of AI. Using an example of managing health data, follow the steps in this article to help you understand how to set up Unified Catalog and use its functionality to build a sound data governance practice for your organization.

## Step 1: Set up your governance domains in Unified Catalog

Governance domains are the key to establishing accountability for your data and help to federate governance of that data across the company. When you create governance domains, start with the proper owner to ensure you can effectively identify and collaborate with experts for all of the data in the data estate. Governance domains can be many different types to align to the type of data boundary for the team that governs that data. For example: functional domains (finance, HR, sales), or data domains (product, customer, health).

### Prerequisites

- You need the [Data governance administrator role for the Unified Catalog](data-governance-roles-permissions#how-to-assign-and-manage-role-groups).

### Grant permissions and build the first governance domain

1. Open the [Microsoft Purview portal](https://purview.microsoft.com).
2. Sign in to the Microsoft Purview portal using credentials for an admin account that has the *Role management* role (for example, a Purview administrator). Go to **Settings &gt; Roles and scopes** to view and manage.
3. Select **Role groups**.
4. On the **Role groups for Microsoft Purview solutions** page, select the **Data Governance** role group.
5. On the **Edit member of the role group** page, select **Choose users** or **Choose groups**.
6. Select the check box for all users or groups you want to add to the role group.
7. Select **Select**.
8. In Unified Catalog, select **Catalog management**, then select **Governance domains**.
9. On the **Governance domains** page, you can set up the rest of your catalog to enable others to federate the ownership of data, empower teams to build out their knowledge, and establish business value of your data.

    1. Start by selecting **New governance domain**.
        1. You can update the name of your governance domain. For this tutorial, name it '(Tutorial) Personal Health' and give it a description of 'Personal health data refers to any information related to an individual’s physical or mental health that is collected and used within the healthcare sector. This data can include a wide range of types, such as medical records, treatment histories, diagnostic images, and laboratory test results. It's often protected under various laws and regulations to ensure privacy and confidentiality.'
        2. Select the type as a 'data domain'.
        3. Leave the parent blank (if this is the first governance domain in the catalog, it doesn't have a parent).
        4. Select **Create**.
        5. Now create two more domains on your own. These domains are key points of federation for collaboration and governance in your organization. Think about who might be the owners of your domains when you implement Unified Catalog.
            1. You can follow these examples:

            - A **Corporate** functional domain represents the highly controlled assets and terms that an entire company uses. - **Sales** is a functional domain that most organizations have as a child domain of Corporate.
10. Select the governance domain you created.
11. Select the **Roles** tab of the governance domain.
12. By default, when you create the governance domain, you're added to all roles in the governance domain. As a governance domain owner, you add the data stewards (business experts in your domain) and the data product owners (who know which data assets are best for others to consume).
13. Switch back to the **Details** tab.
14. Select **Manage policies** to apply a domain level policy. This policy applies to all data products in the domain. By enabling the automatic application of a policy, data experts don't have to be policy experts as well.
15. In the **Manage access policies** tab, select the checkbox next to **Permit data copies.** By selecting this policy option, it automatically applies an attestation requiring all users who request access to your data products to attest that they understand the data copy policy for your data.
16. Select **Save changes** to confirm the policy is set by the governance domain.
17. Select **Publish** on the governance domain, which publishes all other concepts within the domain.

### Create glossary terms

Adding glossary terms to your governance domain helps others understand how the business uses and interprets the data. Glossary terms also ensure insights use common terms, and generally your knowledge across your governance domain.

1. On the page for your governance domain, find the **Glossary terms** card and select **View all**.
2. On the **Glossary terms** page, select **New term**.
3. Enter details: 1. Name: "Outbreak."

    1. Description: A disease that affects or has the potential to affect a large portion of the population.
    2. You can leave the rest blank for now but there are fields to collect: the term owner responsible for defining the term for your company, acronyms to share common also known as names of the term, lastly you can provide links to the resources that would have even more information about the term.
4. Select **Create**.
5. Select **Manage Policies**. Similar to the domain level policies, you can create term level policies that apply wherever the term is in use.
6. Check the box next to **Manager approval required**. This policy enforces a secondary approval from the user's manager in Microsoft Entra ID when access is requested to the data products.
7. Select **Publish** for the Outbreak term created. Published terms are filterable in Unified Catalog and ensure others that use the term to describe their data product can see that description in Unified Catalog while browsing the data product.
8. Now create two more terms. This time, select the "Outbreak" term as the parent term for the terms you created. Try building relationships between these child terms in the related tab on either term to help build out the network of how these terms work together to explain the entirety of a topic.

    1. Pandemic: A global outbreak of a disease that affects a large number of people across multiple countries/regions or continents.
    2. Epidemic: A countrywide or regional outbreak of a disease that is highly contagious and affects a large portion of the population.
9. Try creating a couple of other terms in any other domains you created earlier. If you're not sure what to add, select **Get suggested terms** to have generative AI propose a few based on the description and name of the domain you already provided.

### Add an OKR

Add an OKR (objective and key result) for your Personal Health domain to help others understand the business value of your data. This step builds a direct connection between your data and the business value it provides.

1. Select the **OKR** box from the governance domain page.
2. Select **New OKR**.
3. Enter the details of the objective first:

    1. Objective: Reduce pandemic risk by enabling effective patient vaccine uptake.
    2. Owner: Enter your name
    3. Target date: '2024-12-31'
4. Select **Create**.
5. Add key results to your objective to make the goals measurable and to monitor progress towards the goal. Select **Add key result**.
6. Enter the Key result details:

    1. Key result: Ensure 80% older age groups(&gt;65 years) that are most likely to be affected by the pandemic receive full vaccination by end of the calendar year 2024.
    2. Progress status: On track
    3. Progress Amount: 70
    4. Goal amount: 80
    5. Maximum amount: 100
7. Select **Create**.
8. Select **Publish**.

### Create critical data elements

Create a critical data element (CDE) in Personal Health to ensure the most important columns of data have a consistent definition and understanding. The CDE always meets business expectations for how that data is formed and stored.

1. From the governance domains page with the Personal Health domain selected, select the **Critical data elements** box.
2. Select **New critical data element**.
3. Enter the basic CDE metadata:
    1. Name: Age groups
    2. Description: Common grouping of person ages used to ensure needed analytical reports follow a reference that others can depend on and removing individual ages to improve anonymity of the data. The age group is divided into eight groups: &lt;2 years, 2-4 years, 5-11 years, 12-17 years, 18-24 years, 25-49 years, 50-64 years, 65+ years.
    3. Owner: enter your name
    4. Expected Data Type: Text
    5. Select **Create**.

The real power of the CDE is that it maps directly to the physical data columns where this data is stored. This connection ensures common understanding and enables the evaluation of Data Quality rules and policies at scale.

1. From the CDE you just created, select **Add column**.
2. Search for the **Covid 19 Vaccine and Case Trends** data asset from the gold container of the data lake
3. Select the box, not the name, of the **Covid 19 Vaccine and Case Trends** asset.

    Tip

    If you select the blue name of the asset, it opens a new window showing you the asset details.
4. Select the radio button next to the AgeGroupVacc column.
5. Select **Add**.
6. Select the **Data quality** tab at the top of the CDE you just created to apply data quality rules to the CDE. It's similar to how you added policies for glossary terms and governance domains.
7. Select **New rule**
8. Select **Data type match**
9. Enter Rule name: Confirm Age group formatting
10. Select **Create**.
11. Select **Publish** on the CDE

This CDE now automatically applies a data quality rule to every data product that uses the Covid 19 Vaccine and Case Trends asset, which you see in the next section.

1. Try creating a couple of other CDEs in your other domains. Here are some ideas:
    - Sales: Revenue and Seller Name
    - Corporate: Product ID

## Step 2: Set up and register your data in Data Map

If you don't have data sources available for scanning, follow these steps to fully deploy an Azure Data Lake Storage (ADLS Gen2) example.

Tip

If you already have a data source in the same tenant as your Microsoft Purview account, move ahead the next part of this section to scan your assets.

In a real data estate, you find many different systems in use for different data applications. There are reporting environments like Fabric and Snowflake where teams use copies of data to build analytical solutions and power their reports and dashboards. There are operational data systems that power the applications teams or customers use to complete business processes that collect or add data based on decisions made during the process.

To create a more realistic data estate, show many sources of data in the catalog, which can cover the breadth of different data uses any company might have. The types of data required to power a use case can be vastly different with business users that need reports and dashboards, analysts need conformed dimensions and facts to build reports, data scientists or data engineers need raw source data that came directly from the system that collects the data. All of these and more enable different users to see the importance of finding, understanding, and accessing data in the same place.

For some other tutorials to add data to your estate, follow these guides:

- [Fabric Lakehouse Tutorial](/en-us/fabric/data-engineering/tutorial-build-lakehouse) – provides the base of a reporting environment
- [Azure SQL Database (Sample)](/en-us/sql/samples/sql-samples-where-are) – provides a well structured example of an operational data store

### Prerequisites

- Subscription in Azure: [Create Your Azure Free Account Today](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn)
- Microsoft Entra ID for your tenant: [Microsoft Entra ID Governance](/en-us/entra/id-governance/identity-governance-overview)
- A Microsoft Purview account and [administrator privileges](purview-permissions) (this is the default if you created the Microsoft Purview account).
- All resources; Microsoft Purview, your data source, and Microsoft Entra ID have to be in the same cloud tenant.

### Set up your data estate

##### A. Create and populate a storage account

1. Follow this guide to create a storage account: [Create a storage account for Azure Data Lake Storage Gen2](/en-us/azure/storage/blobs/create-data-lake-storage-account)
2. Create containers for your new data lake:
    1. Go to the **Overview** page of your Storage Account.
    2. Select the **Containers**tab under the Data storage section.
        1. Select **Container**.
        2. Name the container "bronze" and select **Create**.
        3. Repeat these steps to create a "gold" container.
3. Download some example CSV data from data.gov: [Covid-19 Vaccination And Case Trends by Age Group, United States](https://data.cdc.gov/api/views/gxj9-t96f/rows.csv?accessType=DOWNLOAD)
4. Upload the CSV to the container named 'bronze' in the storage account you created.
5. Select the container named 'bronze' and select **Upload**.
6. Browse the location where you saved the CSV and select the **Covid-19\_Vaccination\_Case \_Trends** file.
7. Select **Upload**.

##### B. Create an Azure Data Factory

This step demonstrates how data moves between layers of a medallion data lake and ensures the data is in a standardized format that consumers expect to use. This step is a prerequisite for running data quality.

1. Follow this guide to create an Azure Data Factory: [Create an Azure Data Factory](/en-us/azure/data-factory/quickstart-create-data-factory)
2. Copy the data from the CSV in the 'bronze' container to the 'gold' container as a Delta format table using this Azure Data Factory guide: [Transform data using a mapping data flow](/en-us/azure/data-factory/tutorial-data-flow)
3. Open the Azure Data Factory (ADF) experience from the [Azure portal](https://portal.azure.com) by selecting **Launch studio** on the **Overview** tab of the ADF resource created.
4. Select the **Author** tab in ADF studio.
5. Select the **+** command, then select **Data flow**.
6. Name the dataflow 'CSVtoDeltaC19VaxTrends'.
7. Select **Add Source** in the empty box.
8. Set Source settings to:

    1. Output stream name: 'C19csv'
    2. Description: leave blank
    3. Source type: Inline
    4. Inline dataset type: Delimited Text
    5. Linked Service: Select the data lake where you stored the csv
9. Set Source options to:

    1. File mode: File
    2. File path: /bronze/ Covid-19\_Vaccination\_Case \_Trends
    3. Allow no files found: leave unchecked
    4. Change data capture: leave unchecked
    5. Compression type: None
    6. Encoding: Default(UTF-8)
    7. Column delimiter: Comma (,)
    8. Row delimiter: Default(\r, \n, or\r\n)
    9. Quote character: Double quote (“)
    10. Escape character: Backslash ()
    11. First row as header: CHECKED
    12. Leave the rest as defaults
10. Select **Next** by the source created and select **Sink**.
11. Create the sink where the format and location of the data to be stored to move the data from a csv in 'bronze' to a delta table in 'gold'.

    1. Set the Sink values (leave all settings as default unless specified).
    2. Sink type: Inline.
    3. Inline dataset type: Delta.
    4. Linked service: the same data lake as used in the source, because you are storing in a different container.
12. Set the Setting values (leave all settings as default unless specified)

    1. Folder path: gold/Covid19 Vaccine and Case Trends.
13. Enter the value because this name is how you want to store the data and it doesn't exist to select.
14. Select **Validate**. This action checks your data flow and provides instructions to fix any errors.
15. Select **Publish all**.
16. Select the **+** command, then select **Pipeline**.
17. Name your pipeline 'CSV to Delta C19 Vax Trends'.
18. Select the dataflow created in the previous steps CSV to Delta (C19VaxTrends) and drag and drop it on the open pipeline tab.
19. Select **Validate**.
20. Select **Publish**.
21. Select **Debug** (use activity runtime) to run the pipeline.

    Tip

    If you get errors for spaces or inappropriate characters for delta format, open the downloaded CSV and make corrections. Then re-upload and overwrite the CSV in the bronze zone. Then rerun your pipeline.
22. Navigate to your gold container in the data lake and you should now see the new Delta table created during the pipeline.

### Scan your assets

If you haven't scanned data assets into your Data Map, follow these steps to populate your data map.

Scanning sources in your data estate automatically collects the metadata of the data assets (tables, files, folders, reports, and more) in those sources. When you register a data source and create the scan, you establish the technical ownership over the sources and assets that appear in the catalog. You also control who can access which metadata in Microsoft Purview. When you register and store sources and assets at the domain level, you store them at the highest level of access hierarchy. Typically, it's best to create some collections where you scan the asset metadata and establish the correct access hierarchy for that data.

- [Provide reader access for Microsoft Purview Managed Identity (MSI) to your data lake or other data store.](register-scan-adls-gen2#authentication-for-a-scan)
    Tip

    The MSI is the account name of the Microsoft Purview instance.

If you choose to use Fabric or SQL, use these guides to provide access:

- [Microsoft Fabric](register-scan-fabric-tenant#authentication-to-scan)
- [Azure SQL Database](register-scan-azure-sql-database#configure-authentication-for-a-scan)

### Register your data lake and scan your assets

1. In Data Map, under the domains tab, select the **Role assignments** for the domain (it's the name of Microsoft Purview account):

    1. Add yourself as the data source admin and the data curator to the domain.
        1. Select the person icon next to the role **Data source admin**. 1. Search your name as it is in Microsoft Entra ID (you might need to enter your full name spelled exactly as it is in Microsoft Entra ID).
        2. Select **OK**.
        3. Repeat these steps for data curator.
2. Register the data lake:

    1. Select the **Data sources** tab.
    2. Select **Register**.
    3. Select the Azure Data Lake Storage Gen2 storage type.
3. Provide the details to connect:

    1. Subscription (optional)
    2. Data Source Name (this is the name of the ADLS Gen2 source)
    3. Collection where asset metadata should be stored (optional)
    4. Select **Register**
4. Once registration of the data source is complete, you can configure the scan. Registration signifies that Microsoft Purview is connected to the data source and has placed it in the correct collection for ownership. Scanning reads the metadata from the source and populates the assets in the data map.
5. Select the source you registered in data sources tab
6. Select new scan and provide details:

    1. Use the default integration runtime for this scan
    2. Credential should be Microsoft Purview MSI (system)
    3. Scan level is Auto Detect
    4. Select a collection or use the domain (collection must be the same collection or child collection of where the data source was registered)
    5. Select Continue

    Tip

    At this point the connection is tested to validate a scan can be done. If you don't grant the Microsoft Purview MSI reader access on the data source, it fails. If you're not the data source owner or don't have user access contributor, the scan fails since it expects you have authorization to create the connection.
7. Now only select the container "gold" where you placed the delta table in the building data section of the tutorial. This selection prevents scanning any other data assets that are in your data store.

    1. Should have only one blue check next to gold, you can leave checks next to everything as it will scan the full source and still create the assets we'll use and more.
    2. Select **Continue**
8. In the select a scan rule set screen you should use the default scan rule set.
9. Select **Continue**
10. In set a scan trigger you'll set the frequency of the scanning so as you continue to add data assets to the gold container of the lake it will continue to populate the data map. Select **Once**.
11. Select **Continue**.
12. Select **Save and Run**. This action creates a scan that reads the metadata from the gold container of your data lake and populates the table we'll use in Unified Catalog in the next sections. If you only select save, it doesn't run the scan, and you don't see the assets. Once the scan is running, you see the scan you created with a **Last run** status of **Queued**. When the scan reads complete your assets are ready for the next section. This process could take a few minutes or hours depending on how many assets you have in your source.

## Step 3: Publish your data products

Creating data products is essential to ensure that your organization can discover the right data. Data products help prevent overgoverning data that has low or no value in your data estate because it has no use or limited value. When your data experts publish data products, you activate your most valuable data and build the right level of governance based on that value. Curating assets that technical teams don't know the business purpose of, or trying to govern everything in your complex and growing data estate, causes extra time and lost productivity chasing down the details of data that might never be used or could just be removed from the estate. Instead, focus on the pieces of data that have value and that people need to discover and build even more value. As teams use more data and gain a better understanding of what is needed, you can create more useful data products to meet those demands. Governance can adapt to ensure it always stays the right size based on the value and sensitivity of the data.

### Prerequisites

- Be a [data product owner for the governance domain](data-governance-roles-permissions#governance-domain-level-permissions) you're using.
- Have data assets in the Data Map. If you don't, see [section 2 of this tutorial](section2-setup-data-estate) to add some.
- Publish a governance domain to publish a data product. If you don't have one, see [section 1 of this tutorial](section1-setup-your-governance-domain) to create one.

### Create and publish a data product

1. Open the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Unified Catalog**.
3. Select **Catalog management** and then **Governance domains**.
4. From the **Governance domains** page, select the Personal Health domain.
5. Select **Go to data products** under **Business concepts**.
6. Here's where the data experts called data product owners will identify the data assets that are intended to be consumed by others in your organization, and provide the necessary information to make them usable.
7. Select **New data product**.
8. Provide details about the data product: 1. Name: "Covid-19 Vaccination and Case Trending by Age" 1. Description: "This data comes from the CDC as a part of the U.S. Department of Health & Human Services. The data contains trends in vaccinations and cases by age group, at the US national level. Data is stratified by at least one dose and fully vaccinated. Data also represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities."

    1. Type: Dataset
    2. Select **Next**.
    3. Use cases: `This data is provided for public use and is intended to help understand the trends of vaccination up take and new cases by different age groups. The ages are banded into two groups ranging from <2 years to 65+ years. Similarly the trends are provided in daily numbers that provide seven day average of new cases by age group.`
    4. Mark as **Endorsed** as checked.
    5. Select **Save**.
9. Now you have the base metadata of the data product built out. Next, add some properties and map the asset from Data Map.
10. Select **Add data assets**.
11. You see the assets you scanned into Data Map, including all folders and layers of the data source.
12. Search for the **Covid19 Vaccine and Case Trends** asset you added to the gold container of your data lake and select this resource set.
13. Select **Add**. You can select as many assets as needed for a data product but here only one is needed.

    Tip

    Select **Get suggestions** to have generative AI help pick from the assets in your data map and select the Covid19 Vaccine and Case Trends from a reduced list of results.
14. You can now see the asset added to your data product.
15. Select **Add term** next to the glossary terms title.
16. Select the Outbreak term created earlier and select **Add**.
17. You should see the critical data element for age group from the asset mapped to the data product now.
18. Select **Add OKR** next to the OKR title.
19. Select the Reduce pandemic risk by enabling effective patient vaccine uptake. It's the objective you created in the [first section](section1-setup-your-governance-domain).

### Manage data product access request policies

At the top of the page, the last step before publishing the data product is to select **Manage policies**. Here, you configure the access policies and request access workflow by making selections and providing the names for approval. You can also use the **Inherited policies** tab to see the governance domain policy applied for data copies attestation you applied earlier. It's the same for the **Manager approval** required coming from the Outbreak glossary term.

1. Select the **Manage policies** tab.
2. Under **Access time limit**, provide details for how long the request for access is good before needing to be renewed. Set this value to grant access for up to one year.
3. In the box, enter 1.
4. Select years in the drop-down.
5. Under approval requirements, provide your name in the approvers box. (It requires the name registered in Microsoft Entra ID.)

    Note

    You don't need to check manager approval because that policy is inherited from the outbreak glossary term.
6. Select **Preview request form** to see what the catalog consumers view when requesting access. You see the data copy attestation and manager approval required because they were set by the governance domain and glossary term.
7. Select **Save changes**.

Once you map the data assets and configure the access policies, you're ready to publish your data product to the catalog.

1. Select **Publish** on the data product.
2. Try creating a Profit Report in other domains you created earlier

    1. Profit Report, Type: Dashboards/reports.
    2. Product Master, Type: Maser data and reference data.

Note

You can add many assets to these and see how a data product with many assets looks. Add the data products to the terms from any domain to see how the glossary is used to describe the data using a consistent set of terms.

## Step 4: Run data quality

Now that you have a data product available in the catalog, running data quality rules tells everyone that the data is in good shape and ready to use. As you learn more about the data, add new data quality rules to make sure it's fit for all use cases. Ensuring data products are of the highest quality helps build trust in your data and shows others that you're monitoring and improving it. As the value of data increases, you need to more closely monitor and control the quality of that data. Poorly managed data quality issues can cause significant negative effects.

### Prerequisites

- Data quality rules can only be run on delta format tables in ADLS Gen2 and Microsoft Fabric.
- The Managed Identity from Microsoft Purview must be enabled to read the data source as it is the only supported credential for data quality today.
- You must have the [data quality steward role](data-governance-roles-permissions#governance-domain-level-permissions) in the governance domain you're running data quality in.
- You must be the owner or have user access administrator access to the data source you're connecting data quality scanning to ensure proper security authorization to scan the data.
- You must have the [data profile steward role](data-governance-roles-permissions#governance-domain-level-permissions) to run profiles on your data.

### Create and run data quality rules

1. Open the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Unified Catalog**.
3. Select the **Data quality** tab under **Data management**.
4. Select the Personal Health Domain created in [section 1](section1-setup-your-business-domain).
5. Select **Manage**, then select **Connections**. When you build this connection, you can run data quality scans on your data source in that governance domain. This step prevents teams from gaining access to knowledge of the data without proper authorization.
6. Select **New** on the connections screen to create a new connection: 1. Enter the display name "Personal Health ADLSg2 DQ".

    1. Select source type of Azure Data Lake Storage Gen2.
        1. Enter details of the data source created in [section 2](section2-setup-data-estate). 
            Note

            Credential must be Microsoft Purview MSI (system) for a data quality connection.
        2. Select **Test connection**.
        3. Once the connection is tested, select **Submit**.

Once the connection is established, you're ready to run profiles and start building data quality rules. This step ensures that the experts who know the business rules and appropriate rules are running on the most important data products.

1. Go back to the **Data quality** page.
2. Select the Personal Health governance domain.
3. Select the **Covid-19 Vaccination and Case Trending by Age** data product built in [section 3](section3-publish-data-products).
4. Select the asset that you added to the data product. (It must be in delta format from [section 2](section2-setup-data-estate) or data quality won't run).
5. Apply data quality rules to the columns of the data to measure if it meets your expectation of quality:
    1. Select **Rules** tab on the asset selected.
    2. Select **New rule**.
    3. Select Empty/blank fields rule.
    4. Enter details:
        - Select AgeGroupVacc column from the column drop-down
        - Rule Name: Confirm Vaccination Age Group Exists
    5. Select **Create**.
    6. Select **New rule**.
    7. Select **Data type match**.
    8. Enter details.
    9. Select DateAdministered column.
    10. Select **Create**.
6. Select **Run Data quality scan**.

### Profile data

Create a profile for your data to see the high-level statistics of each column and discover any anomalies that could require a new rule.

1. In Unified Catalog, select **Health management**, then select **Data quality**.
2. Select **Profile data**.
3. Check the top box next to **Column name** to profile all columns. The system recommends which columns to profile, and you can select columns that you know are worth profiling to help prevent profiles on highly sensitive data or data you know is sparsely populated.
4. Select **Run profile**.

When the scan completes, you can review the data quality score and profile for your new data product. All users of the catalog can see the data quality score, so everyone knows the status of the data.

Create a schedule for your data quality scans to ensure you're continuously monitoring for data quality issues. Set alerts to make sure you're addressing data quality issues before consumers are affected.

1. Under **Health management**, select **Data quality**.
2. Select the Personal Health domain where you configured the data quality rules.
3. From the **Manage** dropdown list, select **Scheduled scans**.
4. On the **Scheduled scans** page, select **New**.
5. Add **Overview**details
    1. Name: Personal Health DQ Monthly Evaluation
    2. Description: Monthly scan of DQ rules for continuous improvement.
6. Select **Continue**
7. Select the scope of the scan
8. Check the box next to **Covid-19 Vaccination and Case Trending by Age** data product
9. Select **Continue**
10. Schedule the scan to ensure it runs on the last day of every month
    1. Select **Recurring**
    2. Recurrence: Every one Month
    3. Month days: Last
    4. Schedule scan time (UTC): 12:00:00
    5. Start recurrence at (UTC): leave as default
11. Select **Continue**
12. Review details of the scan to see if there are any changes you want to make before saving.
13. Select **Save**. Because you triggered a manual scan earlier, you don't need to trigger another scan now. If you need a new scan, select **Save and run**.

### Configure alerts

After scheduling scans for data quality, you can set up alerts to notify stewards about issues or when data quality problems or scan failures need attention. Configure a data quality alert for failed scans and when the score decreases by more than 5%.

1. Return to the Personal Health domain on the **Data quality** page.
2. From the **Manage** dropdown list, select **Alerts**.
3. Select **New**.
4. Enter alert details
    1. Display Name: Personal Health DQ Monthly Scan
    2. Description: To ensure minimum DQ thresholds are meeting consumer expectations.
    3. Target: Score decreases by more than
    4. Threshold: 5
    5. Turn off notifications: leave unchecked
    6. Turn on notification for failed quality scans: leave checked
    7. Recipient: enter your name
5. Select **Continue**.

Tip

When implementing in Unified Catalog, send the alerts to the stewards who can notify consumers of the issue and work with the technical owner of the data to make corrections.

At the end of this section, you have a functioning Unified Catalog with operational data quality to manage the data you're offering to organizational data consumers. Everything is set up to get the most valuable data to the consumer and build trust in the data that they use. As the value of the data grows and new data strategies emerge, the next section shows how you can manage the entire catalog or go deeper into specific data management with master data.

## Step 5: Master data management

Master data management (MDM) is the practice of conforming the most important data entities that must be accurate, unique, and consistently applied in all areas of the business because errors and issues in this data can impact the whole business. Through one of our MDM partners, you can integrate your choice of MDM solutions with Microsoft Purview to enable data unification, standardization, and cleansing that enables golden record creation and the publication of master data as data products.

Follow the tutorials here for your solution of choice: [Master data management in Microsoft Purview](data-governance-master-data-management)

## Step 6: Manage data health

In the **Health management** area of Unified Catalog, the central data office and other data managers can evaluate the status of the data against their company standards and effectively manage progress towards their strategy. To make sure that everyone in the company knows what they can do to increase the value of their data, it's essential that the standards are understood and scalable to the whole organization without needing to make everyone a data governance expert. Starting from an industry standard set of controls that are available out of the box, each data office can customize the controls to meet their expectations and ensure it aligns with their data goals. Critical to the effectiveness of these controls isn't only the measurement of these standards but also ensuring those responsible for the data can take action on their own and be held accountable for making the improvements that affect the value of data. In Data Estate Health, you can set and manage all of these critical capabilities.

### Prerequisites

- Data products, glossary terms, and other business concepts published in Unified Catalog. You can follow the previous sections to create these concepts:
    - [Section 1 - Set up a governance domain](section1-setup-your-business-domain)
    - [Section 3 - Publish your data products](section3-publish-data-products)
- At least 24 hours since the curation of data products.
- You must have the [Data Health Owner role](data-governance-roles-permissions#catalog-level-permissions) in Unified Catalog.

### Evaluate your data governance with data estate health

1. Open the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Unified Catalog**.
3. Under **Data Estate Health** in the left navigation, select **Health controls**.
4. Select the carrot **&gt;** next to the **Value Creation** control group.
5. While hovering over a control title, select the pencil icon to edit the control. By editing the control, you change the threshold of the control to set expectations for what the score should be and set the color scoring to demonstrate the progress stages.
6. The details enable you to provide a description of the control and what it means to your organization and set an owner for a specific control.
7. Select the **Rules** tab of the control to change the threshold. This setting has a high target and if it isn't healthy it's critical to follow up on.

    1. Inherit from group: toggle to switch off (should turn grey).
    2. Target score: 90
    3. Select **New rule**.
    4. Set the box next to the score to GreaterThanOrEqual
    5. Set the percentage to 90
    6. Status = Health (green)
    7. Else Box Status = Critical (Purple)
    8. Select **Save**.
8. Under data estate health, select **Metadata quality**.

Here you can change or add rules that create the scores of the control. Here you want to change the severity of the actions for **Value Creation** to ensure all users know the importance of this action.

1. Select **Configure severity**
2. Select the **Value Creation** control group
3. Select the **Business OKRs alignment** control title
4. Change the Severity from Medium to High and select **Save**
5. Select the **Health actions** tab
6. Filter **Assigned to:** to your name
7. Select an action where you can see what the owner of the action needs to do to ensure governance expectations are met or they can assign a new owner to get the best expert to provide their input. There's also a status that lets others know what work is ongoing and where other actions could need prioritization.

## Step 7: Data democratization

Data democratization enables users to find and access the data they need in a compliant manner. It ensures people can find the data they need to build business value. Unified Catalog provides a clean and easy experience to discover data. It empowers stewards to update and manage the data made available in the catalog at scale. In this section, you learn how users can find and request access to data and ensure that the appropriate approvers can track and provide inputs on those access requests.

### Prerequisites

- Completed steps 1-4 at minimum:
    - [Section 1 - Set up a governance domain](section1-setup-your-governance-domain)
    - [Section 2 - Set up your data estate](section2-setup-data-estate)
    - [Section 3 - Publish your data products](section3-publish-data-products)
- [A catalog reader role in one governance domain](data-governance-roles-permissions#governance-domain-level-permissions)

### Discover data products

1. In Unified Catalog, select **Discovery**, then select **Data products**.
2. On the **Data products** page, use the search bar to search for vaccination rates by age.
3. Here you see the data products you published in [section 2](section2-setup-data-estate). This view shows how users only see the data intended for them and prevents users from having to navigate a highly technical data estate.
4. Select the **Covid-19 Vaccination and Case Trending by Age**data product
    1. Here, consumers can see the metadata you provided and any of the other properties that you configured during setup. The data quality score is here as well so consumers know the quality before they even get access to the data.
    2. Select the asset and the consumer can see all of the columns that are available in the data asset.
    3. Select the Outbreak glossary term and the consumer can see the description and other information about the term to gain a deeper understanding of the data.
5. Once the consumer is confident that they want to use that data, they need to get approved access to the data.
    1. Select **Request access**
    2. Fill in the form detail to submit a request.
    3. User: leave your name
    4. Manager Approval: automatically required and directed to the Microsoft Entra ID manager.
    5. Purpose: select a purpose
    6. Business justification: OKR monitoring
    7. Check the box next to the attestation to say you understand the expectations to use this data.
    8. Select *Send.*

The access request is now sent to the listed manager in Microsoft Entra ID. From here, the manager can access the requests by opening the email and selecting a link or coming into Microsoft Purview. Approving and managing access can be done directly in Microsoft Purview.

1. In Unified Catalog, select **Catalog management**, then select **Requests**.
2. Select the **Personal Health** domain.
3. Select the request you submitted.
4. Now the approvers are able to approve or decline by selecting **Respond** on the request.