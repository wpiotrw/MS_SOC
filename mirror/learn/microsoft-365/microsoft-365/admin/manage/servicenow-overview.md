---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft 365 support integration with ServiceNow configuration overview - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/servicenow-overview?view=o365-worldwide
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
description: Scoped Certified application installation and configuration guide for ServiceNow.
locale: en-us
document_id: 51519dd1-c3d8-ee3c-96ec-640ac4c761ab
document_version_independent_id: 51519dd1-c3d8-ee3c-96ec-640ac4c761ab
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/servicenow-overview.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/servicenow-overview
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/servicenow-overview.md
platformId: 9aedf167-4a16-acf5-63a4-7231b9cefdce
---

# Microsoft 365 support integration with ServiceNow configuration overview - Microsoft 365 admin | Microsoft Learn

Important

Microsoft 365 support integration with ServiceNow is retired, and the service will be completely shut down on May 30, 2025. If you installed the integration, take necessary steps to remove it before May 30, 2025.

The following article applies to the Microsoft 365 support integration app with a minimum version of **2.0.0**.

For version 1.0.11 and earlier, see [Microsoft 365 support integration overview v1](servicenow-overview-v1).

Microsoft 365 support integration enables you to integrate Microsoft 365 help, support, and service health with your ServiceNow instances. You can research Microsoft known and reported issues, resolve incidents, complete tasks by using Microsoft recommended solutions, and, if necessary, escalate to Microsoft human-assisted support.

For the Microsoft 365 support integration app, go to the [ServiceNow Store](https://store.servicenow.com/sn_appstore_store.do#!/store/application/6d05c93f1b7784507ddd4227cc4bcb9f).

Note

This app is not supported in regulated or restricted environments.

This app is only supported in English.

## Key features

These are the key features you'll get with the Microsoft 365 support integration app in ServiceNow:

- Service Health Incidents: Information about known Microsoft service health incidents, including user impact, scope, status, and next expected update. Using machine learning, ServiceNow incidents are matched to Microsoft service health incidents based on the short description field.

    [![Service Health Incidents description field.](../../media/servicenow-guide/servicenow_service_health_incidents.png)](../../media/servicenow-guide/servicenow_service_health_incidents.png#lightbox)
- Recommended solutions: Descriptions of tasks and incidents are used to recommend precise targeted solutions and relevant articles from Microsoft powered by machine learning. You can also use Search to find other solutions, if needed.

    [![Recommended solutions description field.](../../media/servicenow-guide/servicenow_recommended_articles.png)](../../media/servicenow-guide/servicenow_recommended_articles.png#lightbox)
- Microsoft service request: Escalate issues to Microsoft support agents and receive status updates for your request. With an updated workflow, you can now create a service request by adding your preferred title, description, and contact information similar to what is found in the Microsoft 365 admin portal.

    [![Screenshot that shows the recommended solutions description field.](../../media/servicenow-guide/snow_escalation.png)](../../media/servicenow-guide/snow_escalation.png#lightbox)

    [![Screenshot that shows the recommended solutions description field.](../../media/servicenow-guide/snow_escalation2.png)](../../media/servicenow-guide/snow_escalation2.png#lightbox)

## Prerequisites

### Permissions requirements

To proceed with this guide, make sure that the following permissions are available and configured for your environments during the entire process:

- Microsoft Entra admin who can create Microsoft Entra Applications
- ServiceNow admin
- Microsoft 365 tenant admin

### Configuration highlights

To set up Microsoft 365 support integration:

- Register application in Microsoft Entra ID for authentication of both outbound and inbound API calls.
- Create ServiceNow entities with Microsoft Entra Application for both outbound and inbound data flow.
- Integrate ServiceNow instance with Microsoft support through the Microsoft 365 admin portal.

    ![ServiceNow integration diagram.](../../media/servicenow-guide/servicenow-overview-integration-diagram.png)

### Application dependencies in your ServiceNow environments

Permissions required:

- oauth\_entity
- oauth\_entity\_profile

After the Microsoft 365 support integration app has been installed, two application cross-scope accesses are created. If they're not created successfully, create them manually.

## Set up the integration

After you've downloaded the app, go to the Microsoft 365 setup wizard in your ServiceNow environment to complete the setup process.

To open the setup wizard, type **Microsoft 365** in the ServiceNow navigator and select **Setup**.

![Start setup wizard.](../../media/servicenow-guide/servicenow-wizard-start-setup.png)

- If you want to get started without setting up the Microsoft 365 support integration app, you can select the option to **Continue without any setup**. This option continues to provide basic recommended solutions.
- To set up the application with full functionality, select **Start setup**, and then follow the instructions in [Integrate Microsoft 365 with ServiceNow Virtual Agent](servicenow-virtual-agent-integration).

Important

The Microsoft 365 support integration app occasionally prompts users for feedback about the app. If you don't want users to be prompted for feedback, turn off this functionality in the app settings. For more information about Microsoft feedback policies, see [Learn about Microsoft feedback for your organization](/en-us/privacy/microsoft-365/feedback/feedback-overview). To change the feedback settings, follow the steps in the installation process.