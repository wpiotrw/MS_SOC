---
layout: Conceptual
title: Create Insider Risk Management notice templates | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-notices
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Create notice templates in Microsoft Purview Insider Risk Management to send automated reminder or training emails when cases are created from policy matches and confirmed alerts.
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
- purview-compliance
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 2978a4ff-19cf-02c0-22df-673c1d5c241f
document_version_independent_id: 2978a4ff-19cf-02c0-22df-673c1d5c241f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-notices.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-notices
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-notices.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 82bb7c33-6777-9856-3960-333a578fd28d
---

# Create Insider Risk Management notice templates | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Insider Risk Management notice templates enable you to automatically send email messages to users when you create a case for risk activities that generate a policy match and confirmed alert. For most alerts that generate cases, user actions result from mistakes or inadvertent actions without ill intent. Use notices as simple reminders for users to be more careful, to provide links to information for refresher training, or to corporate policy resources. Notices can be an important part of your internal compliance training program and can help create a documented audit trail for users with recurring risk activities.

Create notice templates if you want to send users an email reminder notice for policy matches as part of the case resolution process. You can only send notices to the user email address associated with the specific case being reviewed. When selecting a notice template to apply to a policy match, you can choose to accept the field values defined in the template or overwrite the fields as needed.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Notice templates dashboard

The **Notices templates dashboard** displays a list of configured notice templates and lets you create new notice templates. The portal lists the notice templates in reverse date order with the most recent notice template listed first.

![Screenshot of the Notification templates dashboard in Insider Risk Management showing a list of configured notice templates.](media/insider-risk-notices-dashboard.png)

## HTML for notices

If you want to create more than a simple text-based email message for notifications, you can create a more detailed message by using HTML in the message body field of a notice template. The following example provides the message body format for a basic HTML-based email notification template:

```HTML
<!DOCTYPE html>
<html>
<body>
<h2>Action Required: Contoso User Code of Conduct Policy Training</h2>
<p>A recent activity you've performed has generated a risk alert prohibited by the Contoso User <a href='https://www.contoso.com'>Code of Conduct Policy</a>.</p>
<p>You are required to attend the Contoso User Code of Conduct <a href='https://www.contoso.com'>training</a> within the next 14 days. Please contact <a href='mailto:hr@contoso.com'>Human Resources</a> with any questions about this training request.</p>
<p>Thank you,</p>
<p><em>Human Resources</em></p>
</body>
</html>
```

Note

In Insider Risk Management notice templates, the HTML href attribute implementation currently supports only single quotation marks instead of double quotation marks for URL references.

## Create a new notice template

To create a new Microsoft Purview Insider Risk Management notice template, use the notice creation tool in the **Insider Risk Management** solution in the Microsoft Purview portal.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Notification templates** in the left navigation.
4. Select **Create notification template** to open the notice creation tool.
5. On the **New email notification template**page, complete the following fields:
    - **Template name**: Enter a friendly name for the notice. This name appears on the list of notices on the notice dashboard and in the notice selection list when sending notices from a case.
    - **Send from**: Enter the sender email address for the notice. This address appears in the **From:** field in all notices sent to users unless changed when sending a notice from a case.
    - **Subject**: Enter the information that appears in the subject line of the message. You can enter text values.
    - **Message body**: Enter the information that appears in the message body. You can enter text or HTML values.
6. Select **Create** to create and save the notice template.

## Update a notice template

To update an existing notice template, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Notification templates** in the left navigation.
4. In the **Email notification templates** list, select the notification template that you want to manage.
5. On the notice details page, select **Edit**.
6. On the **Edit**page, edit the following fields:
    - **Template name**: Enter a new friendly name for the notice. This name appears on the list of notices on the notice dashboard and in the notice selection list when sending notices from a case.
    - **Send from**: Update the sender email address for the notice. This address appears in the **From:** field in all notices sent to users unless changed when sending a notice from a case.
    - **Subject**: Update the information that appears in the subject line of the message. You can enter text characters.
    - **Message body**: Update the information that appears in the message body. You can enter text characters or HTML values.
7. Select **Save** to update and save the notice.

## Delete a notice template

To delete a notice template that you no longer need, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Notification templates** in the left navigation.
4. In the **Email notification templates** list, select the notification template that you want to delete.
5. Select the **Delete** icon on the toolbar.
6. Select **Yes**.