---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Connect your DNS records at Wix to Microsoft 365 - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-wix?view=o365-worldwide
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
ms.date: 2026-06-16T00:00:00.0000000Z
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
ms.assetid: 7173c635-58b3-400f-95e0-97abe915565e
description: Learn to verify your domain and set up DNS records for email, Microsoft Teams Online, and other services at Wix.
locale: en-us
document_id: d3200297-3d59-9cf3-4d8e-494e8d000bb1
document_version_independent_id: 3edaf8bb-829e-26a5-321c-19fb32f93460
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/dns/create-dns-records-at-wix.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/dns/create-dns-records-at-wix
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/dns/create-dns-records-at-wix.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
platformId: f29d9d74-258f-ad1b-4a1a-455c81728f74
---

# Connect your DNS records at Wix to Microsoft 365 - Microsoft 365 admin | Microsoft Learn

If Wix is your DNS hosting provider, follow the steps in this article to verify your domain and set up DNS records for email, Microsoft Teams Online, and so on.

After you add these records at Wix, your domain will be set up to work with Microsoft services.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

## Add a TXT record for verification

Before you use your domain with Microsoft, we have to make sure you own it. Your ability to sign in to your account at your domain registrar and create the DNS record proves to Microsoft that you own the domain.

Note

- This record is used only to verify that you own your domain; it doesn't affect anything else. You can delete it later if you like.
- WIX doesn't support DNS entries for subdomains.

1. Make sure a domain is added in the Microsoft 365 Admin Center using the steps in [Add a domain](/en-us/admin/setup/add-domain#add-a-domain) and that the domain isn't already verified. Copy the **TXT value** from the **Add a record to verify ownership** page for use later in this procedure.
2. Sign in to your domains page at Wix by using [this link](https://premium.wix.com/wix/api/mpContainerStaticController#/domains?referralAdditionalInfo=account).
3. From the left-hand navigation bar, select **Domains**.
4. Find the domain you wish to configure, select the three dots **(...)**, and then select **Manage DNS Records** from the dropdown list.

    [![Screenshot of where you select Manage DNS Records from the drop-down list.](../../media/dns-wix/wix-domains-1.png)](../../media/dns-wix/wix-domains-1.png#lightbox)
5. Select **+ Add Record** in the **TXT (Text)** row of the DNS editor.

    [![Screenshot of where you select Add record to add a domain verification TXT record.](../../media/dns-wix/wix-domains-txt-add-record.png)](../../media/dns-wix/wix-domains-txt-add-record.png#lightbox)
6. In the boxes for the new record, enter or copy and paste the values from the following table. Use the TXT value you copied earlier (MS=ms*XXXXXXXX*).

    | Host Name | TXT Value | TTL |
    | --- | --- | --- |
    | Automatically populated (leave blank) | MS=ms*XXXXXXXX***Note:** This text is an example. Use your specific **Destination or Points to Address** value here, from the table. For more information, see [Gather the information you need to create DNS records](../get-help-with-domains/information-for-dns-records). | One Hour |
7. Select **Save**.

    [![Screenshot of where you select Save to add domain verification TXT record.](../../media/dns-wix/wix-domains-txt-save.png)](../../media/dns-wix/wix-domains-txt-save.png#lightbox)

    Wait a few minutes before you continue, so that the record you created can update across the Internet.

Now that you added the record at your domain registrar's site, go back to Microsoft and request the record. When Microsoft finds the correct TXT record, your domain is verified.

To verify the record in Microsoft 365:

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.
3. Under **Settings**, select [**Domains**](https://admin.cloud.microsoft/?#/Domains).
4. In the **Domains** page, select the domain that you're verifying, and select **Start setup**.

    [![Screenshot of where you select Start setup.](../../media/dns-ionos/ionos-domainconnects-2.png)](../../media/dns-ionos/ionos-domainconnects-2.png#lightbox)
5. Select **Continue**.
6. On the **Verify domain** page, select **Verify**.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

## Add an MX record so email for your domain comes to Microsoft

1. To get started, Sign in to your domains page at Wix by using [this link](https://premium.wix.com/wix/api/mpContainerStaticController#/domains?referralAdditionalInfo=account).
2. From the left-hand navigation bar, select **Domains**.
3. Find the domain you wish to configure, select the three dots **(...)**, and then select **Manage DNS Records** from the dropdown list.

    ![Select Manage DNS Records from the drop-down list.](../../media/dns-wix/wix-domains-1.png)
4. Under **MX (Mail exchange)**, select the link **connect a business email**.

    [![Screenshot of where you select Edit MX Records.](../../media/dns-wix/wix-domains-edit-mx-records.png)](../../media/dns-wix/wix-domains-edit-mx-records.png#lightbox)
5. Choose **Other** from the drop-down list, and select **+ Add record**.

    [![Screenshot of where you select Other from the drop-down list.](../../media/dns-wix/wix-domains-other.png)](../../media/dns-wix/wix-domains-other.png#lightbox)
6. In the boxes for the new record, enter or copy and paste the values from the following table:

    | Host Name | Points to | Priority | TTL |
    | --- | --- | --- | --- |
    | Automatically populated | *&lt;domain-key&gt;*.mail.protection.outlook.com **Note:** Get your *&lt;domain-key&gt;* from your Microsoft account. For more information, see [Gather the information you need to create DNS records](../get-help-with-domains/information-for-dns-records). | 0  For more information about priority, see [What is MX priority?](../setup/domains-faq) | One Hour |
7. If there are any other MX records listed, delete each of them.

    [![Screenshot of where you select Delete to remove other MX records.](../../media/dns-wix/wix-domains-mx-delete.png)](../../media/dns-wix/wix-domains-mx-delete.png#lightbox)
8. Select **Save**.

## Add the CNAME record required for Microsoft

1. To get started, Sign in to your domains page at Wix by using [this link](https://premium.wix.com/wix/api/mpContainerStaticController#/domains?referralAdditionalInfo=account).
2. From the left-hand navigation bar, select **Domains**.
3. Find the domain you wish to configure, select the three dots **(...)**, and then select **Manage DNS Records** from the dropdown list.

    ![Select Manage DNS Records from the drop-down list.](../../media/dns-wix/wix-domains-1.png)
4. Select **+ Add Record** in the **CNAME (Aliases)** row of the DNS editor for the CNAME record.

    [![Screenshot of where you select Add a record to add a CNAME record.](../../media/dns-wix/wix-domains-cname-add-record.png)](../../media/dns-wix/wix-domains-cname-add-record.png#lightbox)
5. In the boxes for the new record, enter or copy and paste the values from the following table:

    | Host Name | Value | TTL |
    | --- | --- | --- |
    | autodiscover | autodiscover.outlook.com | One Hour |
6. Select **Save**.

    [![Screenshot of where you select Save to add a CNAME record.](../../media/dns-wix/wix-domains-cname-save.png)](../../media/dns-wix/wix-domains-cname-save.png#lightbox)

    Wait a few minutes before you continue, so that the record you created can update across the Internet.

## Add a TXT record for SPF to help prevent email spam

Important

You can't have more than one TXT record for SPF for a domain. If your domain has more than one SPF record, email errors, delivery issues, and spam classification issues can occur. If you already have an SPF record for your domain, don't create a new one for Microsoft. Instead, add the required Microsoft values to the current record so that you have a *single* SPF record that includes both sets of values.

1. To get started, Sign in to your domains page at Wix by using [this link](https://premium.wix.com/wix/api/mpContainerStaticController#/domains?referralAdditionalInfo=account).
2. From the left-hand navigation bar, select **Domains**.
3. Find the domain you wish to configure, select the three dots **(...)**, and then select **Manage DNS Records** from the dropdown list.

    ![Select Manage DNS Records from the drop-down list.](../../media/dns-wix/wix-domains-1.png)
4. Select **+ Add Record** in the **TXT (Text)** row of the DNS editor.

    [![Screenshot of where you select Add a record to add an SPF TXT record.](../../media/dns-wix/wix-domains-txt-add-record.png)](../../media/dns-wix/wix-domains-txt-add-record.png#lightbox)

    Note

    Wix provides an SPF row in the DNS editor. Ignore that row and use the **TXT (Text)** row to enter the following SPF values.
5. In the boxes for the new record, enter or copy and paste the values from the following table:

    | Host Name | Value | TTL |
    | --- | --- | --- |
    | [leave this blank] | v=spf1 include:spf.protection.outlook.com -all **Note:** We recommend copying and pasting this entry, so that all of the spacing stays correct. | One Hour |
6. Select **Save**.

    [![Screenshot of where you select Save to add an SPF TXT record.](../../media/dns-wix/wix-domains-txt-save.png)](../../media/dns-wix/wix-domains-txt-save.png#lightbox)

    Wait a few minutes before you continue, so that the record you created can update across the Internet.

## Advanced option: Microsoft Teams

Only select this option if your organization uses Microsoft Teams for online communication services like chat, conference calls, and video calls, in addition to Microsoft Teams. Skype needs four records: two SRV records for user-to-user communication, and two CNAME records to sign-in and connect users to the service.

### Add the two required SRV records

1. To get started, Sign in to your domains page at Wix by using [this link](https://premium.wix.com/wix/api/mpContainerStaticController#/domains?referralAdditionalInfo=account).
2. From the left-hand navigation bar, select **Domains**.
3. Find the domain you wish to configure, select the three dots **(...)**, and then select **Manage DNS Records** from the dropdown list.

    ![Select Manage DNS Records from the drop-down list.](../../media/dns-wix/wix-domains-1.png)
4. Select **+ Add Record** in the **SRV** row of the DNS editor.

    [![Screenshot of where you select Add a record to add an SRV record.](../../media/dns-wix/wix-domains-srv-add-record.png)](../../media/dns-wix/wix-domains-srv-add-record.png#lightbox)
5. In the boxes for the new record, enter or copy and paste the values from the first row in the table:

    | Service | Protocol | Host name | Weight | Port | Target | Priority | TTL |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | sip | tls | Automatically populated | 1 | 443 | sipdir.online.lync.com | 100 | One Hour |
    | sipfed | tcp | Automatically populated | 1 | 5061 | sipfed.online.lync.com | 100 | One Hour |
6. Select **Save**.

    [![Screenshot of where you select Save to add a SRV record.](../../media/dns-wix/wix-domains-srv-save.png)](../../media/dns-wix/wix-domains-srv-save.png#lightbox)
7. Add the other SRV record by copying the values from the second row of the table.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

### Add the two required CNAME records for Microsoft Teams

1. Select **+ Add another** in the **CNAME (Aliases)** row of the DNS editor, and enter the values from the first row in the following table.

    | Type | Host | Value | TTL |
    | --- | --- | --- | --- |
    | CNAME | sip | sipdir.online.lync.com. **This value MUST end with a period (.)** | One Hour |
    | CNAME | lyncdiscover | webdir.online.lync.com. **This value MUST end with a period (.)** | One Hour |
2. Select **Save**.

    [![Screenshot of where you select Save to add CNAME records for Microsoft Teams.](../../media/dns-wix/wix-domains-cname-save.png)](../../media/dns-wix/wix-domains-cname-save.png#lightbox)
3. Add the other CNAME record by copying the values from the second row of the table.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

## Advanced option: Intune and Mobile Device Management for Microsoft 365

This service helps you secure and remotely manage mobile devices that connect to your domain. Mobile Device Management needs two CNAME records so that users can enroll devices to the service.

### Add the two required CNAME records for Mobile Device Management

1. To get started, Sign in to your domains page at Wix by using [this link](https://premium.wix.com/wix/api/mpContainerStaticController#/domains?referralAdditionalInfo=account).
2. From the left-hand navigation bar, select **Domains**.
3. Find the domain you wish to configure, select the three dots **(...)**, and then select **Manage DNS Records** from the dropdown list.

    ![Select Manage DNS Records from the drop-down list.](../../media/dns-wix/wix-domains-1.png)
4. Select **+ Add Record** in the **CNAME (Aliases)** row of the DNS editor for the CNAME record.

    [![Screenshot of where you select Add a record to add CNAME records for Mobile Device Management.](../../media/dns-wix/wix-domains-cname-add-record.png)](../../media/dns-wix/wix-domains-cname-add-record.png#lightbox)
5. Enter the values from the first row in the following table.

    | Type | Host | Value | TTL |
    | --- | --- | --- | --- |
    | CNAME | enterpriseregistration | enterpriseregistration.windows.net. **This value MUST end with a period (.)** | One Hour |
    | CNAME | enterpriseenrollment | enterpriseenrollment.manage.microsoft.com. **This value MUST end with a period (.)** | One Hour |
6. Select **Save**.

    [![Screenshot of where you select Save to add CNAME records for Mobile Device Management.](../../media/dns-wix/wix-domains-cname-save.png)](../../media/dns-wix/wix-domains-cname-save.png#lightbox)
7. Add the other CNAME record by copying the values from the second row of the table.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

## Support

**[Check the Domains FAQ](../setup/domains-faq)** if you don't find what you're looking for.

Tip

Some configuration tasks might be complex to perform. For technical support, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. At the bottom right, select **Help & Support**.
3. In the **Support Assistant** pane that opens, enter your question.
4. Review the results. If you still have questions, select **Contact support**.

To learn about your options for contacting support, see [Get support for Microsoft 365 for business](/en-us/microsoft-365/admin/get-help-support).