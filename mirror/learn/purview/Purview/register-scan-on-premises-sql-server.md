---
layout: Conceptual
title: Connect to and manage on-premises SQL server instances | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-on-premises-sql-server
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This guide describes how to connect to on-premises SQL server instances in Microsoft Purview, and uses Microsoft Purview's features to scan and manage your on-premises SQL server source.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: shjia
ms.service: purview
ms.subservice: purview-data-map
ms.topic: how-to
ms.date: 2026-03-20T00:00:00.0000000Z
ms.custom:
- template-how-to
- ignite-fall-2021
- sfi-image-nochange
locale: en-us
document_id: 50ded0e8-415b-cc5d-b2a3-4819949dc24e
document_version_independent_id: 50ded0e8-415b-cc5d-b2a3-4819949dc24e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-on-premises-sql-server.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-on-premises-sql-server
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-on-premises-sql-server.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 19cc64ca-ac0d-410a-eec9-4d5f08d4359b
---

# Connect to and manage on-premises SQL server instances | Microsoft Learn

This article outlines how to register on-premises SQL server instances, and how to authenticate and interact with an on-premises SQL server instance in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | Yes | Yes |

The supported SQL Server versions are 2005 and above. SQL Server Express LocalDB isn't supported.

When you scan an on-premises SQL server, Microsoft Purview supports:

- Extracting technical metadata including:

    - Instance
    - Databases
    - Schemas
    - Tables including the columns
    - Views including the columns

When setting up scan, you can choose to specify the database name to scan one database, and you can further scope the scan by selecting tables and views as needed. The whole SQL Server instance will be scanned if database name isn't provided.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

## Prerequisites

- [The enterprise version of Microsoft Purview](data-governance-free-version-upgrade-to-enterprise) or an active Microsoft Purview account using the [classic governance portal](use-microsoft-purview-governance-portal).
- You'll need to be a Data Source Administrator and Data Reader to register a source in the Microsoft Purview Data Map. Get details about [domain and collection permissions](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

- [Set up the right integration runtime for your scenario](data-map-integration-runtime-choose):
    - **To use a self-hosted integration runtime:** Use these instructions to [create and configure a self-hosted integration runtime](data-map-integration-runtime-self-hosted). In this case, classification of SqlBigDecimal isn't supported.

        - **To use a kubernetes supported self-hosted integration runtime:**[Follow the article to create and configure a kubernetes supported integration runtime](data-map-integration-runtime-kubernetes). (SQL authentication only.)

## Register

This section describes how to register an on-premises SQL server instance in Microsoft Purview using the [Microsoft Purview portal](https://purview.microsoft.com).

1. Accessing the Microsoft Purview Data Map depends on which portal experience you're using.

    - If you're using the Microsoft Purview portal, navigate directly to the portal (https://purview.microsoft.com) and select the **Data Map** solution.
    - If you're using the classic Microsoft Purview governance portal, navigate directly to the portal (https://web.purview.azure.com), select your Microsoft Purview account, and select **Data map** from the left menu.
2. Under **Source management**, select **Integration runtimes**. Make sure a self-hosted integration runtime is set up. If it isn't set up, follow the steps mentioned in prerequisites to create a self-hosted integration runtime for scanning from an on-premises or Azure VM that has access to your on-premises network.
3. Select **Data sources** on the left navigation.
4. Select **Register**.
5. Select **SQL Server**, then **Continue9**.

    ![Set up the SQL data source.](media/register-scan-on-premises-sql-server/set-up-sql-data-source.png)
6. Provide a friendly name, which will be a short name you can use to identify your server, and the server endpoint.
7. Select **Finish** to register the data source.

## Scan

Follow the steps below to scan on-premises SQL server instances to automatically identify assets and classify your data. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion)

### Authentication for scanning

There are two authentication methods supported for SQL server on-premises:

- SQL Authentication
- Windows Authentication - Not supported by a Kubernetes SHIR.

If SQL Authentication is applied, ensure the SQL Server deployment is configured to allow SQL Server and Windows Authentication.

To enable this, within SQL Server Management Studio (SSMS), navigate to **Server Properties** and change from **Windows Authentication Mode** to **SQL Server and Windows Authentication mode**.

![The Server Properties window is open with the security page selected. Under Server authentication, the S Q L Server and Windows Authentication mode is selected.](media/register-scan-on-premises-sql-server/enable-sql-server-authentication.png)

If Windows Authentication is applied, configure the SQL Server deployment to use Windows Authentication mode.

A change to the Server Authentication will require a restart of the SQL Server Instance and SQL Server Agent, this can be triggered within SSMS by navigating to the SQL Server instance and selecting "Restart" within the right-click options pane.

#### Creating a new login and user

If you would like to create a new login and user to be able to scan your SQL server, follow the steps below:

The account must have access to the **master** database. This is because the `sys.databases` is in the master database. The Microsoft Purview scanner needs to enumerate `sys.databases` in order to find all the SQL databases on the server.

Note

All the steps below can be executed using the code provided [here](https://github.com/Azure/Purview-Samples/blob/master/TSQL-Code-Permissions/grant-access-to-on-prem-sql-databases.sql)

1. Navigate to SQL Server Management Studio (SSMS), connect to the server, navigate to security, select and hold (or right-click) on login and create New login. If Windows Authentication is applied, select **Windows authentication**. If SQL Authentication is applied, make sure to select **SQL authentication**.

    ![Create new login and user.](media/register-scan-on-premises-sql-server/create-new-login-user.png)
2. Select Server roles on the left navigation and ensure that public role is assigned.
3. Select User mapping on the left navigation, select all the databases in the map and select the Database role: **db\_datareader**.

    ![user mapping.](media/register-scan-on-premises-sql-server/user-mapping.png)
4. Select OK to save.
5. If SQL Authentication is applied, navigate again to the user you created, by selecting and holding (or right-clicking) and selecting **Properties**. Enter a new password and confirm it. Select the 'Specify old password' and enter the old password. **It is required to change your password as soon as you create a new login.**

    ![change password.](media/register-scan-on-premises-sql-server/change-password.png)

##### Storing your SQL login password in a key vault and creating a credential in Microsoft Purview

1. Navigate to your key vault in the Azure portal. Select **Settings &gt; Secrets**
2. Select **+ Generate/Import** and enter the **Name** and **Value** as the *password* from your SQL server login
3. Select **Create** to complete
4. If your key vault isn't connected to Microsoft Purview yet, you'll need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account)
5. Finally, [create a new credential](data-map-data-scan-credentials#create-a-new-credential) using the **username** and **password** to set up your scan. Make sure the right authentication method is selected when creating a new credential. If SQL Authentication is applied, select "SQL authentication" as the authentication method. If Windows Authentication is applied, then select **Windows authentication**.

### Set up a self-hosted integration runtime

If you haven't already, you need to download and install the latest [self-hosted integration runtime](https://go.microsoft.com/fwlink/?linkid=2246619). For more information, see [the create and configure a self-hosted integration runtime guide](data-map-integration-runtime-self-hosted).

### Create and run scan

Now that you've set up authentication and a self-hosted integration

1. Open the Microsoft Purview portal and select the **Data Map**.
2. Select **Data sources**.
3. Select the SQL Server source that you registered.
4. Select **New scan**
5. Select the credential to connect to your data source. The credentials are grouped and listed under different authentication methods.

    ![Set up scan](media/register-scan-on-premises-sql-server/on-premises-sql-set-up-scan-win-auth.png)
6. You can scope your scan to specific tables by choosing the appropriate items in the list after enter Database name.

    ![Scope your scan](media/register-scan-on-premises-sql-server/on-premises-sql-scope-your-scan.png)
7. Then select a scan rule set. You can choose between the system default, existing custom rule sets, or create a new rule set inline.

    ![Scan rule set](media/register-scan-on-premises-sql-server/on-premises-sql-scan-rule-set.png)
8. Choose your scan trigger. You can set up a schedule or run the scan once.

    ![trigger](media/register-scan-on-premises-sql-server/trigger-scan.png)
9. Review your scan and select **Save and run**.

### View your scans and scan runs

To view existing scans:

1. Go to the Microsoft Purview portal. On the left pane, select **Data map**.
2. Select the data source. You can view a list of existing scans on that data source under **Recent scans**, or you can view all scans on the **Scans** tab.
3. Select the scan that has results you want to view. The pane shows you all the previous scan runs, along with the status and metrics for each scan run.
4. Select the run ID to check the [scan run details](data-map-scan-run-monitor-population#scan-run-details).

### Manage your scans

To edit, cancel, or delete a scan:

1. Go to the Microsoft Purview portal. On the left pane, select **Data Map**.
2. Select the data source. You can view a list of existing scans on that data source under **Recent scans**, or you can view all scans on the **Scans** tab.
3. Select the scan that you want to manage. You can then:

    - Edit the scan by selecting **Edit scan**.
    - Cancel an in-progress scan by selecting **Cancel scan run**.
    - Delete your scan by selecting **Delete scan**.

Note

- Deleting your scan does not delete catalog assets created from previous scans.