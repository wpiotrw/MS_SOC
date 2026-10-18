---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Review default governance settings for apps (preview) - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/apps/governance?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn about the default settings for Microsoft Copilot Managed Runtime, where to review them, how to customize them, and how they work with existing Power Platform governance.
ms.date: 2026-09-29T00:00:00.0000000Z
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
document_id: 43385640-88a2-64e2-dc5c-1b36b6557646
document_version_independent_id: 43385640-88a2-64e2-dc5c-1b36b6557646
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/apps/governance.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/apps/governance
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/apps/governance.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/e6f942e8-55a7-4c86-b8e3-7456508ea850
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/f1834696-48d6-470d-966b-6ee418881596
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 417aa135-7d5f-ebe4-8e64-d729f30608d7
---

# Review default governance settings for apps (preview) - Microsoft 365 admin | Microsoft Learn

[This article is prerelease documentation and is subject to change.]

Anyone in your organization can build apps with Copilot Managed Runtime and bring them to the Microsoft 365 ecosystem. Every one of those apps comes with a set of **default settings** already in place. Each app built with Copilot Managed Runtime inherits a default policy that governs what it can connect to, how broadly it can be shared, and how it behaves at runtime.

Important

- This is a preview feature.
- These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?LinkId=2373139), and are available before an official release so that customers can get early access and provide feedback.

Since default governance is in place from day one, you don't need to set up anything as an admin. Makers can build inside a Microsoft-curated set of capabilities from the start. You can review these default settings at any time, customize them when you need to, and rely on them working alongside any Power Platform governance you already have.

This article walks through:

- Where to **review the default settings** that every app built with Copilot Managed Runtime inherits.
- How to **customize those settings** when your organization needs different rules.
- How Copilot Managed Runtime **works with existing Power Platform governance** so the configurations you already set up aren't overridden. See If you're an existing Power Platform customer for details.

## Required roles

Entra role assignments control access to environment groups in the Microsoft 365 admin center.

| Role | Access level |
| --- | --- |
| [Global Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) | Read and write |
| [Power Platform Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#power-platform-administrator) | Read and write |
| [Dynamics 365 Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#dynamics-365-administrator) | Read and write in the Power Platform admin center |
| [Global Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader) | Read-only |
| [AI Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#ai-administrator) | Read-only |
| [AI Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#ai-reader) | Read-only |

Read-only roles can see every setting in the policy (connectors, actions, sharing rules, and content security) but can't make changes.

For more information about Copilot Managed Runtime permissions and admin center access, see [Roles and responsibilities](roles-responsibilities).

## Where to find it

In the Microsoft 365 admin center, go to **Apps** &gt; **Settings**. Select **Environment groups** to open the environment groups page.

## Review the default settings

These default settings live in a **default environment group**. The system automatically provisions this group when you create the first app with Copilot Managed Runtime or when an admin visits the Copilot Managed Runtime admin experience in the Microsoft 365 admin center (MAC) or the Power Platform admin center (PPAC). You can't delete this group. It scopes to **Everyone** (it applies to all makers who build apps with Copilot Managed Runtime), and Microsoft manages it.

To review it, go to **Apps** &gt; **Settings** &gt; **Environment groups** and select the group to open its page. The page lists four rules that together define these settings: routing, connectors and MCP servers, sharing, and content security policy.

### Routing

The routing rule automatically directs new or existing makers into their own personal developer environments when they build apps with Copilot Managed Runtime, so each maker gets an isolated space to build in. By default, it applies to **Everyone**.

### Connectors and MCP servers

Apps reach external services through connectors, and a connector's actions determine what it can do. MCP (Model Context Protocol) servers do the same for an app's AI capabilities. By controlling which connectors, actions, and MCP servers are available, you determine what apps in this group can connect to and do.

The connector and MCP server rule controls which connectors, connector actions, and MCP servers apps in this group can use.

The default environment group includes 18 Microsoft first-party connectors that authenticate exclusively through Entra ID:

| Category | Connectors |
| --- | --- |
| **Content** | SharePoint, OneDrive for Business, Word Online (Business), OneNote (Business) |
| **Collaboration** | Microsoft Teams, Office 365 Outlook, Office 365 Groups Mail |
| **Identity** | Office 365 Users, Office 365 Groups |
| **Task management** | Microsoft Planner, Microsoft To Do, Microsoft Bookings |
| **Data & Analytics** | Microsoft Forms, Excel Online (Business), Dataverse, Power BI |
| **Social** | Yammer / Viva Engage |
| **DevOps** | Azure DevOps |

A connector is included in the allow list when it meets all of the following criteria:

- The publisher is Microsoft.
- It's generally available (GA).
- It supports Entra ID authentication exclusively.
- It keeps data within the tenant or connects to Microsoft-managed services.
- It exposes only purpose-scoped actions.

The following connectors are excluded by design:

- Connectors in preview
- Deprecated connectors
- Flow/automation-only connectors
- Security and admin connectors
- Infrastructure connectors
- Third-party and independent software vendor (ISV) connectors
- Custom connectors

MCP servers follow the same criteria, except for general availability (GA) status, because MCP is an emerging protocol and many servers ship in preview. Any future connector that meets the inclusion criteria is added to the allow list automatically.

#### Blocked connector actions

Some approved connectors contain actions that bypass their intended purpose. For example, these actions can send arbitrary HTTP requests or execute arbitrary code. These actions are blocked by default, even though the connector itself is allowed:

| Action type | Affected connectors | Examples |
| --- | --- | --- |
| **Open-ended HTTP requests** | SharePoint, Microsoft Teams, Office 365 Outlook, Office 365 Users, Office 365 Groups, Office 365 Groups Mail, Azure DevOps | "Send an HTTP request" actions that let makers construct arbitrary REST API calls |
| **Arbitrary code or query execution** | Excel Online (Business), Power BI | "Run script" (Office Scripts), "Run a query" (freeform DAX with user impersonation) |
| **Arbitrary platform API calls** | Dataverse | "Perform an unbound/bound action" that invokes arbitrary Custom APIs |

The connector remains available. Only the specific actions listed earlier are disabled.

#### MCP servers

The default environment group includes 12 Microsoft first-party MCP (Model Context Protocol) servers:

| MCP server | Connects to | Auth |
| --- | --- | --- |
| Power Apps MCP Server | Power Apps tasks, data entry | Entra ID |
| Work IQ Copilot MCP Server | Copilot orchestration | Entra ID |
| Work IQ Teams MCP Server | Teams messages and channels | Entra ID |
| Work IQ Outlook Mail MCP Server | Exchange / Outlook mail | Entra ID |
| Work IQ Outlook Calendar MCP Server | Exchange calendar | Entra ID |
| Work IQ Word MCP Server | Word document operations | Entra ID |
| Work IQ User MCP Server | Entra user profile data | Entra ID |
| Work IQ OneDrive MCP Server | OneDrive files | Entra ID |
| Work IQ SharePoint MCP Server | SharePoint sites and content | Entra ID |
| Fabric MCP | Microsoft Fabric data and analytics | Entra ID |
| Microsoft Learn Docs MCP | Microsoft Learn documentation | None (public) |
| Microsoft MCP Servers | MCP management and custom server creation | Entra ID |

### Sharing

The sharing rule controls how broadly makers can share apps they build:

- **Allow sharing with everyone in your organization**: Allows sharing the app with other people in the tenant.
- **Allow sharing with guest users**: Extends sharing to external guest users.

### Content security policy

[Content Security Policy](https://developer.mozilla.org/docs/Web/HTTP/CSP) (CSP) is a browser standard that limits where an app can load scripts, styles, images, and other resources from, and which sites can frame it. It gives you fine-grained control over what an app is allowed to load and which sites can embed it.

By default, apps built with Copilot Managed Runtime enforce a restrictive policy. Each directive controls a category of resource: `'self'` means only this app's own origin, `'none'` means nothing is allowed, and `data:` allows inline content supplied through data URIs.

| Directive | Default value | Description |
| --- | --- | --- |
| [`default-src`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/default-src) | `'self'` | Only allow content (scripts, images, and so on) to load from the same origin. |
| [`style-src`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/style-src) | `'self' 'unsafe-inline'` | Allow styles from own domain and inline styles. |
| [`form-action`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/form-action) | `'none'` | Prevent all form submissions, including to self. |
| [`frame-src`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/frame-src) | `'self'` | Only allow embedding frames from own domain. |
| [`child-src`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/child-src) | `'none'` | Disallow loading `<iframe>`, `<embed>`, or `<object>` children. |
| [`img-src`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/img-src) | `'self' data:` | Allow images from own domain and data. |
| [`media-src`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/media-src) | `'self' data:` | Allow audio/video from own domain and inline media via data URIs. |
| [`script-src`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/script-src) | `'self' <platform>` | Allow scripts from own domain. |
| [`worker-src`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/worker-src) | `'none'` | Disallow use of web workers or service workers. |
| [`object-src`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/object-src) | `'self' data:` | Allow `<object>` elements only from own domain and inline data. |
| [`connect-src`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/connect-src) | `'self'` | Allow network requests (AJAX/fetch/WebSocket) from own domain; no external connections. |
| [`font-src`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/font-src) | `'self'` | Allow fonts from own domain and inline font definitions. |
| [`base-uri`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/base-uri) | `'self'` | Only allow `<base>` to point to own domain. |
| [`manifest-src`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/manifest-src) | `'none'` | Disallow loading of web app manifests. |
| [`frame-ancestors`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors) | `'self' <platform>` | Controls where the app itself can be embedded. |

Content security policy can run in two modes:

- **Enforced (default).** The browser blocks any resource that violates the policy.
- **Report-only.** The browser allows everything but reports what *would* have been blocked. Use this mode to roll out or tighten a policy without breaking a running app.

The recommended way to introduce or change a policy is to enforce it in a development or test environment first, run report-only in production to surface any real violations, and only then enforce it in production.

When your app legitimately needs a resource that the default policy blocks—such as a font from a CDN, an image host, or a telemetry endpoint—an administrator adds the source to the relevant directive for the environment.

Custom values **merge with** the default value of a directive. For example, allowing an extra script source produces:

```
script-src 'self' https://contoso.com
```

The one exception is a directive whose default is `'none'`: your custom values **replace**`'none'` rather than appending to it. For instance, if your app uses a web worker, an administrator sets `worker-src` to `'self'`, replacing the default `'none'`.

Important

Keep additions as narrow as possible. Add specific origins (`https://contoso.com`), never wildcards like `*` or `'unsafe-inline'` for scripts, which defeat the purpose of the policy.

## Customize the default settings

The default settings are restrictive on day one, but you can adjust the connectors, sharing, and content security rules when your organization needs different behavior. Open the default environment group from **Apps** &gt; **Settings** &gt; **Environment groups**, and then edit the rule you want to change.

### Connectors and MCP servers

View the **allow list** (connectors apps can use) and the **blocked list** (everything else). The allow list shows each connector's name, number of allowed actions, publisher, and a link to learn more.

To see which actions are enabled or disabled for a connector, select the connector name. Each action has an on/off toggle. Actions that are disabled by default (such as open-ended HTTP requests) are clearly marked.

To add connectors, select **Add connectors** and browse or search the full connector catalog.

#### Taking full control

By default, Microsoft curates the connector policy for you. To switch from Microsoft-curated to full control, select **Edit this policy** in the **Connectors and MCP servers** flyout.

This change applies specifically to the **advanced connector policy**: the list of approved connectors, their action controls, and MCP servers. Once switched:

- Automatic updates from Microsoft stop for connectors, MCP servers, and action controls.
- The admin can add or remove connectors from the allow list.
- The admin can enable or disable individual connector actions.
- The admin can add or remove MCP servers.

A warning dialog appears before the switch takes effect, calling out that:

1. Existing apps might be affected if connectors or actions change.
2. The connector policy no longer receives automatic additions from Microsoft.

### Sharing

Select **Sharing** and turn on or off either setting to widen or restrict how broadly makers can share their apps.

### Content security policy

Configure CSP settings to control what apps built with Copilot Managed Runtime can do in a browser:

- **Reporting for apps**: Optionally collect reports on content blocked by this policy.
- **Enforce content security policy**: Block violations of content security policy for end users.
- **Configure directives**: Toggle individual CSP directives (default-src, style-src, script-src, img-src, connect-src, frame-src, and others). When you customize a directive, the values you supply are appended to the default value. If the default value is `'none'`, your custom values replace it.

You can always directly edit sharing rules and content security settings, regardless of whether the connector policy is Microsoft-curated or under your full control.

## Control whether apps can be created using the CLI

The **Allow app creation with the Copilot Managed Runtime command line interface (CLI)** setting controls whether users in an environment can create apps using the CLI.

To configure the setting:

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com).
2. Go to **Copilot** &gt; **Settings** &gt; **Managed apps**.
3. Select **Allow app creation with the Copilot Managed Runtime command line interface (CLI)**.
4. Select **Environment groups** or **Environments**, select the applicable group or environment, and then enable the setting.

For environment groups, you can instead use the group-management experience:

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com).
2. In the Power Platform admin center, go to **Manage** &gt; **Environment groups**.
3. Select the environment group, and then open **Rules**.
4. Open **Allow app creation with the Copilot Managed Runtime command line interface (CLI)** rule, enable the setting, and then save the change.

## Configure source and deployment controls

Copilot Managed Runtime supports external repositories owned by GitHub Enterprise Cloud organizations. Configure repository visibility and other repository management policies in GitHub Enterprise Cloud. For more information, see [Enforcing repository management policies in your enterprise](https://docs.github.com/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise#about-policies-for-repository-management-in-your-enterprise).

Copilot Managed Runtime provides a separate control for externally built artifacts. This setting is disabled by default and can be configured for an environment or environment group. When an environment group has a published rule, it supersedes and locks the corresponding environment setting. Per-environment exceptions aren't supported. For more information, see [Environment groups](/en-us/power-platform/admin/environment-groups#rules).

### External artifact deployment

The **Allow external artifact deployment** setting controls whether developers can deploy artifacts built outside the Microsoft-managed build system. When it's on, [`ms app deploy --artifact <path>`](../../../managed-apps/developer/ms-cli-command-reference#ms-app-deploy) uploads and deploys an artifact without triggering a platform-managed build. When it's off, the CLI throws an error and directs the developer to contact an administrator.

Important

Your organization is responsible for validating externally built artifacts, securing the build pipeline, and confirming that artifacts meet its security, compliance, and software supply-chain requirements.

### Configure external artifact deployment

To configure the setting:

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com).
2. Go to **Copilot** &gt; **Settings** &gt; **Managed apps**.
3. Select **External artifacts in managed apps**.
4. Select **Environment groups** or **Environments**, select the applicable group or environment, and then enable the setting.

For environment groups, you can instead use the group-management experience:

1. In the Power Platform admin center, go to **Manage** &gt; **Environment groups**.
2. Select the environment group, and then open **Rules**.
3. Open **External artifacts in managed apps**, enable the setting, and then save the change.

Note

The alternate path supports environment groups only.

## If you're an existing Power Platform customer

If your tenant already has environment routing rules, environment groups, or advanced connector policies configured in the Power Platform admin center, Copilot Managed Runtime respects those existing configurations. It's designed not to override what IT already set up.

How it works depends on the current routing state. The following changes are applied automatically when the first app built with Copilot Managed Runtime in the company is created or when you visit the Copilot Managed Runtime admin experience in Microsoft 365 admin center or Power Platform admin center.

For more information, see [Environment routing](/en-us/power-platform/admin/default-environment-routing) in the Power Platform documentation.

### No routing configured

Environment routing is enabled for Copilot Managed Runtime only. All new personal developer environments are routed into a single environment group that is preconfigured with the rules described earlier.

### Routing enabled with no routing rules

If you enable environment routing for one or more products (for example, for Copilot Studio) without configuring a routing rule, two things happen. First, routing is auto-enabled for Copilot Managed Runtime. In the Power Platform admin center **Tenant settings** &gt; **Environment routing** panel, Copilot Managed Runtime appears as a routing product with its own checkbox. Then, a routing rule is added so that all new personal developer environments created from routing are placed into a single environment group that is preconfigured with the rules described earlier.

### Routing rules with an "Everyone" catch-all

Microsoft 365 admin center preserves and reflects your existing environment groups and routing rules. The **Environment groups** page in Microsoft 365 admin center (under **Apps** &gt; **Settings**) shows the same information as the **Environment routing** panel in Power Platform admin center (under **Tenant settings**). Each group includes Copilot Managed Runtime-specific settings, such as sharing limits and content security.

### Security-group-scoped routing without a catch-all

This option uses the same configuration as the previous option, but users outside all configured security groups aren't automatically provisioned a personal developer environment. The existing routing scope stays the same.

In all cases, Copilot Managed Runtime-specific rules layer in without overriding existing configurations. Microsoft 365 admin center preserves whatever the admin previously set up.

You can't turn off environment routing for Copilot Managed Runtime. The routing rule you create for Copilot Managed Runtime is permanent and can't be deleted from either Microsoft 365 admin center or Power Platform admin center.

### How connector policies are evaluated for existing environment groups

Power Platform supports [advanced connector policies (ACP)](/en-us/power-platform/admin/advanced-connector-policies) and classic [data loss prevention (DLP) policies](/en-us/power-platform/admin/wp-data-loss-prevention), referred to here as data policies. For an existing environment group, the effective connector access depends on whether the group has an ACP and whether **Advanced connector policies only** is on.

| Existing ACP | **Advanced connector policies only** | Effective connector governance |
| --- | --- | --- |
| No | Off | Applicable data policies are enforced. If no data policy applies, connectors aren't restricted. |
| No | On | Data policies are ignored. Without an ACP, connectors aren't restricted. |
| Yes | Off | The ACP and applicable data policies are both enforced. The most restrictive result applies. |
| Yes | On | Only the ACP is enforced. Existing data policies remain configured but are ignored for environments in the group. |

## Known limitations

For an existing environment group without an advanced connector policy (ACP), the **Connectors and MCP servers** view in the Microsoft 365 admin center might report that no connectors are allowed. This message reflects the absence of an ACP and might not represent the effective connector access:

- If **Advanced connector policies only** is off, applicable classic data policies continue to govern connector access. If no data policy applies, connectors aren't restricted by either policy type.
- If **Advanced connector policies only** is on, classic data policies are ignored. Without an ACP, connectors aren't restricted by either policy type.

Review the group's ACP, **Advanced connector policies only** setting, and applicable data policies in the Power Platform admin center to determine which connectors are available.