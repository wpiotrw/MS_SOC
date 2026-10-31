---
layout: Conceptual
title: How to monitor Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-classic-azure-monitor
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2025-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to configure Microsoft Purview metrics, alerts, and diagnostic settings by using Azure Monitor.
locale: en-us
document_id: b057231a-f037-de74-5885-839c07fece80
document_version_independent_id: b057231a-f037-de74-5885-839c07fece80
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-classic-azure-monitor.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-classic-azure-monitor
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-classic-azure-monitor.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: ce89865d-7ec6-2e45-12bd-e0dd3e230dc2
---

# How to monitor Microsoft Purview | Microsoft Learn

This article describes how to configure metrics, alerts, and diagnostic settings for Microsoft Purview using Azure Monitor.

## Monitor Microsoft Purview

Microsoft Purview admins can use Azure Monitor to track the operational state of Microsoft Purview account. Metrics are collected to provide data points for you to track potential problems, troubleshoot, and improve the reliability of the Microsoft Purview account. The metrics are sent to Azure monitor for events occurring in Microsoft Purview.

## Aggregated metrics

The metrics can be accessed from the Azure portal of a Microsoft Purview account. Access to the metrics is controlled by the role assignment of Microsoft Purview account. Users need to be part of the "Monitoring Reader" role in Microsoft Purview to see the metrics. Learn more about [Monitoring role permissions](/en-us/azure/azure-monitor/roles-permissions-security).

The person who created the Microsoft Purview account automatically gets permissions to view metrics. If anyone else wants to see metrics, add them to the **Monitoring Reader** role, by following these steps:

### Add a user to the Monitoring Reader role

To add a user to the **Monitoring Reader** role, the owner of Microsoft Purview account or the Subscription owner can follow these steps:

1. Go to the [Azure portal](https://portal.azure.com) and search for the Microsoft Purview account name.
2. Select **Access control (IAM)**.
3. Select **Add** &gt; **Add role assignment** to open the **Add role assignment** page.
4. Assign the role listed below. Get details on [assigning Azure roles](/en-us/azure/role-based-access-control/role-assignments-portal).

    | Setting | Value |
    | --- | --- |
    | Role | Monitoring Reader |
    | Assign access to | User, group, or service principal |
    | Members | &lt;Microsoft Entra account user&gt; |

    ![Screenshot showing Add role assignment page in Azure portal.](media/how-to-monitor-with-azure-monitor/add-role-assignment-page.png)

## Metrics visualization

Users in the **Monitoring Reader** role can see the aggregated metrics and diagnostic logs sent to Azure Monitor. The metrics are listed in the Azure portal for the corresponding Microsoft Purview account. In the Azure portal, select the Metrics section to see the list of all available metrics.

[![Screenshot showing available Microsoft Purview metrics section.](media/how-to-monitor-with-azure-monitor/purview-metrics.png)](media/how-to-monitor-with-azure-monitor/purview-metrics.png#lightbox)

Microsoft Purview users can also access the metrics page directly from the management center of the Microsoft Purview account. Select Azure Monitor in the main page of Microsoft Purview management center to launch Azure portal.

[![Screenshot to launch Microsoft Purview metrics from management center.](media/how-to-monitor-with-azure-monitor/launch-metrics-from-management.png)](media/how-to-monitor-with-azure-monitor/launch-metrics-from-management.png#lightbox)

### Available metrics

To get familiarized with how to use the metric section in the Azure portal pre read the following two documents. [Getting started with Metric Explorer](/en-us/azure/azure-monitor/essentials/metrics-getting-started) and [Advanced features of Metric Explorer](/en-us/azure/azure-monitor/essentials/metrics-charts).

The following table contains the list of metrics available to explore in the Azure portal:

| Metric Name | Metric Namespace | Aggregation type | Description |
| --- | --- | --- | --- |
| Data Map Capacity Units | Elastic data map | Sum  Count | Aggregate the elastic data map capacity units over time period |
| Data Map Storage Size | Elastic data map | Sum  Avg | Aggregate the elastic data map storage size over time period |
| Scan Canceled | Automated scan | Sum  Count | Aggregate the canceled data source scans over time period |
| Scan Completed | Automated scan | Sum  Count | Aggregate the completed data source scans over time period |
| Scan Failed | Automated scan | Sum  Count | Aggregate the failed data source scans over time period |
| Scan time taken | Automated scan | Min  Max  Sum  Avg | Aggregate the total time taken by scans over time period |

## Monitoring alerts

Alerts can be accessed from the Azure portal of a Microsoft Purview account. Access to the alerts is controlled by the role assignment of Microsoft Purview account just like metrics. A user can setup alert rules in their purview account to get notified when important monitoring events happen.

[![Screenshot showing creating an alert.](media/how-to-monitor-with-azure-monitor/step-one-alerts-setting.png)](media/how-to-monitor-with-azure-monitor/step-one-alerts-setting.png#lightbox)

The user can also create specific alert rules and conditions for signals within purview.

[![Screenshot showing addition alerts rules and conditions to a signal.](media/how-to-monitor-with-azure-monitor/step-two-alerts-setting.png)](media/how-to-monitor-with-azure-monitor/step-two-alerts-setting.png#lightbox)

## Sending diagnostic logs

Raw telemetry events are sent to Azure Monitor. Events can be sent to a Log Analytics Workspace, archived to a customer storage account of choice, streamed to an event hub, or sent to a partner solution for further analysis. Exporting of logs is done via the Diagnostic settings for the Microsoft Purview account on the Azure portal.

Follow these steps to create a diagnostic setting for your Microsoft Purview account and send to your preferred destination:

1. Locate your Microsoft Purview account in the [Azure portal](https://portal.azure.com).
2. In the menu under **Monitoring** select **Diagnostic settings**.
3. Select **Add diagnostic setting** to create a new diagnostic setting to collect platform logs and metrics. For more information about these settings and logs, see [the Azure Monitor documentation.](/en-us/azure/azure-monitor/essentials/diagnostic-settings).

[![Screenshot showing creating diagnostic log.](media/how-to-monitor-with-azure-monitor/create-diagnostic-setting.png)](media/how-to-monitor-with-azure-monitor/create-diagnostic-setting.png#lightbox)

1. You can send your logs to:

- A log analytics workspace
- A storage account
- An event hub

### Destination - Log Analytics Workspace

1. In the **Destination details**, select **Send to Log Analytics workspace**.
2. Create a name for the diagnostic setting, select the applicable log category group and select the right subscription and workspace, then select save. The workspace doesn't have to be in the same region as the resource being monitored. You to create a new workspace, you can follow this article: [Create a New Log Analytics Workspace](/en-us/azure/azure-monitor/logs/quick-create-workspace).

[![Screenshot showing assigning log analytics workspace to send event to.](media/how-to-monitor-with-azure-monitor/log-analytics-diagnostic-setting.png)](media/how-to-monitor-with-azure-monitor/log-analytics-diagnostic-setting.png#lightbox)

[![Screenshot showing saved diagnostic log event to log analytics workspace.](media/how-to-monitor-with-azure-monitor/log-analytics-select-workspace-diagnostic-setting.png)](media/how-to-monitor-with-azure-monitor/log-analytics-select-workspace-diagnostic-setting.png#lightbox)

1. Verify the changes in your Log Analytics Workspace by performing some operations to populate data. For example, creating/updating/deleting a policy. After which you can open the **Log Analytics Workspace**, navigate to **Logs**, enter query filter as **"purviewsecuritylogs"**, then select **"Run"** to execute the query.

[![Screenshot showing log results in the Log Analytics Workspace after a query was run.](media/how-to-monitor-with-azure-monitor/log-analytics-view-logs-diagnostic-setting.png)](media/how-to-monitor-with-azure-monitor/log-analytics-view-logs-diagnostic-setting.png#lightbox)

### Destination - Storage account

1. In the **Destination details**, select **Archive to a storage account**.
2. Create a diagnostic setting name, select the log category, select the destination as archive to a storage account, select the right subscription and storage account then select save. A dedicated storage account is recommended for archiving the diagnostic logs. If you need a storage account, you can follow this article: [Create a storage account](/en-us/azure/storage/common/storage-account-create?tabs=azure-portal).

[![Screenshot showing assigning storage account for diagnostic log.](media/how-to-monitor-with-azure-monitor/storage-diagnostic-setting.png)](media/how-to-monitor-with-azure-monitor/storage-diagnostic-setting.png#lightbox)

[![Screenshot showing saved log events to storage account.](media/how-to-monitor-with-azure-monitor/storage-select-diagnostic-setting.png)](media/how-to-monitor-with-azure-monitor/storage-select-diagnostic-setting.png#lightbox)

1. To see logs in the **Storage Account**, perform a sample action (for example: create/update/delete a policy), then open the **Storage Account**, navigate to **Containers**, and select the container name.

[![Screenshot showing container in storage account where the diagnostic logs have been sent to.](media/how-to-monitor-with-azure-monitor/storage-two-diagnostic-setting.png)](media/how-to-monitor-with-azure-monitor/storage-two-diagnostic-setting.png#lightbox)

1. Navigate to the file and download it to see the logs.

    [![Screenshot showing folders with details of logs.](media/how-to-monitor-with-azure-monitor/storage-navigate-diagnostic-setting.png)](media/how-to-monitor-with-azure-monitor/storage-navigate-diagnostic-setting.png#lightbox)

    [![Screenshot showing details of logs.](media/how-to-monitor-with-azure-monitor/storage-select-logs-diagnostic-setting.png)](media/how-to-monitor-with-azure-monitor/storage-select-logs-diagnostic-setting.png#lightbox)

### Destination - Event hub

1. In the **Destination details**, select **Stream to an event hub**.
2. Create a diagnostic setting name, select the log category, select the destination as stream to event hub, select the right subscription, event hubs namespace, event hub name and event hub policy name then select save. An event hub name space is required before you can stream to an event hub. If you need to create an event hub namespace, you can follow this article: [Create an event hub & event hubs namespace storage account](/en-us/azure/event-hubs/event-hubs-create)

[![Screenshot showing streaming to an event hub for diagnostic log.](media/how-to-monitor-with-azure-monitor/step-four-diagnostic-setting.png)](media/how-to-monitor-with-azure-monitor/step-four-diagnostic-setting.png#lightbox)

[![Screenshot showing saved log events to event hub.](media/how-to-monitor-with-azure-monitor/step-four-one-diagnostic-setting.png)](media/how-to-monitor-with-azure-monitor/step-four-one-diagnostic-setting.png#lightbox)

1. To see logs in the **Event Hubs Namespace**, Go to the [Azure portal](https://portal.azure.com), and search for the name of the event hubs namespace you created earlier, go the Event Hubs Namespace and click on overview. To find our more about capturing and reading captured audit events in the event hubs namespace, you can follow this article: [Audit Logs & diagnostics](data-gov-classic-audit-logs-diagnostics)

[![Screenshot showing activities in the event hub.](media/how-to-monitor-with-azure-monitor/step-four-one-diagnostic-setting.png)](media/how-to-monitor-with-azure-monitor/step-four-one-diagnostic-setting.png#lightbox)

## Sample Log

Here's a sample log you'd receive from a diagnostic setting.

The event tracks the scan life cycle. A scan operation follows progress through a sequence of states, from Queued, Running and finally a terminal state of Succeeded | Failed | Canceled. An event is logged for each state transition and the schema of the event will have the following properties.

```JSON
{
  "time": "<The UTC time when the event occurred>",
  "properties": {
    "dataSourceName": "<Registered data source friendly name>",
    "dataSourceType": "<Registered data source type>",
    "scanName": "<Scan instance friendly name>",
    "assetsDiscovered": "<If the resultType is succeeded, count of assets discovered in scan run>",
    "assetsClassified": "<If the resultType is succeeded, count of assets classified in scan run>",
    "scanQueueTimeInSeconds": "<If the resultType is succeeded, total seconds the scan instance in queue>",
    "scanTotalRunTimeInSeconds": "<If the resultType is succeeded, total seconds the scan took to run>",
    "runType": "<How the scan is triggered>",
    "errorDetails": "<Scan failure error>",
    "scanResultId": "<Unique GUID for the scan instance>"
  },
  "resourceId": "<The azure resource identifier>",
  "category": "<The diagnostic log category>",
  "operationName": "<The operation that cause the event Possible values for ScanStatusLogEvent category are: 
                    |AdhocScanRun 
                    |TriggeredScanRun 
                    |StatusChangeNotification>",
  "resultType": "Queued – indicates a scan is queued. 
                 Running – indicates a scan entered a running state. 
                 Succeeded – indicates a scan completed successfully. 
                 Failed – indicates a scan failure event. 
                 Cancelled – indicates a scan was cancelled. ",
  "resultSignature": "<Not used for ScanStatusLogEvent category. >",
  "resultDescription": "<This will have an error message if the resultType is Failed. >",
  "durationMs": "<Not used for ScanStatusLogEvent category. >",
  "level": "<The log severity level. Possible values are:
            |Informational
            |Error >",
  "location": "<The location of the Microsoft Purview account>",
}
```

The Sample log for an event instance is shown in the below section.

```JSON
{
  "time": "2020-11-24T20:25:13.022860553Z",
  "properties": {
    "dataSourceName": "AzureDataExplorer-swD",
    "dataSourceType": "AzureDataExplorer",
    "scanName": "Scan-Kzw-shoebox-test",
    "assetsDiscovered": "0",
    "assetsClassified": "0",
    "scanQueueTimeInSeconds": "0",
    "scanTotalRunTimeInSeconds": "0",
    "runType": "Manual",
    "errorDetails": "empty_value",
    "scanResultId": "0dc51a72-4156-40e3-8539-b5728394561f"
  },
  "resourceId": "/SUBSCRIPTIONS/111111111111-111-4EB2/RESOURCEGROUPS/FOOBAR-TEST-RG/PROVIDERS/MICROSOFT.PURVIEW/ACCOUNTS/FOOBAR-HEY-TEST-NEW-MANIFEST-EUS",
  "category": "ScanStatusLogEvent",
  "operationName": "TriggeredScanRun",
  "resultType": "Delayed",
  "resultSignature": "empty_value",
  "resultDescription": "empty_value",
  "durationMs": 0,
  "level": "Informational",
  "location": "eastus",
}
```

## Resources

[Microsoft Purview Data Map](data-map)