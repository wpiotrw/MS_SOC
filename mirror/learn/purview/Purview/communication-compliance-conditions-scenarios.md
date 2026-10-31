---
layout: Conceptual
title: Configure conditions for key Communication Compliance scenarios | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/communication-compliance-conditions-scenarios
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use conditions in Microsoft Purview Communication Compliance by viewing a library of condition examples.
keywords: Microsoft 365, Microsoft Purview, compliance, Communication Compliance, conditions
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2024-09-18T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-communication-compliance
ms.collection:
- purview-compliance
search.appverid:
- MET150
- MOE150
ms.custom: sfi-image-nochange
locale: en-us
document_id: 8de9186a-9ce2-de25-365f-40f5a9d3b9e7
document_version_independent_id: 8de9186a-9ce2-de25-365f-40f5a9d3b9e7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/communication-compliance-conditions-scenarios.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: communication-compliance-conditions-scenarios
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/communication-compliance-conditions-scenarios.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
platformId: 6bf9b441-a32b-5ef1-60ad-5bea03a9c329
---

# Configure conditions for key Communication Compliance scenarios | Microsoft Learn

Important

[Microsoft Purview Communication Compliance](communication-compliance) provides the tools to help organizations detect regulatory compliance (for example, SEC or FINRA) and business conduct violations such as sensitive or confidential information, harassing or threatening language, and sharing of adult content. Communication Compliance is built with privacy by design. Usernames are pseudonymized by default, role-based access controls are built in, investigators are opted in by an admin, and audit logs are in place to help ensure user-level privacy.

This article provides multiple examples of creating conditions with the condition builder in [Microsoft Purview Communication Compliance](communication-compliance). Use the examples for your own scenarios and modify them as needed for your organization.

For general information on creating conditions for Communication Compliance policies, see [Choose conditions for your Communication Compliance policies](communication-compliance-policies#choose-conditions-for-your-policies).

## Data security examples

### Example 1:

Detect all communications sent outside of Contoso.com that contain patterns detected by the *Insiders* sensitive info type OR that include any of these keywords:

- "confidential"
- "top secret"
- "Project Sparta"
- "GenAI"

![Communication Compliance condition builder example 1.](media/communication-compliance-condition-builder-example-1.png)

### Example 2:

Detect all communications coming from outside or sent outside contoso.com that contain patterns detected by the *Insiders* sensitive info type.

![Communication Compliance condition builder example 2.](media/communication-compliance-condition-builder-example-2.png)

### Example 3:

Proactively detect sharing of secret keys and passwords outside of contoso.com.

![Communication Compliance condition builder example 3.](media/communication-compliance-condition-builder-example-3.png)

### Example 4:

Detect Teams phishing requests sent as multifactor authentication requests by using the *Phishing Patterns* sensitive info type.

![Communication Compliance condition builder example 4.](media/communication-compliance-condition-builder-example-4.png)

### Example 5:

Analyze all messages coming from the stateactor1.com, stateactor2.com, and stateactor3.com domains OR messages containing these keywords:

- recruit
- payment for your services
- good offer
- hiring, recruitment

![Communication Compliance condition builder example 5.](media/communication-compliance-condition-builder-example-5.png)

### Example 6:

Analyze specific emails sent to external domains by detecting patterns by using the *Personal* sensitive info type, but ignore specific keywords.

![Communication Compliance condition builder example 6.](media/communication-compliance-condition-builder-example-6.png)

### Example 7:

Analyze and view all emails sent to personal email accounts.

![Communication Compliance condition builder example 7.](media/communication-compliance-condition-builder-example-7.png)

## Business conduct examples

### Example 1:

Detect inappropriate content sent in messages by using the *Sexual*, *Violence*, *Hate*, and *Self-harm* Microsoft provided trainable classifiers OR by using a curated keyword dictionary.

![Communication Compliance condition builder example 8.](media/communication-compliance-condition-builder-example-8.png)

### Example 2:

Detect threats and harassment addressed to Contoso's key executives by using the *Targeted Harassment*, *Threat*, and *Hate* Microsoft provided trainable classifiers.

![Communication Compliance condition builder example 9.](media/communication-compliance-condition-builder-example-9.png)

### Example 3:

Detect all messages that contain patterns detected by the *ABA Routing Number*, *Credit Card Number*, *U.S. Bank Account Number*, *U.S. Individual Taxpayer Identification Number (ITIN)*, and *U.S. Social Security Number (SSN)* sensitive information types sent by any user, but not sent to or sent by the Finance Team.

![Communication Compliance condition builder example 10.](media/communication-compliance-condition-builder-example-10.png)