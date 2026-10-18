---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Set up the Standard or Targeted release options for Microsoft 365 services - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/release-options-in-office-365?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- CSH
ms.author: mabond
author: mkbond007
manager: dansimp
ms.reviewer: sangar
ms.date: 2026-10-07T00:00:00.0000000Z
audience: Admin
ms.topic: install-set-up-deploy
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier2
- M365-subscription-management
- Adm_O365
- Adm_TOC
- change-management
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
- tenant
search.appverid:
- BCS160
- MET150
- MOE150
- BEA160
- GEA150
ms.assetid: 3b3adfa4-1777-4ff0-b606-fb8732101f47
description: Learn how to set up the Targeted release option for new Microsoft 365 product and feature updates in the Microsoft 365 admin center.
locale: en-us
document_id: dd43f78a-7c74-5c56-c1f0-24deb342455f
document_version_independent_id: f7ed9828-2580-1b50-d126-003d222abb5e
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/release-options-in-office-365.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/release-options-in-office-365
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/release-options-in-office-365.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: bb197019-a91a-c1af-c30f-8cf241d7083c
---

# Set up the Standard or Targeted release options for Microsoft 365 services - Microsoft 365 admin | Microsoft Learn

Important

**In November 2026**, admins will no longer have the ability to enroll additional users or tenants in Targeted release. **In January 2027**, Targeted release will be retired and no longer available to use. For more information, see [Targeted release retirement](targeted-release-retirement).

We recommend configuring release preferences for Standard release and Deferred audiences to align with the new release model as Microsoft begins delivering an increasing number of major features through it before Targeted release is retired. For more information, see [Configure Standard and Deferred release options for Microsoft 365](configure-release-options).

With Microsoft 365, you receive new product updates and features as they become available instead of doing costly updates every few years. You can manage how your organization receives these updates. For example, you can sign up for an early release so that your organization receives updates first. You can designate that only certain individuals receive the updates. Or, you can remain on the default release schedule and receive the updates later. This article explains Targeted release and Standard release options and how you can use them for your organization.

If your organization is using Targeted release for Microsoft 365 services, you can continue to do so until its retirement as we drive towards our converged release strategy. We recommend configuring release preferences for Frontier, Standard release, and Deferred release audiences to align with the new release model as Microsoft begins delivering an increasing number of major features through it over time. Use the Microsoft Message Center to keep up with new products and services that use the new, audience-based release model. For information about modern release options for Microsoft 365, see [Configure Standard release and Deferred release for Microsoft 365 services](configure-release-options).

Important

The Microsoft 365 updates described in this article apply to New Outlook for Windows, Outlook on the web, OneDrive, SharePoint Online, Office for the web, Microsoft Teams, and Microsoft 365 admin center. These release options are targeted, best effort ways to release changes to Microsoft 365 but can't be guaranteed at all times or for all updates. They don't currently apply to services other than those listed previously. For information about release options for Microsoft 365 Apps, see [Overview of update channels for Microsoft 365 Apps](/en-us/deployoffice/overview-update-channels).

For customers in GCC, GCC High, and DoD environments, Standard release (general availability) remains the supported release option following the retirement of Targeted release. Currently, Deferred release and Frontier aren't available in government cloud environments. Check this article for future updates regarding availability.

## How release validation works

Any new release is first tested and validated by the feature team, then by the entire Microsoft 365 feature team, followed by all of Microsoft. At each release ring, Microsoft collects feedback and further validates quality by monitoring key usage metrics. This series of progressive validation is in place to make sure the worldwide-release is as robust as possible.

For significant updates, customers are initially notified by the [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap). As an update gets closer to rolling out, it's communicated through your [Microsoft 365 Message center](https://go.microsoft.com/fwlink/p/?linkid=2070717).

## Standard release

For Microsoft 365, **Standard release** is the default option where you and your users receive the latest updates when they're released broadly to all customers.

## Targeted release

By opting-in to **Targeted release**, you and your users can be the first to see the latest updates and help shape the product by providing early feedback. You can choose to have individuals or the entire organization receive updates early.

Important

Large or complex updates may take longer than others so that no users are adversely affected. There is no guarantee on the exact timeline of a release. Targeted release is currently available for customers with either the Office 365 GCC plan or the Office 365 GCC High plan and DoD plan for the following services: new Outlook, OneDrive, SharePoint in Microsoft 365, Microsoft 365 for web, Microsoft 365 admin center, and some components of Exchange Online.

Note

If you switch from Targeted release back to Standard release track, your users may lose access to features that haven't reached Standard release yet.

### Targeted release for entire organization

If you Set up the release option in the admin center for this option, all your users will get the Targeted release experience. For organizations with more than 300 users, we recommend using a test subscription for this option. For test subscription information, reach out to your Microsoft contact.

### Targeted release for selected users

If you Set up the release option in the admin center for this option, you can define specific users, usually power users, to receive early access to features and functionality.

It's important to ensure that your help desk is opted into Targeted release so that they have access to the Targeted release features needed to support your users.

Important

Some features only roll out on a per-organization basis, which means that the entire organization receives access to the feature at the same time. For features like this, it's not possible for selected users in the Targeted release program to get the feature early. This means that your organization won't be able to receive these features early if you have configured selected users in Targeted release. To make sure that you see all features in Targeted release, you'll need to configure Targeted release for the entire organization or set up a test organization.

## Benefits of Targeted release

Targeted release allows admins, change managers, or anyone else responsible for Microsoft 365 updates to prepare for the upcoming changes by letting them:

- Test and validate new updates before they're released to all users in the organization.
- Prepare user notification and documentation before updates are released worldwide.
- Prepare internal help-desk for upcoming changes.
- Go through compliance and security reviews.
- Use feature controls, where applicable, to control the release of updates to end users.

## Best practices for Targeted release

- Keep most users in Standard release and assign IT pros and power users to Targeted release to evaluate new features ahead of broader rollout. Targeted release users can then prepare user notifications, documentation, and the internal help desk before updates are released worldwide.
- Only assign specific users in Targeted release.
- If you need to test a feature in Targeted release with a larger group of users (or a tenant), consider using a test tenant instead of putting your entire organization in Targeted release.

## Set up the release option in the admin center

You can change how your organization receives Microsoft 365 updates by following these steps. You have to be a global admin in Microsoft 365 to opt in.

Important

Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

It can take up to 24 hours for the following changes to take effect in Microsoft 365. If you opt out of Targeted release after enabling it, your users might lose access to features that haven't reached the scheduled release yet.

1. In the Microsoft 365admin center, go to the **Settings** &gt; **Org Setting**, and under the [**Organization profile** tab](https://go.microsoft.com/fwlink/p/?linkid=2067339), choose **Release preferences**.
2. To opt out of Targeted release, select **Standard release**, then select **Save changes**.
3. To enable Targeted release for all users in your organization, select **Targeted release for everyone**, then select **Save changes**.
4. To enable Targeted release for some people in your organization, select **Targeted release for selected users**, then select **Save**.
5. Choose **Select users** to add users one at a time, or **Upload users** to add them in bulk.
6. When you're done adding users, select **Save**.

[![Screenshot: Showing the set up release option in the Microsoft 365 admin.](../../media/release_option_admincenter.png)](../../media/release_option_admincenter.png#lightbox)

## Prepare for Targeted release retirement

To align with the converged release options and to ready your organization for the retirement of Targeted release, review [Plan for the retirement of Targeted release in Microsoft 365](targeted-release-retirement). For answers to frequently asked questions about Targeted release and its retirement, see [Frequently asked questions about modern release options for Microsoft 365](release-options-faq).

Once Targeted release has been retired, users and tenants default to their assigned [Standard and Deferred release preferences](configure-release-options). If you don't configure these preferences, users and tenants enrolled in Targeted release default to Standard release when Targeted release is retired. Until then, they'll continue receiving Targeted release features. Microsoft won't automatically change your release preference settings.