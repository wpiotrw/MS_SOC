---
layout: Conceptual
title: Prompting in Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/prompting-security-copilot
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn the different ways to interact with Microsoft Security Copilot using promptbooks or your own words using the prompt bar.
ms.date: 2026-06-01T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: concept-article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom:
- cx-ti
- cx-cop
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: e6c87a1d-04e6-5fa8-cd42-228f91c173dd
document_version_independent_id: e6c87a1d-04e6-5fa8-cd42-228f91c173dd
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/prompting-security-copilot.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: prompting-security-copilot
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/prompting-security-copilot.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: f2299510-453b-396c-539a-669a6b33a527
---

# Prompting in Microsoft Security Copilot | Microsoft Learn

Once you're all set up in Security Copilot, you can use prompts to interact with the system.

Depending on your experience, you might start with either **agents** or **chat**:

- In newer experiences, agents are the primary entry point.
- To begin prompting, open **All history** and select **New session** to start a chat session.

Prompts help you ask questions, investigate issues, and explore data using natural language. Promptbooks are a series of prompts that are grouped together to accomplish specific security-related tasks.

## Start a prompt session

To begin prompting:

1. Select **History**.
2. Review your existing sessions (if any).
3. Select **New session**.
4. Enter your prompt.

This opens a chat session where you can interact with Security Copilot.

## Use the prompts and promptbooks library

The prompts and promptbooks library in Security Copilot helps you quickly harness the power of the platform in a way that aligns with your role. This set of prompts and promptbooks are designed to guide you through features and capabilities most relevant to your work.

The curated prompts and promptbooks provide easy access to role-based examples to help you get started quickly and streamline your workflow.

Note

Prompts and promptbooks are available within a chat session and through the promptbooks library.

![Screenshot the prompts to try in Security Copilot.](media/prompts-try.png)

### Apply filters

You can apply filters to find prompts or promptbooks that are most relevant to you. Narrow down search results by applying multiple filters to better suit your role or scenario.

Customize your search by selecting filters based on:

- **Roles** - Examples include: CISO, SOC analyst, threat intel analyst, and IT administrator.
- **Plugins** - Examples include: Microsoft Defender XDR, Microsoft Threat Intelligence, and Natural language to KQL for advanced hunting.

You can also use the search function to look up prompts or promptbooks by title.

### Using the prompts library

Follow these steps to use ready-made prompts:

1. Select **Prompts** in an active session and apply filters as needed.
2. Use the search function to find the title of a prompt or select a prompt from the library.
3. If the prompt requires input (for example, an app name or incident ID), provide the necessary details.
4. Select **Send**![Send button](media/send-icon.png) or press Enter.

### Using the promptbooks library

There are two ways you can access the promptbooks library:

- Through an active session
- Through the Security Copilot menu

#### Access promptbooks from a session

There are several actions available when working with promptbooks:

![Screenshot of the promptbook options.](media/promptbook-options.png)

You can choose any of the following actions:

- Filter by **Promptbooks**
- Select **Get started** to run a promptbook
- View details of a promptbook
- Duplicate a promptbook
- Share a promptbook

#### Access promptbooks from the menu

Both prebuilt and user-built promptbooks across your organization appear in the promptbook library. View promptbooks by going to the Security Copilot menu and selecting **Promptbooks**.

To view prebuilt promptbooks, see [Try promptbooks](using-promptbooks).

[![Screenshot of library in menu.](media/using-promptbooks-menu.png)](media/using-promptbooks-menu.png#lightbox)

The promptbook library displays all available promptbooks. They are listed by name, owner, description, number of prompts, required plugins, and visibility.

[![Screenshot of library.](media/promptbook-library.png)](media/promptbook-library.png#lightbox)

Use the search bar in the **Promptbook library** to locate promptbooks by name or apply filters to refine your results.

## Choose individual prompts and promptbooks

In an active session, select the prompts icon ![Screenshot of sparkle icon.](media/sparkle-button.png) to view available prompts and promptbooks.

[![Screenshot of prompt bar](media/prompt-bar-sparkle.png)](media/prompt-bar-sparkle.png#lightbox)

Promptbooks are collections of prompts that run in sequence to complete a task, with each prompt building on the previous one.

For more information, see [Using promptbooks](using-promptbooks).

## When to use prompts and agents

You can use both prompts and agents depending on your task:

- Use **agents** for structured workflows and repeatable tasks
- Use **prompts** for ad-hoc questions and investigations

You can move between agents and prompts as needed to complete your work.

## Create your own prompts

Using the prompt bar, you can enter requests in your own words for Security Copilot to answer.

1. Enter your prompt in an active session.
2. Select **Send**![Send button](media/send-icon.png) or press Enter.
3. Wait for Security Copilot to generate a response.

    As the response is being formed, Security Copilot shows steps in the [process log](navigating-security-copilot#view-the-process-log). The process log provides visibility into the actions taken, sources used, and processing time.

    You can cancel, edit, or delete your prompt during response generation.
4. Review the response and verify that the results meet your needs.

You can continue the session with additional prompts to refine or expand your results. If needed, rephrase your prompt, provide more details, or specify the desired format.

For guidance on writing effective prompts, see [Elements of an effective prompt](prompting-tips#elements-of-an-effective-prompt).

Watch the following video to learn more about prompting:

## Providing feedback

Whether you use promptbooks or your own prompt, providing feedback helps improve Security Copilot. Feedback options appear below each response.

[![Screenshot of prompt feedback options.](media/prompt-feedback-pill.png)](media/prompt-feedback-pill.png#lightbox)

Remember, Security Copilot doesn't always get everything right, and AI-generated content can contain inaccuracies.