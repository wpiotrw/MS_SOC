---
layout: Conceptual
title: Get started with Power Automate integration | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-powerautomate-int-get-started
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1014
search.appverid:
- MET150
description: Use Power Automate integration to trigger custom workflows in data loss prevention rules.
ai-usage: ai-assisted
locale: en-us
document_id: bad16e74-27fe-6653-d927-8364cd2c288d
document_version_independent_id: bad16e74-27fe-6653-d927-8364cd2c288d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-powerautomate-int-get-started.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-powerautomate-int-get-started
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-powerautomate-int-get-started.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 57954f14-a7b8-9880-fb6a-0382cf59292e
---

# Get started with Power Automate integration | Microsoft Learn

Microsoft Power Automate is a workflow service that automates actions across applications and services. By using flows from templates or created manually, you can automate common tasks associated with these applications and services. Microsoft Purview Data Loss Prevention (DLP) can take various actions across locations on sensitive content identified as per DLP policies. With Power Automate integration, you can now trigger custom Power Automate workflows as a DLP rule action.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Before you begin

Before you start using Power Automate integration in Microsoft Purview DLP, read the following information on subscription, licensing, permissions, and supported locations.

### Subscriptions & licensing

Review the following subscription and licensing requirements for Microsoft Purview DLP and Power Automate.

#### Purview DLP

Power Automate integration in Microsoft Purview DLP is available for all existing DLP customers with no other Purview license requirements.

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

#### Power Automate

The access premium connectors when configuring custom flows you need a [Power Automate plan](/en-us/power-platform/admin/power-automate-licensing/types#compare-power-automate-plans). A Power Automate licenses is not needed to access the templates.

### Permissions

The following permissions apply when using Power Automate integration in Microsoft Purview DLP:

- There is no change to required role for DLP policy authoring in Microsoft Purview portal to use Power Automate integration as a DLP rule action.
- See [Get started with Power Automate](/en-us/power-automate/getting-started) for information about Power Automate roles.

### Supported locations in policy

Power Automate integration for DLP supports the following policy locations:

- Exchange emails
- Files in SharePoint Online & OneDrive
- Windows devices (24H2 and above)

## Create a workflow

Create a custom workflow using the DLP trigger provided as part of Microsoft Purview connector. You can create a workflow from any of the following experiences:

- [Power Automate portal](https://make.powerautomate.com)
- DLP rule authoring page: Add **Start a Power Automate workflow** as an action, and then create the workflow using a template or a custom workflow using DLP trigger.

You can select or update the Power Automate workflow linked to a DLP rule just like any other rule action.

### Use a template

The following Power Automate template is available to support process automation for DLP rule violations:

**Notify manager when a DLP policy is violated:** Some organizations might need to have immediate management notification when a user violates a policy. When the **Notify manager when a DLP policy is violated** flow is configured and selected, the manager of the violating user is sent an email message with the following information about the event:

- User name
- Policy name

You can customize the sender and add additional information by editing the workflow in Power Automate.

### Create a custom Power Automate flow

Some processes and workflows for your organization might not fit an available template. If no available template fits your organization's processes, you can create custom Power Automate flows to meet your specific needs. Power Automate flows are flexible and support extensive customization, but can require configuration to integrate with data loss prevention policies:

1. Create a flow that performs one or more tasks after a data loss prevention event. For details on how to create an automated flow, see [Create a flow in Power Automate](/en-us/power-automate/get-started-logic-flow).
2. Select the Microsoft Purview connector: Search for and select the Microsoft Purview connector. For more information on connectors, see: [Connector reference overview](/en-us/connectors/connector-reference/).
3. Choose data loss prevention triggers for your flow.
4. Choose from available Power Automate connectors for your flow.

### Share a Power Automate flow

By default, a Power Automate flow is only available to the user who created it. For other administrators to access and use a flow, the flow creator must share it. For information on how to share a flow, see: [Share a cloud flow](/en-us/power-automate/create-team-flows)

## Known issues and limitations

For files in SharePoint and OneDrive, Power Automate workflows are executed only for new or modified content. Preexisting files matching the rules don't trigger a flow.