---
layout: Conceptual
title: Configure Microsoft Teams for the Data Security Triage Agent remediation messages | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-teams-config
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: tracyp
author: MSFTTracyP
manager: laurawi
ms.date: 2026-05-05T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
search.appverid:
- MET150
description: Configure Microsoft Teams Admin Center settings so the Data Security Triage Agent can send remediation messages to users in your organization.
locale: en-us
document_id: c4a46bf4-ca60-e1eb-6b96-86acaeb4238d
document_version_independent_id: c4a46bf4-ca60-e1eb-6b96-86acaeb4238d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/copilot-in-purview-triage-dlp-agent-teams-config.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: copilot-in-purview-triage-dlp-agent-teams-config
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/copilot-in-purview-triage-dlp-agent-teams-config.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: c504b419-04a8-bae4-1cc4-8ebf97b91972
---

# Configure Microsoft Teams for the Data Security Triage Agent remediation messages | Microsoft Learn

The Data Security Triage Agent in Data Loss Prevention (DLP) can send remediation messages through Microsoft Teams to users who last modified files containing sensitive information. Before the agent can deliver these messages, you must configure two settings in the Microsoft Teams Admin Center.

This article covers the required Microsoft Teams configuration, how to control which users receive remediation messages, and how to troubleshoot common delivery failures.

Important

Remediation reminders for the Data Security Triage Agent are currently in **Preview**. Features and steps described in this article might change before general availability.

For information about deploying and configuring the triage agent itself, see [Get started with the Microsoft Purview Triage Agent in Data Loss Prevention](copilot-in-purview-triage-dlp-agent-get-started).

## Prerequisites

Before configuring Teams for remediation messages, ensure these requirements are met:

- The Data Security Triage Agent in DLP must be [deployed and configured](copilot-in-purview-triage-dlp-agent-get-started#enable-the-agent).
- **Remediation reminders** must be enabled in the agent's settings. For more information, see [Remediation reminder (Preview)](copilot-in-purview-triage-dlp-agent-get-started#remediation-reminder-preview).
- You must have [Teams admin permissions](/en-us/microsoftteams/using-admin-roles) to configure the Microsoft Teams Admin Center settings described in this article.

Note

The Purview admin or analyst who configures the triage agent might not have permissions to access the Microsoft Teams Admin Center. If that's the case, coordinate with a user in your organization who has [Teams admin permissions](/en-us/microsoftteams/using-admin-roles) to configure these settings.

## Required Teams Admin Center settings

Two settings must be correctly configured for the Data Security Triage Agent to send remediation messages through Microsoft Teams.

### Enable org-wide Microsoft apps

The org-wide Microsoft apps setting controls whether Microsoft-published apps can be used across your organization. This toggle must be set to **On** for the Data Security Triage Agent to function.

1. Sign in to the [Teams Admin Center](https://admin.teams.microsoft.com).
2. Go to **Teams apps** &gt; **Manage apps**.
3. Select **Actions** &gt; **Org-wide app settings**.
4. In the **Org-wide app settings** panel, set the **Microsoft apps** toggle to **On**.
5. Select **Save**.

[![Screenshot of the Microsoft Teams Admin Center showing the Org-wide app settings panel with the Microsoft apps toggle set to On.](media/copilot-in-purview-triage/teams-admin-org-wide-settings.png)](media/copilot-in-purview-triage/teams-admin-org-wide-settings.png#lightbox)

### Make the Data Security Triage Agent app available

The Data Security Triage Agent app must not be blocked for users who should receive remediation messages.

1. Sign in to the [Teams Admin Center](https://admin.teams.microsoft.com).
2. Go to **Teams apps** &gt; **Manage apps**.
3. Search for **Data Security Triage Agent** and select it.
4. Go to the **Users and groups** tab.
5. Verify that **Availability** is set to **Available to everyone (org-wide default)**.

[![Screenshot of the Microsoft Teams Admin Center showing the Data Security Triage Agent app with availability set to Available to everyone.](media/copilot-in-purview-triage/teams-admin-app-available-everyone.png)](media/copilot-in-purview-triage/teams-admin-app-available-everyone.png#lightbox)

Important

The Data Security Triage Agent app doesn't need to be preinstalled for users. Microsoft Purview automatically installs the app for a specific user at the time a remediation message is sent. The app only needs to be *available* (not blocked) in your organization.

## Control who receives remediation messages

When remediation reminders are enabled, the Data Security Triage Agent sends Microsoft Teams messages to users who last modified files containing sensitive information. You can control which users receive these messages through two mechanisms.

### Limit remediation to specific policies

To limit the scope of remediation to specific files or locations, edit the agent's policy scope to enable remediation on only a subset of triage-eligible policies. Policies enabled for remediation are always a subset of policies enabled for triage.

1. In the [Microsoft Purview portal](https://purview.microsoft.com), go to **Agents** &gt; **Explore agents**.
2. Select **Go to agent** for the Triage Agent in Data Loss Prevention.
3. Select **Edit agent** &gt; **Agent configuration**.
4. Under **Set agent scope**, select **Edit**.
5. In the **Select policies** panel, enable the **Remediation** toggle only for the policies where you want remediation messages sent to users.
6. Select **Select policies** to save.

[![Screenshot of the Microsoft Purview portal showing the Select policies panel with the Remediation toggle enabled for specific policies.](media/copilot-in-purview-triage/purview-policy-scope-remediation.png)](media/copilot-in-purview-triage/purview-policy-scope-remediation.png#lightbox)

This approach limits remediation by controlling which DLP policies trigger remediation messages. Users who violate policies that aren't enabled for remediation don't receive Teams messages from the agent.

### Block the app for specific users or groups

To prevent the agent from sending messages to specific users--such as executives, sensitive roles, or specific organizational groups--change the app's availability in the Microsoft Teams Admin Center.

1. Sign in to the [Teams Admin Center](https://admin.teams.microsoft.com).
2. Go to **Teams apps** &gt; **Manage apps**.
3. Search for **Data Security Triage Agent** and select it.
4. Go to the **Users and groups** tab.
5. Select **Edit availability**.
6. Change the availability from **Everyone** to **Specific users or groups**, then add only the users or groups who should receive remediation messages.

[![Screenshot of the Microsoft Teams Admin Center showing the Edit availability panel for the Data Security Triage Agent with options for Everyone, Specific users or groups, and No one.](media/copilot-in-purview-triage/teams-admin-users-groups-scope.png)](media/copilot-in-purview-triage/teams-admin-users-groups-scope.png#lightbox)

Important

Blocking the app for a user is a hard block. Even if an alert is triaged and a remediation message is generated, the message *won't* be sent to users for whom the app is blocked. This result is a failsafe mechanism--if you need to *immediately* stop all remediation messages, set availability to **No one**.

Tip

Use policy scoping in Purview for routine control over what files and locations trigger remediation. Use Teams Admin Center blocking as another safeguard when you need to guarantee that specific users never receive messages from this agent, regardless of which policies are in scope.

## Troubleshoot remediation message delivery

If remediation messages aren't being sent, check:

| Symptom | Likely cause | Resolution |
| --- | --- | --- |
| No users receive messages | Org-wide Microsoft apps toggle is off | Enable org-wide Microsoft apps |
| No users receive messages | Data Security Triage Agent app is blocked | Make the app available |
| Some users don't receive messages | App is blocked for specific users or groups | Check the app's **Users and groups** settings in Teams Admin Center |
| Messages sent but not appearing | User hasn't opened Teams recently | Messages appear once the user signs in to Teams |

Important

A common misconfiguration occurs when the org-wide Microsoft apps toggle is *enabled* but the Data Security Triage Agent app is *individually blocked*. Both settings must be correctly configured for remediation to work.