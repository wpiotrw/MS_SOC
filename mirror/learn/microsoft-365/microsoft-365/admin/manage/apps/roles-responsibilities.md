---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Understand roles and responsibilities (preview) - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/apps/roles-responsibilities?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn which administrator roles can manage apps in Microsoft Copilot Managed Runtime and which roles have read-only access.
ms.date: 2026-09-25T00:00:00.0000000Z
author: laneswenka
ms.author: laswenka
manager: zoraz
ms.reviewer: mkaur
ms.topic: concept-article
ms.service: microsoft-365
ms.subservice: managed-apps-admin
ai-usage: ai-assisted
locale: en-us
document_id: f4282067-92b0-cb25-46e8-0e2f97825cd3
document_version_independent_id: f4282067-92b0-cb25-46e8-0e2f97825cd3
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/apps/roles-responsibilities.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/apps/roles-responsibilities
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/apps/roles-responsibilities.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/e6f942e8-55a7-4c86-b8e3-7456508ea850
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/f1834696-48d6-470d-966b-6ee418881596
platformId: c598d741-07da-46e0-d5ae-85b1eea389eb
---

# Understand roles and responsibilities (preview) - Microsoft 365 admin | Microsoft Learn

[This article is prerelease documentation and is subject to change.]

This article explains who can manage apps in Copilot Managed Runtime and who can only view them. If you're new to administering apps in Copilot Managed Runtime, start here to understand the access model before you change settings or assign roles to other people.

Important

- This is a preview feature.
- These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?LinkId=2373139), and are available before an official release so that customers can get early access and provide feedback.

## What is Copilot Managed Runtime?

Copilot Managed Runtime is a platform for business applications that your organization deploys and governs centrally. The apps are built on Microsoft Power Platform, and you administer them from two places:

- The [Microsoft 365 admin center](https://admin.microsoft365.com/Adminportal/Home#/homepage), where you find apps built with Copilot Managed Runtime under the **Apps** section.
- The [Power Platform admin center](https://admin.preview.powerplatform.microsoft.com/home), where apps built with Copilot Managed Runtime appear alongside your other Power Platform resources.

The role you're assigned determines which admin center you use and what you can do there.

Note

- The **Power Platform administrator** (and the other *manage* roles, such as Global administrator and Dynamics 365 administrator) can work from **either** admin center and change settings in both.
- The read-only roles—**AI administrator**, **AI reader**, and **Global reader**—use the **Microsoft 365 admin center** to view the Copilot Managed Runtime experience. Reading app details from the Power Platform admin center isn't supported for these roles yet.

## Two kinds of access: Manage and Read only

Every administrator role falls into one of two groups:

- **Manage (read and write)** — You can view apps in Copilot Managed Runtime *and* make changes. This access includes updating settings, adjusting governance and security policies, and creating alerts.
- **Read only** — You can view apps in Copilot Managed Runtime, their components, and their health, but you can't make changes.

This split lets you give people the visibility they need without giving everyone the ability to change your configuration.

## Roles at a glance

The following table lists the most common roles and the kind of access each one has.

| Role | Access | Where it applies |
| --- | --- | --- |
| [Power Platform administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#power-platform-administrator) | **Manage** (read/write) | Microsoft 365 admin center and Power Platform admin center |
| [Global administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) | **Manage** (read/write) | Microsoft 365 admin center and Power Platform admin center |
| [Dynamics 365 administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#dynamics-365-administrator) | **Manage** (read/write) | Power Platform admin center |
| [AI administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#ai-administrator) | **Read only** | Microsoft 365 admin center |
| [AI reader](/en-us/entra/identity/role-based-access-control/permissions-reference#ai-reader) | **Read only** | Microsoft 365 admin center |
| [Global reader](/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader) | **Read only** | Microsoft 365 admin center |

For more information about these roles and their permissions, note the following details:

- The **Power Platform administrator** is the primary role for managing apps in Copilot Managed Runtime. It has full read and write access to every Copilot Managed Runtime capability.
- A **Global administrator** has the same kind of management access as a Power Platform administrator for Copilot Managed Runtime. If you already use Global administrator to run Microsoft 365, you already have what you need to manage these apps.
- The **AI administrator** and **AI reader** roles in the Microsoft 365 admin center are read-only for Copilot Managed Runtime. They can see apps and their health, but they can't change settings.
- A **Global reader** has the same read-only access as an AI reader. It's the read-only counterpart to the Global administrator role.

## What a Manage role can do

If you have a Manage role, you can do everything a read-only role can do, plus make changes. For example, you can:

- **Update app settings** and adjust how governance is applied. See [Customizing governance](governance).
- **Apply security and compliance policies**, such as advanced connector policies (ACP) and access controls. See [Security and compliance for Copilot Managed Runtime](security-compliance).
- **Create and manage alerts** on app health metrics. See [Visibility and monitoring](visibility-monitoring).
- **Onboard and remove apps in Copilot Managed Runtime**, and decide how they're shared across your organization.

## What a read-only role can do

If you have a read-only role, you can see what's happening without the risk of changing your configuration. For example, you can:

- **View the list of apps in Copilot Managed Runtime** and open any app to see its components and details. The **All apps** list is under **Apps** in the Microsoft 365 admin center. See [Visibility and monitoring](visibility-monitoring).
- **View app health metrics** on the **Monitor** tab of an app, including success rates and performance.
- **View existing alert rules and triggered alerts**, even though you can't create or change them.

Read-only access is a good fit for people who need visibility for reporting, auditing, or support, but who shouldn't change settings. For example, help-desk staff or compliance reviewers.

## Recommended role assignments

Use these guidelines to decide which role to assign:

- Give **Power Platform administrator** or **Global administrator** to the small group of people responsible for configuring and governing apps in Copilot Managed Runtime.
- Give **AI administrator**, **AI reader**, or **Global reader** to people who need to monitor apps or review your setup but shouldn't make changes.
- Follow the principle of *least privilege*: start with read-only access and grant Manage access only when someone's job requires it.

To learn how to give someone a role, see [Assign admin roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/assign-admin-roles) and [About admin roles](/en-us/microsoft-365/admin/add-users/about-admin-roles).