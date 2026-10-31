---
layout: Conceptual
title: Connect to and manage ChatGPT Enterprise AI interactions in Microsoft Purview (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-chatgpt-interactions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to register ChatGPT Enterprise workspaces as a data source in Microsoft Purview to discover and govern AI interactions across your organization.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-19T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-map
ms.collection:
- purview-compliance
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: afd71880-25c4-b6f2-e50e-6bf365b713ac
document_version_independent_id: afd71880-25c4-b6f2-e50e-6bf365b713ac
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-chatgpt-interactions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-chatgpt-interactions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-chatgpt-interactions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 15ee698e-eaa1-4c79-d89c-c9f6a14085e0
---

# Connect to and manage ChatGPT Enterprise AI interactions in Microsoft Purview (preview) | Microsoft Learn

This article outlines how to register ChatGPT Enterprise workspaces as a data source in [Microsoft Purview](purview). This connector allows you to discover and govern interactions with ChatGPT Enterprise AI across your organization. Before you start, ensure you have the required permissions, billing configuration, and a ChatGPT Enterprise plan as described in the Prerequisites section.

Important

Any scans run are subject to the [new Microsoft Purview billing model](purview-billing-models). Be sure to [enable pay-as-you-go billing](purview-payg-consent-based-enablement) in your organization.

## Supported capabilities

This section summarizes which scan modes and governance features are supported for ChatGPT Enterprise sources.

Note

These features only apply to the enterprise version of ChatGPT. For more information on the available Purview features for the consumer version, see [Learn about Microsoft Purview Network Data Security](dlp-network-data-security-learn) and [Learn about Data Loss Prevention for Cloud Apps in Edge for Business](dlp-browser-dlp-learn).

Choose to scan all user interactions from the current date or pick a specific start date from past when configuring your scan.

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan | Classification | Labeling | Access Policy | Lineage | Data Sharing | Live view |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Yes | Yes | Yes | No | Yes | No | No | No | No | No |
|  |  |  |  |  |  |  |  |  |  |

When scanning ChatGPT Enterprise sources, Microsoft Purview supports:

- Extracting technical metadata, including:
    - Text prompts
    - Text responses

Note

Due to OpenAI's current API limitations, conversations are ingested 24 hours after they occur.

## Prerequisites

Make sure you have the following accounts, permissions, and configurations in place:

- An [Azure account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) with an active subscription.
- An active Enterprise [Microsoft Purview account](data-governance-free-version-upgrade-to-enterprise).

    - If you create a [classic Microsoft Purview instance](create-microsoft-purview-portal) for the first time in your organization, the instance is automatically upgraded to the enterprise version of Microsoft Purview.
- *Data Source Administrator* and *Data Reader*[Microsoft Purview Data Governance classic permissions](data-gov-classic-permissions) must be assigned to register a source and manage it in the Microsoft Purview governance portal.
- A ChatGPT Enterprise plan.
- Have [pay-as-you-go billing](purview-billing-models) enabled in your organization.
- Have a collection policy allowing for the ingestion of prompts and responses. There are two ways you can set up the policy:

    - Set up a [one-click policy to capture interactions for enterprise AI apps](dspm-for-ai-considerations#one-click-policies-from-data-security-posture-management-for-ai).
    - Set up a [collection policy](collection-policies-solution-overview) for enterprise AI apps in Microsoft Purview Data Loss Prevention.
- At present, scope for API key is not defined while creating the API key on the [OpenAI API Platform Portal](https://platform.openai.com/api-keys), but it is a prerequisite for Microsoft Purview to run a scan and fetch metadata. Complete the following steps to define the scope:

    - Send an email to `support@openai.com` with:

        1. The last 4 digits of the API key.
        2. The Key Name.
        3. The Created By Name.
        4. The requested scope (**read**, **delete**, or both). Microsoft Purview needs at least the **read** scope to run a scan.
    - The Open AI team will verify the key and grant the requested Compliance API scopes.
    - Administrators can now use this key or pass it to a partner for use with the Compliance API.

## Add permissions

Add the necessary permissions for other Microsoft Purview solutions used as part of this scanning process:

- [Azure Key Vault](/en-us/azure/key-vault/general/rbac-guide?tabs=azure-cli#azure-built-in-roles-for-key-vault-data-plane-operations)
- [Microsoft Purview AI hub](ai-microsoft-purview-permissions)
- [Microsoft Purview Communication Compliance](communication-compliance-permissions)
- [Microsoft Purview Data Lifecycle Management](get-started-with-data-lifecycle-management#permissions-for-retention-policies-and-retention-labels)
- [Microsoft Purview Data Map](data-map-domains-collections-manage#permissions-to-manage-domains-and-collections)
- [Microsoft Purview eDiscovery](edisc-permissions)
- [Microsoft Purview Insider Risk Management](insider-risk-management-permissions)
- [Microsoft Purview Records Management](get-started-with-records-management#permissions)

Microsoft Purview uses the OAuth 2.0 protocol for accessing ChatGPT Enterprise workspaces. To set up the credential, create an API key credential mapped to your Azure Key Vault when you configure the scan. For detailed steps, see the Scan section.

## Register a ChatGPT Enterprise workspace

This section describes how to register a ChatGPT Enterprise workspace in Microsoft Purview using the Microsoft Purview governance portal.

Complete the following steps to register:

1. Open the [Azure portal](https://portal.azure.com/) and complete the following steps:

    1. Search for *Key Vault* to create/manage the secret to use for this connector.
    2. Create a Key Vault.
    3. Grant role assignments to your Key Vault. Assign Key Vault administrators and Key Vault secret users for the required members. For other roles, check the Key Vault roles in the **Required permissions** section.
    4. Create a secret for your Key Vault.
    5. For your Key Vault, assign access policy.
2. Open the Microsoft Purview governance portal and complete the following steps:

    1. Search for Microsoft Purview accounts, select the account you want to use and select **Open Microsoft Purview governance portal**.
    2. Select **Data Map** in left navigation and select the *Data source*.
    3. Select **Register data source**.
    4. On register sources, select **ChatGPT Enterprise** and select **Continue**.
3. Open the ChatGPT Enterprise register source and complete the following steps:

    1. Enter a name for the data source within the catalog.
    2. Enter the WorkspaceID for your Enterprise workspace.
    3. Select a domain and collection.
    4. Select **Register**.
4. Open the Microsoft Purview portal and complete the following steps:

    1. Select **Source management** under **Data Map**, and select **Credentials**.
    2. Select **New**.
    3. Create and manage credentials for scans in Microsoft Purview Data Map
    4. Enter the name, description, and select the domain.
    5. For authentication method, select **API key**.
    6. For Key Vault connection, select the Azure key vault created for *ChatGPT Enterprise*.
    7. Enter the secret name and secret version.

## Scan a ChatGPT Enterprise workspace

Complete the following steps to scan a ChatGPT Enterprise workspace to automatically identify messages. For more information about scanning in general, see [Scans and ingestion in Microsoft Purview](concept-scans-and-ingestion).

1. Navigate to **Sources**.
2. Select the registered ChatGPT Enterprise workspace.
3. Select **New scan**and complete the following:
    1. **Name**: The name of the scan.
    2. **Capture data since**: Select if the scan should capture data from the current date of the new scan or choose a specific date from the past.
    3. **Credential**: Select the credential mapping to the correct Key Vault for this connector.
    4. **Domain**: Select a domain from the existing list or choose default domain.
    5. **Collection**: Select a collection from your domain.
4. Select **Test connection** to ensure the connection is established successfully. Select **Continue**.
5. Review your scan and select **Save** and **Run**.

For future scans, we recommend running an incremental scan. Avoid creating a new scan to avoid duplicate ingestion of data.

## View scan status and results

To view existing scans, complete the following steps:

1. Open the Microsoft Purview portal and select **Data Map**.
2. Select the data source. You can view a list of existing scans on that data source under **Recent scans**, or you can view all scans on the **Scans** tab.
3. Select the scan that has results you want to view. The pane shows you all the previous scans, along with the status and metrics for each scan.
4. Select the scan ID to check the scan details. During scanning, the organization is considered an asset, but isn't classified. The number of assets classified in the scan details are always one less than the number of assets ingested.
5. Review added data to Microsoft Purview in [Data Security Posture Management (DSPM) for AI](ai-microsoft-purview).
    1. View analytics for AI interactions, sensitive data, and insider risk in DSPM for AI reports.
    2. View the AI interactions for prompts and responses in Activity explorer.
    3. View the sensitive info type data identified in prompts and responses in Activity explorer.

Use other Microsoft Purview solutions with this data:

- [Communication Compliance](communication-compliance)
- [Data Lifecycle Management](data-lifecycle-management)
- [eDiscovery](edisc)
- [Insider Risk Management](insider-risk-management)
- [Records Management](records-management)

Find more information about [how Microsoft Purview solutions support AI interactions with ChatGPT Enterprise](ai-chatgpt-enterprise).