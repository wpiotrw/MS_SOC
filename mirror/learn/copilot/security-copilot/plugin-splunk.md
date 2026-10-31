---
layout: Conceptual
title: Splunk and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-splunk
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the Splunk plugin for Microsoft Security Copilot.
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
- sfi-image-nochange
ms.reviewer: shivanpatel
search.audiencetype: Admin
locale: en-us
document_id: 3702500e-4018-dc42-5d12-3d46307cf264
document_version_independent_id: 3702500e-4018-dc42-5d12-3d46307cf264
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-splunk.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-splunk
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-splunk.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: c54a4ba1-87bc-3ec2-2ee7-f30ea98064f2
---

# Splunk and Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

This plugin allows Security Copilot users to make calls to the Splunk REST API. Currently the following functionalities are supported:

- Performing normal and one-shot ad-hoc SPL queries.
- Creating, retrieving, and dispatching saved searches in Splunk.
- Retrieving and viewing information about fired alerts from saved searches in Splunk.
- Getting information about currently running search jobs in Splunk.

## Prerequisites

- Access to an installation of Splunk
- Ensure to allow Security Copilot's egress IPs to contact your Splunk instance. For more information, see [Security Copilot IP address ranges](plugin-ip-address). Follow the steps to allow the below IPs based on the Splunk instance type you're using. For example, for Splunk Cloud, use the guidance here: [Splunk Cloud Platform Admin Manual](https://docs.splunk.com/Documentation/SplunkCloud/9.3.2408/Admin/ConfigureIPAllowList).
- One of the following authentication methods in Splunk
    - Splunk authentication token (preferred)
    - Splunk username and password for basic authentication

Documentation for setting up a Splunk authentication token can be found [here](https://docs.splunk.com/Documentation/Splunk/latest/Security/CreateAuthTokens). In addition, there are other considerations you may need to take in mind if you're running Splunk Cloud. Those considerations are documented [here](https://docs.splunk.com/Documentation/Splunk/latest/RESTTUT/RESTandCloud).

Note

This article contains information about non-Microsoft plugins. This is provided to help complete integration scenarios. However, Microsoft doesn't provide troubleshooting support for non-Microsoft plugins. Contact the vendor for support.

## Know before you begin

Integration with Security Copilot works with either an API key or basic authentication. You need to take the following steps before using the plugin.

### API Key Authentication

API Key Authentication is the preferred method of authentication. To set up authentication via API Key, you need to have the following pieces of information:

- The URL for accessing the REST API
- The Splunk authentication token for the Splunk user account you're using to access the API. Documentation for setting up a Splunk authentication token can be found [here](https://docs.splunk.com/Documentation/Splunk/latest/Security/CreateAuthTokens). In addition, there are other considerations you may need to take in mind if you're running Splunk Cloud. Those considerations are documented [here](https://docs.splunk.com/Documentation/Splunk/latest/RESTTUT/RESTandCloud).

1. When you're asked to set up authentication, select the **APIKey** option.

    ![Image of Splunk select preferred authorization method page](media/splunk-apikey-step1.png)
2. Add the Splunk API URL to the field for **Splunk Instance API URL**. Add the Splunk authentication token in the **Value** field.

    ![Image of Splunk Security Copilot settings.](media/splunk-apikey-step2.png)
3. Select **Save** to complete setup.

### Basic Authentication

To set up authentication using Basic Authentication, you need to have the following pieces of information:

- The URL for accessing the REST API
- The username and password for the Splunk user account you're using to access the API.

1. When you're asked to set up authentication, select the **Basic login** option.

    ![Image of basic log in method to connect Splunk.](media/splunk-basicauth-step1.png)
2. Add the Splunk API URL to the field for **Splunk Instance API URL**. Add the Splunk username in the **Username** field. Add the Splunk password in the **Password** field.

    ![Image of Splunk settings page to set up.](media/splunk-basicauth-step2.png)
3. Select **Save** to complete setup.

## Available Skills

The Splunk Plugin for Microsoft Security Copilot exposes the following skills:

- Ad-hoc searches
    - Creating search jobs
    - Getting information about search jobs
    - Retrieving results from search jobs
    - Running one-shot searches
- Saved searches
    - Retrieving saved searches
    - Creating saved searches
    - Dispatching a saved search
- Fired alerts from saved searches
    - Retrieving fired alerts
    - Retrieving fired alert details

With the Splunk plugin for Microsoft Security Copilot, you can invoke interactions with Splunk in the context of a natural conversation. Here's an example:

1. A user can use the public web to research data on a recently announced vulnerability / CVE.
2. The user can then use a follow-up prompt such as "Save this CVE number as a search in Splunk across all indexes". Security Copilot will maintain the context from the previous prompt in the most recent prompt.
3. The user can then modify the saved search within Splunk to incorporate more advanced SPL techniques or to create visualizations.

## Sample Splunk prompts

| Skill | Prompt |
| --- | --- |
| Create a search job | `Run the following search in Splunk in normal mode: index=notable "System Network Configuration Discovery". Ensure to begin the query with the word "search".` |
| Get the search job results | `Get the search job results for SID 1740764708.5591 from Splunk` |
| Run a oneshot search | `Run the following search in Splunk in oneshot mode: index=notable "System Network Configuration Discovery"` |
| Create a saved search | `Save the following search in Splunk: index=notable "System Network Configuration Discovery". Name the search "Network Config Discovery report".` |
| Retrieve saved searches | `Get all of the saved searches for the copilot user from Splunk` |
| Dispatch a saved search | `Dispatch the saved search "Top Mitre Techniques" in Splunk` |
| Retrieve fired alerts | `Get the list of fired alerts from Splunk` |
| Retrieve fired alert details | `Tell me about the fired alert Apache_HTTP_StatusCode_Alert_Test` |
| Get current search jobs | `Get all of the current search jobs in Splunk` |

Microsoft Security Copilot will often understand and get context from answers that are returned. As a result, you can use natural conversation in a chain of prompts. For example: if you use a prompt such as `Dispatch the saved search "Cloud Alerts" in Splunk`, the search job ID is returned. Security Copilot will have that search job ID in its current context, and you can follow up with `Get the search job results` rather than having to manually specify a search job ID.

## Troubleshoot the Splunk plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred*. Make sure the plugin is turned on. This error may occur if the lookback period is too long, causing the query to attempt to retrieve an excessive amount of data. If the issue persists, sign out of Security Copilot, and then sign back in. Also, make sure that the authentication mechanism has the appropriate permissions within Splunk (ensure that the Splunk user you're authenticating as with bearer authentication, has permissions to invoke API calls). Finally, if you're connecting to Splunk enterprise, make sure that the SSL you're using for the REST API endpoint isn't using a self-signed certificate.

If you're creating a search job and the error is an HTTP status 400 with a status code of BadRequest, there are two potential causes:

- The keyword `search` is missing from the SPL query being sent to the Splunk API. This can be addressed by adding `Make sure the SPL query starts with the word "search".` to the prompt.
- The execution mode isn't specified or is incorrectly specified. This can be addressed by adding one of the following statements (or some flavor of it) to your prompt:
    - `Run this search in normal mode.`
    - `Run this search in oneshot mode.`

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

## Provide feedback

To provide feedback, contact the [Splunk partner engineering team](mailto:splunk-partnereng-sec-copilot@cisco.com).