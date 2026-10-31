---
layout: Conceptual
title: Audit logs, diagnostics, and activity history in Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-classic-audit-logs-diagnostics
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2024-05-22T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to enable enable and capture audit logs and time series activity history in Microsoft Purview Data Map with Azure Event Hubs.
ms.custom: sfi-image-nochange
locale: en-us
document_id: 0f04683e-1298-9cd5-10a3-56a6357c21ef
document_version_independent_id: 0f04683e-1298-9cd5-10a3-56a6357c21ef
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-classic-audit-logs-diagnostics.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-classic-audit-logs-diagnostics
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-classic-audit-logs-diagnostics.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f0234678-3067-4edc-abf7-8142d54bb7d2
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b0f4f6b9-28ed-4892-be4e-517310289c68
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: be8725d3-ef72-5071-2007-aa040d682ac4
---

# Audit logs, diagnostics, and activity history in Data Map | Microsoft Learn

This tutorial lists the step-by-step configuration required to enable and capture audit and diagnostics logs for the Microsoft Purview Data Map via Azure Event Hubs.

A Microsoft Purview administrator or Microsoft Purview data-source admin needs the ability to monitor audit and diagnostics logs captured from Data Map. Audit and diagnostics information consists of the timestamped history of actions taken and changes made to a Microsoft Purview account by every user. Captured activity history includes actions made using the Microsoft Purview portal, or using the REST API.

This tutorial takes you through the steps to enable audit logging. It also shows you how to configure and capture streaming audit events from the Microsoft Purview portal via Azure Diagnostics event hubs.

## Enable audit and diagnostics

The following sections walk you through the process of enabling audit and diagnostics.

### Configure Event Hubs

Create an [Azure Event Hubs namespace by using an Azure Resource Manager (ARM) template (GitHub)](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.eventhub/eventhubs-create-namespace-and-enable-capture). This automated Azure ARM template will deploy and finish creating your Event Hubs instance with the required configuration.

For step-by-step explanations and manual setup:

- [Event Hubs: Use an ARM template to enable Event Hubs capture](/en-us/azure/event-hubs/event-hubs-resource-manager-namespace-event-hub-enable-capture)
- [Event Hubs: Enable capturing of events streaming manually by using the Azure portal](/en-us/azure/event-hubs/event-hubs-capture-enable-through-portal)

### Connect a Microsoft Purview account to Diagnostics event hubs

Now that Event Hubs is deployed and created, connect your Microsoft Purview account diagnostics audit logging to Event Hubs.

1. Go to your Microsoft Purview account home page. This page is where the overview information is displayed in the [Azure portal](https://portal.azure.com). It's not the Microsoft Purview governance portal home page.
2. On the left menu, select **Monitoring** &gt; **Diagnostic settings**.

    [![Screenshot that shows selecting Diagnostic settings.](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-e.png)](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-e.png#lightbox)
3. Select **Add diagnostic setting** or **Edit setting**. Adding more than one diagnostic setting row in the context of Microsoft Purview isn't recommended. In other words, if you already have a diagnostic setting row, don't select **Add diagnostic**. Select **Edit** instead.

    [![Screenshot that shows the Add or Edit Diagnostic settings screen.](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-f.png)](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-f.png#lightbox)
4. Select the **audit** and **allLogs** checkboxes to enable collection of audit logs. Optionally, select **AllMetrics** if you also want to capture Data Map capacity units and Data Map size metrics of the account.

    [![Screenshot that shows configuring Microsoft Purview Diagnostic settings and selecting diagnostic types.](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-g.png)](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-g.png#lightbox)

Diagnostics configuration on the Microsoft Purview account is complete.

Now that diagnostics audit logging configuration is complete, configure the data capture and data retention settings for Event Hubs.

1. Go to the [Azure portal](https://portal.azure.com) home page, and search for the name of the Event Hubs namespace you created earlier.
2. Go to the Event Hubs namespace. Select **Event Hubs** &gt; **Capture Data**.
3. Supply the name of the Event Hubs namespace and the event hub where you want the audit and diagnostics to be captured and streamed. Modify the **Time Window** and **Size Window** values for the retention period of the streaming events. Select **Save**.

    [![Screenshot that shows Capture settings on the Event Hubs namespace and Event Hubs.](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-h.png)](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-h.png#lightbox)
4. Optionally, on the left menu, go to **Properties** and change **Message Retention** to any value between one and seven days. The retention period value depends on the frequency of scheduled jobs or the scripts you've created to continuously listen and capture the streaming events. If you schedule a capture once every week, move the slider to seven days.

    [![Screenshot that shows Event Hubs Properties message retention period.](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-i.png)](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-i.png#lightbox)
5. At this stage, the Event Hubs configuration is complete. The Microsoft Purview governance portal will start streaming all its audit history and diagnostics data to this event hub. You can now proceed to read, extract, and perform further analytics and operations on the captured diagnostics and audit events.

### Read captured audit events

To analyze the captured audit and diagnostics log data:

1. Go to **Process data** on the Event Hubs page to see a preview of the captured audit logs and diagnostics.

    [![Screenshot that shows configuring Event Hubs Process data.](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-d.png)](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-d.png#lightbox)

    [![Screenshot that shows navigating Event Hubs.](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-c.png)](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-c.png#lightbox)
2. Switch between the **Table** and **Raw** views of the JSON output.

    [![Screenshot that shows exploring Microsoft Purview audit events on Event Hubs.](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-a.png)](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-a.png#lightbox)
3. Select **Download sample data** and analyze the results carefully.

    [![Screenshot that shows Query and Process Microsoft Purview Audit data on Event Hubs.](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-b.png)](media/tutorial-purview-audit-logs-diagnostics/azure-purview-diagnostics-audit-eventhub-b.png#lightbox)

Now that you know how to gather this information, you can use automatic, scheduled scripts to extract, read, and perform further analytics on the Event Hubs audit and diagnostics data. You can even build your own utilities and custom code to extract business value from captured audit events.

These audit logs can also be transformed to Excel, any database, Dataverse, or Synapse Analytics database for analytics and reporting by using Power BI.

While you're free to use any programming or scripting language of your choice to read the event hubs, here's a ready-made [Python-based script](https://github.com/Azure/Azure-Purview-API-PowerShell/blob/main/purview_atlas_eventhub_sample.py). See this Python tutorial on how to [capture Event Hubs data in Azure Storage and read it by using Python (azure-eventhub)](/en-us/azure/event-hubs/event-hubs-capture-python).

## Audit event categories

Some of the important categories of Microsoft Purview governance portal audit events that are currently available for capture and analysis are listed in the table.

More types and categories of activity audit events will be added.

| Category | Activity | Operation |
| --- | --- | --- |
| Management | Collections | Create |
| Management | Collections | Update |
| Management | Collections | Delete |
| Management | Role assignments | Create |
| Management | Role assignments | Update |
| Management | Role assignments | Delete |
| Management | Scan rule set | Create |
| Management | Scan rule set | Update |
| Management | Scan rule set | Delete |
| Management | Classification rule | Create |
| Management | Classification rule | Update |
| Management | Classification rule | Delete |
| Management | Scan | Create |
| Management | Scan | Update |
| Management | Scan | Delete |
| Management | Scan | Run |
| Management | Scan | Cancel |
| Management | Scan | Create |
| Management | Scan | Schedule |
| Management | Data source | Register |
| Management | Data source | Update |
| Management | Data source | Delete |