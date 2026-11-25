---
layout: Conceptual
title: Use the local browser with Copilot Cowork | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/cowork/cowork-local-browser
feedback_system: Standard
uhfHeaderId: MSDocs-Header-Copilot
breadcrumb_path: breadcrumb/copilot-cowork/toc.json
permissioned-type: public
description: Let Microsoft Copilot Cowork run browser tasks in your local Microsoft Edge, using your existing sign-ins and your organization's policies.
ms.date: 2026-10-22T00:00:00.0000000Z
ms.topic: how-to
author: pratyusha1602
manager: ankitdp
ms.author: pravadha
ms.reviewer: angieandrews
ms.service: microsoft-365-copilot
ms.subservice: cowork
ai-usage: ai-assisted
ms.collection: bap-ai-copilot
locale: en-us
document_id: 9a0c226b-82ff-d427-8505-d5822ca4e78d
document_version_independent_id: 9a0c226b-82ff-d427-8505-d5822ca4e78d
original_content_git_url: https://github.com/MicrosoftDocs/copilot-modes-pr/blob/live/articles/cowork/cowork-local-browser.md
site_name: Docs
depot_name: Learn.Copilot-Cowork
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: cowork-local-browser
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cowork/cowork-local-browser.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 48aaad2f-2ee4-e9f0-f8d3-688744b070ea
---

# Use the local browser with Copilot Cowork | Microsoft Learn

Microsoft Copilot Cowork can complete browser automation for you in Microsoft Edge on your device, using the sites you're already signed in to. Cowork shows its work in a hidden Edge tab so you can stay in the conversation while it acts on your behalf. This article explains how browser use works, what you need to set up, and what to expect when Cowork hands the browser back to you.

Note

In GCC, local browsing is governed by the default-off **Local Browsing Allowed** policy. Enabling local browsing doesn't enable built-in web search, web page retrieval, or image search. For government access and feature differences, see [Cowork in GCC](cowork-government). The web address and admin click path below describe the worldwide experience.

## How browser use works

When Cowork needs to use a website to complete a task, it opens a hidden tab in Microsoft Edge and works there. You stay in the Cowork conversation and watch progress through chat updates and the side panel.

Because the tab runs in your own copy of Edge, it uses your existing single sign-on, cookies, and sessions. The agent has exactly the same access to sites that you have when you browse by hand—no more and no less. Credentials, cookies, and session tokens stay on your device.

If Cowork needs information from you to keep going—for example, an address or a confirmation code—it asks you in the chat instead of switching you over to the browser. For sensitive requests, such as signing in, Cowork switches to the browser so you can enter the required information.

## Where browser use is available

Browser use is available in Cowork on the web at https://copilot.cloud.microsoft.

| Surface | Browser use supported? |
| --- | --- |
| Cowork on the web (Microsoft Edge) | Yes |
| Cowork on the web (other browsers) | Not yet. More information: If you're not using Microsoft Edge |
| Microsoft Copilot desktop app | No. If you ask the desktop app to run a browser task, Cowork tells you that browser tasks run in Cowork on the web. |

## Requirements

Before Cowork can use the browser on your behalf, ensure you meet the following requirements:

- Your tenant admin enabled browser use for your organization. For worldwide tenants, this setting is **Cowork Browsing**. For GCC, use the [government browser policy guidance](cowork-government#cowork-capabilities-in-gcc).
- You're using Cowork in a browser. This feature isn't currently supported in the desktop app or [on mobile](cowork-mobile).
- Edge is installed on your device. Edge doesn't need to be your default browser.
- You're using the recommended minimum Edge version 152.0.4191.53 or higher.
- You're signed in to Edge with the same work or school account you use for Cowork. InPrivate windows and guest profiles don't have your sign-in sessions, so browser tasks can't run there.

### If you're not using Microsoft Edge

Browser tasks currently work only in Microsoft Edge. If you start Cowork from a different browser or if Edge isn't installed, Cowork still completes every step of your request that doesn't need the browser. For example, if you ask it to file an expense report, it can still pull receipts from Outlook and draft the line items, but Cowork doesn't tell you which steps need Edge. It says that it doesn't have access to a browser tool to complete the task.

## First-run consent

The first time Cowork needs to use the browser for one of your tasks, a consent notice appears in the conversation.

- Select **I understand** to let Cowork use the browser. After that, Cowork uses normal per-site and per-action permissions and doesn't show the first-run notice again.
- If you don't select **I understand**, browser use stays off. Cowork keeps working on any parts of your request that don't need the browser, and tells you which steps it skipped. The notice appears again the next time you ask for a browser task.

Your acknowledgment is stored in Microsoft Edge on your device, not in Cowork.

Note

You can assign policies to user groups to enable browser automation through Edge with Edge 152, released the week of August 24, 2026. Tenant admins can use the Edge policy documented in [Microsoft Edge Browser policy documentation](/en-us/deployedge/microsoft-edge-policies/copilotcoworktoolactionsenabled) to control the Edge instances in which Cowork is allowed to use the browser.

## Run a browser task

For GCC, every action requires explicit approval. Use the [GCC approval requirements](cowork-government#review-the-plan-and-approve-actions) rather than interpreting the sensitive-action examples below as the full government approval scope.

You don't need a special command to start a browser task. Ask Cowork to do something that requires the web, and it decides when to open the browser.

1. In the Cowork conversation, describe the task—for example, *"File my expense report in Concur for last week's trip to Seattle"* or *"Find the cheapest nonstop flight from SEA to JFK on Friday and put a hold on it."*
2. Watch the conversation. Cowork shows progress chips as it works, such as *Opening Concur*, *Filling expense details*, or *Submitting form*.
3. Answer any questions Cowork asks. When the agent needs information it can't get from the page, it asks you in the chat—for example, *"Which corporate card did you use?"*—and waits for your reply before continuing.
4. Approve sensitive actions when prompted. For actions that submit personal data or are otherwise sensitive or consequential, Cowork shows an approval card in the conversation. Review it and select **Approve** to approve the action once, or select **Reject**.

The hidden tab stays out of your way during the task. Cowork shows it only when it needs to hand the browser back to you or when you select **Switch to tab**.

## When Cowork hands the browser back to you

For most tasks, the Edge tab never appears. In a few cases, Cowork asks you to take over and shows the tab, including:

- When a **CAPTCHA** or human-verification prompt appears and must be resolved.
- When **credentials**, such as a **password**, or a **multifactor authentication** code are needed.
- When account settings must be changed, or when the account is **locked** or requires a **password reset**.

In each case, Cowork pauses the task and asks you to take over. When you're done, Cowork picks the task back up. If you can't complete the step, Cowork stops the task and reports what was left unfinished.

## Sites your organization blocks

Because Cowork drives your local Edge, it inherits every site restriction your admin already enforces—web filtering, Conditional Access, browser-management policy, and Microsoft Purview data loss prevention (DLP). The agent has the same reach you do, never more.

If a task can't continue because of a DLP restriction, Cowork tells you which step is blocked, explains that your organization's policy doesn't allow that browser action on that site, and suggests manual steps you can take.

## Resume an interrupted browser task

If a browser task is interrupted—for example, you close the tab, put your device to sleep, or lose your network connection—Cowork pauses the task instead of failing it.

To pick the task back up:

1. Open the same Cowork conversation when you're ready.
2. Send a message such as *"continue"*, *"resume"*, or any follow-up that relates to the task.
3. Cowork detects the interrupted browser task, checks that Edge is available again, and either keeps going or asks you to confirm before it resumes.

## Privacy and auditing

When Cowork uses the browser on your behalf:

- The session, cookies, and credentials stay in your local copy of Edge. They aren't sent to Cowork's servers.
- The sites Cowork visits and the actions it takes are scoped to your identity and your device. Existing Microsoft Entra sign-in, Conditional Access, and Microsoft Purview policies apply unchanged.

Learn more about tenant-level controls and audit logs in [Manage Cowork](cowork-admin-governance).

## Admin control

Admins can use the following browser features:

- Opt the tenant in to browser use in the Microsoft 365 admin center.
- Limit the browser use feature to specific security groups or individuals.

For worldwide and GCC tenants, admins enable Cowork browsing by performing the following steps. This feature is disabled by default.

1. From the menu, select **Copilot** &gt; **Settings** &gt; **View All** &gt; **Cowork settings**.
2. Under **Allow browser access**, select **Allow Cowork to use the Microsoft Edge browser to perform tasks on behalf of users**.

## Related information

- [Use Cowork](use-cowork)
- [Get started with Cowork](get-started)
- [Best practices for Cowork](best-practices)
- [Cowork common questions](cowork-faq)
- [Manage Cowork](cowork-admin-governance)