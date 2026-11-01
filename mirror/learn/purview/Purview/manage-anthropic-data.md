---
layout: Conceptual
title: Set up a connector to manage Anthropic Claude data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/manage-anthropic-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how administrators can setup & use a native connector to manage data from Anthropic Claude.
f1.keywords:
- NOCSH
ms.author: v-reezaali
author: ReezaAli149
manager: laurawi
ms.date: 2026-05-21T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-connectors
search.appverid:
- MET150
ms.collection:
- purview-compliance
- data-connectors
ai-usage: ai-assisted
locale: en-us
document_id: 0ffd749e-d2c8-a28e-da3a-1e4a45135cc2
document_version_independent_id: 0ffd749e-d2c8-a28e-da3a-1e4a45135cc2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/manage-anthropic-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: manage-anthropic-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/manage-anthropic-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: addfaaa1-6b89-2800-d78c-cbaedff3c734
---

# Set up a connector to manage Anthropic Claude data | Microsoft Learn

Use a connector to manage the activity feed and chat conversations from Anthropic Claude. After you set up and configure the connector, it connects by using the Anthropic Compliance API. Microsoft Purview ingests the data, which begins showing up in Data Security Posture Management reports after about one day.

## Before you begin

Before you set up the Anthropic Claude data connector, make sure the following prerequisites are in place.

### Subscription

To learn more about Microsoft 365 tenant-level services licensing requirements, see [Microsoft 365 Security](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance).

### Anthropic Enterprise plan

Your organization must have an **Enterprise** plan from Anthropic. The primary owner must enable the Compliance API in **Organization Settings &gt; Data and Privacy**. On this page, you can also retrieve your Compliance Access Key by going to **Compliance access keys &gt; Create key**. You need this key in the next section where you set up the connector.

For more information about the Anthropic Compliance API, see [Access the Compliance API](https://support.claude.com/articles/13015708-access-the-compliance-api).

### Permissions

Assign the Data Connector Admin role to the user who creates the Anthropic Claude data connector in the Microsoft Purview portal. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).

## Set up the Anthropic Claude data connector

To set up the Anthropic Claude data connector, perform the following steps.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **All connectors**.
4. From the list, select **Anthropic Claude**.
5. On the **Anthropic Claude** product description page, select **Add connector**.
6. On the **Terms of service** page, review and select **Accept**.
7. On the **Connector name** page, enter a descriptive name for the connector and select **Next**.
8. On the **Authentication** page, enter the following information:

    - **API Key**: Enter the Compliance API key generated from your Anthropic Organization Settings. Select **Validate connection**.
    - **Organization IDs**: Select your Anthropic organization identifier.
    - **API Base URL**: Confirm the Anthropic API base URL (the default is `https://api.anthropic.com`).
9. Select **Next**.
10. On the **Data scope** page, select the data types to import:

    - **Activity Feed** — Authentication events, chat interactions, file uploads, admin actions, and compliance audit events across Claude.ai, Console, and API. *(Scope: read:compliance\_activities)*
    - **Chat Conversations** — Full message history between users and Claude, including user prompts, AI responses, and metadata for DSPM analysis. *(Scope: read:compliance\_user\_data)*
    - Select a **Sync frequency** to determine how often the connector pulls new data from the Anthropic Compliance API.
11. Select **Next**.
12. On the **Review your connector** page, verify your connector configuration and select **Finish**.

After you create the connector, you can see the following data:

- **Ongoing sync**: View new activities and chats that the connector imports based on your selected frequency.
- **DSPM**: View Claude interaction data in the DSPM Dashboard and Activity Explorer.
- **Monitoring**: View connector health and sync status in **Data connectors** &gt; **My connectors**.