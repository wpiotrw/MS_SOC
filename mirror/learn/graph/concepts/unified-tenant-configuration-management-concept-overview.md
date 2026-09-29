---
layout: Conceptual
title: Overview of the Tenant Configuration Management APIs in Microsoft Graph - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/unified-tenant-configuration-management-concept-overview
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: Swatyario
ms.author: MSGraphDocsVteam
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: tenant-configuration-management
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: article
description: Use the Tenant Configuration Management APIs in Microsoft Graph to control and manage configuration settings for an entire organization.
ms.date: 2026-01-19T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: conceptual
locale: en-us
document_id: 1477ea03-6515-2818-ab86-afe16dfc5765
document_version_independent_id: 1477ea03-6515-2818-ab86-afe16dfc5765
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/unified-tenant-configuration-management-concept-overview.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-tenant-configuration-management-concept-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/unified-tenant-configuration-management-concept-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: e3f75a07-520e-5886-49e1-4d06449dc81c
---

# Overview of the Tenant Configuration Management APIs in Microsoft Graph - Microsoft Graph | Microsoft Learn

In traditional Tenant Configuration Management, any administrator within an organization uses their credentials to access the resources to which they have access. However, administrators don't have full control over the tenant configuration and lack visibility into whether it deviates from the desired configuration state.

The Tenant Configuration Management (TCM) APIs allow administrators to control and manage configuration settings across a single workload or multiple workloads within the organization. The following list shows the supported workloads:

- [Microsoft Defender](/en-us/graph/utcm-securityandcompliance-resources)
- [Microsoft Entra](/en-us/graph/utcm-entra-resources)
- [Microsoft Exchange Online](/en-us/graph/utcm-exchange-resources)
- [Microsoft Intune](/en-us/graph/utcm-intune-resources)
- [Microsoft Purview](/en-us/graph/utcm-securityandcompliance-resources)
- [Microsoft Teams](/en-us/graph/utcm-teams-resources)

Administrators have the ability to manage tenant configuration through a declarative representation that helps maintain configuration settings in the desired state. This representation can define one or multiple resources, each with one or more associated properties.

## Why integrate with the Tenant Configuration Management APIs?

### Maintain a secure and consistent tenant configuration

As the Microsoft 365 ecosystem grows, keeping tenant settings aligned with the desired configuration of an organization becomes increasingly complex. Currently, IT administrators often have to manually detect and resolve configuration drift, a process that is time-consuming and prone to error. The TCM APIs address this challenge by enabling automated monitoring of tenant settings. With the [monitoring](/en-us/graph/api/resources/configurationmonitor) APIs in TCM, you can ensure your configurations remain secure and consistent, and quickly identify any deviations from the desired state.

### Easily extract and understand current configuration states

The [snapshot](/en-us/graph/api/resources/configurationsnapshotjob) APIs in TCM simplify the process of retrieving the current configuration across multiple workloads within a tenant. Administrators can use these snapshots to get a clear, declarative view of how settings are currently applied, which makes audits, reviews, and troubleshooting much easier.

## API reference

Looking for the API reference for this service, see [Tenant Configuration Management APIs in Microsoft Graph](/en-us/graph/api/resources/unified-tenant-configuration-management-api-overview).