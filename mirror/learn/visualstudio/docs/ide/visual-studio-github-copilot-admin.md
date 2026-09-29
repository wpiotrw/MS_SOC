---
layout: Conceptual
monikers:
- vs-2022
- visualstudio
defaultMoniker: visualstudio
versioningType: Ranged
title: Admin controls for GitHub Copilot in Visual Studio - Visual Studio (Windows) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-admin?view=visualstudio
config_moniker_range: '>= vs-2022'
feedback_system: Standard
feedback_help_link_url: https://developercommunity.microsoft.com/VisualStudio
feedback_help_link_type: ask-the-community
feedback_product_url: https://developercommunity.visualstudio.com/VisualStudio/suggest
breadcrumb_path: /visualstudio/_breadcrumb/toc.json
ms.manager: wiwagn
author: RoseHJM
ms.author: rosemalcolm
audience: developer
ms.service: visual-studio-windows
uhfHeaderId: MSDocsHeader-VisualStudio
toc_preview: true
archive_url: /previous-versions/visualstudio
recommendations: true
description: Learn about the new features for administrators in GitHub Copilot for Visual Studio that enable admins to manage Copilot effectively.
ms.date: 2026-03-26T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: how-to
ms.subservice: ai-tools
ms.collection: ce-skilling-ai-copilot
ms.custom: ai-learning-hub, awp-ai
locale: en-us
document_id: f6e77a5d-c25f-4669-a897-aaa88f71609e
document_version_independent_id: f6e77a5d-c25f-4669-a897-aaa88f71609e
original_content_git_url: https://github.com/MicrosoftDocs/visualstudio-docs-pr/blob/live/docs/ide/visual-studio-github-copilot-admin.md
default_moniker: visualstudio
site_name: Docs
depot_name: VS.docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/VS.docs/{branchName}{pdfName}
asset_id: ide/visual-studio-github-copilot-admin
moniker_range_name: f22a899ea89b53168e6a2ccb9c507f5c
monikers:
- vs-2022
- visualstudio
item_type: Content
source_path: docs/ide/visual-studio-github-copilot-admin.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/4628cbd9-6f47-4ae1-b371-d34636609eaf
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/341fdab2-4964-4759-8241-f5820b012a47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/be21deb8-8c64-44b0-b71f-2dc56ca7364f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cc1f92bb-c0d6-4d40-99ce-dabea3161a84
platformId: 0f8beac6-fb17-3d35-4a7c-a612a19be8af
---

# Admin controls for GitHub Copilot in Visual Studio - Visual Studio (Windows) | Microsoft Learn

Visual Studio 2022 introduces new features that enable administrators to configure and manage GitHub Copilot more effectively within their enterprise. These features provide administrators greater control over the use of Copilot within their organization. Admins can disable Copilot for individual accounts, disable it entirely, and configure content exclusion to prevent certain files from being available to Copilot in Visual Studio.

In this article, you learn how to:

- Disable Copilot

::: moniker range="visualstudio"

- Configure MCP server allowlist

::: moniker-end

- Configure content exclusion

## Disable Copilot SKUs

With Visual Studio 2022 version 17.10 or later, project administrators can disable Copilot for individual accounts or disable it entirely using the [Visual Studio Administrative Templates (ADMX/ADML)](https://www.microsoft.com/en-us/download/details.aspx?id=104405). This helps ensure that your repository remains protected.

With Visual Studio 2022 version 17.13 or later, you can disable Copilot Free.

To configure and deploy these policies, you can use [Microsoft Intune](../install/administrative-templates#deploying-the-policies) or the Local Group Policy Editor directly on the client machine.

### Configure Copilot group policy

1. Visit the Microsoft Download Center to download the Visual Studio [Group Policy Administrative Template files (ADMX/ADML)](https://www.microsoft.com/en-us/download/details.aspx?id=104405). When prompted, ensure the files are saved to `C:\Windows\PolicyDefinitions`.
2. Open the **Windows Local Group Policy Editor** and navigate to **Computer Configuration &gt; Administrative Templates &gt; Visual Studio &gt; Copilot Settings**. Select a group policy.

    [![Screenshot of Group Policy Settings.](media/vs-2022/copilot-inbox/intune-group-policy.png)](media/vs-2022/copilot-inbox/intune-group-policy.png#lightbox)
3. Once you select the group policy, configure it to enable or disable Copilot as needed.

    [![Screenshot of Group Policy to block Copilot for individuals.](media/vs-2022/copilot-inbox/copilot-for-individuals-group-poilcy.png)](media/vs-2022/copilot-inbox/copilot-for-individuals-group-poilcy.png#lightbox)
4. Restart your Visual Studio instance to apply the new policy changes.

### Disable Copilot Agent Mode

With Visual Studio 2022 version 17.14.16 or later, project administrators can fully disable Agent Mode using [Visual Studio Administrative Templates (ADMX/ADML)](https://www.microsoft.com/en-us/download/details.aspx?id=104405). With this policy setting administrators can control which AI-assisted features are available in their organization, helping ensure usage aligns with security and compliance requirements.

Policy location in the Local Group Policy Editor: **Computer Configuration &gt; Administrative Templates &gt; Visual Studio &gt; Copilot Settings &gt; Disable Agent Mode**

::: moniker range="visualstudio"

## Configure MCP server allowlist

With Visual Studio 2026, administrators can configure an allowlist of approved MCP servers through the GitHub Copilot administration dashboard. When an allowlist is configured, developers in the organization can only connect to MCP servers that appear on the approved list.

### How the MCP server allowlist works

- Administrators specify which MCP servers are allowed within their organization by using the [GitHub Copilot enterprise policies for MCP](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise#defining-policies-for-your-enterprise). In the enterprise or organization settings, navigate to **AI Controls** and select **MCP** in the sidebar to configure MCP server policies.
- Visual Studio checks the allowlist when a user attempts to connect to an MCP server.
- If the server is on the allowlist, the connection proceeds normally.
- If the server isn't on the allowlist, Visual Studio blocks the connection and displays an error message indicating that the server isn't permitted by the organization's policy.

This feature helps organizations control which MCP servers can process sensitive data and maintain compliance with security policies.

For more information on using MCP servers in Visual Studio, see [Use MCP servers](mcp-servers).

::: moniker-end

## Configure content exclusion

Content exclusion for GitHub Copilot enables administrators to prevent certain files from being available to Copilot and keep sensitive content secure from Copilot use. You can use content exclusions to configure GitHub Copilot to ignore specific files in a [repository](https://docs.github.com/en/copilot/managing-github-copilot-in-your-organization/configuring-content-exclusions-for-github-copilot#configuring-content-exclusions-for-your-repository) or [organization](https://docs.github.com/en/copilot/managing-github-copilot-in-your-organization/configuring-content-exclusions-for-github-copilot#configuring-content-exclusions-for-your-organization).

Content exclusion is available only with a GitHub Copilot Business or a GitHub Copilot Enterprise [subscriptions](https://docs.github.com/en/copilot/about-github-copilot/subscription-plans-for-github-copilot).

With [Visual Studio 2022 version 17.11](/en-us/visualstudio/releases/2022/release-notes), GitHub Copilot for Visual Studio will ignore excluded content. When content is excluded, completions and chat aren't available for the affected files.

Note that Visual Studio 2022 version 17.11 respects rules only in the root repository where your solution lives, and doesn't apply rules from git submodules or for files not under a git repository.

### GitHub Copilot Completions in Visual Studio and content exclusions

- Code completions aren't available for excluded files.

    [![Screenshot of Copilot completions on an excluded file.](media/vs-2022/visual-studio-github-copilot-admin/copilot-content-exclusions-completions.png)](media/vs-2022/visual-studio-github-copilot-admin/copilot-content-exclusions-completions.png#lightbox)
- Excluded content isn't included in code completion suggestions for other files.

### GitHub Copilot Chat in Visual Studio and content exclusions

- Excluded files can't be referenced in the chat window or in inline chat.

    **Chat window**

    [![Screenshot of using an excluded file in chat window.](media/vs-2022/visual-studio-github-copilot-admin/copilot-content-exclusions-chat-window.png)](media/vs-2022/visual-studio-github-copilot-admin/copilot-content-exclusions-chat-window.png#lightbox)

    **Inline chat**

    [![Screenshot of using an excluded file in inline chat.](media/vs-2022/visual-studio-github-copilot-admin/copilot-content-exclusions-chat-inline.png)](media/vs-2022/visual-studio-github-copilot-admin/copilot-content-exclusions-chat-inline.png#lightbox)
- Excluded content isn't included in GitHub Copilot Chat's responses.

    [![Screenshot of chat's responses on excluded content.](media/vs-2022/visual-studio-github-copilot-admin/copilot-content-exclusions-chat-response.png)](media/vs-2022/visual-studio-github-copilot-admin/copilot-content-exclusions-chat-response.png#lightbox)