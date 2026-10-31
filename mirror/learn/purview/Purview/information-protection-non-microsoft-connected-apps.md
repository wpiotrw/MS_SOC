---
layout: Conceptual
title: Use Microsoft Purview sensitivity label policies for non-Microsoft connected apps (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-protection-non-microsoft-connected-apps
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: v-reezaali
author: ReezaAli149
manager: laurawi
ms.date: 2026-08-26T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
search.appverid:
- MET150
ms.custom: seo-marvel-apr2021
description: Learn how to use auto-labeling policies in Microsoft Purview to protect sensitive data at rest in non-Microsoft connected apps like Box and Google Workspace.
ai-usage: ai-assisted
locale: en-us
document_id: 5a6271e9-3918-9baf-7662-da72132ba0be
document_version_independent_id: 5a6271e9-3918-9baf-7662-da72132ba0be
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-protection-non-microsoft-connected-apps.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-protection-non-microsoft-connected-apps
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-protection-non-microsoft-connected-apps.md
platformId: ccb56ca8-b885-7556-4a45-723e47771573
---

# Use Microsoft Purview sensitivity label policies for non-Microsoft connected apps (preview) | Microsoft Learn

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

Auto-labeling isn't limited to Microsoft 365 locations. Through the integration between Microsoft Purview Information Protection and Microsoft Defender for Cloud Apps, you can automatically apply your Microsoft Purview sensitivity labels to files stored in non-Microsoft connected apps, such as Box and Google Workspace. Because these labels use the same sensitive information types and classifiers similar to Microsoft 365, your sensitive content is classified and protected consistently, wherever it's stored.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Supported non-Microsoft apps

Microsoft Purview supports auto-labeling policies for the following non-Microsoft apps:

- Box
- Google Workspace

Note

These apps are rolling out in phases. Not all apps may be available in your tenant at the same time. Check the [Microsoft 365 roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap) for the latest availability information.

## Before you begin

### Licensing requirements

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions

The account you use to create and deploy policies must be a member of one of these role groups:

- Compliance administrator
- Compliance data administrator
- Information Protection
- Information Protection Admin
- Security administrator

Important

Microsoft recommends that you use roles with the fewest permissions. This helps improve security for your organization. Global Administrator is a highly privileged role that should only be used in scenarios where a lesser privileged role can't be used.

### Publish labels

To select sensitivity labels when setting up auto-labeling policies, the labels must first be published. For more information on creating and publishing labels, see [Create and configure sensitivity labels and their policies](create-sensitivity-labels).

### Set up a Microsoft Defender for Cloud Apps connector

Before you can apply auto-labeling policies to a non-Microsoft app, you must connect that app to Microsoft Defender for Cloud Apps using an app connector. Purview uses the existing Microsoft Defender for Cloud Apps connectors to access capabilities in the non-Microsoft app.

For instructions on setting up app connectors, see [Connect apps to get visibility and control with Microsoft Defender for Cloud Apps](/en-us/defender-cloud-apps/enable-instant-visibility-protection-and-governance-actions-for-your-apps).

After you connect your cloud apps to Defender for Cloud Apps, you can create auto-labeling policies for them in Microsoft Purview.

## Create an auto-labeling policy for non-Microsoft connected apps

You can use auto-labeling policies to automatically apply or remove sensitivity labels on data stored in non-Microsoft connected apps. For the general procedure to create an auto-labeling policy, see [Automatically apply a sensitivity label to Microsoft 365 data](apply-sensitivity-label-automatically).

To create an auto-labeling policy scoped to non-Microsoft connected apps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Go to **Solutions** &gt; **Information protection** &gt; **Policies** &gt; **Auto-labeling policies** &gt; **+ Create auto-labeling policy**.
3. On **What type of auto-labeling policy do you want to create?**, choose **Automatically apply labels only**.
4. Select **Custom** &gt; **Custom policy** &gt; **Next**.

    Important

    Non-Microsoft connected app policies are only supported with the **Custom** policy template. The predefined Financial, Medical and health, and Privacy templates don't support non-Microsoft app locations.
5. Enter a name and description for the auto-labeling policy, then select **Next**.
6. On **Choose a label to auto-apply**, choose **Choose a label**. On **Choose a sensitivity label**, select all labels to include in the policy, and then select **Add** &gt; **Next**.
7. On **Assign admin units**, the scope is set to **Full directory**. Administrative units aren't supported for non-Microsoft app locations.
8. On **Choose locations where you want to apply the label**, select one or more of the supported non-Microsoft apps (such as **Box** or **Google Workspace**).

    Important

    Non-Microsoft app locations can be selected together, but they can't be combined with other locations like SharePoint, Exchange, SQL Server, Azure Storage or OneDrive in the same policy.
9. By default, the policy applies to all instances of the selected app. To scope the policy to specific tenants, select **Edit**.

    1. To exclude instances, in **All instances**, select **Exclude instances** &gt; **+ Exclude instance**. From the list of instances, select instances to exclude from the policy, and then select **Done** &gt; **Done**.
    2. To apply the policy to specific instances, select **Specific instances** &gt; **+ Include instance**. From the list of instances, select instances to include, then select **Done** &gt; **Done**.
10. Select **Next** to proceed.
11. On **Set up common or advanced rules**, begin creating rules by selecting **Advanced Rules**. Select **Next**.
12. Select **+ New rule**, and provide a **Name** and **Description**.
13. Configure **Conditions** for the rule. The conditions you can use vary by app.
14. Select **Save** to save the rule, then select **Next**.
15. On **Additional label settings**, optionally select **All locations** to replace existing labels with lower priority in the selected applications. Select **Next**.
16. On **Decide if you want to test out the policy now or later**, choose either **Turn on policy** or **Leave policy turned off**. Select **Next**.

    Important

    **Simulation mode** isn't supported for non-Microsoft connected app policies.
17. Review your settings and select **Create policy** to create the policy.

## Attribute availability by app

The conditions and actions you can use in a policy depend on the item attributes that each app makes available. Most attributes are available for all supported apps, but some aren't available for certain apps. Use the following table to understand which attributes you can rely on when you build rules for a specific app.

| Attribute | Description | Availability |
| --- | --- | --- |
| Name | The display name of the item. | Available in all apps |
| File access level | The item's access level, which indicates its sharing scope. | Available in all apps |
| Created date | The date the item was created. | Not available |
| Modified date | The date the item was last modified. | Available in all apps |
| Collaborators | The users the item is shared with, including their roles. | Not available |
| Parent folders | The parent folders that contain the item. | Available in all apps |

## Monitoring and reporting

### Activity explorer

Activity explorer supports non-Microsoft connected app policies. You can monitor labeling policy activity for your non-Microsoft apps in the same way you monitor Microsoft 365 locations.

### Content explorer

Content explorer isn't supported for non-Microsoft connected apps. You can't browse or inspect content stored in these apps through Content explorer.

## Known issues

The following is a list of known issues when using non-Microsoft connected apps for sensitivity label policies:

- **Encrypted files** – Encrypted files stored in non-Microsoft apps aren't currently supported for classification.
- **PDF files** – PDF files stored in non-Microsoft apps aren't currently supported for classification.
- In Microsoft Purview for Microsoft 365, when a sensitivity label is applied automatically through an auto-labeling policy, a higher-priority label replaces any existing lower-priority label. However, for Box and Google Workspace, if a label has already been applied to a file by an auto-labeling policy, it cannot be replaced by a higher-priority label from **another** auto-labeling policy. For more information, see [Automatically apply a sensitivity label to Microsoft 365 data](apply-sensitivity-label-automatically).