---
layout: Conceptual
title: Take action with Data Security Posture Management recommendations - (classic) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-posture-management-recommendations
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use recommendations in Data Security Posture Management (classic).
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
- data-security-posture-management
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
locale: en-us
document_id: 5b374f9b-3fcb-0eef-2386-a9c99cc2bb04
document_version_independent_id: 5b374f9b-3fcb-0eef-2386-a9c99cc2bb04
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-posture-management-recommendations.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-posture-management-recommendations
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-posture-management-recommendations.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/a3955c7b-f5ee-420d-aff5-d7119738f38b
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31948f4-2f38-404b-ac93-c3c8c5b3ae33
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 4d339aed-340a-420a-1d20-5ecaa565e60f
---

# Take action with Data Security Posture Management recommendations - (classic) | Microsoft Learn

Note

This article is for the **classic** version of Data Security Posture Management, now replaced with a new version that expands coverage to more data sources, introduces guided workflows for proactive risk management, and streamlines data security operations so you can more confidently adopt AI across your digital estate.

These improvements won't be added to this classic version so we invite you to try the new [Data Security Posture Management](data-security-posture-management-learn-about).

Data Security Posture Management (DSPM) generates recommendations directly from the processed data, current state of unprotected sensitive assets in your organization, and user activities that put the unprotected sensitive assets at risk. Specific recommendations enable you to take action and quickly create data loss prevention (DLP) and Insider Risk Management policies to help mitigate data security risks. DSPM recommendations can also help you identify coverage gaps in existing Insider Risk Management and DLP policies.

## Using recommendations

To display and review recommendations, go to **Data Security Posture Management (classic)** &gt; **Overview** or **Data Security Posture Management (classic)** &gt; **Recommendations**.

- From the **Overview** page, you can review the top two data security recommendations or select **View all recommendations** for a complete listing of all recommendations.
- From the **Recommendations** page, you can directly review a complete listing of all recommendations.

Recommendations come from the last 30 days of user activity and the state of unprotected sensitive assets. As processing continues, the list of recommendations automatically updates and removes recommendations older than 30 days.

Each recommendation provides a short description of the risky activity or state of the unprotected sensitive asset and includes a recommended policy to configure to help mitigate ongoing and future data security risks. The recommendation displays metrics for the number of activities, the associated type of protection, and the number of users involved.

Select **View recommendation** to take action and create a new policy to help mitigate the data security risks associated with the recommendation.

### Creating policies from recommendations

After selecting **View recommendation** for a specific recommendation, you can create one or more policies in data loss prevention (DLP) and/or Insider Risk Management to help mitigate the data security risks associated with the recommendation.

For example, if you have a recommendation to prevent users from copying sensitive files to network shares, the recommendation might be to create both an Insider Risk Management policy to detect when certain users perform risky activities containing sensitive data and a DLP policy to prevent those same users from sharing the data with others.

To create policies from a recommendation, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned DSPM permissions.
2. Select the **Data Security Posture Management (classic)** solution card, then select **Recommendations** in the left nav.
3. Select a recommendation, then select **View recommendation**.
4. On the recommendation flyout pane, choose the option to create either one type of policy or multiple policies. By default, if more than one policy applies to the recommendation, the option to create multiple policies is selected by default.
5. Each policy type has a dedicated section for configuring the policy options:
6. For the **Insider Risk Management policy**section options, configure the following policy options:
    1. **Policy name**: Enter a unique policy name or accept the suggested policy name.
    2. **User scope**: Select **Include all users and groups (recommended for best coverage)** or **I want to choose specific users and groups**. If you choose to include specific users or groups, enter the user and group names in the picker field.
    3. **Settings we filled in for you**: The settings for the policy are automatically scoped to the type of activity and unprotected data asset insights associated to the recommendation. These settings include specific policy templates, triggering events, and indicators. If you need to change the suggested settings, select **Customize** &gt; **Insider risk policy** to create the policy in the Insider Risk Management policy workflow.
7. For the **Data Loss Prevention policy**section options, configure the following policy options:
    1. **Policy name**: Enter a unique policy name.
    2. **Mode**: Select **Simulation** or **On**.
    3. **Settings we filled in for you**: The settings for the policy are automatically scoped to the type of activity and unprotected data asset insights associated to the recommendation. These settings include specific sensitive information types, enforcement actions, triggering events, and data locations. If you need to change the suggested settings, select **Customize** &gt; **DLP policy** to create the policy in the DLP policy workflow.
8. If the suggested policy options meet your needs, select **Create policy**. This step creates one or more policies in the applicable solutions.

It takes a few minutes to create each policy. The new policies appear on the **Policies** tab in the applicable solutions. Once the policy is active, it could take at least 24 hours for the triggering event to occur and score user activity, then the first alert is generated. If administrator notifications are turned on, you get an email when this alert occurs.

You can triage the alert and confirm it to a case for further investigation or dismiss it as normal behavior. After you review a few alerts, fine tune your policy to control how many alerts are generated, what activities are detected, and more. Additional recommendations might be generated for this type of activity that can help you with policy updates.

### Updating policies in other solutions

To update policies you created from recommendations, use the policy management tools in each solution. The tools in the solutions let you fully customize policies beyond the quick policy settings included with recommendations.

- Manage [Insider Risk Management policies](insider-risk-management-policies)
- Manage [DLP policies](dlp-create-deploy-policy)

### Verifying the configuration of existing policies

If your organization already has Insider Risk Management or DLP policies configured, recommendations in DSPM help you identify and correct any gaps in your current policy configurations. Instead of using the policy creation options directly in the recommendation, you might choose to use the insights associated with the recommendation to update or refine an existing Insider Risk Management or DLP policy.