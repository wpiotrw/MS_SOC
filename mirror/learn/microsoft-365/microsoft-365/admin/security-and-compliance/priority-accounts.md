---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Manage and monitor priority accounts - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/priority-accounts?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- CSH
ms.author: deniseb
author: denisebmsft
manager: dansimp
ms.date: 2026-08-12T00:00:00.0000000Z
ai-usage: ai-assisted
audience: Admin
ms.topic: how-to
ms.service: m365-core
ms.subservice: security
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- Adm_O365
- Adm_TOC
- trust-pod
ms.custom:
- AdminSurgePortfolio
- admindeeplinkMAC
description: Admins can learn how to tag users as priority accounts, and about the extra protection and monitoring features priority accounts get.
locale: en-us
document_id: 55b2a404-0c8f-b434-65ce-68416ffd8bd3
document_version_independent_id: 55b2a404-0c8f-b434-65ce-68416ffd8bd3
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/security-and-compliance/priority-accounts.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/security-and-compliance/priority-accounts
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/security-and-compliance/priority-accounts.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/609dad7f-61d2-4958-9386-e6e4bb38d61e
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/1af30562-083a-42e2-aad4-17ae29f4ad72
platformId: 5e8611fd-fc3d-ddd3-3ccb-6a70d8970608
---

# Manage and monitor priority accounts - Microsoft 365 admin | Microsoft Learn

Every Microsoft 365 organization contains essential users like executives, leaders, managers, administrators, or others who have access to sensitive, proprietary, or high priority information, or who are influential in your organization. You can designate up to 250 of these users as *priority accounts* and (depending on your subscription) use app-specific features that give them extra protection, visibility, and priority.

This article describes how to tag users and groups as priority accounts, and the extra protections, visibility, and priority they receive.

Tip

For security best practices for high value accounts, see [Security recommendations for priority accounts in cloud organizations](/en-us/defender-office-365/priority-accounts-security-recommendations).

## Benefits of priority accounts

Tagging a user as a priority account enables the following features for that user. Availability depends on your subscription and, for the Exchange Online features, on the size of your organization.

| Feature | Description | Requirements |
| --- | --- | --- |
| Reporting in Microsoft Defender for Office 365 | Filter alerts, reports, and investigations to priority accounts. | Defender for Office 365 Plan 1 or Plan 2 |
| Priority account protection | Applies other heuristics that are specifically tailored to company executives. Turned on by default. | Defender for Office 365 Plan 2 |
| Exchange Online priority account monitoring | Shows mailbox health for scenarios like licensing, mailbox storage, message limits, and mail delivery. | At least 5,000 qualifying licenses **and** at least 50 monthly active users. For more information, see Monitor priority accounts. |
| Premium Mail Flow Monitoring | Alerts you when failed or delayed email exceeds a threshold. You configure the threshold and the alerts. | At least 5,000 qualifying licenses **and** at least 50 monthly active users. For more information, see Monitor priority accounts. |
| Priority feedback in Copilot Chat | Feedback is flagged and moved to the front of the triage queue to ensure your most important users are heard first. | Allow users to submit feedback and include log files and relevant content samples. For more information, see [Manage Microsoft feedback for your organization](/en-us/privacy/microsoft-365/feedback/feedback-manage). |

## What do you need to know before you begin?

- The maximum number of priority accounts is 250.
- You need to be assigned permissions before you can do the procedures in this article. You have the following options:

    - [Microsoft Defender XDR Unified role based access control (RBAC)](/en-us/defender-xdr/manage-rbac) (If **Email & collaboration** &gt; **Defender for Office 365** permissions is ![](../../media/scc-toggle-on.png)**Active**. Affects the Defender portal only, not PowerShell): **Authorization and settings/System settings/manage** or **Authorization and settings/System settings/Read-only**.
    - [Email & collaboration permissions in the Microsoft Defender portal](/en-us/defender-office-365/scc-permissions):

        - *Apply and remove the Priority account tag from users*: Membership in the **Security Administrator** and **Exchange Admin** role groups.
    - [Microsoft Entra permissions](/en-us/entra/identity/role-based-access-control/manage-roles-portal): Membership in the **Global Administrator**^\*^ or **Security Administrator** roles gives users the required permissions *and* permissions for other features in Microsoft 365.

Important

^\*^ Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that you should limit to emergency scenarios when you can't use an existing role.

## Manage priority accounts

You can manage priority accounts in the Microsoft 365 admin center, Microsoft Defender portal, or by using PowerShell.

### Manage priority accounts in the Microsoft admin center

1. In the Microsoft admin center at [https://admin.cloud.microsoft](https://go.microsoft.com/fwlink/p/?linkid=2024339), go to the **Priority accounts** page at https://admin.microsoft.com/Adminportal/Home#/priorityaccounts.

    If you prefer the long way, go to **Users** &gt; **Active users** &gt; on the **Active users** page, select ![](../../media/m365-cc-sc-more-actions-icon.png)**More actions** &gt; ![](../../media/m365-cc-sc-medal.png)**Manage priority accounts**.
2. On the **Priority accounts** page, take either of the following actions:

    - **Add members**:

        1. Select ![](../../media/m365-cc-sc-create-icon.png)**Tag accounts**. In the **Tag user accounts as priority** flyout that opens, select one of the following values in **How would you like to search for accounts?**:

            - **Name and email address** (default)
            - **Job title**
            - **Distribution list**

            When you're finished, select **Next**.
        2. In the flyout that opens, find and select the users or distribution groups, and then select **Tag**.
        3. The process starts over on the **Tag user accounts as priority** flyout with the **Priority accounts tagged** total updated (the maximum is 250). Select **Next** to tag more users or distribution groups, or select **Cancel** to finish.

            Back on the **Priority accounts** page, the users or groups you select are listed.
    - **Remove members**: In the list of members on the **Priority accounts** page, do either of the following steps:

        1. Select one or more entries from the list by selecting the check box next to the **Display name** column, select the ![](../../media/m365-cc-sc-minus.png)**Remove tag** action that appears, and then select **Remove** in the confirmation dialog that appears.
        2. Between the **Display name** and **Username** column values of an entry, select **⋮** **More actions** &gt; ![](../../media/m365-cc-sc-minus.png)**Remove tag**, and then select **Remove** in the confirmation dialog that appears.

### Manage priority accounts in the Microsoft Defender portal

1. In the Microsoft Defender portal at https://security.microsoft.com, go to **Settings** &gt; **Email & collaboration** &gt; **User tags**. Or, to go directly to the **User tags** page, use https://security.microsoft.com/securitysettings/userTags.
2. On the **User tags** page, select and edit the **Priority account** tag by using one of the following methods:

    - Select the check box next to the first column of the **Priority account** row, and then select the ![](../../media/m365-cc-sc-edit-icon.png)**Edit** action.
    - Select any area in the **Priority account** row other than the check box. In the details flyout that opens, select ![](../../media/m365-cc-sc-edit-icon.png)**Edit** at the top of the flyout.
3. The **Edit tag Priority account** wizard opens. On the **Assign members** page, take one of the following actions:

    - **Add members**: Use one of the following methods:

        - Select ![](../../media/m365-cc-sc-create-icon.png)**Add members**. In the **Add members** flyout that opens, add individual users or groups in the **Search users and groups to add** box by using any of the following methods:

            - Select the box and scroll through the list.
            - Start typing a name to filter the list, and then select the value in the list.

            To add more members, select an empty area in the box and repeat the previous step.

            To remove individual entries from the box, select ![](../../media/m365-cc-sc-remove-selection-icon.png) next to the entry.

            When you're finished in the **Add members** flyout, select **Add**.

            Back on the **Assign members** page, the users and groups that you added are listed by **Name** and **Type**.
        - Select ![](../../media/m365-cc-sc-download-icon.png)**Import** to select a text file that contains the email addresses of the users or groups (one entry per line).
        - **Remove members**: In the list of members on the **Assign members** page, select ![](../../media/m365-cc-sc-delete-icon.png)**Delete** in the entry row.

        When you're finished on the **Assign members** page, select **Next**.
4. On the **Review tag** page, review your settings. You can select **Edit** in each section to modify the settings within the section. Or you can select **Back** or the specific page in the wizard.

    When you're finished on the **Review tag** page, select **Submit**.
5. On the **Tag Priority account updated** page, select the links to add a new tag or manage the tag members.

    When you're finished on the **New tag created** page, select **Done**.

    Tip

    It can take up to eight hours to completely apply tags.

### Manage priority accounts in PowerShell

To manage priority accounts in [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell), use the following commands:

- To view the list of priority accounts, run the following command:

    ```powershell
    Get-User -IsVIP | Select-Object Identity
    ```
- To add a user to the list of priority accounts, replace `<Identity>` with the user's email address, and then run the following command:

    ```powershell
    Set-User -VIP $true -Identity <Identity> -Confirm:$false
    ```
- To remove a user from the list of priority accounts, replace `<Identity>` with the user's email address, and then run the following command:

    ```powershell
    Set-User -VIP $false -Identity <Identity> -Confirm:$false
    ```

For detailed syntax and parameter information, see [Get-User](/en-us/powershell/module/exchangepowershell/get-user) and [Set-User](/en-us/powershell/module/exchangepowershell/set-user).

## Monitor priority accounts

After you tag users or groups as priority accounts, they get the following protections and visibility in Microsoft 365:

- **Visibility in reporting in Microsoft Defender for Office 365 Plan 1 or Plan 2**: Microsoft 365 Business Premium and other subscriptions that include Defender for Office 365 (for example, Microsoft 365 E5 or an add-on subscription) support priority accounts as tags in filters in alerts, reports, and investigations. For more information, see [User tags in Microsoft Defender for Office 365](../../security/office-365-security/user-tags-about).
- **Priority account protection in Defender for Office 365 Plan 2**: A natural question is, "Aren't all users a priority? Why not designate all users as priority accounts for priority account protection?" Yes, all users are a priority, but priority account protection in Defender for Office 365 Plan 2 (for example, in Business Premium with the [Microsoft Defender Suite for Business Premium add-on](add-defender-suite-business-premium)) offers the following benefits:

    - **Other heuristics**: Our analysis of mail flow in the Microsoft datacenters indicates that mail flow patterns for company executives are different than the average user. Priority account protection offers other heuristics specifically tailored to company executives that don't benefit regular users.
    - **Extra visibility in reporting**: Priority account protection as a filter allows you to specifically target your investigations.

    For more information, see [Configure and review priority account protection in Microsoft Defender for Office 365](/en-us/defender-office-365/priority-accounts-turn-on-priority-account-protection).

    Tip

    When you apply priority account protection to a mailbox, you should also apply priority account protection to users with access to the mailbox. For example, the CEO and their executive assistant.
- **Email monitoring in Exchange Online**: Email monitoring features for priority accounts have the following requirements:

    - At least 5,000 licenses in any combination of the following products:

        - Office 365 E3
        - Microsoft 365 E3
        - Office 365 E5
        - Microsoft 365 E5

        For example, your organization has 3,000 Office 365 E3 licenses and 2,500 Microsoft 365 E5 licenses, for a total of 5,500 licenses from the qualifying products.
    - At least 50 monthly active users for one or more core workloads:

        - Microsoft Teams
        - OneDrive
        - SharePoint
        - Exchange Online
        - Microsoft 365 productivity apps

    If your organization meets **both of these requirements**, you can use the following email monitoring features for priority accounts:

    - **Exchange Online priority account monitoring**: You can view health of priority accounts for scenarios like Exchange licensing, mailbox storage, message limit, and mail delivery. For more information, see [Priority accounts monitoring scenarios](/en-us/microsoft-365/enterprise/microsoft-365-exchange-monitoring#priority-accounts-monitoring-scenarios).
    - **Premium Mail Flow Monitoring**: Healthy mail flow can be critical to business success, and delivery delays or failures can have a negative effect on the business. You can choose a threshold for failed or delayed emails, receive alerts when that threshold is exceeded, and view a report of email issues for priority accounts. For more information, see [Email issues for priority accounts report in the new EAC](/en-us/exchange/monitoring/mail-flow-reports/mfr-email-issues-for-priority-accounts-report).

## More information

[Using Priority Accounts in Microsoft 365](https://techcommunity.microsoft.com/t5/microsoft-365-blog/using-priority-accounts-in-microsoft-365/ba-p/1873314)