---
layout: Conceptual
title: Communication Compliance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/communication-compliance-solution-overview
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to configure Communication Compliance in Microsoft Purview.
keywords: Microsoft 365, insider risk, compliance
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-communication-compliance
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2023-11-01T00:00:00.0000000Z
audience: itpro
ms.collection:
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- m365solution-scenario
- highpri
- microsoft-365-copilot
locale: en-us
document_id: 350686ad-2e96-a138-71c4-8822050aa9d2
document_version_independent_id: 350686ad-2e96-a138-71c4-8822050aa9d2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/communication-compliance-solution-overview.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: communication-compliance-solution-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/communication-compliance-solution-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/d6f38669-3d05-40f2-afd8-e49f7dd20884
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/55265cca-de9b-48dc-a77a-9047cc39a575
platformId: 9bb39a77-6c24-abf1-c770-625dbb0c01e4
---

# Communication Compliance | Microsoft Learn

Important

[Microsoft Purview Communication Compliance](communication-compliance) provides the tools to help organizations detect regulatory compliance (for example, SEC or FINRA) and business conduct violations such as sensitive or confidential information, harassing or threatening language, and sharing of adult content. Communication Compliance is built with privacy by design. Usernames are pseudonymized by default, role-based access controls are built in, investigators are opted in by an admin, and audit logs are in place to help ensure user-level privacy.

Protecting sensitive information and detecting and acting on workplace harassment incidents is an important part of compliance with internal policies and standards. Microsoft Purview Communication Compliance helps minimize these risks by helping you quickly detect, capture, and take remediation actions for email, Microsoft Teams communications, Microsoft 365 Copilot, and Microsoft 365 Copilot Chat interactions. These communications can include potentially inappropriate communications containing profanity, threats, and harassment and communications that share sensitive information inside and outside of your organization.

Microsoft Purview Communication Compliance is an insider risk solution that helps you detect, capture, and act on inappropriate messages that can lead to potential data security or compliance incidents within your organization. Communication Compliance evaluates text and image-based messages in Microsoft and third-party apps (Teams, Microsoft 365 Copilot and Microsoft 365 Copilot Chat, Viva Engage, Outlook, WhatsApp, and others) for potential business policy violations including inappropriate sharing of sensitive information, threatening or harassing language, and potential regulatory violations such as stock and capital manipulations.

Communication Compliance's mission is to foster safe and compliant communications across customers' enterprise communication channels. With role-based access controls, human investigators can take remediation actions such as removing a message from Teams or notifying senders of potentially inappropriate conduct.

## System capabilities

Important

Microsoft is committed to making sure artificial intelligence (AI) systems are developed responsibly and in ways that warrant people's trust. As part of this commitment, Microsoft Purview engineering teams are operationalizing the six core principles of [Microsoft's Responsible AI](https://www.microsoft.com/ai/our-approach) strategy to design, build, and manage AI solutions. As part of our effort to responsibly deploy AI, we provide documentation, role-based access, scenario attestation, and more to help organizations use AI systems responsibly.

Communication Compliance uses machine learning models and keyword matching to identify messages containing potential business conduct or regulatory policy violations that an investigator reviews. Communication Compliance cultivates user privacy with pseudonymization and responsible use of the product by providing role-based access controls.

Users get [permissions](communication-compliance-plan#configure-permissions) that allow them to perform the tasks in their role, such as:

- **Administrator role**: Administrators configure policies to detect specific patterns in an organization. Admins choose which machine learning classifiers to include in policies and can use the value of machine learning classifiers alongside keyword and phrase matching to meet organizational needs.
- **Investigator role**: Investigators view and remediate potentially risky messages flagged by built-in classifiers. Investigators have a range of actions they can take to address the displayed message and no automatic actions are taken without manual investigator review. Investigators can share feedback on messages misclassified by Microsoft classifiers via the *Report as Misclassified* action, which aims to continually improve classifier performance through customer submitted feedback.
- **Communication Compliance role**: Communication Compliance role can create policies for the organization and review policy matches for every policy.

## Intended uses of Communication Compliance

Important

Microsoft Purview Communication Compliance provides built-in machine learning tools for detecting messages that might violate regulatory, code of conduct, or organizational requirements. Users can choose built-in classifiers during policy configuration to evaluate organization communications. Admins can edit policy settings at any time according to organizational needs. Built with privacy by design, Microsoft doesn't receive any customer data or evaluations unless your organization's investigators explicitly consent to the *Report as Misclassified* action.

Communication Compliance empowers organizations to detect, triage, and remediate communications with potential business conduct and regulatory compliance violations. Communication Compliance provides the following policy templates that use machine learning classifiers for users:

- **Business conduct**: Discrimination, Profanity, Threat, and Targeted harassment classifiers
- **Regulatory compliance**: Corporate sabotage, customer complaints, gifts & entertainment, money laundering, regulatory collusion, stock manipulation, unauthorized disclosure classifiers

## Metrics used to evaluate and measure performance

Communication Compliance considers many metrics to holistically evaluate system accuracy and performance. False positive rates and true positive rates (also known as recall rates) from test data sets are two of the most important metrics that inform the classifier's performance. Quantitative metrics, such as the number of hits, and qualitative feedback from customers also help evaluate performance and improve the classifiers.

## Operational factors and settings

Operational factors and settings allow for effective and responsible use of the system. The following table details these factors and settings:

| Operational factor | Benefits |
| --- | --- |
| Role-based access control | - No individual has too much power to influence usage of Communication Compliance in the organization:  - Investigators can only view policies they have permission to view  - Administrators can only create and edit policies  - Communication Compliance role has the most widespread permissions to view and edit policies. |
| Using multiple conditions in a policy | You can fine-tune the value from machine learning classifiers with other capabilities such as key phrase matching, detection of sensitive information, or scoping to specific domains. |
| End user reporting of inappropriate content in Teams | Message recipients can report messages they find inappropriate or deem a data security incident as a proactive approach to identifying communication risks. |
| Keyword highlighting of messages caught by built-in classifiers | Investigators gain clarity on which key phrases trigger which classifiers. |
| Pseudonymization | Sender and recipient aliases are pseudonymized to minimize investigation bias. |
| Users choose which communication channels to detect for patterns in | Users can choose which channels, such as Microsoft Teams, Exchange, Viva Engage, or third-party sources, to identify and detect content patterns. |
| Feedback loop to report misclassified items | Items misclassified by machine learning classifiers can be reported to Microsoft to improve future performance of classifiers. User privacy is honored as per the [Microsoft Privacy Statement](https://privacy.microsoft.com/privacystatement). |

## Limitations of Communication Compliance

Every artificial intelligence solution has limitations. You can minimize the impact of these limitations when using Communication Compliance. The following table describes these limitations.

| Limitations | Impacted users | Ways to minimize impact |
| --- | --- | --- |
| False positive messages | Message senders | - Communications compliance uses a feedback loop to report misclassified items to continually improve classifier performance.  - Human reviewers must view message before action is taken. |
| False negative messages | Admins and message recipients | Machine learning classifiers can be combined with multiple conditions such as key phrase matching or user scoping to satisfy unique organizational needs. |
| Limited support for evasive typing and other adversarial inputs | Message recipients | Basic evasive typing coverage is provided to address swapping letters with numbers with improvements to come in future releases. |
| Not all languages covered | Message recipients | 12 languages supported today corresponding to highest usage regions. |

## Configure Communication Compliance

Use the following steps to configure Communication Compliance for your organization:

![Insider risk solution Communication Compliance steps.](media/ir-solution-cc-steps.png)

1. Learn about [Communication Compliance](communication-compliance)
2. Plan for [Communication Compliance](communication-compliance-plan) and [verify licensing](https://aka.ms/M365EnterprisePlans)
3. Configure [prerequisites](communication-compliance-configure#step-2-required-enable-the-audit-log) and [permissions](communication-compliance-permissions)
4. Create and configure [Communication Compliance policies](communication-compliance-configure#step-5-required-create-a-communication-compliance-policy)

## More information about Communication Compliance

- [Investigate and remediate alerts](communication-compliance-investigate-remediate)
- [Case study: Contoso quickly configures an inappropriate content policy for Microsoft Teams, Exchange, and Viva Engage communications](communication-compliance-case-study)