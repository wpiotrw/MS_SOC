---
layout: Conceptual
title: Automate Insider Risk Management actions with Microsoft Power Automate flows | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-power-automate
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to automate Microsoft Purview Insider Risk Management actions with Microsoft Power Automate flows.
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
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 18421765-4bed-d9a8-9aee-fe23c131505f
document_version_independent_id: 18421765-4bed-d9a8-9aee-fe23c131505f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-settings-power-automate.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-settings-power-automate
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-settings-power-automate.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
platformId: b9d02ab3-e42a-2597-616e-320864ea254e
---

# Automate Insider Risk Management actions with Microsoft Power Automate flows | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

[Microsoft Power Automate](/en-us/power-automate/getting-started) is a workflow service that automates actions across applications and services. By using flows from templates or created manually, you can automate common tasks associated with these applications and services. When you enable Power Automate flows for Microsoft Purview Insider Risk Management, you can automate important tasks for cases and users. You can configure Power Automate flows to retrieve user, alert, and case information and share this information with stakeholders and other applications, as well as automate actions in Insider Risk Management, such as posting to case notes. Power Automate flows are applicable for cases and any user in scope for a policy.

Customers with Microsoft 365 subscriptions that include Insider Risk Management don't need extra Power Automate licenses to use the recommended Insider Risk Management Power Automate templates. These templates can be customized to support your organization and cover core Insider Risk Management scenarios. If you choose to use premium Power Automate features in these templates, create a custom template by using the Microsoft Purview connector, or use Power Automate templates for other compliance areas in Microsoft 365, you might need more Power Automate licenses.

The following Power Automate templates support process automation for Microsoft Purview Insider Risk Management users and cases:

- **Notify users when they're added to an insider risk policy**: Use this template if your organization has internal policies, privacy requirements, or regulatory requirements that users must be notified when they're subject to Microsoft Purview Insider Risk Management policies. When you configure this flow and select it for a user, the user and their manager receive an email message when the user is added to a Microsoft Purview Insider Risk Management policy. This template also supports updating a SharePoint list hosted on a SharePoint site to detect notification message details like date/time and the message recipient. If you choose to anonymize users through the **Privacy** setting, flows created from this template don't function as intended so that user privacy is maintained.

    Power Automate flows using this template are available on the **Users dashboard**.
- **Request information from HR or business about a user in an insider risk case**: When acting on a case, insider risk analysts and investigators might need to consult with HR or other stakeholders to understand the context of the case activities. When you configure this flow and select it for a case, analysts and investigators send an email message to HR and business stakeholders configured for this flow. Each recipient receives a message with preconfigured or customizable response options. When recipients select a response option, the response is recorded as a case note and includes recipient and date/time information. If you choose to anonymize users through the **Privacy** setting, flows created from this template don't function as intended so that user privacy is maintained.

    Power Automate flows using this template are available on the **Cases dashboard**.
- **Notify manager when a user has an insider risk alert**: Some organizations might need to have immediate management notification when a user has a Microsoft Purview Insider Risk Management alert. When you configure and select this flow, the manager for the case user receives an email message with the following information about all case alerts:

    - Applicable policy for the alert
    - Date/time of the alert
    - Severity level of the alert

    The flow automatically updates the case notes that the message was sent and that the flow was activated. If you choose to anonymize users through the **Privacy** setting, flows created from this template don't function as intended so that user privacy is maintained.

    Power Automate flows using this template are available on the **Cases dashboard**.
- **Create record for insider risk case in ServiceNow**: Use this template if your organization wants to use their ServiceNow solution to keep track of Microsoft Purview Insider Risk Management cases. When in a case, insider risk analysts and investigators can create a record for the case in ServiceNow. You can customize this template to populate selected fields in ServiceNow based on your organization's requirements. For more information on available ServiceNow fields, see the [ServiceNow Connector reference](/en-us/connectors/service-now/) article.

    Power Automate flows using this template are available on the **Cases dashboard**.

## Create a Power Automate flow from an Insider Risk Management template

Important

Currently, only Power Automate flows that you create in the default environment work with Insider Risk Management.

To create a Power Automate flow in the settings area, you must be a member of the *Insider Risk Management* or *Insider Risk Management Admins* role group. To create a Power Automate flow with the **Manage Power Automate flows** option, you must be a member of at least one Insider Risk Management role group.

1. Perform one of the following actions:
    - Sign in to the [Microsoft Purview portal](https://purview.microsoft.com), select **Settings** in the upper-right corner of the page, select **Insider Risk Management** to go to the Insider Risk Management settings, then select **Power Automate flows**.
    - In the **Cases dashboard** or the **Users dashboard**, select **Automate** &gt; **Manage Power Automate flows**.
2. On the **Power Automate flows** page, select a recommended template from the **Insider Risk Management templates you may like** section.
3. Review the flow's embedded connections and check their statuses. If needed, update any connections that aren't displayed as available, then select **Continue**.
4. By default, the recommended flows come pre-configured with the recommended Insider Risk Management and Microsoft 365 service data fields required to complete the assigned task for the flow. If needed, customize the flow components by using the **Show advanced options** control and configuring the available properties for the flow component.
5. If needed, add any other steps to the flow by selecting **New step**. In most cases, you shouldn't need to add steps for the recommended default templates.
6. Select **Save draft** to save the flow for further configuration or select **Save** to complete the configuration for the flow.
7. Select **Close** to return to the **Power Automate flows** page. The new template appears as a flow on the **My flows** tabs and is automatically available from the **Automate** dropdown control when working with Insider Risk Management cases for the user creating the flow.

Important

To give other users in your organization access to the flow, you must share the flow.

## Create a custom Power Automate flow for Insider Risk Management

Important

Currently, only Power Automate flows that you create in the default environment work with Insider Risk Management.

Some processes and workflows for your organization might be outside the recommended Insider Risk Management flow templates. In these cases, you might need to create custom Power Automate flows for Insider Risk Management areas. Power Automate flows are flexible and support extensive customization, but they have required steps to integrate with Insider Risk Management features.

To create a custom Power Automate template for Insider Risk Management:

1. **Check your Power Automate flow license**: To create customized Power Automate flows that use Insider Risk Management triggers, you need a Power Automate license. The recommended Insider Risk Management flow templates don't require extra licensing and are included as part of your Insider Risk Management license.
2. **Create an automated flow**: Create a flow that performs one or more tasks after it's triggered by an Insider Risk Management event. For details on how to create an automated flow, see [Create a flow in Power Automate](/en-us/power-automate/get-started-logic-flow).
3. **Select the Microsoft Purview connector**: Search for and select the Microsoft Purview connector. This connector enables Insider Risk Management triggers and actions. For more information on connectors, see the [Connector reference overview](/en-us/connectors/connector-reference/) article.
4. **Choose Insider Risk Management triggers for your flow**: Insider Risk Management has two triggers available for custom Power Automate flows:
    - **For a selected Insider Risk Management case**: You can select flows with this trigger from the Insider Risk Management **Cases dashboard**.
    - **For a selected Insider Risk Management user**: You can select flows with this trigger from the Insider Risk Management **Users dashboard**.
5. **Choose Insider Risk Management actions for your flow:**You can choose from several actions for Insider Risk Management to include in your custom flow:
    - Get Insider Risk Management alert
    - Get Insider Risk Management case
    - Get Insider Risk Management user
    - Get Insider Risk Management alerts for a case
    - Add Insider Risk Management case note

## Share a Power Automate flow with other users

By default, only the creator can access Power Automate flows they create. For other Insider Risk Management users to access and use a flow, the flow creator must share it. To share a flow, use the settings controls in the Insider Risk Management solution or the **Manage Power Automate flows** option from the **Automate** control when working directly in the **Cases dashboard** or **Users dashboard**. After you share a flow, everyone you share it with can access the flow in the **Automate** control dropdown in the **Cases dashboard** and **Users dashboard**.

To share a Power Automate flow in the settings area, you must be a member of the *Insider Risk Management* or *Insider Risk Management Admins* role group. To share a Power Automate flow with the **Manage Power Automate flows** option, you must be a member of at least one Insider Risk Management role group.

### Share a Power Automate flow

1. Perform one of the following actions:
    - Sign in to the [Microsoft Purview portal](https://purview.microsoft.com), select **Settings** in the upper-right corner of the page, select **Insider Risk Management** to go to the Insider Risk Management settings, then select **Power Automate flows**.
    - In the **Cases dashboard** or the **Users dashboard**, select **Automate** &gt; **Manage Power Automate flows**.
2. On the **Power Automate flows** page, select the **My flows** or **Team flows** tab.
3. Select the flow to share, then select **Share** from the flow options menu.
4. On the flow sharing page, enter the name of the user or group you want to add as an owner for the flow.
5. In the **Connection Used** dialog box, select **OK** to acknowledge that the added user or group has full access to the flow.

## Edit a Power Automate flow

To edit a Power Automate flow in the settings area, you must be a member of the *Insider Risk Management* or *Insider Risk Management Admins* role group. To edit a Power Automate flow with the **Manage Power Automate flows** option, you must be a member of at least one Insider Risk Management role group.

1. Perform one of the following actions:
    - Sign in to the [Microsoft Purview portal](https://purview.microsoft.com), select **Settings** in the upper-right corner of the page, select **Insider Risk Management** to go to the Insider Risk Management settings, then select **Power Automate flows (preview)**.
    - In the **Cases dashboard** or the **Users dashboard**, select **Automate** &gt; **Manage Power Automate flows**.
2. On the **Power Automate flows** page, select a flow to edit, then select **Edit** from the flow control menu.
3. Select **ellipsis** &gt; **Settings** to change a flow component setting or **ellipsis** &gt; **Delete** to delete a flow component.
4. Select **Save**, then select **Close** to complete editing the flow.

## Delete a Power Automate flow

Note

When you delete a flow, you remove it as an option for all users.

To delete a Power Automate flow in the settings area, you must be a member of the *Insider Risk Management* or *Insider Risk Management Admins* role group. To delete a Power Automate flow with the **Manage Power Automate flows** option, you must be a member of at least one Insider Risk Management role group.

1. Perform one of the following actions:
    - Sign in to the [Microsoft Purview portal](https://purview.microsoft.com), select **Settings** in the upper-right corner of the page, select **Insider Risk Management** to go to the Insider Risk Management settings, then select **Power Automate flows**.
    - In the **Cases dashboard** or the **Users dashboard**, select **Automate** &gt; **Manage Power Automate flows**.
2. On the **Power Automate flows** page, select a flow to delete, then select **Delete** from the flow control menu.
3. In the deletion confirmation dialog box, select **Delete**.