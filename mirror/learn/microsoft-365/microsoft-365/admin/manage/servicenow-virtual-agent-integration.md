---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Integrate Microsoft 365 with ServiceNow Virtual Agent - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/servicenow-virtual-agent-integration?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2025-04-28T00:00:00.0000000Z
audience: Admin
ms.topic: integration
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_TOC
- operations-pod
ms.custom: AdminSurgePortfolio
ROBOTS: NOINDEX, NOFOLLOW
search.appverid:
- MET150
description: Configure support integration to test and provide the Microsoft 365 support integration team with feedback.
locale: en-us
document_id: d549e898-9d1f-d844-0a3e-0181dc04374d
document_version_independent_id: d549e898-9d1f-d844-0a3e-0181dc04374d
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/servicenow-virtual-agent-integration.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/servicenow-virtual-agent-integration
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/servicenow-virtual-agent-integration.md
platformId: 6f70c487-63ec-e390-dc90-56409ec34e38
---

# Integrate Microsoft 365 with ServiceNow Virtual Agent - Microsoft 365 admin | Microsoft Learn

Important

Microsoft 365 support integration with ServiceNow is retired, and the service will be completely shut down on May 30, 2025. If you installed the integration, take necessary steps to remove it before May 30, 2025.

When you configure the Microsoft 365 support integration app to work with ServiceNow Virtual Agent, you access the self-help created by Microsoft 365 product teams through two different user experiences:

- Microsoft 365 step-by-step and walk-through solutions.

    [![Quick Insights.](../../media/servicenow-guide/servicenow-support-integration-2.png)](../../media/servicenow-guide/servicenow-support-integration-1.png#lightbox)[![Quick Insights.](../../media/servicenow-guide/servicenow-support-integration-2b.png)](../../media/servicenow-guide/servicenow-support-integration-2b.png#lightbox)
- Top web search results from Microsoft 365 knowledge base articles.

    [![Knowledge base article search results.](../../media/servicenow-guide/servicenow-support-integration-1.png)](../../media/servicenow-guide/servicenow-support-integration-1.png#lightbox)

## Before you begin

- Enable Virtual Agent in ServiceNow. For details, see [Activate Virtual Agent](https://docs.servicenow.com/bundle/quebec-now-intelligence/page/administer/virtual-agent/task/activate-virtual-agent.html).
- Install and complete the setup of the Microsoft 365 support integration app from the ServiceNow Store.
- Minimum version of ServiceNow: Rome.
- Role required: ServiceNow admin or virtual\_agent\_admin.

## Configure Microsoft 365 support integration to work with ServiceNow Virtual Agent

### Standalone fallback topic

Set Microsoft 365 Support as your fallback topic. For details, see [Configure a Virtual Agent chat experience](https://docs.servicenow.com/bundle/quebec-now-intelligence/page/administer/virtual-agent/task/configure-default-chat-experience.html).

[![Set default chat experience fallback topic.](../../media/servicenow-guide/servicenow-support-integration-3.png)](../../media/servicenow-guide/servicenow-support-integration-3.png#lightbox)

### Topic blocks

If you don't have any topic created, you can use the standalone fallback topic as above or [create your own virtual agent topic](https://docs.servicenow.com/bundle/rome-now-intelligence/page/administer/virtual-agent/task/create-virtual-agent-topic.html).

Follow these steps to add the Microsoft 365 Support topic block:

1. Under **Utilities**, select **Topic Block**, and add it to your flow.

    [![Add a topic block to your flow.](../../media/servicenow-guide/servicenow-topic-block-1.png)](../../media/servicenow-guide/servicenow-topic-block-1.png#lightbox)
2. Under **Topic Block Properties**, choose **Microsoft 365 Support Topic Block**.

    [![Choose the Support Topic Block property.](../../media/servicenow-guide/servicenow-topic-block-2.png)](../../media/servicenow-guide/servicenow-topic-block-2.png#lightbox)
3. A Microsoft 365 Support Topic Block accesses input text in this order:

    a. Checks for input variable. If the input variable is not empty, fetches the results for the input variable.

    [![Fetches the results for input variable.](../../media/servicenow-guide/servicenow-topic-block-3.png)](../../media/servicenow-guide/servicenow-topic-block-3.png#lightbox)

    b. If the input variable is empty, checks for text entered by the user in the chat window and fetches results for the text.

    [![Checks for text entered in the chat window.](../../media/servicenow-guide/servicenow-topic-block-4.png)](../../media/servicenow-guide/servicenow-topic-block-4.png#lightbox)

    c. If the user didn't enter text, asks the user to enter text to fetch results.

    [![Checks for text entered in the chat window.](../../media/servicenow-guide/servicenow-topic-block-5.png)](../../media/servicenow-guide/servicenow-topic-block-5.png#lightbox)
4. Microsoft 365 Support Topic Block provides an output variable, which is the user's feedback for the results.

    a. Output variable name: m365\_success b. Possible output variable values: YES/NO

    [![Output variable name and values.](../../media/servicenow-guide/servicenow-topic-block-6.png)](../../media/servicenow-guide/servicenow-topic-block-6.png#lightbox)