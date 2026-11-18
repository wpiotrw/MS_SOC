---
layout: Conceptual
title: Monitor and disconnect Azure Bastion sessions in PIM - Microsoft Entra ID Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-manage-bastion-sessions
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: tamimsangrar
ms.author: tamimsangrar
ms.service: entra-id-governance
ms.subservice: privileged-identity-management
manager: dougeby
description: Learn how to find active Azure Bastion sessions in Microsoft Entra Privileged Identity Management and disconnect a selected session.
ms.topic: how-to
ms.date: 2026-11-17T00:00:00.0000000Z
ms.custom: msecd-doc-authoring-1032
ai-usage: ai-generated
locale: en-us
document_id: c61bd4c5-8cd3-1513-a14a-b2b6ca7558a8
document_version_independent_id: c61bd4c5-8cd3-1513-a14a-b2b6ca7558a8
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/id-governance/privileged-identity-management/pim-manage-bastion-sessions.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: id-governance/privileged-identity-management/pim-manage-bastion-sessions
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/id-governance/privileged-identity-management/pim-manage-bastion-sessions.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7c01134-b8f3-438c-822d-13471e513908
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac4b7417-d4c2-43d4-94bf-f22fa1416b34
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://authoring-docs-microsoft.poolparty.biz/devrel/82fff6b2-939d-4e9a-8f9c-d1c41a59749b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68876bab-7da4-4e70-b295-395b3a255a1f
platformId: beddb504-b76c-943d-2f09-442410e29d22
---

# Monitor and disconnect Azure Bastion sessions in PIM - Microsoft Entra ID Governance | Microsoft Learn

Use Microsoft Entra Privileged Identity Management (PIM) to find active Azure Bastion sessions in an Azure subscription or resource group and disconnect a selected session.

Session Management in PIM is in preview and supports RDP and SSH sessions.

## Prerequisites

- Microsoft Entra ID Governance licensing is required for Session Management. See [Microsoft Entra ID Governance licensing fundamentals](../licensing-fundamentals).
- A deployed Azure Bastion host and an active session in the scope you want to manage. For deployment, see [Deploy Azure Bastion](/en-us/azure/bastion/quickstart-host-portal).
- The **Network Contributor** role on the resource group containing the Azure Bastion host, for viewing and disconnecting sessions.

## Find and disconnect a session

Find the session before you disconnect it so that you act on the intended user and Azure Virtual Machine.

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Open **Privileged Identity Management**, select **Azure resources**, and select the Azure subscription or resource group you want to manage.
3. Under **Activity**, select **Session Management (Preview)**.
4. Search for the user, Azure Virtual Machine, Bastion host, protocol, or IP address.

    [![Screenshot of Session Management with an active SSH session selected and the Disconnect action available.](media/pim-manage-bastion-sessions/session-management-active-session.png)](media/pim-manage-bastion-sessions/session-management-active-session.png#lightbox)
5. Select the session, and then select **Disconnect**.

    In the confirmation dialog, select **Disconnect** to confirm, or **Cancel** to keep the session connected.

    After a successful disconnection, the session automatically disappears from the list.
6. Optional: Select **Refresh** to reload the session list. Use **Load more** to scan additional hosts.

Selecting **Disconnect** ends the selected Azure Bastion connection without deactivating the user’s role assignments. The user can reconnect if they still meet the connection requirements. For more information, see [Azure Bastion session monitoring and management](/en-us/azure/bastion/session-monitoring).