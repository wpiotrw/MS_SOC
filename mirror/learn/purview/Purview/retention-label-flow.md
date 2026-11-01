---
layout: Conceptual
title: Customize what happens at the end of the retention period | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/retention-label-flow
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-02-10T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-records-management
ms.collection:
- purview-compliance
- SPO_Content
ms.custom: admindeeplinkCOMPLIANCE
search.appverid:
- MOE150
- MET150
description: Instructions how to configure a retention label with custom actions and logic when the retention period has expired by using Power Automate flows.
locale: en-us
document_id: 1b2cc594-2c5f-3c45-6cd2-5431549037db
document_version_independent_id: 1b2cc594-2c5f-3c45-6cd2-5431549037db
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/retention-label-flow.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: retention-label-flow
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/retention-label-flow.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
platformId: bc9c930d-1d13-7500-fa2d-5abdb908b40c
---

# Customize what happens at the end of the retention period | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

When you configure a [retention label](retention) to retain items for a specific period, you specify what action to take at the end of that retention period. You can choose from the built-in actions of permanently deleting the item, relabeling the item, deactivating the label, and starting a disposition review.

However, if you choose the option to run a Power Automate flow, this label configuration supports custom actions such as:

- Send an email notification to a records manager, or to the person who created or last modified a document
- Move a document item to a SharePoint location where you centrally store records

You can also select the Microsoft 365 compliance label-specific actions of relabel the item or permanently delete it:

![Configuring a Power Automate flow for when an item reaches the end of its retention period.](media/retention-label-power-automate.png)

For example, a flow can move the item, relabel it, and then send an email notification.

Note

You can also use the relabel action to remove the existing retention label when you select this action but don't specify a replacement label (leave the label name blank). If the existing retention label marked the item as a record, the record must be [locked](record-versioning#locking-and-unlocking-a-record) for the label to be removed.

The actions also allow integration with other apps and services. For example, you might have another solution that starts your own customized disposition review process when an email notification is received. Or your flow adds a new entry into a table and this change automatically starts an existing records management procedure.

It's outside the scope of this article to document all the ways in which you can configure a flow and integrate with other solutions. However, to learn more about Power Automate, see [Get started with Power Automate](/en-us/power-automate/getting-started) and [Overview of cloud flows](/en-us/power-automate/overview-cloud). In this article, you learn about:

- Overview of using retention labels with a Power Automate flow
- Limitations
- Power Automate dependency
- How to configure a retention label to run a Power Automate flow
- When the flow is triggered

## Overview of using retention labels with a Power Automate flow

The following processes show the high-level overview of how retention labels work with a Power Automate flow:

![Process overview of how retention labels work with a Power Automate flow.](media/retention-label-flow-overview.png)

In Power Automate, create an automated cloud flow from blank that uses the trigger **When an item reaches the end of its retention period**. Then, add one or more steps and specify the operations that run your choice of actions.

Next, in the Microsoft Purview portal, create a new retention label with the following configuration:

- Retain the item for a specified period of time
- At the end of the retention period, run the flow that you just created

Apply the label by using either of the following methods:

- [Publish retention labels and apply them in apps](create-apply-retention-labels)
- [Apply a retention label to content automatically](apply-retention-labels-automatically)

When the retention period expires, your configured flow runs.

Note

In a Power Automate flow, you can also select the action **Apply a retention label on the item**. This action is independent from this scenario that applies actions at the end of the retention period. Instead, it's the equivalent to manually applying a retention label. The label is applied immediately.

## Add resilience to your flow

Although optional, we recommend you always add the **Trigger a new instance of the flow if an item can't be located** action before **Relabel an item at the end of retention** and **Deletes an item at the end of retention**.

This additional action is required for files that you move or rename after an instance of the flow is triggered but your specified compliance actions aren't completed. Without it, a renamed or moved file results in the flow failing because it can't find the file.

Although renaming and moving files after an instance of the flow is triggered are an unusual occurrence, adding this recommended action improves the reliability of the compliance actions succeeding because the current path and name of the file is retrieved automatically just before the selected actions run.

## Limitations for this scenario

- You must create a new retention label to run a flow at the end of the retention period. You can't edit an existing retention label for this configuration.
- By default, the account that creates the Power Automate flow must be the same account that creates the retention label. If you share the flow in Power Automate, the people you share it with can also select the flow when they create a retention label.
- In Power Automate, you must use the option **My flows** to create the flow. Currently, creating a flow under **Solutions** isn't supported.
- If you select the relabel action in the flow, the retention label that you select as the replacement can't be [configured to mark the item as a regulatory record](declare-records#configuring-retention-labels-to-declare-records). It can be configured to mark the item as a record, or not mark the item as a record.
- If your chosen flow uses an [environment type other than Default](/en-us/power-platform/admin/environments-overview#types-of-environments), you must use [PowerShell to create the retention label](/en-us/powershell/module/exchange/new-compliancetag), and use the *FlowId* parameter.

## Power Automate dependency

Power Automate is a workflow service that automates actions across applications and services. Specific to running a Power Automate flow at the end of the retention period:

- You must have a [Power Automate plan](/en-us/power-platform/admin/power-automate-licensing/types) that includes premium connectors, separate from your Microsoft 365 compliance plan.
- The Power Automate flow must be an automated cloud flow that you create from blank, and configure to use the trigger **When an item reaches the end of its retention period**.

For more information about how to use and configure the dependent automated cloud flows, see the [Microsoft Power Automate Documentation](/en-us/power-automate).

## How to configure a retention label to run a Power Automate flow

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), create a new retention label with your preferred name and settings. For more information, see [Use file plan to create and manage retention labels](file-plan-manager).
2. For this scenario, complete the following steps:

    1. On the **Define label settings** page, select **Retain items indefinitely or for a specific period** and specify the retention period.
    2. On the **Choose what happens after the retention period** page, select **Run a Power Automate flow**, and then **Select a flow**:

        ![Configuring a retention label to run a Power Automate flow after the retention period expires.](media/retention-label-flow-configuration.png)
    3. From the **Select a Power Automate flow** flyout pane, you'll see any automated cloud flows that you created (or somebody has shared with you) and that have the **When an item reaches the end of its retention period** trigger.

        Select the flow you want, and complete the configuration to create the retention label.

A retention label can be configured for only one Power Automate flow, but the same flow can be used by more than one retention label.

## When the flow is triggered

Just as it can take up to seven days to automatically apply a retention label or display it so you can apply it, so you should allow up to seven days after the expiration period expires before the Power Automate flow is triggered. The initiation of the flow can then take a few hours.

For the Microsoft 365 compliance actions of delete and relabel, then allow up to seven days for these actions to complete. Specific for Exchange and the Microsoft 365 compliance actions of delete, allow up to 14 days.

Both the flow itself and the Microsoft 365 compliance actions in the flow are queued so that if there are any network or service delays, the flow and actions are automatically retried.

The [principles of retention](retention#the-principles-of-retention-or-what-takes-precedence) still apply to retention labels that are configured to run a flow at the end of the retention period, in that an item is always retained for the longest period if there is a conflict with one or more retention policies. However, the flow is always triggered at the end of the label's retention period.