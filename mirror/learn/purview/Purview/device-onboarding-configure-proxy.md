---
layout: Conceptual
title: Configure device proxy and internet connection settings for Microsoft Purview Endpoint DLP | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/device-onboarding-configure-proxy
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.subservice: purview-device-onboarding
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
- highpri
search.appverid:
- MET150
description: Learn how to configure WinHTTP-based proxy and internet connectivity settings so that Microsoft Endpoint DLP can communicate with cloud services, including supported proxy discovery methods and manual configuration options.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 458406d2-7654-ac74-8e67-cc614c376a12
document_version_independent_id: 458406d2-7654-ac74-8e67-cc614c376a12
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/device-onboarding-configure-proxy.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: device-onboarding-configure-proxy
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/device-onboarding-configure-proxy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/486161dc-fa28-4625-9b1c-1a21d690bc8d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/5dd28c86-729c-4723-ab5a-57e26fcec2a8
platformId: 568721b6-4446-9a89-cd90-bbf71bf91474
---

# Configure device proxy and internet connection settings for Microsoft Purview Endpoint DLP | Microsoft Learn

Microsoft Endpoint technologies use Microsoft Windows HTTP (WinHTTP) to report data and communicate with the Microsoft endpoint cloud service. The embedded service runs in system context using the LocalSystem account.

Tip

For organizations that use forward proxies as a gateway to the Internet, you can use network protection to investigate behind a proxy. For more information, see [Investigate connection events that occur behind forward proxies](/en-us/windows/security/threat-protection/microsoft-defender-atp/investigate-behind-proxy).

The WinHTTP configuration setting is independent of the Windows Internet (WinINet) Internet browsing proxy settings and can only discover a proxy server by using the following auto discovery methods:

- Transparent proxy
- Web Proxy Auto-discovery Protocol (WPAD)

    Note

    If you’re using Transparent proxy or WPAD in your network topology, you don’t need special configuration settings. For more information on Defender for Endpoint URL exclusions in the proxy, see Enable access to Endpoint DLP cloud service URLs in the proxy server.
- Manual static proxy configuration:

    - Registry-based configuration
    - WinHTTP configured using netsh command – Suitable only for desktops in a stable topology (for example: a desktop in a corporate network behind the same proxy)

## Configure the proxy server manually using a registry-based static proxy

For endpoint devices that aren't permitted to connect to the Internet, you need to configure a registry-based static proxy. You need to configure the registry-based static proxy to allow only Microsoft Endpoint DLP to report diagnostic data and communicate with Microsoft endpoint cloud service.

The static proxy is configurable through Group Policy (GP). The Group Policy settings can be found under:

1. Open **Administrative Templates &gt; Windows Components &gt; Data Collection and Preview Builds &gt; Configure Authenticated Proxy usage for the Connected User Experience and Telemetry Service**
2. Set it to **Enabled** and select **Disable Authenticated Proxy usage**:

    ![Screenshot of Group Policy setting to disable authenticated proxy usage for the Connected User Experience and Telemetry Service.](media/atp-gpo-proxy1.png)
3. Open **Administrative Templates &gt; Windows Components &gt; Data Collection and Preview Builds &gt; Configure connected user experiences and telemetry**:

    Configure the proxy

    ![Screenshot of Group Policy setting to configure the telemetry proxy server for connected user experiences.](media/atp-gpo-proxy2.png)

    The policy sets two registry values `TelemetryProxyServer` as REG\_SZ and `DisableEnterpriseAuthProxy` as REG\_DWORD under the registry key `HKLM\Software\Policies\Microsoft\Windows\DataCollection`.

    The registry value TelemetryProxyServer is in this format &lt;server name or ip&gt;:&lt;port&gt;. For example: **10.0.0.6:8080**

    The registry value `DisableEnterpriseAuthProxy` should be set to 1.

## Configure the proxy server manually using "netsh" command

Use netsh to configure a system-wide static proxy.

Note

This will affect all applications including Windows services which use WinHTTP with default proxy. - Laptops that are changing topology (for example: from office to home) will malfunction with netsh. Use the registry-based static proxy configuration.

1. Open an elevated command line:

    1. Go to **Start** and type **cmd**
    2. Right-click **Command prompt** and select **Run as administrator**.
2. Enter the following command and press **Enter**:

    `netsh winhttp set proxy <proxy>:<port>`

    For example: **netsh winhttp set proxy 10.0.0.6:8080**
3. To reset the winhttp proxy, enter the following command and press **Enter**:

    `netsh winhttp reset proxy`

See [Netsh Command Syntax, Contexts, and Formatting](/en-us/windows-server/networking/technologies/netsh/netsh-contexts) to learn more.

## Enable access to Endpoint DLP cloud service URLs in the proxy server

If a proxy or firewall is blocking all traffic by default and allowing only specific domains through, add the domains listed in the [Microsoft Defender for Endpoint service URLs spreadsheet](https://aka.ms/MDE-streamlined-urls) to the allowed domains list.

This [Microsoft Defender for Endpoint service URLs spreadsheet](https://aka.ms/MDE-streamlined-urls) lists the services and their associated URLs that your network must be able to connect to. You should ensure that there are no firewall or network filtering rules that would deny access to these URLs, or you may need to create an allow rule specifically for them.

If a proxy or firewall has HTTPS scanning (SSL inspection) enabled, exclude the domains listed in the Microsoft Defender for Endpoint service URLs spreadsheet from HTTPS scanning. If a proxy or firewall is blocking anonymous traffic, as Endpoint DLP is connecting from system context, make sure anonymous traffic is permitted in the previously listed URLs.

## Verify client connectivity to Microsoft cloud service URLs

Verify the proxy configuration completed successfully, that WinHTTP can discover and communicate through the proxy server in your environment, and that the proxy server allows traffic to the Defender for Endpoint service URLs.

1. Download the [MDATP Client Analyzer tool](https://aka.ms/mdatpanalyzer) to the PC where Endpoint DLP is running on.
2. Extract the contents of MDATPClientAnalyzer.zip on the device.
3. Open an elevated command line:

    1. Go to **Start** and type **cmd**.
    2. Right-click **Command prompt** and select **Run as administrator**.
4. Enter the following command and press **Enter**:

    `HardDrivePath\MDATPClientAnalyzer.cmd`

    Replace *HardDrivePath* with the path where the MDATPClientAnalyzer tool was downloaded to, for example

    **C:\Work\tools\MDATPClientAnalyzer\MDATPClientAnalyzer.cmd**
5. Extract the **MDATPClientAnalyzerResult.zip**\* file created by tool in the folder used in the *HardDrivePath*.
6. Open **MDATPClientAnalyzerResult.txt** and verify that you have performed the proxy configuration steps to enable server discovery and access to the service URLs. The tool checks the connectivity of Defender for Endpoint service URLs that Defender for Endpoint client is configured to interact with. It then prints the results into the **MDATPClientAnalyzerResult.txt** file for each URL that can potentially be used to communicate with the Defender for Endpoint services. For example:

    ```cmd
    Testing URL: https://xxx.microsoft.com/xxx
    1 - Default proxy: Succeeded (200)
    2 - Proxy auto discovery (WPAD): Succeeded (200)
    3 - Proxy disabled: Succeeded (200)
    4 - Named proxy: Doesn't exist
    5 - Command-line proxy: Doesn't exist
    ```

If at least one of the connectivity options returns a (200) status, then the Defender for Endpoint client can communicate with the tested URL properly using this connectivity method.

However, if the connectivity check results indicate a failure, an HTTP error is displayed (see [HTTP Status Codes](https://developer.mozilla.org/docs/Web/HTTP/Status)). You can then use the URLs listed in Enable access to Endpoint DLP cloud service URLs in the proxy server. The URLs you’ll use will depend on the region selected during the onboarding procedure.

Note

The Connectivity Analyzer tool is not compatible with attack surface reduction rule [Block process creations originating from PSExec and WMI commands](/en-us/defender-endpoint/attack-surface-reduction-rules-reference#block-process-creations-originating-from-psexec-and-wmi-commands). You will need to temporarily disable this rule to run the connectivity tool.

When the TelemetryProxyServer is set, in Registry or via Group Policy, Defender for Endpoint will fall back to direct if it can’t access the defined proxy. Related topics:

- Onboard Windows 10 devices
- Troubleshoot Microsoft Endpoint DLP onboarding issues