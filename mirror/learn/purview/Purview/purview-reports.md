---
layout: Conceptual
title: Microsoft Purview posture reports overview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/purview-reports
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-05-20T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ai-usage: ai-assisted
ms.service: purview
ms.collection:
- highpri
- purview-compliance
- m365solution-mip
- m365initiative-compliance
- highpri
ms.custom:
- admindeeplinkDEFENDER
- sfi-ga-nochange
search.appverid:
- MOE150
- MET150
description: Learn how Microsoft Purview posture reports help admins evaluate sensitivity-label adoption, DLP policy effectiveness, and information-protection coverage across your organization.
locale: en-us
document_id: 40fc139a-3072-7c4f-c461-9484cddc70d9
document_version_independent_id: 40fc139a-3072-7c4f-c461-9484cddc70d9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/purview-reports.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purview-reports
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/purview-reports.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 4c1134ce-f84a-9282-e3fd-a3e0e0425efe
---

# Microsoft Purview posture reports overview | Microsoft Learn

Note

Information Protection posture reports, Data Loss Prevention posture reports, and Custom posture reports are in preview. The capabilities, terminology, and UX may change before general availability.

## Prerequisites

### Permissions

To access **Reports**, your account must belong to one of the following Microsoft 365 role groups, Microsoft Purview roles, or Microsoft Purview role groups.

#### Microsoft 365 role groups

- Compliance administrator
- Security administrator
- Compliance data administrator
- Global administrator

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

#### Microsoft Purview roles

To fine-tune access controls, use Microsoft Purview roles. To learn more, see [Permissions in the Microsoft Purview portal](purview-permissions).

- Information Protection Admin
- Information Protection Analyst
- Information Protection Investigator
- Information Protection Reader

#### Microsoft Purview role groups

To grant access through role groups, use the following Microsoft Purview role groups. To learn more, see [Permissions in the Microsoft Purview portal](purview-permissions).

- Information Protection
- Information Protection Admins
- Information Protection Analysts
- Information Protection Investigators
- Information Protection Readers

## Posture reports

Microsoft Purview collects and analyzes large volumes of data about how information in your organization is used and protected. This data surfaces through audit logs, Activity explorer, Content explorer, solution-level dashboards, and reports. Posture reports give SOC admins and solution-level admins prebuilt views that turn that data into key insights about your information protection and DLP posture.

Posture reports help you answer questions for executives and operations teams, such as:

- Is Purview doing what we intend it to do?
- Are our policies effective?
- Where are the gaps in our protection strategy?

You find **Posture Reports** in the [Microsoft Purview portal](https://purview.microsoft.com):

- **Information Protection** &gt; **Reports**
- **Data Loss Prevention** &gt; **Reports**

Note

The data shown in posture reports is gathered on a 30-day rolling-window basis. Save any reports (as .PDF) that you want to keep for future reference. You can also configure and save your preferred filter settings for future use.

## Information Protection posture reports

These reports are in preview.

- Label distribution and adoption
- Auto-labeling policy coverage
- Sensitivity label activity

## Data Loss Prevention posture reports

These reports are in preview.

- Most triggered DLP rules and activities
- DLP policies with highest trigger volume
- Top DLP policy violators

Note

DLP policies in simulation mode don't show up in posture reports.

## How the Reports tool works

As a Microsoft 365 administrator or compliance administrator, you can evaluate and then tag content in your organization to control where it goes, protect it no matter where it is, and ensure that it's preserved and deleted according to your organization's needs. You do this through the application of [sensitivity labels](sensitivity-labels), [retention labels](retention#retention-labels), [sensitive information types](sit-sensitive-information-type-learn-about) (SIT) classification, and classification by [trainable classifiers](trainable-classifiers-learn-about). There are various ways to do the discovery, evaluation, and tagging, but the end result is that you might have large numbers of documents and emails that are tagged and classified with one or more of these labels. You need to see:

- How labels are used across your tenant and what's done with those items.
- The protections placed on items.
- The most common activities.

The **Reports** tool, available in the **Information Protection** and **Data Loss Prevention (DLP)** solutions, provides visibility into that information and more. The reports include information from both Microsoft 365 source services (Exchange, SharePoint, OneDrive) and non-Microsoft 365 sources.

For example, the **Reports** tool shows you:

- Information on [protection policies (preview)](data-gov-protection-policy).
- The [trainable classifiers](trainable-classifiers-learn-about) detected most often across your cloud platforms.
- The number of items classified as a sensitive information type and what those classifications are.
- The SITs detected most often across your cloud platforms.
- The top applied sensitivity labels and activities.
- A summary of activities users take on your sensitive content.
- The locations of your sensitive and retained data.
- Summary information on email encryption.

The sections in the **Reports** page are interactive, so you can drill down for more detail. The **Reports** page also links to:

- [Activity explorer](data-classification-activity-explorer)
- [Data explorer](data-classification-data-explorer)
- [Content explorer (classic)](data-classification-content-explorer)

## Custom posture reports

Note

Custom posture reports are in preview. The capabilities, terminology, and UX may change before general availability.

Custom posture reports work alongside the built-in posture reports to give your team flexibility. Use the built-in reports for ready-made insights that cover common information-protection and DLP scenarios, and create custom reports to assemble the metrics, charts, and filters that answer questions specific to your organization.

Use custom posture reports to answer questions such as:

- Are sensitivity labels being adopted consistently across workloads?
- Where is sensitive content concentrated, and is that concentration growing?
- Are DLP policies reducing risk for specific data types?

To create or open a custom posture report, go to one of the following locations in the [Microsoft Purview portal](https://purview.microsoft.com):

- **Information Protection** &gt; **Reports** &gt; **Add report**
- **Data Loss Prevention** &gt; **Reports** &gt; **Add report**

### Key concepts

A custom report is a container that holds the cards you use to visualize labeling, classification, and protection activity. Every custom report includes:

- A **report name** and description that state the report's purpose.
- One or more **sections** that group cards by purpose, audience, or theme.
- One or more **cards** within each section that each answer a specific question.

#### Sections

Sections give a report structure by grouping related cards. They make multi-card reports easier to read and navigate. A report can contain one or more sections, and each section can hold multiple cards.

Add sections before you add cards—sections are the layout framework for the report.

#### Card types

Cards are the building blocks of a custom report. You can mix and match built-in cards within the same report, or add a custom card.

| Card type | Description | Use for |
| --- | --- | --- |
| Metric card | Displays a single, high-level value or KPI. | Pairing a primary metric with its historical trend. Common uses include adoption, growth, and compliance-health indicators. |
| Chart card | Provides richer visualizations that reveal patterns and trends. | Distributions, breakdowns, and trend analysis across locations, labels, or workloads. |

#### Custom card configuration

Custom cards let you tailor views to the specific questions your organization needs to answer. They complement built-in cards by adding organization-specific perspectives to the foundation that built-in cards already provide.

**Metric-based custom cards** support these configuration options:

- **Time range**: Choose any window up to 30 days, extending the 7-day view that built-in metric cards provide.
- **Display format**: **Number** (a raw count), **Percentage** (a proportional view), or **Compound** (a value combined with a trend direction).
- **Filters**: Limit data to specific criteria, such as a sensitivity label, location, or workload.

**Chart-based custom cards** support these chart types:

- **Vertical bar**: Compares values across categories using vertical bars.
- **Horizontal bar**: Compares values across categories using horizontal bars. Useful when category labels are long.
- **Pie**: Shows the proportional distribution of values across categories.
- **Donut**: Similar to a pie chart, with a central area that improves readability.
- **Line chart**: Shows trends or changes over time.

Apply filters and pivot by grouping dimensions—such as **Activity** or **Sensitive info type**—to tailor chart-based cards to specific scenarios.

#### Example: configure a custom card

This example tracks adoption of the *Confidential* sensitivity label over the last 30 days.

| Setting | Value |
| --- | --- |
| Card type | Metric card |
| Metric | Number of items labeled *Confidential* |
| Time range | Last 30 days (custom) |
| Display format | **Compound** (total count with trend direction) |
| Sensitivity label filter | *Confidential* |
| Workload filter | SharePoint |

**What the card shows:**

- The current total number of items labeled *Confidential*.
- Whether labeling activity is increasing or decreasing over the last 30 days.
- A focused view of adoption for one label and one workload.

#### Best practices

- Start with clear questions, then choose the cards that answer them.
- Avoid overcrowding a report. A few well-chosen cards are more effective than many.
- Use metric cards for status at a glance and chart cards for deeper analysis.
- Treat custom reports as living assets and iterate as needs evolve.
- For larger reports, save after every two sections.