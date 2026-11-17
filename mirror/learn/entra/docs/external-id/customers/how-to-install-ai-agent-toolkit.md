---
layout: Conceptual
title: Install the Microsoft Entra External ID agent toolkit - Microsoft Entra External ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/external-id/customers/how-to-install-ai-agent-toolkit
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://aka.ms/microsoftentraexternalid
author: csmulligan
ms.author: cmulligan
ms.service: entra-external-id
ms.subservice: external
manager: dougeby
description: Set up the Microsoft Entra External ID agent toolkit with your AI coding agent, then choose the skill for your app's task.
ms.topic: how-to
ms.date: 2026-11-11T00:00:00.0000000Z
ai-usage: ai-generated
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: 2c4a1838-ae69-dd7b-fdff-a28639397551
document_version_independent_id: 2c4a1838-ae69-dd7b-fdff-a28639397551
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/external-id/customers/how-to-install-ai-agent-toolkit.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: external-id/customers/how-to-install-ai-agent-toolkit
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/external-id/customers/how-to-install-ai-agent-toolkit.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c77bc83e-f0b0-4b63-836e-6630e606bf7c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/341fdab2-4964-4759-8241-f5820b012a47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b98eda1f-6af8-444f-bbfb-7f2366948cbc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cc1f92bb-c0d6-4d40-99ce-dabea3161a84
platformId: 112245b6-4887-3945-3efe-08888cf025b8
---

# Install the Microsoft Entra External ID agent toolkit - Microsoft Entra External ID | Microsoft Learn

Install the Microsoft Entra External ID agent toolkit for your AI coding agent so you can choose a skill for your app's task. Installation is shared across the toolkit; follow the guide for your chosen skill after setup.

**Applies to**: ![Green circle with a white check mark symbol that indicates the following content applies to external tenants.](../media/common/applies-to-yes.png) External tenants ([learn more](/en-us/entra/external-id/tenant-configurations))

## Prerequisites

- [Node.js](https://nodejs.org/en/download) 22.20 or later, only if you use the Skills CLI installation option.
- An AI coding agent, such as GitHub Copilot CLI, Claude Code, Codex, GitHub Copilot in Visual Studio Code, or Cursor.

## Install the toolkit

Choose the tab for your coding agent. The plugin installation options use the identifier `eeid-toolkit`. The Skills CLI option installs the toolkit's skills for agents such as GitHub Copilot in Visual Studio Code and Cursor.

# [GitHub Copilot CLI](#tab/github-copilot)
- Run these commands in your terminal:

    ```bash
    copilot plugin marketplace add AzureAD/ms-eeid-agent-toolkit
    copilot plugin install eeid-toolkit@ms-eeid-agent-toolkit
    ```

# [Claude Code](#tab/claude-code)
- Run these commands in a Claude Code session:

    ```text
    /plugin marketplace add AzureAD/ms-eeid-agent-toolkit
    /plugin install eeid-toolkit@ms-eeid-agent-toolkit
    ```

# [Codex](#tab/codex)
1. Run this command in your terminal:

    ```bash
    codex plugin marketplace add AzureAD/ms-eeid-agent-toolkit
    ```
2. Start Codex, enter `/plugins`, and install `eeid-toolkit` from the plugin list.

# [Other agents](#tab/other-agents)
Use the [Skills CLI](https://github.com/vercel-labs/skills) to install all the toolkit's skills for Cursor, GitHub Copilot in Visual Studio Code, and other agents.

- Run this command in your terminal:

    ```bash
    npx skills add AzureAD/ms-eeid-agent-toolkit --all
    ```

To install all the skills for a specific agent instead, use `--agent` with the agent's name. For example, use this optional form for Cursor:

```bash
npx skills add AzureAD/ms-eeid-agent-toolkit --skill '*' --agent cursor
```

---

## Choose your next skill

Select the guide for the task you want to complete. The guides describe skill-specific prerequisites and procedures without requiring you to repeat toolkit installation.

1. Review the [skills catalog](ai-agent-toolkit-overview#skills-catalog) and choose the skill for your task.
2. Follow the corresponding guide:

    - Use [`eeid-onboarding`](how-to-ai-agent-toolkit-onboard) to onboard an app to Microsoft Entra External ID.
    - Use [`eeid-native-auth-migrate-v2`](how-to-ai-agent-toolkit-migrate-native-auth-v2) to migrate an existing app from native authentication V1 to V2.