---
layout: Conceptual
title: Connect to and manage Snowflake in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-snowflake
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to register a Snowflake source in Microsoft Purview, configure authentication, and run scans to catalog your Snowflake databases and lineage.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: karashah
ms.service: purview
ms.subservice: purview-data-map
ms.topic: how-to
ms.date: 2026-03-24T00:00:00.0000000Z
ms.custom: template-how-to
locale: en-us
document_id: 272bde83-02d5-d9b2-cc8b-1adc9aa8a6eb
document_version_independent_id: 272bde83-02d5-d9b2-cc8b-1adc9aa8a6eb
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-snowflake.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-snowflake
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-snowflake.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 5ec577b3-01b2-2b8f-966e-312ba2513216
---

# Connect to and manage Snowflake in Microsoft Purview | Microsoft Learn

This article outlines how to register Snowflake, and how to authenticate and interact with Snowflake in Microsoft Purview. For more information about Microsoft Purview, read the [Microsoft Purview overview](purview).

Important

Snowflake [announced the deprecation of basic authentication](https://docs.snowflake.com/user-guide/security-mfa-rollout) and plans to disable it by August 2026. To align with the change and avoid any service disruptions, Microsoft Purview customers using the Snowflake Data Map connector should transition to Key Pair (SHIR) authentication.

**Recommended action (complete by July 2026)**: To provide customers with more time, Snowflake allows service users of type **LEGACY\_SERVICE** to continue using basic authentication until July 2026. This policy helps ensure there's no disruption to your service while you transition to the new authentication method. You can continue to use basic authentication for a limited period of time, while at the same time setting up and validating the new authentication mechanism Key Pair.

We recommend that Microsoft Purview customers update their users to the **LEGACY\_SERVICE** type. This change ensures continued access and provides more time to complete the transition. **This update must be completed before the end of July 2026 by running the following command in Snowflake**:

> 
> `*ALTER USER <purview_user_name> SET TYPE = LEGACY_SERVICE;`
> 
> The creation of new users with the LEGACY\_SERVICE type isn't permitted beginning August 2026.

## Supported capabilities

The following sections describe the capabilities available when scanning Snowflake in Microsoft Purview.

### Scanning capabilities

The following table summarizes the scanning capabilities supported for Snowflake in Microsoft Purview.

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

When scanning a Snowflake source, Microsoft Purview supports:

- Extracting technical metadata including:

    - Server
    - Databases
    - Schemas
    - Tables including the columns, foreign keys, and unique constraints
    - Views including the columns
    - Stored procedures including the parameter dataset and result set
    - Functions including the parameter dataset
    - Pipes
    - Stages
    - Streams including the columns
    - Tasks
    - Sequences
- Fetching static lineage on assets relationships among tables, views, streams, and stored procedures.

For stored procedures, you can choose the level of detail to extract in the Create and run scan section. Stored procedure lineage is supported for Snowflake Scripting (SQL) and JavaScript languages, and generated based on the procedure definition.

When setting up a scan, you can choose to scan one or more Snowflake databases entirely based on the given names or name patterns, or further scope the scan to a subset of schemas matching the given names or name patterns.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Known limitations

Be aware of the following limitations when scanning Snowflake in Microsoft Purview.

- When you delete an object from the data source, the subsequent scan doesn't automatically remove the corresponding asset in Microsoft Purview.
- Stored procedure lineage isn't supported for the following patterns:
    - Stored procedure defined in Java, Python, and Scala languages.
    - Stored procedure using SQL [EXECUTE IMMEDIATE](https://docs.snowflake.com/en/sql-reference/sql/execute-immediate) with static SQL query as variable.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You need Data Source Administrator and Data Reader permissions to register a source and manage it in the Microsoft Purview portal. For more information about permissions, see [Access control in Microsoft Purview](data-gov-classic-permissions).
- [Choose the right integration runtime configuration for your scenario](data-map-integration-runtime-choose).

    - To use Managed Virtual Network Integration Runtime to connect to Snowflake via private link, follow the steps in Connect to Snowflake via Managed Private Endpoint to set up the private endpoint.
    - To use Self-hosted Integration Runtime for scan, set up the latest [self-hosted integration runtime](https://go.microsoft.com/fwlink/?linkid=2246619). For more information, see [the create and configure a self-hosted integration runtime guide](data-map-integration-runtime-self-hosted).
        - Ensure [JDK 11](https://www.oracle.com/java/technologies/downloads/#java11) is installed on the machine where the self-hosted integration runtime is installed. Restart the machine after you newly install the JDK for it to take effect.
        - Ensure Visual C++ Redistributable (version Visual Studio 2012 Update 4 or newer) is installed on the self-hosted integration runtime machine. If you don't have this update installed, [download the Visual C++ Redistributable](/en-us/cpp/windows/latest-supported-vc-redist).

### Required permissions for scan

Microsoft Purview supports basic authentication (username and password) for scanning Snowflake. The default role of the given user will be used to perform the scan. The Snowflake user must have usage rights on a warehouse and the databases to be scanned, and read access to system tables to access advanced metadata.

Here's a sample walkthrough to create a user specifically for Microsoft Purview scan and set up the permissions. If you choose to use an existing user, make sure it has adequate rights to the warehouse and database objects.

1. Set up a `purview_reader` role. You need *ACCOUNTADMIN* rights to do this.

    ```sql
    USE ROLE ACCOUNTADMIN;
    
    --create role to allow read only access - this will later be assigned to the Microsoft Purview user
    CREATE OR REPLACE ROLE purview_reader;
    
    --make sysadmin the parent role
    GRANT ROLE purview_reader TO ROLE sysadmin;
    ```
2. Create a warehouse for Microsoft Purview to use and grant rights.

    ```sql
    --create warehouse - account admin required
    CREATE OR REPLACE WAREHOUSE purview_wh WITH 
        WAREHOUSE_SIZE = 'XSMALL' 
        WAREHOUSE_TYPE = 'STANDARD' 
        AUTO_SUSPEND = 300 
        AUTO_RESUME = TRUE 
        MIN_CLUSTER_COUNT = 1 
        MAX_CLUSTER_COUNT = 2 
        SCALING_POLICY = 'STANDARD';
    
    --grant rights to the warehouse
    GRANT USAGE ON WAREHOUSE purview_wh TO ROLE purview_reader;
    ```
3. Create a user `purview` for Microsoft Purview scan.

    ```sql
    CREATE OR REPLACE USER purview 
        PASSWORD = '<password>'; 
    
    --note the default role will be used during scan
    ALTER USER purview SET DEFAULT_ROLE = purview_reader;
    
    --add user to purview_reader role
    GRANT ROLE purview_reader TO USER purview;
    ```
4. Grant reader rights to the database objects.

    ```sql
    GRANT DATABASE ROLE SNOWFLAKE.OBJECT_VIEWER TO USER purview_reader;
    GRANT USAGE ON DATABASE <your_database_name> TO purview_reader;
    
    --grant reader access to all the database structures that purview can currently scan
    GRANT USAGE ON ALL SCHEMAS IN DATABASE <your_database_name> TO role purview_reader;
    GRANT USAGE ON ALL FUNCTIONS IN DATABASE <your_database_name> TO role purview_reader;
    GRANT USAGE ON ALL PROCEDURES IN DATABASE <your_database_name> TO role purview_reader;
    GRANT SELECT ON ALL TABLES IN DATABASE <your_database_name> TO role purview_reader;
    GRANT SELECT ON ALL VIEWS IN DATABASE <your_database_name> TO role purview_reader;
    GRANT USAGE, READ on ALL STAGES IN DATABASE <your_database_name> TO role purview_reader;
    
    --grant reader access to any future objects that could be created
    GRANT USAGE ON FUTURE SCHEMAS IN DATABASE <your_database_name> TO role purview_reader;
    GRANT USAGE ON FUTURE FUNCTIONS IN DATABASE <your_database_name> TO role purview_reader;
    GRANT USAGE ON FUTURE PROCEDURES IN DATABASE <your_database_name> TO role purview_reader;
    GRANT SELECT ON FUTURE TABLES IN DATABASE <your_database_name> TO role purview_reader;
    GRANT SELECT ON FUTURE VIEWS IN DATABASE <your_database_name> TO role purview_reader;
    GRANT USAGE, READ ON FUTURE STAGES IN DATABASE <your_database_name> TO role purview_reader;
    ```

## Register

This section describes how to register Snowflake in Microsoft Purview using the classic [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Steps to register

To register a new Snowflake source in Microsoft Purview Unified Catalog, follow these steps:

1. Navigate to your Microsoft Purview account in the classic [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Select **Data Map** on the left navigation.
3. Select **Register.**
4. On Register sources, select **Snowflake**. Select **Continue**.

On the **Register sources (Snowflake)** screen, follow these steps:

1. Enter a **Name** that the data source will be listed within the Catalog.
2. Enter the **server** URL in the form of `<account_identifier>.snowflakecomputing.com`, for example, `orgname-accountname.snowflakecomputing.com`. Learn more about Snowflake [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html#). Note this URL is used as part of the Snowflake assets' fully qualified name, and is the default endpoint for Microsoft Purview to connect to Snowflake during scan.
3. Add **additional hosts** if applicable. Specify it when you want the scan operations to connect to a Snowflake endpoint other than the server URL. You can choose the host for connection during scan setup.

    Tip

    If you already scanned Snowflake but want to switch to use another endpoint, for example, from public endpoint to private endpoint, you can add another host in data source and choose that host for connection in scan to ensure Microsoft Purview generate the assets with the same fully qualified name as previous.

    When registering a data source, Microsoft Purview performs uniqueness check that the server URL and other hosts doesn't overlap with any existing sources.
4. Select a collection from the list.
5. Finish to register the data source.

    ![Screenshot of the Register sources page for Snowflake in Microsoft Purview with fields for name, server URL, and collection.](media/register-scan-snowflake/register-sources.png)

## Scan

Follow these steps to scan Snowflake to automatically identify assets. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion).

### Authentication for a scan

The supported authentication types for a Snowflake source are **Basic authentication** and **Key Pair**.

Follow this process to configure a Key Pair credential.

**Prerequisites for Key Pair Authentication**

Before starting, ensure you have:

1. **Snowflake Access**

    1. Snowflake account with admin privileges
    2. User account for Microsoft Purview scanning (for example, purview\_scanner)
    3. Access to execute ALTER USER commands
2. **Tools & Software**

    1. OpenSSL installed (for key generation)
    2. Azure CLI or PowerShell (for Key Vault operations)
    3. Access to Microsoft Purview Portal
    4. Ensure you have Microsoft Open JDK 11. [Download Microsoft Open JDK 11](/en-us/java/openjdk/download). Other JDK variants might have issues with advanced encrypted algorithms.

**Step by Step Configuration**

**Part 1: Snowflake Configuration**

This step involves creating public and private keys and then assigning the public key to the purview user (‘purview\_scanner’ in below example) that connects to Snowflake to perform the scan.

**Step 1.1: Generate RSA Key Pair**

- Generate Private Key

Open a terminal and generate the private key:

```text
--For Encrypted Private Key (Recommended):  

openssl genrsa 2048 | openssl pkcs8 -topk8 -v2 aes-256-cbc -v2prf hmacWithSHA512 - inform PEM -out rsa_key.p8  

--Note: You'll be prompted to enter a passphrase. Remember this passphrase! 
```

OR

```text
--For Unencrypted Private Key:  

openssl genrsa 2048 | openssl pkcs8 -topk8 -v2 aes-256-cbc -v2prf hmacWithSHA512 - inform PEM -out rsa_key.p8 -nocrypt 
```

Note: Use the above commands to generate the key

- Generate Public Key

```text
openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub 
```

- Extract Public Key Content

View and copy the public key content (excluding headers):

```text
cat rsa_key.pub 
```

```text
-----BEGIN PUBLIC KEY----- 
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA... 
... -----END PUBLIC KEY----- 
```

Copy everything between the BEGIN and END lines (don't include the delimiter lines).

**Step 1.2: Assign Public Key to Snowflake User**

Connect to Snowflake and execute:

```sql
-- Create user if it doesn't exist 
CREATE USER IF NOT EXISTS purview_scanner 
  DEFAULT_ROLE = 'PUVRIEW_READER' 
  TYPE = 'SERVICE'  ; 
 -- Assign the public key (paste your key without the BEGIN/END lines) 
ALTER USER purview_scanner  
SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...'; 
 -- Grant necessary privileges 
GRANT ROLE purview_reader TO USER purview_scanner; 
 -- Verify the fingerprint 
DESC USER purview_scanner; 

```

**Step 1.3: Verify Key Configuration [optional step to validate]**

Verify the public key fingerprint matches:

In Snowflake:

```sql
DESC USER purview_scanner ->> SELECT SUBSTR( 
(SELECT "value" FROM $1 
WHERE "property" = 'RSA_PUBLIC_KEY_FP'), 
LEN('SHA256:') + 1) AS key; 
```

In Command Line:

```text
openssl rsa -pubin -in rsa_key.pub -outform DER | openssl dgst -sha256 -binary | openssl 
enc -base64 
```

Note that both should produce the same fingerprint hash.

**Part 2: Azure Key Vault Setup**

**Step 2.1: Prepare Private Key Content**

View your private key:

```text
cat rsa_key.p8 
```

Copy the entire content including the <sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page> lines.

**Step 2.2: Store Secrets in Azure Key Vault**

You need to store TWO secrets in Azure Key Vault:

**Secret 1: Private Key**

**CRITICAL REQUIREMENT**: The private key **MUST be stored using Azure CLI or Azure Cloud Shell**.

**DO NOT use the Azure Portal UI** for creating the private key secret because:

- The Azure Portal text input doesn't preserve multi-line formatting
- It converts line breaks to spaces, corrupting the PEM format
- **Snowflake connections will FAIL** with malformed key errors

The password/passphrase secret CAN be created via Portal (single-line value).

**Method 1: Azure CLI (Recommended)**

```text
# Replace with your values 
KEY_VAULT_NAME="your-keyvault-name"
CREDENTIAL_NAME="snowflake-purview-cred" 

# Store the private key from file (preserves multi-line format) 
az keyvault secret set \
 --vault-name $KEY_VAULT_NAME \
 --name "${CREDENTIAL_NAME}-privateKey" \
 --file rsa_key.p8 
```

OR

**Method 2: Azure Cloud Shell**

1. Open Azure Cloud Shell (https://shell.azure.com)
2. Upload your rsa\_key.p8 file using the upload button (folder icon)
3. Run the command:

```text
az keyvault secret set \ 
  --vault-name your-keyvault-name \ 
  --name "snowflake-purview-cred-privateKey" \ 
  --file rsa_key.p8 
```

OR

**Method 3: PowerShell with Azure CLI**

```powershell
# Read the private key preserving line breaks 
$privateKeyContent = Get-Content -Path "rsa_key.p8" -Raw 
 
# Store in Key Vault using Azure CLI 
az keyvault secret set ` 
  --vault-name "your-keyvault-name" ` 
  --name "snowflake-purview-cred-privateKey" ` 
  --value $privateKeyContent 

```

OR

**Verify the Private Key Format After Upload: [optional step]**

```text
# Retrieve and check the secret maintains proper formatting 
az keyvault secret show \ 
  --vault-name $KEY_VAULT_NAME \ 
  --name "${CREDENTIAL_NAME}-privateKey" \ 
  --query value -o tsv 
 
# Expected output: Multiple lines like this 
# <sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>

```

Correct: Multiple lines with line breaks preserved

Incorrect: Single long line or text with spaces instead of newlines

**Secret 2: Private Key Passphrase**

The passphrase **can be created using either Azure Portal or Azure CLI** (it's a single-line value).

```text
# Store the passphrase (if your key is encrypted) 
az keyvault secret set \
 --vault-name $KEY_VAULT_NAME \
 --name "${CREDENTIAL_NAME}-password" \
 --value "your_passphrase_here" 
```

**Important:** If you used an **unencrypted** private key, you still need to create the .password secret, but set it to an empty string or a placeholder value.

Using Azure Portal:

1. Go to **Secrets → Generate/Import**
2. Name: snowflake-purview-cred.password
3. Value: Your passphrase (or empty string for unencrypted keys)
4. Select **Create**

### Create and run scan

To create and run a new scan, follow these steps:

1. In the classic [Microsoft Purview governance portal](https://web.purview.azure.com/), navigate to **Sources**.
2. Select the registered Snowflake source.
3. Select **+ New scan**.
4. Provide the following details:

    1. **Name**: The name of the scan
    2. **Connect via integration runtime**: Select the Azure autoresolved integration runtime, Managed Virtual Network IR or SHIR according to your scenario. Learn more from [Choose the right integration runtime configuration for your scenario](data-map-integration-runtime-choose). To use Managed Virtual Network IR to connect to Snowflake via private link, follow the steps in Connect to Snowflake via Managed Private Endpoint to set up the private endpoint first.
    3. **Host for connection**: Choose the endpoint used to establish connection to Snowflake during scan. You can choose from the server URL or the other hosts that you configured in Register.
    4. **Credential**: Select the credential to connect to your data source.

        If using **Basic Authentication** while creating a credential.

        - Provide the user name used to connect to Snowflake in the User name input field.
        - Store the user password used to connect to Snowflake in the secret key.

        If using **Key Pair** while creating a credential

        - Provide User name: purview\_scanner (your Snowflake user)
        - Password Key Vault Reference:

        - Key Vault Connection: Select your Key Vault
        - Secret Name: snowflake-purview-cred.password

        - Private Key Vault Reference:

        - Key Vault Connection: Select your Key Vault
        - Secret Name: snowflake-purview-cred.privateKey
    5. **Warehouse**: Specify the name of the warehouse instance used to empower scan in uppercase. The default role assigned to the user specified in the credential must have USAGE rights on this warehouse.
    6. **Databases**: Specify one or more database instance names to import in uppercase. Separate the names in the list with a semi-colon (;). For example, `DB1;DB2`. The default role assigned to the user specified in the credential must have adequate rights on the database objects.

        Note

        Classification is not applied to tables when more than one database instance names are specified.

        Acceptable database name patterns can be static names or contain wildcard %. For example: `A%;%B;%C%;D`:

        - Start with A or
        - End with B or
        - Contain C or
        - Equal D
    7. **Schema**: List subset of schemas to import expressed as a semicolon separated list. For example, `schema1;schema2`. All user schemas are imported if that list is empty. All system schemas and objects are ignored by default.

        Acceptable schema name patterns using can be static names or contain wildcard %. For example: `A%;%B;%C%;D`:

        - Start with A or
        - End with B or
        - Contain C or
        - Equal D

        Usage of NOT and special characters aren't acceptable.
    8. **Stored procedure details**: Controls the number of details imported from stored procedures:

        - Signature (default): The name and parameters of stored procedures.
        - Code, signature: The name, parameters, and code of stored procedures.
        - Lineage, code, signature: The name, parameters and code of stored procedures, and the data lineage derived from the code.
        - None: Stored procedure details aren't included.

        Note

        If you use Self-hosted Integration Runtime for scan, customized setting other than the default Signature is supported since version 5.30.8541.1. The earlier versions always extract the name and parameters of stored procedures.
    9. **Maximum memory available** (applicable when using self-hosted integration runtime): Maximum memory (in GB) available on customer's VM to be used by scanning processes. It's dependent on the size of Snowflake source to be scanned.

        Note

        As a rule of thumb, provide 1GB memory for every 1000 tables.
5. Select **Test connection** to validate the settings (available when using Azure Integration Runtime).
6. Select **Continue**.
7. Select a **scan rule set** for classification. You can choose between the system default, existing custom rule sets, or [create a new rule set](data-map-scan-rule-set) inline. For more information, see [Apply classifications automatically in Microsoft Purview](data-map-classification-apply-auto).

    Note

    Classification won't be applied to tables or views when the table name, view name, schema name, or database name contain special characters.

    Note

    If you're using self-hosted runtime, you need to upgrade to version 5.26.404.1 or higher to use Snowflake classification. [Download the latest Microsoft Integration Runtime](https://go.microsoft.com/fwlink/?linkid=2246619).
8. Choose your **scan trigger**. You can set up a schedule or ran the scan once.
9. Review your scan and select **Save and Run**.

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

## Lineage

After scanning your Snowflake source, you can [browse Unified Catalog](unified-catalog-data-assets-search#browse-the-unified-catalog) or [search Unified Catalog](unified-catalog-data-assets-search) to view the asset details.

Go to the asset -&gt; lineage tab, you can see the asset relationship when applicable. Refer to the supported capabilities section on the supported Snowflake lineage scenarios. For more information about lineage in general, see [data lineage](data-gov-classic-lineage) and [lineage user guide](data-gov-classic-lineage-user-guide).

![Snowflake lineage view](media/register-scan-snowflake/lineage.png)

Note

If a view was created by tables from different databases or different schemas, scan all databases and schemas simultaneously using the names in the semicolon (;) list.

## Connect to Snowflake via Managed Private Endpoint

This section describes the required steps to set up a Managed Private Endpoint (PE) from Microsoft Purview to Snowflake on Azure. Learn more about [Azure Private Link and Snowflake](https://docs.snowflake.com/en/user-guide/privatelink-azure).

1. In your Snowflake account, retrieve the target endpoints and resource ID. Run the system function [SYSTEM$GET_PRIVATELINK_CONFIG()](https://docs.snowflake.com/en/sql-reference/functions/system_get_privatelink_config) with Account Admin role, and note down the values of the following properties:

    - privatelink-pls-id
    - privatelink-account-url
    - regionless-privatelink-account-url
    - privatelink\_ocsp-url

    ```sql
    use role accountadmin; 
    select key, value::varchar from table(flatten(input=>parse_json(SYSTEM$GET_PRIVATELINK_CONFIG())));
    ```
2. In Microsoft Purview, create a managed private endpoint to Snowflake.

    1. Follow the steps to [Create a Managed Virtual Network Integration Runtime](data-governance-private-endpoints-managed-virtual-network#create-managed-virtual-network-integration-runtime). If you already have one, make sure it's in version 2, which supports Snowflake PE.
    2. Create a managed private endpoint for Snowflake. Navigate to **Managed private endpoint** -&gt; **+ New** -&gt; **Snowflake**, and fill in the following information.
        - **Resource ID or alias**: Fill in the value of **privatelink-pls-id** you retrieved.
        - **Fully qualified domain names**: Add the **privatelink\_ocsp-url**, **regionless-privatelink-account-url** and **privatelink-account-url**.

    ![Screenshot of the managed private endpoint creation page for Snowflake in Microsoft Purview.](media/register-scan-snowflake/snowflake-managed-pe.png)
3. After creating the PE, you can see its provisioning state as **Succeeded** and approval state as **Pending**. Open the PE and find the **Managed private endpoint resource ID** in details page.
4. [Contact Snowflake Technical Support](https://community.snowflake.com/s/#SUPPORT) and provide the resource ID to let Snowflake approve this PE.
5. Once Snowflake Support confirms the PE is approved, you should see your managed private endpoint approval state as **Approved** in Microsoft Purview.
6. Register the data source and set up a scan. When setting up scan, choose the Managed Virtual Network IR associated with the Snowflake PE.

## Troubleshooting tips

If you encounter issues while registering or scanning Snowflake, review the following tips.

- Check your account identifier in the source registration step. Don't include `https://` at the beginning.
- Make sure the warehouse name and database name are in uppercase on the scan setup page.
- Check your key vault. Make sure there are no typos in the password.
- Check the credential you set up in Microsoft Purview. The user you specify must have a default role with the necessary access rights to both the warehouse and the database you're trying to scan. See Required permissions for scan. USE `DESCRIBE USER;` to verify the default role of the user you specified for Microsoft Purview.
- Use Query History in Snowflake to see if any activity is coming across.
    - If there's a problem with the account identifier or password, you won't see any activity.
    - If there's a problem with the default role, you should at least see a `USE WAREHOUSE . . .` statement.
    - You can use the [QUERY_HISTORY_BY_USER table function](https://docs.snowflake.com/en/sql-reference/functions/query_history.html) to identify what role is being used by the connection. Setting up a dedicated Microsoft Purview user makes troubleshooting easier.

## Troubleshooting for Key Pair authentication

This section covers common connection issues when using Snowflake key pair authentication in Microsoft Purview.

**Issue 1: "Test Connection Failed"**

**Symptoms**: Connection test fails in Purview

**Possible causes and solutions:**

1. **Public Key Not Assigned**

    1. Verify in Snowflake: DESC USER purview\_scanner;
    2. Check RSA\_PUBLIC\_KEY\_FP is populated
2. **Key Vault Access Issues**

    1. Verify Managed Identity has Get and List permissions
    2. Check Key Vault firewall settings
3. **Incorrect Secret Names**

    1. Verify: {credentialName}.password exists
    2. Verify: {credentialName}.privateKey exists

**Issue 2: "Invalid Private Key Format" or "Connection Failed with Key Error"**

**Symptoms:**

- Authentication fails with "invalid private key format" error
- Connection test fails immediately
- Error messages about malformed PEM or key parsing errors

**Common cause:** Private key was stored via Azure Portal (corrupted multi-line format)

**Solution:**

1. Verify if the key format is corrupted:

    ```text
    # Retrieve the secret and check format 
    az keyvault secret show \
     --vault-name your-keyvault \
     --name "snowflake-purview-cred-privateKey" \
     --query value -o tsv | head -5 
    
    # Should show multiple lines starting with: 
    # <sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page> lines
    3. Verify key locally first:

    ```text
    openssl rsa -in rsa_key.p8 -check
    ```

**Remember**: Always use Azure CLI or Cloud Shell for private key secrets, NEVER the Azure Portal UI.

**Issue 3: "Public Key Fingerprint Mismatch"**

**Symptom**: Authentication succeeds but wrong key is being used

**Solution:**

```text
# Regenerate public key from private key 
openssl rsa -in rsa_key.p8 -pubout -out rsa_key_new.pub 

# Verify fingerprint 
openssl rsa -pubin -in rsa_key_new.pub -outform DER | openssl dgst sha256 -binary | openssl enc -base64 

# Update in Snowflake 
ALTER USER purview_scanner SET RSA_PUBLIC_KEY='';
```

**Issue 4: "Passphrase Incorrect"**

**Symptom:** Key decryption fails

**Solution**:

1. Verify passphrase in Key Vault matches the one used during key generation
2. Test passphrase locally:

```text
openssl rsa -in rsa_key.p8 -check 
# Enter passphrase when prompted
```

**Issue 5: "Missing Snowflake Permissions"**

**Symptom**: Connection succeeds but scan fails

**Solution**:

Grant required privileges to the Snowflake user:

```sql
-- Create role for Purview 
CREATE ROLE IF NOT EXISTS purview_reader; 

-- Grant usage on warehouse 
GRANT USAGE ON WAREHOUSE COMPUTE_WH TO ROLE purview_reader; 

-- Grant usage on database  
GRANT USAGE ON DATABASE my_database TO ROLE purview_reader; 

-- Grant usage on all schemas  
GRANT USAGE ON ALL SCHEMAS IN DATABASE my_database TO ROLE  purview_reader; 

-- Grant select on all tables  
GRANT SELECT ON ALL TABLES IN DATABASE my_database TO ROLE  purview_reader;  
GRANT SELECT ON FUTURE TABLES IN DATABASE my_database TO ROLE  purview_reader; 

-- Grant select on all views  
GRANT SELECT ON ALL VIEWS IN DATABASE my_database TO ROLE  purview_reader;  
GRANT SELECT ON FUTURE VIEWS IN DATABASE my_database TO ROLE  purview_reader; 

-- Assign role to user  
GRANT ROLE purview_reader TO USER purview_scanner; 

-- Set as default role  
ALTER USER purview_scanner SET DEFAULT_ROLE = purview_reader;

```