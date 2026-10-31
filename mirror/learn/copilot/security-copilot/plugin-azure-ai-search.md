---
layout: Conceptual
title: Azure AI Search in Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-azure-ai-search
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn to use the Azure AI Search plugin to connect org knowledge base content into Copilot.
ms.date: 2025-12-17T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: concept-article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom:
- cx-ti
- cx-cop
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: 7641be63-d533-6171-cf64-1e1e821783c5
document_version_independent_id: 7641be63-d533-6171-cf64-1e1e821783c5
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-azure-ai-search.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-azure-ai-search
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-azure-ai-search.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/45da903a-8cff-40ca-99bf-9237f80d6982
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7af51462-ed96-4b66-aefd-ea77337d1b96
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: c767aa16-1f64-4aa5-b8c7-3d215e544e39
---

# Azure AI Search in Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

Azure AI Search is a service that allows you to search, retrieve information, and extract insights from your content at scale and securely. It is commonly used for document search, data exploration, and chat-style Copilot apps over proprietary data.

There are two primary workloads in Azure AI Search: indexing and querying. Indexing loads your content into the search service and makes it searchable, while querying allows you to search the content from your index.

The Microsoft Security Copilot integration for Azure AI Search allows you to connect to one of your Azure AI Search indexes from within Copilot, allowing you to reference your content in Copilot to generate contextualized, relevant, and specific responses.

## Requirements

To use the Azure AI Search plugin in Copilot, make sure that the Azure AI Search index that you would like to connect to Copilot is configured as follows:

- The text field must be searchable.
- The title field must be filterable.
- The vector field must use **text-embedding-ada-002**.

One way you can get started with setting up an index in the required way is to use integrated vectorization. To get started with the integrated vectorization wizard, see [Quickstart: Integrated vectorization (preview)](/en-us/azure/search/search-get-started-portal-import-vectors).

These steps are required to get your index ready for integration into Copilot.

## Connect Azure AI Search to Copilot

To create the connection:

1. Open Copilot, making sure you're authenticated.
2. Select the Copilot sources icon ![Screenshot of sources icon.](media/sources-icon.png) in the prompt bar.
3. Go to **Microsoft &gt; Azure AI search** and select **Set up**.

    [![Screenshot of manage plugins dialog box.](media/azure-ai-search-manage.png)](media/azure-ai-search-manage.png#lightbox)
4. In **Azure AI Search settings**, enter the following information in the corresponding fields:

    - **Configuration level** - specify the parameters if it applies only to you or for everyone in the workspace
    - **Azure AI Search instance** – the name of your search instance
    - **Index** – the name of the index within your instance to search
    - **Vector** – the name of the field label in the index containing the vector of embeddings
    - **Text** – the name of the field label in the index containing the text to search
    - **Title** – the title of each document to display as a source
    - **Value** – the API key for authentication

    Note

    Using private links are not supported.

    [![Screenshot of Azure AI Search settings.](media/copilot-security-azure-ai-search-settings.png)](media/copilot-security-azure-ai-search-settings.png#lightbox)

    You can find the required information for the plugin setup in your Azure AI Search page in the Azure portal.
5. Select **Save** to complete the setup.
6. Close the **Azure AI Search settings** window.

Note

Currently, Copilot does not validate your credentials when you save your settings. If they are not correct, you will see an error later when Copilot attempts to run the Azure AI Search plugin.

This plugin isn't exclusive to knowledge base scenarios, but it's well-suited for this. The indexing and vectorizing capabilities provided by Azure AI Search are what enable apps like Copilot to search through and retrieve information across large volumes of data and content.

For more information about prompting a knowledge base in Copilot, read [Prompting a knowledge base connected using Azure AI Search](connect-org-kb#prompting-for-a-knowledge-base-connected-using-azure-ai-search).

## Known limitations

- Only one index at a time can be connected using the plugin. To query a different index, you need to update the plugin settings.
- The plugin supports hybrid search (keyword and vector search), so it can only support queries on indexes that were configured according to the required settings in [Requirements](plugin-azure-ai-search#requirements).
- To invoke the plugin, you need to explicitly mention "Azure AI Search" in the prompt.
- Copilot displays the titles of the referenced documents from the index, but they aren't hyperlinked.