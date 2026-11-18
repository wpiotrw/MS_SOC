---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft Copilot Managed Runtime overview for admins - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/apps/?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn how Microsoft Copilot Managed Runtime hosts and governs the apps your organization builds, what's in place from the first app, and how to get started as an admin.
ms.date: 2026-11-17T00:00:00.0000000Z
author: mihaelablendea
manager: zoraz
ms.author: mihaelab
ms.reviewer: mkaur
ms.topic: overview
ms.service: microsoft-365
ms.subservice: managed-apps-admin
ai-usage: ai-assisted
locale: en-us
document_id: 3f2d57ec-181a-e167-479d-b6b963c3da1b
document_version_independent_id: 3f2d57ec-181a-e167-479d-b6b963c3da1b
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/apps/index.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/apps/index
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/apps/index.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: f28e2172-f4f2-59dc-d9d2-58940d969e3d
---

# Microsoft Copilot Managed Runtime overview for admins - Microsoft 365 admin | Microsoft Learn

Microsoft Copilot Managed Runtime helps teams build and run line-of-business agentic applications that automatically comply with your organization's IT governance policies. Every app is governed from the moment it's created, with no extra setup required:

- Each maker builds in a personal environment that's created automatically, with policies already applied.
- Every app inherits the default environment group settings, which control what it can connect to, who it can be shared with, and what external content it can load.
- Apps sign users in with Microsoft Entra ID, follow your Conditional Access policies, and have your policies enforced while they run.

This built-in governance uses the same managed platform that governs Microsoft Power Platform. For more information, see [Managed environments overview](/en-us/power-platform/admin/managed-environment-overview).

To understand how the platform delivers these protections, see:

- [How the managed host secures apps](/en-us/microsoft-365/copilot-managed-runtime/managed-runtime-security-governance): how the Copilot Managed Runtime host protects apps at runtime and how its built-in protections work with the controls you manage.
- [Copilot Managed Runtime architecture](/en-us/microsoft-365/copilot-managed-runtime/developer/apps/architecture): how the Copilot Managed Runtime host, the SDK, and the CLI work together as apps are built, published, and run.

Each app appears in the Microsoft 365 admin center, where you can track usage, monitor health, and manage its lifecycle.

Copilot Managed Runtime brings three audiences together around the same governed app:

- **Makers and developers** build apps with the tools they already use, such as Copilot Cowork, Copilot Code, Microsoft Copilot Studio, the Copilot Managed Runtime CLI, or Lovable.
- **Users** discover and run the apps that are shared with them.
- **Administrators** govern apps across the tenant from the Microsoft 365 admin center, while Microsoft operates the Copilot Managed Runtime host.

This article helps you get started as an admin. It covers:

- **Get started:** what's in place before makers start building, how to review and adjust it for your organization, and the tasks to keep apps running.
- **App building options:** the tools makers and developers use to build apps, and how you control each one.
- **Licensing and billing:** how building and running apps are billed, and what people need to run the apps shared with them.

Each section is a short summary that links to the article covering the topic in detail.

## Get started

You don't need to do anything before makers start building. Default governance, including the default environment group, is configured once, triggered by whichever comes first: a maker starts to create the first app, or an admin selects **Set up governance** on the **Apps** &gt; **Overview** page in the Microsoft 365 admin center. Either way, governance is in place before the first app exists, so every app is governed from the moment it's created. Once configured, the **Set up governance** option is no longer available. Use the following steps to review what's in place, adjust it for your organization, and oversee apps as adoption grows. Each step links to the article that covers it in detail.

### Before you start

From the first app, Copilot Managed Runtime provides:

- **A personal environment for each maker.** When a maker starts building, they get their own private, managed space with policies already applied. They can build and test without affecting anyone else.
- **A default environment group that Microsoft manages.** Every app inherits the default environment group settings, based on Microsoft best practices. These settings cover which connectors and MCP servers apps can use, who apps can be shared with, and which external content apps can load. You can review these settings and take them over when your organization needs different rules.
- **One inventory.** Every app appears in the Microsoft 365 admin center with its owner, location, dependencies, usage, and health, whichever tool built it.

Because these protections are in place from the start, you can begin with the default environment group settings and adjust as adoption grows. Before you roll out broadly:

- **Assign admin roles.** Decide who manages Copilot Managed Runtime and who needs read-only access for reporting, security, or support. See [Roles and responsibilities](roles-responsibilities).

### Review and adjust

1. **Review the default environment group settings.** Check what's in place and customize the settings if your organization needs different rules. See [Review and customize default settings](governance). Optionally, add security and compliance controls beyond the default environment group settings. See [Manage security and compliance for Copilot Managed Runtime](security-compliance).
2. **Choose who can build apps, and with which tools.** Decide whether every maker can build apps from day one or whether to start with a pilot group. See App building options.
3. **Set up licensing and billing.** Make sure makers can build and that the people apps are shared with can run them. See Licensing and billing.

### Operate

- **Oversee your apps.** See what's been built, who owns it, what it depends on, and how it's used. If an app doesn't meet your policies, block it and follow up with the owner. See [View and oversee apps across your tenant](inventory).
- **Monitor health and performance.** Track app reliability and performance, and set alerts so you can act before users are affected. See [Monitor the health of apps in Copilot Managed Runtime](visibility-monitoring).
- **Manage costs.** Review consumption and respond to requests for more credits. See [Manage licensing and Copilot Credits for apps on Copilot Managed Runtime](licensing-credits).

## App building options

The tool a maker chooses changes the building experience, not how the app is hosted or governed.

| Creation tool | Who it's for | How you govern app building enablement |
| --- | --- | --- |
| Copilot Cowork | Business users who describe an app in chat | On by default. You can turn it off or limit it to specific users and groups with the Build apps in Copilot setting in the Microsoft 365 admin center. See [Build apps in Copilot Cowork](/en-us/copilot/cowork/cowork-build-apps#enable-or-disable-app-building). |
| Copilot Code | Business users and developers who build with an AI coding agent | Through spending policies. Only users included in a spending policy for Copilot Code can build apps. See Control who can build apps in Copilot Code. |
| Microsoft Copilot Studio | Makers who want more control over planning, previewing, and publishing | On by default. You can turn it off or limit it to specific security groups. See Control app creation in Copilot Studio, and [Data residency when building apps in Copilot Studio](/en-us/microsoft-copilot-studio/geo-data-residency-build-apps) |
| Copilot Managed Runtime CLI and SDK | Professional developers who work in Visual Studio Code, GitHub Copilot, or other tools of their choice | Off by default. See [Control whether apps can be created using the CLI](governance#control-whether-apps-can-be-created-using-the-cli). |
| Lovable | Makers who build in Lovable and deploy to your tenant | See [Set up Copilot Managed Runtime for Lovable](configure-lovable). |

### Control who can build apps in Copilot Code

Copilot Code uses cost controls to decide who can build apps. Only users who are included in a spending policy for Copilot Code can build apps with it.

To limit who can build apps using Copilot Code, create a spending policy in the Microsoft 365 admin center that selects the Copilot Code service and includes only the users, or a security group of users, who are allowed to build apps.

For step-by-step instructions, including turning on usage-based billing and setting per-user limits, see [Cowork and Copilot Code](licensing-credits#cowork-and-copilot-code) in [Manage licensing and Copilot Credits for apps on Copilot Managed Runtime](licensing-credits).

### Control app creation in Copilot Studio

App creation in Copilot Studio is controlled by tenant settings that you configure with the Microsoft Power Platform CLI.

#### Turn off app creation in Copilot Studio

To turn off Copilot Studio app creation, use the following command:

```bash
pac admin update-tenant-settings --setting-name powerPlatform.powerapps.enableManagedAppsMcsPreview --setting-value 'off'
```

For more information, see [Programmability and extensibility - Power Platform](/en-us/power-platform/admin/programmability-extensibility-overview#available-tools) and [Microsoft Power Platform CLI admin command group](/en-us/power-platform/developer/cli/reference/admin#pac-admin-update-tenant-settings).

Note

Copilot Studio retrieves the tenant settings each time you refresh the page. If you leave a Copilot Studio tab open, the settings are cached for up to 15 minutes or until the next page load.

#### Scope access to Copilot Studio app creation with security groups

To restrict Copilot Studio app creation to specific Microsoft Entra security groups, set `powerPlatform.powerapps.enabledGroupsManagedAppsMcsPreview` to a security group's object ID (GUID). To configure multiple groups, use a comma-separated string of object IDs.

The following example configures access for one security group. Replace `<SGID>` with the Microsoft Entra security group object ID:

```bash
pac admin update-tenant-settings --setting-name powerPlatform.powerapps.enabledGroupsManagedAppsMcsPreview --setting-value '<SGID>'
```

When the Copilot Studio app creation path is enabled, users who belong to any configured security group can create apps.

## Licensing and billing

Apps on Copilot Managed Runtime use consumption-based billing through Copilot Credits, and building an app is billed separately from running it:

- **Building** an app is billed through the tool the maker uses. Cowork and Copilot Code use spending policies in the Microsoft 365 admin center. Copilot Studio uses environment credits in the Power Platform admin center, or spending policies in the Microsoft 365 admin center for environments that have moved there as Copilot Studio cost management moves to the Microsoft 365 admin center. The CLI doesn't require a license for development.
- **Running** an app requires either a Power Apps Premium license or Copilot Credits through a spending policy that includes Copilot Managed Runtime, which administrators set up per user in the Microsoft 365 admin center. Sharing an app gives people access to it, but it doesn't cover the cost of running it. Each person **running the app** also needs a Power Apps Premium license or must be included in a spending policy that includes Copilot Managed Runtime.

For setup steps, recommended policy patterns, cost examples, and troubleshooting, see [Manage licensing and Copilot Credits for apps on Copilot Managed Runtime](licensing-credits). For answers to common licensing questions, see the [Copilot Managed Runtime licensing FAQ](licensing-faq).

## Related information

- [What is Copilot Managed Runtime](./)
- [Copilot Managed Runtime architecture](/en-us/microsoft-365/copilot-managed-runtime/developer/apps/architecture)
- [How the managed host secures apps](/en-us/microsoft-365/copilot-managed-runtime/managed-runtime-security-governance)
- [Roles and responsibilities](roles-responsibilities)
- [View and oversee apps across your tenant](inventory)
- [Review and customize default settings](governance)
- [Monitor the health of apps in Copilot Managed Runtime](visibility-monitoring)
- [Manage security and compliance for Copilot Managed Runtime](security-compliance)
- [Set up Copilot Managed Runtime for Lovable](configure-lovable)
- [Manage licensing and Copilot Credits for apps on Copilot Managed Runtime](licensing-credits)
- [FAQ about Microsoft Copilot Managed Runtime](faq-about-apps)
- [Copilot Managed Runtime licensing FAQ](licensing-faq)
- [Govern apps in Copilot Managed Runtime at scale](governance)
- [Apps in Microsoft Copilot Studio (preview)](/en-us/microsoft-copilot-studio/apps-experience/apps-overview)