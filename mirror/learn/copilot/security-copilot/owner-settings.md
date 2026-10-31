---
layout: Conceptual
title: Configure owner settings in Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/owner-settings
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to configure Copilot owner settings and allow access to plugins, promptbooks and capacity management.
ms.date: 2026-05-28T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: how-to
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: c19123e5-0c33-4e91-26b2-58e4418e94a8
document_version_independent_id: c19123e5-0c33-4e91-26b2-58e4418e94a8
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/owner-settings.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: owner-settings
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/owner-settings.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 7dd69cfd-31c4-0cd6-29e7-0c51fab1c730
---

# Configure owner settings in Microsoft Security Copilot | Microsoft Learn

Give administrators the ability to manage the data and custom plugin use in Security Copilot.

## Prerequisites

You need the Security Copilot owner role to manage owner settings.

For more information, see [Understand authentication in Microsoft Security Copilot](authentication#assign-roles).

## Manage owner settings

Manage the usage and data privacy for Copilot in the owner settings menu in Security Copilot.

- Manage capacity - Manage security compute unit association and creation.
- Help improve Copilot - Help improve Copilot by allowing Microsoft to capture data.
- Logging audit data in Microsoft Purview - Manage logging audit data by configuring whether to allow Microsoft Purview to access, process, copy, and store Customer Data.
- Manage who can upload files - Specify who can upload files. For more information, see [File upload](upload-file).

### Manage capacity settings

Manage capacity association, overage units, and geo location evaluation options. Keep in mind, purchasing new security capacity units (SCUs), changing capacity, or associating with a different capacity all require Azure Owner or Contributor access to the capacity resource in the Azure portal.

![Screenshot showing capacity association configuration menu.](media/owner-settings-capacity-unit-association.png)*Figure shows owner setting for associating SCUs.*

For more information on purchasing SCUs, see [Onboarding to Security Copilot](security-compute-units-capacity#security-compute-units).

Tip

Use the [Security Copilot Cost Estimator](https://securitycopilot.microsoft.com/calculator) to estimate how many SCUs your organization may need based on the number of Security Copilot users.

### Help improve Copilot

The following data sharing options are available:

| Setting | Description |
| --- | --- |
| **Allow Microsoft to capture data from Security Copilot to validate product performance using human review** | Such validations include but aren't limited to:  - Ability of Security Copilot to successfully provide responses to user requests and understand capability gaps that need to be addressed based on user prompts.- Understand the types of tasks customers are using Security Copilot for. - Produce metrics surrounding the usability and quality of responses.  - Validate Security Copilot capabilities involving other Microsoft products purchased and integrated by a customer. - Improve responses from plugins accessing other Microsoft products. For more information, see [Set up location for prompt evaluation and opt-in (or out of) data sharing](privacy-data-security#set-up-location-for-prompt-evaluation-and-opt-in-or-out-of-data-sharing). |
| **Allow Microsoft to capture and human review data from Security Copilot to build and validate Microsoft's security AI model** | Such validations include but aren't limited to: - Captured data is used to develop security specific models built on top of Azure OpenAI foundational model, which would power more intelligent and personalized capabilities for Security Copilot and other Microsoft products that it integrates with. **NOTE:** Data isn't shared with OpenAI or used to train the Azure OpenAI foundational model. |

For more information, see [Data sharing and feedback options](privacy-data-security#customer-data-sharing-preferences).

### Manage logging audit data in Microsoft Purview

Manage logging audit data by configuring whether to allow Microsoft Purview to access, process, copy, and store Customer Data.

Security Copilot uses Microsoft Purview to process and store data such as administrator actions, user actions, and system responses.

In most scenarios, logs are available within 24 hours in Microsoft Purview after enabling the capability.

Important

Microsoft Purview will store your Customer Data in the region where your Microsoft 365 data is stored. For more information, see, [Privacy and data security](privacy-data-security). The default retention period for audit logs is 180 days, but can be extended using audit log retention policies. For more information, see [Manage audit log retention policies](/en-us/purview/audit-log-retention-policies?tabs=microsoft-purview-portal).

If you already use Microsoft Purview, no further set up is needed. Otherwise, you'll need to provision a free, limited experience. For more information, see [Turn auditing on or off](/en-us/purview/audit-log-enable-disable?tabs=microsoft-purview-portal).

For more information, see [Audit logging](audit-log).

## Manage who can upload files

As an owner, you can configure who can upload files into Security Copilot to allow Copilot to refer to contents of the file for responses. You can set it so that no one can upload files or contributors and owners can upload files.