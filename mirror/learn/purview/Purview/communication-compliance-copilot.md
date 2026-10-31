---
layout: Conceptual
title: Configure a Communication Compliance policy to detect generative AI interactions | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/communication-compliance-copilot
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Set up a Communication Compliance policy to detect inappropriate or risky generative AI interactions, including prompts, responses, and potential confidential information sharing across supported apps.
keywords: Microsoft 365, Microsoft Purview, compliance, Communication Compliance, copilot
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
ms.update-cycle: 180-days
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-communication-compliance
ms.collection:
- highpri
- purview-compliance
- msec-ai-copilot
- highpri
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1014
search.appverid:
- MET150
- MOE150
ai-usage: ai-assisted
locale: en-us
document_id: 3b1309f5-c0bb-66e2-3c95-5531abb0a8eb
document_version_independent_id: 3b1309f5-c0bb-66e2-3c95-5531abb0a8eb
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/communication-compliance-copilot.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: communication-compliance-copilot
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/communication-compliance-copilot.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 9225fd72-7df9-7dbb-5c81-7e3cd7999ae2
---

# Configure a Communication Compliance policy to detect generative AI interactions | Microsoft Learn

Important

[Microsoft Purview Communication Compliance](communication-compliance) provides the tools to help organizations detect regulatory compliance (for example, SEC or FINRA) and business conduct violations such as sensitive or confidential information, harassing or threatening language, and sharing of adult content. Communication Compliance is built with privacy by design. Usernames are pseudonymized by default, role-based access controls are built in, investigators are opted in by an admin, and audit logs are in place to help ensure user-level privacy.

## Overview

You can use Communication Compliance to analyze interactions (prompts and responses) to detect inappropriate or risky interactions or sharing of confidential information entered into numerous generative AI applications.

These applications include [Microsoft 365 Copilot](/en-us/copilot/microsoft-365/), Copilots built with [Microsoft Copilot Studio](/en-us/microsoft-copilot-studio/), AI applications connected by [Microsoft Entra](/en-us/entra/fundamentals/what-is-entra) or [Microsoft Purview Data Map](data-map) connectors, and more.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Microsoft Copilot experience

Important

To detect inappropriate or risky interactions for non-Microsoft 365 AI data, you must enable [pay-as-you-go billing](/en-us/purview/purview-billing-models) in your organization. Non-Microsoft 365 AI data includes information from other generative AI applications from Microsoft and connected external AI applications. Examples of non-Microsoft 365 AI data include [Copilot in Microsoft Fabric](/en-us/fabric/fundamentals/copilot-fabric-overview), [Microsoft Security Copilot](/en-us/copilot/security/microsoft-security-copilot), [Microsoft Copilot Studio](/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio), and any connected or cloud AI application. There are no pay-as-you-go billing requirements or charges for Microsoft 365 detecting inappropriate or risky interactions for Microsoft 365 Copilot data.

Communication Compliance can detect interactions in any message with the IPM.SkypeTeams.Message.Copilot.*application* item class. These item classes include Copilot applications in Microsoft solutions like Teams, Outlook, and many more.

For example, Communication Compliance detects interactions in Copilot messages with the IPM.SkypeTeams.Message.Copilot.Teams, IPM.SkypeTeams.Message.Copilot.Outlook item classes, and others.

## Connected generative AI application

Important

To detect inappropriate or risky interactions for connected generative AI applications, you must enable [pay-as-you-go billing](/en-us/purview/purview-billing-models) in your organization.

Communication Compliance can detect prompt and response interactions with non-Copilot AI applications. These applications are generative AI applications connected by using [Microsoft Entra](/en-us/entra/fundamentals/what-is-entra) and [Microsoft Purview Data Map](data-map) connectors.

## Other AI applications

Important

To detect inappropriate or risky interactions for other AI applications, your organization must enable [pay-as-you-go billing](/en-us/purview/purview-billing-models).

Communication Compliance can also detect interactions with AI applications from browser and network activity by users in your organization. This capability helps you detect inappropriate or risky interactions or sharing of confidential information that users enter into AI applications outside of your organization.

## Prerequisites

To investigate Copilot interactions in Communication Compliance, you must be assigned one of the following roles:

- *Communication Compliance*
- *Communication Compliance Investigators*
- *Communication Compliance Analysts*

You must also be assigned as a [reviewer in the Reviewers field when creating a communication compliance policy](communication-compliance-configure#step-5-required-create-a-communication-compliance-policy).

## How it works

Important

Microsoft is committed to making sure artificial intelligence (AI) systems are developed responsibly and in ways that warrant people's trust. As part of this commitment, Microsoft Purview engineering teams operationalize the six core principles of [Microsoft's Responsible AI](https://www.microsoft.com/ai/our-approach) strategy to design, build, and manage AI solutions. To responsibly deploy AI, we provide documentation, role-based access, scenario attestation, and more to help organizations use AI systems responsibly.

You can take advantage of all Communication Compliance features when you create a Communication Compliance policy that detects Microsoft 365 Copilot and Microsoft 365 Copilot Chat interactions, including:

- [Sensitive information types](communication-compliance-policies#sensitive-information-types)
- [Keywords](communication-compliance-policies#custom-keyword-dictionaries)
- [Microsoft provided trainable classifiers](communication-compliance-policies#microsoft-provided-trainable-classifiers)
- [Content safety classifiers for Teams based on large language models](communication-compliance-policies#content-safety-classifiers-based-on-large-language-models)
- [Conditions](communication-compliance-policies#choose-conditions-for-your-policies)

Any prompt or response that a user enters into a supported generative AI app and that matches a Communication Compliance policy appears as a [policy match](communication-compliance-investigate-remediate) on the **Policies** page on the **Pending** tab, with separate entries for prompts and responses. If only the prompt or only the response matches a policy, the **Pending** tab shows an item just for that policy match. You can remediate policy matches for generative AI apps in the same way that you remediate any other policy match.

The following information appears for each item on the **Pending** tab for AI policy matches:

- **Icons**: The Copilot icon identifies the policy match as a generative AI interaction with a Microsoft-based Copilot For all other generative AI interactions, this icon is an email icon.
- **Subject column**: The *[Copilot]* value in this column identifies the policy match as a generative AI interaction with Microsoft-based Copilots. The *[AI app]* value in this column identifies the policy match for all other generative AI interactions.
- **Sender column**: Sender of the message. Depending on the source AI application, the sender appears as follows:
    - If the policy match is a response from a Copilot application, the value is *Copilot*.
    - If the policy match is a response from a connected AI application, the value is *Connected AI app*.
    - If the policy match is a response from a cloud AI application, the value is *Cloud AI app*.
- **Recipient column**: Recipients included in the message. This value is the user interacting with the AI application.
- **Message text**: The message text that the user entered (the text that caused the policy match) appears on the right side of the screen in its entirety.

## Create a policy that detects Microsoft Copilot interactions

Follow these steps to create a policy that detects Microsoft Copilot interactions:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Communication Compliance** solution.
3. Select **Policies** in the left navigation.
4. Select **Create policy**, then select the **Detect Microsoft Copilot interactions** template.
5. Enter the policy name, select the users and groups to apply the policy to, and select the reviewers for the policy. [Learn more about these options when creating a policy from a template](communication-compliance-configure#create-a-policy-from-a-template)
6. Review the list of settings chosen for you based on the template. Select **Create policy** to create the policy or select **Customize policy** if you want to make any changes before creating the policy.

## Add a generative AI app as a location for an existing policy

Follow these steps to add a generative AI app as a location for an existing Communication Compliance policy:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Communication Compliance** solution.
3. Select **Policies** in the left navigation.
4. Select **More actions** (ellipsis) in the row for the policy you want to change, then select **Edit**.
5. Select **Next** two times in the policy creation workflow to go to the **Choose locations to detect communications** page.
6. Select one or more of the following checkboxes to add a generative AI application as a location:

    - **Microsoft Copilot experiences**
    - **Enterprise AI apps**
    - **Other AI apps**
7. Make any other changes to the policy, then on the **Review and finish** page, select **Save**.

## Create a policy to review all generative AI interactions

When you first work with generative AI interactions, consider reviewing all AI interactions to understand how people in your organization use these applications. To create a policy that reviews all generative AI interactions, when you create or edit the policy:

- Set the location to include all generative AI applications:

    - **Microsoft Copilot experiences**
    - **Enterprise AI apps**
    - **Other AI apps**
- Set the **Review percentage** option on the **Choose conditions and review percentage** page to 100%.
- Don't set any conditions for the policy.

Note

Depending on the size of your organization, a policy that detects all generative AI interactions might result in a high volume of detected messages. This volume could cause your organization to reach its [storage limit](communication-compliance-policies#storage-limit-notification). If your organization reaches its storage limit, adjust the policy to reduce the number of detections.

## Remediate policy matches and alerts that contain generative AI interactions

Remediate policy matches and alerts that contain generative AI interactions the same way you remediate any policy match or alert in Communication Compliance. For example, you can tag a policy match, escalate it, resolve it, download it, or export it. [Learn more about resolving policy matches and alerts in Communication Compliance](communication-compliance-investigate-remediate#review-and-remediate-policy-matches-and-alerts).

## Reports

AI interactions that you bring into the scope of a Communication Compliance policy appear in Communication Compliance reports and audit data. [Learn more about Communication Compliance reports and audits](communication-compliance-reports-audits).