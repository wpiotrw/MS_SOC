---
layout: Conceptual
title: Create an investigation in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-investigation
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to create and manage investigations in Data Security Investigations. Discover methods, AI context, and integration options to streamline your analysis.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-security-investigations
ms.collection:
- purview-compliance
- data-security-investigations
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: 7d80e4e1-2666-fc22-75d3-2e6c491919a8
document_version_independent_id: 7d80e4e1-2666-fc22-75d3-2e6c491919a8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-investigation.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-investigation
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-investigation.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1577a46d-8446-40bd-bfae-0578362f4d94
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cdf3f22d-5420-4d59-a2bf-66d6b3d9c828
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
platformId: 87a2163f-2bcb-6cff-0cef-3fc4f0d3d5ea
---

# Create an investigation in Data Security Investigations | Microsoft Learn

After configuring [billing and usage options](data-security-investigations-billing) for Data Security Investigations and [assigning permissions to analysts](data-security-investigations-permissions) in your organization that manage investigations, create and manage an investigation for collection and analysis activities.

## Investigations dashboard

Depending on your permissions, the **Investigations** dashboard in the Microsoft Purview portal displays investigations in your organization. If you're not assigned to the *Data Security Investigations Admins* role group, you can only view investigations you're assigned to as an investigator or reviewer.

The **Investigations** dashboard lets you quickly see the investigations in your organization that you have access to, the description of the investigations, and important information associated with each investigation.

- **Name**: The name of the investigation. The investigation name must be unique in your organization.
- **Description**: The description entered when the investigation was created.
- **Created on**: The date and time in Coordinated Universal Time (UTC) when the investigation was created.
- **Last modified**: The date and time in Coordinated Universal Time (UTC) when the investigation was last modified.

Select **Edit columns** to customize the displayed columns and the order of the columns in the **Investigations** dashboard. Choose the columns to display or drag and drop columns to reorder.

## AI context for investigations

Additional context for AI helps focus AI-provided results in an investigation to specific areas, subjects, and issues to help eliminate noise and decrease the time it takes to discover and mitigate relevant items. Without additional context, AI analysis might return nonrelated categories and risk examinations results for data prepared for AI in your investigation. By providing detailed context for an investigation, categorization and risk examination results more accurately represent the areas you need to investigate.

For example, if you want an investigation to focus primarily on bribery issues, consider including *Find instances of bribery* in the **Additional context for AI** field on the **Create an investigation** dialog when creating new investigations in full-draft mode, from Defender XDR, or from Insider Risk Management. The more details that you provide as the context for the investigation, the more focused the AI analysis results are in the investigation.

Tip

Use natural language to provide the context and details you're looking for in the investigation. The context is automatically processed to remove typos, incorrect grammar or punctuation, symbols, and more to help improve clarity and readability for backend AI processing. This context review doesn't change the original intent of the provided context.

Any AI-related analysis for an investigation includes the context you provide for a new or existing investigation. Context-related categories are automatically included in AI-suggest categories and risk examinations for investigations including a custom context statement. You can add or edit context for an investigation at any time, but you must rerun categorization and risk examinations after any context changes. All changes to context statements are automatically recorded as extended properties for an investigation.

## Create an investigation

Depending on your scenario, you can create investigations by using each of the following methods:

- **From Microsoft Defender XDR incidents**: Create an investigation from a Defender XDR incident.
- **From Microsoft Insider Risk Management cases**: Create an investigation from an Insider Risk Management case.
- **From Data Security Posture Management insights**: Create an investigation from exfiltration activities identified in Data Security Posture Management.
- **Manually by using full draft mode**: Create an investigation by using the *full draft mode* option to configure specific data sources and search conditions.

### Create an investigation from Defender XDR

With the integration with the [Microsoft Defender XDR](/en-us/defender-xdr/microsoft-365-defender) solution, you can quickly open an investigation in Data Security Investigations as part of your response to data breach incidents. You can create an investigation from Defender XDR incidents containing mailbox, email message, or file nodes. To create investigations in Data Security Investigations in the Microsoft Defender portal, you must have the following roles assigned:

- [Security Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator)
- [Security Operator](/en-us/entra/identity/role-based-access-control/permissions-reference#security-operator)

Create a new investigation from a Defender XDR incident by using one of the following methods:

- Select **Create investigation** from the Data Security Investigations banner at the top of any incident in Defender XDR. This banner automatically displays if the incident might contain sensitive information. The new investigation contains all nodes included in the Defender XDR incident.
- Select **Create Data Security Investigation** from the ellipsis control in the top right of an incident page. The new investigation contains all nodes included in the Defender XDR incident.
- Select any individual mailbox, email message, or file node in the Defender XDR incident to display the node menu and select **Create Data Security Incident**. The investigation contains only the selected node from the Defender XDR incident.

After you select one of the previous options, the **Create a data security investigation** dialog is displayed. Complete the following steps:

1. In the **Name** field, give the investigation a name (required). The investigation name must be unique in your organization. If the name you enter isn't unique, you're notified when you select **Create**.
2. In the **Description** field, add an optional description to help others understand this investigation.
3. In the **Scope** field, choose the items from the incident to include in the investigation.
4. In the **Additional context for AI** field, enter additional context to help AI focus your investigation on specific areas and issues.

Important

You can't include mailboxes in the scope of an investigation and also include files or email messages. Investigations created from incidents including mailboxes must be standalone investigations. Select either mailboxes in the scope area OR email messages and files. Both email messages and files from an incident can be included in the same investigation.

1. Select **Create** to create the investigation.

The items included in the scope of the investigation are automatically included as data sources and you're ready to start reviewing and adding these items to the investigation scope in Data Security Investigations.

Note

Sometimes the data sources for SharePoint site or files might not autopopulate in an investigation. If this situation occurs, manually add the data sources and use the suggested query.

Important

Investigations created from Defender XDR incidents that contain more than approximately 3,000 items might not return complete results. The exact limit depends on the file names and paths of the returned items. For more information about limits, see [Limits in Data Security Investigations](data-security-investigations-ref-limits).

### Create an investigation from Insider Risk Management

With the integration of [Microsoft Purview Insider Risk Management](insider-risk-management), you can quickly open an investigation in Data Security Investigations from a case and for potentially risky activities. To create investigations in Data Security Investigations in Insider Risk Management, you must have at least one of the following roles assigned:

- Insider Risk Management
- Insider Risk Management Investigator

To create a new investigation from an Insider Risk Management case, complete the following steps:

1. In the Microsoft Purview portal, go to **Insider Risk Management &gt; Cases** and select a case.
2. On the **Cases** page, select **Case actions**.
3. Select **Investigate data security with AI**.
4. In the **Create a data security investigations** dialog box, complete the following fields:

    1. In the **Name** field, enter a name for the investigation (required). The investigation name must be unique in your organization. If the name you enter isn't unique, you're notified when you select **Create investigation**.
    2. In the **Description** field, add an optional description to help others understand this investigation.
    3. In the **Investigation scope** field, choose the items from the case to include in the investigation.
    4. In the **Additional context for AI** field, enter additional context to help AI focus your investigation on specific areas and issues.
5. Select **Create investigation** to create the investigation.

The items included in the case are automatically included as data sources. You're ready to start reviewing and adding these items to the investigation scope in Data Security Investigations.

Important

Investigations created from Insider Risk Management cases that contain more than approximately 3,000 items might not return complete results. The exact limit depends on the file names and paths of the returned items. For more information about limits, see [Limits in Data Security Investigations](data-security-investigations-ref-limits).

### Create an investigation from Data Security Posture Management

By using the integration with the [Microsoft Purview Data Security Posture Management (DSPM)](data-security-posture-management-learn-about) solution, you can investigate data exposure insights surfaced by DSPM exfiltration objectives. The **Prevent exfiltration to risky destinations** objective card supports two investigation modes:

- **Manual investigation**: Create an investigation on demand from the exfiltration objective card to analyze specific data exposure insights.
- **Proactive AI insights (preview)**: Enable an opt-in toggle that automatically creates and refreshes a single investigation for your tenant every 24 hours. This investigation continuously analyzes recently exfiltrated sensitive data across five fixed risk categories: credentials and access information, personally identifiable information (PII), financial information, confidential information, and intellectual property (IP). The DSPM exfiltration objective card displays the count of items identified in each risk category.

Investigations created from DSPM automatically scope to all sensitive data exfiltrated from your organization in the last 30 days. These investigations enable deeper, AI-powered content analysis of recently exfiltrated data, giving security teams actionable insights without extra configuration.

For more information about the roles and permissions needed to create an investigation in Data Security Investigations from DSPM, see [Permissions for Microsoft Purview Data Security Posture Management](data-security-posture-management-permissions).

#### Create a manual investigation from DSPM

To manually create a new investigation from DSPM, complete the following steps:

1. In the Microsoft Purview portal, go to **DSPM**.
2. In **Objectives**, select the **Prevent exfiltration to risky destinations** card.
3. Select **View objective** to view exfiltration details and proactive insights.

    Note

    It might take 24 hours or more for insights to display for the objective.
4. On the **Exfiltration risk patterns** card, select **Create investigation**.
5. In the **Create a data security investigation** dialog, complete the following fields:

    - **Name**: Enter a unique name for the investigation (required).
    - **Description**: Provide a description to help others understand the purpose of the investigation (optional).
    - **Add context for AI**: Provide context for the investigation (optional).
6. Select **Create investigation** to create the investigation in Data Security Investigations.

After the investigation is created, it automatically includes all scoped data items as data sources. You're ready to start reviewing, analyzing, and taking mitigation actions by using the full capabilities of Data Security Investigations. If you didn't configure Data Security Investigations before creating the investigation, the investigation is created but you need to [configure Data Security Investigations](data-security-investigations-get-started) before you can view the investigation.

The most recent manual investigation that you created from DSPM (preview) is always available for selection on the **Exfiltration risk patterns** card in the **Prevent exfiltration to risky destinations** objective.

#### Enable proactive AI insights from DSPM

To enable proactive AI insights, complete the following steps:

1. In the Microsoft Purview portal, go to **DSPM (preview)**.
2. In **Objectives**, select the **Prevent exfiltration to risky destinations** card.
3. Select **View objective** to view exfiltration details.
4. On the **Exfiltration risk patterns** card, turn on the **Proactive AI insights** toggle.

After you enable the toggle, the first investigation is created automatically. Insights might take up to 24 hours to appear after initial activation. The investigation refreshes automatically every 24 hours while the toggle remains enabled.

Important

Proactive AI insights consume Data Security Investigations storage and AI analysis meters while the toggle is enabled. In the current preview, proactive AI insights use five fixed risk categories. Custom category templates and per-item deletion within the auto-created investigation aren't supported. For more information about billing, see [Data Security Investigations billing](data-security-investigations-billing).

### Create an investigation using full draft mode

In some scenarios, you might prefer to create a new investigation that isn't associated with a Microsoft Purview Insider Risk Management or Microsoft Defender XDR incident. By using [full draft mode](data-security-investigations-investigation-full-draft-mode), create a new investigation that starts with new data sources and queries.

## Manage investigation settings

Investigation settings include investigation information and access permissions. You can access settings for a specific investigation by selecting **Investigation settings** after selecting an investigation.

For more information about investigation settings, see:

- [Investigation settings](data-security-investigations-settings-investigation)
- [Access and permissions settings](data-security-investigations-settings-access-permissions)