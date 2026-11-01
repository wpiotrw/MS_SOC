---
layout: Conceptual
title: All Credential Types entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-all-creds
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-10T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: All Credential Types sensitive information type entity definition.
locale: en-us
document_id: c21614ef-8edf-c9ef-94e5-1126406515be
document_version_independent_id: c21614ef-8edf-c9ef-94e5-1126406515be
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-all-creds.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-all-creds
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-all-creds.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/9bdc1705-9b40-49d6-8377-caa0b71fda66
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/686ed158-d915-41e9-9760-efa46ba88f6d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 349024ca-ffc8-7548-f0f3-302b483a9a43
---

# All Credential Types entity definition | Microsoft Learn

"All credentials" is a bundled-entity sensitive information type (SIT). It detects credentials from all supported services and environments, which include Amazon, Azure, GitHub, Google, Microsoft general, Slack and more.

Important

Because the **All Credetials** SIT is a bundled SIT, it ***does not*** contain any keywords. The keywords that it detects are based on the individual SITs it contains. Refer to the individual SITs for keyword information.

For information about implementing bundled SITs, see [Learn about named entities](sit-named-entities-learn).

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a bundled SIT in an endpoint DLP policy. This requirement is specific to the combination of bundled SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

Various

## Pattern

Various

## Checksum

No

## Keyword Highlighting

Not supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Description

The All credentials SIT is a bundled SIT that scans for individual credential types. This includes checksum evaluated values and keyword/pattern combinations. The All credential entity scans for any of the underlying credential information type checksums and/or patterns are detected in a document.

## Contains

This bundled entity SIT contains these individual SITs:

- [Amazon S3 Client Secret Access Key](sit-defn-amazon-s3-client-secret-access-key)
- [ASP.NET Machine Key](sit-defn-asp-net-machine-key)
- [Microsoft Entra Client Access Token](sit-defn-azure-ad-client-access-token)
- [Microsoft Entra Client Secret](sit-defn-azure-ad-client-secret)
- [Microsoft Entra user Credentials](sit-defn-azure-ad-user-credentials)
- [Azure App Service Deployment Password](sit-defn-azure-app-service-deployment-password)
- [Azure Batch Shared Access Key](sit-defn-azure-batch-shared-access-key)
- [Azure Bot Framework Secret Key](sit-defn-azure-bot-framework-secret-key)
- [Azure Bot Service App Secret](sit-defn-azure-bot-service-app-secret)
- [Azure Cognitive Search API Key](sit-defn-azure-cognitive-search-api-key)
- [Azure Cognitive Service Key](sit-defn-azure-cognitive-service-key)
- [Azure Container Registry Access Key](sit-defn-azure-container-registry-access-key)
- [Azure COSMOS DB Account Access Key](sit-defn-azure-cosmos-db-account-access-key)
- [Azure Databricks Personal Access Token](sit-defn-azure-databricks-personal-access-token)
- [Azure DevOps App Secret](sit-defn-azure-devops-app-secret)
- [Azure DevOps Personal Access Token](sit-defn-azure-devops-personal-access-token)
- [Azure EventGrid Access Key](sit-defn-azure-eventgrid-access-key)
- [Azure Function Master / API Key](sit-defn-azure-function-master-api-key)
- [Azure IoT Shared Access Key](sit-defn-azure-iot-shared-access-key)
- [Azure Logic App Shared Access Signature](sit-defn-azure-logic-app-shared-access-signature)
- [Azure Machine Learning Web Service API Key](sit-defn-azure-machine-learning-web-service-api-key)
- [Azure Maps Subscription Key](sit-defn-azure-maps-subscription-key)
- [Azure Redis Cache Connection String Password](sit-defn-azure-redis-cache-connection-string-password)
- [Azure Service Bus Shared Access Signature](sit-defn-azure-service-bus-shared-access-signature)
- [Azure Shared Access Key / Web Hook Token](sit-defn-azure-shared-access-key-web-hook-token)
- [Azure SignalR Access Key](sit-defn-azure-signalr-access-key)
- [Azure SQL Connection String](sit-defn-azure-sql-connection-string)
- [Azure Storage Account Access Key](sit-defn-azure-storage-account-access-key)
- [Azure Storage Account Shared Access Signature](sit-defn-azure-storage-account-shared-access-signature)
- [Azure Storage Account Shared Access Signature for High Risk Resources](sit-defn-azure-storage-account-shared-access-signature-high-risk-resources)
- [Azure Subscription Management Certificate](sit-defn-azure-subscription-management-certificate)
- [Client Secret / API Key](sit-defn-client-secret-api-key)
- [General Password](sit-defn-general-password)

Tip

General Password detects password related keywords in English only.

- [General Symmetric Key](sit-defn-general-symmetric-key)
- [GitHub Personal Access Token](sit-defn-github-personal-access-token)
- [Google API key](sit-defn-google-api-key)
- [Http Authorization Header](sit-defn-http-authorization-header)
- [Microsoft Bing Maps Key](sit-defn-google-api-key)
- [Slack Access Token](sit-defn-slack-access-token)
- [User Login Credentials](sit-defn-user-login-credentials)
- [X.509 Certificate Private Key](sit-defn-x-509-certificate-private-key)

## Supported languages

- English
- Bulgarian
- Chinese
- Croatian
- Czech
- Danish
- Estonian
- Finnish
- French
- German
- Hungarian
- Icelandic
- Irish
- Italian
- Japanese
- Latvian
- Lithuanian
- Maltese
- Dutch
- Norwegian
- Polish
- Portuguese
- Romanian
- Slovak
- Slovenian
- Spanish
- Swedish
- Turkish