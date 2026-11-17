---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: FAQ about Microsoft Copilot Managed Runtime - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/apps/faq-about-apps?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Get answers to common administrator questions about Microsoft Copilot Managed Runtime, including environments, routing, app building controls, governance, monitoring, and sharing.
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
document_id: 12f7ecea-894f-43ff-7986-f3d0222825ce
document_version_independent_id: 12f7ecea-894f-43ff-7986-f3d0222825ce
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/apps/faq-about-apps.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/apps/faq-about-apps
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/apps/faq-about-apps.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 95be2335-c6f4-6697-810a-4454edf8ee94
---

# FAQ about Microsoft Copilot Managed Runtime - Microsoft 365 admin | Microsoft Learn

This article answers common administrator questions about Microsoft Copilot Managed Runtime. For questions about licenses and Copilot Credits, see [Copilot Managed Runtime licensing FAQ](licensing-faq).

## Where are apps built with Copilot Managed Runtime created?

Apps built with Copilot Managed Runtime are created in personal environments. If a maker already owns one, the app reuses it. Otherwise, the app creates a new personal environment based on your existing environment routing rules.

Personal environments give each maker a dedicated place to build, without putting everyone's apps in a single, organization-wide environment such as the Default environment, which is hard to govern at scale. Much like a personal OneDrive, a personal environment belongs to one maker but stays part of your organization's governed estate. Administrators keep full visibility and control over every app, and makers can start building right away.

## Which admin center do I use to govern Copilot Managed Runtime?

You use both, for different purposes:

- **Microsoft 365 admin center**: App-level visibility and governance. View the inventory of apps, monitor usage and operational health, block or delete apps, and configure environment group level policies specific to Copilot Managed Runtime, such as sharing rules.
- **Power Platform admin center**: Environment-level granularity and policies that aren't specific to Copilot Managed Runtime. Manage environments, environment groups, environment routing, and data policies, and find the environment that hosts each app.

## Where can I find the environment that hosts an app built with Copilot Managed Runtime?

The environment that hosts each app is listed in the inventory in the Power Platform admin center. To find it:

1. In the Power Platform admin center, go to **Manage** &gt; **Inventory**.
2. Set **Item type** to **Copilot Managed Runtime**.
3. Add the **Environment**, **Environment ID**, **Environment Group**, and **Environment Group ID** columns.

## Are newly created personal environments managed environments?

Yes. Personal environments created through environment routing are always managed environments. Learn more in [Environment routing for Copilot Managed Runtime](/en-us/power-platform/admin/default-environment-routing-copilot-managed-runtime).

## Will Copilot Managed Runtime disrupt my existing routing rules or environment groups?

No. Copilot Managed Runtime preserves your existing routing rules, rule priority, and target environment groups.

## What happens if no routing rule matches a maker?

An unmatched maker can't get a personal environment or create an app with Copilot Managed Runtime.

To resolve the issue, add the maker to a security group targeted by an existing routing rule, update a rule to include one of the maker's groups, or add an **Everyone** catch-all rule.

## When does the service initialize Copilot Managed Runtime governance?

Default governance, including the default environment group, is set up once, triggered by whichever comes first: a maker starts to create the first app, or an administrator selects **Set up governance** on the **Apps** &gt; **Overview** page in the Microsoft 365 admin center. Either way, governance is in place before the first app exists. After governance is set up, the **Set up governance** option is no longer available.

## Can I delete or modify the existing **Everyone** catch-all routing rule after Copilot Managed Runtime governance is initialized?

No. After the service initializes Copilot Managed Runtime governance, you can't delete or modify the **Everyone** catch-all rule.

## Can I roll out app building to a pilot group first?

Yes. Each app building tool has its own control, so you can start with a small group of makers and expand access over time. For details, see [Copilot Managed Runtime overview for admins](./).

## Are all apps created in Cowork governed by Copilot Managed Runtime?

Apps that makers build with the app building skill in Cowork run on Copilot Managed Runtime. They're created in the maker's personal environment, appear in the app inventory in the Microsoft 365 admin center, and follow the policies of their environment group.

Other files that Cowork creates, such as HTML pages saved to OneDrive, aren't apps on Copilot Managed Runtime. They're governed like any other file in OneDrive or SharePoint and don't appear in the app inventory. To give makers a governed path for building apps, encourage them to use the app building skill. You can only govern what you can see.

## Users report errors when they run an app. How can I help?

Check the app's operational health in the Microsoft 365 admin center:

1. Go to **Apps** &gt; **All apps** and select the app.
2. Select the **Monitor** tab to review health trends for the app.

To find issues before users report them, create an alert rule. Go to **Apps** &gt; **Monitor** and select **+New Alert Rule**. You're notified when an app's health crosses the thresholds that you define.

## Can administrators inspect an app's connectors, data sources, destinations, actions, dynamic endpoints, and effective user permissions?

In the Microsoft 365 admin center, go to **Apps** &gt; **All apps**, open the app, and select **Data & tools** to view its connectors, data sources, and dependencies.

Administrators can block or delete an app and restrict connectors or connector actions through policy. App access can be revoked separately, but no single operation removes both a person's app access and all permissions to the underlying data.

## How do I find and clean up unused or broadly shared apps?

Use the app inventory in the Microsoft 365 admin center to see how each app is used and who it's shared with. For more information, see [View and oversee apps across your tenant](inventory).

Based on what you find, you can:

- **Block** an app to stop people from opening it, while keeping the app and its data.
- **Delete** an app that's no longer used.

## Can I share an app through an organization-wide link, a security group, or with multiple recipients?

Yes. You can share an app directly with specific users or groups, including Microsoft Entra security groups, or through a **People in your organization** link. Direct sharing supports multiple recipients.

Sharing grants access to the app, but it doesn't grant access to the app's underlying data. Recipients still need the appropriate source permissions and connections. You can revoke direct access or a sharing link later. For more information, see [Share your app](../../../copilot-managed-runtime/developer/apps/share-app).

## What controls can administrators use to manage app sharing?

Administrators configure sharing rules for an environment group. These rules apply to every app in the group and control whether makers can share apps with everyone in the organization or with guest users. For more information, see [Review default governance settings for apps](governance#sharing).

## Why does a connector appear allowed in the Microsoft 365 admin center but remain blocked in the app?

This condition can occur when the environment group has an advanced connector policy (ACP) and **Advanced connector policies only** is off. In this mixed mode, both the ACP and applicable classic data policies are enforced, and the most restrictive setting takes precedence.

The Microsoft 365 admin center shows the ACP allow list but might not show restrictions imposed by data policies. Review the environment group's **Advanced connector policies only** setting and applicable data policies in the Power Platform admin center to determine the connector's effective access.

## Where can I find information about licensing and Copilot Credits?

For what makers and users need to build and run apps, and how to set up and monitor Copilot Credits, see [Manage licensing and Copilot Credits for apps on Copilot Managed Runtime](licensing-credits). For answers to common licensing questions, see [Copilot Managed Runtime licensing FAQ](licensing-faq).