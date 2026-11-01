---
layout: Conceptual
title: Troubleshoot the self-hosted integration runtime in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/scanning-shir-troubleshooting
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to troubleshoot self-hosted integration runtime issues in Microsoft Purview.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: arindamba
ms.service: purview
ms.subservice: purview-data-map
ms.custom: purview
ms.topic: troubleshooting
ms.date: 2023-09-26T00:00:00.0000000Z
locale: en-us
document_id: bb1c2c9d-c099-4948-b48e-2fdc6387291c
document_version_independent_id: bb1c2c9d-c099-4948-b48e-2fdc6387291c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/scanning-shir-troubleshooting.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: scanning-shir-troubleshooting
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/scanning-shir-troubleshooting.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/655f39c4-21c5-49d3-8367-a1f9c1a0b930
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/d30b39f7-a405-488d-84ef-d6d5296ad372
platformId: 24fb2fef-c19e-ee5e-edb7-d01736260f6e
---

# Troubleshoot the self-hosted integration runtime in Microsoft Purview | Microsoft Learn

This article explores common troubleshooting methods for self-hosted integration runtime (SHIR) in Microsoft Purview.

The self-hosted integration runtime (SHIR) is also used by Azure Data Factory and Azure Synapse Analytics. Though many of the troubleshooting steps overlap, follow this guide to troubleshoot your SHIR for those products:

- [Troubleshoot SHIR for Azure Data Factory and Azure Synapse Analytics](/en-us/azure/data-factory/self-hosted-integration-runtime-troubleshoot-guide)

## Gather Microsoft Purview specific SHIR self-hosted integration runtime logs

For failed Microsoft Purview scans that are running on a self-hosted IR, the service supports viewing and uploading error logs from the [Windows Event Viewer](/en-us/shows/inside/event-viewer).

You can look up any errors you see in the error guide below. To get support and troubleshooting guidance for SHIR issues, you may need to generate an error report ID and [reach out to Microsoft support](https://azure.microsoft.com/support/create-ticket/).

To generate the error report ID for Microsoft Support, follow these instructions:

1. Before starting a scan in the Microsoft Purview governance portal:

    1. Navigate to the machine where the self-hosted integration runtime is installed and open the Windows Event Viewer.
    2. Clear the windows event viewer logs in the **Integration Runtime** section. Right-click on the logs and select the clear logs option.
    3. Navigate back to the Microsoft Purview governance portal and start the scan.
2. Once the scan shows status **Failed**, navigate back to the SHIR VM, or machine and refresh the event viewer in the **Integration Runtime** section.
3. The activity logs are displayed for the failed scan run.
4. For further assistance from Microsoft, select **Send Logs**.

    The **Share the self-hosted integration runtime (SHIR) logs with Microsoft** window opens.

    [![Screenshot of the send logs button on the self-hosted integration runtime (SHIR) to upload logs to Microsoft.](media/scanning-shir-troubleshooting/shir-send-logs-ir.png)](media/scanning-shir-troubleshooting/shir-send-logs-ir.png#lightbox)
5. When the logs are uploaded, keep a record of the Report ID to use if you reach out to Microsoft support.

    [![Screenshot of the displayed report ID in the upload progress window for the Purview SHIR logs.](media/scanning-shir-troubleshooting/shir-send-logs-complete.png)](media/scanning-shir-troubleshooting/shir-send-logs-complete.png#lightbox)

## Self-hosted integration runtime SHIR general failure or error

There are lots of common errors, warnings, and issues between the Purview SHIR, Azure Data Factory, or Azure Synapse SHIR. The guide below covers many of the most common issues.

## Self-hosted IR general failure or error

### Out of memory issue

#### Symptoms

An OutOfMemoryException (OOM) error occurs when you try to run a scan with a self-hosted IR.

#### Cause

A new scan can throw an OOM error if the IR machine experiences momentary high memory usage. The issue might be caused by a large volume of concurrent activity or a low amount of memory and the error is by design.

#### Resolution

Check the resource usage to confirm if any other software is running at the same time, and confirm that your SHIR machine meets the [recommended configurations](data-map-integration-runtime-self-hosted#prerequisites).

### Self-hosted IR could not load file or assembly

#### Symptoms

You get the following error message:

"Could not load file or assembly 'XXXXXXXXXXXXXXXX, Version=4.0.2.0, Culture=neutral, PublicKeyToken=XXXXXXXXX' or one of its dependencies. The system cannot find the file specified. Activity ID: 92693b45-b4bf-4fc8-89da-2d3dc56f27c3"

Here is a more specific error message:

"Could not load file or assembly 'System.ValueTuple, Version=4.0.2.0, Culture=neutral, PublicKeyToken=XXXXXXXXX' or one of its dependencies. The system cannot find the file specified. Activity ID: 92693b45-b4bf-4fc8-89da-2d3dc56f27c3"

#### Cause

In Process Monitor, you can view the following result:

[![Screenshot of the Paths list in Process Monitor.](media/self-hosted-integration-runtime-troubleshoot-guide/process-monitor.png#lightbox)](media/self-hosted-integration-runtime-troubleshoot-guide/process-monitor.png#lightbox)

Tip

In Process Monitor, you can set filters as shown in following screenshot. The preceding error message says that the DLL System.ValueTuple is not located in the related *Global Assembly Cache* (GAC) folder, in the *C:\Program Files\Microsoft Integration Runtime\4.0\Gateway* folder, or in the *C:\Program Files\Microsoft Integration Runtime\4.0\Shared* folder. Basically, the process loads the DLL first from the *GAC* folder, then from the *Shared* folder, and finally from the *Gateway* folder. Therefore, you can load the DLL from any path that's helpful.

![Screenshot of the &amp;quot;Process Monitor Filter&amp;quot; page, listing the filters for the DLL.](media/self-hosted-integration-runtime-troubleshoot-guide/set-filters.png)

#### Resolution

You'll find the *System.ValueTuple.dll* file in the *C:\Program Files\Microsoft Integration Runtime\4.0\Gateway\DataScan* folder. To resolve the issue, copy the *System.ValueTuple.dll* file to the *C:\Program Files\Microsoft Integration Runtime\4.0\Gateway* folder.

You can use the same method to resolve other missing file or assembly issues.

#### More information

The reason why you see the *System.ValueTuple.dll* under *%windir%\Microsoft.NET\assembly* and *%windir%\assembly* is that this is a .NET behavior.

In the following error, you can clearly see that the *System.ValueTuple* assembly is missing. This issue arises when the application tries to check the *System.ValueTuple.dll* assembly.

> 
> "&lt;LogProperties&gt;&lt;ErrorInfo&gt;[{"Code":0,"Message":"The type initializer for 'Npgsql.PoolManager' threw an exception.","EventType":0,"Category":5,"Data":{},"MsgId":null,"ExceptionType":"System.TypeInitializationException","Source":"Npgsql","StackTrace":"","InnerEventInfos":[{"Code":0,"Message":"Could not load file or assembly 'System.ValueTuple, Version=4.0.2.0, Culture=neutral, PublicKeyToken=XXXXXXXXX' or one of its dependencies. The system cannot find the file specified.","EventType":0,"Category":5,"Data":{},"MsgId":null,"ExceptionType":"System.IO.FileNotFoundException","Source":"Npgsql","StackTrace":"","InnerEventInfos":[]}]}]&lt;/ErrorInfo&gt;&lt;/LogProperties&gt;"

For more information about GAC, see [Global Assembly Cache](/en-us/dotnet/framework/app-domains/gac).

### Self-hosted integration runtime Authentication Key is missing

#### Symptoms

The self-hosted integration runtime suddenly goes offline without an Authentication Key, and the Event Log displays the following error message:

"Authentication Key is not assigned yet"

![Screenshot of the integration runtime event pane showing that the Authentication Key is not yet assigned.](media/self-hosted-integration-runtime-troubleshoot-guide/key-missing.png)

#### Cause

The self-hosted IR node or logical self-hosted IR in the Microsoft Purview portal was deleted, or a clean uninstall was performed.

#### Resolution

If neither of the preceding causes applies, you can go to the *%programdata%\Microsoft\Data Transfer\DataManagementGateway* folder to see whether the *Configurations* file has been deleted. If it was deleted, follow the instructions in the Netwrix article [Detect who deleted a file from your Windows file servers](https://www.netwrix.com/how_to_detect_who_deleted_file.html).

![Screenshot of the event log details pane for checking the Configurations file.](media/self-hosted-integration-runtime-troubleshoot-guide/configurations-file.png)

### Can't choose the certificate because the private key is missing

#### Symptoms

- You've imported a PFX file to the certificate store.
- When you selected the certificate through the IR Configuration Manager UI, you received the following error message:

"Failed to change intranet communication encryption mode. It is likely that certificate '&lt;*certificate name*&gt;' might not have a private key that is capable of key exchange or the process might not have access rights for the private key. Please see inner exception for detail."

![Screenshot of the Integration Runtime Configuration Manager Settings pane, displaying a &amp;quot;private key missing&amp;quot; error message.](media/self-hosted-integration-runtime-troubleshoot-guide/private-key-missing.png)

#### Cause

- The user account has a low privilege level and can't access the private key.
- The certificate was generated as a signature but not as a key exchange.

#### Resolution

- To operate the UI, use an account with appropriate privileges for accessing the private key.
- Import the certificate by running the following command:

```
certutil -importpfx FILENAME.pfx AT_KEYEXCHANGE
```

### UserErrorJreNotFound error message when you run a scan

#### Symptoms

When you try to scan a data source using a Java-based tool or program (for example, Parquet format files), you receive an error message that resembles the following:

> 
> ErrorCode=UserErrorJreNotFound,'Type=Microsoft.DataTransfer.Common.Shared.HybridDeliveryException,Message=Java Runtime Environment is not found. Go to `http://go.microsoft.com/fwlink/?LinkId=808605` to download and install on your Integration Runtime (Self-hosted) node machine. Note 64-bit Integration Runtime requires 64-bit JRE and 32-bit Integration Runtime requires 32-bit JRE.,Source=Microsoft.DataTransfer.Common,''Type=System.DllNotFoundException,Message=Unable to load DLL 'jvm.dll': The specified module could not be found. (Exception from HRESULT: 0x8007007E),Source=Microsoft.DataTransfer.Richfile.HiveOrcBridge

#### Cause

This issue occurs for either of the following reasons:

- Java Runtime Environment (JRE) isn't installed correctly on your Integration Runtime server.
- Your Integration Runtime server lacks the required dependency for JRE.

By default, Integration Runtime resolves the JRE path by using registry entries. Those entries should be automatically set during JRE installation.

#### Resolution

Follow the steps in this section carefully. Serious problems might occur if you modify the registry incorrectly. Before you modify it, [back up the registry for restoration](https://support.microsoft.com/topic/how-to-back-up-and-restore-the-registry-in-windows-855140ad-e318-2a13-2829-d428a2ab0692) in case problems occur.

To fix this issue, follow these steps to verify the status of the JRE installation:

1. Make sure that Integration Runtime (Diahost.exe) and JRE are installed on the same platform. Check the following conditions:

    - 64-bit JRE for 64-bit ADF Integration Runtime should be installed in the folder: `C:\Program Files\Java\`

        Note

        The folder is not `C:\Program Files (x86)\Java\`
    - JRE 11 is compatible for scanning. JRE 8 is also compatible, but versions that are earlier than JRE 8 have not been validated for this use.
2. Check the registry for the appropriate settings. To do this, follow these steps:
3. In the **Run** menu, type **Regedit**, and then press Enter.
4. In the navigation pane, locate the following subkey:

    `HKEY_LOCAL_MACHINE\SOFTWARE\JavaSoft\Java Runtime Environment`.

    In the **Details** pane, there should be a Current Version entry that shows the JRE version (for example, 1.8).

    ![Screenshot showing the Java Runtime Environment.](media/self-hosted-integration-runtime-troubleshoot-guide/java-runtime-environment-image.png)
5. In the navigation pane, locate a subkey that is an exact match for the version (for example 1.8) under the JRE folder. In the details pane, there should be a **JavaHome** entry. The value of this entry is the JRE installation path.

    ![Screenshot showing a JavaHome entry.](media/self-hosted-integration-runtime-troubleshoot-guide/java-home-entry-image.png)
6. Locate the bin\server folder in the following path:

    `C:\Program Files\Java\jre1.xx.xxx`

    ![Screenshot showing the JRE folder.](media/self-hosted-integration-runtime-troubleshoot-guide/folder-of-jre.png)
7. Check whether this folder contains a jvm.dll file. If it does not, check for the file in the `bin\client` folder.

    ![Screenshot showing a jvm.dll file location.](media/self-hosted-integration-runtime-troubleshoot-guide/file-location-image.png)

Note

- If any of these configurations are not as described in these steps, use the [JRE windows installer](https://www.java.com/download/) to fix the problems.
- If all the configurations in these steps are correct as described, there might be a VC++ runtime library missing in the system. You can fix this problem by installing the VC++ 2010 Redistributable Package.

## Self-hosted IR setup

### Integration runtime registration error

#### Symptoms

You might occasionally want to run a self-hosted IR in a different account for either of the following reasons:

- Company policy disallows the service account.
- Some authentication is required.

After you change the service account on the service pane, you might find that the integration runtime stops working, and you get the following error message:

"The Integration Runtime (Self-hosted) node has encountered an error during registration. Cannot connect to the Integration Runtime (Self-hosted) Host Service."

![Screenshot of the Integration Runtime Configuration Manager window, showing an IR registration error.](media/self-hosted-integration-runtime-troubleshoot-guide/ir-registration-error.png)

#### Cause

Many resources are granted only to the service account. When you change the service account to another account, the permissions of all dependent resources remain unchanged.

#### Resolution

Go to the integration runtime event log to check the error.

![Screenshot of the IR event log, showing that a runtime error has occurred.](media/self-hosted-integration-runtime-troubleshoot-guide/ir-event-log.png)

- If the error in the event log is "UnauthorizedAccessException," do the following:

    1. Check the *DIAHostService* sign-in service account in the Windows service panel.

        ![Screenshot of the sign-in service account properties pane.](media/self-hosted-integration-runtime-troubleshoot-guide/logon-service-account.png)
    2. Check to see whether the sign-in service account has read/write permissions for the *%programdata%\Microsoft\DataTransfer\DataManagementGateway* folder.

        - By default, if the service sign-in account hasn't been changed, it should have read/write permissions.

            ![Screenshot of the service permissions pane.](media/self-hosted-integration-runtime-troubleshoot-guide/service-permission.png)
        - If you've changed the service sign-in account, mitigate the issue by doing the following:

            1. Perform a clean uninstallation of the current self-hosted IR.
            2. Install the self-hosted IR bits.
            3. Change the service account by doing the following:
                1. Go to the self-hosted IR installation folder, and then switch to the *Microsoft Integration Runtime\4.0\Shared* folder.
                2. Open a Command Prompt window by using elevated privileges. Replace *&lt;user&gt;* and *&lt;password&gt;* with your own username and password, and then run the following command: `dmgcmd.exe -SwitchServiceAccount "<user>" "<password>"`
                3. If you want to change to the LocalSystem account, be sure to use the correct format for this account: `dmgcmd.exe -SwitchServiceAccount "NT Authority\System" ""`
                4. Do *not* use this format: `dmgcmd.exe -SwitchServiceAccount "LocalSystem" ""`
                5. Optionally, because Local System has higher privileges than Administrator, you can also directly change it in "Services".
                6. You can use a local/domain user for the IR service sign-in account.
            4. Register the integration runtime.
- If the error is "Service 'Integration Runtime Service' (DIAHostService) failed to start. Verify that you have sufficient privileges to start system services," do the following:

    1. Check the *DIAHostService* sign-in service account in the Windows service panel.

        ![Screenshot of the 'Log On' pane for the service account.](media/self-hosted-integration-runtime-troubleshoot-guide/logon-service-account.png)
    2. Check to see whether the sign-in service account has **Log on as a service** permission to start the Windows service:

        ![Screenshot of the 'Log on as service' properties pane.](media/self-hosted-integration-runtime-troubleshoot-guide/logon-as-service.png)

#### More information

If neither of the preceding two resolution patterns applies in your case, try to collect the following Windows event logs:

- Applications and Services Logs &gt; Integration Runtime
- Windows Logs &gt; Application

### Can't find the Register button to register a self-hosted IR

#### Symptoms

When you register a self-hosted IR, the **Register** button isn't displayed on the Configuration Manager pane.

![Screenshot of the Configuration Manager pane, displaying a message that the integration runtime node is not registered.](media/self-hosted-integration-runtime-troubleshoot-guide/no-register-button.png)

#### Cause

As of the release of Integration Runtime 3.0, the **Register** button on existing integration runtime nodes has been removed to enable a cleaner and more secure environment. If a node has been registered to an integration runtime, whether it's online or not, re-register it to another integration runtime by uninstalling the previous node, and then install and register the node.

#### Resolution

1. In Control Panel, uninstall the existing integration runtime.

    Important

    In the following process, select **Yes**. Do not keep data during the uninstallation process.

    ![Screenshot of the &amp;quot;Yes&amp;quot; button for deleting all user data from the integration runtime.](media/self-hosted-integration-runtime-troubleshoot-guide/delete-data.png)
2. If you don't have the integration runtime installer MSI file, go to [download center](https://www.microsoft.com/en-sg/download/details.aspx?id=105539) to download the latest integration runtime.
3. Install the MSI file, and register the integration runtime.

### Unable to register the self-hosted IR because of localhost

#### Symptoms

You're unable to register the self-hosted IR on a new machine when you use get\_LoopbackIpOrName.

**Debug:** A runtime error has occurred. The type initializer for 'Microsoft.DataTransfer.DIAgentHost.DataSourceCache' threw an exception. A nonrecoverable error occurred during a database lookup.

**Exception detail:** System.TypeInitializationException: The type initializer for 'Microsoft.DataTransfer.DIAgentHost.DataSourceCache' threw an exception. ---&gt; System.Net.Sockets.SocketException: A nonrecoverable error occurred during a database lookup at System.Net.Dns.GetAddrInfo(String name).

#### Cause

The issue usually occurs when the localhost is being resolved.

#### Resolution

Use localhost IP address 127.0.0.1 to host the file and resolve the issue.

### Self-hosted setup failed

#### Symptoms

You're unable to uninstall an existing IR, install a new IR, or upgrade an existing IR to a new IR.

#### Cause

The integration runtime installation depends on the Windows Installer service. You might experience installation problems for the following reasons:

- Insufficient available disk space.
- Lack of permissions.
- The Windows NT service is locked.
- CPU utilization is too high.
- The MSI file is hosted in a slow network location.
- Some system files or registries were touched unintentionally.

### The IR service account failed to fetch certificate access

#### Symptoms

When you install a self-hosted IR via Microsoft Integration Runtime Configuration Manager, a certificate with a trusted certificate authority (CA) is generated. The certificate couldn't be applied to encrypt communication between two nodes, and the following error message is displayed:

"Failed to change Intranet communication encryption mode: Failed to grant Integration Runtime service account the access of to the certificate '&lt;*certificate name*&gt;'. Error code 103"

![Screenshot displaying the error message &amp;quot;... Failed to grant Integration Runtime service account certificate access&amp;quot;.](media/self-hosted-integration-runtime-troubleshoot-guide/integration-runtime-service-account-certificate-error.png)

#### Cause

The certificate is using key storage provider (KSP) storage, which is not supported yet. To date, self-hosted IR supports only cryptographic service provider (CSP) storage.

#### Resolution

We recommend that you use CSP certificates in this case.

**Solution 1**

To import the certificate, run the following command:

`Certutil.exe -CSP "CSP or KSP" -ImportPFX FILENAME.pfx`

![Screenshot of the certutil command for importing the certificate.](media/self-hosted-integration-runtime-troubleshoot-guide/use-certutil.png)

**Solution 2**

To convert the certificate, run the following commands:

`openssl pkcs12 -in .\xxxx.pfx -out .\xxxx_new.pem -password pass: <EnterPassword>``openssl pkcs12 -export -in .\xxxx_new.pem -out xxxx_new.pfx`

Before and after conversion:

![Screenshot of the result before the certificate conversion.](media/self-hosted-integration-runtime-troubleshoot-guide/before-certificate-change.png)

![Screenshot of the result after the certificate conversion.](media/self-hosted-integration-runtime-troubleshoot-guide/after-certificate-change.png)

### Self-hosted integration runtime version 5.x

For the upgrade to version 5.x of the self-hosted integration runtime, we require **.NET Framework Runtime 4.7.2** or later. On the download page, you'll find download links for the latest 4.x version and the latest two 5.x versions.

For Azure Data Factory v2 and Azure Synapse customers:

- If automatic update is on and you've already upgraded your .NET Framework Runtime to 4.7.2 or later, the self-hosted integration runtime will be automatically upgraded to the latest 5.x version.
- If automatic update is on and you haven't upgraded your .NET Framework Runtime to 4.7.2 or later, the self-hosted integration runtime won't be automatically upgraded to the latest 5.x version. The self-hosted integration runtime will stay in the current 4.x version. You can see a warning for a .NET Framework Runtime upgrade in the portal and the self-hosted integration runtime client.
- If automatic update is off and you've already upgraded your .NET Framework Runtime to 4.7.2 or later, you can manually download the latest 5.x and install it on your machine.
- If automatic update is off and you haven't upgraded your .NET Framework Runtime to 4.7.2 or later. When you try to manually install self-hosted integration runtime 5.x and register the key, you will be required to upgrade your .NET Framework Runtime version first.

For Azure Data Factory v1 customers:

- Self-hosted integration runtime 5.X doesn't support Azure Data Factory v1.
- The self-hosted integration runtime will be automatically upgraded to the latest version of 4.x. And the latest version of 4.x won't expire.
- If you try to manually install self-hosted integration runtime 5.x and register the key, you'll be notified that self-hosted integration runtime 5.x doesn't support Azure Data Factory v1.

## Self-hosted IR connectivity issues

### Self-hosted integration runtime can't connect to the cloud service

#### Symptoms

When you attempt to register the self-hosted integration runtime, Configuration Manager displays the following error message:

"The Integration Runtime (Self-hosted) node has encountered an error during registration."

![Screenshot of the &amp;quot;The Integration Runtime (Self-hosted) node has encountered an error during registration&amp;quot; message.](media/self-hosted-integration-runtime-troubleshoot-guide/unable-to-connect-to-cloud-service.png)

#### Cause

The self-hosted IR can't connect to the service back end. This issue is usually caused by network settings in the firewall.

#### Resolution

1. Check to see whether the integration runtime service is running. If it is, go to step 2.

    ![Screenshot showing that the self-hosted IR service is running.](media/self-hosted-integration-runtime-troubleshoot-guide/integration-runtime-service-running-status.png)
2. If no proxy is configured on the self-hosted IR, which is the default setting, run the following PowerShell command on the machine where the self-hosted integration runtime is installed:

    ```powershell
     (New-Object System.Net.WebClient).DownloadString("https://wu2.frontend.clouddatahub.net/")
    ```

    Note

    The service URL might vary, depending on the location of your data factory or Synapse workspace instance. To find the service URL, use the Manage page of the UI in your data factory or Azure Synapse instance to find **Integration runtimes** and select your self-hosted IR to edit it. There select the **Nodes** tab and select **View Service URLs**.
3. The following is the expected response:

    ![Screenshot of the PowerShell command response.](media/self-hosted-integration-runtime-troubleshoot-guide/powershell-command-response.png)
4. If you don't receive the response you had expected, use one of the following methods, as appropriate:

    - If you receive a "Remote name could not be resolved" message, there's a Domain Name System (DNS) issue. Contact your network team to fix the issue.
    - If you received an "ssl/tls cert is not trusted" message, check the certificate (`https://wu2.frontend.clouddatahub.net/`) to see whether it's trusted on the machine, and then install the public certificate by using Certificate Manager. This action should mitigate the issue.
    - Go to **Windows** &gt; **Event viewer (logs)** &gt; **Applications and Services Logs** &gt; **Integration Runtime**, and check for any failure that's caused by DNS, a firewall rule, or company network settings. If you find such a failure, forcibly close the connection. Because every company has its own customized network settings, contact your network team to troubleshoot these issues.
5. If "proxy" has been configured on the self-hosted integration runtime, verify that your proxy server can access the service endpoint. For a sample command, see [PowerShell, web requests, and proxies](https://stackoverflow.com/questions/571429/powershell-web-requests-and-proxies).

    ```powershell
     $user = $env:username
     $webproxy = (get-itemproperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet
     Settings').ProxyServer
     $pwd = Read-Host "Password?" -assecurestring
     $proxy = new-object System.Net.WebProxy
     $proxy.Address = $webproxy
     $account = new-object System.Net.NetworkCredential($user,	[Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($pwd)), "")
     $proxy.credentials = $account
     $url = "https://wu2.frontend.clouddatahub.net/"
     $wc = new-object system.net.WebClient
     $wc.proxy = $proxy
     $webpage = $wc.DownloadData($url)
     $string = [System.Text.Encoding]::ASCII.GetString($webpage)
     $string
    ```

The following is the expected response:

![Screenshot of the expected PowerShell command response.](media/self-hosted-integration-runtime-troubleshoot-guide/powershell-command-response.png)

Note

Proxy considerations:

- Check to see whether the proxy server needs to be put on the Safe Recipients list. If so, make sure [these domains](/en-us/azure/data-factory/data-movement-security-considerations#firewall-requirements-for-on-premisesprivate-network) are on the Safe Recipients list.
- Check to see whether SSL/TLS certificate "wu2.frontend.clouddatahub.net/" is trusted on the proxy server.
- If you're using Active Directory authentication on the proxy, change the service account to the user account that can access the proxy as "Integration Runtime Service."

### Couldn't establish a trust relationship for the SSL/TLS secure channel

#### Symptoms

The self-hosted IR couldn't connect to Microsoft Purview.

When you check the self-hosted IR event log after going to **Windows** &gt; **Event viewer (logs)** &gt; **Applications and Services Logs** &gt; **Integration Runtime**, you'll find the following error message:

"The underlying connection was closed: Could not establish trust relationship for the SSL/TLS secure channel. The remote certificate is invalid according to the validation procedure."

The simplest way to check the server certificate of the service is to open the service URL in your browser. For example, open the check server certificate link (`(https://eu.frontend.clouddatahub.net/`) on the machine where the self-hosted IR is installed, and then view the server certificate information.

![Screenshot of the check server certificate pane of the Azure Data Factory service.](media/self-hosted-integration-runtime-troubleshoot-guide/server-certificate.png)

![Screenshot of the window for checking the server certification path.](media/self-hosted-integration-runtime-troubleshoot-guide/certificate-path.png)

#### Cause

There are two possible reasons for this issue:

- Reason 1: The root CA of the service's server certificate isn't trusted on the machine where the self-hosted IR is installed.
- Reason 2: You're using a proxy in your environment, the server certificate of the service is replaced by the proxy, and the replaced server certificate isn't trusted by the machine where the self-hosted IR is installed.

#### Resolution

- For reason 1: Make sure that the service's server certificate and its certificate chain are trusted by the machine where the self-hosted IR is installed.
- For reason 2: Either trust the replaced root CA on the self-hosted IR machine, or configure the proxy not to replace the service's server certificate.

For more information about trusting certificates on Windows, see [Installing the trusted root certificate](/en-us/skype-sdk/sdn/articles/installing-the-trusted-root-certificate).

#### More information

We've rolled out a new SSL certificate, which is signed from DigiCert. Check to see whether the DigiCert Global Root G2 is in the trusted root CA.

![Screenshot showing the DigiCert Global Root G2 folder in the Trusted Root Certification Authorities directory.](media/self-hosted-integration-runtime-troubleshoot-guide/trusted-root-ca-check.png)

If it isn't in the trusted root CA, [download it here](http://cacerts.digicert.com/DigiCertGlobalRootG2.crt).