---
layout: Conceptual
title: Collection Policies Solution Overview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about collection policies and how to use them.
keywords: Microsoft 365, Microsoft Purview, collection policies, compliance
ms.service: purview
ms.subservice: purview-collection-policies
ms.topic: article
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-11-12T00:00:00.0000000Z
audience: itpro
ms.collection:
- purview-compliance
- m365initiative-compliance
- m365solution-scenario
- highpri
ai-usage: ai-assisted
locale: en-us
document_id: 971c8f49-b22a-b4fd-4b90-509c50ac672a
document_version_independent_id: 971c8f49-b22a-b4fd-4b90-509c50ac672a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/collection-policies-solution-overview.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: collection-policies-solution-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/collection-policies-solution-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: c026453f-86c6-7c34-6f7a-22ce7c2a258c
---

# Collection Policies Solution Overview | Microsoft Learn

Collection policies are an event collection and filtering tool in Microsoft Purview that enables monitoring and classification of events from apps and locations that lay both inside of and beyond your organizations trust boundaries. They let you filter which events from both untrusted and trusted sources are ingested into Purview. Once ingested, that data can be classified and used by various Microsoft Purview signal consuming solutions, such as [Microsoft Purview Activity explorer](data-classification-activity-explorer), [Microsoft Purview Insider Risk Management](insider-risk-management), [Microsoft Purview eDiscovery](edisc), [Microsoft Purview Data Lifecycle Management](data-lifecycle-management).

Collection policies can help you achieve these data security outcomes:

## Only ingest the events that you want

The primary purpose of collection policies is to enable you to define the events that your organization wants to bring into Microsoft Purview, so you can focus on the data that you care about. Here are some examples of how this capability can help you.

### Regulatory compliance by geopolitical location

Your organization may span geopolitical and regulatory boundaries with different regions having different data security and privacy requirements. One may require all events be ingested into Purview, while another area may be subject to restrictions on what events can be collected. Collection policies let you define the events that are collected for each region. This allows you to meet the data security and privacy requirements of each region while still having a single consolidated view into your organization's sensitive information.

### Filter out unnecessary events

Your organization may have many events that are being collected, but you only want to see the events that are relevant to your needs. For example, say your organization has onboarded all devices and enabled **Always audit file activity for devices** in Endpoint DLP settings. This means that all file activity is being collected and placed into activity explorer. Sifting through all events may slow event investigation as you sort out the unwanted data to get to the data you need. With collection policies, you can filter out the events that you don't want to see before they get to activity explorer. This can help reduce noise and make it easier to find the events that are relevant to your organization.

## How collection policies work

The key to understanding collection policies is to know what an event is.

An *event* is made up of two things:

- A *condition*, like **Content contains**, or **File extension is**. This requires the use of classifiers, like sensitive information types. For example, a condition could be **Content contains** a sensitive information type, like **U.S. Social Security Number** or **File extension is** &gt; **.docx**.
- An *activity* that a user can take on a sensitive item, like **File copied to removable media**

Collection policies filter events based on:

- A match to one or more conditions and activities defined in the event.
- A match to the *data source* or location where the event is happening. For example, a collection policy can be scoped to only collect events from devices, or only collect events from Copilot in Fabric.

A policy is considered matched when one or more of the conditions are met (unless you AND the conditions) and the activity is matched on the data source.

### Multiple collection policies for single data source

It's possible your organization will need to create multiple collection policies for any given data source. Collection policies handle the multiple policy scenario differently than DLP or other Purview policies, which assign a priority to policy evaluation based on the order in which the policies are created.

On the collection polices page, you see all the individual policies that have been created. But on the back end, during policy evaluation, Microsoft Purview combines all the collection policies for a data source into a single collection policy for that data source. So all the conditions for a data source are used when identifying matches.

## Accessing collection policies

Collection policies are a component of the Microsoft Purview portal **Classifiers** feature. You can access them from anywhere in the Purview portal where the **Classifiers** feature is available. For example,

- In the Microsoft Purview portal, select **Solutions** &gt; **Data Loss Prevention** &gt; **Classifiers** &gt; **Collection policies**.
- Alternately, you can access collection policies in the Microsoft Purview portal from **Solutions** &gt; **Information Protection** &gt; **Classifiers** &gt; **Collection policies**.

## Collection policy configuration overview

You have flexibility in how you create and configure your collection policies. All collection policies require the same information from you. You must know this information *before* you start creating a collection policy. For additional details about each step, including supported configuration, see [Collection policies policy reference](collection-policies-policy-reference).

1. Define **data to detect** by configuring conditions required for a policy match. There are five supported conditions:

    - **Content contains classifiers**, which makes use of [sensitive information types](sit-sensitive-information-type-learn-about) and [trainable classifiers](trainable-classifiers-learn-about). Can be scoped to all classifiers, all classifiers except selected ones, or only specific classifiers. 
        Note

        The devices location doesn't support using trainable classifiers.
    - **Content contains sensitivity labels**, which makes use of [sensitivity labels](sensitivity-labels). Can be scoped to specific sensitivity labels. Only supported with browser and cloud apps detection.
    - **Document size equals or is greater than**, as measured in bytes, kilobytes (KB), megabytes (MB), gigabytes (GB), or terabytes (TB).
    - **Document is equal to or smaller than**, as measured in bytes, kilobytes (KB), megabytes (MB), gigabytes (GB), or terabytes (TB).
    - **File extension is**, which makes use of file extensions.
2. Choose the **activities** required for a policy match - The supported activities are specific for the data source. For devices, there are 19 supported activities, such as **File copied to removable media**, **File printed**, and **File uploaded to cloud**. A full list of the supported activities is available in the [Collection policies policy reference](collection-policies-policy-reference#activities).
3. Choose **where to apply** the policy by selecting a [data source](collection-policies-policy-reference#data-sources).
4. Depending on the policy settings you choose, you may have [additional settings](collection-policies-policy-reference#other-collection-policy-settings) to configure, such as whether or not to enable content capture for AI interactions and the cloud apps detection method.

## Content capture for AI interactions

To help comply with regulatory requirements, you can decide whether to capture and store all detected prompts and responses from any generative AI data sources added to the policy. This makes it easy to discover and protect the captured content later with additional Microsoft Purview policies and solutions. This capability doesn't include content in files shared with generative AI, and only applies to:

- Copilot experiences
- Enterprise AI
- Unmanaged cloud apps categorized as generative AI
- All unmanaged AI apps adaptive app scope

Without the setting enabled, content detected in prompts and responses are limited to sensitive information only.

Note

To capture AI content, you must have the **Content contains classifiers** condition set to **All**.

## Collection Policies and Microsoft Purview Insider Risk Management

Depending on your configuration, [Microsoft Purview Insider Risk Management](insider-risk-management) policy behavior might be impacted by collection policies. When an insider risk policy is configured, it monitors service and third-party indicators to help you quickly identify, triage, and act on risk activity. Using logs from Microsoft 365 and Microsoft Graph, Insider Risk Management allows you to define specific policies to identify risk indicators. These policies allow you to identify risky activities and to act to mitigate these risks.

Warning

When a device collection policy is configured and deployed, if there's a conflict between what the Insider Risk Management policy is configured to monitor and what the collection policy is configured to filter for, the collection policy configuration takes precedence. This means that if an Insider Risk Management policy is configured to monitor a specific activity, but the collection policy is configured to filter out that activity, the activity isn't collected and isn't available for review in Insider Risk Management. This only applies to [device indicators](insider-risk-management-settings-policy-indicators#device-indicators) in Insider Risk Management policies, and only when a device collection policy is deployed. If a collection policy is configured to collect something that an Insider Risk Management policy isn't configured for, then the indicator is collected, but Insider Risk Management ignores it.

## Collection policies and Endpoint Data Loss Prevention

When **[Always audit file activity for devices](dlp-configure-endpoint-settings#always-audit-file-activity-for-devices)** is enabled all activities for Office, PDF, and CSV files are collected by default. If you want to modify which activities are collected for devices in this case, you can do so by configuring a collection policy targeted to devices. If **Always audit file activity for devices** isn't enabled, activities aren't collected from devices, even if a collection policy is created scoped to devices.

Collection policies can't impact the behavior of DLP policies, only what is collected and recorded for audit file events on devices.

## Collection policies and Microsoft Purview Data Security Posture Management and Purview Data Security Posture Management for AI

When you use one-click policies in [Microsoft Data Security Posture Management](data-security-posture-management) or [Microsoft Data Security Posture Management for AI](dspm-for-ai) (DSPM for AI), you can take action on recommendations that automatically create collection policies on your behalf.

You can view and monitor the outcomes of these policies in tailored experiences within DSPM and DSPM for AI, as well as in activity explorer. These policies are named automatically by the quick policy experience. Post-creation, these collection policies can be viewed and edited in the same manner as collection policies created using the workflow.