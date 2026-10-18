---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Connect your DNS records at Network Solutions to Microsoft 365 - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-network-solutions?view=o365-worldwide
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
ms.service: microsoft-365-business
ms.subservice: m365-domains
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
ms.assetid: 1dc55f9f-5309-450f-acc3-b2b4119c8be3
description: Learn to verify your domain and set up DNS records for email, Microsoft Teams Online, and other services at Network Solutions for Microsoft.
locale: en-us
document_id: e9c6bbf8-c699-5317-5751-339dd499f8d7
document_version_independent_id: 20b3d64a-ef3e-da1f-a0b1-7bcb54acfeb2
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/dns/create-dns-records-at-network-solutions.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/dns/create-dns-records-at-network-solutions
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/dns/create-dns-records-at-network-solutions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
platformId: 320b6c88-ab21-9727-0929-eeb3d51932e2
---

# Connect your DNS records at Network Solutions to Microsoft 365 - Microsoft 365 admin | Microsoft Learn

**[Check the Domains FAQ](../setup/domains-faq)** if you don't find what you're looking for.

If Network Solutions is your DNS hosting provider, follow the steps in this article to verify your domain and set up DNS records for email, Microsoft Teams Online, and so on.

After you add these records at Network Solutions, your domain will be set up to work with Microsoft services.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

Tip

Some configuration tasks might be complex to perform. For technical support, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. At the bottom right, select **Help & Support**.
3. In the **Support Assistant** pane that opens, enter your question.
4. Review the results. If you still have questions, select **Contact support**.

To learn about your options for contacting support, see [Get support for Microsoft 365 for business](/en-us/microsoft-365/admin/get-help-support).

## Add a TXT record for verification

Before you use your domain with Microsoft, we have to make sure that you own it. Your ability to log in to your account at your domain registrar and create the DNS record proves to Microsoft that you own the domain.

Note

This record is used only to verify that you own your domain; it doesn't affect anything else. You can delete it later, if you like.

1. To get started, go to your domains page at Network Solutions by using [this link](https://www.networksolutions.com/manage-it). You'll be prompted to log in.
2. On the landing page, select **Domain Names**.
3. Select the check box next to the domain that you want to modify.
4. Under **Actions**, select the three dots, and then select **Manage** from the drop-down list.

    ![Select Manage from the drop-down list.](../../media/dns-networksolutions/networksolutions-domains-1.png)
5. Scroll down to select **Advanced Tools**, and next to **Advanced DNS Records**, select **MANAGE**.

    ![Next to Advanced DNS records, select MANAGE.](../../media/dns-networksolutions/networksolutions-domains-2.png)

    You might have to select **Continue** to get to the Manage Advanced DNS Records page.
6. On the Manage Advanced DNS Records page, select **+ADD RECORD**.

    ![Select +ADD RECORD.](../../media/dns-networksolutions/networksolutions-domains-add-record.png)
7. Under **Type**, select **TXT** from the drop-down list.
8. In the boxes for the new record, type or copy and paste the values in the following table.

    | Refers to | TXT Value | TTL |
    | --- | --- | --- |
    | @  (The system will change this value to **@ (None)** when you save the record.) | MS=ms *XXXXXXXX***Note:** This is an example. Use your specific **Destination or Points to Address** value here, from the table. [How do I find this?](../get-help-with-domains/information-for-dns-records) | 3600 |
9. Select **ADD**.

    ![Screenshot of where you select Add to add a domain verification TXT record.](../../media/dns-networksolutions/networksolutions-domains-add.png)

    Note

    Select **Classic View** in the upper right to view the TXT record you created.

    Wait a few minutes before you continue, so that the record you just created can update across the Internet.

Now that you've added the record at your domain registrar's site, you'll go back to Microsoft and request the record. When Microsoft finds the correct TXT record, your domain is verified.

To verify the record in Microsoft 365:

1. In the admin center, go to the **Settings** &gt; [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).
2. On the Domains page, select the domain that you're verifying, and select **Start setup**.

    ![Select Start setup.](../../media/dns-ionos/ionos-domainconnects-2.png)
3. Select **Continue**.
4. On the **Verify domain** page, select **Verify**.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

## Add an MX record so email for your domain will come to Microsoft

1. To get started, go to your domains page at Network Solutions by using [this link](https://www.networksolutions.com/manage-it). You'll be prompted to log in.
2. On the landing page, select **Domain Names**.
3. Select the check box next to the domain that you want to modify.
4. Under **Actions**, select the three dots, and then select **Manage** in the drop-down list.

    ![Select Manage from the drop-down list.](../../media/dns-networksolutions/networksolutions-domains-1.png)
5. Scroll down to select **Advanced Tools**, and next to **Advanced DNS Records**, select **MANAGE**.

    ![Next to Advanced DNS records, select MANAGE.](../../media/dns-networksolutions/networksolutions-domains-2.png)

    You might have to select **Continue** to get to the Manage Advanced DNS Records page.
6. On the Manage Advanced DNS Records page, select **+ADD RECORD**.

    ![Select +ADD RECORD.](../../media/dns-networksolutions/networksolutions-domains-add-record.png)
7. Under **Type**, select **MX** from the drop-down list.
8. In the boxes for the new record, type or copy and paste the values from the following table.

    | Refers to | Mail server | Priority | TTL |
    | --- | --- | --- | --- |
    | @ | *&lt;domain-key&gt;*.mail.protection.outlook.com **This value CANNOT end with a period (.)** **Note:** Get your *&lt;domain-key&gt;* from your Microsoft account. [How do I find this?](../get-help-with-domains/information-for-dns-records) | 0  For more information about priority, see [What is MX priority?](../setup/domains-faq) | 1 Hour |
9. Select **ADD**.

    ![Screenshot of where you select Add to add an MX record.](../../media/dns-networksolutions/networksolutions-domains-mx-add.png)

    Note

    Select **Classic View** in the upper right to view the TXT record you created.
10. If there are any other MX records, delete all of them by selecting the edit tool, and then **Delete** for each record.

    ![Select the Edit tool.](../../media/dns-networksolutions/networksolutions-domains-edit.png)

## Add the CNAME record required for Microsoft

1. To get started, go to your domains page at Network Solutions by using [this link](https://www.networksolutions.com/manage-it). You'll be prompted to log in.
2. On the landing page, select **Domain Names**.
3. Select the check box next to the domain that you want to modify.
4. Under **Actions**, select the three dots, and then select **Manage** in the drop-down list.

    ![Select Manage from the drop-down list.](../../media/dns-networksolutions/networksolutions-domains-1.png)
5. Select **Advanced Tools**, and next to **Advanced DNS Records**, select **MANAGE**.

    ![Next to Advanced DNS records, select MANAGE.](../../media/dns-networksolutions/networksolutions-domains-2.png)

    You might have to select **Continue** to get to the Manage Advanced DNS Records page.
6. On the Manage Advanced DNS Records page, select **+ADD RECORD**.

    ![Select +ADD RECORD.](../../media/dns-networksolutions/networksolutions-domains-add-record.png)
7. Under **Type**, select **CNAME** from the drop-down list.

    ![Select CNAME type from the drop-down list.](../../media/dns-networksolutions/networksolutions-domains-cname.png)
8. In the boxes for the CNAME record, type or copy and paste the values from the following table.

    | Refers to | Host Name | Alias to | TTL |
    | --- | --- | --- | --- |
    | Other Host | autodiscover | autodiscover.outlook.com **This value CANNOT end with a period (.)** 1 Hour |  |

    ![Type or copy and paste the CNAME values from the table into the window.](../../media/dns-networksolutions/networksolutions-domains-cname-values.png)
9. Select **ADD**.

    Note

    Select **Classic View** in the upper right to view the record you created.

## Add a TXT record for SPF to help prevent email spam

Important

You cannot have more than one TXT record for SPF for a domain. If your domain has more than one SPF record, you'll get email errors, as well as delivery and spam classification issues. If you already have an SPF record for your domain, don't create a new one for Microsoft. Instead, add the required Microsoft values to the current record so that you have a *single* SPF record that includes both sets of values.

1. To get started, go to your domains page at Network Solutions by using [this link](https://www.networksolutions.com/manage-it). You'll be prompted to log in.
2. On the landing page, select **Domain Names**.
3. Select the check box next to the domain that you want to modify.
4. Under **Actions**, select the three dots, and then select **Manage** in the drop-down list.

    ![Select Manage from the drop-down list.](../../media/dns-networksolutions/networksolutions-domains-1.png)
5. Select **Advanced Tools**, and next to **Advanced DNS Records**, select **MANAGE**.

    ![Next to Advanced DNS records, select MANAGE.](../../media/dns-networksolutions/networksolutions-domains-2.png)

    You might have to select **Continue** to get to the Manage Advanced DNS Records page.
6. On the Manage Advanced DNS Records page, select **+ADD RECORD**.

    ![Select +ADD RECORD.](../../media/dns-networksolutions/networksolutions-domains-add-record.png)
7. Under **Type**, select **TXT** from the drop-down list.

    ![Select TXT from the Type drop-down list.](../../media/dns-networksolutions/networksolutions-domains-txt.png)
8. In the boxes for the new record, type or copy and paste the following values.

    | Refers to | TXT Value | TTL |
    | --- | --- | --- |
    | @  (The system will change this value to **@ (None)** when you save the record.) | v=spf1 include:spf.protection.outlook.com -all **Note:** We recommend copying and pasting this entry, so that all of the spacing stays correct. | 1 Hour |
9. Select **ADD**.

    ![Screenshot of where you select Add to add an SPF TXT record.](../../media/dns-networksolutions/networksolutions-domains-add.png)

    Note

    Select **Classic View** in the upper right to view the record you created.

## Advanced option: Microsoft Teams

Only select this option if your organization uses Microsoft Teams for online communication services like chat, conference calls, and video calls, in addition to Microsoft Teams. Skype needs 4 records: 2 SRV records for user-to-user communication, and 2 CNAME records to sign-in and connect users to the service.

### Add the two required SRV records

1. To get started, go to your domains page at Network Solutions by using [this link](https://www.networksolutions.com/manage-it). You'll be prompted to log in.
2. On the landing page, select **Domain Names**.
3. Select the check box next to the domain that you want to modify.
4. Under **Actions**, select the three dots, and then select **Manage** in the drop-down list.

    ![Select Manage from the drop-down list.](../../media/dns-networksolutions/networksolutions-domains-1.png)
5. Select **Advanced Tools**, and next to **Advanced DNS Records**, select **MANAGE**.

    ![Next to Advanced DNS records, select MANAGE.](../../media/dns-networksolutions/networksolutions-domains-2.png)

    You might have to select **Continue** to get to the Manage Advanced DNS Records page.
6. On the Manage Advanced DNS Records page, select **+ADD RECORD**.

    ![Select +ADD RECORD.](../../media/dns-networksolutions/networksolutions-domains-add-record.png)
7. Under **Type**, select **SRV** from the drop-down list.

    ![Select SRV from the Type drop-down list.](../../media/dns-networksolutions/networksolutions-domains-srv.png)
8. In the boxes for the two new records, type or copy and paste the values from the following table.

    (Choose the **Service** and **Protocol** values from the drop-down lists.)

    | Type | Service | Protocol | Weight | Port | Target | Priority | TTL |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | SRV | \_sip | TLS | 100 | 443 | sipdir.online.lync.com **This value CANNOT end with a period (.)** | 1 | 1 Hour |
    | SRV | \_sipfederationtls | TCP | 100 | 5061 | sipfed.online.lync.com **This value CANNOT end with a period (.)** | 1 | 1 Hour |
9. Select **ADD**.

    ![Screenshot of where you select Add to add an SRV record.](../../media/dns-networksolutions/networksolutions-domains-srv-add.png)

    Note

    Select **Classic View** in the upper right to view the record you created.
10. Add the other SRV record by copying the values from the second row of the table.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

### Add the two required CNAME records for Microsoft Teams

1. To get started, go to your domains page at Network Solutions by using [this link](https://www.networksolutions.com/manage-it). You'll be prompted to log in.
2. On the landing page, select **Domain Names**.
3. Select the check box next to the domain that you want to modify.
4. Under **Actions**, select the three dots, and then select **Manage** in the drop-down list.

    ![Select Manage from the drop-down list.](../../media/dns-networksolutions/networksolutions-domains-1.png)
5. Select **Advanced Tools**, and next to **Advanced DNS Records**, select **MANAGE**.

    ![Next to Advanced DNS records, select MANAGE.](../../media/dns-networksolutions/networksolutions-domains-2.png)

    You might have to select **Continue** to get to the Manage Advanced DNS Records page.
6. On the Manage Advanced DNS Records page, select **+ ADD RECORD**.

    ![Select +ADD RECORD.](../../media/dns-networksolutions/networksolutions-domains-add-record.png)
7. Under **Type**, select **CNAME** from the drop-down list.

    ![Select CNAME type from the drop-down list.](../../media/dns-networksolutions/networksolutions-domains-cname.png)
8. In the boxes for the CNAME record, type or copy and paste the values from the following table.

    | Type | Refers to | Host Name | Alias to | TTL |
    | --- | --- | --- | --- | --- |
    | CNAME | Other Host | sip | sipdir.online.lync.com **This value CANNOT end with a period (.)** | 1 Hour |
    | CNAME | Other Host | lyncdiscover | webdir.online.lync.com **This value CANNOT end with a period (.)** | 1 Hour |

    ![Type or copy and paste the CNAME values from the table into the window.](../../media/dns-networksolutions/networksolutions-domains-cname-values.png)
9. Select **ADD**.

    Note

    Select **Classic View** in the upper right to view the record you created.
10. Add the other CNAME record by copying the values from the second row of the table.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

## Advanced option: Intune and Mobile Device Management for Microsoft 365

This service helps you secure and remotely manage mobile devices that connect to your domain. Mobile Device Management needs 2 CNAME records so that users can enroll devices to the service.

### Add the two required CNAME records for Mobile Device Management

1. To get started, go to your domains page at Network Solutions by using [this link](https://www.networksolutions.com/manage-it). You'll be prompted to log in.
2. On the landing page, select **Domain Names**.
3. Select the check box next to the domain that you want to modify.
4. Under **Actions**, select the three dots, and then select **Manage** in the drop-down list.

    ![Select Manage from the drop-down list.](../../media/dns-networksolutions/networksolutions-domains-1.png)
5. Select **Advanced Tools**, and next to **Advanced DNS Records**, select **MANAGE**.

    ![Next to Advanced DNS records, select MANAGE.](../../media/dns-networksolutions/networksolutions-domains-2.png)

    You might have to select **Continue** to get to the Manage Advanced DNS Records page.
6. On the Manage Advanced DNS Records page, select **+ADD RECORD**.

    ![Select +ADD RECORD.](../../media/dns-networksolutions/networksolutions-domains-add-record.png)
7. Under **Type**, select **CNAME** from the drop-down list.

    ![Select CNAME type from the drop-down list.](../../media/dns-networksolutions/networksolutions-domains-cname.png)
8. In the boxes for the CNAME record, type or copy and paste the values from the following table.

    | Type | Refers to | Host Name | Alias to | TTL |
    | --- | --- | --- | --- | --- |
    | CNAME | Other Host | enterpriseregistration | enterpriseregistration.windows.net **This value CANNOT end with a period (.)** | 1 Hour |
    | CNAME | Other Host | enterpriseenrollment | enterpriseenrollment-s.manage.microsoft.com **This value CANNOT end with a period (.)** | 1 Hour |

    ![Type or copy and paste the CNAME values from the table into the window.](../../media/dns-networksolutions/networksolutions-domains-cname-values.png)
9. Select **ADD**.

    Note

    Select **Classic View** in the upper right to view the record you created.
10. Add the other CNAME record by copying the values from the second row of the table.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).