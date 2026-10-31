---
layout: Conceptual
title: Tanium and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-tanium
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use Tanium with Microsoft Security Copilot.
ms.date: 2026-02-19T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: concept-article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
ms.reviewer: shivanpatel
search.audiencetype: Admin
locale: en-us
document_id: 95d57153-f20d-7e11-4307-cb02265eb1af
document_version_independent_id: 95d57153-f20d-7e11-4307-cb02265eb1af
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-tanium.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-tanium
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-tanium.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/54918a83-0404-4863-9c91-715186c1f582
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/b26f5f7a-0913-4a95-8337-ed7543902f2d
platformId: 5ec93f0c-499c-9f01-c90e-1264e2ba73e5
---

# Tanium and Microsoft Security Copilot | Microsoft Learn

Tanium provides a converged endpoint management (XEM) reference platform to manage complex security and technology environments. Tanium protects endpoints from cyber threats by integrating workflows across IT, Risk, Compliance, and Security into a single platform. Tanium delivers comprehensive visibility across devices, a unified set of controls, real-time remediation, and a common taxonomy to protect critical information and infrastructure at scale.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Microsoft Security Copilot requires a Tanium instance URL and API token. You'll need to take the following steps before using the plugin.

1. Sign in to [Tanium Console](https://help.tanium.com/bundle/ug_console_cloud/page/platform_user/console_getting_started.html#Log_in) to retrieve information you need to configure the Tanium plugin.

    1. Select Modules &gt; Connect &gt; Overview. The Connect overview page appears.
    2. Select Settings and navigate to **Microsoft Copilot for Security**.
    3. Select **Tanium Instance URL Copy** to copy the Tanium instance URL to the clipboard. Paste the URL in a text editor, such as Notepad.
    4. Select **Generate** to generate an API token, and copy the token value to the clipboard. Paste the token value in a text editor.
2. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).

    1. Select **Sources** from the prompt bar. The **Manage sources** modal appears.
    2. Go to the **Tanium** plugin, and then select **Set up**.
    3. On the Tanium settings, copy the Tanium Instance URL and paste it in **Tanium Instance URL**.
    4. Copy the token value and paste it in **Value**.
    5. Select **Save**.

## Sample Tanium prompts

After the Tanium plugin is configured, you can use it to retrieve information about endpoints (devices) in your organization. The following table lists some capabilities and example prompts you can try:

| Capability | Example prompts |
| --- | --- |
| **Get Logged In User** Retrieves the user that is currently logged into an endpoint Requires Tanium Core Platform | `Using Tanium, return the user currently logged into the endpoint with the hostname hostname so that I can investigate possible unauthorized endpoint use. Return a Tanium Console Question Results URL so that I can view more real-time information for this endpoint.` |
| **Get Real-time Data from Endpoints** Retrieves real-time data from endpoints based on a Tanium sensor. For more information on supported sensors  Requires Tanium Core Platform, sensor-dependent | `Using Tanium, return the computer name and IP address of endpoints. Display the results in a table, alphabetically sorted by computer name, and return a Tanium Console Question Results URL so that I can view the real-time list of endpoints.` |
| **Count Endpoints Having Package Version**Retrieves the total count of endpoints that have the given software package  Requires Asset, SBOM | `Using Tanium, return the total number of endpoints with a software package for software-name, so that I can start cataloging which computers have the software installed. Display the results in a table, alphabetically sorted by host name, and return a Tanium Console Question Results URL so that I can view the real-time list of endpoints.` |
| **List Endpoints Having Package**Retrieves up to 10 endpoints that have the given software package  Requires Asset, SBOM | `Using Tanium, return the endpoints with a software package for software-name so that I can start cataloguing which computers might have an out-of-date version. Display the results in a table, alphabetically sorted by host name, and return a Tanium Console Question Results URL so that I can view the real-time list of endpoints.` |
| **List Process SHA-256 Hashes and Versions**Retrieves the SHA-256 file hash and version for a given process Requires Asset, SBOM, Threat Response | `Using Tanium, return the SHA-256 hash value and process version for the running process process-name, so that I can find other instances of this process based on the hash value.` |
| **Get Vulnerability Test Results** Returns whether an endpoint is vulnerable to a given CVE, and the reason why it is vulnerable Requires Tanium Comply | `Using Tanium, examine whether endpoint <hostname> is vulnerable to <cve-id>, and return the reasons that this endpoint is vulnerable, along with a suggested plan of action to remediate the intrusion.` |
| **List Endpoints Vulnerable To CVE**Retrieves up to 10 endpoints vulnerable to a given CVE ID Requires Tanium Comply | `Using Tanium, return the endpoints vulnerable to cve-id, so that I can remediate the vulnerability on these endpoints. Display the results in a table, sorted alphabetically by host name, and return a Tanium Console Question Results URL so that I can view the real-time list of endpoints.` |
| **View Endpoint Processes** Retrieves a URL to the Threat Response Live Connection page for the requested endpoint, which contains a list of running processes Requires Direct Connect, Threat Response | `Using Tanium, return a Threat Response Live Connection URL for the endpoint with the hostname hostname, so that I can review the running processes and identify potential vulnerabilities.` |
| **List Service Module Details**Retrieves running service module information for an endpoint, including name, caption, and image path Requires Incident Response | `Using Tanium, return information for the service modules running on the endpoint with the hostname hostname, so that I can review the list for unexpected service modules. Display the results in a table, alphabetically sorted by service module name, and return a Tanium Console Question Results URL so that I can view the real-time list of service modules.` |
| **List Service Process Details** Retrieves running service process information for an endpoint, including name, process ID, and file path  Requires Incident Response | `Using Tanium, return information for the service processes running on the endpoint with the hostname hostname, so that I can review the list for unexpected service processes. Display the results in a table, alphabetically sorted by service process name, and return a Tanium Console Question Results URL so that I can view the real-time list of service processes.` |
| **List WMI Event Consumers**Retrieves Windows Management Instrumentation (WMI) event consumers running on an endpoint Requires Incident Response | `Using Tanium, return the WMI event consumers running on the endpoint with the hostname hostname so that I can ensure only expected event consumers are running, and return a Tanium Console Question Results URL so that I can view the real-time list of event consumers.` |
| **List File Details**Retrieves details for a file by name, including the endpoints on which it is installed, the file path, and file size Requires Index | `Using Tanium, return information for the file named file-name so that I can determine if it is running on unintended endpoints. Display the results in a table, alphabetically sorted, and return a Tanium Console Question Results URL so that I can view the real-time list.` or `Using Tanium, return information for the file named file-name installed on the endpoint with the hostname hostname, so that I can determine if it is running on unintended endpoints. Display the results in a table, alphabetically sorted, and return a Tanium Console Question Results URL so that I can view real-time information.` |
| **List Child Processes for Process File**Returns all child processes running on an endpoint based on a given process file name Requires Threat Response | `Using Tanium, list the child processes of process-name so that I can analyze resource usage. Display the results in a table, alphabetically sorted by process name, and return a Tanium Console Question Results URL so that I can view the real-time list of endpoints.` or `Using Tanium, list the child processes of process-name that are running on the computer with the hostname hostname, so that I can analyze resource usage. Display the results in a table, alphabetically sorted by process name, and return a Tanium Console Question Results URL so that I can view the real-time list of endpoints.` |
| **List Endpoints with Process Command**Retrieves up to 10 endpoints running the given command line command Requires Threat Response | `Using Tanium, return the endpoints running the command line command process-command, so that I can ensure this process is not running on unexpected endpoints. Display the results in a table, sorted alphabetically by host name, and return a Tanium Console Question Results URL so that I can view the real-time list of endpoints.` |
| **List Endpoints with Process Name**Retrieves up to 10 endpoints running the given process Requires Threat Response | `Using Tanium, return the endpoints running a process called process-name, so that I can ensure this process is not running on unexpected endpoints. Display the results in a table, sorted alphabetically by host name, and return a Tanium Console Question Results URL so that I can view the real-time list of endpoints.` |
| **List Endpoints with Process MD5 Hash**Retrieves up to 10 endpoints running the given process matching the provided MD5 hash valueRequires Threat Response | `Using Tanium, return all endpoints that are running a process with the MD5 hash value md5-hash-value, so that I can ensure this process is not running under a different file name. Display the results in a table, sorted alphabetically by host name, and return a Tanium Console Question Results URL so that I can view the real-time list of endpoints.` |
| **List File Operations**Retrieves historical file operation information from endpoints, including endpoint name, file path, and the file operation type, such as create or delete Requires Threat Response | `Using Tanium, return file operation information for the endpoint named hostname running on the file path "_partial-file-path" over the past time-frame so that I can determine if any malicious file behavior is occuring on the endpoint. Display the results in a table, alphabetically sorted, and return a Tanium Console Question Results URL so that I can view the real-time list.` or `Using Tanium, return file operation information for files running on the file path "_partial-file-path" over the past time-frame so that I can determine if there is any malicious file creation or deletion. Display the results in a table, alphabetically sorted, and return a Tanium Console Question Results URL so that I can view the real-time list.` |
| **List Processes Connected To IPv4 Address**Retrieves the processes running on an endpoint with the given IPv4 address Requires Threat Response | `Using Tanium, return the processes running on the endpoint with the IPv4 address ipv4-address, so that I can analyze any potential security intrusions and resource usage. Display the results in a table, sorted alphabetically by process name, and return a Tanium Console Question Results URL so that I can view the real-time list of endpoints.` |
| **List Process Ran As User**Retrieve the processes running on an endpoint as a given user Requires Threat Response | `Using Tanium, return the processes running as the user user-name, so that I can determine whether there are issues with unauthorized access. Display the results in a table, sorted alphabetically by computer name, and return a Tanium Console Question Results URL so that I can view the real-time list of endpoints.` or `Using Tanium, return the processes running as the user user-name on the endpoint with the hostname hostname, so that I can determine whether there are issues with unauthorized access. Display the results in a table, sorted alphabetically by process name, and return a Tanium Console Question Results URL so that I can view the real-time list of endpoints.` |

## Troubleshoot the Tanium plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred*, make sure the plugin is turned on. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts are not invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

## Provide feedback

To provide feedback, contact [Tanium](https://www.tanium.com/).