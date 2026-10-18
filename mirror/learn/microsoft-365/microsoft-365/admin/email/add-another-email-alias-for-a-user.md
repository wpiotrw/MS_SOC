---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Add another email alias for a user - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/email/add-another-email-alias-for-a-user?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2026-07-09T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier1
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- operations-pod
ms.custom:
- MSStore_Link
- AdminSurgePortfolio
- AdminTemplateSet
- business_assist
- user-accounts
description: Learn how you can add more than one email address, called an email alias to users in your Microsoft 365 organization.
locale: en-us
document_id: 94754a91-ac3b-9b1c-ded9-3fdab2dd229c
document_version_independent_id: 517f9726-1861-8b1c-fe9d-6c50047e16d3
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/email/add-another-email-alias-for-a-user.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/email/add-another-email-alias-for-a-user
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/email/add-another-email-alias-for-a-user.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 29cb93b3-4d99-fac4-307e-d606e6b33b62
---

# Add another email alias for a user - Microsoft 365 admin | Microsoft Learn

A primary email address in Microsoft 365 is usually the email address a user was assigned when their account was created. When the user sends email to someone else, their primary email address is what typically appears in the *From* field in email apps. They can also have more than one email address associated with their Microsoft 365 for business account. These additional addresses are called aliases. You can create up to 400 aliases for a user. No additional fees or licenses are required. This article is for Microsoft 365 administrators who have business subscriptions. It's not for home users.

For example, Jenna at your organization has the email address jenna@contosoco.com, but she also wants to receive email at jen@contosoco.com because some people refer to her by that name. You can create aliases for her so that email sent to both email addresses go to Jenna's inbox.

If you want multiple people to manage email sent to a single email address like info@contoso.com or sales@contoso.com, create a shared mailbox. Learn more at [Create a shared mailbox](create-a-shared-mailbox).

Note

This article is for Microsoft 365 administrators who have business subscriptions. It's not for home users.

## Before you begin

Managing email aliases for a user requires an Exchange-based administrative role, such as Exchange Administrator. For more info, see [About admin roles in the Microsoft 365 admin center](../add-users/about-admin-roles).

## Add email aliases to a user

1. In the admin center, go to the **Users** &gt; [Active users](https://go.microsoft.com/fwlink/p/?linkid=834822) page.
2. On the **Active Users** page, select the user you want to manage.
3. Under **Aliases** and select **Manage username and email**. You won't see this option if the person doesn't have a license assigned to them.
4. On the **Manage username and email** page, add the new alias in the **Username** field, select a domain and choose **Add**.

    Tip

    The email alias must end with a domain from the drop-down list. To add another domain name to the list, see [Add a domain to Microsoft 365](../setup/add-domain).
5. When you're done, choose **Save changes**. It can take up 24 hours for the new aliases to update.
6. The user will now have a primary address and an alias. For example, all mail sent to jenna@contoso.com, and her alias, jen@contoso.com, will go to Jenna's inbox. **When the user replies, the *From* address will depend on her Outlook client. Outlook on the web will use the alias at which the email was received. Outlook desktop will use her primary email alias.**

### Sending email from the proxy address easily

Your users can now send from their aliases when using Outlook on the web. When the `Set-OrganizationConfig -SendFromAliasEnabled $true` cmdlet is set, users within the organization will get access to a list of checkboxes where each entry corresponds to an alias in their Outlook settings. Selecting an alias will make it appear in the **From** dropdown in the **Compose** form.

## Troubleshooting

### Did you get "A parameter cannot be found that matches parameter name EmailAddresses" message?

If you get this error message it means that it's taking a bit longer to finish setting up your tenant, or your custom domain if you recently added one. The setup process can take up to 4 hours to complete. Wait a while so the setup process has time to finish, and then try again. If the problem persists, call Support and they will do a full sync for you.

### Did you get "This user is synchronized with your local Active Directory. Some details can be edited only through your local Active Directory" message?

If you get this error message, it means that you need to add the alias in your on-premises Active Directory. Open Active Directory Users and Computers (ADUC) and select the user account you would like to edit. Select **Properties** &gt; **Attribute Editor** &gt; **proxyAddresses** (if not visible, under ADUC's **View** menu, enable **Advanced Features**). Next, add the required alias, which should start with the all-lowercase prefix "smtp:" (for example, `smtp:jsmith@contoso.com`). Lastly, wait for the changes to sync to Microsoft Entra ID.

### Did you purchase your subscription from GoDaddy or another Partner?

If you purchased your subscription from GoDaddy or another Partner, to set the new alias as the primary, you can't set the new alias in the Microsoft 365 admin center. You must go to the GoDaddy/partner management console.