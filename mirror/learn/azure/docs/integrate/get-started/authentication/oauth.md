---
layout: Conceptual
monikers:
- azure-devops
defaultMoniker: azure-devops
versioningType: Ranged
title: OAuth 2.0 Authentication for Azure DevOps REST APIs - Azure DevOps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/oauth?view=azure-devops
config_moniker_range: azure-devops || >= azure-devops-2022 <= azure-devops-server
feedback_system: Standard
feedback_product_url: https://developercommunity.visualstudio.com/AzureDevOps
breadcrumb_path: /azure/devops/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-AzureDevOps
archive_url: https://docs.microsoft.com/en-us/previous-versions/azure/devops/all/
ms.topic: how-to
ms.manager: wiwagn
author: chcomley
ms.author: chcomley
ms.date: 2025-07-14T00:00:00.0000000Z
ms.service: azure-devops
ms.version: ALM
MSHAttr.msprod: ms.prod:ALM
ms.prodfamily: ALM
description: Learn how to use OAuth 2.0 authentication with Azure DevOps REST APIs, with Microsoft Entra ID as the recommended approach.
ai-usage: ai-assisted
ms.custom: pat-reduction
ms.subservice: azure-devops-security
locale: en-us
document_id: ac47cbcf-45ed-81aa-b532-e7ad0046658e
document_version_independent_id: 7aa1f60e-069f-3d62-5cac-b65e4b1116ef
original_content_git_url: https://github.com/MicrosoftDocs/azure-devops-docs-pr/blob/live/docs/integrate/get-started/authentication/oauth.md
default_moniker: azure-devops
site_name: Docs
depot_name: MSDN.azure-devops-docs
page_type: conceptual
toc_rel: ../../../dev-resources/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.azure-devops-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: integrate/get-started/authentication/oauth
moniker_range_name: 348281b5e6207d94331bdbf3987314df
monikers:
- azure-devops
item_type: Content
source_path: docs/integrate/get-started/authentication/oauth.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5bd2b3fa-c186-4b92-a3c8-09f22a249d37
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7eba7926-b7b2-4a7a-bf89-e6ac53b3e7f6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: 9b1dd718-ee9d-e942-4516-cc7f9a9a36cf
---

# OAuth 2.0 Authentication for Azure DevOps REST APIs - Azure DevOps | Microsoft Learn

**Azure DevOps Services**

Learn how to use OAuth 2.0 to authenticate your applications for Azure DevOps REST API access without requiring users to repeatedly provide credentials.

Important

Use Microsoft Entra ID OAuth for new applications. Azure DevOps OAuth 2.0 is deprecated and no longer accepts new registrations.

## How OAuth 2.0 works with Azure DevOps

Note

OAuth 2.0 is available only for Azure DevOps Services, not Azure DevOps Server. For on-premises scenarios, use [Client libraries](../../concepts/dotnet-client-libraries), Windows Authentication, or [personal access tokens](../../../organizations/accounts/use-personal-access-tokens-to-authenticate).

Azure DevOps Services uses the [OAuth 2.0 protocol](https://oauth.net/2/) to authorize applications and generate access tokens for REST API calls. The process involves the following steps:

- **App registration**: Register your application with the OAuth provider.
- **User authorization**: Grant permission for your app to access user data.
- **Token exchange**: Receive an access token to make API calls.
- **API access**: Use the token for authenticated REST API requests.
- **Token refresh**: Refresh expired tokens to maintain access.

![Diagram that shows the OAuth 2.0 authorization flow process from app registration to API access.](media/oauth-overview.png)

## OAuth implementation options

Choose the appropriate OAuth implementation based on your application's needs.

### Microsoft Entra ID OAuth (recommended)

Microsoft Entra ID OAuth provides the most secure and future-proof authentication method for Azure DevOps applications. Benefits include:

- **Enterprise integration**: Seamless integration with existing Microsoft Entra ID infrastructure.
- **Enhanced security**: Advanced security features include Microsoft Entra Conditional Access and multifactor authentication.
- **Future support**: Actively maintained and supported platform.
- **Unified identity**: Single sign-on experience across Microsoft services.

**Get started**: Follow our [Microsoft Entra ID OAuth guide](entra-oauth) for implementation details and migration guidance.

### Azure DevOps OAuth (deprecated)

Warning

Azure DevOps OAuth is deprecated. New app registrations are no longer accepted as of April 2025. The service is scheduled for full deprecation in 2026. Migrate existing applications to Microsoft Entra ID OAuth.

For existing Azure DevOps OAuth applications:

- Review the [Azure DevOps OAuth guide](azure-devops-oauth) for current implementation details.
- Plan migration to Microsoft Entra ID OAuth before 2026.
- [Manage existing app authorizations](../../../organizations/settings/manage-authorizations) as needed.

**Migration planning**: Start planning your migration to Microsoft Entra ID OAuth early. The [Migration guide](entra-oauth) provides tips and considerations for a smooth transition.

## OAuth scopes

Scopes define what Azure DevOps resources your application can access. Both Microsoft Entra ID OAuth and Azure DevOps OAuth use the same scope definitions.

### Key scope considerations

- **Principle of least privilege**: Request only the minimum scopes your application needs.
- **Scope inheritance**: Some scopes include others (for example, `vso.code_manage` includes `vso.code_write`).
- **API coverage**: Scopes enable access to REST APIs and select Git endpoints only (SOAP APIs not supported).
- **User consent**: Users must explicitly grant permission for each requested scope.

### Find required scopes

To determine what scopes your application needs:

- Check the API reference documentation for each endpoint you plan to use.
- Look for the `scopes` header on each API page.
- To avoid requesting redundant permissions, consider scope relationships.

### Available scopes

| Category | Scope | Name | High privilege | Description | Inherits from |
| --- | --- | --- | --- | --- | --- |
| Advanced security | `vso.advsec` | Advanced security (read) | Yes | Grants the ability to read alerts, result instances, and analysis result instances. |  |
|  | `vso.advsec_write` | Advanced security (read and write) | Yes | Grants the ability to upload analyses in serif. | `vso.advsec` |
|  | `vso.advsec_manage` | Advanced security (read, write, and manage) | Yes | Grants the ability to upload analyses in serif. | `vso.advsec_write` |
| Agent pools | `vso.agentpools` | Agent pools (read) |  | Grants the ability to view tasks, pools, queues, agents, and currently running or recently completed jobs for agents. |  |
|  | `vso.agentpools_manage` | Agent pools (read and manage) | Yes | Grants the ability to manage pools, queues, and agents. | `vso.agentpools` |
|  | `vso.environment_manage` | Environment (read and manage) | Yes | Grants the ability to manage pools, queues, agents, and environments. | `vso.agentpools_manage` |
| Analytics | `vso.analytics` | Analytics (read) |  | Grants the ability to query analytics data. |  |
| Auditing | `vso.auditlog` | Audit log (read) |  | Grants the ability to read the auditing log to users. |  |
|  | `vso.auditstreams_manage` | Audit streams (read) | Yes | Grants the ability to manage auditing streams to users. | `vso.auditlog` |
| Build | `vso.build` | Build (read) |  | Grants the ability to access build artifacts, including build results, definitions, and requests, and the ability to receive notifications about build events via service hooks. | `vso.hooks_write` |
|  | `vso.build_execute` | Build (read and execute) | Yes | Grants the ability to access build artifacts, including build results, definitions, and requests. Also grants the ability to queue a build, update build properties, and receive notifications about build events via service hooks. | `vso.build` |
| Code | `vso.code` | Code (read) |  | Grants the ability to read source code and metadata about commits, changesets, branches, and other version control artifacts. Also grants the ability to search code and get notified about version control events via service hooks. | `vso.hooks_write` |
|  | `vso.code_write` | Code (read and write) | Yes | Grants the ability to read, update, and delete source code and access metadata about commits, changesets, branches, and other version control artifacts. Also grants the ability to create and manage pull requests and code reviews and receive notifications about version control events via service hooks. | `vso.code` |
|  | `vso.code_manage` | Code (read, write, and manage) | Yes | Grants the ability to read, update, and delete source code, access metadata about commits, changesets, branches, and other version control artifacts. Also grants the ability to create and manage code repositories, create and manage pull requests and code reviews, and to receive notifications about version control events via service hooks. | `vso.code_write` |
|  | `vso.code_full` | Code (full) | Yes | Grants full access to source code, metadata about commits, changesets, branches, and other version control artifacts. Also grants the ability to create and manage code repositories, create and manage pull requests and code reviews, and receive notifications about version control events via service hooks. Also includes limited support for Client OM APIs. | `vso.code_manage` |
|  | `vso.code_status` | Code (status) |  | Grants the ability to read and write commit and pull-request status. |  |
| Connected server | `vso.connected_server` | Connected server |  | Grants the ability to access endpoints needed from an on-premises connected server. |  |
| Entitlements | `vso.entitlements` | Entitlements (read) |  | Grants read-only access to licensing entitlement endpoints to get account entitlements. |  |
|  | `vso.memberentitlementmanagement` | Member entitlement management (read) |  | Grants the ability to read users, their licenses, and the projects and extensions they can access. |  |
|  | `vso.memberentitlementmanagement_write` | Member entitlement management (write) | Yes | Grants the ability to manage users and their licenses and the projects and extensions they can access. | `vso.memberentitlementmanagement` |
| Extensions | `vso.extension` | Extensions (read) |  | Grants the ability to read installed extensions. | `vso.profile` |
|  | `vso.extension_manage` | Extensions (read and manage) | Yes | Grants the ability to install, uninstall, and perform other administrative actions on installed extensions. | `vso.extension` |
|  | `vso.extension.data` | Extension data (read) |  | Grants the ability to read data (settings and documents) stored by installed extensions. | `vso.profile` |
|  | `vso.extension.data_write` | Extension data (read and write) |  | Grants the ability to read and write data (settings and documents) stored by installed extensions. | `vso.extension.data` |
| GitHub connections | `vso.githubconnections` | GitHub connections (read) |  | Grants the ability to read GitHub connections and GitHub repositories data. |  |
|  | `vso.githubconnections_manage` | GitHub connections (read and manage) | Yes | Grants the ability to read and manage GitHub connections and GitHub repositories data. | `vso.githubconnections` |
| Graph and identity | `vso.graph` | Graph (read) |  | Grants the ability to read user, group, scope, and group membership information. |  |
|  | `vso.graph_manage` | Graph (manage) | Yes | Grants the ability to read user, group, scope, and group membership information, add users and groups, and manage group memberships. | `vso.graph` |
|  | `vso.identity` | Identity (read) |  | Grants the ability to read identities and groups. |  |
|  | `vso.identity_manage` | Identity (manage) | Yes | Grants the ability to read, write, and manage identities and groups. | `vso.identity` |
| Machine group | `vso.machinegroup_manage` | Deployment group (read, manage) | Yes | Grants the ability to manage deployment group and agent pools. | `vso.agentpools_manage` |
| Marketplace | `vso.gallery` | Marketplace |  | Grants read access to public and private items and publishers. | `vso.profile` |
|  | `vso.gallery_acquire` | Marketplace (acquire) |  | Grants read access and the ability to acquire items. | `vso.gallery` |
|  | `vso.gallery_publish` | Marketplace (publish) | Yes | Grants read access and the ability to upload, update, and share items. | `vso.gallery` |
|  | `vso.gallery_manage` | Marketplace (manage) | Yes | Grants read access and the ability to publish and manage items and publishers. | `vso.gallery_publish` |
| Notifications | `vso.notification` | Notifications (read) |  | Grants read access to subscriptions and event metadata, including filterable field values. | `vso.profile` |
|  | `vso.notification_write` | Notifications (write) |  | Grants read and write access to subscriptions and read access to event metadata, including filterable field values. | `vso.notification` |
|  | `vso.notification_manage` | Notifications (manage) |  | Grants read, write, and management access to subscriptions and read access to event metadata, including filterable field values. | `vso.notification_write` |
|  | `vso.notification_diagnostics` | Notifications (diagnostics) |  | Grants access to notification-related diagnostic logs and grants the ability to enable diagnostics for individual subscriptions. | `vso.notification` |
| Packaging | `vso.packaging` | Packaging (read) |  | Grants the ability to read feeds and packages. | `vso.profile` |
|  | `vso.packaging_write` | Packaging (read and write) | Yes | Grants the ability to create and read feeds and packages. | `vso.packaging` |
|  | `vso.packaging_manage` | Packaging (read, write, and manage) | Yes | Grants the ability to create, read, update, and delete feeds and packages. | `vso.packaging_write` |
| Pipeline resources | `vso.pipelineresources_use` | Pipeline resources (use) | Yes | Grants the ability to approve a pipeline's request to use a protected resource: agent pool, environment, queue, repository, secure files, service connection, and variable group. |  |
|  | `vso.pipelineresources_manage` | Pipeline resources (use and manage) | Yes | Grants the ability to manage a protected resource or a pipeline's request to use a protected resource: agent pool, environment, queue, repository, secure files, service connection, and variable group. | `vso.pipelineresources_use` |
| Project and team | `vso.project` | Project and team (read) |  | Grants the ability to read projects and teams. |  |
|  | `vso.project_write` | Project and team (read and write) |  | Grants the ability to read and update projects and teams. | `vso.project` |
|  | `vso.project_manage` | Project and team (read, write, and manage) | Yes | Grants the ability to create, read, update, and delete projects and teams. | `vso.project_write` |
| Release | `vso.release` | Release (read) |  | Grants the ability to read release artifacts, including releases, release definitions, and release environment. | `vso.profile` |
|  | `vso.release_execute` | Release (read, write, and execute) | Yes | Grants the ability to read and update release artifacts, including releases, release definitions, and release environment. Also grants the ability to queue a new release. | `vso.release` |
|  | `vso.release_manage` | Release (read, write, execute, and manage) | Yes | Grants the ability to read, update, and delete release artifacts, including releases, release definitions, and release environment. Also grants the ability to queue and approve a new release. | `vso.release_execute` |
| Secure files | `vso.securefiles_read` | Secure files (read) | Yes | Grants the ability to read secure files. |  |
|  | `vso.securefiles_write` | Secure files (read and create) | Yes | Grants the ability to read and create secure files. | `vso.securefiles_read` |
|  | `vso.securefiles_manage` | Secure files (read, create, and manage) | Yes | Grants the ability to read, create, and manage secure files. | `vso.securefiles_write` |
| Security | `vso.security_manage` | Security (manage) | Yes | Grants the ability to read, write, and manage security permissions. |  |
| Service connections | `vso.serviceendpoint` | Service endpoints (read) |  | Grants the ability to read service endpoints. | `vso.profile` |
|  | `vso.serviceendpoint_query` | Service endpoints (read and query) |  | Grants the ability to read and query service endpoints. | `vso.serviceendpoint` |
|  | `vso.serviceendpoint_manage` | Service endpoints (read, query, and manage) | Yes | Grants the ability to read, query, and manage service endpoints. | `vso.serviceendpoint_query` |
| Service hooks | `vso.hooks` | Service hooks (read) |  | Grants the ability to read service hook subscriptions and metadata, including supported events, consumers, and actions. (No longer public.) | `vso.profile` |
|  | `vso.hooks_write` | Service hooks (read and write) |  | Grants the ability to create and update service hook subscriptions and read metadata, including supported events, consumers, and actions. (No longer public.) | `vso.hooks` |
|  | `vso.hooks_interact` | Service hooks (interact) |  | Grants the ability to interact and perform actions on events received via service hooks. (No longer public.) | `vso.profile` |
| Settings | `vso.settings` | Settings (read) |  | Grants the ability to read settings. |  |
|  | `vso.settings_write` | Settings (read and write) |  | Grants the ability to read and write settings. | `vso.settings` |
| Symbols | `vso.symbols` | Symbols (read) |  | Grants the ability to read symbols. | `vso.profile` |
|  | `vso.symbols_write` | Symbols (read and write) |  | Grants the ability to read and write symbols. | `vso.symbols` |
|  | `vso.symbols_manage` | Symbols (read, write, and manage) |  | Grants the ability to read, write, and manage symbols. | `vso.symbols_write` |
| Task groups | `vso.taskgroups_read` | Task groups (read) |  | Grants the ability to read task groups. |  |
|  | `vso.taskgroups_write` | Task groups (read and create) |  | Grants the ability to read and create task groups. | `vso.taskgroups_read` |
|  | `vso.taskgroups_manage` | Task groups (read, create, and manage) | Yes | Grants the ability to read, create, and manage task groups. | `vso.taskgroups_write` |
| Team dashboard | `vso.dashboards` | Team dashboards (read) |  | Grants the ability to read team dashboard information. |  |
|  | `vso.dashboards_manage` | Team dashboards (manage) |  | Grants the ability to manage team dashboard information. | `vso.dashboards` |
| Test management | `vso.test` | Test management (read) |  | Grants the ability to read test plans, cases, results, and other test management-related artifacts. | `vso.profile` |
|  | `vso.test_write` | Test management (read and write) |  | Grants the ability to read, create, and update test plans, cases, results, and other test management-related artifacts. | `vso.test` |
| Threads | `vso.threads_full` | PR threads |  | Grants the ability to read and write to pull request comment threads. |  |
| Tokens | `vso.tokens` | Delegated authorization tokens | Yes | Grants the ability to manage delegated authorization tokens to users. |  |
|  | `vso.tokenadministration` | Token administration | Yes | Grants the ability to manage (view and revoke) existing tokens to organization administrators. |  |
| User profile | `vso.profile` | User profile (read) |  | Grants the ability to read your profile, accounts, collections, projects, teams, and other top-level organizational artifacts. |  |
|  | `vso.profile_write` | User profile (write) |  | Grants the ability to write to your profile. | `vso.profile` |
| Variable groups | `vso.variablegroups_read` | Variable groups (read) |  | Grants the ability to read variable groups. |  |
|  | `vso.variablegroups_write` | Variable groups (read and create) |  | Grants the ability to read and create variable groups. | `vso.variablegroups_read` |
|  | `vso.variablegroups_manage` | Variable groups (read, create, and manage) | Yes | Grants the ability to read, create, and manage variable groups. | `vso.variablegroups_write` |
| Wiki | `vso.wiki` | Wiki (read) |  | Grants the ability to read wikis, wiki pages, and wiki attachments. Also grants the ability to search wiki pages. |  |
|  | `vso.wiki_write` | Wiki (read and write) |  | Grants the ability to read, create, and update wikis, wiki pages, and wiki attachments. | `vso.wiki` |
| Work items | `vso.work` | Work items (read) |  | Grants the ability to read work items, queries, boards, area and iterations paths, and other work item tracking-related metadata. Also grants the ability to execute queries, search work items, and receive notifications about work item events via service hooks. | `vso.hooks_write` |
|  | `vso.work_write` | Work items (read and write) |  | Grants the ability to read, create, and update work items and queries, update board metadata, read area and iterations paths and other work item tracking-related metadata, execute queries, and receive notifications about work item events via service hooks. | `vso.work` |
|  | `vso.work_full` | Work items (full) |  | Grants full access to work items, queries, backlogs, plans, and work-item tracking metadata. Also grants the ability to receive notifications about work item events via service hooks. | `vso.work_write` |
| User impersonation | `user_impersonation` | User impersonation | Yes | Grants full access to Visual Studio Team Services REST APIs. *Request or consent this scope with caution because it's very powerful.* |  |

## Frequently asked questions

### Q. Can I use OAuth with mobile applications?

A. No. Azure DevOps Services supports only the web server flow (authorization code flow), which requires securely storing an app secret. Mobile applications can't securely store secrets, which makes OAuth unsuitable for mobile scenarios.

**Alternative for mobile apps**: Use [personal access tokens](../../../organizations/accounts/use-personal-access-tokens-to-authenticate) for mobile application authentication.

### Q. Does OAuth work with all Azure DevOps APIs?

A. OAuth supports REST APIs and select Git endpoints only. SOAP APIs don't support OAuth authentication.

### Q. How do I migrate from Azure DevOps OAuth to Microsoft Entra ID OAuth?

A. Follow the [Microsoft Entra ID OAuth migration guide](entra-oauth), which includes:

- Step-by-step migration instructions.
- Code examples and best practices.
- Timeline considerations for the deprecation.

### Q. What happens to my existing Azure DevOps OAuth app after 2026?

A. Existing Azure DevOps OAuth apps stop working when the service is fully deprecated in 2026. Plan your migration to Microsoft Entra ID OAuth well before this deadline.

## Choose your implementation path

- **For new applications:**[Build with Microsoft Entra ID OAuth](entra-oauth)
- **For existing Azure DevOps OAuth apps:**[Plan your migration to Microsoft Entra ID](entra-oauth)
- **For existing apps that need immediate support:**[Azure DevOps OAuth documentation](azure-devops-oauth)