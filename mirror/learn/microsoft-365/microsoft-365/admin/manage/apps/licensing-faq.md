---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Copilot Managed Runtime licensing FAQ (preview) - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/apps/licensing-faq?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Get answers to common questions about licensing and billing for building and running apps with Microsoft Copilot Managed Runtime, including Copilot Credits and Power Apps Premium.
ms.date: 2026-11-10T00:00:00.0000000Z
author: mihaelablendea
manager: tiffanyt
ms.author: mihaelab
ms.reviewer: mkaur
ms.topic: faq
ms.service: microsoft-365
ms.subservice: managed-apps-admin
ai-usage: ai-assisted
locale: en-us
document_id: 24d5ffbf-aef1-8982-34ae-9820e9be52da
document_version_independent_id: 24d5ffbf-aef1-8982-34ae-9820e9be52da
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/apps/licensing-faq.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/apps/licensing-faq
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/apps/licensing-faq.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 8e203185-14ca-2f12-c3ad-acbe8f5c47d0
---

# Copilot Managed Runtime licensing FAQ (preview) - Microsoft 365 admin | Microsoft Learn

[This article is prerelease documentation and is subject to change.]

Microsoft Copilot Managed Runtime hosts internal line-of-business apps that comply with your organization's governance policies from the moment they're created. This article answers common questions about the licenses and Copilot Credits that makers, developers, and users need to build and run these apps, and where administrators manage them.

For setup guidance, see [Manage licensing and Copilot Credits for apps on Copilot Managed Runtime](licensing-credits).

Important

This is a preview feature. These features are subject to supplemental terms of use, and are available before an official release so that customers can get early access and provide feedback.

## Licensing at a glance

| Activity | What's required | Where administrators manage billing |
| --- | --- | --- |
| Build an app in Cowork | A Microsoft Copilot license, plus Copilot Credits billed through a spending policy that includes Copilot Cowork | Microsoft 365 admin center |
| Build an app in Copilot Code | A Microsoft Copilot license, plus Copilot Credits billed through a spending policy that includes Copilot Code | Microsoft 365 admin center |
| Build an app in Copilot Studio | Copilot Credits billed through Copilot Studio billing for the environment | Power Platform admin center or Microsoft 365 admin center, depending on where the environment is in the move of Copilot Studio cost management |
| Build an app with the Copilot Managed Runtime CLI | No license required to create, build, or deploy | Not applicable |
| Run an app regardless of where you built it, including locally with the CLI | A Power Apps Premium license, or inclusion in a spending policy that includes Copilot Managed Runtime | Microsoft 365 admin center |

## General

### Do administrators need to buy or enable anything for Copilot Managed Runtime to be available in the tenant?

No. Eligible tenants in the commercial cloud get Copilot Managed Runtime automatically without a separate installation. Each app creation path has its own enablement default. For example, Copilot Studio app creation is on by default, while CLI app creation is off by default. For details, see [Enable Copilot Managed Runtime for your tenant](./#enable-copilot-managed-runtime-for-your-tenant).

### Are build costs and runtime costs billed together?

No. Building an app is billed through the product used to create it (Cowork, Copilot Code, or Copilot Studio). Running an app is billed per user through a spending policy that includes Copilot Managed Runtime in the Microsoft 365 admin center, irrespective of the tool used to build the app.

## Building apps

### How is building an app billed?

Building an app is billed through the product you use to create it, not through Copilot Managed Runtime:

- **Cowork and Copilot Code:** Copilot Credits, through a user-based spending policy in the Microsoft 365 admin center that includes Copilot Cowork or Copilot Code. For details, see [Get started with Copilot Cowork](/en-us/copilot/cowork/get-started) and [Get started with Copilot Code](/en-us/copilot/code/get-started).
- **Copilot Studio:** Apps are built with the Microsoft Copilot harness (formerly the GitHub Copilot harness), so billable activity starts during creation and includes natural-language authoring, testing, and evaluation. For details, see [Manage costs for agents powered by the Microsoft Copilot harness](/en-us/power-platform/admin/manage-usage-github-copilot-harness).

### Do makers need a Microsoft Copilot license to build apps?

It depends on the tool:

- **Cowork and Copilot Code:** Makers need a Microsoft Copilot license to access these tools. The license doesn't include Cowork or Copilot Code usage, which is billed through Copilot Credits.
- **Copilot Studio:** No. Building is billed through Copilot Studio billing for the environment.
- **Copilot Managed Runtime CLI:** No license is needed to create, build, or deploy an app.

### Do developers who use the Copilot Managed Runtime CLI need a license?

Yes, but only to run an app locally. Other CLI development activities, such as creating, building, and deploying an app, don't require a license. To run an app locally, developers need the same coverage as any other user: a Power Apps Premium license or inclusion in a spending policy that includes Copilot Managed Runtime.

### Do makers need a Power Apps Premium license because their personal developer environment is a managed environment?

No. Personal developer environments created for Copilot Managed Runtime are managed environments. However, license auto-claiming doesn't apply to makers who use these environments only to create apps hosted on Copilot Managed Runtime. These makers don't need a premium license. If makers also build Power Apps or Power Automate flows in the same personal developer environment, license auto-claiming applies, and they might need a premium license. For more information, see [Environment routing for Copilot Managed Runtime](/en-us/power-platform/admin/default-environment-routing-copilot-managed-runtime).

## Running apps

### What do users need to run an app?

Users need one of the following:

- **A Power Apps Premium license.** Running apps doesn't consume Copilot Credits.
- **Inclusion in a spending policy that includes Copilot Managed Runtime.** Usage is billed in Copilot Credits, up to the policy's per-user and policy limits.

These requirements apply to every user who runs an app, regardless of the tool used to build it, and to developers who run apps locally with the CLI. Users also need permissions and connections for the app's underlying data.

### Which actions consume Copilot Credits?

Copilot Managed Runtime measures app usage in Copilot Credits. Credits are consumed by the API calls an app makes, at 0.1 Copilot Credits per call (1 credit covers 10 API calls). Actions that count as API calls include:

- **Launching an app.** Each static asset the app loads at launch, such as a script, style sheet, or image, counts as one API call, so a single launch can make several calls.
- **Calling data through a connector,** such as reading or writing records. Each call counts as one API call.
- **Calling data sources, including Dataverse.** Each call counts as one API call.
- **Publishing an app.**

Specialized services that an app uses, such as Work IQ APIs, are charged separately at their own rates. For the authoritative metric and rate, see the [Copilot Credits Guide](https://go.microsoft.com/fwlink/?linkid=2368800).

### How much does it cost to run an app?

US$1 buys 100 Copilot Credits, which cover about 1,000 API calls. For most users, a per-user limit of 100 credits (US$1) a month covers typical use, often several hundred app launches depending on how many assets each app loads and how much data it reads and writes. For worked examples, see [Estimate runtime costs](licensing-credits#estimate-runtime-costs).

### Do Power Apps Premium users also need Copilot Credits?

Users with a Power Apps Premium license don't consume Copilot Credits when they run apps. Their API calls count toward the daily [Power Platform request limits](/en-us/power-platform/admin/api-request-limits-allocations) for their license. Reaching those limits is unlikely, but usage above them is billed through Copilot Credits. Specialized services, such as Work IQ APIs, are still charged at their own rates.

### If a user has Power Apps Premium and is also in a spending policy, are they charged credits?

No. When a user has both a Premium license and coverage through a spending policy that includes Copilot Managed Runtime, the license is used first, and running apps doesn't consume Copilot Credits. The policy is used only for usage the license doesn't cover, such as specialized services or usage above the daily Power Platform request limits. You don't need to exclude Premium users from a broad runtime policy.

### Can users run apps with Power Apps use rights included in Microsoft 365 or Dynamics 365?

No. Power Apps use rights included with Microsoft 365 or Dynamics 365 licenses (for example, Microsoft 365 E3 or E5) don't cover apps hosted on Copilot Managed Runtime, regardless of the type of connector the app uses. These users need a Power Apps Premium license or inclusion in a spending policy that includes Copilot Managed Runtime.

### Do users need a Microsoft 365 Copilot license to run an app?

No. A Copilot license isn't required to run apps, and on its own it doesn't cover runtime. Users need a Power Apps Premium license or inclusion in a spending policy that includes Copilot Managed Runtime.

### Does sharing an app give recipients a license to run it?

No. Sharing an app gives people access to it, but it doesn't cover the cost of running it. Each person running the app also needs a Power Apps Premium license or must be included in a spending policy that includes Copilot Managed Runtime, plus permissions and connections for the app's underlying data.

### Does Copilot Studio environment billing cover running an app built in Copilot Studio?

No. Copilot Studio billing for the environment covers building the app. Running it is billed through a spending policy that includes Copilot Managed Runtime in the Microsoft 365 admin center, the same as for apps built with any other tool.

### What happens when a user isn't covered or reaches their limit?

During preview, users who don't meet the credit requirements to run an app first see a warning, and access is blocked after 20 app operations or five minutes of use, whichever comes first. Users can select **Request more** inside the app to ask for credits. Administrators review these requests in **Cost management** in the Microsoft 365 admin center. Per-user limits reset on the first of each month.

## Managing costs

### What do administrators need to set up so users can run apps?

If users don't have a Power Apps Premium license, set up these items in the Microsoft 365 admin center:

1. Turn on usage-based billing for Copilot Credits.
2. Create a spending policy that selects the **Copilot Managed Runtime** service and includes the users or groups who run apps.
3. Set the per-user limit, policy limit, and alerts.

For step-by-step guidance, see [Manage licensing and Copilot Credits for apps on Copilot Managed Runtime](licensing-credits) and [Set up usage-based billing for Copilot Credits](/en-us/microsoft-365/copilot/usage-based-billing-copilot-credits-setup).

### What's the recommended way to cover users?

Start with one spending policy that covers all users, selects Copilot Managed Runtime, and sets a per-user limit such as 100 credits (US$1) a month. Apps are often shared beyond the maker's team, so a broad policy means people can open an app as soon as it's shared with them. You don't need to work out who has a Power Apps Premium license first, because their license is used before credits. Add separate policies with higher per-user limits for groups that use apps heavily.

### Does a spending policy reserve or prepay credits?

No. Spending policies are limits, not purchases. A policy doesn't reserve or allocate credits to anyone, and you pay only for what's actually consumed. Deleting a policy doesn't refund or reallocate credits.

### How are prepaid credits, P3, and pay-as-you-go applied?

When you select more than one billing method, the billing uses them in this order: prepaid capacity packs, the Copilot Credit Pre-Purchase Plan (P3), and pay-as-you-go. Turn on a pay-as-you-go meter so users aren't blocked when prepaid credits run out. For details, see [Set up usage-based billing for Copilot Credits](/en-us/microsoft-365/copilot/usage-based-billing-copilot-credits-setup).

### What happens if a user is in more than one spending policy?

If a user is in more than one policy for the same service, the policy with the highest per-user limit applies. Ties go to the largest overall policy limit, then to the most recently created policy. Settings from different policies aren't combined, and when a user reaches their limit, they don't fall back to another policy. Moving a user to another group mid-month doesn't reset their consumption. For details, see [Managing AI experiences enabled by usage-based billing](/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits).

### Which admin roles can manage spending policies?

In the Microsoft 365 admin center, Global Administrators and Billing Administrators can turn on usage-based billing and create spending policies. AI Administrators and License Administrators can edit existing policies, limits, and alerts, but can't create policies. Reader roles, such as AI Reader and Global Reader, can view consumption. To manage Copilot Studio capacity in the Power Platform admin center, you need the Power Platform Administrator or Global Administrator role.

### Where do administrators manage credits for building apps?

In the product where the app is built:

- **Cowork and Copilot Code:** In the Microsoft 365 admin center, under **Copilot** &gt; **Cost management**, in a spending policy that includes Copilot Cowork or Copilot Code.
- **Copilot Studio:** Copilot Studio cost management is moving from the Power Platform admin center to the Microsoft 365 admin center. For environments still managed in the Power Platform admin center, allocate credits per environment. For details, see [Manage costs for agents powered by the Microsoft Copilot harness](/en-us/power-platform/admin/manage-usage-github-copilot-harness). For environments managed in the Microsoft 365 admin center, use a resource-based spending policy. For details, see [Manage Copilot Studio costs in the Microsoft 365 admin center](/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-studio-costs). To see which experience manages an environment, open **Manage capacity** in the Power Platform admin center.

### Where do administrators manage runtime credits and monitor consumption?

In the Microsoft 365 admin center, go to **Copilot** &gt; **Cost management**. You can create spending policies that include Copilot Managed Runtime, select covered users and groups, set policy-level and per-user limits and alerts, review credit requests, and monitor consumption by policy, service, and user. For more information, see [Managing AI experiences enabled by usage-based billing](/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits).

### Can I scope runtime spending to a specific app?

No. Apps can't be selected individually in a spending policy. Cover the users who run the app instead.