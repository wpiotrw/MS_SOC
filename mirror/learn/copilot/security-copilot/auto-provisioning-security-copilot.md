---
layout: Conceptual
title: Understand how Security Copilot is auto provisioned for eligible Microsoft 365 E5 and E7 customers | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/auto-provisioning-security-copilot
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about how Security Copilot is auto provisioned for eligible Microsoft 365 E5 and E7 customers
ms.date: 2026-06-18T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: overview
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
- essentials-get-started
locale: en-us
document_id: b3850ffd-fa2e-3a0c-644e-f4288cb358f7
document_version_independent_id: b3850ffd-fa2e-3a0c-644e-f4288cb358f7
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/auto-provisioning-security-copilot.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: auto-provisioning-security-copilot
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/auto-provisioning-security-copilot.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 4ebbed77-2c4d-1c56-85f0-7b5ab99b807f
---

# Understand how Security Copilot is auto provisioned for eligible Microsoft 365 E5 and E7 customers | Microsoft Learn

If Security Copilot is included in your Microsoft 365 E5 or E7 license and your tenant has been enabled, Microsoft will automatically provision and onboard, so that you can immediately get started with Security Copilot in the flow of your work. You can start using Security Copilot in the following experiences:

- Data security in Microsoft Purview: https://purview.microsoft.com
- Identity and access in Microsoft Entra: https://entra.microsoft.com
- Endpoint management in Microsoft Intune: https://intune.microsoft.com
- Access Security Copilot portal: https://securitycopilot.microsoft.com

For more information on Security Copilot capabilities included in your license, see [Learn about Security Copilot inclusion in Microsoft 365 E5 and E7](security-copilot-inclusion).

## What gets autoprovisioned?

As part of the autoprovisioning process, the following steps are done for you so that you can easily get started:

- Creation of a default Security Copilot virtual capacity and a default workspace
- Assign default workspace settings

    - Customer Data storage location
    - Customer Data sharing preferences
- Assign additional settings

    - Prompt evaluation location
    - Accessing data from Microsoft 365 services
- Assign default roles for the default workspace

## Workspace and capacity

A workspace is a logical container that defines three things:

- Where your data is stored (Customer Data storage location)
- Which capacity powers your experience, and
- Who has access (Security Copilot owners and contributors are scoped per workspace)

When your customer tenant is provisioned, Security Copilot automatically creates a default workspace and links it to your Security Copilot capacity. If your tenant already has workspaces, the earliest-created workspace becomes the default.

Security Copilot experiences across Microsoft Defender, Entra, Purview, and Intune use the default workspace.

## Customer Data storage location

Customer Data storage location is the geography where customer's prompts, responses, and any Customer Data associated with a workspace are stored. For the default workspace that Microsoft creates for you, the Customer Data storage location that is preselected is your Microsoft Entra geography.

If your customer tenant has Microsoft 365 geo override (Preferred Data location, Go Local move programs, [Advanced Data Residency (ADR add-on)](/en-us/microsoft-365/enterprise/advanced-data-residency) etc.), then we use this Microsoft 365 geo override and map to one of the supported geos by Security Copilot.

You can view the Customer Data storage location that is preselected for your Security Copilot default workspace within the **Owner settings** page in the Security Copilot portal. For more information, see [Configure owner settings](owner-settings).

## Customer Data sharing preferences

By default, the following settings are set to **Off**:

- **Allow Microsoft to capture data from Security Copilot to validate product performance using human review**
- **Allow Microsoft to capture and human review data from Security Copilot to build and validate Microsoft's security AI model**

You can change the data sharing settings within the **Owner settings** page in the Security Copilot portal.

For more information, see [Privacy and data security](privacy-data-security#set-up-data-sharing).

## Prompt evaluation location

Prompt evaluation location determines where your prompts are processed (evaluated) using GPU resources. When a user enters a prompt, Security Copilot evaluates it on GPU clusters in Azure datacenters. This configuration setting is preselected during autoprovisioning. By default,

- If your tenant's Customer Data storage location is in the EU, then prompts are processed in the EU
- If your tenant's Customer Data storage location is not in the EU, then prompts are processed globally (US, UK, EU, ANZ) depending on locality and GPU availability.

## Accessing data from Microsoft 365 services

This setting allows customers to configure whether Security Copilot can query information directly from Microsoft 365 services such as Microsoft Purview.

By default, this setting is set to ON.

If you want to disable Security Copilot's access to Microsoft 365 service data, administrators can adjust this in [Owner settings](privacy-data-security#accessing-data-from-microsoft-365-services).

Note

Choosing to disable Security Copilot or limit it's access to Microsoft 365 service data will limit Security Copilot's ability to work with Microsoft 365 products.

What admins should do once enabled:

- Review Owner settings to confirm your organization's preferred configuration.
- Inform users that Security Copilot is available as part of your Microsoft 365 E5 and E7 license and how it can be used within your organization's policies.

For more information, see [Privacy and data security](privacy-data-security#accessing-data-from-microsoft-365-services).

## Default roles

The following Microsoft Entra, Intune, Defender, and Purview roles automatically inherit **Security Copilot owner** access:

- Global Administrator
- Security Administrator
- Conditional Access Administrator
- Intune Administrator
- ComplianceBundle
    - Microsoft Entra Compliance Administrator
    - Purview Compliance Admin
    - Purview Organization Management
- Purview Data Governance Administrator

The following Microsoft Defender and Purview roles automatically inherit **Security Copilot contributor** access:

- Microsoft Defender roles
    - *Any custom Microsoft Defender XDR roles that include Security Copilot permission*. For more information, see [Create custom roles](/en-us/defender-xdr/create-custom-rbac-roles).
- Microsoft Purview roles. For more information, see [Purview roles in Security Copilot](purview-contributor-roles).
- Microsoft Intune roles
    - Any Microsoft Intune roles that include Security Copilot permission. For more information, see [Intune RBAC roles in Security Copilot](/en-us/intune/whats-new/#role-based-access-control).

These roles that were added by default, can be modified within the **Role assignment** page of Security Copilot portal.