---
layout: Conceptual
title: Connect to and manage an SAP Business Warehouse with Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-sap-bw
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: pragyarathi
ms.date: 2026-04-27T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to connect to SAP Business Warehouse in Microsoft Purview, and use Microsoft Purview's features to scan and manage your SAP BW source.
locale: en-us
document_id: 30532284-437f-d8a6-b231-d2f00767b361
document_version_independent_id: 30532284-437f-d8a6-b231-d2f00767b361
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-sap-bw.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-sap-bw
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-sap-bw.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: aa1dd554-c186-d558-1810-0ce4f28324b5
---

# Connect to and manage an SAP Business Warehouse with Microsoft Purview | Microsoft Learn

This article outlines how to register SAP Business Warehouse (BW), and how to authenticate and interact with SAP BW in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | No |

Purview supports SAP BW versions 7.3 to 7.5, and SAP BW/4HANA.

When you scan an SAP BW source, Microsoft Purview extracts technical metadata, including:

- Instance
- InfoArea
- InfoSet
- InfoSet query
- Classic InfoSet
- InfoObject, including unit of measurement, time characteristic, navigation attribute, data packet characteristic, currency, characteristic, field, and key figure
- Data store object (DSO), including its schema of InfoObject attributes and primary keys
- Advanced data store object (ADSO), including its schema of InfoObject attributes and primary keys
- Aggregation level
- Open hub destination
- Query, including the query condition
- Query view
- HybridProvider
- MultiProvider
- InfoCube
- Aggregate
- Dimension
- Time dimension

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Known limitations

- When you delete an object from the data source, the subsequent scan doesn't automatically remove the corresponding asset in Purview.
- You can extract only the `sap_bw_query_condition` under the `sap_bw_query`.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview resource](create-microsoft-purview-portal).
- You need Data Source Administrator and Data Reader permissions to register a source and manage it in the classic Microsoft Purview governance portal. For more information about permissions, see [Access control in Microsoft Purview](data-gov-classic-permissions).
- When you create a scan for the first time, you need to create a function module in your SAP server. Microsoft Purview provides some code in the asset page in the Microsoft Purview Data Map to create the module. To download this code, you need to have Data Source Administrator permissions on the root collection in your data map.
- [Set up the right integration runtime for your scenario](data-map-integration-runtime-choose):

    - **To use a self-hosted integration runtime:**
        - [Follow the article to create and configure a self-hosted integration runtime](data-map-integration-runtime-self-hosted).
        - Ensure [JDK 11](https://www.oracle.com/java/technologies/downloads/#java11) is installed on the machine where the self-hosted integration runtime is installed. Restart the machine after you newly install the JDK for it to take effect.
        - Ensure that Visual C++ Redistributable (version Visual Studio 2012 Update 4 or newer) is installed on the machine where the self-hosted integration runtime is running. If you don't have this update installed, [download it now](/en-us/cpp/windows/latest-supported-vc-redist).
        - The connector reads metadata from SAP using the [SAP Java Connector (JCo)](https://support.sap.com/en/product/connectors/jco.html) 3.0 API. Make sure the Java Connector is available on your machine where self-hosted integration runtime is installed. Make sure that you use the correct JCo distribution for your environment, and the **sapjco3.jar** and **sapjco3.dll** files are available.
    - **To use a kubernetes supported self-hosted integration runtime:**
        - [Follow the article to create and configure a kubernetes supported integration runtime](data-map-integration-runtime-kubernetes).
        - The connector reads metadata from SAP using the [SAP Java Connector (JCo)](https://support.sap.com/en/product/connectors/jco.html) 3.0 API. Make sure the Java Connector is available on your machine where self-hosted integration runtime is installed. Make sure that you use the correct JCo distribution for your environment, and the **sapjco3.jar** and **sapjco3.dll** files are available.

    Note

    The driver should be accessible to all accounts in the machine. Don't put it in a path under user account.

    - Self-hosted integration runtimes communicate with the SAP server over dispatcher port 32NN and gateway port 33NN, where NN is your SAP instance number from 00 to 99. Make sure the outbound traffic is allowed on your firewall.
- Deploy the metadata extraction ABAP function module on the SAP server by following the steps mentioned in [ABAP functions deployment guide](abap-functions-deployment-guide). You need to download a separate ABAP module for SAP BW/4 HANA version from the scan page. You need an ABAP developer account to create the RFC function module on the SAP server. For scan execution, the user account requires sufficient permissions to connect to the SAP server and execute the following RFC function modules:
- STFC\_CONNECTION (check connectivity)

    - RFC\_SYSTEM\_INFO (check system information)
    - OCS\_GET\_INSTALLED\_COMPS (check software versions)
    - Z\_MITI\_BW\_DOWNLOAD (main metadata import, the function module you create following the Purview guide)

    The underlying SAP Java Connector (JCo) libraries might call more RFC function modules, such as. RFC\_PING, RFC\_METADATA\_GET. Refer to [SAP support note 460089](https://launchpad.support.sap.com/#/notes/460089) for details.

## Register

This section describes how to register SAP BW in Microsoft Purview using the classic [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Authentication for registration

The only supported authentication method for an SAP BW source is **Basic authentication**.

### Steps to register

1. Open the classic Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Selecting the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Select **Data Map** on the left navigation.
3. Select **Register**.
4. In **Register sources**, select **SAP BW** &gt; **Continue**.

On the **Register sources (SAP BW)** screen, complete the following steps:

1. Enter a **Name** for the data source to list it within the catalog.
2. Enter the **Application server** name to connect to the SAP BW source. You can also enter an IP address for the SAP application server host.
3. Enter the SAP **System number**. It's an integer between 0 and 99.
4. Select a collection from the list.
5. Finish the registration of the data source.

    ![Screenshot of registering an SAP BW source.](media/register-scan-sap-bw/register-sap-bw.png)

## Scan

Follow the steps in this section to scan SAP BW and automatically identify assets. For more information about scanning, see [introduction to scans and ingestion](data-map-scan-ingestion).

Important

When you create a scan for the first time, you need to create a function module in your SAP server. Microsoft Purview provides some code in the asset page in the Microsoft Purview Data Map to create the module. To download this code, you need to have Data Source Administrator permissions on the root collection in your data map.

### Create and run scan

1. In the Management Center, select **Integration runtimes**. Make sure you set up a self-hosted integration runtime. If you don't have a self-hosted integration runtime, use the steps mentioned in prerequisites to create one.
2. Go to **Sources**.
3. Select the registered SAP BW source.
4. Select **New scan**.
5. Enter the following details:

    1. **Name**: The name of the scan.
    2. **Connect via integration runtime**: Select the configured self-hosted integration runtime.
    3. **Credential**: Select the credential to connect to your data source. Make sure to:

        - Select Basic Authentication while creating a credential.
        - Provide a user ID to connect to SAP server in the User name input field.
        - Store the user password used to connect to SAP server in the secret key.
    4. **Client ID**: Enter the SAP Client ID. It's a three-digit numeric number from 000 to 999.
    5. **SNC Mode (Optional)**: Turn the toggle **on** if you prefer to use Secure Network Communications (SNC) mode for securing your technical connections to SAP RFCs through a certificate-based authentication mechanism. SNC Mode is **off** by default. Follow the steps to set up the SAP personal secure environment with SNC certificate.
    6. **JCo library path**: Specify the directory path where the JCo libraries are located, for example: `D:\Drivers\SAPJCo`. Make sure the path is accessible by the self-hosted integration runtime, learn more from prerequisites section.

        - For self-hosted integration runtime on a local machine: `D:\Drivers\SAPJCo`. It's the path to a valid JAR folder location. The value must be a valid absolute file path and doesn't contain space. Make sure the driver is accessible by the self-hosted integration runtime. To learn more, see the prerequisites section.
        - For Kubernetes-supported self-hosted integration runtime: `./drivers/SAPJCo`. It's the path to a valid JAR folder location. The value must be a valid relative file path. Refer to the documentation to [set up a scan with external drivers](data-map-integration-runtime-kubernetes#set-up-a-scan-with-external-drivers) for uploading drivers in advance.
    7. **Maximum memory available:** Maximum memory (in GB) available on the self-hosted integration runtime machine to be used by scanning processes. This value depends on the size of SAP BW source to be scanned.![Screenshot of setting up an SAP BW scan.](media/register-scan-sap-bw/scan-sap-bw.png)
6. Select **Test connection**.
7. Select **Continue**.
8. Choose your **scan trigger**. You can set up a schedule or run the scan once.
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

### Set up SAP personal secure environment with SNC certificate

#### Get SAPCAR

- Go to the SAP Software Download Center and sign in with your SAP credentials.
- Search for SAPCAR and select the latest nonarchived version.
- Select your operating system.
- Download the `.EXE file to C:\sap\SAR`.

#### Get SAP Common Crypto Library

- In the SAP Software Download Center, search for "COMMONCRYPTOLIB" and select the latest version.
- Select your operating system.
- Download the .SAR file with the most recent release date to `C:\sap\SAR`.

#### Extract SAP Common Crypto Library

- Open PowerShell and go to `C:\sap\SAR`.
- Enter the following command, replacing xxxx with your values: `.\SAPCAR_xxxx.EXE -xvf .\SAPCRYPTOLIBP_xxxx.SAR -R .\..\libs\sapcryptolib`.
- Confirm that `sapgenpse.exe` is in the `C:\sap\libs\sapcryptolib` directory.

#### Generate certificates

Note

This method is for demonstration purposes only and isn't recommended for production systems. For production systems, consult your internal PKI guidance or security team.

- Set up the folder structure:

    - `mkdir rootCA`
    - `mkdir sncCert`
- Create the necessary serial and index files if they don't exist:

    - `if (-Not (Test-Path "rootCA\index.txt")) { New-Item -Path "rootCA\index.txt" ItemType File }`
    - `if (-Not (Test-Path "rootCA\serial")) { Set-Content -Path "rootCA\serial" -Value "01" }`
- Generate a Root CA:

    - `openssl genpkey -algorithm RSA -out rootCA/ca.key.pem -pkeyopt rsa_keygen_bits:2048`
    - `openssl req -x509 -new -key rootCA/ca.key.pem -days 7305 -sha256 -extensions v3_ca -out rootCA/ca.cert.pem -subj "/O=Contoso/CN=Root CA"`
- Generate the SNC certificate

    - `openssl genrsa -out sncCert/snc.key.pem 2048`
    - `openssl req -key sncCert/snc.key.pem -new -sha256 -out sncCert/snc.csr.pem subj "/O=Contoso/CN=SNC"`
- Create an OpenSSL configuration file, `sncCert/extensions.cnf`, for signing:

    - `subjectKeyIdentifier = hash`
    - `authorityKeyIdentifier = keyid,issuer`
    - `basicConstraints = critical,CA:false`
    - `keyUsage = critical,digitalSignature,keyEncipherment,dataEncipherment`
    - `extendedKeyUsage = clientAuth,emailProtection`
- Sign the SNC certificate with the Root CA:

    - `openssl x509 -req in sncCert/snc.csr.pem CA rootCA/ca.cert.pem CAkey rootCA/ca.key.pem CAcreateserial out sncCert/snc.cert.pem days 3650 sha256 extfile sncCert\extensions.cnf extensions v3_leaf`

#### Create a personal secure environment

Create a personal secure environment (PSE) for the on-premises data gateway. The NCo library looks for the SNC certificate inside the PSE.

- Create a PKCS#12 container:

    - `openssl pkcs12 -export -out snc.p12 -inkey sncCert\snc.key.pem -in sncCert\snc.cert.pem -certfile rootCA\ca.cert.pem`
- Create the SECUDIR environment variable.
- Open **System Properties**: In **File Explorer**, right-click **This PC**, and then select **Properties** &gt; **Advanced system settings**.
- Select **Environment Variables**.
- Under **System variables**, select **New**.
- Set the variable name to **SECUDIR**.
- Set the value to `C:\sapsecudir`.
- Select **OK**.

Import the PKCS#12 container into a PSE: `C:\sap\libs\sapcryptolib\sapgenpse.exe import_p12 -p SAPSNCSKERB.pse C:\pki certs\snc.p12`

#### Allow your SHIR process to use your SAP PSE

Verify which user or service is being used by your SNC client to obtain the certificate to communicate with SAP. The Microsoft Purview SHIR uses the service user **NT SERVICE\DIAHostService**.

- Add a credential to allow the certificate retrieval request from the PSE: `.\sapgenpse.exe seclogin -p C:\sapsecudir\SAPSNCSKERB.pse -x your-pse-pin -O "NT SERVICE\DIAHostService"`
- Verify credentials like this: `.\sapgenpse.exe seclogin -l -O "NT SERVICE\DIAHostService"`
- You can delete them like this: `.\sapgenpse.exe seclogin -d -O "NT SERVICE\DIAHostService"`
- Use the -h parameter to get help with the sapgenpse command line tool or check the command reference here.

#### Give permission to access the SAP JCo library to SHIR process

Verify if Microsoft Purview SHIR user **NT SERVICE\DIAHostService** has **Read/Write/Execute/List** permissions over these folders:

- SNC Library Path: The folder that has the SNC Library, `sapcrypto.dll`. Example: `C:\Users\shir-admin\Desktop\snc\SAPCRYPTOLIBP_8557-20011729\sapcrypto.dll`
- JCo Library Path: The folder that has the SAP Java Connector jar file. Example: `C:\Users\shir-admin\Desktop\snc\sapjco3-ntamd64-3.1\sapjco3-ntamd64-3.1.3`

SAP NCo Library should also be installed on the virtual machine for test connection to work properly, as it still uses NCo library. This isn't necessary, and Test Connection can be skipped.

Enter SCN details for **my name**, **partner name**, **library path**, and **quality of protection**, as seen below, and initiate the scan:

![User's image](media/register-scan-sap-bw/image.png)