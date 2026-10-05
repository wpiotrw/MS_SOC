---
layout: Conceptual
title: Microsoft Purview DLP for Microsoft 365 Copilot and Cowork | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-09-30T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1013
ms.update-cycle: 180-days
audience: ITPro
ms.topic: article
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
- highpri
- msec-ai-copilot
search.appverid:
- MET150
description: Learn how Microsoft Purview DLP protects Microsoft 365 Copilot, Copilot Chat, and Cowork by blocking sensitive prompts, web search, and labeled content.
locale: en-us
document_id: 5cbec236-bc0a-5145-ede6-91c929379ea8
document_version_independent_id: 5cbec236-bc0a-5145-ede6-91c929379ea8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-microsoft365-copilot-location-learn-about.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-microsoft365-copilot-location-learn-about
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-microsoft365-copilot-location-learn-about.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0fc65d4-7c73-4029-a261-7f99ff744363
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b2daec57-5914-4967-8ed3-1d444897ba59
platformId: f01964fa-3fed-e996-89bb-a6c29cdc5ab1
---

# Microsoft Purview DLP for Microsoft 365 Copilot and Cowork | Microsoft Learn

Microsoft Purview Data Loss Prevention (DLP) can help you protect interactions with Microsoft 365 Copilot, Copilot Chat, and Cowork in the following ways:

- **Restrict Microsoft 365 Copilot, Copilot Chat, and Cowork from using external web search when prompts contain sensitive data.** You can use DLP policies to prevent these Copilot experiences from sending sensitive information to external web services. When a prompt contains sensitive information types (SITs)—such as credit card numbers, passport numbers, Social Security numbers, or custom SITs defined by your organization—these experiences automatically block the use of external web search as a grounding source for that prompt. Instead, they continue to generate responses using permitted internal Microsoft 365 data sources. This prevents prompt text that matches the configured SITs from being sent to external search providers for that request.
- **Restrict Microsoft 365 Copilot, Copilot Chat, and Cowork from processing sensitive prompts.** You can create a DLP policy to help protect against the use of sensitive information types (SITs), such as credit card numbers, passport numbers, or Social Security numbers in prompts submitted in these Copilot experiences. This includes Microsoft-provided SITs and custom SITs that you create. This real-time control helps organizations reduce data leakage and oversharing risks. It prevents these experiences from returning a response when prompts contain sensitive data and from using that sensitive data for both internal and external web searches.
- **Restrict Microsoft 365 Copilot, Copilot Chat, and Cowork from processing sensitive files and emails.** You can create a DLP policy to prevent these Copilot experiences from using files and emails that have sensitivity labels when generating responses.
- **Restrict Microsoft 365 Copilot and Copilot Chat from processing external email (preview).** You can prevent Microsoft 365 Copilot and Copilot Chat from using emails sent from external domains as grounding data for responses. When this control is enabled, Copilot excludes external emails received by users from being referenced or summarized during prompt processing, while continuing to use internal Microsoft 365 data sources where permitted. This protection helps organizations reduce the risk of prompt injection and untrusted data influence. Copilot responses are grounded only in content from trusted internal sources.

Important

You can't use both content contains sensitive info types and content contains sensitivity labels conditions in the same rule. You can create a rule for each condition in the same policy, but not in the same rule.

## Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

## Permissions

Accounts with one of the following roles or role groups can create or edit a DLP policy for the Microsoft 365 Copilot and Copilot Chat location:

- **Microsoft Entra AI Admin** - Role for managing all aspects of Microsoft 365 Copilot and AI-related enterprise services in Microsoft 365.
- **Purview Data Security AI Admin** - Role for editing Data Loss Prevention policies related to Copilot and viewing AI content in Data Security Posture Management. This role doesn't have access to read prompts and responses of AI interactions.
- **Purview Data Security AI Admins** - Use this group to assign editing capabilities for Data Loss Prevention policies related to Copilot and viewing AI content in Data Security Posture Management. Review the role description for access details. It contains the Data Security AI Admin role.
- **Purview Compliance Administrator**
- **Purview Compliance Data Administrator**
- **Purview Information Protection**
- **Purview Information Protection Admin**
- **Purview Security Administrator**
- **Microsoft Entra Global Admin** - Role for managing all aspects of Microsoft Entra ID and Microsoft services that use Microsoft Entra identities.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## Block sensitive information types in web search

To prevent Microsoft 365 Copilot, Copilot Chat, and Cowork from sending sensitive data to external web search providers when grounding responses:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Go to **Data Loss Prevention** &gt; **Policies** and select **+ Create policy**.
3. Select the **Custom** template, then **Custom policy**.
4. On the **Locations** page, set the **Microsoft 365 Copilot and Copilot Chat** location to on.
5. Add a rule with the **Content contains** &gt; **Sensitive information types** condition and choose the SITs you want to detect.
6. In the same rule, set the action to **Prevent Copilot from processing content** &gt; **Performing Web Searches**.
7. Save and turn on the policy.

When a user prompt contains the configured SITs, Copilot and Cowork block external web search as a grounding source and continue to generate the response using allowed internal Microsoft 365 data sources.

### Block SITs in web search use case example

*Contoso wants employees to use Microsoft 365 Copilot for productivity, but doesn't want sensitive customer data sent to external web search providers when Copilot grounds responses on the web.*

To meet this business need, Contoso configures a DLP policy as follows:

1. Targets the **Microsoft 365 Copilot and Copilot Chat** policy location.
2. Adds a rule with the **Content contains** &gt; **Sensitive information types** condition that detects the SITs representing sensitive customer data.
3. Sets the rule action to **Prevent Copilot from processing content** &gt; **Performing Web Searches**.

When a user submits a prompt containing those SITs, Copilot doesn't send the prompt to external web search providers. Copilot still returns a response grounded in internal Microsoft 365 data sources where the user has access.

## Block sensitive information types in prompts

This feature is in preview and is rolling out to all tenants with access to Microsoft 365 Copilot and Copilot Chat. Check whether rollout has reached your tenant. It's available in Microsoft 365 Copilot, Copilot Chat, Cowork, and Copilot in Word, Excel, and PowerPoint.

To set this up, create DLP policies that use the **Microsoft 365 Copilot and Copilot Chat** policy location with the **Content contains** &gt; **Sensitive information types** condition. This policy prevents Copilot and Cowork from returning a response when prompts contain sensitive data. Only out-of-the-box and custom SITs are currently supported.

Tip

During preview, the user messaging in Word, Excel, PowerPoint might not clearly state that the interaction with Copilot in those products is blocked due to an organizational policy. The sensitive prompt is still restricted, and Copilot won't provide a response.

### Block SITs in prompts use case example

*Contoso encourages their employees to use Microsoft 365 Copilot to enhance productivity, but they don't want their users placing Canada physical addresses or EU debit card numbers into prompts.*

To meet this business need, Contoso creates a DLP policy that targets the Microsoft 365 Copilot and Copilot Chat location and has a rule that uses the **Content contains** &gt; **Sensitive information types** &gt; **Canada physical addresses** or **EU debit card numbers** condition to identify prompts that contain those SITs. The actions in the rule are configured to **Restrict Copilot from processing content** &gt; **Processing prompts**.

When a user attempts to submit a prompt that contains either of these sensitive information types, they receive a message indicating that the request can't be completed because it contains sensitive information that the organization has blocked Microsoft 365 Copilot from using.

## Block files and emails with sensitivity labels from being processed

This feature is available in Microsoft 365 Copilot, Copilot Chat, Cowork, and Copilot in Word, Excel, and PowerPoint.

To set this up, create DLP policies that use the **Microsoft 365 Copilot and Copilot Chat** policy location with the **Content contains** &gt; **Sensitivity labels** condition to exclude items from being processed. Identified items still appear in the citations of the response, but Copilot and Cowork don't access or use the content of the item in the response.

### Block items with sensitivity labels example use case

Contoso establishes and applies a sensitivity label taxonomy to their data. The taxonomy includes these labels:

- **Highly Confidential**
- **Confidential**
- **Internal**
- **Public**
- **Personal**

They deploy Microsoft 365 Copilot and Copilot Chat to help users find and use Contoso enterprise information in their organization. They want to minimize the risk of General Data Protection Regulation (GDPR) data being included in Microsoft 365 Copilot and Copilot Chat summaries and also exclude private information from summaries. They create a DLP policy that uses the **Microsoft 365 Copilot and Copilot Chat** policy location with the **Content contains** &gt; **Sensitivity labels** condition to exclude items that have the **Personal** sensitivity label from being processed in the response summary and also to exclude items that have the **Highly Confidential** sensitivity label from being processed in the response summary.

### Coverage of email and file content

The DLP for **Microsoft 365 Copilot and Copilot Chat** policy location supports specific content that Copilot processes across various experiences.

Microsoft 365 Copilot and Copilot Chat rule configured to protect items with sensitivity labels supports:

- File items, which are stored and items that are actively open. For more information on supported file types, see: [file types supported by sensitivity labels](sensitivity-labels-sharepoint-onedrive-files).
- Emails sent on or after January 1, 2025.
- Calendar invites aren't supported.

Note

When a file is open in Word, Excel, or PowerPoint and has a sensitivity label for which DLP policy is configured to prevent processing by Microsoft 365 Copilot and Copilot Chat, the skills in these apps are disabled. Certain experiences that don't reference file content or that aren't using any large language models aren't currently blocked on the user experience.

## Block external email from being processed (preview)

This feature is in preview. It applies to Microsoft 365 Copilot and Copilot Chat, including email summarization and reasoning experiences that use email data.

To set this up, create DLP policies that use the **Microsoft 365 Copilot and Copilot Chat** policy location with the **Email is received from** &gt; **External users** condition. When the policy detects that an email was received from a sender outside your organization's accepted domains, Copilot excludes that email from grounding, summarization, and citation. Copilot continues to use internal Microsoft 365 data sources where permitted, and the user's access to the email itself isn't affected.

The policy evaluates email metadata only - specifically, the sender domain compared against your tenant's accepted domains. The body of the email isn't inspected.

### Block external email use case example

*Contoso wants employees to keep using Microsoft 365 Copilot for productivity, but is concerned that external email could carry untrusted instructions or prompt-injection content. They want Copilot to ground responses only in trusted internal data.*

To meet this need, Contoso creates a DLP policy that targets the Microsoft 365 Copilot and Copilot Chat location with a rule that uses the **Email is received from** &gt; **External users** condition. The action is configured to **Prevent Copilot from processing content**.

When a user prompts Copilot to summarize their inbox or reason over recent email, external emails are excluded from grounding. Copilot returns a response based on internal email and other permitted Microsoft 365 sources, and the user sees a message that some content was excluded by an organizational policy.

## Files uploaded in prompts

You can upload files when you craft a prompt for Microsoft 365 Copilot to analyze. DLP can't scan the contents of files that you upload directly into prompts, so evaluation of the uploaded file for sensitive data doesn't occur. DLP only checks the text you type into the prompt itself.

## Availability

- The **Microsoft 365 Copilot and Copilot Chat** policy location is only available in the **Custom** policy template.
- When you select the **Microsoft 365 Copilot and Copilot Chat** policy location, all other locations for that policy are disabled.
- DLP alerts, DLP notifications, and policy simulation mode are supported.
- Updates to a DLP policy can take up to four hours to reflect in Microsoft 365 Copilot and Copilot Chat experience.

## Admin units

The **Microsoft 365 Copilot and Copilot Chat** policy location doesn't support **Admin units**.

## Supported conditions and actions

The **Microsoft 365 Copilot and Copilot Chat** policy location supports the following conditions and actions:

| Conditions | Supported policy actions | Description |
| --- | --- | --- |
| **Content contains** &gt; **Sensitivity labels** | **Prevent Copilot from processing content** | Detects when a file or an email in Exchange has a chosen sensitivity label. Copilot and Cowork don't process the content of the item or use it in the response summary, but the item could be available in the citations of the response. |
| **Content contains** &gt; **Sensitive information types** | **Prevent Copilot from processing content** &gt; **Processing prompts** | Detects when the text entered directly into a Copilot or Cowork prompt contains chosen sensitive information types. The experience doesn't respond to the prompt. The prompt isn't used for internal or web searches. |
| **Content contains** &gt; **Sensitive information types** | **Prevent Copilot from processing content** &gt; **Performing Web Searches** | Detects when the text entered directly into a Copilot or Cowork prompt contains chosen sensitive information types. The experience blocks the use of external web search as a grounding source for that prompt. |
| **Email is received from** &gt; **External users** | **Prevent Copilot from processing content** | Detects when an email was received from a sender outside your organization's accepted domains. The external email is excluded from being used by Copilot for grounding, summarization, or citation. Email body content isn't inspected; only sender metadata is evaluated. |

Note

All Microsoft 365 Copilot prompts run in the security context of the user who initiates the prompt. This means for a user to see an item in a prompt response, they must first have the necessary permissions to access the content of the item. You can then use the **Microsoft 365 Copilot and Copilot Chat** policy location feature to exclude items from being processed in the response summary.

In Word, Excel, and PowerPoint the **Microsoft 365 Copilot and Copilot Chat** policy to prevent Copilot from processing content is evaluated at file open. If a sensitivity label is applied mid-session, the policy will be enforced starting the next time the file is opened.