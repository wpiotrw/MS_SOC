---
layout: Conceptual
title: Microsoft Copilot in Microsoft Purview prompts and promptbooks | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/copilot-in-purview-promptbooks
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: tracyp
author: MSFTTracyP
manager: laurawi
ms.date: 2026-02-24T00:00:00.0000000Z
ms.update-cycle: 180-days
audience: ITPro
ms.topic: article
ms.service: purview
ms.collection:
- highpri
- purview-compliance
- magic-ai-copilot
search.appverid:
- MET150
description: Learn how to use prompts in Microsoft Security Copilot to gain insights into your Microsoft Purview data.
locale: en-us
document_id: d8cdd680-088d-3103-0617-19caf5abb180
document_version_independent_id: d8cdd680-088d-3103-0617-19caf5abb180
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/copilot-in-purview-promptbooks.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: copilot-in-purview-promptbooks
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/copilot-in-purview-promptbooks.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: c9cc1f6a-56d2-ce3a-c2c1-70c455ff9ae7
---

# Microsoft Copilot in Microsoft Purview prompts and promptbooks | Microsoft Learn

Microsoft Security Copilot is a [stand-alone](/en-us/security-copilot/experiences-security-copilot#standalone-and-embedded-experiences) chat-based experience that helps you get insights from your security data and make connections between datapoints. You interact with the stand-alone experience by entering [prompts](/en-us/security-copilot/prompting-security-copilot), and Security Copilot returns results. This article focuses on the stand-alone experience and how to use it to get insights from your Microsoft Purview data.

## Know before you begin

If you're new to Microsoft Security Copilot, read these articles before you begin creating your own prompts and promptbooks:

- [What is Microsoft Security Copilot?](/en-us/security-copilot/microsoft-security-copilot)
- [Microsoft Security Copilot experiences](/en-us/security-copilot/experiences-security-copilot)
- [Get started with Microsoft Security Copilot](/en-us/security-copilot/get-started-security-copilot)
- [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview)
- [Understand authentication in Microsoft Security Copilot](/en-us/security-copilot/authentication)
- [Prompting in Microsoft Security Copilot](/en-us/security-copilot/prompting-security-copilot)

Important

You must enable the Security Copilot in Purview plugin to use the Microsoft Purview prompts and promptbooks. Use the steps in [Enable the Microsoft Purview source in Microsoft Security Copilot](copilot-in-purview-overview#enable-the-microsoft-purview-source-in-microsoft-security-copilot)

## Prompting in Security Copilot in Microsoft Purview

You can use prompts in three different ways:

### Open ended

[Open ended prompts](/en-us/security-copilot/prompting-security-copilot#create-your-own-prompts) are ones that you write yourself without any suggestions from Security Copilot. You can use these prompts to ask questions about your data that are specific to your needs at a certain point in time or when you need a custom prompt that isn't covered by the prompt suggestions or a promptbook. For more information on creating solid prompts, see [Create effective prompts](/en-us/security-copilot/prompting-tips).

### Prompt suggestions

[Prompt suggestions](/en-us/security-copilot/prompting-security-copilot#select-from-prompt-suggestions) are prewritten prompts that you can use as a starting point and customize to fit your needs. They're listed under all system capabilities. Once you enable the Purview add-in, these prompt suggestions are available to you.

**Get Data Risk Summary** fetches information from Microsoft Purview Information Protection and Microsoft Purview Data Loss Prevention (DLP), and summarizes the risk associated with data impacted by a security incident or a DLP alert.

**Get User Risk Summary** summarizes the risk associated with any user by using their risk profile from Microsoft Purview Insider Risk Management.

**Summarize Purview Alert** provides more details about a Purview alert, including a DLP alert and an insider risk management alert.

**Triage Purview Alerts** retrieves the top or most recent DLP alerts, organizing DLP alerts based on user preferences.

**Zoom Into Purview Data Risk** fetches the information from Microsoft Purview Information Protection and DLP and helps identify the risks and attributes related to the data.

**Zoom Into Purview User Risk** fetches information about the user's activities, including operations and actions done by the user, user activity over a time span, data leakage or exfiltration activities by the user, sequential activities by the user, or any signs of anomalous or unusual behavior by the user.

### Promptbooks

A promptbook is a collection of prompts that are in sequence. The stand-alone experience can use the output from one prompt as the input for the next prompt, and it can run multiple prompts in a sequence. As you use Security Copilot with the [Microsoft Purview add-in enabled](/en-us/security-copilot/manage-plugins#turn-plugins-on-or-off), you may find that you keep using the same prompts over and over. You can save time by collecting all these prompts into a [promptbook](/en-us/security-copilot/using-promptbooks#what-are-promptbooks). Then, you can run the promptbook to get all the insights you need in one go. You can limit the use of a promptbook to yourself, or you can share it with others in your organization.

This article provides two sample sets of prompts you can use for investigating Microsoft Purview Data Loss Prevention (DLP) and Microsoft Purview Insider Risk Management data. You can start with these prompts, then customize them to fit your specific needs. Once you have them tuned the way you want, you can create promptbooks from them.

## Run a prompt

1. Go to [Microsoft Security Copilot](https://go.microsoft.com/fwlink/?linkid=2247989) and sign in with your credentials.
2. By default, the **Purview** plugin should be enabled. To confirm, select **Sources**. In **Plugins**, confirm Microsoft Purview is on. Close **Sources**.
3. Navigate to the prompt bar.
4. Enter your prompt.

For example, enter:

- *Show me the five most recent high severity DLP alerts* or
- *Show me the risk associated with user user@contoso.com*.

For more information on creating solid prompts, see [Create effective prompts](/en-us/security-copilot/prompting-tips)

## Promptbooks for Microsoft Purview features

Here are two sequences of prompts that you can use to investigate Microsoft Purview Data Loss Prevention (DLP) and Microsoft Purview Insider Risk Management data. Refer to [Build your own promptbooks](/en-us/security-copilot/build-promptbooks) for the procedures on how to create, share, and edit a promptbook.

## Sample prompt sequences

### Microsoft Purview Data Loss Prevention

1. Show me the top five high severity DLP alerts.
2. Summarize the first alert in the list.
3. What actions were performed on the file in the alert?
4. Who is the user related to the alert?
5. What are the data risks related to the alert?
6. What is the risk summary of the user?

### Microsoft Purview Insider Risk Management

1. Show me the risk associated with user *user@contoso.com*
2. Show me the exfiltration activities for this user.
3. Show me the sequential activities for this user.
4. Show me obfuscation activities for this user.
5. Show me all the activities that this user performed over the past 30 days.