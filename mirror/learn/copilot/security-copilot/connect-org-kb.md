---
layout: Conceptual
title: Connect your org knowledge base | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/connect-org-kb
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn the different ways to connect your org's internal knowledge bases into Copilot.
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
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: 583ec07d-ec48-60f7-dc17-c27128cffa95
document_version_independent_id: 583ec07d-ec48-60f7-dc17-c27128cffa95
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/connect-org-kb.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: connect-org-kb
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/connect-org-kb.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/45da903a-8cff-40ca-99bf-9237f80d6982
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/7af51462-ed96-4b66-aefd-ea77337d1b96
platformId: c0d32064-2f60-0562-c642-f83394279ee4
---

# Connect your org knowledge base | Microsoft Learn

Important

Some information in this article relates to a prereleased product which might be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

Using the Azure AI search plugin or file upload, you can bring in business context like your organization's security knowledge base into Microsoft Security Copilot so you can directly reference them in your session.

An organization's knowledge base might include the repository of an organization's proprietary information, like: wikis, policy and compliance documents, investigation and response procedures templates, historical data, KQL (Kusto Query Language) libraries, or even information from public repositories like Microsoft Learn documentation, prescriptive guidelines, and frameworks.

Integrating this wealth of knowledge into Copilot allows Copilot to reason over the knowledge base or documents and generate responses that are more relevant, specific, and customized to your operational need.

## Options for connecting a knowledge base

There are two ways to integrate a knowledge base into Copilot:

1. Azure AI Search plugin – set up the Azure AI Search plugin to connect to an Azure AI Search index containing your organization's knowledge base. Follow the steps in Prompting for a knowledge base connected using Azure AI Search.
2. File upload – upload your files and get Copilot to reason over them. Follow the steps in Prompting for a knowledge base uploaded as a file.

## Prompting for a knowledge base connected using Azure AI Search

To connect a knowledge base using the Azure AI Search plugin, follow the steps in [Azure AI Search](plugin-azure-ai-search).

Once connected, prompt Copilot to look for information related to the knowledge base you uploaded. Make sure to mention "**Azure AI Search**" in the prompt. For example:

- New staff can ask Copilot about the organization’s processes within their Copilot workflows. This avenue can speed up the onboarding process.

    *Sample prompt: Summarize my organization’s multifactor authentication policies in Azure AI Search.*
- While performing an incident investigation, SOC analysts can ask Copilot for investigation steps from their organization’s processes and procedures.

    *Sample prompt: Search my Azure AI Search index for investigation steps that I should follow for this incident involving multiple failed sign-in attempts by a user.*

The Azure AI Search plugin performs a semantic and keyword search across the index's contents to find the relevant information so it's advisable to be as specific as you can in prompting. For more on the elements of an effective prompt and other prompting tips, read [Create effective prompts](prompting-tips).

## Prompting for an uploaded file

To upload a file, follow the steps in [Add a source by uploading a file](upload-file).

You can use this option to directly add text documents as a source that Copilot can refer to when responding to a prompt that references it.

In the prompt bar, you need to mention "uploaded files" if you want Copilot to reason over your available files. You can also include the file name if you would like to guide Copilot to reason over a specific file. For example:

- You can ask Copilot to check a user account's actions against your organization's data handling policies to find out if any violations were committed.

    *Sample prompt: Based on the Contoso Data Handling Policy file, list any actions taken by user Preston-123 that might be a violation of the data handling policies. Include a verdict to the action and level of confidence of the verdict. Cite the policy name and section applicable to the verdict.*

## Known limitations

For both the Azure AI Search plugin and file upload methods of connecting knowledge bases:

- Copilot reasons over text content only, not other data or media types.
- Searches over structured content like tables aren't well-supported yet.