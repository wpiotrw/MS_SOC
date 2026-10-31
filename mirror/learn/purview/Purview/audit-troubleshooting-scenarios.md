---
layout: Conceptual
title: Search the audit log to investigate common support issues | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-troubleshooting-scenarios
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use the Microsoft 365 audit log search tool to investigate common email account issues, including compromised accounts and mailbox activities.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-03-30T00:00:00.0000000Z
audience: Admin
ms.topic: troubleshooting-general
ms.service: purview
ms.subservice: purview-audit
ms.collection:
- purview-compliance
- audit
search.appverid:
- MET150
- MOE150
ms.custom:
- seo-marvel-apr2020
- admindeeplinkEXCHANGE
- sfi-image-nochange
ai-usage: ai-assisted
locale: en-us
document_id: 6cd1021c-fe86-6af5-d835-84dac82ce2fd
document_version_independent_id: 6cd1021c-fe86-6af5-d835-84dac82ce2fd
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-troubleshooting-scenarios.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-troubleshooting-scenarios
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-troubleshooting-scenarios.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: c8779aa1-998c-ad99-c0aa-65a7440147fb
---

# Search the audit log to investigate common support issues | Microsoft Learn

This article describes how to use the audit log search tool to help you investigate common support issues. This guidance includes using the audit log to:

- Find the IP address of the computer used to access a compromised account
- Determine who set up email forwarding for a mailbox
- Determine if a user deleted email items in their mailbox
- Determine if a user created an inbox rule
- Investigate why there was a successful sign-in by a user outside your organization
- Search for mailbox activities performed by users with non-E5 licenses
- Search for mailbox activities performed by delegate users

## Use the audit log search tool

Each investigation scenario described in this article is based on using the audit log search tool in the [Microsoft Purview portal](purview-portal). This section lists the permissions required to search the audit log and describes the steps to access and run audit log searches. Each scenario section explains how to configure an audit log search query and what to look for in the detailed information in the audit records that match the search criteria.

### Permissions required to use the audit log search tool

To search the audit log, you must be assigned the *Audit Logs* or *View-Only Audit Logs* roles in Purview. By default, the *Audit Reader* and *Audit Manager* role groups on the **Role groups** page in the Microsoft Purview portal have these roles assigned.

To access audit cmdlets, you must be assigned the *Audit Logs* and *View-Only Audit Logs* roles in the Exchange admin center. By default, the *Compliance Management* and *Organization Management* role groups on the **Permissions page** in the Exchange admin center have these roles assigned.

For more information, see [Get started with auditing solutions](audit-get-started).

### Run audit log searches

For detailed guidance on how to run a search of the audit log, see [Search the audit log](audit-search).

## Find the IP address of the computer used to access a compromised account

Most audit records include the IP address for any user activity. The audit record also includes information about the client used.

To configure an audit log search query for this scenario, use the following settings:

- **Activities:** If relevant to your case, select a specific activity to search for. For investigating compromised accounts, consider selecting the **User signed in to mailbox** activity under **Exchange mailbox activities**. This selection returns auditing records that show the IP address used when signing in to the mailbox. Otherwise, leave this field blank to return audit records for all activities.

Tip

If you leave this field blank, the search returns **UserLoggedIn** activities, which is a Microsoft Entra activity that indicates that someone signed in to a user account. Use filtering in the search results to display the **UserLoggedIn** audit records.

- **Start date** and **End date:** Select a date range that's applicable to your investigation.
- **Users:** If you're investigating a compromised account, select the user whose account was compromised. This selection returns audit records for activities performed by that user account.
- **File, folder, or site:** Leave this field blank.

After you run the search, the IP address for each activity appears in the **IP address** column in the search results. Select the record in the search results to view more detailed information on the detail page.

## Determine who set up email forwarding for a mailbox

When you configure email forwarding for a mailbox, you forward email messages sent to that mailbox to another mailbox. You can forward messages to users inside or outside of your organization. When you set up email forwarding on a mailbox, use the underlying Exchange Online cmdlet **Set-Mailbox**.

To configure an audit log search query for this scenario, use the following settings:

- **Activities:** Leave this field blank so the search returns audit records for all activities. This setting is necessary to return any audit records related to the **Set-Mailbox** cmdlet.
- **Start date** and **End date:** Select a date range that's applicable to your investigation.
- **Users:** Unless you're investigating an email forwarding issue for a specific user, leave this field blank. This setting helps you identify if email forwarding was set up for any user.
- **File, folder, or site:** Leave this field blank.

After you run the search, select **Filter results** on the search results page. In the box under the **Activity** column header, type **Set-Mailbox** so only audit records related to the **Set-Mailbox** cmdlet are displayed.

![Filtering the results of an audit log search.](media/emailforwarding1.png)

You need to look at the details of each audit record to determine if the activity is related to email forwarding. Select the audit record to display the **Details** flyout page, and then select **More information**. The following screenshot and descriptions highlight the information that indicates email forwarding was set on the mailbox.

![Detailed information from the audit record.](media/emailforwarding2.png)

a. In the **ObjectId** field, the alias of the mailbox that email forwarding was set on is displayed. This mailbox also appears in the **Item** column in the search results page.

b. In the **Parameters** field, the value *ForwardingSmtpAddress* indicates that email forwarding was set on the mailbox. In this example, mail is being forwarded to the email address mike@contoso.com, which is outside of the alpinehouse.onmicrosoft.com organization.

c. The *True* value for the *DeliverToMailboxAndForward* parameter indicates that a copy of the message is delivered to sarad@alpinehouse.onmicrosoft.com *and* is forwarded to the email address specified by the *ForwardingSmtpAddress* parameter, which in this example is mike@contoso.com. If the value for the *DeliverToMailboxAndForward* parameter is set to *False*, then email is only forwarded to the address specified by the *ForwardingSmtpAddress* parameter. It's not delivered to the mailbox specified in the **ObjectId** field.

d. The **UserId** field indicates the user who set email forwarding on the mailbox specified in the **ObjectId** field. This user also appears in the **User** column on the search results page. In this case, it seems that the owner of the mailbox set email forwarding on the mailbox.

If you determine that email forwarding shouldn't be set on the mailbox, remove it by running the following command in Exchange Online PowerShell:

```powershell
Set-Mailbox <mailbox alias> -ForwardingSmtpAddress $null
```

For more information about the parameters related to email forwarding, see the [Set-Mailbox](/en-us/powershell/module/exchange/set-mailbox) article.

## Determine if a user deleted email items

Starting in January 2019, Microsoft turned on mailbox audit logging by default for all Office 365 and Microsoft 365 organizations. This change means that the system automatically logs certain actions that mailbox owners perform, and you can access the corresponding mailbox audit records when you search the mailbox audit log. Before this change, you had to manually enable mailbox audit logging for every user mailbox in your organization.

By default, the system logs mailbox actions that include the SoftDelete and HardDelete mailbox actions that mailbox owners perform. By using this audit logging, you can search the audit log for events related to deleted email items. For more information about mailbox auditing by default, see [Manage mailbox auditing](audit-mailboxes).

To configure an audit log search query for this scenario, use the following settings:

- **Activities:** Under **Exchange mailbox activities**, select one or both of the following activities:
- **Deleted messages from Deleted Items folder:** This activity corresponds to the **SoftDelete** mailbox auditing action. The audit log records this activity when a user deletes a message from the **Deleted Items** folder. It also records this activity when a user permanently deletes an item by selecting it and pressing **Shift+Delete**. After an item is permanently deleted, the user can recover it until the deleted item retention period expires.
- **Purged messages from mailbox:** This activity corresponds to the **HardDelete** mailbox auditing action. The audit log records this activity when a user purges an item from the **Recoverable Items** folder. Admins can use the search tool in the Microsoft Purview portal to search for and recover purged items until the deleted item retention period expires or longer if the user's mailbox is on hold.
- **Start date** and **End date:** Select a date range that's applicable to your investigation.
- **Users:** If you select a user in this field, the audit log search tool returns audit records for email items that the specified user deleted (SoftDeleted or HardDeleted). Sometimes the user who deletes an email isn't the mailbox owner.
- **File, folder, or site:** Leave this field blank.

After you run the search, you can filter the search results to display the audit records for soft-deleted items or for hard-deleted items. Select the audit record to display the **Details** flyout page, and then select **More information**. Additional information about the deleted item, such as the subject line and the location of the item when it was deleted, appears in the **AffectedItems** field. The following screenshots show an example of the **AffectedItems** field from a soft-deleted item and a hard-deleted item.

**Example of AffectedItems field for soft-deleted item**

![Audit record for soft-deleted item.](media/softdeleteditem.png)

**Example of AffectedItems field for hard-deleted item**

![Audit record for hard-deleted email item.](media/harddeleteditem.png)

### Recover deleted email items

Users can recover soft-deleted items if the deleted items retention period hasn't expired. In Exchange Online, the default deleted items retention period is 14 days, but admins can increase this setting to a maximum of 30 days. For instructions on recovering deleted items, see [Recover deleted items or email in Outlook on the web](https://support.office.com/article/Recover-deleted-items-or-email-in-Outlook-Web-App-C3D8FC15-EEEF-4F1C-81DF-E27964B7EDD4).

As previously explained, admins might be able to recover hard-deleted items if the deleted item retention period hasn't expired or if the mailbox is on hold. In this case, items are kept until the hold duration expires. When you run a content search, soft-deleted and hard-deleted items in the Recoverable Items folder appear in the search results if they match the search query. For more information about running content searches, see [Content Search in Office 365](ediscovery-content-search).

Tip

To search for deleted email items, search for all or part of the subject line that's displayed in the **AffectedItems** field in the audit record.

## Determine if a user created an inbox rule

When users create an inbox rule for their Exchange Online mailbox, the system saves a corresponding audit record to the audit log. For more information about inbox rules, see:

- [Use inbox rules in Outlook on the web](https://support.office.com/article/use-inbox-rules-in-outlook-on-the-web-8400435c-f14e-4272-9004-1548bb1848f2)
- [Manage email messages in Outlook by using rules](https://support.office.com/article/Manage-email-messages-by-using-rules-C24F5DEA-9465-4DF4-AD17-A50704D66C59)

To configure an audit log search query for this scenario, use the following settings:

- **Activities:** Under **Exchange mailbox activities**, select one or both of the following activities:
- **New-InboxRule Create new inbox rule from Outlook Web App**. This activity returns audit records when users create inbox rules by using Outlook web app or Exchange Online PowerShell.
- **Updated inbox rules from Outlook client**. This activity returns audit records when users create, modify, or remove inbox rules by using the Outlook desktop client.
- **Start date** and **End date:** Select a date range that's applicable to your investigation.
- **Users:** Unless you're investigating a specific user, leave this field blank. This approach helps you identify new inbox rules set up by any user.
- **File, folder, or site:** Leave this field blank.

After you run the search, the search results display any audit records for this activity. Select an audit record to display the **Details** flyout page, and then select **More information**. The **Parameters** field displays information about the inbox rule settings. The following screenshot and descriptions highlight the information about inbox rules.

![Audit record for new inbox rule.](media/newinboxrulerecord.png)

a. In the **ObjectId** field, the audit record displays the full name of the inbox rule. This name includes the alias of the user's mailbox (for example, SaraD) and the name of the inbox rule (for example, "Move messages from admin").

b. In the **Parameters** field, the audit record displays the condition of the inbox rule. In this example, the condition is specified by the *From* parameter. The value defined for the *From* parameter indicates that the inbox rule acts on email sent by admin@alpinehouse.onmicrosoft.com. For a complete list of the parameters that you can use to define conditions of inbox rules, see the [New-InboxRule](/en-us/powershell/module/exchange/new-inboxrule) article.

c. The *MoveToFolder* parameter specifies the action for the inbox rule. In this example, messages received from admin@alpinehouse.onmicrosoft.com are moved to the folder named *AdminSearch*. For a complete list of parameters that you can use to define the action of an inbox rule, see the [New-InboxRule](/en-us/powershell/module/exchange/new-inboxrule) article.

d. The **UserId** field indicates the user who created the inbox rule specified in the **ObjectId** field. The **User** column on the search results page also displays this user.

## Investigate why a user outside your organization successfully signed in

When you review audit records in the audit log, you might see records that show Microsoft Entra ID authenticated an external user who successfully signed in to your organization. For example, an admin in contoso.onmicrosoft.com might see an audit record showing that a user from a different organization (for example, fabrikam.onmicrosoft.com) successfully signed in to contoso.onmicrosoft.com. Similarly, you might see audit records that show users with a Microsoft Account (MSA), such as an Outlook.com or Live.com, successfully signed in to your organization. In these situations, the audited activity is **User logged In**.

This behavior is by design. Microsoft Entra ID, the directory service, supports *pass-through authentication* when an external user tries to access a SharePoint site or a OneDrive location in your organization. When the external user tries to access the resource, they're prompted to enter their credentials. Microsoft Entra ID uses the credentials to authenticate the user, so only Microsoft Entra ID verifies that the user is who they say they are. The indication of the successful sign-in in the audit record comes from Microsoft Entra authenticating the user. The successful sign-in doesn't mean that the user accessed any resources or performed any other actions in your organization. It only shows that Microsoft Entra ID authenticated the user. For a pass-through user to access SharePoint or OneDrive resources, a user in your organization must explicitly share a resource with the external user by sending them a sharing invitation or anonymous sharing link.

Note

Microsoft Entra ID supports pass-through authentication only for *first-party applications*, such as SharePoint Online and OneDrive for Business. It doesn't support pass-through authentication for other third-party applications.

Here's an example and descriptions of relevant properties in an audit record for a **User logged In** event that results from pass-through authentication. Select the audit record to display the **Details** flyout page, and then select **More information**.

![Example of audit record for successful pass-thru authentication.](media/passthroughauth1.png)

a. This field shows that the user who tried to access a resource in your organization isn't found in your organization's Microsoft Entra ID.

b. This field shows the UPN of the external user that tried to access a resource in your organization. This user ID also appears in the **User** and **UserId** properties in the audit record.

c. The **ApplicationId** property shows the application that triggered the sign-in request. The value of `00000003-0000-0ff1-ce00-000000000000` displayed in the **ApplicationId** property in this audit record indicates SharePoint Online. OneDrive for Business also has this same **ApplicationId**.

d. This field shows that the pass-through authentication succeeded. In other words, Microsoft Entra ID successfully authenticated the user.

e. The **RecordType** value of **15** shows that the audited activity (UserLoggedIn) is a Secure Token Service (STS) sign-in event in Microsoft Entra ID.

For more information about the other properties displayed in a UserLoggedIn audit record, see the Microsoft Entra related schema information in [Office 365 Management Activity API schema](/en-us/office/office-365-management-api/office-365-management-activity-api-schema#azure-active-directory-base-schema).

Here are two example scenarios that result in a successful **User logged in** audit activity because of pass-through authentication:

- A user with a Microsoft Account (such as SaraD@outlook.com) tries to access a document in a OneDrive for Business account in fourthcoffee.onmicrosoft.com and there's no corresponding guest user account for SaraD@outlook.com in fourthcoffee.onmicrosoft.com.
- A user with a Work or School account in an organization (such as pilarp@fabrikam.onmicrosoft.com) tries to access a SharePoint site in contoso.onmicrosoft.com and there's no corresponding guest user account for pilarp@fabrikam.com in contoso.onmicrosoft.com.

### Tips for investigating successful sign-ins resulting from pass-through authentication

- Search the audit log for activities performed by the external user identified in the **User logged in** audit record. Type the UPN for the external user in the **Users** box and use a date range if relevant to your scenario. For example, you can create a search using the following search criteria:

    ![Search for all activities performed by the external user.](media/audit-pass-thru-authentication.png)

    In addition to the **User logged in** activities, you might see other audit records, such as records that indicate a user in your organization shared resources with the external user and whether the external user accessed, modified, or downloaded a document that was shared with them.
- Search for SharePoint sharing activities that indicate a file was shared with the external user identified by a **User logged in** audit record. For more information, see [Use sharing auditing in the audit log](audit-log-sharing).
- Export the audit log search results that contain records relevant to your investigation so that you can use Excel to search for other activities related to the external user. For more information, see [Export, configure, and view audit log records](audit-log-export-records).

## Search for mailbox activities performed by users with non-E5 licenses

Even when [mailbox auditing on by default](audit-mailboxes) is turned on for your organization, you might notice that mailbox audit events for some users don't appear in audit log searches by using the Microsoft Purview portal, the **Search-UnifiedAuditLog** cmdlet, or the Office 365 Management Activity API. The reason for this behavior is that mailbox audit events return only for users with E5 licenses when you use one of the previous methods to search the unified audit log.

To retrieve mailbox audit log records for non-E5 users, use one of the following workarounds:

- Manually enable mailbox auditing on individual mailboxes (run the `Set-Mailbox -Identity <MailboxIdentity> -AuditEnabled $true` command in Exchange Online PowerShell). After you enable mailbox auditing, search for mailbox audit activities by using the Microsoft Purview portal, the **Search-UnifiedAuditLog** cmdlet, or the Office 365 Management Activity API.

    Note

    If mailbox auditing already appears to be enabled on the mailbox, but your searches return no results, change the value of the *AuditEnabled* parameter to `$false` and then back to `$true`.

## Search for mailbox activities performed in a specific mailbox (including shared mailboxes)

When you use the **Users** dropdown list in the audit log search tool in the Microsoft Purview portal or the **Search-UnifiedAuditLog -UserIds** command in Exchange Online PowerShell, you can search for activities performed by a specific user. For mailbox audit activities, this type of search finds activities performed by the specified user. It doesn't guarantee that the search results include all activities performed in the same mailbox. For example, an audit log search doesn't return audit records for activities performed by a delegate user because searching for mailbox activities performed by a specific user doesn't return activities performed by a delegate user who has been assigned permissions to access another user's mailbox. A delegate user is someone who is assigned the SendAs, SendOnBehalf, or FullAccess mailbox permission to another user's mailbox.

Also, using the **User** dropdown list in the audit log search tool or the **Search-UnifiedAuditLog -UserIds** doesn't return results for activities performed in a shared mailbox.

To search for the activities performed in a specific mailbox or to search for activities performed in a shared mailbox, use the following syntax when running the **Search-UnifiedAuditLog** cmdlet:

```powershell
Search-UnifiedAuditLog -StartDate <date> -EndDate <date> -FreeText (Get-Mailbox <mailbox identity).ExchangeGuid
```

For example, the following command returns audit records for activities performed in the Contoso Compliance Team shared mailbox between August 2020 and October 2020:

```powershell
Search-UnifiedAuditLog -StartDate 08/01/2020 -EndDate 10/31/2020 -FreeText (Get-Mailbox complianceteam@contoso.onmicrosoft.com).ExchangeGuid
```