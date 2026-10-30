---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Connect your DNS records at IONOS to Microsoft 365 - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-ionos-com?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- CSH
ms.author: frankroj
author: frankroj
manager: dansimp
ms.date: 2026-04-23T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: m365-core
ms.subservice: domains
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_NonTOC
- Adm_O365_Setup
- operations-pod
ms.custom:
- AdminSurgePortfolio
- domains
search.appverid:
- BCS160
- MET150
- MOE150
ms.assetid: 5762c3ca-1de2-4999-bfe5-4c5e25a8957e
description: Learn to verify your domain and set up DNS records for email, Microsoft Teams Online, and other services at IONOS for Microsoft.
locale: en-us
document_id: 94b814d9-0ee8-b196-fb76-be23100d0d38
document_version_independent_id: ad2503a5-998d-bfce-8686-afa2e7f1e68d
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/dns/create-dns-records-at-ionos-com.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/dns/create-dns-records-at-ionos-com
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/dns/create-dns-records-at-ionos-com.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: efb09903-1d0d-5aa7-695f-957c51655ac8
---

# Connect your DNS records at IONOS to Microsoft 365 - Microsoft 365 admin | Microsoft Learn

**[Check the Domains FAQ](../setup/domains-faq)** if you don't find what you're looking for.

If IONOS is your DNS hosting provider, follow the steps in this article to verify your domain and set up DNS records for email, Microsoft Teams Online, and so on.

Tip

Some configuration tasks might be complex to perform. For technical support, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. At the bottom right, select **Help & Support**.
3. In the **Support Assistant** pane that opens, enter your question.
4. Review the results. If you still have questions, select **Contact support**.

To learn about your options for contacting support, see [Get support for Microsoft 365 for business](/en-us/microsoft-365/admin/get-help-support).

## Before you begin

You have two options for setting up DNS records for your domain:

- **Use Domain Connect** If you haven't set up your domain with another email service provider, use the Domain Connect steps to automatically verify and set up your new domain to use with Microsoft 365.

    OR
- **Use the manual steps** Verify your domain using the following manual steps and choose when and which records to add to your domain registrar. This allows you to set up new MX (mail) records, for example, at your convenience.

## Use Domain Connect to verify and set up your domain

Follow these steps to automatically verify and set up your IONOS domain with Microsoft 365:

1. In the Microsoft 365 admin center, select **Settings** &gt; [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818), and select the domain you want to set up.

    ![Select your domain in Microsoft 365.](../../media/dns-ionos/ionos-domainconnects-1.png)
2. Select the three dots (more actions) &gt; choose **Start setup**.

    ![Select Start setup.](../../media/dns-ionos/ionos-domainconnects-2.png)
3. On the How do you want to connect your domain? page, select **Continue**.
4. On the Add DNS records page, select **Add DNS records**.
5. On the IONOS sign-in page, sign in to your account, and select **Connect**, and **Allow**.

    ![Select Connect, and then Allow.](../../media/dns-ionos/ionos-domainconnects-3.png)

    This completes your domain setup for Microsoft 365.

## Create DNS records with manual setup

After you add these records at IONOS, your domain will be set up to work with Microsoft services.

Caution

IONOS doesn't allow a domain to have both an MX record and a top-level Autodiscover CNAME record. This limits the ways in which you can configure Exchange Online for Microsoft. There's a workaround, but we recommend employing it **only** if you already have experience with creating subdomains at IONOS. If despite this [service limitation](../setup/domains-faq) you choose to manage your own Microsoft DNS records at IONOS, follow the steps in this article to verify your domain and to set up DNS records for email, Microsoft Teams Online, and so on.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

### Add a TXT record for verification

Before you use your domain with Microsoft, we have to make sure that you own it. Your ability to sign in to your account at your domain registrar and create the DNS record proves to Microsoft that you own the domain.

Note

This record is used only to verify that you own your domain; it doesn't affect anything else. You can delete it later, if you like.

1. To get started, go to your domains page at IONOS by using [this link](https://login.ionos.com/). Follow the prompt to sign in.
2. Select **Menu**, and then select **Domains and SSL**.

    ![Select Domains and SSL.](../../media/dns-ionos/ionos-domains-1.png)
3. Under **Actions** for the domain that you want to update, select the gear control, and then select **DNS**.

    ![Select DNS from the drop-down list.](../../media/dns-ionos/ionos-domains-2.png)
4. Select **Add record**.

    ![Screenshot of where you select Add record to add a domain verification TXT record.](../../media/dns-ionos/ionos-domains-3.png)
5. Select the **TXT** section.

    ![Select the TXT section.](../../media/dns-ionos/ionos-domains-4.png)
6. On the Add a DNS record page, in the boxes for the new record, type or copy and paste the values from the following table.

    | Host name | Value | TTL |
    | --- | --- | --- |
    | (Leave this field blank) | MS=ms *XXXXXXXX* NOTE: This is an example. Use your specific **Destination or Points to Address** value here, from the table. [How do I find this?](../get-help-with-domains/information-for-dns-records) | 1 hour |
7. Select **Save**.

    ![Screenshot of where you select Save to add a TXT verification record.](../../media/dns-ionos/ionos-domains-5.png)

    Wait a few minutes before you continue, so that the record you just created can update across the Internet.

Now that you've added the record at your domain registrar's site, go back to Microsoft 365 and request Microsoft 365 to look for the record. When Microsoft finds the correct TXT record, your domain is verified.

To verify the record in Microsoft 365:

1. In the admin center, go to the **Settings** &gt; [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).
2. On the Domains page, select the domain that you're verifying, and select **Start setup**.

    ![Select Start setup.](../../media/dns-ionos/ionos-domainconnects-2.png)
3. Select **Continue**.
4. On the **Verify domain** page, select **Verify**.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

### Add an MX record so email for your domain will come to Microsoft

1. To get started, go to your domains page at IONOS by using [this link](https://login.ionos.com/). Follow the prompt to sign in.
2. Select **Menu**, and then select **Domains and SSL**.

    ![Select Domains and SSL.](../../media/dns-ionos/ionos-domains-1.png)
3. Under **Actions** for the domain that you want to update, select the gear control, and then select **DNS**.

    ![Select DNS from the drop-down list.](../../media/dns-ionos/ionos-domains-2.png)
4. Select **Add record**.

    ![Screenshot of where you select Add record to add an MX record.](../../media/dns-ionos/ionos-domains-3.png)
5. Select the **MX** section.

    ![Select the MX section.](../../media/dns-ionos/ionos-domains-mx.png)
6. On the Add a DNS record page, in the boxes for the new record, type or copy and paste the values from the following table.

    | Host name | Points to | Priority | TTL |
    | --- | --- | --- | --- |
    | @ | *&lt;domain-key&gt;*.mail.protection.outlook.com  NOTE: Get your &lt;domain-key&gt; from your Microsoft account. [How do I find this?](../get-help-with-domains/information-for-dns-records) | 10  For more information about priority, see [What is MX priority?](../setup/domains-faq) | 1 hour |
7. Select **Save**.

    ![Screenshot of where you select Save to add an MX record.](../../media/dns-ionos/ionos-domains-mx-save.png)
8. If there are any MX records already listed, delete each of them by selecting the **Delete record** trash can on the **Add record** page.

    ![Select Delete record.](../../media/dns-ionos/ionos-domains-delete.png)

### Add the CNAME record required for Microsoft

1. To get started, go to your domains page at IONOS by using [this link](https://login.ionos.com/). Follow the prompt to sign in.
2. Select **Menu**, and then select **Domains and SSL**.

    ![Select Domains and SSL.](../../media/dns-ionos/ionos-domains-1.png)
3. Under **Actions** for the domain that you want to update, select the gear control, and then select **DNS**.

    ![Select DNS from the drop-down list.](../../media/dns-ionos/ionos-domains-2.png)

    Now you'll create two subdomains and set an **Alias** value for each.

    (This is required because IONOS supports only one top-level CNAME record, but Microsoft requires several CNAME records.)

    First, you'll create the Autodiscover subdomain.
4. Select **Subdomains**.

    ![Select Subdomain.](../../media/dns-ionos/ionos-domains-subdomains.png)
5. Select **Add subdomain**.

    ![Select Add subdomains.](../../media/dns-ionos/ionos-domains-add-subdomains.png)
6. In the **Add subdomain** box for the new subdomain, type or copy and paste only the **Add subdomain** value from the following table. (You'll add the **Alias** value in a later step.)

    | Add subdomain | Alias |
    | --- | --- |
    | autodiscover | autodiscover.outlook.com |
7. Under **Actions** for the **autodiscover** subdomain that you created, select the gear control, and then select **DNS** from the drop-down list.
8. Select **Add record**, and then select the **CNAME** section.
9. In the **Alias:** box, type or copy and paste only the **Alias** value from the following table.

    | Add subdomain | Alias |
    | --- | --- |
    | autodiscover | autodiscover.outlook.com |
10. Select **Save**.

## Add a TXT record for SPF to help prevent email spam

Important

You can't have more than one TXT record for SPF for a domain. If your domain has more than one SPF record, you'll get email errors, and delivery and spam classification issues. If you already have an SPF record for your domain, don't create a new one for Microsoft. Instead, add the required Microsoft values to the current record so that you have a *single* SPF record that includes both sets of values. Need examples? Check out these [External Domain Name System records for Microsoft](../../enterprise/external-domain-name-system-records). To validate your SPF record, you can use one of these[SPF validation tools](../setup/domains-faq).

1. To get started, go to your domains page at IONOS by using [this link](https://login.ionos.com/). Follow the prompt to sign in.
2. Select **Menu**, and then select **Domains and SSL**.

    ![Select Domains and SSL.](../../media/dns-ionos/ionos-domains-1.png)
3. Under **Actions** for the domain that you want to update, select the gear control, and then select **DNS**.

    ![Select DNS from the drop-down list.](../../media/dns-ionos/ionos-domains-2.png)
4. Select **Add record**.

    ![Screenshot of where you select Add record to add an SPF TXT record.](../../media/dns-ionos/ionos-domains-3.png)
5. Select the **SPF (TXT)** section.

    ![Select the SPF (TXT) section.](../../media/dns-ionos/ionos-domains-spftxt.png)
6. In the boxes for the new record, type or copy and paste the values from the following table.

    | Type | Host name | Value | TTL |
    | --- | --- | --- | --- |
    | SPF (TXT) | (Leave this field empty.) | v=spf1 include:spf.protection.outlook.com -all **Note:** We recommend copying and pasting this entry, so that all of the spacing stays correct. | 1 hour |
7. Select **Save**.

    ![Screenshot of where you select Save to add an SPF TXT record.](../../media/dns-ionos/ionos-domains-spftxt-save.png)

## Advanced option: Microsoft Teams

Only select this option if your organization uses Microsoft Teams for online communication services like chat, conference calls, and video calls, in addition to Microsoft Teams. Skype needs four records: Two SRV records for user-to-user communication, and two CNAME records to sign-in and connect users to the service.

### Add two more CNAME records

1. To get started, go to your domains page at IONOS by using [this link](https://login.ionos.com/). Sign in.
2. Select **Menu**, and then select **Domains and SSL**.

    ![Select Domains and SSL.](../../media/dns-ionos/ionos-domains-1.png)
3. Under **Actions** for the domain that you want to update, select the gear control, and then select **DNS**.

    ![Select DNS from the drop-down list.](../../media/dns-ionos/ionos-domains-2.png)

    Now you'll create two subdomains and set an **Alias** value for each.

    (This is required because IONOS supports only one top-level CNAME record, but Microsoft requires several CNAME records.)

    First, you'll create the lyncdiscover subdomain.
4. Select **Subdomains**.

    ![Select Subdomain.](../../media/dns-ionos/ionos-domains-subdomains.png)
5. Select **Add subdomain**.

    ![Select Add subdomains.](../../media/dns-ionos/ionos-domains-add-subdomains.png)
6. In the **Add subdomain** box for the new subdomain, type or copy and paste only the **Add subdomain** value from the following table. (You'll add the **Alias** value in a later step.)

    | Add subdomain | Alias |
    | --- | --- |
    | lyncdiscover | webdir.online.lync.com |
7. Under **Actions** for the **lyncdiscover** subdomain that you created, select the gear control, and then select **DNS** from the drop-down list.
8. Select **Add record**, and then select the **CNAME** section.
9. In the **Alias:** box, type or copy and paste only the **Alias** value from the following table.

    | Create Subdomain | Alias |
    | --- | --- |
    | lyncdiscover | webdir.online.lync.com |
10. Create another subdomain (SIP): Select **Add subdomain**.
11. In the **Add subdomain** box for the new subdomain, type or copy and paste only the **Add subdomain** value from the following table. (You'll add the **Alias** value in a later step.)

    | Add subdomain | Alias |
    | --- | --- |
    | sip | sipdir.online.lync.com |
12. Under **Actions** for the subdomain that you created, select the gear control, and then select **DNS** from the drop-down list.
13. Select **Add record**.

    ![Screenshot of where you select Add record to add CNAME records for Microsoft Teams.](../../media/dns-ionos/ionos-domains-3.png)
14. Select the **CNAME** section.
15. in the **Alias:** box, type or copy and paste only the **Alias** value from the following table.

    | Create Subdomain | Alias |
    | --- | --- |
    | sip | sipdir.online.lync.com |
16. Select the check box for the **I am aware** disclaimer, and then select **Save**.

## Add the two SRV records required for Microsoft

1. To get started, go to your domains page at IONOS by using [this link](https://login.ionos.com/). Sign in.
2. Select **Menu**, and then select **Domains and SSL**.

    ![Select Domains and SSL.](../../media/dns-ionos/ionos-domains-1.png)
3. Under **Actions** for the domain that you want to update, select the gear control, and then select **DNS**.

    ![Select DNS from the drop-down list.](../../media/dns-ionos/ionos-domains-2.png)
4. Select **Add record**.

    ![Screenshot of where you select Add record to add an SRV record.](../../media/dns-ionos/ionos-domains-3.png)
5. Select the **SRV** section.

    ![Select the SRV section.](../../media/dns-ionos/ionos-domains-srv.png)
6. In the boxes for the new record, type or copy and paste the values from the following table.

    | Type | Service | Protocol | Host name | Points to | Priority | Weight | Port | TTL |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | SRV | \_sip | tls | (Leave this field empty.) | sipdir.online.lync.com | 100 | 1 | 443 | 1 hour |
    | SRV | \_sipfederationtls | tcp | (Leave this field empty.) | sipfed.online.lync.com | 100 | 1 | 5061 | 1 hour |
7. Select **Save**.

    ![Screenshot of where you select Save to add an SRV record.](../../media/dns-ionos/ionos-domains-srv-save.png)
8. Add the other SRV record.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

## Advanced option: Intune and Mobile Device Management for Microsoft 365

This service helps you secure and remotely manage mobile devices that connect to your domain. Mobile Device Management needs two CNAME records so that users can enroll devices to the service.

### Add the two required CNAME records

Important

Follow the subdomain procedure that you used for the other CNAME records, and supply the values from the following table.

1. To get started, go to your domains page at IONOS by using [this link](https://login.ionos.com/). Follow the prompt to sign in.
2. Select **Menu**, and then select **Domains and SSL**.

    ![Select Domains and SSL.](../../media/dns-ionos/ionos-domains-1.png)
3. Under **Actions** for the domain that you want to update, select the gear control, and then select **DNS**.

    ![Select DNS from the drop-down list.](../../media/dns-ionos/ionos-domains-2.png)

    Now you'll create two subdomains and set an **Alias** value for each.

    (This is required because IONOS supports only one top-level CNAME record, but Microsoft requires several CNAME records.)

    First, you'll create the lyncdiscover subdomain.
4. Select **Subdomains**.

    ![Select Subdomain.](../../media/dns-ionos/ionos-domains-subdomains.png)
5. Select **Add subdomain**.

    ![Select Add subdomains.](../../media/dns-ionos/ionos-domains-add-subdomains.png)
6. In the **Add subdomain** box for the new subdomain, type or copy and paste only the **Add subdomain** value from the following table. (You'll add the **Alias** value in a later step.)

    | Add subdomain | Alias |
    | --- | --- |
    | enterpriseregistration | enterpriseregistration.windows.net |
7. Under **Actions** for the **enterpriseregistration** subdomain that you created, select the gear control, and then select **DNS** from the drop-down list.
8. Select **Add record**, and then select the **CNAME** section.
9. In the **Alias:** box, type or copy and paste only the **Alias** value from the following table.

    | Add subdomain | Alias |
    | --- | --- |
    | enterpriseregistration | enterpriseregistration.windows.net |
10. Create another subdomain: Select **Add subdomain**.
11. In the **Add subdomain** box for the new subdomain, type or copy and paste only the **Add subdomain** value from the following table. (You'll add the **Alias** value in a later step.)

    | Add subdomain | Alias |
    | --- | --- |
    | enterpriseenrollment | enterpriseenrollment-s.manage.microsoft.com |
12. Under **Actions** for the **enterpriseenrollment** subdomain that you created, select the gear control, and then select **DNS** from the drop-down list.
13. Select **Add record**.

    ![Screenshot of where you select Add record to add CNAME records for Mobile Device Management.](../../media/dns-ionos/ionos-domains-3.png)
14. Select the **CNAME** section.
15. in the **Alias:** box, type or copy and paste only the **Alias** value from the following table.

    | Create Subdomain | Alias |
    | --- | --- |
    | enterpriseenrollment | enterpriseenrollment-s.manage.microsoft.com |
16. Select the check box for the **I am aware** disclaimer, and then select **Save**.