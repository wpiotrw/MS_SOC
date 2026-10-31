---
layout: Conceptual
title: Compliance Manager scoring | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/compliance-manager-scoring
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2025-02-24T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-compliance-manager
ms.collection: M365-security-compliance
search.appverid:
- MOE150
- MET150
description: Understand how Microsoft Purview Compliance Manager calculates a personalized score based on actions taken to address risks and improve your compliance posture.
ms.custom: seo-marvel-apr2020
locale: en-us
document_id: e656ac07-a92b-58bd-8a98-c58eea9b2b15
document_version_independent_id: e656ac07-a92b-58bd-8a98-c58eea9b2b15
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/compliance-manager-scoring.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: compliance-manager-scoring
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/compliance-manager-scoring.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/eab1aabc-e18c-405b-ac29-e35eb0b15e3b
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/574d2eb1-e22a-49c0-b4eb-64e86dbeee6b
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
2PlusCloud:
- M365
- Azure
- Power
platformId: 9a5a2c23-d250-4fe9-ea70-3843db78a465
---

# Compliance Manager scoring | Microsoft Learn

Important

Recommendations from Compliance Manager should not be interpreted as a guarantee of compliance. It is up to you to evaluate and validate the effectiveness of customer controls per your regulatory environment. These services are subject to the terms and conditions in [Product Terms](https://www.microsoft.com/licensing/terms/). See also [Microsoft 365 licensing guidance for security and compliance](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-compliance-manager).

## Understanding your compliance score

The Compliance Manager dashboard displays your overall compliance score. This score measures your progress in completing recommended improvement actions within controls. Your score can help you understand your current compliance posture. It can also help you prioritize actions based on their potential to reduce risk.

A score value is assigned at these levels:

1. **Improvement action**: Each action has a different impact on your score depending on the potential risk involved. See Action types and scoring below for details.
2. **Assessment**: This score is calculated using improvement action scores. Each Microsoft action and each improvement action managed by your organization is counted once, regardless of how often it's referenced in a control.

The overall compliance score is calculated using improvement action scores, where each Microsoft action is counted once, each technical action you manage is counted once, and each nontechnical action you manage is counted once per group. This logic is designed to provide the most accurate accounting of how actions are implemented and tested in your organization. You may notice that this can cause your overall compliance score to differ from the average of your assessment scores. Read more below about how actions are scored.

#### Initial score based on Microsoft 365 data protection baseline

Compliance Manager gives you an initial score based on the Microsoft 365 data protection baseline. This baseline is a set of controls that includes key regulations and standards for data protection and general data governance. This baseline draws elements primarily from NIST CSF (National Institute of Standards and Technology Cybersecurity Framework) and ISO (International Organization for Standardization), as well as from FedRAMP (Federal Risk and Authorization Management Program) and GDPR (General Data Protection Regulation of the European Union).

Your initial score is calculated according to the default Data Protection Baseline assessment provided to all organizations. Upon your first visit, Compliance Manager is already collecting signals from your Microsoft 365 solutions. You see at a glance how your organization is performing relative to key data protection standards and regulations, and see suggested improvement actions to take.

Because every organization has specific needs, Compliance Manager relies on you to set up and manage assessments to help minimize and mitigate risk as comprehensively as possible.

## Action types and scoring

Improvement actions have points that are awarded when you complete the requirements for implementation. Your action status is updated on your dashboard within 24 hours of a change being made. Once you follow a recommendation to implement a control, you’ll typically see the control status updated the next day.

Points are awarded per action per assessment. For example, if an action is worth 10 points but it appears in two assessments, the action is worth 20 points overall for your tenant. An exception is for [technical actions](compliance-manager-improvement-actions#action-type) that are scoped to your tenant; points for these actions are granted once per action, regardless of how many groups the action belongs to.

### Actions for services supported by Microsoft Defender for Cloud

An improvement action’s overall score is based on the average of scores received by its subscriptions. Each subscription is scored based on the status of the relevant virtual resources.

For example, consider an action with two subscriptions, A and B. Subscription A has 0 out of 1 resource completed, and subscription B has 1 out of 2 resources completed. The subscription scores are: A is 0%, B is 50%. The two subscription scores are averaged to get the overall action score of 25%.

### How score values are determined

Actions are assigned a score value based on whether they’re mandatory or discretionary, and whether they’re preventative, detective, or corrective.

### Mandatory and discretionary actions

- **Mandatory actions** can't be bypassed, either intentionally or accidentally. An example of a mandatory action is a centrally managed password policy that sets requirements for password length, complexity, and expiration. Users must follow these requirements to access the system.
- **Discretionary actions** rely upon users to understand and adhere to a policy. For example, a policy requiring users to lock their computer when unattended is a discretionary action because it relies on the user.

### Preventative, detective, and corrective actions

- **Preventative actions** address specific risks. For example, protecting information at rest using encryption is a preventative action against attacks and breaches. Separation of duties is a preventative action to manage conflict of interest and guard against fraud.
- **Detective actions** actively monitor systems to identify irregular conditions or behaviors that represent risk, or that can be used to detect intrusions or breaches. Examples include system access auditing and privileged administrative actions. Regulatory compliance audits are a type of detective action used to find process issues.
- **Corrective actions** try to keep the adverse effects of a security incident to a minimum, take corrective action to reduce the immediate effect, and reverse the damage if possible. Privacy incident response is a corrective action to limit damage and restore systems to an operational state after a breach.

Each action has an assigned value in Compliance Manager based on the risk it represents:

| **Type** | **Assigned score** |
| --- | --- |
| Preventative mandatory | 27 |
| Preventative discretionary | 9 |
| Detective mandatory | 3 |
| Detective discretionary | 1 |
| Corrective mandatory | 3 |
| Corrective discretionary | 1 |

![Compliance Manager action point values.](media/compliance-score-action-scoring.png)