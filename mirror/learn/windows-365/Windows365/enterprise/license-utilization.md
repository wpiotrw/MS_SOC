---
layout: Conceptual
title: License and utilization | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/license-utilization
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: License and utilization
author: tanialima
ms.author: talima
ms.service: windows-365
ms.topic: feature-guide
ms.date: 2026-10-19T00:00:00.0000000Z
ms.subservice: windows-365-enterprise
zone_pivot_groups: windows-365-products
locale: en-us
document_id: ff6697a7-a124-c92e-6e16-eb7922556c4b
document_version_independent_id: ff6697a7-a124-c92e-6e16-eb7922556c4b
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/license-utilization.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/license-utilization
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/license-utilization.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: e4b5a3d9-f0cf-5590-0efa-5bb3fac95fca
---

# License and utilization | Microsoft Learn

Important

The License and utilization page is in public preview. Preview features are tagged with **(preview)** in the admin user interface and might have restricted or limited functionality. These features are subject to change before general availability (GA) and are fully supported by Microsoft. Preview features are considered unfinished, might not be suitable for production workloads, and should be used with caution.

The License and utilization page gives IT administrators a single view of Windows 365 license inventory and utilization, including assigned and available licenses by SKU, peak concurrent Cloud PC connections, total usage hours, and trends. The data retention for this page is 180 days and 28 for the **View data** table.

Note

The License and utilization page displays data after a connection has been established on the Cloud PC.

## Understand the charts

Each selected breakdown includes a trend chart and an aggregated chart.

1. A trend chart that shows connections over time. Each line represents a value within the selected dimension.
2. An aggregated chart that summarizes total connections during the selected time range.

::: zone pivot="enterprise-flex"

## Current license information

The **Current license information** section includes the License breakdown and Licenses by type & SKU charts show the tenant’s total licenses including by type and SKU, with the number and percentage of assigned and available licenses.

The **Current license information** charts typically refresh within 3 minutes and are reconciled daily for accuracy. Some license assignments and seats in transition may take up to 24 hours to appear, even though the Microsoft admin center updates immediately.

| Chart | Description |
| --- | --- |
| License breakdown | Total licenses in the tenant, grouped by license type |
| Licenses by type & SKU | Total licenses by type and SKU, including assigned and available counts |

**How to use these metrics:**

- Use the License breakdown chart to compare license types by total count; the center displays the total number of licenses across all types.
- In Licenses by type & SKU, click or hover over a license type to view its SKU-level Total, Assigned, and Available license counts.

## Enterprise, Flex Dedicated and Flex Shared

These charts show peak concurrent connections and total Cloud PC usage hours as trends and totals for the selected period, and support Enterprise, Flex Dedicated, and Flex Shared. Data freshness for these charts varies by selected time range: 2-hour and 12-hour data is available within 3 minutes; 24-hour, 4-day, 7-day, and 14-day data updates every 30 minutes; and 28-day, 90-day, 180-day, and 365-day data updates daily.

| Chart | Description |
| --- | --- |
| Max concurrent connections trend | Shows the peak number of simultaneous Cloud PC connections during the selected time range, grouped by the chosen data series. Helps administrators understand when and how users access their Cloud PCs. |
| Max concurrent connections | Shows the peak Cloud PC connection count in the Max concurrent connections trend for the selected time range. |
| Total hours used trend | Shows the total hours that Cloud PCs in the tenant were used during the selected time range. |
| Total hours used | Shows the combined usage hours for all Cloud PCs during the selected time range. |

**How to use these metrics:**

- Use Max concurrent and total hours data to ensure right-size license purchases and identify underutilization or overutilization or licenses by Cloud PC SKU, region, and provisioning policy name.

::: zone-end

::: zone pivot="agents"

## Agents

Session utilization hours trend and Session utilization hours for Windows 365 for Agents. Note that Agents don’t have a license type and are based on consumption. Data freshness for these charts varies by selected time range: 2-hour and 12-hour data is available within 3 minutes; 24-hour, 4-day, 7-day, and 14-day data updates every 30 minutes; and 28-day, 90-day, 180-day, and 365-day data updates daily.

| Chart | Description |
| --- | --- |
| Session utilization hours trend | Shows total Windows 365 for Agents session utilization hours for the selected filters, with each bar representing the hours recorded during that interval. |
| Session utilization hours | Shows Windows 365 for Agents session utilization hours for the selected time range, grouped by the chosen data series. |

**How to use these metrics:**

- Use Agents data to assess session utilization hours and determine underutilization or overutilization by User type, Pool name and User name.

::: zone-end

## View data table

The **View data** table in **License and utilization** provides a more granular view of Cloud PC utilization, organized by device or user. For more information, visit [View data](/en-us/windows-365/enterprise/monitor-cloud-pcs-view-data). The **View data** table always has a 3-minute latency, regardless of the selected time range.

| Tab | Description |
| --- | --- |
| Devices | The Devices tab provides a device-level view of Cloud PC utilization, including device name, device ID and session information. |
| Users | The Users tab provides a user-level view of Cloud PC utilization, including user principal name and number of session and duration for certain license types. |

## Examine License and utilization

1. Select the time range you want to analyze for license or Cloud PC utilization.
2. Review the License breakdown and Licenses by type & SKU charts for an at-a-glance view of license capacity across your environment.
3. Select the pivot for the license or utilization type you want to explore in more detail.
4. Review the trend and aggregated charts to identify how effectively or intensively a resource is being used, relative to available, assigned, or expected capacity.

Note

These charts provide a clear view of license inventory, assignment, and utilization patterns across the environment. Administrators should interpret assigned and available license counts in the context of their organization's deployment and assignment practices; these values alone do not determine whether licenses are being consumed efficiently.

#### Next steps

- Connection health
- Users and Devices
- Configuration Monitoring
- View data