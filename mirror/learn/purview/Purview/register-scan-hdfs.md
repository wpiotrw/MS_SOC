---
layout: Conceptual
title: Connect to and manage HDFS | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-hdfs
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This guide describes how to connect to HDFS in Microsoft Purview, and use Microsoft Purview's features to scan and manage your HDFS source.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: jingwang
ms.service: purview
ms.subservice: purview-data-map
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: template-how-to, msecd-doc-authoring-1030
locale: en-us
document_id: 94aa1d86-8fdf-d7e0-6af7-a1277a84a86c
document_version_independent_id: 94aa1d86-8fdf-d7e0-6af7-a1277a84a86c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-hdfs.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-hdfs
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-hdfs.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 597e7257-0b6e-bad0-8a7d-415a76242252
---

# Connect to and manage HDFS | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article outlines how to register Hadoop Distributed File System (HDFS), and how to authenticate and interact with HDFS in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | Yes | Yes |

When scanning HDFS source, Microsoft Purview supports extracting technical metadata including HDFS:

- Namenode
- Folders
- Files
- Resource sets

When setting up scan, you can choose to scan the entire HDFS or selective folders. Learn about the supported file format [here](data-map-data-sources#file-types-supported-for-scanning).

The connector uses *webhdfs* protocol to connect to HDFS and retrieve metadata. MapR Hadoop distribution is not supported.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You need Data Source Administrator and Data Reader permissions to register a source and manage it in the Microsoft Purview governance portal. For more information about permissions, see [Access control in Microsoft Purview](data-gov-classic-permissions).
- [Set up the right integration runtime for your scenario](data-map-integration-runtime-choose):
    - **To use a self-hosted integration runtime:**
        - [Follow the article to create and configure a self-hosted integration runtime](data-map-integration-runtime-self-hosted).
        - Ensure [JDK 11](https://www.oracle.com/java/technologies/downloads/#java11) is installed on the machine where the self-hosted integration runtime is installed. Restart the machine after you newly install the JDK for it to take effect.
        - Ensure that Visual C++ Redistributable (version Visual Studio 2012 Update 4 or newer) is installed on the machine where the self-hosted integration runtime is running. If you don't have this update installed, [download it now](/en-us/cpp/windows/latest-supported-vc-redist).
        - To set up your environment to enable Kerberos authentication, see the Use Kerberos authentication for the HDFS connector section.
    - **To use a kubernetes supported self-hosted integration runtime:**
        - [Follow the article to create and configure a kubernetes supported integration runtime](data-map-integration-runtime-kubernetes).
        - To set up your environment to enable Kerberos authentication, see the Use Kerberos authentication for the HDFS connector section.

## Register

This section describes how to register HDFS in Microsoft Purview using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Steps to register

To register a new HDFS source in Microsoft Purview Unified Catalog, follow these steps:

1. Navigate to your Microsoft Purview account in the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Select **Data Map** on the left navigation.
3. Select **Register**
4. On Register sources, select **HDFS**. Select **Continue**.

On the **Register sources (HDFS)** screen, follow these steps:

1. Enter a **Name** that the data source will be listed within the Catalog.
2. Enter the **Cluster URL** of the HDFS NameNode in the form of `https://<namenode>:<port>` or `http://<namenode>:<port>`, e.g. `https://namenodeserver.com:50470` or `http://namenodeserver.com:50070`.
3. Select a collection from the list.
4. Finish to register the data source.

    ![Screenshot of HDFS source registration in Purview.](media/register-scan-hdfs/register-sources.png)

## Scan

Follow the steps below to scan HDFS to automatically identify assets. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion).

### Authentication for a scan

The supported authentication type for an HDFS source is **Kerberos authentication**.

### Create and run scan

To create and run a new scan, follow these steps:

1. Make sure a self-hosted integration runtime is set up. If it isn't set up, use the steps mentioned in prerequisites to create a self-hosted integration runtime.
2. Navigate to **Sources**.
3. Select the registered HDFS source.
4. Select **+ New scan**.
5. On "**Scan *source\_name***"" page, provide the below details:

    1. **Name**: The name of the scan
    2. **Connect via integration runtime**: Select the configured self-hosted integration runtime. See setup requirements in Prerequisites section.
    3. **Credential**: Select the credential to connect to your data source. Make sure to:

        - Select **Kerberos Authentication** while creating a credential.
        - Provide the user name in the format of `<username>@<domain>.com` in the User name input field. Learn more from Use Kerberos authentication for the HDFS connector.
        - Store the user password used to connect to HDFS in the secret key.

        ![Screenshot of HDFS scan configurations in Purview.](media/register-scan-hdfs/scan.png)
6. Select **Test connection**.
7. Select **Continue**.
8. On "**Scope your scan**" page, select the path(s) that you want to scan.
9. On "**Select a scan rule set**" page, select the scan rule set you want to use for schema extraction and classification. You can choose between the system default, existing custom rule sets, or create a new rule set inline. Learn more from [Create a scan rule set](data-map-scan-rule-set).
10. On "**Set a scan trigger**" page, choose your **scan trigger**. You can set up a schedule or ran the scan once.
11. Review your scan and select **Save and Run**.

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

## Use Kerberos authentication for the HDFS connector

There are two options for setting up the on-premises environment to use Kerberos authentication for the HDFS connector. You can choose the one that better fits your situation.

- Option 1: Join a self-hosted integration runtime machine in the Kerberos realm
- Option 2: Enable mutual trust between the Windows domain and the Kerberos realm

For either option, make sure you turn on webhdfs for Hadoop cluster:

1. Create the HTTP principal and keytab for webhdfs.

    Important

    The HTTP Kerberos principal must start with "**HTTP/**" according to Kerberos HTTP SPNEGO specification. Learn more from [here](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/WebHDFS.html#HDFS_Configuration_Options).

    ```bash
    Kadmin> addprinc -randkey HTTP/<namenode hostname>@<REALM.COM>
    Kadmin> ktadd -k /etc/security/keytab/spnego.service.keytab HTTP/<namenode hostname>@<REALM.COM>
    ```
2. HDFS configuration options: add the following three properties in `hdfs-site.xml`.

    ```xml
    <property>
        <name>dfs.webhdfs.enabled</name>
        <value>true</value>
    </property>
    <property>
        <name>dfs.web.authentication.kerberos.principal</name>
        <value>HTTP/_HOST@<REALM.COM></value>
    </property>
    <property>
        <name>dfs.web.authentication.kerberos.keytab</name>
        <value>/etc/security/keytab/spnego.service.keytab</value>
    </property>
    ```

### Option 1: Join a self-hosted integration runtime machine in the Kerberos realm

#### Requirements

- The self-hosted integration runtime machine needs to join the Kerberos realm and can’t join any Windows domain.

#### How to configure

**On the KDC server:**

Create a principal, and specify the password.

Important

The username should not contain the hostname.

```bash
Kadmin> addprinc <username>@<REALM.COM>
```

**On the self-hosted integration runtime machine:**

1. Run the Ksetup utility to configure the Kerberos Key Distribution Center (KDC) server and realm.

    The machine must be configured as a member of a workgroup, because a Kerberos realm is different from a Windows domain. You can achieve this configuration by setting the Kerberos realm and adding a KDC server by running the following commands. Replace *REALM.COM* with your own realm name.

    ```cmd
    C:> Ksetup /setdomain REALM.COM
    C:> Ksetup /addkdc REALM.COM <your_kdc_server_address>
    ```

    After you run these commands, restart the machine.
2. Verify the configuration with the `Ksetup` command. The output should be like:

    ```cmd
    C:> Ksetup
    default realm = REALM.COM (external)
    REALM.com:
        kdc = <your_kdc_server_address>
    ```

**In your Purview account:**

- Configure a credential with Kerberos authentication type with your Kerberos principal name and password to scan the HDFS. For configuration details, check the credential setting part in Scan section.

### Option 2: Enable mutual trust between the Windows domain and the Kerberos realm

#### Requirements

- The self-hosted integration runtime machine must join a Windows domain.
- You need permission to update the domain controller's settings.

#### How to configure

Note

Replace REALM.COM and AD.COM in the following tutorial with your own realm name and domain controller.

**On the KDC server:**

1. Edit the KDC configuration in the *krb5.conf* file to let KDC trust the Windows domain by referring to the following configuration template. By default, the configuration is located at */etc/krb5.conf*.

    ```config
    [logging]
     default = FILE:/var/log/krb5libs.log
     kdc = FILE:/var/log/krb5kdc.log
     admin_server = FILE:/var/log/kadmind.log
    
    [libdefaults]
     default_realm = REALM.COM
     dns_lookup_realm = false
     dns_lookup_kdc = false
     ticket_lifetime = 24h
     renew_lifetime = 7d
     forwardable = true
    
    [realms]
     REALM.COM = {
      kdc = node.REALM.COM
      admin_server = node.REALM.COM
     }
    AD.COM = {
     kdc = windc.ad.com
     admin_server = windc.ad.com
    }
    
    [domain_realm]
     .REALM.COM = REALM.COM
     REALM.COM = REALM.COM
     .ad.com = AD.COM
     ad.com = AD.COM
    
    [capaths]
     AD.COM = {
      REALM.COM = .
     }
    ```

    After you configure the file, restart the KDC service.
2. Prepare a principal named *krbtgt/REALM.COM@AD.COM* in the KDC server with the following command:

    ```cmd
    Kadmin> addprinc krbtgt/REALM.COM@AD.COM
    ```
3. In the *hadoop.security.auth\_to\_local* HDFS service configuration file, add `RULE:[1:$1@$0](.*\@AD.COM)s/\@.*//`.

**On the domain controller:**

1. Run the following `Ksetup` commands to add a realm entry:

    ```cmd
    C:> Ksetup /addkdc REALM.COM <your_kdc_server_address>
    C:> ksetup /addhosttorealmmap HDFS-service-FQDN REALM.COM
    ```
2. Establish trust from the Windows domain to the Kerberos realm. [password] is the password for the principal *krbtgt/REALM.COM@AD.COM*.

    ```cmd
    C:> netdom trust REALM.COM /Domain: AD.COM /add /realm /password:[password]
    ```
3. Select the encryption algorithm that's used in Kerberos.

    1. Select **Server Manager** &gt; **Group Policy Management** &gt; **Domain** &gt; **Group Policy Objects** &gt; **Default or Active Domain Policy**, and then select **Edit**.
    2. On the **Group Policy Management Editor** pane, select **Computer Configuration** &gt; **Policies** &gt; **Windows Settings** &gt; **Security Settings** &gt; **Local Policies** &gt; **Security Options**, and then configure **Network security: Configure Encryption types allowed for Kerberos**.
    3. Select the encryption algorithm you want to use when you connect to the KDC server. You can select all the options.

        ![Screenshot of the Network security: Configure encryption types allowed for Kerberos pane.](media/register-scan-hdfs/config-encryption-types-for-kerberos.png)
    4. Use the `Ksetup` command to specify the encryption algorithm to be used on the specified realm.

        ```cmd
        C:> ksetup /SetEncTypeAttr REALM.COM DES-CBC-CRC DES-CBC-MD5 RC4-HMAC-MD5 AES128-CTS-HMAC-SHA1-96 AES256-CTS-HMAC-SHA1-96
        ```
4. Create the mapping between the domain account and the Kerberos principal, so that you can use the Kerberos principal in the Windows domain.

    1. Select **Administrative tools** &gt; **Active Directory Users and Computers**.
    2. Configure advanced features by selecting **View** &gt; **Advanced Features**.
    3. On the **Advanced Features** pane, right-click the account to which you want to create mappings and, on the **Name Mappings** pane, select the **Kerberos Names** tab.
    4. Add a principal from the realm.

        ![Screenshot of the Security Identity Mapping pane.](media/register-scan-hdfs/map-security-identity.png)

**On the self-hosted integration runtime machine:**

- Run the following `Ksetup` commands to add a realm entry.

    ```cmd
    C:> Ksetup /addkdc REALM.COM <your_kdc_server_address>
    C:> ksetup /addhosttorealmmap HDFS-service-FQDN REALM.COM
    ```

**In your Purview account:**

- Configure a credential with Kerberos authentication type with your Kerberos principal name and password to scan the HDFS. For configuration details, check the credential setting part in Scan section.

## Known limitations

Currently, HDFS connector doesn't support custom resource set pattern rule for [advanced resource set](data-map-resource-sets#advanced-resource-sets), the built-in resource set patterns will be applied.

[Sensitivity label](data-map-sensitivity-labels) is not yet supported.