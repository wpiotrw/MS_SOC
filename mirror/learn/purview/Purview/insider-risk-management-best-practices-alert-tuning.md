---
layout: Conceptual
title: Best practices for managing your alert volume in Insider Risk Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-best-practices-alert-tuning
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about best practices for managing your Insider Risk Management alert queue so that you don't have too few or too many alerts to review.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: best-practice
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-02-27T00:00:00.0000000Z
audience: itpro
ms.collection:
- highpri
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- highpri
ms.custom: admindeeplinkCOMPLIANCE
locale: en-us
document_id: e82e78c9-2b02-5614-35f7-9d8ecd65bbcb
document_version_independent_id: e82e78c9-2b02-5614-35f7-9d8ecd65bbcb
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-best-practices-alert-tuning.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-best-practices-alert-tuning
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-best-practices-alert-tuning.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 80ee6c82-34b5-18e2-71a9-197b9ed122e9
---

# Best practices for managing your alert volume in Insider Risk Management | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Reviewing, investigating, and acting on potentially risky insider alerts are important parts of minimizing insider risks in your organization. When you quickly take action to minimize the impact of these risks, you can potentially save time, money, and regulatory or legal ramifications for your organization. In this remediation process, the first step of reviewing alerts can seem like the most difficult task for many analysts and investigators.

This article provides best practices for managing the volume of alerts in your organization so that you don't have too many or too few alerts. For a general discussion of how alerts are generated and the tools for managing alerts, see [Investigate insider risk activities](insider-risk-management-activities).

## Too few alerts to review

If you're receiving too few Insider Risk Management alerts, try the following solutions:

- **Update your settings:** Changes that you make to settings apply globally across all of your policies.

    - **Enable more indicators:** When you select more indicators, your policies can detect a larger group of activities.

        **How to:** Go to **Settings** &gt; **Policy indicators**, and then enable all available and relevant indicators.
    - **Adjust the Alert volume slider:** Use this slider to see all medium and high severity alerts, and most low severity alerts. **Note:** Adjusting the slider might result in more false positives.

        **How to:** Go to **Settings** &gt; **Intelligent detections** &gt; **Alert volume**, and then move the slider to **More alerts**.
- **Modify the policy:** Find the policy that isn't generating enough alerts, and then consider the following actions:

    - **Increase the user coverage in the policy:** Policies with few users included in the scope are less likely to generate alerts. If applicable, consider increasing the number of users in scope for your policy.

        **How to:** Select a specific policy on the **Policies** page, select **Edit policy**, and then go to the **Users and groups** page to increase the number of included users.
    - **Lower the trigger thresholds:** For policies based on the *Data leaks* and *Risky Browser Usage (preview)* templates, you can customize some trigger thresholds. These thresholds define when you start to detect user activities. If you lower trigger thresholds, you lower the criteria for a user to start being evaluated for risky activity. **Note:** If a user doesn't appear in the **Users and groups** page, it means that triggering event criteria isn't met yet.

        **How to:** Go to the specific policy on the **Policies** page, select **Edit policy**, go to the **Trigger thresholds** page, select the **Use custom thresholds** option, and then adjust your thresholds.
    - **Add more indicators:** Indicators are the activities a user must do to be considered risky. If you don't have many indicators (activities considered to be risky) selected in your policy, alerts are less likely to be generated.

        **How to:** Go to the specific policy on the **Policies** page, select **Edit policy**, go to the **Indicators** page, and then select more indicators.
    - **Lower indicator thresholds:** After your users begin getting evaluated (have a triggering event), an alert is generated only if they do activities over a certain threshold that might indicate that their activity is risky. When you lower the indicator thresholds, you lower the threshold that users must surpass to generate an alert.

        **How to:** Go to the specific policy on the **Policies** page, select **Edit policy**, go to the **Indicator thresholds** page, select the **Customize thresholds** option, and then set your thresholds. [Learn about indicator threshold recommendations](insider-risk-management-settings-policy-indicators#use-real-time-analytics-recommendations-to-set-thresholds)

## Too many alerts to review

If you receive too many valid alerts or have too many stale low-risk alerts, consider taking the following actions:

- **Enable analytics:** When you enable analytics, you can quickly identify potential risk areas for your users. Analytics helps you determine the type and scope of Insider Risk Management policies that you might want to configure.

    **How to:** Go to **Settings** &gt; **Analytics**.
- **Get real-time insights:** If you want to take advantage of threshold recommendations, get real-time insights from analytics. These insights can help you efficiently adjust the selection of indicators and thresholds of activity occurrence so that you don't receive too few or too many policy alerts.

    **How to:** See [Use real-time analytics to help manage alert volume](insider-risk-management-settings-policy-indicators#use-real-time-analytics-recommendations-to-set-thresholds).
- **Adjust your policies:** The most basic method to address the type and volume of alerts is selecting and configuring the correct insider risk policy. Starting with the appropriate [policy template](insider-risk-management-policy-templates#policy-templates) helps you focus the types of risk activities and alerts you see. Other factors that might impact alert volume are the size of the in-scope user and groups and the content and [channels that you prioritize](insider-risk-management-policies#prioritize-content-in-policies). Consider adjusting policies to refine these areas to what is most important for your organization.

    **How to:** Select a specific policy on the **Policies** page, then select **Edit policy**.
- **Modify your insider risk settings:** Insider risk settings include a wide variety of configuration options that can impact the volume and types of alerts you receive. Review and understand the following settings to filter out alert noise:

    - [Policy indicators and indicator thresholds](insider-risk-management-settings-policy-indicators)
    - [Global exclusions](insider-risk-management-settings-global-exclusions)
    - [Detection groups](insider-risk-management-settings-detection-groups)
    - [Variants of built-in indicators](insider-risk-management-settings-policy-indicators#create-a-variant-of-a-built-in-indicator)
    - [Intelligent detections](insider-risk-management-settings-intelligent-detections)
    - [Policy timeframes](insider-risk-management-settings-policy-timeframes)
- **Enable inline alert customization:** When you enable [inline alert customization](insider-risk-management-settings-inline-alert-customization), analysts and investigators can quickly edit policies when reviewing alerts. They can update thresholds for activity detection with Microsoft recommendations, configure custom thresholds, or choose to ignore the type of activity that created the alert. If you don't enable this setting, only users assigned to the *Insider Risk Management* role group can use inline alert customization.

    **How to:** Go to **Settings** &gt; **Inline alert customization**.
- **Bulk delete alerts, where applicable:** To save triage time for your analysts and investigators, consider immediately [dismissing multiple alerts](insider-risk-management-activities#dismiss-multiple-alerts-preview) in bulk. You can select up to 400 alerts to dismiss at one time.

## Managing resource constraints in your organization

Modern workplace users often have a wide variety of responsibilities and demands on their time. To address resource constraints, take these actions:

- **Focus analyst and investigator efforts on the highest risk alerts first:** Depending on your policies, you might capture user activities and generate alerts with varying degrees of potential impact on your risk mitigation efforts. [Filter alerts](insider-risk-management-activities#filter-alerts-save-a-view-of-a-filter-set-customize-columns-or-search-for-alerts) by severity and prioritize *High severity* alerts.
- **Use Microsoft Copilot**: You can use [Microsoft Copilot in Microsoft Purview to summarize an alert without even opening it](insider-risk-management-activities#use-copilot-to-summarize-an-alert). This approach can speed up the triaging experience.
- **Assign users as analysts and investigators:** Having the right user assigned to the proper roles is an important part of the insider risk alert review process. Make sure you assign the appropriate users to the *Insider Risk Management Analysts* and *Insider Risk Management Investigators* role groups.
- **Use automated insider risk features to help discover the highest risk activities:**
    - Use Insider Risk Management [sequence detection](insider-risk-management-policies#sequence-detection) and [cumulative exfiltration detection](insider-risk-management-policies#cumulative-exfiltration-detection) to quickly discover harder to find risks in your organization.
    - Consider fine-tuning your [risk score boosters](insider-risk-management-settings-policy-indicators), and use [global exclusions](insider-risk-management-settings-global-exclusions), [detection groups](insider-risk-management-settings-detection-groups), and [variants](insider-risk-management-settings-policy-indicators#create-a-variant-of-a-built-in-indicator).
    - [Fine tune minimum indicator threshold settings](insider-risk-management-settings-policy-indicators#indicator-level-settings) for your policies.