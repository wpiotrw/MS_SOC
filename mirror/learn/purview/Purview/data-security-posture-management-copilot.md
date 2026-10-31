---
layout: Conceptual
title: Use Microsoft Security Copilot with Data Security Posture Management - (classic) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-posture-management-copilot
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use Microsoft Security Copilot with Data Security Posture Management (classic).
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2025-12-15T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-security-posture-management
ms.collection:
- purview-compliance
- data-security-posture-maangement
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
locale: en-us
document_id: 66d8b373-b3a0-d538-61db-897c689c6961
document_version_independent_id: 66d8b373-b3a0-d538-61db-897c689c6961
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-posture-management-copilot.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-posture-management-copilot
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-posture-management-copilot.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 0b791919-b3bb-35e5-c0e8-2dd7d20fe67c
---

# Use Microsoft Security Copilot with Data Security Posture Management - (classic) | Microsoft Learn

Note

This article is for the **classic** version of Data Security Posture Management, now replaced with a new version that expands coverage to more data sources, introduces guided workflows for proactive risk management, and streamlines data security operations so you can more confidently adopt AI across your digital estate.

These improvements won't be added to this classic version so we invite you to try the new [Data Security Posture Management](data-security-posture-management-learn-about).

Use Microsoft Security Copilot and Data Security Posture Management (DSPM) to quickly explore the details and get answers about unprotected sensitive data assets and potentially risky user activities in your organization. Data security insights come from scanned data across [Data Loss Prevention (DLP)](dlp-learn-about-dlp), [Information Protection](information-protection), and [Insider Risk Management](insider-risk-management) solutions in [Microsoft Purview](purview).

## Get started with Copilot

After you [configure DSPM](data-security-posture-management-get-started), [onboard your organization](data-security-posture-management-get-started#step-3-configure-security-copilot) to Security Copilot, and complete the automated scanning, use Security Copilot featured promptbooks and the new prompt gallery to help you get started. Promptbooks are a built-in sequence of prompts that help you quickly learn more about your data security posture. Choose from the following Security Copilot promptbooks or built-in prompts in the Copilot Prompt Gallery:

### Risky user investigation promptbook

This promptbook is a six-prompt sequence that helps you investigate users handling sensitive data and shows their data activities, anomalies, and related alerts. By providing the User Principal Name (UPN) for a user and a duration (in days), this promptbook automatically runs the following prompts in order:

1. Show all sensitive data activities performed by &lt;upn&gt; in the last &lt;duration&gt; days
2. Was &lt;upn&gt; involved in any potential sensitive data exfiltration (for example, email forwarding, external file sharing, USB transfers, cloud uploads) in the last &lt;duration&gt; days?
3. Summarize &lt;upn&gt;'s sensitive data interactions over the last &lt;duration&gt; days, highlighting the most accessed classifiers, labels, SharePoint sites, common upload domains, and primary email recipient domains and users.
4. Did &lt;upn&gt; exhibit unusual behavior or take uncommon actions like excessive access or downloads in the last &lt;duration&gt; days?
5. Are there any alerts associated with &lt;upn&gt; in the last &lt;duration&gt; days, and what is the user's current risk level?
6. What actions can be taken to prevent &lt;upn&gt; from leaking sensitive data? Include policies, data loss prevention controls, and access restriction strategies.

### Sensitive data protection promptbook

This promptbook is a sequence of six prompts that helps you identify and protect sensitive data across your organization. It suggests recommended policy changes and data loss prevention rules. By using the full name of the trainable classifier, sensitivity label, or sensitive information type (SIT) and a duration in days, this promptbook automatically runs the following prompts in order:

1. Where is data labeled as &lt;label\_or\_classifier\_or\_SIT&gt; stored?
2. Provide an overview of activities involving &lt;label\_or\_classifier\_or\_SIT&gt; data in the last &lt;duration&gt; days.
3. Identify instances where &lt;label\_or\_classifier\_or\_SIT&gt; data was transferred outside of the organization in the last &lt;duration&gt; days.
4. Who are the top five users with the most &lt;label\_or\_classifier\_or\_SIT&gt; data exfiltration in the last &lt;duration&gt; days?
5. Are there any alerts for users who interacted with &lt;label\_or\_classifier\_or\_SIT&gt; data in the last &lt;duration&gt; days?
6. How can I prevent unauthorized transfers of &lt;label\_or\_classifier\_or\_SIT&gt; data?

To get started with Security Copilot promptbooks, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned DSPM permissions.
2. Select the **Data Security Posture Management (classic)** solution card, then select **Overview** in the left nav.
3. Select one of the suggested prompts for Security Copilot:

    - Risky user investigation promptbook
    - Sensitive data protection promptbook
4. Enter the requested inputs for the user, classifier, sensitivity label, or SIT and duration in days.
5. Select **Submit**.

The promptbook responses automatically scope insight data and provide quick answers in a separate flyout pane. You can select additional built-in prompts to automatically update and generate new responses in the flyout pane. Select **New chat** to clear previous responses to suggested prompts. Create additional custom prompts directly in Copilot to generate responses from AI-driven analytics based on the scanning results from your organization.

### Copilot prompt gallery

Data Security Posture Management also offers built-in prompts to help you investigate sensitive areas, potentially risky users, potentially suspicious activity, and more in your organization. To view these built-in Copilot prompts, select **View more in prompt gallery** in the **Get started with Security Copilot featured promptbooks** section on the **Overview** page. You can customize the built-in prompt or immediately run the prompt directly in Copilot.

Select built-in Copilot prompts from the following categories:

- Alerts and policies
- Data at risk
- Potentially risky users
- Potentially suspicious activity
- Sensitive data

## Tips for custom Copilot prompts in DSPM

For an enhanced experience with Security Copilot in Data Security Posture Management, use the following tips for higher accuracy for your Copilot responses:

- Always include the user's UPN for questions involving a specific user.
- Always specify the complete name for the sensitive info type or label for questions that involve a specific type of sensitive info type or label.
- Clearly list the sorting criteria for questions for top users, activities, and alerts.
- Always specify the date period for questions for data in a specific date period. If you don't specify a date period, only data from the last 10 days from current date is included. The maximum lookback is 30 days from the current date.
- Put all items (classifiers or labels) in single quotes in your prompt.
- Use "/" as a separator for any path (for example, a file path) in a user prompt.
- Scope the prompt to a single intent for higher accuracy of responses. Break complex prompts into single intent questions and enter the prompts one by one.
- Make questions self-contained. Avoid referring to previous questions or responses.
- Avoid using generic terms.
- Support prompts for data security across Information Protection, DLP, Insider Risk Management, or from public documentation.

For more information about creating Security Copilot prompts, see [Create effective prompts](/en-us/copilot/security/prompting-tips).

## Using Copilot in other solutions

Security Copilot is also available directly in other Purview solutions to help you quickly find answers for specific scenarios or to generate insights scoped to specific solution areas that aren't related to unprotected assets.

- [Using Copilot to summarize an alert in Insider Risk Management](insider-risk-management-activities#use-copilot-to-summarize-an-alert)
- [Use Copilot to summarize user activities in Insider Risk Management](insider-risk-management-users#use-copilot-to-summarize-user-activities-preview)