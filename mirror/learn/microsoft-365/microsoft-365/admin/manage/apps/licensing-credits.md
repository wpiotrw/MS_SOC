---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Manage licensing and Copilot Credits for apps on Copilot Managed Runtime - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/apps/licensing-credits?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn about managing licensing and Copilot Credits for apps on Copilot Managed Runtime, including how they are billed, setting up spending policies, and reviewing usage.
ms.date: 2026-11-09T00:00:00.0000000Z
author: mikferland-msft
ms.author: miferlan
manager: zoraz
ms.reviewer: mkaur
contributors:
- sidhartg
- mihaelablendea
- laneswenka
- praveenmantha
- jordanchodakWork
- caburk
ms.topic: how-to
ms.service: microsoft-365
ms.subservice: managed-apps-admin
ai-usage: ai-assisted
locale: en-us
document_id: 043e6d2b-0e60-2a66-c786-5ad9b3f760b0
document_version_independent_id: 043e6d2b-0e60-2a66-c786-5ad9b3f760b0
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/apps/licensing-credits.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/apps/licensing-credits
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/apps/licensing-credits.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c389ea6b-b6a0-46df-93a1-1e21f25e19e7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/19ada1b6-705b-4ed7-aad0-bffd1bd03dfa
platformId: 5c73d487-0ac5-a2dc-ecb7-b1e856478418
---

# Manage licensing and Copilot Credits for apps on Copilot Managed Runtime - Microsoft 365 admin | Microsoft Learn

Apps built on Copilot Managed Runtime use consumption-based billing through Copilot Credits. Building an app and running an app are billed separately, through different policies. This article explains what makers and app users need and what administrators set up in the Microsoft 365 admin center and/or the Power Platform admin center so that makers can build and users can run the apps shared with them.

## Key steps for admins

1. **Enable users to run apps.** In the Microsoft 365 admin center, create one spending policy that covers all users, selects Copilot Managed Runtime, and sets a per-user limit of 100 credits (US$1) a month. This step unblocks most users who can't open an app that was shared with them. For details, see Step 1: Turn on usage-based billing and Step 2: Create a broad Copilot Managed Runtime spending policy.
2. **Give heavier users higher limits.** Add policies for specific groups with higher limits, for example 1,000 credits (US$10) a month. For details, see Step 3: Add cohort policies for heavier use and Choose your approach.
3. **Enable makers to build apps.** Cover makers with the tool they use: a spending policy for Cowork or Copilot Code in the Microsoft 365 admin center, or Copilot Studio credits in the Power Platform admin center or Microsoft 365 admin center, depending on where your organization is with the move to Copilot Studio cost management. For details, see Enable makers to build.
4. **Monitor usage and handle requests.** Set alerts, review consumption, and approve the credit requests that users send from apps. For details, see Monitor and adjust and Establish an access and credit request process.

Spending policies are limits, not purchases. A policy doesn't reserve or allocate credits to anyone, and you pay only for what is actually consumed. For an estimate, see Estimate runtime costs.

## Licensing at a glance

| Activity | What's required | Where admins manage billing |
| --- | --- | --- |
| Build an app in Cowork | A Microsoft Copilot license and Copilot Credits billed through the maker's Cowork spending policy | Microsoft 365 admin center |
| Build an app in Copilot Code | A Microsoft Copilot license, plus Copilot Credits billed through a spending policy that includes Copilot Code | Microsoft 365 admin center |
| Build an app in Copilot Studio | Copilot Credits billed through Copilot Studio billing for the environment | Power Platform admin center or Microsoft 365 admin center, depending on where the environment is in the move (see Copilot Studio under Enable makers to build) |
| Build an app with the Copilot Managed Runtime CLI | No license required to create, build, or deploy | Not applicable |
| Run an app, regardless of where you build it | A Power Apps Premium license or Copilot Credits through a spending policy that includes Copilot Managed Runtime | Microsoft 365 admin center |

## Before you begin

To turn on usage-based billing and create spending policies, go to **M365 admin center** &gt; **Copilot** &gt; **Cost management**. You need the Global Administrator or Billing Administrator role. AI Administrators and License Administrators can edit existing spending policies, limits, and alerts, but can't create policies. Reader roles, such as AI Reader and Global Reader, can view consumption dashboards and reports.

To manage Copilot Studio capacity for building in the Power Platform admin center, you need the Power Platform Administrator or Global Administrator role. For Copilot Studio environments managed in the Microsoft 365 admin center, the roles listed for accessing the Cost Management experiences above are still required. Microsoft recommends giving the Billing administrator role to Power Platform administrator who will manage these policies, and the AI Reader role to environment administrators who need to view consumption.

Before you configure anything, check:

- Who builds apps today and which tool they use: Cowork, Copilot Code, Copilot Studio, or the CLI.
- Who runs apps. Assume the app user population is much broader than the maker population because makers share apps with their teams and departments.
- Which users already have a Power Apps Premium license.
- Whether your Copilot Studio environments are still managed in the Power Platform admin center or are managed in the Microsoft 365 admin center.
- Which billing method you will use: prepaid [capacity packs](/en-us/copilot/implement/copilot-capacity-packs), a Copilot Credit [Pre-Purchase Plan (P3)](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/MicrosoftCopilotStudioLicensingGuide.pdf), [pay-as-you-go](/en-us/copilot/implement/setup-pay-as-you-go) through an Azure subscription, or a combination.
- Who reviews consumption and responds to alerts, and how users ask for more credits.

## Enable users to run apps

Apps are often shared with users beyond the maker who built the app, such as their team or department. To run the app, each user need either a Power Apps Premium license or inclusion in a spending policy with Copilot Managed Runtime.

The simplest approach is one spending policy for all users, with a small per-user limit such as 100 credits (US$1) a month. You don't need to identify users who have a Power Apps Premium license first. When a user has both a Premium license and coverage through a spending policy, Premium is used and the user's app usage doesn't consume Copilot Credits. Setting this up before apps are widely shared means users can open them as soon as they need to run them.

### How running apps is billed

To set up spending policies for runtime, use the Copilot Managed Runtime service in the Microsoft 365 admin center under **Copilot** &gt; **Cost management**, regardless which tool is used to build the app. For example, an app built in Copilot Studio is billed through Copilot Studio billing for build and through Copilot Managed Runtime service for runtime. The environment-based billing policy for Copilot Studio doesn't cover credits needed to run the app.

Copilot Managed Runtime measures app usage in Copilot Credits. Credits are consumed by the API calls an app makes, at 0.1 Copilot Credits per call (1 credit covers 10 API calls). Actions that count as API calls include:

- **Launching an app.** Each static asset the app loads at launch, such as a script, style sheet or image, counts as one API call, so a single launch can make several calls.
- **Calling data through a connector**, such as reading or writing records. Each call counts as one API call.
- **Calling native data sources, including Dataverse.** Each call counts as one API call.
- **Publishing an app.**

Apps that use specialized services, like Work IQ APIs, are charged separately at their own rates. For the authoritative metric and rate, see the [Copilot Credits Guide](https://go.microsoft.com/fwlink/?linkid=2368800).

| User has | Runs apps? | What is billed |
| --- | --- | --- |
| Power Apps Premium license | Yes | Nothing for normal use. API calls count toward the daily [Power Platform request limits](/en-us/power-platform/admin/api-request-limits-allocations#licensed-user-request-limits) for the license. Though it is highly unlikely for these limits to be reached, usage above those limits is billed through Copilot Credits. Specialized services such as Work IQ are still charged. |
| Coverage in a spending policy that includes Copilot Managed Runtime | Yes | 0.1 Copilot Credits per API call, up to the policy's per-user and policy limits |
| Power Apps use rights included with Microsoft 365 or Dynamics 365 | No | These use rights don't cover apps on Copilot Managed Runtime, regardless of connector type |
| Microsoft 365 Copilot license only | No | A Copilot license isn't required to run apps, and on its own it doesn't cover runtime |
| Access to an app that was shared with them | Not by itself | Sharing an app gives users access to it, but it doesn't cover the cost of running it. Each person **running the app** also needs a Power Apps Premium license or must be included in a spending policy that includes Copilot Managed Runtime, plus permissions and connections for the app's underlying data. |

The following steps set up runtime coverage in the Microsoft 365 admin center. Start with Steps 1 and 2 to cover everyone in your organization, then use Steps 3 and 4 to adjust coverage for specific groups and tell users how it works.

### Step 1: Turn on usage-based billing

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com) as a Global Administrator or Billing Administrator.
2. Go to **Copilot** &gt; **Cost management** and select **Get started**.
3. In **Billing method**, select the subscription to bill for Copilot Credit usage. If your tenant has prepaid capacity packs or a P3 plan, the service uses them first.
4. Set the monthly spending limit and alerts for the default spending policy, and review **Auto-apply new services**.

When prepaid capacity packs and a P3 plan are both selected, billing applies in this order: prepaid capacity packs, then the Copilot Credit Pre-Purchase Plan (P3), then pay-as-you-go. Turn on a pay-as-you-go meter so users aren't blocked when prepaid credits run out.

For more details, see [Getting started with usage-based billing](/en-us/microsoft-365/copilot/usage-based-billing-copilot-credits-setup#getting-started-with-usage-based-billing) and [Configure billing method](/en-us/microsoft-365/copilot/usage-based-billing-copilot-credits-setup#configure-billing-method).

### Step 2: Create a broad Copilot Managed Runtime spending policy

Create one policy for everyone in your organization with whom you might share the app.

1. Go to **Copilot** &gt; **Cost management** &gt; **Configuration** and select **+ Add spending policy**.
2. Name the policy, for example "CMR apps runtime for all users". Keep **All users** selected as the scope.
3. In **Select agents and services**, select **Copilot Managed Runtime**. This service covers running apps on Copilot Managed Runtime, regardless of which tool was used to build them.
4. Set a monthly per-user limit. For example, start with 100 credits per user per month (US$1), which covers about 1,000 API calls. That's typically several hundred app launches, depending on how many assets each app loads and how much data it reads and writes. Set the policy limit at or above the required minimum for the users the policy covers.
5. Configure policy-level alerts and, optionally, user notifications as users approach their limit.
6. Review the billing method, then select **Create spending policy**. The policy starts applying to the users in scope immediately.

> 
> **Include Power Apps Premium users.** You don't need to exclude users who have a Power Apps Premium license. When a user has both a Premium license and coverage through this policy, the license is used first, and running apps doesn't consume Copilot Credits. Their credits are used only for usage the license doesn't cover, such as specialized services like Work IQ APIs or usage above the daily Power Platform request limits for the license.

### Step 3: Add cohort policies for heavier use

Some groups run apps much more than others: a department that adopts a shared app, a team running a line-of-business app all day, or an operations group whose apps make many connector calls. Create a separate policy scoped to a security group for each, with a higher per-user limit, and its own alerts.

How overlapping policies resolve:

- If a user is in more than one policy for the same service, the policy with the highest per-user limit applies. Ties go to the largest overall policy limit, then to the most recently created policy. Settings from different policies aren't combined.
- When a user reaches their limit, they don't fall back to another policy. They can request more credits.
- Moving a user to another group mid-month doesn't reset their consumption. Credits consumed under the earlier policy count against the new policy's limit.
- Limits reset on the first of the month.

For details, see "How spending policies apply to users" in [Managing AI experiences enabled by usage-based billing](/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits).

### Step 4: Tell makers and users how it works

Tell makers which groups are covered by runtime policies, and that the users they share an app with need their own coverage to run it. For details, see How running apps is billed. Publish how users request more credits, for details, see Establish an access and credit request process.

## Choose your approach

| Approach | Policy setup | Use when | Watch out for |
| --- | --- | --- | --- |
| Broad baseline (recommended start) | One policy, All users, Copilot Managed Runtime selected, 100 credits (US$1) per user per month | You want shared apps to just work and to learn real usage before tuning | Monitor the first month and adjust; set alerts |
| Broad baseline plus cohorts | Baseline policy plus group policies with higher per-user limits, for example 1,000 credits (US$10) | Some departments or apps have heavier, predictable use | Highest per-user limit wins for overlapping users |
| Restricted | Policies for specific groups only | You deliberately limit who can run apps during a pilot | Users outside the groups are blocked, including users a maker shares an app with. Tell makers who is in scope. |

## Estimate runtime costs

Runtime is usually a small part of total app consumption. Use these examples to set expectations.

The first example shows a simple app with each launch as one API call plus the stated number of data calls over 22 working days per month. Real launches can make more calls, depending on the assets the app loads. US$1 buys 100 Copilot Credits, and each credit covers 10 API calls.

| Example | Users | Usage per user | Credits per user per month | Total credits per month | Approximate cost per month |
| --- | --- | --- | --- | --- | --- |
| Personal productivity app | 1 | 3 launches a day, 5 data calls each | 39.6 | 39.6 | US$0.40 |
| Team tracker | 25 | 2 launches a day, 10 data calls each | 48.4 | 1,210 | US$12.10 |
| Department request app | 300 | 1 launch a day, 8 data calls each | 19.8 | 5,940 | US$59.40 |

The second example uses a more conservative estimate of 10 API calls per launch:

| Example | **Users** | **Usage per user** | **Credits per user per month** | **Total credits per month** | **Approximate cost per month** |
| --- | --- | --- | --- | --- | --- |
| Personal productivity app | 1 | 3 launches a day, 5 data calls each | 99 | 99 | US$0.99 |
| Team tracker | 25 | 2 launches a day, 10 data calls each | 88 | 2,200 | US$22.00 |
| Department request app | 300 | 1 launch a day, 8 data calls each | 39.6 | 11,880 | US$118.80 |

For scale: US$1 (100 credits) covers about 1,000 API calls. Each user in all examples stays within a 100-credit monthly limit, even if each launch makes up to 10 API calls.

Specialized services such as Work IQ APIs are billed on top of these figures at their own rates.

## Enable makers to build

Building an app is billed through the surface maker used to create it, not through Copilot Managed Runtime spending policy.

### Cowork and Copilot Code

1. Make sure each maker has a Microsoft Copilot license to access Cowork and Code tools. The license doesn't include Cowork or Code usage, which is billed through Copilot Credits, and making Cowork or Code discoverable alone doesn't let users start building.
2. In the Microsoft 365 admin center, go to **Copilot** &gt; **Cost management** and turn on usage-based billing if it isn't already on (see Step 1 in the next section).
3. Create or edit a user-based spending policy that includes the makers, or a security group that contains them, and select **Copilot Cowork** and **Copilot Code**.
4. Set a monthly per-user limit and alerts. Building is the most credit-intensive part of the lifecycle, so size build limits separately from runtime limits.

### Copilot Studio

Apps in Copilot Studio are built with the Microsoft Copilot harness (formerly the GitHub Copilot harness), so billable activity starts during creation and includes natural-language authoring, testing, and evaluation.

Copilot Studio cost management is moving from the Power Platform admin center to the Cost management experience in the Microsoft 365 admin center. Where you manage credits for building apps in Copilot Studio depends on where each environment is in that move.

- **Environments still managed in the Power Platform admin center.** Credits for building apps are managed per environment, the same way as for Copilot Studio agents on the Microsoft Copilot harness. Allocate Copilot Credits to the environments where makers build (including their personal environments), set overage behavior, and set limits. For details, see [Manage costs for agents powered by the GitHub Copilot harness](/en-us/power-platform/admin/manage-usage-github-copilot-harness). This guidance covers agents, workflows, and apps powered by the Microsoft Copilot harness (formerly the GitHub Copilot harness), which is the only option supported by Copilot Studio to build apps.
- **Environments managed in the Microsoft 365 admin center.** Under **Copilot** -&gt; **Cost management**, create a resource-based spending policy that covers specific environments, or all environments. For the environments it covers, the policy replaces the Power Platform admin center capacity allocations and linked billing plans. Apps can't be selected individually, so cover them with a policy for the environment where they're deployed. For details, see [Manage Copilot Studio costs in the Microsoft 365 admin center](/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-studio-costs).

To see which experience manages an environment, open **Manage capacity** in the Power Platform admin center. It shows when an environment's Copilot Credits are managed by a policy in the Microsoft 365 admin center.

After the move, admins will be able to set policies in the Microsoft 365 admin center for both building and running, scoped to users or to environments. The following table shows the policy scopes for apps built in Copilot Studio after the move.

| Policy scope in the Microsoft 365 admin center | Build apps in Copilot Studio | Run apps |
| --- | --- | --- |
| Users or security groups (identity-based policy) | Not available | Available, through a policy that includes Copilot Managed Runtime |
| Specific environments or all environments (resource-based policy) | Available | Runtime events don’t count towards a per environment spending policy. |
| Individual apps | Not available | Not available |

### Building apps using the CLI and Copilot Runtime SDK

Developers don't need a license to build apps with the CLI. To run the app, a developer needs the same coverage as any other user: a Power Apps Premium license or inclusion in a spending policy that includes Copilot Managed Runtime.

## Monitor and adjust

- Use **Copilot** &gt; **Cost management** in the Microsoft 365 admin center to review consumption by policy, service, and user, and adjust limits.
- Set policy alerts to budget owners. Alert emails start when usage reaches the threshold and continue daily until the period resets or the policy changes.
- Deleting a spending policy doesn't refund or reallocate credits. Spending policies define access and limits only, and past usage stays in reports.

During preview, users who don't meet the credit requirements to run an app first see a warning, and access is blocked after 20 app operations or five minutes of use, whichever comes first.

## Establish a credit request process

Users who aren't covered or reach their limit can request more credits in the app by selecting **Request more**. Admins review and manage these requests in **Cost management** in the Microsoft 365 admin center, alongside spending policies and consumption.

To handle requests consistently, decide and publish:

- Who approves higher limits for a user or group.
- How makers request coverage for an app they plan to share widely.
- What business justification and expected usage a request should include.
- Who reviews consumption after a request is approved.

Pair restrictive limits with this request path so users know how to get unblocked.

## Troubleshoot blocked users

| Symptom | Likely cause | What to do |
| --- | --- | --- |
| Users see "You do not have enough credits to use this app" and nobody in the tenant has runtime coverage | Usage-based billing isn't turned on, or there is no spending policy that includes Copilot Managed Runtime | Complete Steps 1 and 2 |
| Some users can open an app, but others can't. | The runtime policy is scoped to a group, and the app was shared with users outside it | Add a broad baseline policy, or add those users to a covered group |
| A policy exists, but users are still blocked. | The policy doesn't select the Copilot Managed Runtime service (for example, it covers only Cowork) | Edit the policy and select Copilot Managed Runtime |
| A user ran apps earlier in the month but is now blocked. | The user reached their per-user limit or the policy reached its limit | Approve the credit request or raise the limit. Moving the user to another group doesn't reset consumption. |
| Users with Microsoft 365 E3 or E5 can't run apps | Power Apps use rights included with Microsoft 365 or Dynamics 365 don't cover Copilot Managed Runtime | Add them to a broad spending policy that covers all users and includes Copilot Managed Runtime (see Step 2). Users who also have Power Apps Premium aren't charged credits for normal use. |
| An app built in Copilot Studio is blocked for users even though the environment has credits | Environment allocations in the Power Platform admin center cover building, not app runtime | Create a runtime spending policy in the Microsoft 365 admin center |
| Users were running apps, then everyone is blocked | Prepaid credits are exhausted and no pay-as-you-go meter is set, or the policy limit was reached | Check the billing method and the policy limit in Cost management |