---
layout: Conceptual
title: Test a sensitive information type | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-test-a-sit
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-sensitive-information-types
ms.date: 2026-10-14T00:00:00.0000000Z
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Test how a custom sensitive information type performs over time by using the Microsoft Purview portal. Use this process to validate detection behavior before broader deployment.
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1030
ai-usage: ai-assisted
locale: en-us
document_id: 7b0c142d-5ba8-061f-4ec3-a234eb731666
document_version_independent_id: 7b0c142d-5ba8-061f-4ec3-a234eb731666
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-test-a-sit.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-test-a-sit
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-test-a-sit.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: e50a15fe-578d-610d-c83c-a935bce663cf
---

# Test a sensitive information type | Microsoft Learn

At any time during the life of a sensitive information type (SIT), you can test how it performs. This article explains how to do that in the Microsoft Purview portal.

## Before you begin

Before you test a sensitive information type, make sure you have the following background knowledge and preparation.

- You should be familiar with sensitive information types and what they're composed of. For more information, see, [Learn about sensitive information types](sit-sensitive-information-type-learn-about).
- It's critical to understand the roles of:
    - [regular expressions](https://www.boost.org/doc/libs/1_68_0/libs/regex/doc/html/) - Microsoft 365 sensitive information types uses the Boost.RegEx 5.1.3 engine
    - keyword lists - you can create your own as you define your sensitive information type or choose from existing keyword lists
    - [keyword dictionary](sit-create-a-keyword-dictionary)
    - [Sensitive information type functions](sit-functions)
    - [confidence levels](sit-sensitive-information-type-learn-about#more-on-confidence-levels)
- Familiarize yourself with [Sensitive information type limits](sit-limits).

Important

Microsoft Customer Service & Support can't assist with creating custom classifications or regular expression patterns. Support engineers can provide limited support for the feature, such as, providing sample regular expression patterns for simulation purposes, or helping to troubleshoot an existing regular expression pattern that's not triggering as expected. However, they can't provide assurances that any custom content-matching development fulfills your requirements or obligations.

### Permissions and role groups

The account you use to perform tests of SITs must be assigned one of these roles in the Microsoft Purview *and* one of these roles or role groups in Exchange.

#### Role groups assignments in the Microsoft Purview portal

The account you use must be assigned one of these role groups in the Microsoft Purview portal:

- Compliance Administrator
- Compliance Data Administrator
- Security Administrator
- Communication Compliance Admins
- Information Protection Admins
- Information Protection Investigators
- Organization Management

To assign a user to a role group in the Microsoft Purview portal, follow the steps in [Add users or groups to a Microsoft Purview built-in role group](purview-permissions#add-users-or-groups-to-a-microsoft-purview-built-in-role-group).

#### Microsoft Entra Roles in Exchange Online

The following roles can be assigned either in the Exchange Admin center or in Microsoft Entra.

- Communication Compliance Admin
- Communication Compliance Investigation
- Compliance Admin
- Data Loss Prevention
- Information Protection Admin
- Information Protection Investigator
- Information Protection Reader
- Insider Risk Management Admin
- Insider Risk Management Investigation
- Privacy Management Admin
- Privacy Management Investigation
- Security Admin

#### Microsoft Entra Role Groups in Exchange Online

The following Exchange Online role groups satisfy this requirement:

- Communication Compliance
- Communication Compliance Administrators
- Compliance Administrator
- Organization Management
- Compliance Management
- Information Protection
- Information Protection Admins
- Information Protection Investigators
- Information Protection Readers
- Insider Risk Management
- Insider Risk Management Admins
- Insider Risk Management Investigators
- Privacy Management
- Privacy Management Administrators
- Privacy Management Investigators
- Security Administrator

### Enable access to simulation mode

To enable access to simulation mode, your account must be assigned one of the following role groups:

**Applies to these role groups:**

- Communication Compliance Admins
- Information Protection Admins
- Information Protection Investigators
- Organization Management

## Test the effects of a sensitive information type

You can test the effects of any sensitive information type in the **Sensitive info types** list. Test each sensitive information type that you create before using it in a policy.

This uploaded-file test is different from auto-labeling policy simulation. It tests the SIT against the file you upload; it doesn't refresh classification for existing SharePoint or OneDrive files. A policy simulation uses available classification results for those files. See [Auto-labeling classification and simulation concepts](auto-label-classification-simulation) for how to interpret differences and when classification needs updating.

Note

This procedure is only supported for unencrypted files.

1. Prepare two files, for example, two Word documents. One should have content that matches the elements you specified in your sensitive information type. The other should have content that doesn't match.
2. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Information Protection** &gt; **Classifiers** &gt; **Sensitive info types** and choose the sensitive information type from the list to open the details pane. Choose **Test**.
3. Upload a file and choose **Test**. (You can only upload and test one file at a time.)
4. On the **Match results** page, review the results and choose **Finish**.
5. Perform the same steps for the second file.