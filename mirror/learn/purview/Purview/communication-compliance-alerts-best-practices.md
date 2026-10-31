---
layout: Conceptual
title: Best practices for managing your alerts queue | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/communication-compliance-alerts-best-practices
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn best practices for managing the volume of alerts in Microsoft Purview Communication Compliance.
keywords: Microsoft 365, Microsoft Purview, compliance, Communication Compliance
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: Admin
ms.topic: best-practice
ms.service: purview
ms.subservice: purview-communication-compliance
ms.collection:
- highpri
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- highpri
ms.custom: admindeeplinkCOMPLIANCE
search.appverid:
- MET150
- MOE150
locale: en-us
document_id: fc1f5974-ccf6-4699-78bc-67c51c8b5ba4
document_version_independent_id: fc1f5974-ccf6-4699-78bc-67c51c8b5ba4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/communication-compliance-alerts-best-practices.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: communication-compliance-alerts-best-practices
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/communication-compliance-alerts-best-practices.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: a1a8ceda-9b40-5bbe-2181-3cf7f7d0b443
---

# Best practices for managing your alerts queue | Microsoft Learn

Important

[Microsoft Purview Communication Compliance](communication-compliance) provides the tools to help organizations detect regulatory compliance (for example, SEC or FINRA) and business conduct violations such as sensitive or confidential information, harassing or threatening language, and sharing of adult content. Communication Compliance is built with privacy by design. Usernames are pseudonymized by default, role-based access controls are built in, investigators are opted in by an admin, and audit logs are in place to help ensure user-level privacy.

After you configure Microsoft Purview Communication Compliance, make some adjustments to manage the volume of alerts that you receive. Use the list of best practices in this article to help create policies that cover as many users as possible while reducing the number of nonactionable alerts.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Understand keyword list volumes

Many customers use custom keyword lists for compliance scenarios. Understanding the volume of policy matches for each keyword can help you tune your policies. Use the [Sensitive information type per location report](communication-compliance-reports-audits#detailed-reports) to analyze keyword lists to see which keywords trigger most matches. You can investigate further to see if those keywords have high false-positive rates. You can also use the [Message details reports](communication-compliance-reports-audits#export-a-message-details-report) to get data on keyword matches for a specific policy.

## Use Microsoft Purview Reports and the data explorers

It's important to understand the volume of items classified by Microsoft provided trainable classifiers and sensitive information types. [Microsoft Purview Reports](purview-reports) is the primary tool you should use. You can also use these tools to help you understand the volume that you can expect for your organization.

- [Get started with content explorer (classic)](data-classification-content-explorer)
- [Get started with data explorer](data-classification-data-explorer)
- [Get started with activity explorer](data-classification-activity-explorer)

When you first start using Microsoft provided trainable classifiers, you might not get enough matches, or you might get too many matches. The following table shows the volume level to expect for different types of Microsoft provided trainable classifiers.

| Microsoft trainable classifier | Volume |
| --- | --- |
| Adult images | Low |
| Customer complaints | Medium |
| Discrimination | Low |
| Gifts & entertainment | Medium |
| Gory images | Medium |
| Money laundering | Medium |
| Profanity | Medium |
| Racy images | Medium |
| Regulatory collusion | Medium |
| Stock manipulation | Medium |
| Targeted harassment | Low |
| Threat | Low |
| Unauthorized disclosure | High |

Consider using the *Adult images* classifier instead of the *Racy images* classifier since the *Adult images* classifier detects a more explicit image. You can use the [Content explorer](data-classification-content-explorer) to help you understand the volume that you can expect for your organization for each of the Microsoft provided trainable classifiers.

## Filter email blasts

You can [filter out email messages](communication-compliance-policies#filter-email-blasts) that are generic and intended for mass communication. For example, you can filter out spam, newsletters, and similar messages. For more information, see [Learn about the Email blast senders report](communication-compliance-reports-audits#detailed-reports).

## Filter out email signatures and disclaimers

Sensitive information types can be triggered from footers in emails, such as disclaimers. If many of your nonactionable alerts come from a specific set of sentences or phrases in an email signature or disclaimer, you can [filter out the email signature or disclaimer](sit-common-scenarios#ignore-disclaimer-notices-when-configuring-sensitive-information-type-detection).

## Use sentiment evaluation

Messages in alerts include [sentiment evaluation](communication-compliance-investigate-remediate#examine-the-message-details) to help you quickly prioritize potentially riskier messages to address first. Using sentiment evaluation doesn't reduce your detection volumes but makes it easier to prioritize detections. Messages are flagged as *Positive*, *Negative*, or *Neutral* sentiment. For some organizations, messages with *Positive* sentiment might be a lower priority, allowing you to spend more time on other message alerts.

## Report messages as misclassified

[Reporting false positives as misclassified](communication-compliance-investigate-remediate#review-and-remediate-policy-matches-and-alerts) helps improve Microsoft’s models and reduces the number of false positives that you see in the future.

## Filter out specific senders by using a condition

If you have senders that consistently trigger detections, you can filter out these particular senders by using the following conditional setting:

- [Message isn't received from any of these domains](communication-compliance-policies#choose-conditions-for-your-policies).

Some examples of consistently triggering detections can occur through newsletters, automated mails, and so on. For more scenario information, see [Scenarios for creating conditions in Communication Compliance policies](communication-compliance-conditions-scenarios).

## Use communication direction to target a particular set of users

If you’re detecting standards of business conduct scenarios and only care about communications from your users (not from guests), consider using a policy that detects only [outbound communications](communication-compliance-policies#direction). If you make the entire organization in scope, you can ensure that all of the users in your organization are covered but exclude users from outside your organization.

## Combine trainable classifiers

Consider combining two or more [Microsoft provided trainable classifiers](trainable-classifiers-learn-about) together. For example, combine the [Threat](trainable-classifiers-definitions#threat) and [Profanity](trainable-classifiers-definitions#profanity) classifiers or the [Targeted harassment](trainable-classifiers-definitions#harassment) and [Profanity](trainable-classifiers-definitions#profanity) classifiers to raise the threshold for messages captured.

## Lower the percentage of reviewed communications

To sample a subset of all the messages that trigger alerts, [specify a percentage of communications to review](communication-compliance-policies#review-percentage).