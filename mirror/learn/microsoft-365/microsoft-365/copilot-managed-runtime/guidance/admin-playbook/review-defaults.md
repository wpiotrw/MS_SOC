---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Review and adjust the defaults for Copilot Managed Runtime governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/copilot-managed-runtime/guidance/admin-playbook/review-defaults?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/help/4021566/windows-10-send-feedback-to-microsoft-with-feedback-hub-app
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: true
uhfHeaderId: MSDocsHeader-M365-IT
description: Review the Copilot Managed Runtime governance defaults, learn when to change them, and find where to manage each one. For Microsoft 365 admins.
ms.topic: concept-article
ms.date: 2026-11-19T00:00:00.0000000Z
ms.author: yapatel
author: yashpatel22
manager: mihaelab
ms.service: microsoft-copilot
ai-usage: ai-generated
locale: en-us
document_id: dda5f650-7d2a-9099-0649-b47c41a331e2
document_version_independent_id: dda5f650-7d2a-9099-0649-b47c41a331e2
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/copilot-managed-runtime/guidance/admin-playbook/review-defaults.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: copilot-managed-runtime/guidance/admin-playbook/review-defaults
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/copilot-managed-runtime/guidance/admin-playbook/review-defaults.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 407bdfb8-c914-fac0-87c6-5d07b320a471
---

# Review and adjust the defaults for Copilot Managed Runtime governance | Microsoft Learn

Copilot Managed Runtime applies a default governance policy from the moment a maker creates the first app. This article covers nine governance areas. For each one, it describes the default, why you might change it, where to manage it, and a recommended starting point. Use it when you decide how strict or relaxed your organization's rules should be.

The recommendations suit a gradual rollout. They're optional, so adjust them to fit your organization's size, risk tolerance, and existing policies. For the day-0 summary of these defaults, see [What's in place on day 0 for Copilot Managed Runtime governance](day-zero). For roles and responsibilities, see [Before you start on Copilot Managed Runtime governance](before-start).

## Where to start

You don't need to configure anything before makers start building. Governance is set up automatically when a maker starts creating the first app, or when an admin selects **Set up governance** on the **Apps** &gt; **Overview** page in the Microsoft 365 admin center, whichever comes first.

The nine areas are grouped under three principles.

| Principle | Governance areas in this article |
| --- | --- |
| Safe by default | Who can create apps, where apps live, connectors and actions, content security policy, audit and sign-in |
| Govern at scale | Sharing, access, and licensing; inventory and Monitor |
| Balance control and productivity | Cost and spending policies; code, build, and release |

Most organizations start with three steps:

- Choose who can build apps, and with which tools.
- Review the default environment group settings.
- Set up licensing and billing so people can run the apps shared with them.

Change the other areas when your organization needs different rules.

## Safe by default: who can create apps

People can create apps through four paths: Copilot Cowork, Copilot Studio, Copilot Code, and the CLI and SDK. Each path has its own switch. A second gate, environment routing, decides whether a person gets a personal developer environment to build in. Both gates matter.

**Default:** Creation through Copilot Cowork, Copilot Studio, and Copilot Code is on. Creation through the CLI and SDK is off.

| Creation path | Where you control it |
| --- | --- |
| Copilot Cowork | Microsoft 365 admin center: **Copilot** &gt; **Cowork** &gt; **Settings** &gt; **Build apps in Copilot** |
| Copilot Studio | A PowerShell command. You can scope it to specific security groups. |
| Copilot Code | Cost controls. Users must be included in a spending policy for Copilot Code. |
| CLI and SDK | Power Platform admin center: **Copilot** &gt; **Settings** &gt; **Managed apps**, or an environment group rule |

Note

Environment admins can create apps with the CLI even when this setting is off.

**Recommendation:** Pilot first. Limit Copilot Studio creation to a pilot security group. Keep the CLI off until you have a developer group and an environment group for it. Treat Cowork and Copilot Code as gated by your organization's decision to allow access to those tools.

For configuration instructions, see [App building options](../../../admin/manage/apps/#app-building-options) and [Control whether apps can be created using the CLI](../../../admin/manage/apps/governance#control-whether-apps-can-be-created-using-the-cli).

## Safe by default: where apps live

Every app lives in an environment. Each maker automatically gets a personal environment. An environment group applies one set of rules to many environments, like a folder with a policy attached. Routing rules decide which environment a person lands in.

**Default:** A default environment group, scoped to Everyone, is created at first use. Microsoft manages it, and you can't delete it. It has four rules: routing, connectors and MCP servers, sharing, and content security policy. Personal environments are managed environments that start without Dataverse.

**Where to manage it:** In the Microsoft 365 admin center, go to **Apps** &gt; **Settings** &gt; **Environment groups**, and open the group to see its rules.

**Recommendation:** Keep personal builders in the default group. Like OneDrive, each maker gets a private space, and the group applies your rules to all of them. Don't remodel your Power Platform environment strategy on day 1. Create separate groups for team or organization-wide apps when you have real demand.

For routing details, see [Routing](../../../admin/manage/apps/governance#routing). For environment cleanup and owner departures, see [Manage the lifecycle of personal environments](../../../admin/manage/apps/personal-environments-lifecycle-copilot-managed-runtime).

## Safe by default: connectors, actions, and MCP servers

Apps reach business data through connectors. Each connector exposes actions. MCP servers do the same for an app's AI features. An advanced connector policy lets you allow or block at both levels. Approving a connector doesn't approve every action inside it.

**Default:** A Microsoft-curated policy allows selected first-party connectors and MCP servers, and blocks a set of high-risk actions. Third-party, custom, preview, deprecated, infrastructure, and admin connectors are excluded from the default policy, but you can edit the policy to suit your needs.

**Where to manage it:** In the Microsoft 365 admin center, go to **Apps** &gt; **Settings** &gt; **Environment groups** &gt; your group &gt; **Connectors and MCP servers**. You see an allow list, a blocked list, and an on/off toggle for each action.

**Recommendation:** Stay on the Microsoft-curated policy. Handle exceptions case by case. Approve the narrowest set of actions for the one environment group that needs it, and record who asked and why. Avoid **Edit this policy (full control)**, because Microsoft's automatic updates then stop.

For configuration instructions and the implications of changing the curated policy, see [Customize connectors and MCP servers](../../../admin/manage/apps/governance#connectors-and-mcp-servers-1).

## Safe by default: content security policy

An app's code runs in an isolated environment. It has two ways to reach outside services. Connectors go through the managed host and your connector policy. Direct browser requests are controlled by a content security policy.

**Default:** The policy is enforced and restrictive. An app can only load content from, and send requests to, its own origin.

**Where to manage it:** In the Microsoft 365 admin center, go to **Apps** &gt; **Settings** &gt; **Environment groups** &gt; your group &gt; **Content security policy**. The options are **Reporting for apps**, **Enforce content security policy**, and per-directive configuration.

**Recommendation:** Leave the default enforced. Allow only specific origins, never wildcards. In production, use report-only mode before you enforce a new rule.

For default directives, see [Content security policy](../../../admin/manage/apps/governance#content-security-policy). For configuration instructions, see [Customize content security policy](../../../admin/manage/apps/governance#content-security-policy-1).

## Safe by default: audit and sign-in

Microsoft Entra ID signs people in to every app, and your Conditional Access policies apply. Microsoft Purview is where you search audit records. Use Monitor to catch a problem and Purview to investigate.

**Default:** Every app uses Entra sign-in and authorization, with no setup per app. Audit records for app creation, launch, deletion, and governance changes appear in Purview. You can't change these defaults.

**Where to manage it:** Use the Microsoft Entra admin center for Conditional Access, security groups, and roles. Use the Microsoft Purview portal for audit search.

**Recommendation:** In your pilot, create, launch, and delete a test app. Then confirm you can find those events in Purview audit search.

For sign-in protections, see [App access requires sign-in and permission](../../managed-runtime-security-governance#app-access-requires-sign-in-and-permission). For audit permissions, event names, and search instructions, see [Audit app activities with Microsoft Purview](../../../admin/manage/apps/security-compliance#audit-app-activities-with-microsoft-purview).

## Govern at scale: sharing, access, and licensing

To run an app, a person must pass three separate gates. Passing one gate doesn't pass the others.

| Gate | Who controls it | What it decides |
| --- | --- | --- |
| 1. The app is shared with the person | App owner, within your sharing rules | Direct share, group share, or organization link |
| 2. Access to the underlying data and connections | Data owners | Whether the person can reach the SharePoint site, database, and so on |
| 3. A license to run | Billing or licensing admin, in cost management | Power Apps Premium license, or Copilot Credits through a spending policy |

**Default:** An app is private to its owner until shared. Owners can share with specific users, with groups (including Entra security groups), or with a **People in your organization** link, and they can revoke access later.

**Where to manage it:** In the Microsoft 365 admin center, go to **Apps** &gt; **Settings** &gt; **Environment groups** &gt; your group &gt; **Sharing**. These controls apply to every app in the group, not to individual apps.

| Sharing control | What it does |
| --- | --- |
| Anyone in the org (default) | Creators can generate a link that any member of the organization can open, and can still share with named users and groups. |
| Only the users and groups selected when the app is shared | Organization-wide links are turned off. Creators must add the users or groups who can open the app. |
| Allow guest users to open apps from shared links | Off by default. When selected, guest (B2B) users can also open apps from shared links. |

**Recommendation:** Start restrictive. Allow sharing with specific people and groups, treat guest access as an exception, and enable organization-wide sharing only when you're comfortable with how new apps are reviewed. Because "Anyone in the org" is the default, decide your position on day 1.

For configuration instructions, see [Customize sharing settings](../../../admin/manage/apps/governance#sharing-1). For runtime access requirements, see [Enable users to run apps](../../../admin/manage/apps/licensing-credits#enable-users-to-run-apps).

## Govern at scale: inventory and monitor

Every app appears in one tenant-wide list with its owner, status, region, and governing environment group. Open an app to see usage, health, and what it connects to, or to block or delete it. The list shows what exists. It isn't an approval step.

**Default:** New, updated, and deleted apps appear within about 15 minutes. Health metrics are collected for apps in use. No alert rules exist until you create them.

**Where to manage it:** In the Microsoft 365 admin center, use **Apps** &gt; **All apps** for the list, and **Apps** &gt; **Monitor** for alerts.

**Recommendation:** Create monitoring rules for important or widely used apps. Task the app owners with acting on the alerts.

For inventory details, see [View and oversee apps across your tenant](../../../admin/manage/apps/inventory). For health metrics and alert setup, see [Monitor the health of apps](../../../admin/manage/apps/visibility-monitoring) and [Create an alert for an app](../../../admin/manage/apps/alerts).

## Balance control and productivity: cost and spending policies

Microsoft bills separately for building an app and running an app. Running an app uses Copilot Credits unless the user has a Power Apps Premium license. A user's applicable spending policy determines how many credits they can use.

**Default:** Users need a Power Apps Premium license or Copilot Credits to run an app. The spending policy must include usage-based billing and Copilot Managed Runtime.

**Where to manage it:** In the Microsoft 365 admin center, go to **Copilot** &gt; **Cost management**. For Copilot Studio, use Copilot Studio cost management.

| Activity | What's required | Where you manage it |
| --- | --- | --- |
| Build in Cowork or Copilot Code | A Microsoft Copilot license, plus Copilot Credits through a spending policy that includes Cowork or Copilot Code | Microsoft 365 admin center |
| Build in Copilot Studio | Copilot Credits through Copilot Studio billing for the environment | Power Platform admin center, or the Microsoft 365 admin center after the environment migrates |
| Deploy with the CLI | A license is needed only to run the app locally | Not applicable |
| Run an app, from any tool | Power Apps Premium, or Copilot Credits through a spending policy that includes Copilot Managed Runtime | Microsoft 365 admin center: **Copilot** &gt; **Cost management** |

**Recommendation:** Before pilot users run apps, create one spending policy that covers all users, includes Copilot Managed Runtime, and sets a modest per-user limit, such as 100 credits a month. Power Apps Premium users use their license first, so you don't need to exclude them. Policies are limits, not purchases. Review consumption weekly during the pilot.

For setup instructions and policy examples, see [Manage licensing and Copilot Credits for apps on Copilot Managed Runtime](../../../admin/manage/apps/licensing-credits).

## Balance control and productivity: code, build, and release

A Copilot Managed Runtime app is real source code. It's stored in a Git repository, built in an isolated environment, and released only when someone explicitly publishes. Each build maps to a specific commit, and you can redeploy an earlier good version.

**Default:** The app uses a platform-managed Git repository. Deploying externally built artifacts is off.

**Where to manage it:** In the Power Platform admin center, go to **Copilot** &gt; **Settings** &gt; **Managed apps** &gt; **External artifacts in managed apps**, or use the environment group rule of the same name.

**Recommendation:** Leave external artifacts off until a team shows a real need and your security team agrees how to validate them. If you turn them on, you own validating artifacts and securing the build pipeline.

For admin configuration, see [Configure source and deployment controls](../../../admin/manage/apps/governance#configure-source-and-deployment-controls). For the developer workflow, see [Build, preview, and deploy Copilot Managed Runtime apps](../../developer/apps/dev-inner-loop).