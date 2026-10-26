---
layout: Conceptual
title: Manage agent instances in Microsoft 365 admin center | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-agent-instances
breadcrumb_path: ../breadcrumb/agent365/toc.json
uhfHeaderId: MSDocsHeader-Agent365
feedback_system: Standard
permissioned-type: public
ms.service: agent-365
hideScope: false
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
ms.subservice: admin
description: Manage agent instances in Microsoft 365 admin center.
f1.keywords:
- NOCSH
ms.author: mkaur
author: mduelae
manager: tapanm
ms.date: 2025-11-21T00:00:00.0000000Z
ms.update-cycle: 180-days
audience: Admin
ms.topic: concept-article
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- m365copilot
- magic-ai-copilot
- operations-pod
search.appverid:
- BCS160
- MET150
- MOE150
locale: en-us
document_id: 9f1f277b-340a-c02e-6f58-363cdc9c75d1
document_version_independent_id: 9f1f277b-340a-c02e-6f58-363cdc9c75d1
original_content_git_url: https://github.com/MicrosoftDocs/agent365-docs-pr/blob/live/agent365-docs/admin/manage-agent-instances.md
site_name: Docs
depot_name: Learn.agent365
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage-agent-instances
moniker_range_name: 
monikers: []
item_type: Content
source_path: agent365-docs/admin/manage-agent-instances.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 482c067b-a947-c4c9-72a9-1f6cd313bc47
---

# Manage agent instances in Microsoft 365 admin center | Microsoft Learn

Once an admin or AI admin activates an agent, requestor can create instances of that agent. The Microsoft 365 admin center provides a centralized view for managing these instances:

- **Agent Registry** - Navigate to **Agents** &gt; **All agents** &gt; **Registry**. You can view agents with the **AI teammate** tag. You'll also see the number of instances that have been created for the specific agent.
- **Agent Details flyout** - Select an agent to open a flyout panel that displays the agent details.
- **Instance details** - Select **See details** to display a detailed list of all instances created under that agent. From this screen, administrators can perform the following actions:

    - **Manage individual instances** - Access and update settings for each instance.
    - **Review security and compliance status** - Ensure every instance meets organizational standards.
    - **Apply and customize licenses** - Assign licenses and configure options at the instance level.

This streamlined experience helps administrators maintain control, compliance, and flexibility across all agent instances.

Important

Certain features are available within Microsoft 365 admin center based on services licensed in your subscription. To view your licensed subscriptions in the [Microsoft 365 admin center](https://admin.cloud.microsoft/), select **Billing** &gt; **Licenses** &gt; **Subscriptions**. For more information, see [Plans and licensing](../overview#plans-and-licensing).

## Block agent instances

You can block or unblock agent instances for the entire organization using the same controls available for any other app in the Microsoft 365 admin center. Blocking an instance stops it and any actions it's performing.

To block or unblock an agent:

1. In the [Microsoft 365 admin center](https://admin.microsoft.com/), go to **Agents** &gt; **All Agents**.
2. Select an agent from the list. A panel opens.
3. Under the **Details** tab, select the **Instances** tab to see all instances created by that agent.
4. Select an instance and choose **Block**.

To restore functionality, the administrator can **Unblock** the instance at any time.

## Delete agent instances

Administrators and AI administrators can delete an instance from the Microsoft 365 admin center when it's no longer needed.

1. In the left navigation pane, select **Agents** &gt; **All agents**.
2. Filter the list by setting **Agent template** to **Yes**, and then select the agent. A panel opens where you can see the **Instances** tab.
3. Select the **Instances** tab to see all instances created by that agent.
4. Select the instance you want to delete, then select **Delete**.
5. Confirm the deletion when prompted.
6. Notify the owner of the deletion.
7. Remove or reassign Microsoft 365 licenses tied to the instance.
8. After 30 days, all instance accounts and data are permanently deleted. Audit logs are kept.
9. Once deleted, the instance no longer appears in the list.