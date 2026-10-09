---
layout: Conceptual
title: Microsoft Copilot enhanced personalization control - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/control-enhanced-personalization-privacy
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: Ross-GH
ms.author: rossav
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: microsoft-365-copilot
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: overview
description: Looking to learn about Microsoft Copilot enhanced personalization? Learn what it is, and how to control it respecting your privacy through Microsoft Learn.
ms.date: 2025-04-03T00:00:00.0000000Z
locale: en-us
document_id: 495bab2a-b5d8-98b1-15b1-0d5b9ad82130
document_version_independent_id: 495bab2a-b5d8-98b1-15b1-0d5b9ad82130
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/control-enhanced-personalization-privacy.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: control-enhanced-personalization-privacy
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/control-enhanced-personalization-privacy.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 257f1a9f-5665-0fe8-5165-43599f710b96
---

# Microsoft Copilot enhanced personalization control - Microsoft Graph | Microsoft Learn

Microsoft Copilot can become personalized to each user, aiding them in their day-to-day tasks by understanding their work knowledge on an individual level, including from their communications, Microsoft 365 work data, usage signals, and profile information. Tenant administrators, such as the Global Administrator role, and users through requests to their tenant administrators, use the enhanced personalization control to manage this personalization.

Understand how Microsoft Copilot achieves greater personalization through various features when enhanced personalization is enabled. How your privacy is maintained, and how to control the use of enhanced personalization for Microsoft Copilot.

## Data processing scenario

To provide a more personalized experience with Microsoft Copilot. Microsoft, with consent provided from enabling this control, uses a user's private communication data connected to Microsoft 365, such as Microsoft Teams chats, Outlook emails, Microsoft transcripts, Microsoft 365 usage data, user profile information such as role, and data from connectors. This data is used solely to make the individual user's tools more efficient and personalized to them. It's important to note that this information remains confidential and is not shared with other users, ensuring user privacy. The option to disable all linked features for the tenant or a group of users through this scenario control is available anytime, causing Microsoft to cease using a user's data for this purpose. In some cases, this renders a feature disabled for use, such as Copilot memory, which is dependent on this data processing scenario.

## Features controlled by enhanced personalization

**[Copilot memory](/en-us/microsoft-365/copilot/copilot-personalization-memory)** - Memory and personalization make Copilot personalized to you and your work. Copilot learns how you work and understands your needs and preferences through your chats, job profile, custom instructions, and more.

**Personalized recommendations** - Microsoft Copilot users who have Copilot memory enabled can discover capabilities through personalized recommendations tailored to their role, experience level, and previous interactions. Examples include recommending relevant Copilot capabilities based on a user’s role, adjusting recommendations to the user’s experience level, and using previous Copilot interactions to reduce generic or repetitive recommendations.