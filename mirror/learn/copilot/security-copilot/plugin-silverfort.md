---
layout: Conceptual
title: Silverfort and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-silverfort
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use Silverfort with Microsoft Security Copilot.
ms.date: 2025-08-25T00:00:00.0000000Z
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
document_id: ce52e493-9188-3e34-b9a8-2fccd1e54967
document_version_independent_id: ce52e493-9188-3e34-b9a8-2fccd1e54967
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-silverfort.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-silverfort
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-silverfort.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8a94907f-2511-4271-b5ca-ec7f2e75067c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bffa8e88-f633-409d-a24d-083bdbc68872
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: b83e6506-aa58-871d-294e-55b191901e6c
---

# Silverfort and Microsoft Security Copilot | Microsoft Learn

The Silverfort plugin for Microsoft Security Copilot enables seamless integration of Silverfort's advanced CEF data within the Microsoft Sentinel environment to bring in Identity protection insights. This plugin empowers security teams to enhance their threat detection and response capabilities through intuitive natural language queries and detailed insights.

The Silverfort plugin leverages KQL-based queries to extract and analyze data from Silverfort's security logs within the Microsoft Sentinel workspace. Users can customize their queries using a range of input parameters to retrieve targeted information, enabling more efficient threat investigation and proactive defense measures.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Prerequisites

To use the Silverfort plugin you must first configure Common Event Format (CEF) and Syslog through Azure Monitor Agent (AMA) forwarding using the following guide. This plugin queries data stored in the CommonSecurityLog table in a log Analytics workspace enabled for Microsoft Sentinel. For more information, see [Ingest syslog and CEF messages to Microsoft Sentinel with the Azure Monitor Agent](/en-us/azure/sentinel/connect-cef-syslog-ama).

After setting up a forwarder, proceed to:

- Assign a public IP address
- Allow Syslog inbound traffic on port 514 in network settings

You're now ready to set up your Syslog Server in Silverfort to send the events and have the newly configured AMA forward the information to Microsoft Sentinel.

1. Enter the IP Address of your AMA Forwarder in the Server IP field.
2. Enter port 514 in the Port field.
3. Select TCP Protocol in the Protocol Field.

    ![Screenshot the syslog server in Silverfort.](media/silverfort-syslog-server.png)
4. Verify that all the information in the fields are present except the Splunk application.
5. Select **Save All**.

## Know before you begin

You'll need to take the following steps before using the plugin.

1. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
2. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
3. Next to **Silverfort**, select the toggle to enable it.

    Provide the following information:

    - TenantId: The ID of the Microsoft Entra ID Organization that the Microsoft Sentinel workspace is in.
    - WorkspaceName: The name of the Microsoft Sentinel workspace.
    - SubscriptionId: The ID of the Azure Subscription that the Microsoft Sentinel workspace is in.
    - ResourceGroupName: The name of the Resource Group that the Microsoft Sentinel workspace is in.
4. Save your changes.

## Sample Silverfort prompts

After the Silverfort plugin is configured, you can use it by taking one of the following steps:

- Access the plugin capabilities by selecting the **Plugin button** from the prompt bar and selecting **Silverfort**.
- Prompt Security Copilot using any of the following example prompts.

The following table lists example prompts to try:

| Capability | Example prompts |
| --- | --- |
|  |  |
| QuerySilverfortInformation  Queries information related to CEF data within Microsoft Sentinel based on time, risk, indicator, source IP, source hostname, and others. | `Provide a count of Silverfort risk requests that have the Silverfort policy name 'mypolicy' in the last week.``How many Silverfort MFA subtype requests have there been in the last week that have an MFA response of 'Blocked'?``How many requests in the last week have a Silverfort policy action of 'MFA'?``Give me the top 10 Silverfort requests with Criticalrisk where the source username is "john.doe@something.com".` |
| QuerySilverfortIncidents  Queries for all Silverfort related Incidents within the time period specified | `Give me all Silverfort incidents in the last month.``Give me all Silverfort incidents in the last week with status ongoing.` |

## Troubleshoot the Silverfort plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred* | Make sure the plugin is turned on. This error may occur if the lookback period is too long, causing the query to attempt to retrieve an excessive amount of data. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

## Provide feedback

To provide feedback, contact [Silverfort](https://silverfort.com/).