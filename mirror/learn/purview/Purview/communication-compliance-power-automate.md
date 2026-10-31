---
layout: Conceptual
title: Use Microsoft Power Automate with Communication Compliance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/communication-compliance-power-automate
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn more about using Micrsoft Power Automate with Communication Compliance.
keywords: Microsoft 365, Microsoft Purview, compliance, Communication Compliance
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-25T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-communication-compliance
ms.collection:
- purview-compliance
- microsoft-365-copilot
search.appverid:
- MET150
- MOE150
locale: en-us
document_id: 1789c87d-cdfb-9e79-1a66-acd126297418
document_version_independent_id: 1789c87d-cdfb-9e79-1a66-acd126297418
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/communication-compliance-power-automate.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: communication-compliance-power-automate
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/communication-compliance-power-automate.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
platformId: 8f07b061-cbea-c5ae-21bd-132c47a1f4a1
---

# Use Microsoft Power Automate with Communication Compliance | Microsoft Learn

[Microsoft Power Automate](/en-us/power-automate/getting-started) is a workflow service that automates actions across applications and services. By using flows from templates or creating them manually, you can automate common tasks associated with these applications and services. When you enable Power Automate flows for Communication Compliance, you can automate important tasks for alerts and users. You can configure Power Automate flows to notify managers when users have Communication Compliance alerts and other applications.

Customers with Microsoft 365 subscriptions that include Communication Compliance don't need extra Power Automate licenses to use the recommended default Communication Compliance Power Automate template. Customize the default template to support your organization and cover core Communication Compliance scenarios. If you choose to use premium Power Automate features in these templates, create a custom template by using the Microsoft Purview connector, or use Power Automate templates for other compliance areas in Microsoft Purview, you might need extra Power Automate licenses.

Important

Are you receiving requests for extra license validation when testing Power Automate flows? Your organization might not have received service updates for this preview feature yet. We're deploying updates, and all organizations with Microsoft 365 subscriptions that include Communication Compliance should have license support for flows created from the recommended Power Automate templates before October 30, 2020.

![Communication Compliance Power Automate.](media/communication-compliance-power-automate.png)

The following Power Automate template is provided to customers to support process automation for Communication Compliance alerts:

- **Notify manager when a user has a Communication Compliance alert**: Some organizations might need immediate management notification when a user has a Communication Compliance alert. When you configure and select this flow, the manager for the case user receives an email message with the following information about all alerts:
    - Applicable policy for the alert
    - Date and time of the alert
    - Severity level of the alert

## Automate tasks for alerts and users with Microsoft Power Automate

To create a Power Automate flow from a recommended default template, use the **Manage Power Automate flows** option from **Automate** when working directly in an alert. To create a Power Automate flow with **Manage Power Automate flows**, you must be a member of at least one Communication Compliance role group.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Communication Compliance** solution.
3. Select **Policies** in the left navigation, then select the policy that includes the policy matches that you want to review.
4. Select the **Pending** tab, and select a policy match.
5. Select **Power Automate** from the alert action menu.
6. On the **Power Automate** page, select a default template from the **Communication Compliance templates you may like** section on the page.
7. Review the embedded connections needed for the flow and check the connection statuses. If needed, update any connections that aren't displayed as available. Select **Continue**.
8. By default, the recommended flows are preconfigured with the recommended Communication Compliance and Microsoft 365 service data fields required to complete the assigned task for the flow. If needed, customize the flow components by using **Show advanced options** and configuring the available properties for the flow component.
9. If needed, add any additional steps to the flow by selecting **New step**. In most cases, this change shouldn't be needed for the recommended default templates.
10. Select **Save draft** to save the flow for further configuration later, or select **Save** to complete the configuration for the flow.
11. Select **Close** to return to the **Power Automate flows** page. The new template is listed as a flow on the **My flows** tab and is automatically available for the user that created the flow when working with Communication Compliance alerts.

## Share a Power Automate flow

By default, only the creator can access a Power Automate flow. To give other Communication Compliance users access to a flow, the creator must share it. Use **Power Automate** to share a flow when working directly in an alert.

To share a Power Automate flow, you must be a member of at least one Communication Compliance role group.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Communication Compliance** solution.
3. Select **Policies** in the left navigation, then select the policy that contains the policy matches you want to review.
4. Select the **Pending** tab, then select a pending policy match.
5. Select **Power Automate** from the alert action menu.
6. On the **Power Automate flows** page, select the **My flows** or **Team flows** tab.
7. Select the flow to share, then select **Share** from the **Flow Options** menu.
8. On the flow sharing page, enter the name of the user or group you want to add as an owner for the flow.
9. On the **Connection Used** dialog, select **OK** to acknowledge that the added user or group has full access to the flow.

## Edit a Power Automate flow

Use **Power Automate** to edit a flow when working directly in an alert. To edit a Power Automate flow, you must be a member of at least one Communication Compliance role group.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Communication Compliance** solution.
3. Select **Policies** in the left navigation, then select the policy that contains the policy matches you want to review.
4. Select the **Pending** tab, then select a pending policy match.
5. Select **Power Automate** from the alert action menu.
6. On the **Power Automate flows** page, select the flow to edit. Select **Edit** from the flow control menu.
7. Select **ellipsis** &gt; **Settings** to change a flow component setting or **ellipsis** &gt; **Delete** to delete a flow component.
8. Select **Save**, then select **Close** when finished editing the flow.

## Delete a Power Automate flow

If you need to delete a flow, use **Power Automate** when working directly in an alert. To delete a Power Automate flow, you must be a member of at least one Communication Compliance role group.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Communication Compliance** solution.
3. Select **Policies** in the left navigation, then select the policy that contains the policy matches you want to review.
4. Select the **Pending** tab, then select a pending policy match.
5. Select **Power Automate** from the alert action menu.
6. On the **Power Automate flows** page, select the flow that you want to delete. Select **Delete** from the flow control menu.
7. On the deletion confirmation dialog, select **Delete** to remove the flow or select **Cancel**.