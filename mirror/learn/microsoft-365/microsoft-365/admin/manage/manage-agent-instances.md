---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Manage agent instances in Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-agent-instances?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
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
ms.service: microsoft-365-copilot
ms.subservice: agent-management
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
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
search.appverid:
- BCS160
- MET150
- MOE150
locale: en-us
document_id: b5cc9749-90fe-4cb2-d612-8fe768a73cca
document_version_independent_id: b5cc9749-90fe-4cb2-d612-8fe768a73cca
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/manage-agent-instances.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/manage-agent-instances
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/manage-agent-instances.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: f2d8c53d-7112-fb73-570d-ff0dc7d1d165
---

# Manage agent instances in Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn

Once an admin or AI admin activates an agent, requestor can create instances of that agent. The Microsoft 365 admin center provides a centralized view for managing these instances:

- **Agent Registry** - Navigate to **Agents** &gt; **All agents** &gt; **Registry**. You can view agents with the **AI teammate** tag. You'll also see the number of instances that have been created for the specific agent.
- **Agent Details flyout** - Select an agent to open a flyout panel that displays the agent details.
- **Instance details** - Select **See details** to display a detailed list of all instances created under that agent. From this screen, administrators can perform the following actions:

    - **Manage individual instances** - Access and update settings for each instance.
    - **Review security and compliance status** - Ensure every instance meets organizational standards.
    - **Apply and customize licenses** - Assign licenses and configure options at the instance level.

This streamlined experience helps administrators maintain control, compliance, and flexibility across all agent instances.

Important

Certain features are available within Microsoft 365 admin center based on services licensed in your subscription. To view your licensed subscriptions in the [Microsoft 365 admin center](https://admin.cloud.microsoft/), select **Billing** &gt; **Licenses** &gt; **Subscriptions**. For more information, see [Plans and licensing](/en-us/microsoft-agent-365/overview#plans-and-licensing).

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