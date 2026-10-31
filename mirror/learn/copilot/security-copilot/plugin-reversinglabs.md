---
layout: Conceptual
title: ReversingLabs and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-reversinglabs
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the ReversingLabs plugin with Microsoft Security Copilot.
ms.date: 2025-08-25T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: concept-article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
ms.reviewer: shivanpatel
search.audiencetype: Admin
locale: en-us
document_id: b9d1b4e0-ffd3-9519-5564-8b979904ff45
document_version_independent_id: b9d1b4e0-ffd3-9519-5564-8b979904ff45
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-reversinglabs.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-reversinglabs
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-reversinglabs.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: dfec7308-67ae-1684-765b-185b9aaf8b48
---

# ReversingLabs and Microsoft Security Copilot | Microsoft Learn

ReversingLabs provides empowers SOC teams to understand the file-based threats in an environment. Analysts can use Security Copilot to summarize complex file reputation information and file analysis reports for quicker triage and response time.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Security Copilot requires a Spectra Intelligence user account. You'll need to take the following steps before using the plugin.

1. Get your ReversingLabs user account and password.
2. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
3. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.

    - If you use, **ReversingLabs Spectra Analyze**, select "Set Up" to configure and enable it.
    - If you use, **ReversingLabs Spectra Intelligence**, select "Set Up" to configure and enable it.
4. In the ReversingLabs settings pane, provide your ReversingLabs user account and password.
5. Save your changes.

## Sample ReversingLabs Spectra Intelligence prompts

After the ReversingLabs Spectra Intelligence plugin is configured, you can use it by typing `ReversingLabs` in your Security Copilot prompt bar, followed by an action. The following table provides several examples you can try:

| Capability Prompt Suggestion | Description | Example natural language prompt |
| --- | --- | --- |
| `GetFileHashReputation` | This capability is used to retrieve file hash reputation information. | `What is the reputation of hash a6e728c3331f46763f643f7192959716034767e5?` |
| `GetDetailedFileAnalysisResults` | Retrieve additional analysis details for the supplied file hash. | `Get the MITRE ATT&CK techniques from the detailed file analysis of a6e728c3331f46763f643f7192959716034767e5.` |
| `GetDynamicAnalysisReport` | Retrieve the full sandbox dynamic analysis report for the supplied file hash. | `Get the dynamic analysis report for a6e728c3331f46763f643f7192959716034767e5 and summarize any new network connections created.` |

## Sample ReversingLabs Spectra Analyze prompts

After the ReversingLabs Spectra Analyze plugin is configured, you can use it by typing `ReversingLabs` in your Security Copilot prompt bar, followed by an action. The following table provides several examples you can try:

| Capability Prompt Suggestion | Description | Example natural language prompt |
| --- | --- | --- |
| `GetFileClassification` | This capability is used to retrieve file hash classification information from a Spectra Analyze appliance. | `What is the classification of hash a6e728c3331f46763f643f7192959716034767e5?` |
| `GetTiCoreReport` | Retrieve the TitanumCore analysis report for the provided file hash from a Spectra Analyze appliance. | `Get the TiCore report for hash a6e728c3331f46763f643f7192959716034767e5` |

## Frequently Asked Questions (FAQ)

### Why are prompts failing to invoke ReversingLabs?

If prompts fail to invoke, make sure you're using a supported prompt (see the preceding examples). Otherwise, invoke ReversingLabs directing by using `/`.

### Why are prompts failing to return data?

If prompts fail to return data, check your Spectra Intelligence usage limits.

## Provide feedback

To provide feedback, contact [ReversingLabs](https://www.reversinglabs.com/).