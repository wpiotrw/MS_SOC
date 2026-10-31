---
layout: Conceptual
title: Microsoft Security Copilot egress IPs | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-ip-address
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about the egress IPs for Microsoft Security Copilot
ms.date: 2025-12-19T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: concept-article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
ms.reviewer: shivanpatel
search.audiencetype: Admin
locale: en-us
document_id: 30b1a354-c6c5-e205-7a04-ebccbd3b356f
document_version_independent_id: 30b1a354-c6c5-e205-7a04-ebccbd3b356f
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-ip-address.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-ip-address
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-ip-address.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 5f9905e6-f19a-e3c3-00ce-9505069f958b
---

# Microsoft Security Copilot egress IPs | Microsoft Learn

To ensure communication between Security Copilot and certain security solutions, ensure to allow Security Copilot's egress IPs to contact the solution.

The egress IP addresses enable Security Copilot to securely send requests and receive responses from the plugin.

Allow the following IPs based on the instance type you are using.

| Region | Egress IP address |
| --- | --- |
| Australia East | 4.237.91.160/29 |
| Brazil South | 4.160.64.120/29 |
| Canada Central | 4.173.72.88/29 |
| Canada East | 4.248.114.8/29 |
| Central India | 4.188.45.56/29 |
| East US | 48.211.114.168/29 |
| East US 2 | 72.153.16.200/29 |
| France Central | 4.251.29.8/29 |
| Germany West Central | 4.182.156.104/29 |
| Japan East | 48.210.117.64/29 |
| Korea Central | 4.230.181.72/29 |
| North Europe | 72.145.24.32/29 |
| Qatar Central | 4.171.44.192/29 |
| South Africa North | 4.222.245.0/29 |
| South Central US | 23.98.246.88/29 |
| Southeast Asia | 57.155.157.72/29 |
| Sweden Central | 135.225.147.168/29 |
| Switzerland North | 74.242.234.136/29 |
| UAE North | 74.243.192.152/29 |
| UK South | 4.250.47.152/29 |
| West Central US | 172.208.176.8/29 |
| West Europe | 72.145.132.208/29 |
| West US | 172.178.185.8/29 |
| West US 2 | 72.154.34.248/29 |
| West US 3 | 57.154.125.160/29 |