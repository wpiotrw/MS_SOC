---
layout: Conceptual
title: Create effective prompts | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/prompting-tips
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: How to write effective prompts with Microsoft Security Copilot
ms.date: 2026-06-02T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: how-to
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom:
- cx-ti
- cx-cop
- sfi-image-nochange
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: 28a469a6-9d1e-ccb0-7cb3-0cae626b3ade
document_version_independent_id: 28a469a6-9d1e-ccb0-7cb3-0cae626b3ade
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/prompting-tips.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: prompting-tips
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/prompting-tips.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 089e3d0b-b615-bbd1-8893-8f87b1b890f2
---

# Create effective prompts | Microsoft Learn

As with any Microsoft Copilot, a prompt refers to the text-based, natural language input you provide in the prompt bar that instructs Security Copilot to generate a response. The quality of the response that Security Copilot returns depends in large part on the quality of the prompt used. In general, a well-crafted prompt with clear and specific inputs leads to more useful responses by Security Copilot.

Watch the following video to learn more about creating effective prompts:

To see the different ways you can create prompts in Security Copilot, read [Prompting in Security Copilot](prompting-security-copilot).

## Elements of an effective prompt

Effective prompts give Security Copilot adequate and useful parameters to generate a valuable response. Security analysts or researchers should include the following elements when writing a prompt.

- **Goal** - specific, security-related information that you need
- **Context** - why you need this information or how you plan to use it
- **Expectations** - format or target audience you want the response tailored to
- **Source** - known information, data sources, or plugins Security Copilot should use

[![List of available promptbooks](media/prompt-elements.png)](media/prompt-elements.png#lightbox)

Every good prompt should have a goal. Whether it comes in the form of instructions or questions, it should indicate what you want out of your current session.

For Security Copilot, context can mean such information as the time frame, or that you plan to use the response for a report. Expectations can include whether you want the response to be in a table format, a list of action steps, a summary, or even a diagram. Source might be useful in specifying which Microsoft plugins you're referring to, if needed. Some plugins require more context to work effectively or supporting plugins to ensure a response when initial responses fail.

## Other prompting tips

Some things to remember when coming up with your own prompts:

- **Be specific, clear, and concise** as much as you can about what you want to achieve. You can always start simply with your first prompt, but as you get more familiar with Security Copilot, include more details following the elements of an effective prompt.

    - Basic prompt: Pearl Sleet actor
    - Better prompt: Can you give me information about Pearl Sleet activity, including a list of known indicators of compromise and tools, tactics, and procedures (TTPs)?
- **Iterate.** Subsequent prompts are typically needed to either clarify what you need further, or try other versions of a prompt to get closer to what you're looking for. Like all LLM-based systems, Security Copilot can respond to the same prompt in slightly different ways.
- **Provide necessary context** to narrow down where Security Copilot looks for data.

    - Basic prompt: Summarize incident 15134.
    - Better prompt: Summarize incident 15134 in Microsoft Defender XDR into a paragraph that I can submit to my manager and create a list of entities involved.
- **Give positive instructions** instead of "what not to do". Security Copilot is geared toward action, so telling it what you want it to do for exceptions is more productive.

    - Basic prompt: Give me a list of unmanaged devices in my network.
    - Better prompt: Give me a list of high-risk unmanaged devices in my network. If they're named "test", remove them from the list.
- **Directly address Security Copilot as "You"**, as in, "You should ..." or "You must ...", as this is more effective than referring to it as a model or assistant.

​While these guidelines can help you get started in creating prompts, it’s important to note that you’re not limited to forming prompts following the structure of the previous examples. What’s great about Security Copilot is that it's designed to respond to questions or instructions made in your own words (that is, using natural language).

You have the flexibility to adapt these guidelines to your specific needs.

Watch the following video to learn more about creating better prompts: