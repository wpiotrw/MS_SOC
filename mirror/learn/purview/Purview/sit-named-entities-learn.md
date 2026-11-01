---
layout: Conceptual
title: Learn about named entities | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-named-entities-learn
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2024-10-08T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: article
ms.service: purview
ms.subservice: purview-sensitive-information-types
ms.collection:
- purview-compliance
description: Learn how named entities help you detect sensitive items containing names of people, physical addresses, and medical terms via data loss prevention policies
locale: en-us
document_id: 35e96b1a-dc01-e50e-ddc4-c0237e2a4c2f
document_version_independent_id: 35e96b1a-dc01-e50e-ddc4-c0237e2a4c2f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-named-entities-learn.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-named-entities-learn
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-named-entities-learn.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b916aa27-f8c3-eed6-06bd-5a73be34f8a6
---

# Learn about named entities | Microsoft Learn

*Named entities* are [sensitive information types](sit-sensitive-information-type-learn-about) (SIT). They're complex dictionary and pattern-based classifiers that you can use to detect person names, physical addresses, and medical terms and conditions. You can see them in the **Microsoft Purview portal &gt; Data classification &gt; Sensitive info types**. Here's a partial list of where you can use SITs:

- [Microsoft Purview Data Loss Prevention policies (DLP)](dlp-learn-about-dlp)
- [Sensitivity labels](sensitivity-labels)
- [Insider risk management](insider-risk-management-solution-overview)
- [Microsoft Defender for Cloud Apps](/en-us/cloud-app-security/what-is-cloud-app-security)
- [Microsoft Purview Information Protection](apply-sensitivity-label-automatically)
- [Data Lifecycle Management](data-lifecycle-management)
- [Records management](records-management)
- [Microsoft Purview eDiscovery](ediscovery)
- [Microsoft Priva](/en-us/privacy/priva/priva-overview)
- [Exact data match sensitive information types](sit-learn-about-exact-data-match-based-sits)

DLP makes special use of named entities in *enhanced policy templates*, which are preconfigured DLP policies that you can customize for your organizations needs. You can also [create your own DLP policies](dlp-create-deploy-policy) from a blank template and use a named entity SIT as a condition. Entity Match and other advanced classifiers are offered only to users with E5 licenses.

## Examples of named entity SITs

Named entity SITs come in two flavors, *bundled* and *unbundled*

Bundled named entity SITs detect all possible matches. Use them as broad criteria in your DLP policies for detecting sensitive items.

Unbundled named entity SITs have a narrower focus, like a single country. Use them when you need a DLP policy with a narrower detection scope.

Note

To use named entity SITs, you must activate [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) for the relevant [data loss prevention settings](dlp-configure-endpoint-settings) before they will be discoverable.

Here are some examples of named entity SITs. You can find all of them in [Sensitive information type entity definitions](sit-sensitive-information-type-entity-definitions).

| Named Entity | Description | Bundled/Unbundled |
| --- | --- | --- |
| All full names | Detects all possible matches of full names | bundled |
| All physical addresses | Detects all possible matches of physical addresses | bundled |
| All medical terms and conditions | Detects all possible matches of medical terms and conditions | bundled |
| Australia Physical Addresses | Detects patterns related to physical addresses from Australia. Included in All physical addresses SIT. | unbundled |
| Blood Test Terms | Detects terms related to blood tests, such as 'hCG'. English terms only. Included in All medical terms and conditions SIT | unbundled |
| Brand Medication Names | Detects names of brand medication, such as 'Tylenol'. English terms only. Included in All medical terms and conditions. | unbundled |

## Examples of enhanced DLP policies

Here are some examples of enhanced DLP policies that use named entity SITs. You can find all 10 of them in the **Microsoft Purview portal** Navigate to **Data loss prevention** &gt; **Create policy**. Enhanced templates can be used in DLP and auto-labeling.

| Policy category | Template | Description |
| --- | --- | --- |
| Financial | U.S. Gramm-Leach-Bliley Act (GLBA) Enhanced | Helps detect the presence of information subject to Gramm-Leach-Bliley Act (GLBA), including information like social security numbers or credit card numbers. This enhanced template extends the original by also detecting people's full names, U.S./U.K. passport number, U.S. driver's license number and U.S. physical addresses. |
| Medical and health | Australia Health Records Act (HRIP Act) Enhanced | Helps detect the presence of information commonly considered to be subject to the Health Records and Information Privacy (HRIP) act in Australia, like medical account number and tax file number. This enhanced template extends the original by also detecting people's full names, medical terms and conditions, and Australia physical addresses. |
| Privacy | General Data Protection Regulation (GDPR) Enhanced | Helps detect the presence of personal information for individuals inside the European Union (EU) to help meet GDPR privacy obligations. This enhanced template detects people's full names and physical addresses for countries in the EU. |