---
layout: Conceptual
monikers:
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Migrate business email and calendar from Google Workspace - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/moveto-microsoft-365/migrate-email?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: heidip
author: MicrosoftHeidi
manager: dansimp
ms.date: 2026-09-25T00:00:00.0000000Z
audience: Admin
ms.topic: upgrade-and-migration-article
ms.service: m365-core
ms.subservice: migration
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- highpri
- M365-subscription-management
- Adm_O365
ms.custom:
- VSBFY23
- AdminSurgePortfolio
- adminvideo
- admindeeplinkMAC
search.appverid:
- BCS160
- MET150
- MOE150
description: Learn how to migrate email, contacts, and calendar from Google Workspace to Microsoft 365 for business.
ai-usage: ai-assisted
locale: en-us
document_id: 3bd31a7b-580e-dc50-ed21-f1513cc44d09
document_version_independent_id: 3bd31a7b-580e-dc50-ed21-f1513cc44d09
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/moveto-microsoft-365/migrate-email.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/moveto-microsoft-365/migrate-email
moniker_range_name: 2ccba01628bf08e8f21ea76d73b162e1
monikers:
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/moveto-microsoft-365/migrate-email.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/86a4b315-a9f1-4577-b985-6fb0e0e67420
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/96ac410d-d052-4707-8007-df31dd0fe041
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 85f50405-e739-92ee-dc10-ef9aa63888f1
---

# Migrate business email and calendar from Google Workspace - Microsoft 365 admin | Microsoft Learn

Note

The videos and content in this article provide a high-level overview of using an automated batch migration in the Exchange admin center to migrate your users' email, contacts, and calendars from Google Workspace. Use the linked resources for detailed instructions.

## Automated batch migration overview

Watch this video and find more on the [Microsoft 365 small business YouTube channel](https://go.microsoft.com/fwlink/?linkid=2198034).

You can use the batch migration tool in the Exchange admin center to migrate email, contacts, and calendars from Google Workspace to Microsoft 365. With it, you can:

- Keep both environments active.
- Migrate groups of email users to Microsoft 365 over time.
- Close your Google Workspace environment when you're done moving your business.

## Recommendations for migrating from Google Workspace

- An *automated* batch migration does some of the migration tasks for you, so it's recommended over the *manual* batch migration. For more detailed information, see [Perform a Google Workspace migration to Microsoft 365](/en-us/exchange/mailbox-migration/perform-g-suite-migration).

    Note

    You can also migrate your email from Google Workspace to Microsoft 365 through an [IMAP migration](/en-us/exchange/mailbox-migration/migrating-imap-mailboxes/migrate-g-suite-mailboxes). You should compare methods to determine which is more suitable for migrating your email.
- It's recommended that you [get help from Microsoft](/en-us/microsoft-365/admin/get-help-support) or from a [partner](https://marketplace.microsoft.com/en-us/marketplace/partner-dir) when planning to migrate with either of the above methods.
- If you're a VSB (very small business) where you have a few users, you should migrate your email using a different method, such as [importing to Outlook through a PST file](https://support.microsoft.com/en-us/outlook/import-email-contacts-and-calendar-from-an-outlook-pst-file).

## Prerequisites for automated batch migration from Google Workspace

To successfully use the automated batch migration tool, it's important to correctly complete all of the prerequisite tasks. For more detailed information, see [Google Workspace migration prerequisites](/en-us/exchange/mailbox-migration/google-workspace-migration-prerequisites).

In Exchange Online, the administrator performing these steps must have at least the **Recipient Management** role group.

These tasks include:

- Creating a subdomain to correctly route email to users who were migrated to Microsoft 365.
- Creating a subdomain to correctly route email from users you migrated to Microsoft 365 back to users who are in your Google Workspace environment.
- Preparing the destination email accounts.
- Verifying that the Google migration administrator has the required Google Cloud IAM roles and that a Google Workspace super administrator can authorize domain-wide delegation.

Note

Completing the prerequisite tasks might require you to sign in to your domain host to create subdomains and update DNS records. If you aren't comfortable doing this, seek assistance.

### Create a subdomain for email going to Microsoft 365

1. Go to the **Google Workspace admin** console.
2. Select **Add a domain**.
3. Enter a domain name for your subdomain, such as *m365.contoso.com*.
4. Select **User alias domain**, select **Add domain and start verification**, and then select **Continue**. Follow the instructions to verify domain ownership.

    Domain verification usually takes just a few minutes, but it can take up to 48 hours.
5. Go to the **Microsoft 365 admin center**.
6. In the Microsoft 365 admin center, in the left nav, select **Show all**, select **Settings**, select **Domains**, and then **Add domain**.
7. Enter the subdomain you previously created, then select **Use this domain**.
8. To connect the domain, select **Continue**.
9. Select **Add DNS records**. Depending on your domain host provider, Microsoft 365 tries to update your DNS records for the domain.
10. When complete, select **Done**.

### Create a subdomain for mail routing to Google Workspace

1. Return to the **Google Workspace admin** console.
2. Select **Add a domain**.
3. Enter a domain name for your subdomain, such as *gsuite.contoso.com*.
4. Select **User alias domain**, select **Add domain and start verification**, and then select **Continue**. Follow the instructions to verify domain ownership.
5. At your DNS host, add the current Google Workspace MX record for this routing subdomain. See [Set up MX records for Google Workspace](https://support.google.com/a/answer/140034).

    DNS changes can take up to 72 hours to be recognized.

Before starting a batch, allow the required forwarding in [Google Workspace](https://knowledge.workspace.google.com/admin/gmail/let-users-automatically-forward-their-own-gmail-emails) and [Exchange Online](/en-us/defender-office-365/outbound-spam-policies-external-email-forwarding). Exchange outbound spam policies, Remote Domain settings, and mail flow rules can each block forwarding. Any exception needs your security administrator's approval.

### Prepare mail user accounts

Mail users are Microsoft 365 accounts whose email is hosted externally. Use these steps to create new mail users. If accounts already exist, follow the [Exchange recipient prerequisites](/en-us/exchange/mailbox-migration/google-workspace-migration-prerequisites) before creating additional accounts.

1. In the Exchange admin center, select **Recipients** &gt; **Contacts**, then **Add a mail user**.
2. On the **Set up the basic information** page, enter the user's name, display name, alias, user ID, and password.

    - For **External email address**, enter the person's complete Google routing address, such as `adeyoung@gsuite.contoso.com`.
    - For **User ID** and **Domain**, use the planned username and verified business domain, such as `adeyoung@contoso.com`.
    - Enter and confirm a password that meets your organization's requirements.
3. Select **Next**. On **Review mail user**, check the details, then select **Create**.
4. On **Status**, wait for creation to finish, then select **Done**.

For details, see [Manage mail users in Exchange Online](/en-us/exchange/recipients-in-exchange-online/manage-mail-users).

### Add Microsoft 365 routing aliases to mail users

For each mail user, add a proxy address for the Microsoft 365 routing domain.

1. In the Exchange admin center, select **Recipients** &gt; **Contacts**. Select the display name of the entry with **Contact type** **MailUser**.
2. On **Others**, under **Email addresses**, select **Manage email address types**.
3. Add an **SMTP** proxy address using the person's alias and Microsoft 365 routing domain, such as `adeyoung@m365.contoso.com`.
4. Save the address changes, and repeat for the other mail users.

### Verify that your Google migration administrators have the required permissions

The account that creates the Google Cloud project and service account needs these Google Cloud IAM roles:

- Project creator
- Service Account Creator

Creating the JSON key also requires **Service Account Key Admin** or equivalent permissions and an organization policy that permits key creation. See [Create and delete service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete). Ask your Google Cloud administrator to resolve a policy block for the migration project.

Domain-wide delegation is a separate Google Workspace authorization. A Google Workspace super administrator must authorize the API client and OAuth scopes.

## Migrate your email, contacts, and calendars from Google Workspace

After successfully completing all the prerequisites, you can now use the batch migration tool to migrate your users from Google Workspace to Microsoft 365. Here's a summary of the required steps. For more detailed information, see [Perform an automated Google Workspace migration to Microsoft 365](/en-us/exchange/mailbox-migration/automated-migration-neweac).

Important

Review the [migration limitations](/en-us/exchange/mailbox-migration/perform-g-suite-migration#migration-limitations) and the [Default MRM Policy and archival guidance](/en-us/exchange/mailbox-migration/automated-migration-neweac) before starting a batch. The archival guidance isn't an instruction to remove legal holds.

1. In the Exchange admin center, select **Migration**.
2. On the **Migration batches** page, select **Add migration batch**.
3. Give the migration batch a unique name, and from the **Select the mailbox migration path** menu, select **Migration to Exchange Online**. Then select **Next**.
4. For the **Migration type**, select **Google Workspace (Gmail) migration**. Then select **Next**.
5. On the **Prerequisites for Google Workspace migration** page, select **Start**.
6. Sign in with your Google admin account and password.
7. On the **EAC Migration wants access to your Google Account** page, select **Continue**.
8. EAC Migration involves four required tasks in Google Workspace that are needed for migration.
9. When all four tasks are complete, note the **ClientID** and **Scope** values. Then select **Link**.
10. On the **API Clients** page, select **Add new**.
11. Copy the **ClientID** and **Scope** values from the migration page, and paste them into the corresponding fields (**Client ID** and **OAuth scopes**) on the **Add a new client** page. Then select **Authorize**.
12. On the **Prerequisites for Google Workspace migration** page, select **Next**.
13. On the **Set a migration endpoint** page, select **Create a new migration endpoint**, then **Next**.
14. Enter a unique **Migration endpoint name**, and use the default values for **Maximum concurrent migrations** and **Maximum concurrent incremental syncs**, then select **Next**.
15. On the **Gmail migration configuration** page, enter the email address of the Google admin account you're using to perform the migration.
16. Select **Import JSON** and then browse to the location where the JSON key file was created and downloaded to your local computer. The JSON key file was created during the automated tasks configuration part of the migration (step 8) and should be found in your local **Downloads** folder. Select the file, select **Open**, and then **Next**.
17. Create a CSV file with a list of the mailboxes you want to migrate. Make sure the file follows this format:

    ```CSV
     EmailAddress
     adeyoung@contoso.com
     awilber@contoso.com
    ```
18. On the **Add user mailboxes** page, select **Import CSV file**, and then choose the CSV file containing the users' email addresses. Select **Next**.
19. On the **Move configuration** page, enter the target delivery domain you created for routing email to Microsoft 365, such as *m365.contoso.com*. Then select **Next**.
20. On the **Schedule batch migration page**, you can:

    1. Enter the email address of people you want a report to be sent.
    2. Select how you want the batch to be started (manually, automatically, or at a specific time and date).
    3. Select how you want the batch to be ended (manually, automatically, or at a specific time and date).
21. Select **Save**, then **Done** when the batch has been created.
22. In the Exchange admin center, select **Migration**. On the **Migration batches** page, you can see the status of your batch migration.
23. After the batch starts and mail users are converted to mailboxes, assign their Exchange licenses within 30 days. See [batch completion and licensing](/en-us/exchange/mailbox-migration/completion-gspace-migration-batch-neweac).
24. When the batch shows **Synced**, select **Complete migration batch**, then **Confirm**.
25. Wait for the batch to show **Completed**.
26. Have migrated users check that their email, contacts, and calendars migrated successfully.

After all batches are complete, [connect the primary domain to Microsoft 365](connect-domain-tom365) to change its production MX records.