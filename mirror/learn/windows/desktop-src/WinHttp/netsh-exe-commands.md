---
layout: Conceptual
title: Netsh.exe commands - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/winhttp/netsh-exe-commands
breadcrumb_path: /windows/desktop/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-WinDevCenter
recommendations: true
adobe-target: true
ms.service: windows-api-desktop-tech
ms.subservice: networking
ms.author: jken
author: GrantMeStrength
feedback_system: Standard
feedback_product_url: https://www.microsoft.com/en-us/windowsinsider/feedbackhub/fb
feedback_help_link_url: https://learn.microsoft.com/answers/tags/224/windows-api-win32/
feedback_help_link_type: get-help-at-qna
description: You can use commands in the netsh winhttp context to configure proxy and tracing settings for Windows HTTP.
ms.topic: concept-article
ms.date: 2023-12-11T00:00:00.0000000Z
locale: en-us
document_id: e8d04b38-52dc-cf1a-c8b1-b9194a6868a4
document_version_independent_id: e8d04b38-52dc-cf1a-c8b1-b9194a6868a4
original_content_git_url: https://github.com/MicrosoftDocs/win32-pr/blob/live/desktop-src/WinHttp/netsh-exe-commands.md
site_name: Docs
depot_name: MSDN.win32
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.win32/{branchName}{pdfName}
asset_id: winhttp/netsh-exe-commands
moniker_range_name: 
monikers: []
item_type: Content
source_path: desktop-src/WinHttp/netsh-exe-commands.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
platformId: 5e395848-741a-1aaa-adf0-630854aaceff
---

# Netsh.exe commands - Win32 apps | Microsoft Learn

Tip

Use `Netsh.exe` anywhere you would previously have used the deprecated tool `ProxyCfg.exe`.

You can use commands in the `netsh winhttp` context to configure proxy and tracing settings for Windows HTTP. The `netsh` commands for WinHTTP can be run manually at the `netsh` prompt, or in scripts and batch files.

To run these commands from the command prompt, you must either enter the `netsh winhttp` context, or prepend the context to the command. For example, if you're at the command prompt, but you haven't yet typed `netsh` followed by `winhttp` in order to enter the `netsh winhttp` context, then you need to type a command with the format:

**netsh winhttp***command*

In that format, *command* is the command that you want to run. And that should include all of the required parameters for that command.

## Netsh winhttp commands

The following entries provide details for each command.

### flush logbuffer

Flushes the internal buffers for the log files.

#### Syntax

**flush logbuffer**

### import proxy

Imports the proxy settings in the Internet Explorer (IE) Web browser's **Internet Options**. Importing settings from IE is the only available option.

#### Syntax

**import proxy source =ie**

### reset proxy

Resets the WinHTTP proxy setting to *DIRECT*.

#### Syntax

**reset proxy**

### reset tracing

Resets the WinHTTP trace parameters to the default settings.

#### Syntax

**reset tracing**

#### Remarks

Here are the default WinHTTP trace parameters:

| Parameter | Value |
| --- | --- |
| Tracing state | Disabled |
| trace-file-prefix | None |
| output | File |
| level | Default |
| format | Ansi |
| max-trace-file-size | 65535 |

### set advproxy

Configures the WinHTTP advanced proxy setting. Note that SOCKS5 isn't supported. Also see show advproxy.

#### Syntax

**set advproxy** [**setting-scope=**]*&lt;Scope&gt;* [**settings=**]*&lt;Settings&gt;***set advproxy** [**setting-scope=**]*&lt;Scope&gt;* [**settings-file=**]*&lt;SettingsFile&gt;*

#### Parameters

**setting-scope**. User or machine.

**settings**. Proxy settings in JSON format. The JSON object must contain the properties "Proxy" (string value), "ProxyBypass" (string value), "AutoconfigUrl" (string value), and "AutoDetect" (Boolean value). The format of the strings structure is `([<scheme>=][<scheme>"://"]<server>[":"<port>])`. For more info, see **Remarks** in [WINHTTP_PROXY_INFO structure](/en-us/windows/win32/api/winhttp/ns-winhttp-winhttp_proxy_info).

**setting-file**. A file, in JSON format, that contains the settings.

#### Examples

```console
set advproxy setting-scope=machine settings={<settings>}

set advproxy setting-scope=user settings-file=settings.json

set advproxy setting-scope=machine settings={\"Proxy\":\"contoso-proxy.com:3128\",\"ProxyBypass\":\"\",\"AutoconfigUrl\":\"\",\"AutoDetect\":true}
```

Here is an example of WinHTTP advanced proxy setting that sets different proxies for HTTP, HTTPS, FTP, and SOCKS protocols:

```console
netsh winhttp set advproxy setting-scope=user settings={\"Proxy\":\"http=http-proxy.com:8080;https=https-proxy.com:8081;ftp=ftp-proxy.com:8082;socks=socks-proxy.com: 8083\",\"ProxyBypass\":\"\",\"AutoconfigUrl\":\"\",\"AutoDetect\":true}"

{
  "ProxyIsEnabled": true,
  "Proxy": "http=http-proxy.com:8080;https=https-proxy.com:8081;ftp=ftp-proxy.com:8082;socks=socks-proxy.com:8083",
  "AutoConfigIsEnabled": false,
  "AutoDetect": true,
  "PerUserProxySettings": true
}
```

### set proxy

Important

`set proxy` is deprecated. Use set advproxy instead.

Configures the WinHTTP proxy setting.

#### Syntax

**set proxy** [**proxy-server=**]*ProxyServerName* [**bypass-list=**]*&lt;HostsList&gt;*

#### Parameters

**proxy-server**. Required. Specifies the proxy server to use for http, secure http (https), or both http and https protocols.

**bypass-list**. Optional. Specifies a list of web sites that should be visited without using the proxy server. Use "&lt;local&gt;" to bypass all short name hosts.

#### Examples

Following are three examples of how to use the `set proxy` command.

```console
set proxy myproxy

set proxy myproxy:80 "<local>bar"

set proxy proxy-server="http=myproxy;https=sproxy:88" bypass-list="*.contoso.com"
```

### set tracing

Configures the WinHTTP tracing parameters.

#### Syntax

**set tracing** [**output=**]**file** | **debugger** | **both** [**trace-file-prefix=**]*FilePrefix* [**level=**]**default** | **verbose** [**format=**]**ansi** | **hex** [**max-trace-file-size=**]*FileSize* [**state=**]**enabled** | **disabled**

#### Parameters

**output**. Optional. Specifies whether tracing data is exported to a file, to a debugger, or to both.

**trace-file-prefix**. Optional. Specifies a string value that's a prefix for the log file. The file prefix can include a folder location/path. Type "\*" to delete an existing prefix.

**level**. Optional. Specifies the amount of information to log.

**format**. Optional. Specifies the display format of network traffic (hexadecimal or ansi).

**max-trace-file-size**. Optional. Specifies a numeric value that's the maximum size of the trace file in bytes.

**state**. Required. Specifies whether tracing is enabled or disabled.

#### Examples

Following are two examples of how to use the set tracing command.

```console
set tracing trace-file-prefix="C:\Temp\Test3" level=verbose format=hex

set tracing output=debugger max-trace-file-size=512000 state=enabled
```

### show advproxy

Displays the current WinHTTP advanced proxy setting. Note that SOCKS5 isn't supported. Also see set advproxy.

#### Syntax

**show advproxy**

### show proxy

Important

`show proxy` is deprecated. Use show advproxy instead.

Displays the current WinHTTP proxy setting.

#### Syntax

**show proxy**

### show tracing

Displays the current WinHTTP tracing parameters.

#### Syntax

**show tracing**