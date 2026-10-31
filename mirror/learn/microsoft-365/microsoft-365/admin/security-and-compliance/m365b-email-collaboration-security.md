---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Email and collaboration security - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-email-collaboration-security?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: vpattnaik
author: vpattnai
manager: dansimp
audience: Admin
ms.topic: how-to
ms.service: m365-core
ms.subservice: security
ms.date: 2025-08-14T00:00:00.0000000Z
ms.localizationpriority: medium
ms.collection:
- M365-Campaigns
- m365solution-smb
- highpri
- m365-security
- tier2
- trust-pod
ms.custom:
- MiniMaven
- security
search.appverid:
- BCS160
- MET150
description: Get help with increasing the level of protection in Microsoft 365 Business Premium
locale: en-us
document_id: 4dd1a85a-037c-d632-c0a3-6cb90f7fc56d
document_version_independent_id: 4dd1a85a-037c-d632-c0a3-6cb90f7fc56d
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/security-and-compliance/m365b-email-collaboration-security.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/security-and-compliance/m365b-email-collaboration-security
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/security-and-compliance/m365b-email-collaboration-security.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/609dad7f-61d2-4958-9386-e6e4bb38d61e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/1af30562-083a-42e2-aad4-17ae29f4ad72
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 24d1505b-71cb-57c3-f1e0-ae4fd8ee736c
---

# Email and collaboration security - Microsoft 365 admin | Microsoft Learn

This article describes the configuration steps for email and collaboration you need to do in the earliest days of your Microsoft 365 for business organization.

Although your organization includes a default level of protection for email and collaboration from the moment you create it, the steps in this article give you an actionable plan to unleash the full protection capabilities of Microsoft 365. After you complete the steps, you can also use this article to show management that you're maximizing your investment in Microsoft 365.

## Requirements

[Built-in security features](/en-us/defender-office-365/eop-about) are included in *all* Microsoft 365 organizations with cloud mailboxes. Microsoft 365 Business Premium includes Microsoft Defender for Office 365 Plan 1 with more mail and collaboration protections. For detailed comparisons of the built-in security features for all cloud mailboxes and Defender for Office 365, see [Microsoft Defender for Office 365 overview](/en-us/defender-office-365/mdo-about).

### Roles and permissions

To configure email and collaboration protection features, you need permissions. The following table lists the permissions that allow you to do the procedures in this article:

| Role or role group | Learn more |
| --- | --- |
| Global Administrator in Microsoft Entra^\*^ | [Microsoft Entra built-in roles](/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) |
| Organization Management in Email & collaboration role groups | [Role groups in Microsoft Defender for Office 365](/en-us/defender-office-365/scc-permissions#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) |
| Security Administrator in Microsoft Entra | [Microsoft Entra built-in roles](/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |
| Security Administrator in Email & collaboration role groups | [Email & collaboration permissions in Microsoft Defender for Office 365](/en-us/defender-office-365/scc-permissions#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) |
| Exchange Online Organization Management | [Permissions in Exchange Online](/en-us/exchange/permissions-exo/permissions-exo) |
| SharePoint Administrator in Microsoft Entra | [About the SharePoint Administrator role in Microsoft 365](/en-us/sharepoint/sharepoint-admin-role) |

Important

^\*^ Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.

## Configure email authentication for your Microsoft 365 domains

Configure [SPF](/en-us/defender-office-365/email-authentication-spf-configure), [DKIM](/en-us/defender-office-365/email-authentication-dkim-configure), and [DMARC](/en-us/defender-office-365/email-authentication-dmarc-configure) records (in that order) for all custom Microsoft 365 domains (including parked domains and subdomains). If necessary, configure any [trusted ARC sealers](/en-us/defender-office-365/email-authentication-arc-configure).

For more information, see [Configure email authentication for your Microsoft 365 domains](/en-us/defender-office-365/mdo-deployment-guide#step-1-configure-email-authentication-for-your-microsoft-365-domains).

## Configure threat policies

Turn on and use the Standard and/or Strict [preset security policies](/en-us/defender-office-365/preset-security-policies) for all recipients. Or, if [business needs dictate](/en-us/defender-office-365/mdo-deployment-guide#determine-your-threat-policy-strategy), create and use custom threat policies instead, but check them periodically using the [configuration analyzer](/en-us/defender-office-365/configuration-analyzer-for-security-policies).

For more information, see [Configure threat policies](/en-us/defender-office-365/mdo-deployment-guide#step-2-configure-threat-policies).

### Identify priority accounts

Identify and tag the appropriate users in your organization as [priority accounts](../setup/priority-accounts) for easier identification in reports and investigations.

For more information, see [Priority accounts and user tags](/en-us/defender-office-365/mdo-deployment-guide#step-4-priority-accounts-and-user-tags).

## Review and configure user reported message settings

Use the [built-in Report button in Outlook](/en-us/defender-office-365/submissions-outlook-report-messages#use-the-built-in-report-button-in-outlook) or a [supported non-Microsoft tool](/en-us/defender-office-365/submissions-user-reported-messages-custom-mailbox#message-submission-format-for-non-microsoft-reporting-tools) so users can report false positives and false negatives in Outlook, and so those reported messages are available to admins on the **User-reported** tab of the **Submissions** page in the Defender portal. Configure the organization so reported messages go to a specified reporting mailbox, to Microsoft, or both (default).

For more information, see [Review and configure user reported message settings](/en-us/defender-office-365/mdo-deployment-guide#step-5-review-and-configure-user-reported-message-settings).

### Prepare for block and allow entries

Familiarize yourself with the procedures to block and allow messages, files, and URLs in the Microsoft Defender portal.

For more information, see [Block and allow entries](/en-us/defender-office-365/mdo-deployment-guide#step-6-block-and-allow-entries).

### Adjust sharing settings for SharePoint and OneDrive files and folders

By default, sharing levels are set to the most permissive level for both SharePoint and OneDrive. We recommend changing the default settings to better protect your business:

1. In the **Sharepoint admin center** at https://admin.microsoft.com/sharepoint, go to **Policies** &gt; **Sharing**. Or, to go directly to the **Sharing** page, use https://admin.microsoft.com/sharepoint?page=sharing.
2. On the **Sharing** page, configure the following settings:

    - **External sharing** section &gt; **Content can be shared with**: We recommend **Least permissive** for both **SharePoint** and **OneDrive** to prevent external sharing.
    - **File and folder links**section:
        - **Choose the type of link that's selected by default when users share files and folders in SharePoint and OneDrive**: Select **Specific people (only the people the user specifies**).
    - **Choose the permission that's selected by default for sharing links**: Select **View**.
    - **Other settings**: Verify the following settings are selected:
        - **Show owners the names of people who viewed their files in OneDrive**
        - **Let site owners choose to display the names of people who viewed files or pages in SharePoint**

    When you're finished on the **Sharing** page, select **Save**.

For more information, see [Manage sharing settings](/en-us/sharepoint/turn-external-sharing-on-or-off).

### Set up and review alert policies and alerts

Alert policies are useful for tracking user and admin activities, potential malware threats, and data loss incidents in your business. Your subscription includes a set of default policies, but you can also create custom policies. For example, if you store an important file in SharePoint that you don't want to share externally, you can create an alert policy to notify you if someone shares it.

1. In the Microsoft Defender portal at https://security.microsoft.com, go to **Email & collaboration** &gt; **Policies & rules** &gt; **Alert policy**. Or, to go directly to the **Alert policy** page, use https://security.microsoft.com/alertpoliciesv2.
2. On the **Alert policy** page, review the default policies:

    - Click on the **Name** column header to sort the alert policies by name.
    - Use ![](../../media/m365-cc-sc-filter-icon.png)**Filter** to filter the alert policies by **Category**.
    - Click on the **Name** value of a policy to open the details flyout for more information and notification options.
3. The alerts that result from alert policies are available on the **Alerts** page in the Defender portal at **Incidents & alerts** &gt; **Alerts** or directly at https://security.microsoft.com/alerts.

For more information, see [Alert policies in the Microsoft Defender portal](/en-us/defender-xdr/alert-policies) and [View alerts](/en-us/defender-xdr/alert-policies#view-alerts).

### Manage organization calendar sharing

You can help people share their calendars securely by limiting the level of detail they can share (for example, free/busy times only).

1. In the Microsoft 365 admin center at https://admin.microsoft.com, go to **Show all** &gt; **Settings** &gt; **Org settings** &gt; **Services** tab. If you don't see **Settings**, select **Show all**. Or, to go directly to the **Services** tab on the **Org settings** page, use https://admin.microsoft.com/#/Settings/Services.
2. On the **Services** tab on the **Org settings** page, select **Calendar**.
3. In the **Calendar** flyout that opens, configure the following settings:

    - **External sharing**section:
        - **Let your users share their calendars with people outside of your organization who have Office 365 or Exchange**: We recommend clearing this setting.

            [![Screenshot of showing external calendar sharing as not allowed.](../../media/nocalendarsharing.png)](../../media/nocalendarsharing.png#lightbox)

            If you leave this setting selected, **Allow anyone to access calendars with an email invitation** is also available. For this setting, we recommend **Show calendar free/busy information with time only**.

            [![Screenshot of calendar free/busy sharing with anyone.](../../media/sharefreebusy.png)](../../media/sharefreebusy.png#lightbox)

    When you're finished in the **Calendar** flyout, select **Save**.

If your users are allowed to share their calendars, see [Share your calendar in Outlook on the web](https://support.microsoft.com/office/7ecef8ae-139c-40d9-bae2-a23977ee58d5).