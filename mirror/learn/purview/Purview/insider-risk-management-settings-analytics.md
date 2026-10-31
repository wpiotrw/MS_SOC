---
layout: Conceptual
title: Enable analytics in Insider Risk Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-analytics
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about turning on the Analytics setting for Microsoft Purview Insider Risk Management to conduct an evaluation of potential insider risks and to get real-time analytics for indicator thresholds.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: how-to
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: itpro
ms.collection:
- highpri
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- highpri
ms.custom: msecd-doc-authoring-1014, admindeeplinkCOMPLIANCE, sfi-ga-nochange
ai-usage: ai-assisted
locale: en-us
document_id: 31343a23-a74e-4615-cde9-742bc7693fc2
document_version_independent_id: 31343a23-a74e-4615-cde9-742bc7693fc2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-settings-analytics.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-settings-analytics
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-settings-analytics.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/0e857f04-a3df-4ca1-a2b1-974e863ca385
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1ded9ced-b14e-446b-ab28-ea44c4e7ee3a
platformId: 3979c694-d9c7-815e-98f2-c553bd859397
---

# Enable analytics in Insider Risk Management | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

When you enable Microsoft Purview Insider Risk Management analytics, you get several important benefits. You can:

- Evaluate potential insider risks in your organization without configuring any insider risk policies.
- Get real-time guidance on configuring indicator threshold settings.
- Generate insider risk severity and user activity summary for the users not part of policies. Share this summary information with Data Loss Prevention, Communication Compliance, and Microsoft Defender.

## Evaluate insider risks in your organization

Microsoft Purview Insider Risk Management analytics enables you to evaluate potential insider risks in your organization without configuring any insider risk policies. This evaluation can help your organization identify potential areas of higher user risk and help determine what types of Insider Risk Management policies to configure and how broadly to scope them. Analytics scans offer the following advantages for your organization:

- **Easy to configure**: Select **Run scan** when prompted by the analytics recommendation or go to **Insider risk settings** &gt; **Analytics** and enable analytics.
- **Privacy by design**: Scanned results and insights are returned as aggregated and anonymized user activity. Reviewers can't identify individual usernames. Since Insider Risk Management doesn't classify any identity in the organization for analytics, the solution accounts for all the UPNs/identities that might be involved in data leaving the organization boundary. Accounting for all relevant identities might involve user accounts, system accounts, guest accounts, and non-person accounts.
- **Understand potential risks through consolidated insights**: Scan results help you quickly identify potential risk areas for your users and which policy best helps mitigate these risks.

To learn how analytics can help accelerate the identification of potential insider risks, see the [Insider Risk Management Analytics video](https://www.youtube.com/watch?v=5c0P5MCXNXk).

## Areas scanned

Analytics scans several sources for risk management activity to help you identify insights into potential areas of risk. Depending on your current configuration, analytics looks for qualifying risk activities in the following areas:

- **Microsoft 365 audit logs**: Included in all scans, this primary source helps you identify most of the potentially risky activities.
- **Exchange Online**: Included in all scans, Exchange Online activity helps you identify activities where data in attachments are emailed to external contacts or services.
- **Microsoft Entra ID**: Included in all scans, Microsoft Entra history helps you identify risky activities associated with users with deleted user accounts.
- **Microsoft 365 HR data connector**: If configured, [HR connector](import-hr-data) events help you identify risky activities associated with users that have resignation or upcoming termination dates.

Analytics insights from scans use the same risk management activity signals as Insider Risk Management policies. They report results based on both single and sequence user activities. However, the risk scoring for analytics uses up to 10 days of activity while insider risk policies use daily activity for insights. When you first enable and run analytics in your organization, you see the scan results for one day. If you leave analytics enabled, you see the results of each daily scan added to the insight reports for a maximum range of the previous 10 days of activity.

## Receive real-time guidance on configuring indicator threshold settings

Manually tuning policies to reduce "noise" can be a time-consuming experience that requires a lot of trial and error testing to determine the desired configuration for your policies. If you turn on analytics, you can get real-time insights to help you efficiently adjust the selection of indicators and thresholds of activity occurrence so that you don't receive too few or too many policy alerts. [Use real-time analytics recommendations to set thresholds](insider-risk-management-settings-policy-indicators#use-real-time-analytics-recommendations-to-set-thresholds).

## Enable analytics and start a scan of potential insider risks in your organization

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

To enable insider risk analytics, you must be a member of the *Insider Risk Management*, *Insider Risk Management Admins*, or *Microsoft 365 Global admin* role group.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. On the **Overview** tab, scroll down to the **Insider risk analytics** card. Selecting **Run scan** turns on analytics scanning for your organization, and scan results can take up to 48 hours before insights are available as reports for review. Under **Scan for insider risks in your organization**, select **Run scan**.

Tip

You can also turn on scanning in your organization through **Settings** at the top of any Insider Risk Management page. Select **Analytics**, then turn on the setting.

## View analytics insights after the first analytics scan

To view the results of analytics scanning in your organization, go to **Insider Risk Management** &gt; **Reports** &gt; **Analytics**. For more information about reports, see [Use reports in Insider Risk Management](insider-risk-management-reports).

## Turn off analytics

To turn off insider risk analytics, you must be a member of the *Insider Risk Management*, *Insider Risk Management Admins*, or Microsoft 365 *Global admin* role group.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page.
3. Select **Insider Risk Management** to go to the Insider Risk Management settings.
4. Under **Insider risk settings**, select **Analytics**, and then turn off the setting.

When you disable analytics:

- Analytics insight reports stop updating and don't show new risks.
- You can't [see real-time analytics when you customize indicator threshold settings for your policies](insider-risk-management-settings-policy-indicators#indicator-level-settings).

## Enable user-level analytics in your organization

Insider Risk Management generates user activity summaries and insider risk severity insights for potentially risky behaviors at a user level. You can view these insights in the following experiences:

- Data Loss Prevention (DLP) alerts
- Communication Compliance policies
- Microsoft Defender user entity pages and alerts

User analytics cover all eligible users in your organization, including users not in the scope of any Insider Risk Management policy. When investigating alerts in Microsoft Defender, DLP, or Communication Compliance, analysts automatically have access to user information that helps improve risk assessments. Analysts can also use insider risk severity to quickly identify the most egregious and time-sensitive alerts and prioritize these alerts for investigation and remediation.

To enable insider risk user-level analytics, you must be a member of the *Insider Risk Management*, *Insider Risk Management Admins*, or Microsoft 365 *Global admin* role group.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page.
3. Select **Insider Risk Management** to go to the Insider Risk Management settings.
4. Under **Insider Risk Management settings**, select **Analytics** and turn on the **Show insights at user level** setting.
5. Under **Insider Risk Management settings**, select **Data sharing** and turn on the **Share user risk details with other security solutions** setting.