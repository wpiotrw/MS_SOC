---
layout: Conceptual
title: Settings overview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/settings-overview
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: This page provides an overview for all W365 settings including Cloud PC configurations, Windows App settings, and User settings.
author: rachellelcheung
ms.author: racheun
ms.service: windows-365
ms.topic: overview
ms.date: 2026-01-27T00:00:00.0000000Z
ms.subservice: windows-365-enterprise
ai-usage: ai-assisted
locale: en-us
document_id: b2125f80-0fb0-cc86-88bc-95981e573510
document_version_independent_id: b2125f80-0fb0-cc86-88bc-95981e573510
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/settings-overview.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/settings-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/settings-overview.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cd440f3c-1b78-40a7-97ba-aa00a1d79df7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c828f7e0-89b4-459c-9bae-d7ab1c4bd9ad
platformId: dbc57ce8-00d2-789a-66e1-76d14a4be656
---

# Settings overview | Microsoft Learn

Cloud PC Settings is a central place for IT administrators to configure and manage settings for Cloud PCs. These settings are dynamic and can be updated throughout the Cloud PC lifecycle.

Windows 365 supports four types of settings objects:

- [Cloud PC configurations](/en-us/windows-365/enterprise/cloud-pc-configurations)
- [Windows App settings](/en-us/windows-365/enterprise/windows-app-settings)
- [Remote connection experience](/en-us/windows-365/enterprise/remote-connection-experience)
- [User settings](/en-us/windows-365/enterprise/assign-users-as-local-admin)

Each settings object serves a specific purpose and includes one or more settings features. For most settings, you can choose from these options:

- **Not configured (default)**: No value is set, and the setting isn’t explicitly enabled or disabled.
- **Enabled**: Turns the setting on.
- **Disabled**: Turns the setting off.

## Rank

Each settings policy is assigned a unique global rank, where **1** is the highest priority. By default, a new policy is assigned as the lowest rank.

If two settings policies include conflicting settings values, the policy with the higher rank takes precedence over the lower-rank policy. Conflict resolution applies independently to each setting and considers only settings that are configured. **Not configured** means the policy doesn't manage that setting; it doesn't assign a default value or participate in conflict resolution.

Administrators can rerank settings policies to determine which policy takes precedence when conflicting settings are configured. Policies can be reranked by clicking on the **Rerank policies button** and:

1. changing their rank,
2. using drag-and-drop controls, or
3. moving policies up and down the list.

Note

For AI-enabled features, the most secure policy will always take precedence regardless of the priority number.