---
layout: Conceptual
title: Censys and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-censys
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the Censys plugin with Microsoft Security Copilot.
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
document_id: 6bd3ee04-e750-0db1-d649-99ce404ecc36
document_version_independent_id: 6bd3ee04-e750-0db1-d649-99ce404ecc36
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-censys.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-censys
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-censys.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: cbcb6981-eb44-55d3-3178-9ece3f73a3ab
---

# Censys and Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product that can be substantially modified before commercial release. Microsoft makes no warranties, express or implied, with respect to the information provided here.

This plugin allows Security Copilot users to enrich investigations using threat intelligence from the Censys Platform. Currently the following functionalities are supported:

- Generating and executing Censys queries using natural language
- Searching the Censys Global Index
- Aggregating search results by specific fields
- Retrieving detailed information about IP addresses
- Looking up certificate information by SHA256 hash
- Getting web property information by domain and port

## **Prerequisites**

- Access to the Censys Platform account
- A Personal Access Token (PAT) from Censys
- Your Censys Organization ID

Note

This article contains information about non-Microsoft plugins. This guidance is provided to help complete integration scenarios. However, Microsoft doesn't provide troubleshooting support for non-Microsoft plugins. Contact the vendor for support.

## Know before you begin

Integration with Security Copilot works with a combination of a Personal Access Token (PAT) and Organization ID. You need to take the following steps before using the plugin.

### Authentication Setup

1. Sign in to your [Censys Account](https://accounts.censys.io/settings).
2. Navigate to the **Personal Access Tokens** tab and select **Create New Token**.
3. Give your token a descriptive name (for example, "Security Copilot Token") and select **Create**.
4. Locate your Organization ID from the Censys Platform URL (appears as `?org=ORG_ID`).
5. Combine your PAT and Organization ID with a colon separator: `PAT:ORG_ID`

### Plugin Configuration

1. When you're asked to set up authentication, enter the combined PAT and Organization ID in the following format into the **Value** field:

```plain
PAT:ORG_ID
```

1. Select **Save** to complete setup.

## Available Skills

The Censys Plugin for Microsoft Security Copilot exposes the following skills:

- Query Generation
    - Creating Censys queries from natural language
    - Converting user intent into CenQL syntax
- Global Index Search
    - Executing queries against the Censys database
    - Retrieving and formatting search results
- Data Aggregation
    - Aggregating results by specified fields
    - Generating statistical summaries
- Asset Information
    - IP address lookups
    - Certificate information retrieval
    - Web property analysis

With the Censys plugin for Microsoft Security Copilot, you can invoke interactions with Censys in the context of a natural conversation. Here's an example:

1. A user can ask about specific IP addresses or domains of interest
2. The user can then use follow-up prompts such as "What other assets are associated with this IP?"
3. The user can further investigate by asking for aggregated data about similar assets or certificates

## Example Prompts

| Skill | Prompt |
| --- | --- |
| Generate Query | `Generate a Censys query to find all the nginx servers` |
| Search Global Index | `Query Censys for host.location.country: "Netherlands"` |
| Aggregate Results | `What are the top 10 ASNs in the world?` |
| IP Lookup | `What does Censys know about IP 1.1.1.1?` |
| Multiple IP Lookup | `Get information about 1.1.1.1 and 2.2.2.2` |
| Certificate Lookup | `Get the certificate 14e641e9f3eb7cf4bdf6b0bc364bd8529feafdb78904c45a49ce25d7daecc824` |
| Web Property Lookup | `Get the web property google.com:443` |
| Multiple Properties | `Look up google.com:443 and censys.io:443` |

Microsoft Security Copilot maintains context between queries, allowing for natural conversation flows. For example, after looking up an IP address, you can ask follow-up questions about related certificates or web properties without needing to specify the IP again.

## Troubleshoot the Censys plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred*, check:

1. Ensure the plugin is turned on
2. Verify your PAT and Organization ID are correctly formatted
3. Check that your PAT hasn't expired
4. Confirm you have sufficient API credits in your Censys account
5. If issues persist, sign out of Security Copilot and sign back in

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set:

- Ensure you're using supported prompt formats
- Try using direct skill invocation with "/"
- Check if other plugins might be intercepting similar queries

## Provide feedback

To provide feedback, contact the [Censys team](mailto:support+sec-copilot@censys.com).