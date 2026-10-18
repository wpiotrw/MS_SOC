---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: FAQ about Microsoft Copilot Managed Runtime (preview) - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/apps/faq-about-apps?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Microsoft Copilot Managed Runtime
ms.date: 2026-09-25T00:00:00.0000000Z
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
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 95be2335-c6f4-6697-810a-4454edf8ee94
---

# FAQ about Microsoft Copilot Managed Runtime (preview) - Microsoft 365 admin | Microsoft Learn

## Where are apps built with Copilot Managed Runtime created?

Apps built with Copilot Managed Runtime are created in personal developer environments. If a maker already owns one, the app reuses it. Otherwise, the app creates a new personal developer environment based on your existing environment routing rules.

## Where can I find the environment that hosts an app built with Copilot Managed Runtime?

Use the Power Platform admin center to find the environment that hosts an app built with Copilot Managed Runtime:

1. Go to **Manage** &gt; **Inventory**.
2. Set **Item type** to **Copilot Managed Runtime**.
3. Add the **Environment**, **Environment ID**, **Environment Group**, and **Environment Group ID** columns.

## Are newly created personal developer environments managed environments?

Yes. Personal developer environments created through environment routing are always managed environments. Learn more in [Environment routing](/en-us/power-platform/admin/default-environment-routing).

## Will Copilot Managed Runtime disrupt my existing routing rules or environment groups?

No, Copilot Managed Runtime preserves your existing routing rules, rule priority, and target environment groups.

## What happens if no routing rule matches a maker?

An unmatched maker can't get a personal developer environment or create an app with Copilot Managed Runtime.

To resolve the issue, add the maker to a security group targeted by an existing routing rule, update a rule to include one of the maker's groups, or add an **Everyone** catch-all rule.

## When does the service initialize Copilot Managed Runtime governance?

The service initializes Copilot Managed Runtime governance when you create the first app. An administrator can initialize it earlier by opening the app governance experience in the Microsoft 365 admin center.

## Can I delete or modify the existing **Everyone** catch-all routing rule after Copilot Managed Runtime governance is initialized?

No. After the service initializes Copilot Managed Runtime governance, you can't delete or modify the **Everyone** catch-all rule.

## Can I turn off environment routing only for apps created in Cowork?

No. You can't turn off environment routing for apps created in Cowork.

## Can administrators keep Copilot Cowork available while disabling app creation or limiting it to selected users?

Yes. During preview, building apps in Copilot Cowork is available only in Frontier tenants. The app-building skill respects the tenant and user access settings for Frontier. For more information, see [Get started with the Microsoft Copilot Frontier Program](../get-started-frontier).

## Do users need Microsoft 365 Copilot to run an app created in Cowork?

No. A user's runtime eligibility is based on Copilot Credits or a Power Apps Premium license. Runtime entitlement is separate from the requirements and charges for creating the app.

## Application users are telling me that there are errors while running the app. How can I help?

Monitor in the Microsoft 365 admin center is the place for IT and Operations teams to check the operational health of managed apps created in your tenant. They can understand operational health trends per app in addition to creating alerts to proactively monitor the health of their managed apps against custom thresholds they define. To find operational health trends for apps, go to **Apps** &gt; **All Apps**, select the app, and go to the **Monitor** tab. To create alerts, go to **Apps** &gt; **Monitor** and then select **+New Alert Rule**.

## Where can administrators allocate credits and monitor the credits that running apps consume?

In the Microsoft 365 admin center, go to **Copilot** &gt; **Cost management**. You can configure spending policies for managed applications, select covered users and groups, set limits, allocate credits, and monitor consumption. For more information, see [Usage-based billing and cost management for Copilot Credits](/en-us/microsoft-365/copilot/usage-based-billing-overview-copilot-credits).

## Can administrators inspect an app's connectors, data sources, destinations, actions, dynamic endpoints, and effective user permissions?

In the Microsoft 365 admin center, go to **Apps** &gt; **All apps**, open the app, and select **Data & tools** to view its connectors, data sources, and dependencies. This information doesn't provide a complete view of exact destinations, dynamically resolved endpoints, actions that the app executed, or each user's permissions to the underlying data.

Administrators can block or delete an app and restrict connectors or connector actions through policy. App access can be revoked separately, but no single operation removes both a person's app access and all permissions to the underlying data.

## Can I share an app through an organization link, a security group, or with multiple recipients?

Yes. You can share an app directly with specific users or groups, including Microsoft Entra security groups, or through a **People in your organization** link. Direct sharing supports multiple recipients.

Sharing grants access to the app, but it doesn't grant access to the app's underlying data. Recipients still need the appropriate source permissions and connections. You can revoke direct access or a sharing link later. For more information, see [Share your app](../../../managed-apps/developer/share-app).

## What controls can administrators use to manage app sharing?

Administrators configure sharing rules for an environment group. These rules apply to every app in the group and control whether makers can share apps with everyone in the organization or with guest users. For more information, see [Review default governance settings for apps](governance#sharing).

## Why does a connector appear allowed in the Microsoft 365 admin center but remain blocked in the app?

This condition can occur when the environment group has an advanced connector policy (ACP) and **Advanced connector policies only** is off. In this mixed mode, both the ACP and applicable classic data policies are enforced, and the most restrictive setting takes precedence.

The Microsoft 365 admin center shows the ACP allow list but might not show restrictions imposed by data policies. Review the environment group's **Advanced connector policies only** setting and applicable data policies in the Power Platform admin center to determine the connector's effective access.