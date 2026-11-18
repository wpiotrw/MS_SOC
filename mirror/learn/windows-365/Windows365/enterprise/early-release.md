---
layout: Conceptual
title: Windows 365 Early Release (Preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/early-release
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Concept article that explains early release and why a customer would want to use it
author: cawerner
ms.author: cawerner
ms.service: windows-365
ms.topic: concept-article
ms.date: 2026-11-10T00:00:00.0000000Z
ms.subservice: windows-365-enterprise
locale: en-us
document_id: cd9173c4-ae45-6eb6-7579-67ea1f6159ee
document_version_independent_id: cd9173c4-ae45-6eb6-7579-67ea1f6159ee
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/early-release.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/early-release
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/early-release.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 550d771d-d7db-2017-accb-7906b64c4d8b
---

# Windows 365 Early Release (Preview) | Microsoft Learn

Windows 365 Early Release is an optional service release setting that lets a dedicated test or QA tenant receive eligible Windows 365 service changes before those changes reach tenants on Standard Release. It's designed for organizations with established change-management practices that want to validate changes against representative Cloud PCs, applications, policies, and user workflows before the same changes reach production.

This article explains what Early Release is, why you might use it, how it relates to the default Standard Release, and what you need to configure it.

Important

Don't enable Early Release on a tenant that serves your production users. Use Early Release only in a separate, secondary test, QA, or validation tenant, and keep your production tenant on Standard Release.

## Prerequisites

- A separate test, QA, or validation tenant that isn't your production tenant.
- Windows 365 licenses in that tenant. Early Release supports Windows 365 Enterprise, Frontline, Flex, Cloud Apps, and Reserve. Windows 365 Business and W365 for Agents isn't supported.
- Representative Cloud PCs, users, applications, policies, and connection scenarios to exercise during each validation cycle.
- An admin account with a role that can change the service release setting. For more information, see Role-based access control for the service release setting.

## What Early Release includes

Early Release defines which Windows 365 service changes your test tenant receives early. The initial scope is Windows 365 access and connection experiences, including changes to:

- How users access their Cloud PCs.
- How users and Cloud PCs authenticate to Microsoft Entra ID.
- How connections are established between the client and the Cloud PC.
- How local devices, such as keyboards, cameras, and printers, are used in a remote session.

## Standard Release is the default

Standard Release is the default service release setting, and it's the right choice for production tenants. Every Windows 365 tenant is on Standard Release unless an authorized administrator explicitly changes it. You don't need to take any action to stay on Standard Release.

The service release setting applies to the entire tenant. You can't scope it to selected users, groups, or individual Cloud PCs. If you enable Early Release on a tenant, every user and Cloud PC in that tenant receives eligible service changes before Standard Release. For this reason, mixed production and validation deployments aren't supported.

## Why use Early Release

Early Release gives your IT team a predictable window to test Windows 365 service changes before they reach production. Because Windows 365 is a continuously updated service, this window helps you plan for change instead of reacting to it.

Organizations use Early Release to:

- Find compatibility or operational issues before they affect production users.
- Prepare help desk staff and business stakeholders for upcoming changes.
- Make Windows 365 service changes more predictable within existing change-management processes.
- Share findings with Microsoft, which can inform the assessment of a change before broader deployment.

When a new service release reaches Early Release, Microsoft publishes a notice in the Microsoft 365 Message center. The notice summarizes the changes and recommends validation scenarios to run in your test tenant.

## How the service release setting works

Administrators manage the service release setting at the tenant level in the Microsoft Intune admin center, under **Tenant administration** &gt; **Windows 365 administration** &gt; **Service release**. To change the setting, an authorized administrator selects **Edit**, chooses **Early release** or **Standard release**, and selects **Update**.

As part of the preview of Early Release, any newly provisioned or re-provisioned Cloud PC is in the new release state.

To return a tenant to the default, change the setting back to **Standard release**.

## Role-based access control for the service release setting

Only administrators with the appropriate Windows 365 or Intune role can change the service release setting. Assign these roles in the test tenant only to the administrators who own your validation process.

| Role | View the setting | Change the setting |
| --- | --- | --- |
| Global Administrator | Yes | Yes |
| Intune Administrator | Yes | Yes |
| Windows 365 Administrator | Yes | Yes |
| Cloud PC Administrator | Yes | Yes |
| Cloud PC Reader | Yes | No |