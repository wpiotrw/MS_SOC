---
layout: Conceptual
title: Learn about Communication Compliance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/communication-compliance
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about Communication Compliance in Microsoft Purview
keywords: Microsoft 365, Microsoft Purview, compliance, Communication Compliance
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-02-27T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-communication-compliance
ms.collection:
- highpri
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- highpri
- microsoft-365-copilot
search.appverid:
- MET150
- MOE150
ms.custom: sfi-ga-nochange
locale: en-us
document_id: 6e017f34-a8bb-7e67-0fb0-2cbc1bf69db8
document_version_independent_id: 6e017f34-a8bb-7e67-0fb0-2cbc1bf69db8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/communication-compliance.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: communication-compliance
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/communication-compliance.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 3b267306-1858-0482-4f05-e4a8b23fcb95
---

# Learn about Communication Compliance | Microsoft Learn

Important

[Microsoft Purview Communication Compliance](communication-compliance) provides the tools to help organizations detect regulatory compliance (for example, SEC or FINRA) and business conduct violations such as sensitive or confidential information, harassing or threatening language, and sharing of adult content. Communication Compliance is built with privacy by design. Usernames are pseudonymized by default, role-based access controls are built in, investigators are opted in by an admin, and audit logs are in place to help ensure user-level privacy.

Microsoft Purview Communication Compliance is an insider risk solution that helps you minimize communication risks by helping you detect, capture, and act on potentially inappropriate messages in your organization. Predefined and custom policies allow you to check internal and external communications for policy matches so designated reviewers can examine them. Reviewers can investigate email, Microsoft Teams, Microsoft 365 Copilot and Microsoft 365 Copilot Chat, Viva Engage, or third-party communications in your organization and take appropriate actions to make sure they're compliant with your organization's message standards.

Communication Compliance policies in Microsoft 365 help you overcome many modern challenges associated with compliance and internal and external communications, including:

- Checking increasing types of communication channels
- The increasing volume of message data
- Regulatory enforcement and the risk of fines

Additionally, there might be a separation of duties between your IT admins and your compliance management team. Communication Compliance supports the separation between configuration of policies and the investigation and review of messages. For example, the IT group for your organization might be responsible for setting up Communication Compliance role permissions, groups, and policies. Investigators and reviewers might be responsible for message triage, review, and mitigation actions.

For more information and an overview of the planning process to address compliance and risky activities in your organization, see [Starting an Insider Risk Management program](https://download.microsoft.com/download/b/2/0/b208282a-2482-4986-ba07-15a9b9286df0/pwc-starting-an-insider-risk-management-program-with-pwc-and-microsoft.pdf).

Watch the following video to learn how to fulfill regulatory compliance requirements with Communication Compliance: 

Important

Communication Compliance is currently available in tenants hosted in geographical regions and countries supported by Azure service dependencies. To verify that Communication Compliance is supported for your organization, see [Azure dependency availability by country/region](/en-us/troubleshoot/azure/general/dependency-availability-by-country).

## Scenarios for Communication Compliance

Communication Compliance policies can help you review messages in your organization for several important compliance areas:

- **Corporate policies**

    Users must comply with acceptable use, ethical standards, and other corporate policies in all their business-related communications. Communication Compliance policies can detect policy matches and help you take corrective actions to help mitigate these types of incidents. For example, you can check user communications in your organization for human resources concerns such as harassment or the use of potentially inappropriate or offensive language.
- **Risk management**

    Organizations are responsible for all communications distributed throughout their infrastructure and corporate network systems. By using Communication Compliance policies to help identify and manage potential legal exposure and risk, you can minimize risks before they damage corporate operations. For example, you can check messages in your organization for unauthorized communications and conflicts of interest about confidential projects such as upcoming acquisitions, mergers, earnings disclosures, reorganizations, or leadership team changes.
- **Regulatory compliance**

    Most organizations must comply with some type of regulatory compliance standards as part of their normal operating procedures. These regulations often require organizations to implement some type of scoping or oversight process for messaging that is appropriate for their industry. The Financial Industry Regulatory Authority (FINRA) Rule 3110 is a good example of a requirement for organizations to have scoping procedures in place to check user communications and the types of businesses in which it engages. Another example might be a need to review broker-dealer communications in your organization to safeguard against potential insider trading, collusion, or bribery activities. Communication Compliance policies can help your organization meet these requirements by providing a process to both analyze and report on corporate communications. For more information on support for financial organizations, see [Key compliance and security considerations for US banking and capital markets](/en-us/microsoft-365/solutions/financial-services-secure-collaboration).

## Key feature areas

Communication Compliance offers several important features to help address compliance concerns on your messaging platforms:

- Intelligent customizable templates
- Flexible remediation workflows
- Actionable insights

### Intelligent customizable templates

Intelligent customizable templates in Communication Compliance help you apply machine learning to detect communication violations in your organization.

- **Customizable pre-configured templates**: Policy templates help address the most common communications risks. You can create and update policies faster with predefined templates that analyze and mitigate potentially inappropriate content, sensitive information, conflict of interest, and regulatory compliance issues.
- **New machine learning support**: Built-in [classifiers](trainable-classifiers-get-started-with) analyze and mitigate discrimination, threats, harassment, profanity, and potentially inappropriate images. They help reduce misclassified content in communication messages, saving reviewers time during the investigation and remediation process.
- **Improved condition builder**: You can now configure policy conditions through a single, integrated experience in the policy workflow. This update reduces confusion about how conditions apply to policies.

### Flexible remediation workflows

Built-in remediation workflows help you quickly identify and take action on messages with policy matches in your organization. The following new features increase efficiency for investigation and remediation activities:

- **Flexible remediation workflow**: The new remediation workflow helps you quickly take action on policy matches. New options let you escalate messages to other reviewers and send email notifications to users with policy matches.
- **Conversation policy matching**: Messages in conversations group by policy matches to give you more visibility about how conversations relate to your communication policies. For example, conversation policy matching in the **Pending** tab automatically shows all messages in a Teams channel that match your communications policies for analyzing and mitigating potentially inappropriate messages. Other messages in conversations that don't match your communications policies don't display.
- **Keyword highlighting**: Terms that match policy conditions highlight in the message text view to help reviewers quickly analyze and remediate policy alerts.
- **Optical character recognition (OCR)**: You can check, detect, and investigate printed and handwritten text within images embedded or attached to email or Microsoft Teams chat messages.
- **New filters**: You can investigate and remediate policy alerts faster with message filters for several fields, including sender, recipient, date, domains, and many more.
- **Improved message views**: Investigation and remediation actions are now quicker with new message source and text views. You can now view message attachments to provide complete context when taking remediation actions.
- **User history**: A historical view of all user message remediation activities, such as past notifications and escalations for policy matches, now provides reviewers with more context during the remediation workflow process. First-time or repeat instances of policy matches for users are now archived and easily viewable.
- **Pattern detected notification**: Many harassing and bullying actions take place over time and involve recurring instances of the same behavior by a user. The pattern detected notification displayed in alert details helps raise attention to these alerts and this type of behavior.
- **Translation**: You can quickly investigate message details in eight languages using translate support in the remediation workflow. Messages in other languages automatically convert to the display language of the reviewer.
- **Attachment detection**: You can check, detect, and investigate linked content (Modern attachments) from OneDrive and Microsoft Teams that match policy classifiers and conditions for Microsoft Teams messages. Attachment content is automatically extracted to a text file for detailed review and action.
- **Summarize message content for policy matches**: Save time for investigators by [using Microsoft Copilot in Microsoft Purview](communication-compliance-investigate-remediate#summarize-a-message-by-using-copilot-in-microsoft-purview) to summarize lengthy Teams, email, or Viva Engage messages. Copilot in Microsoft Purview creates a summary of the conversation, including recordings, meeting transcripts, and attachments.

### Actionable insights

New interactive dashboards for alerts, policy matches, actions, and trends help you quickly view the status of pending and resolved alerts in your organization.

- **Proactive intelligent alerts**: Get alerts for policy matches that need immediate attention. New dashboards show pending items sorted by severity. Designated reviewers receive new automatic email notifications.
- **Interactive dashboards**: View new dashboards that display policy matches, pending and resolved actions, and trends by users and policy.
- **Auditing support**: Easily export a full log of policy and review activities from the Microsoft Purview portal to help support audit review requests.

## Integration with Microsoft 365 services

Communication Compliance policies check, detect, and capture messages across several communication channels to help you quickly review and remediate compliance issues:

- **Generative AI**: Use Communication Compliance policies to analyze interactions (prompts and responses) entered into generative AI applications to help detect inappropriate or risky interactions or sharing of confidential information. Coverage is supported for [Microsoft 365 Copilot](/en-us/copilot/microsoft-365/), Copilots built using [Microsoft Copilot Studio](/en-us/microsoft-copilot-studio/), AI applications connected by [Microsoft Entra](/en-us/entra/fundamentals/what-is-entra) or [Microsoft Purview Data Map](data-map) connectors, and more.
- **Microsoft Teams**: Communication Compliance supports chat communications for public and private [Microsoft Teams](/en-us/MicrosoftTeams/Teams-overview) channels and individual chats as a standalone channel source or with other Microsoft 365 services. You can also detect communications included in meetings transcripts (preview). You need to manually add individual users, distribution groups, or specific Microsoft Teams channels when you select users and groups to apply a Communication Compliance policy to. Teams users can also self-report potentially inappropriate messages in private and group channels and chats for review and remediation.
- **Exchange Online**: All mailboxes hosted on [Exchange Online](/en-us/Exchange/exchange-online) in your Microsoft 365 organization are eligible for analyses. Emails and attachments matching Communication Compliance policy conditions are instantly available for investigation and in compliance reports. Exchange Online is now an optional source channel and is no longer required in Communication Compliance policies.
- **Microsoft 365 Copilot and Microsoft 365 Copilot Chat**: Communication Compliance policies detect interactions (prompts and responses) entered by users into Copilot.
- **Viva Engage**: Communication Compliance policies support private messages and public community conversations in [Viva Engage](/en-us/viva/engage/overview). Viva Engage is an optional channel and must be in [native mode](/en-us/viva/engage/overview-native-mode) to support checking of messages and attachments.
- **Third-party sources**: You can check messages from [third-party sources](archive-third-party-data) for data imported into mailboxes in your Microsoft 365 organization. Communication Compliance supports connections to several popular platforms, including Instant Bloomberg and others.

To learn more about messaging channel support in Communication Compliance policies, see [Detect channel signals with Communication Compliance](communication-compliance-channels).

Watch the following video to learn how to detect communication risks in Microsoft Teams with Communication Compliance: 

## Integration with Microsoft Purview Insider Risk Management

When users experience employment stressors, they might engage in risky activities. Workplace stress can lead to uncharacteristic or malicious behavior by some users that surfaces as potentially inappropriate behavior on your organization's messaging systems. Counterproductive work behavior can be a precursor to more serious violations, such as sabotaging company assets or leaking sensitive information. By integrating Communication Compliance with [Microsoft Purview Insider Risk Management](insider-risk-management), you can detect stressors that indicate an unhealthy workplace environment.

[Learn more about integrating Communication Compliance with Insider Risk Management](communication-compliance-policies#integrate-communication-compliance-with-microsoft-purview-insider-risk-management)

## Get started with recommended actions

Whether you're setting up Communication Compliance for the first time or getting started with creating new policies, the new [recommended actions](communication-compliance-configure#recommended-actions) experience can help you get the most out of Communication Compliance capabilities. Recommended actions include setting up permissions, creating distribution groups, creating policies, and more.

## Workflow

Communication Compliance helps you address common pain points associated with complying with internal policies and regulatory compliance requirements. With focused policy templates and a flexible workflow, you can use actionable insights to quickly resolve detected compliance issues.

Before you create a policy, decide whether you want to apply an **adaptive scope**. For more information, see [Adaptive policy scopes for compliance solutions](purview-adaptive-scopes#advantages-of-using-adaptive-scopes). If you decide to create an adaptive policy, you must create one or more adaptive scopes before you create your policy, then select them during the create new policy process. For instructions, see [Configuration information for adaptive scopes](purview-adaptive-scopes#configure-adaptive-scopes).

Identifying and resolving compliance issues with Communication Compliance uses the following workflow:

![Communication Compliance workflow.](media/communication-compliance-workflow.png)

### Configure

In this workflow step, you identify your compliance requirements and configure applicable Communication Compliance policies. Policy templates are a great way to not only quickly configure a new compliance policy but also quickly modify and update policies as your requirements change. For example, you might want to quickly test a policy for potentially inappropriate content on communications for a small group of users before configuring a policy for all users in your organization.

Important

By default, Global Administrators don't have access to Communication Compliance features. To enable permissions for Communication Compliance features, see [Assign permissions in Communication Compliance](communication-compliance-permissions).

You can choose from the following policy templates in the Microsoft Purview portal:

- **Detect inappropriate text**: Use this template to quickly create a policy that uses built-in classifiers to automatically detect text in messages that might be considered inappropriate, abusive, or offensive.
- **Detect inappropriate images**: Use this template to quickly create a policy that uses built-in classifiers to automatically detect content that contains adult and racy images that might be considered inappropriate in your organization.
- **Detect sensitive info types**: Use this template to quickly create a policy to check communications containing defined sensitive information types or keywords to help make sure that important data isn't shared with people that shouldn't have access.
- **Detect financial regulatory compliance**: Use this template to quickly create a policy to check communications for references to standard financial terms associated with regulatory standards.
- **Detect conflict of interest**: Use this template to quickly create a policy to detect communications between two groups or two users to help avoid conflicts of interest.
- **Custom policy**: Use this template to configure specific communication channels, individual detection conditions, and the amount of content to detect and review in your organization.
- **User-reported messages policy**: This system policy supports user reported messages from channel, group, and private chat messages. Enabled by default in the Teams admin center.

Tip

Use [recommended actions](communication-compliance-configure#recommended-actions) to help you determine if you need a sensitive information type policy or if you need to update existing inappropriate content policies.

### Investigate

In this step, you can look deeper into the issues detected as matching your Communication Compliance policies. This step includes the following actions available in the Microsoft Purview portal:

- **Alerts**: When a group of messages matches a policy condition, an alert is automatically generated. For each alert, you can see the status, the severity, the time detected, and if an eDiscovery (Premium) case is assigned and its status. New alerts are displayed on the Communication Compliance home page and the **Alerts** page and are listed in order of severity.
- **Issue management**: For each alert, you can take investigative actions to help remediate the issue detected in the message.
- **Document review**: During the investigation of an issue, you can use several views of the message to help properly evaluate the detected issue. The views include a conversation summary, text-only, and detail views of the communication conversation.
- **Reviewing user activity history**: View the history of user message activities and remediation actions, such as past notifications and escalations, for policy matches.
- **Filters**: Use filters such as sender, recipient, date, and subject to quickly narrow down the message alerts that you want to review.

### Remediate

Remediate Communication Compliance issues you investigate by using the following options:

- **Resolve**: After reviewing an issue, resolve the alert. Resolving an alert removes it from the **Pending** tab. The action is preserved as an entry on the **Resolved** tab for the matching policy. Alerts are automatically resolved after you mark the alert as misclassified, send a notice to a user about the alert, or open a new case for the alert.
- **Tag a message**: As part of the resolution of an issue, tag a policy match as *Compliant*, *Non-compliant*, or *Questionable* as it relates to the policies and standards for your organization. You can also [create a custom tag](communication-compliance-investigate-remediate#create-a-custom-tag). Tagging can help you micro-filter policy alerts for escalations or as part of other internal review processes. You can filter on any tag value.
- **Notify the user**: Often, users accidentally or inadvertently violate a Communication Compliance policy. Use the notify feature to provide a warning notice to the user and to resolve the issue.
- **Escalate to another reviewer**: Sometimes, the initial reviewer of an issue needs input from other reviewers to help resolve the incident. You can easily escalate message issues to reviewers in other areas of your organization as part of the resolution process.
- **Report as misclassified**: Messages incorrectly detected as matches of compliance policies will occasionally slip through to the review process. Mark these types of alerts as misclassified to submit feedback to Microsoft about the misclassification to help improve global classifiers and automatically resolve the issue.
- **Remove message in Teams**: Potentially inappropriate messages can be removed from displaying in Microsoft Teams channels or personal and group chat messages. Those identified messages that are removed are replaced with a notification that the message has been removed for a policy violation.
- **Escalate for investigation**: In the most serious situations, you might need to share Communication Compliance information with other reviewers in your organization. Communication Compliance is tightly integrated with other Microsoft Purview features to help you with end-to-end risk resolution. Escalating a case for investigation allows you to transfer data and management of the case to Microsoft Purview eDiscovery (Premium). eDiscovery (Premium) provides an end-to-end workflow to preserve, collect, review, analyze, and export content that's responsive to your organization's internal and external investigations. It allows legal teams to manage the entire legal hold notification workflow. To learn more about eDiscovery (Premium) cases, see [Overview of Microsoft Purview eDiscovery (Premium)](ediscovery-overview).

### Maintain

Keeping track and mitigating compliance issues identified by Communication Compliance policies spans the entire workflow process. As alerts are generated and investigation and remediation actions are implemented, you might need to review and update existing policies or create new policies.

- **Review and report**: Use Communication Compliance dashboard widgets, export logs, and events recorded in the unified audit logs to continually evaluate and improve your compliance posture.
- **Get insights on policy health**: Communication Compliance provides warnings and recommendations to improve policy health. [Learn more about policy health](communication-compliance-policies#policy-health-preview)

## Ready to get started?

- For planning information, see [Plan for Communication Compliance](communication-compliance-plan).
- Check out the [case study for Contoso](communication-compliance-case-study) and see how they quickly configured a Communication Compliance policy to detect potentially inappropriate content in Microsoft Teams, Exchange Online, and Viva Engage communications.
- To configure Communication Compliance for your Microsoft 365 organization, see [Configure Communication Compliance](communication-compliance-configure).