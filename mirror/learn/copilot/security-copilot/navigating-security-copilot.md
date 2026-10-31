---
layout: Conceptual
title: Navigate Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/navigating-security-copilot
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn the main navigation areas in Microsoft Security Copilot, including the home menu, agents, chat sessions, prompt features, and key settings.
ms.date: 2026-05-26T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: how-to
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom:
- sfi-image-nochange
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: d24e5cfe-e9e8-88be-ae15-1121dcd72308
document_version_independent_id: d24e5cfe-e9e8-88be-ae15-1121dcd72308
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/navigating-security-copilot.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: navigating-security-copilot
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/navigating-security-copilot.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: a07b6114-f89c-eaef-ac03-2494178c4370
---

# Navigate Microsoft Security Copilot | Microsoft Learn

The [Security Copilot platform](https://securitycopilot.microsoft.com) includes navigation features that help you work efficiently. This article covers two landing experiences, home menu options, how to start chat sessions, and prompt features.

## Understand the landing experience

When you open Security Copilot, the landing page can vary by onboarding and rollout stage.

- **Agents-first experience (new)** – Agents are the default homepage, with guided actions to help you get started.
- **Chat-first experience (existing)** – Chat and prompts are available directly on the homepage.

### Agents-first experience

In the agents-first experience, the **Agents** area is the primary entry point when you open Security Copilot. From the **Agents** area, you can browse available agents, view active agents in your workspace, and access setup options.

Note

The agents-first homepage doesn't include the general chat prompt bar. To start a general chat session, go to **All history** and select **New session**.

### Chat-first experience

In the chat-first experience, the homepage opens directly to the chat prompt bar where you can start typing prompts immediately. The **Agents** area is accessible from the home menu but is not the default view.

[![Screenshot of the Security Copilot chat-first homepage showing the prompt bar and home menu.](media/navigate-initial-updated.png)](media/navigate-initial-updated.png#lightbox)

## Explore interface landmarks

Homepage landmarks vary by experience: agents-first or chat-first.

### Agents-first landmarks

In the agents-first experience, navigation centers on the **Agents** area and the home menu.

[![Screenshot of the Security Copilot left navigation menu showing Agents as the primary entry point.](media/agents-menu.png)](media/agents-menu.png#lightbox)

For more information on finding and using agents, see [Discover agents](discover-agents).

### Chat-first landmarks

In the chat-first experience, the homepage includes key landmarks.

In this context, plugins are data connectors and capabilities that Security Copilot can use while responding to prompts.

![Screenshot showing home screen with numbered locations for home menu, plugins, prompt bar, and help icon.](media/navigate-initial-updated.png)

1. Use the home menu
2. Use prompts
3. Sources
4. Help

After you submit your first prompt, additional features become available.

[![Screenshot showing active prompt with share and side display menu locations.](media/navigate-post-prompt-updated.png)](media/navigate-post-prompt-updated.png#lightbox)

1. View the process log to see what Security Copilot is up to.
2. Create a promptbook based on the selected prompts.
3. Share your session with your team.
4. Side panel where the Pin board displays.
5. Pin a prompt to the pin board.

## Use the home menu

The home menu provides access to key areas of Security Copilot. The same options are available in both experiences, but the default homepage view differs.

- **Home** gets you back to the initial page.
- **Agents** – In the agents-first experience, this is the default homepage. In the chat-first experience, select **Agents** from the home menu to access the agent library. Browse the agent library, view agents active in your workspace, and, depending on your role, set up and manage agents. For more information, see [Discover agents](discover-agents) and [Setup and manage agents](agents-manage).
- **Promptbooks** - For more information, see [Using promptbooks](using-promptbooks).
- **Build** - For more information, see [Build custom agents](/en-us/copilot/security/developer/custom-agent-overview).
- **All history** - Provides access to your session history and allows you to create a new session.
- **Owner** - This menu is available only if you have the Security Copilot Owner role.

    - **Owner settings** - For more information, see [Configure owner settings](owner-settings).
    - **Plugin settings** - For more information, see [Manage plugin restrictions](manage-plugins#manage-custom-plugins).
    - **Role assignment** - For more information, see [Assign roles](authentication#assign-security-copilot-access).
    - **Usage monitoring** - For more information, see [Monitor security compute units use](manage-usage#monitor-security-compute-units-usage).
- **Settings** - Includes access to set the theme, time zone, and language preferences.
- **Tenant switching** - Allows you to switch between tenants. Requires specific authentication.

    ![Screenshot showing tenant switch setting.](media/tenant-switch.png)

    When a user signs in to Security Copilot in their home tenant, but the security data is in a different tenant, they must explicitly switch to the tenant that contains the security data.

    With the tenant switch feature, an external member or guest account that has the appropriate role in the target tenant is authorized to conduct sessions by using data in that tenant.

    The Security Copilot portal reloads and initially shows the tenant ID in the URL, for example:

    `https://securitycopilot.microsoft.com/?tenantId=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`

    Tip

    Manually modifying the tenant ID portion of the Security Copilot URL will also switch the tenant.

For more information, see the following articles:

- [Understand authentication](authentication#multitenant)
- [Grant MSSP access](grant-access-external-users)

## Access chat and sessions

Note

If you have the **agents-first experience** (the **Agents** page opens first), the homepage doesn't include the general chat prompt bar. Use the steps in this section to start a general chat session. If you have the **chat-first experience** (the prompt bar opens first), the prompt bar is available directly on the homepage. You can also use **All history** to resume a previous session or start a new one.

To start a chat session:

1. Select **All history**.
2. Review your previous sessions.
3. Select **New session**.

You can continue previous sessions or start a new one from the **All history** view.

### Use prompts

Use these resources for promptbooks, starter prompts, and prompt-writing guidance.

Note

In some experiences, prompts are accessed through a chat session instead of directly from the homepage.

- [Try promptbooks](using-promptbooks)
- [Prompting in Security Copilot](prompting-security-copilot)
- [Create effective prompts](prompting-tips)

### Manage sources

Manage plugin enablement and file sources.

To manage plugins and file inputs, see:

- [Manage plugins](manage-plugins)
- [File uploads](upload-file)

### Get help

Access the support link and documentation articles from the **Get help** menu.

![Screenshot showing the help icon menu options including documentation, training and support.](media/get-help.png)

For documentation, training videos, and support options, see:

- [Security Copilot documentation](./)
- [Security Copilot training videos](https://www.youtube.com/playlist?list=PLmAptfqzxVEW6hqgkKT_a4LNnBQm4omQq)
- [Security Copilot support options](support)

## Prompt features

The following features are available after you submit a prompt.

### View the process log

The process log appears directly under your prompt after you send it. As the response forms, notice the selected plugin.

![Screenshot showing process log steps highlighting the plugin choice.](media/process-log-choose-plugin.png)

Each plugin and its capabilities directly correspond to prompts found when selecting **See all system capabilities**.

For example, in the process log, the Microsoft Defender XDR plugin is selected. The prompt icon ![](media/sparkle-button.png) precedes the prompt `Generate guided response`, which indicates that this prompt was a specific capability of the plugin.

When you select the **Prompts** button, use the search to find capabilities. Select **See all system capabilities** to see all the prompts listed for each plugin.

![Screenshot showing filtered list of system capabilities for the Microsoft Defender XDR plugin.](media/system-capabilities-filtered.png)

Note

The `Generate guided response` session is just one of the possible sessions created by the Defender XDR embedded experience. When you interact with an embedded Copilot experience to produce results, the session will appear in your session list.

Many responses include direct links to data provided by the Microsoft service plugin used to generate that response. Use the direct links and the process log to build trust in Security Copilot while you verify it's delivering accurate, appropriate responses.

![Screenshot showing Microsoft Sentinel incident link in a response.](media/incident-link.png)

### Pin important items to the session

Use the pin board to keep track of important responses in your session.

![Screenshot of icon that controls toggling the side panel to reveal the pin board.](media/toggle-side-panel.png)

When a response is pinned for the first time, Security Copilot generates a summary of the session for the pin board.

Pin multiple prompt-response pairs to expand what is included in the summary. Pinned items show a condensed response that is expandable. The last prompt pinned is ordered last in the pin board. If you pin a prompt from the middle of the session last, that's where it's pinned on the pin board.

![Screenshot showing pin board and sample session.](media/pinboard-pins.png)

Along with the summary, the pin board features tags under the session name to help provide context to the session.

### Share a session

At any time during a Security Copilot session, share your work with your team or decision makers. Select the **Share** icon to create a link.

![Screenshot showing session sharing link options to just copy link or send link via email.](media/share-session-link-options.png)

The send via email option isn't available in these regions. Use the **Copy link** and send manually for the following regions:

- `SouthAfricaNorth`
- `UAENorth`

Tip

Keep in mind that the shared session link references the entire session, not just the portion completed before you selected the **Share** feature.

The **Share** feature is also available while reviewing **All history**.

Warning

When the link is shared by the owner to anyone with Security Copilot access in the same tenant, they are able to view the shared session. Shared sessions show a static display of the entire session, whether they normally have access to the underlying security data or not.

While accessing a shared session, there's an option to **Export** the results.

![Screenshot showing export options for shared sessions.](media/export.png)

View the shared session summary and pinned items to quickly understand the shared content. For more information, see [Shared session access](authentication#shared-sessions).

### Create a promptbook

For more information, see [Build your own promptbook](build-promptbooks)