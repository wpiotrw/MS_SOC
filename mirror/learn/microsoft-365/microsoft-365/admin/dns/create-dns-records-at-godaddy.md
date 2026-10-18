---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Connect your DNS records at GoDaddy to Microsoft 365 - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-godaddy?view=o365-worldwide
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
ms.assetid: f40a9185-b6d5-4a80-bb31-aa3bb0cab48a
description: Learn to verify your domain and set up DNS records for email, Microsoft Teams, and other services at GoDaddy for Microsoft.
locale: en-us
document_id: fa9b019f-fa0b-5e2d-57fc-1e3acef0c75d
document_version_independent_id: a75691ca-2f8a-9b6f-4e1f-b7d726da1d96
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/dns/create-dns-records-at-godaddy.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/dns/create-dns-records-at-godaddy
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/dns/create-dns-records-at-godaddy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 57cc9ccf-2c3c-2aa4-0141-3e198a86e6c2
---

# Connect your DNS records at GoDaddy to Microsoft 365 - Microsoft 365 admin | Microsoft Learn

**[Check the Domains FAQ](../setup/domains-faq)** if you don't find what you're looking for.

If GoDaddy is your DNS hosting provider, follow the steps in this article to verify your domain and set up DNS records for email, Teams, and so on.

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
- **Use the manual steps** Verify your domain using the manual steps below and choose when and which records to add to your domain registrar. This allows you to set up new MX (mail) records, for example, at your convenience.

## Use Domain Connect to verify and set up your domain

Follow these steps to automatically verify and set up your GoDaddy domain with Microsoft 365:

1. In the Microsoft 365 admin center, select **Settings** &gt; [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818), and select the domain you want to set up.
2. Select the three dots (more actions) &gt; choose **Start setup**.

    ![Select Start setup.](../../media/dns-ionos/ionos-domainconnects-2.png)
3. On the How do you want to connect your domain? page, select **Continue**.
4. On the Add DNS records page, select **Add DNS records**.
5. On the GoDaddy login page, sign in to your account, and select **Authorize**.

    This completes your domain setup for Microsoft 365.

## Create DNS records with manual setup

After you add these records at GoDaddy, your domain will be set up to work with Microsoft services.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

### Add a TXT record for verification

Before you use your domain with Microsoft, we have to make sure that you own it. Your ability to log in to your account at your domain registrar and create the DNS record proves to Microsoft that you own the domain.

Note

This record is used only to verify that you own your domain; it doesn't affect anything else. You can delete it later, if you like.

1. To get started, go to your domains page at GoDaddy by using [this link](https://account.godaddy.com/products/?go_redirect=disabled).

    If you're prompted to log in, use your login credentials, select your login name in the upper right, and then select **My Products**.
2. Under **Domains**, in the Portfolio tab, select the ellipse (...) next to the domain you want to verify, and select **Edit DNS** from the drop-down menu.

    ![Select DNS.](../../media/dns-godaddy/godaddy-manage-dns.png)
3. Under **DNS Records**, select **Add New Record** on the top right corner.

    ![Screenshot of where you select Add to add a domain verification TXT record.](../../media/dns-godaddy/godaddy-domains-add.png)
4. Select **TXT** option from the filter box.
5. In the boxes for the new record, type or copy and paste the values from the table.

    | Type | Name | Value | TTL |
    | --- | --- | --- | --- |
    | TXT | @ | MS=ms *XXXXXXXX***Note**: This is an example. Use your specific **Destination or Points to Address** value here, from the table. [How do I find this?](../get-help-with-domains/information-for-dns-records) | 1 hour |

    ![Fill in the values from the table for the domain verification TXT record.](../../media/dns-godaddy/godaddy-domains-txtvalue.png)
6. Select **Save**.

    Wait a few minutes before you continue, so that the record you just created can update across the Internet.

Now that you've added the record at your domain registrar's site, you'll go back to Microsoft and request the record. When Microsoft finds the correct TXT record, your domain is verified.

To verify the record in Microsoft 365:

1. In the admin center, go to the **Settings** &gt; [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).
2. On the Domains page, select the domain that you're verifying, and select **Start setup**.

    ![ Diagram showing Select Start setup.](../../media/dns-ionos/ionos-domainconnects-2.png)
3. Select **Continue**.
4. On the **Verify domain** page, select **Verify**.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

### Add an MX record so email for your domain will come to Microsoft

1. To get started, go to your domains page at GoDaddy by using [this link](https://account.godaddy.com/products/?go_redirect=disabled).

    If you're prompted to log in, use your login credentials, select your login name in the upper right, and then select **My Products**.
2. Under **Domains**, in the Portfolio tab, select the ellipse (...) next to the domain you want to verify, and select **Edit DNS** from the drop-down menu.

    ![Screenshot showing Select DNS.](../../media/dns-godaddy/godaddy-manage-dns.png)
3. Under **Records**, select **Add New Record**.

    ![Screenshot of where you select Add to add an MX record.](../../media/dns-godaddy/godaddy-domains-add.png)
4. Choose **MX** option from the filter box.
5. In the boxes for the new record, type or copy and paste the values from the following table.

    (Choose the **Type** and **TTL** values from the drop-down list.)

    | Type | Name | Priority | Value | TTL |
    | --- | --- | --- | --- | --- |
    | MX | @ | 10  For more information about priority, see [What is MX priority?](../setup/domains-faq) | *&lt;domain-key&gt;*.mail.protection.outlook.com **Note:** Get your *&lt;domain-key&gt;* from your Microsoft account. [How do I find this?](../get-help-with-domains/information-for-dns-records) | 1 hour |

    ![Screenshot showing paste values for the MX record.](../../media/dns-godaddy/godaddy-domains-mxvalues.png)
6. Select **Save**.

### Add the CNAME record required for Microsoft

1. To get started, go to your domains page at GoDaddy by using [this link](https://account.godaddy.com/products/?go_redirect=disabled).

    If you're prompted to log in, use your login credentials, select your login name in the upper right, and then select **My Products**.
2. Under **Domains**, in the Portfolio tab, select the ellipse (...) next to the domain you want to verify, and select **Edit DNS** from the drop-down menu.

    ![Screenshot displaying Select DNS.](../../media/dns-godaddy/godaddy-manage-dns.png)
3. Under **Records**, select **Add New Record**.

    ![Screenshot of where you select Add to add a CNAME record.](../../media/dns-godaddy/godaddy-domains-add.png)
4. Choose **CNAME** from the drop-down list.
5. Create the CNAME record.

    In the boxes for the new record, type or copy and paste the values from the first row of the following table.

    (Choose the **TTL** value from the drop-down list.)

    | Type | Name | Value | TTL |
    | --- | --- | --- | --- |
    | CNAME | autodiscover | autodiscover.outlook.com | 1 hour |

    ![Screenshot to paste the values for the CNAME record.](../../media/dns-godaddy/godaddy-domains-cname-values.png)
6. Select **Save**.

### Add a TXT record for SPF to help prevent email spam

Important

You cannot have more than one TXT record for SPF for a domain. If your domain has more than one SPF record, you'll get email errors, as well as delivery and spam classification issues. If you already have an SPF record for your domain, don't create a new one for Microsoft. Instead, add the required Microsoft values to the current record so that you have a *single* SPF record that includes both sets of values.

1. To get started, go to your domains page at GoDaddy by using [this link](https://account.godaddy.com/products/?go_redirect=disabled).

    If you're prompted to log in, use your login credentials, select your login name in the upper right, and then select **My Products**.
2. Under **Domains**, in the Portfolio tab, select the ellipse (...) next to the domain you want to verify, and select **Edit DNS** from the drop-down menu.

    ![Screenshot showing Select DNS from the drop-down list.](../../media/dns-godaddy/godaddy-manage-dns.png)
3. Under **Records**, select **Add New Record**.

    ![Screenshot of where you select Add to add an SPF TXT record.](../../media/dns-godaddy/godaddy-domains-add.png)
4. Choose **TXT** from the drop-down list.
5. In the boxes for the new record, type or copy and paste the following values.

    (Choose the **TTL** value from the drop-down lists.)

    | Type | Name | Value | TTL |
    | --- | --- | --- | --- |
    | TXT | @ | v=spf1 include:secureserver.net -all **Note:** We recommend copying and pasting this entry, so that all of the spacing stays correct. | 1 hour |

    ![Fill in the values from the table for the SPF TXT record.](../../media/dns-godaddy/godaddy-domains-txtvalue.png)
6. Select **Save**.

## Advanced option: Microsoft Teams

Only select this option if your organization uses Microsoft Teams. Teams needs 4 records: 2 SRV records for user-to-user communication, and 2 CNAME records to sign-in and connect users to the service.

### Add the two required SRV records

1. To get started, go to your domains page at GoDaddy by using [this link](https://account.godaddy.com/products/?go_redirect=disabled).

    If you're prompted to log in, use your login credentials, select your login name in the upper right, and then select **My Products**.
2. Under **Domains**, in the Portfolio tab, select the ellipse (...) next to the domain you want to verify, and select **Edit DNS** from the drop-down menu.

    ![Screenshot showing select DNS from the drop-down list.](../../media/dns-godaddy/godaddy-manage-dns.png)
3. Under **Records**, select **Add New Record**.

    ![Screenshot of where you select Add to add an SRV record.](../../media/dns-godaddy/godaddy-domains-add.png)
4. Choose **SRV** from the drop-down list.
5. Create the first SRV record.

    In the boxes for the new record, type or copy and paste the values from the first row of the following table.

    (Choose the **Type** and **TTL** values from the drop-down lists.)

    | Type | Service | Protocol | Name | Value | Priority | Weight | Port | TTL |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | SRV | \_sip | \_tls | @ | sipdir.online.lync.com | 100 | 1 | 443 | 1 Hour |
    | SRV | \_sipfederationtls | \_tcp | @ | sipfed.online.lync.com | 100 | 1 | 5061 | 1 Hour |

    ![Fill in the values from the table for the SRV records.](../../media/dns-godaddy/godaddy-domains-srv-records.png)
6. Select **Save**.
7. Add the other SRV record by performing steps 3-5 again.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

### Add the two required CNAME records for Microsoft Teams

1. To get started, go to your domains page at GoDaddy by using [this link](https://account.godaddy.com/products/?go_redirect=disabled).

    If you're prompted to log in, use your login credentials, select your login name in the upper right, and then select **My Products**.
2. Under **Domains**, in the Portfolio tab, select the ellipse (...) next to the domain you want to verify, and select **Edit DNS** from the drop-down menu.

    ![Screenshot showing Select Manage DNS from the drop-down list.](../../media/dns-godaddy/godaddy-manage-dns.png)
3. Under **Records**, select **Add New Record**.

    ![Screenshot of where you select Add to add CNAME records for Microsoft Teams.](../../media/dns-godaddy/godaddy-domains-add.png)
4. Choose **CNAME** from the drop-down list.
5. In the empty boxes for the new records, type or copy and paste the values from the first row in the following table.

    | Type | Name | Value | TTL |
    | --- | --- | --- | --- |
    | CNAME | sip | sipdir.online.lync.com. **This value MUST end with a period (.)** | 1 Hour |
    | CNAME | lyncdiscover | webdir.online.lync.com. **This value MUST end with a period (.)** | 1 Hour |

    ![Fill in the values from the table for the CNAME records for Microsoft Teams.](../../media/dns-godaddy/godaddy-domains-cname-values.png)
6. Select **Save**.
7. Add the other CNAME record by performing steps 3-5 again.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

## Advanced option: Intune and Mobile Device Management for Microsoft 365

This service helps you secure and remotely manage mobile devices that connect to your domain. Mobile Device Management needs 2 CNAME records so that users can enroll devices to the service.

### Add the two required CNAME records Mobile Device Management

1. To get started, go to your domains page at GoDaddy by using [this link](https://account.godaddy.com/products/?go_redirect=disabled).

    If you're prompted to log in, use your login credentials, select your login name in the upper right, and then select **My Products**.
2. Under **Domains**, in the Portfolio tab, select the ellipse (...) next to the domain you want to verify, and select **Edit DNS** from the drop-down menu.

    ![Screesnhot showing Select DNS from the drop-down list.](../../media/dns-godaddy/godaddy-manage-dns.png)
3. Under **Records**, select **Add New Record**.

    ![Screenshot of where you select Add to add CNAME records for Mobile Device Management.](../../media/dns-godaddy/godaddy-domains-add.png)
4. Choose **CNAME** from the drop-down list.
5. In the empty boxes for the new records, type or copy and paste the values from the first row in the following table.

    | Type | Name | Value | TTL |
    | --- | --- | --- | --- |
    | CNAME | enterpriseregistration | enterpriseregistration.windows.net. **This value MUST end with a period (.)** | 1 Hour |
    | CNAME | enterpriseenrollment | enterpriseenrollment-s.manage.microsoft.com. **This value MUST end with a period (.)** | 1 Hour |

    ![Fill in the values from the table for the CNAME records for Mobile Device Management.](../../media/dns-godaddy/godaddy-domains-cname-values.png)
6. Select **Save**.
7. Add the other CNAME record by performing steps 3-5 again.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).