---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Connect your DNS records at 123-reg.co.uk to Microsoft 365 - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-123-reg-co-uk?view=o365-worldwide
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
- domains
ms.custom: AdminSurgePortfolio
search.appverid:
- BCS160
- MET150
- MOE150
ms.assetid: 1f2d08c9-2a88-4d2f-ae1f-e39f9e358b17
description: Learn to verify your domain and set up DNS records for email, Microsoft Teams Online, and other services at 123-reg.co.uk for Microsoft.
locale: en-us
document_id: 2ac69fb3-1a2f-cb6d-8a0b-1bbc6169e50d
document_version_independent_id: 2b9e64b6-023f-41ca-c774-c8e51e85802c
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/dns/create-dns-records-at-123-reg-co-uk.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/dns/create-dns-records-at-123-reg-co-uk
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/dns/create-dns-records-at-123-reg-co-uk.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
platformId: d0fdbe43-dad1-af48-c32f-1adc69c5e1bf
---

# Connect your DNS records at 123-reg.co.uk to Microsoft 365 - Microsoft 365 admin | Microsoft Learn

**[Check the Domains FAQ](../setup/domains-faq)** if you don't find what you're looking for.

If 123-reg.co.uk is your DNS hosting provider, follow the steps in this article to verify your domain and set up DNS records for email, Microsoft Teams Online, and so on.

After you add these records at 123-reg.co.uk, your domain will be set up to work with Microsoft services.

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

1. To get started, go to your domains page at 123-reg.co.uk and follow the prompt to log in.
2. Select **Domains**, and on the Domain name overview page, select the name of the domain that you want to verify or go to Control panel.

    ![Select the domain you want to verify.](../../media/dns-123reg/123reg-domains-1.png)
3. On the Manage domain page, under **Advanced domain settings**, choose **Manage DNS**.

    ![Select Manage DNS from the drop-down list.](../../media/dns-123reg/123reg-domains-2.png)
4. On the Manage your DNS page, select the **Advanced DNS** tab.

    ![Select the Advanced DNS tab.](../../media/dns-123reg/123reg-domains-3.png)
5. In the **Type** box for the new record choose **TXT/SPF** from the drop-down list, and then type or copy and paste the other values from the following table.

    | Hostname | Type | Destination TXT/SPF |
    | --- | --- | --- |
    | @ | TXT/SPF | MS=ms*XXXXXXXX***Note:** This is an example. Use your specific **Destination or Points to Address** value here, from the table. [How do I find this?](../get-help-with-domains/information-for-dns-records) |

    ![Select the TXT/SPF type from the drop-down list, and fill in the values.](../../media/dns-123reg/123reg-domains-typetxtspf.png)
6. Select **Add**.

    ![Screenshot of where you select Add to add a domain verification TXT record.](../../media/dns-123reg/123reg-domains-txtspf-add.png)

    Wait a few minutes before you continue, so that the record you just created can update across the Internet.

Now that you've added the record at your domain registrar's site, you'll go back to Microsoft and request a search for the record. When Microsoft finds the correct TXT record, your domain is verified.

To verify the record in Microsoft 365:

1. In the admin center, go to the **Settings** &gt; [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).
2. On the Domains page, select the domain that you're verifying, and select **Start setup**.

    ![Select Start setup.](../../media/dns-ionos/ionos-domainconnects-2.png)
3. Select **Continue**.
4. On the **Verify domain** page, select **Verify**.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

## Add an MX record so email for your domain will come to Microsoft

1. To get started, go to your domains page at 123-reg.co.uk. You'll be prompted to log in first.
2. On the Domain name overview page, select the name of the domain that you want to edit.

    ![Select the name of the domain you want to edit.](../../media/dns-123reg/123reg-domains-1.png)
3. On the Manage domain page, under **Advanced domain settings**, choose **Manage DNS**.

    ![Select Manage DNS from the drop-down list.](../../media/dns-123reg/123reg-domains-2.png)
4. On the Manage your DNS page, select the **Advanced DNS** tab.

    ![Select the Advanced DNS tab.](../../media/dns-123reg/123reg-domains-3.png)
5. In the **Type** box for the new record choose **MX** from the drop-down list, and then type or copy and paste the other values from the following table.

    | Hostname | Type | Priority | Destination MX |
    | --- | --- | --- | --- |
    | @ | MX | 1  For more information about priority, see [What is MX priority?](../setup/domains-faq) | *&lt;domain-key&gt;*.mail.protection.outlook.com. **This value MUST end with a period (.)** **Note:** Get your &lt;domain-key&gt; from your Microsoft account. [How do I find this?](../get-help-with-domains/information-for-dns-records) |

    ![Select the MX type from the drop-down list, and fill in the values.](../../media/dns-123reg/123reg-domains-mx.png)
6. Select **Add**.

    ![Screenshot of where you select Add to add an MX record.](../../media/dns-123reg/123reg-domains-mx-add.png)
7. If there are any other MX records, remove each one by selecting the **Delete (trash can)** icon for that record.

    ![Select Delete (trash can).](../../media/dns-123reg/123reg-domains-mx-delete.png)

## Add the CNAME record required for Microsoft

1. To get started, go to your domains page at 123-reg.co.uk. You'll be prompted to log in first.
2. On the Domain name overview page, select the name of the domain that you want to edit.

    ![Select the name of the domain you want to edit.](../../media/dns-123reg/123reg-domains-1.png)
3. On the Manage domain page, under **Advanced domain settings**, choose **Manage DNS**.

    ![Select Manage DNS from the drop-down list.](../../media/dns-123reg/123reg-domains-2.png)
4. On the Manage your DNS page, select the **Advanced DNS** tab.

    ![Select the Advanced DNS tab.](../../media/dns-123reg/123reg-domains-3.png)
5. Add the CNAME record.

    In the **Type** box for the new record choose **CNAME** from the drop-down list, and then type or copy and paste the other values from the following table.

    | Hostname | Type | Destination CNAME |
    | --- | --- | --- |
    | autodiscover | CNAME | autodiscover.outlook.com. **This value MUST end with a period (.)** |

    ![Select the CNAME type from the drop-down list, and fill in the values.](../../media/dns-123reg/123reg-domains-cname.png)
6. Select **Add**.

    ![Screenshot of where you select Add to add a CNAME record.](../../media/dns-123reg/123reg-domains-cname-add.png)

## Add a TXT record for SPF to help prevent email spam

Important

You cannot have more than one TXT record for SPF for a domain. If your domain has more than one SPF record, you'll get email errors, as well as delivery and spam classification issues. If you already have an SPF record for your domain, don't create a new one for Microsoft. Instead, add the required Microsoft values to the current record so that you have a *single* SPF record that includes both sets of values. Need examples? Check out these [External Domain Name System records for Microsoft](../../enterprise/external-domain-name-system-records). To validate your SPF record, you can use one of these [SPF validation tools](../setup/domains-faq).

1. To get started, go to your domains page at 123-reg.co.uk. You'll be prompted to log in first.
2. On the Domain name overview page, select the name of the domain that you want to edit.

    ![Select the name of the domain you want to edit.](../../media/dns-123reg/123reg-domains-1.png)
3. On the Manage domain page, under **Advanced domain settings**, choose **Manage DNS**.

    ![Select Manage DNS from the drop-down list.](../../media/dns-123reg/123reg-domains-2.png)
4. On the Manage your DNS page, select the **Advanced DNS** tab.

    ![Select the Advanced DNS tab.](../../media/dns-123reg/123reg-domains-3.png)
5. In the **Type** box for the new record choose **TXT/SPF** from the drop-down list, and then type or copy and paste the other values from the following table.

    | Hostname | Type | Destination TXT/SPF |
    | --- | --- | --- |
    | @ | TXT/SPF | v=spf1 include:spf.protection.outlook.com -all **Note:** We recommend copying and pasting this entry, so that all of the spacing stays correct. |

    ![Select the TXT/SPF type from the drop-down list, and fill in the values.](../../media/dns-123reg/123reg-domains-typetxtspf.png)
6. Select **Add**.

## Advanced option: Microsoft Teams

Only select this option if your organization uses Microsoft Teams for online communication services like chat, conference calls, and video calls, in addition to Microsoft Teams. Skype needs 4 records: 2 SRV records for user-to-user communication, and 2 CNAME records to sign-in and connect users to the service.

### Add the two required SRV records

1. To get started, go to your domains page at 123-reg.co.uk. You'll be prompted to log in first.
2. On the Domain name overview page, select the name of the domain that you want to edit.

    ![Select the name of the domain you want to edit.](../../media/dns-123reg/123reg-domains-1.png)
3. On the Manage domain page, under **Advanced domain settings**, choose **Manage DNS**.

    ![Select Manage DNS from the drop-down list.](../../media/dns-123reg/123reg-domains-2.png)
4. On the Manage your DNS page, select the **Advanced DNS** tab.

    ![Select the Advanced DNS tab.](../../media/dns-123reg/123reg-domains-3.png)
5. Add the first of the two SRV records:

    In the **Type** box for the new record choose **SRV** from the drop-down list, and then type or copy and paste the other values from the following table.

    | Hostname | Type | Priority | TTL | Destination SRV |
    | --- | --- | --- | --- | --- |
    | \_sip.\_tls | SRV | 100 | 3600 | 1 443 sipdir.online.lync.com. **This value MUST end with a period (.)** **Note:** We recommend copying and pasting this entry, so that all of the spacing stays correct. |
    | \_sipfederationtls.\_tcp | SRV | 100 | 3600 | 1 5061 sipfed.online.lync.com. **This value MUST end with a period (.)** **Note:** We recommend copying and pasting this entry, so that all of the spacing stays correct. |

    ![Select the TXT/SPF type from the drop-down list, and fill in the values.](../../media/dns-123reg/123reg-domains-typetxtspf.png)
6. Select **Add**.

    ![Screenshot of where you select Add to add an SRV record.](../../media/dns-123reg/123reg-domains-txtspf-add.png)
7. Add the other SRV record.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

### Add the two required CNAME records for Microsoft Teams

1. To get started, go to your domains page at 123-reg.co.uk. You'll be prompted to log in first.
2. On the Domain name overview page, select the name of the domain that you want to edit.

    ![Select the name of the domain you want to edit.](../../media/dns-123reg/123reg-domains-1.png)
3. On the Manage domain page, under **Advanced domain settings**, choose **Manage DNS**.

    ![Select Manage DNS from the drop-down list.](../../media/dns-123reg/123reg-domains-2.png)
4. On the Manage your DNS page, select the **Advanced DNS** tab.

    ![Select the Advanced DNS tab.](../../media/dns-123reg/123reg-domains-3.png)
5. Add the first CNAME record.

    In the **Type** box for the new record choose **CNAME** from the drop-down list, and then type or copy and paste the other values from the following table.

    | Hostname | Type | Destination CNAME |
    | --- | --- | --- |
    | sip | CNAME | sipdir.online.lync.com. **This value MUST end with a period (.)** |
    | lyncdiscover | CNAME | webdir.online.lync.com. **This value MUST end with a period (.)** |

    ![Select the CNAME type from the drop-down list, and fill in the values.](../../media/dns-123reg/123reg-domains-cname.png)
6. Select **Add**.

    ![Screenshot of where you select Add to add CNAME records for Microsoft Teams.](../../media/dns-123reg/123reg-domains-cname-add.png)
7. Add the other CNAME record.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

## Advanced option: Intune and Mobile Device Management for Microsoft 365

This service helps you secure and remotely manage mobile devices that connect to your domain. Mobile Device Management needs two CNAME records so that users can enroll devices to the service.

### Add the two required CNAME records for Mobile Device Management

1. To get started, go to your domains page at 123-reg.co.uk. You'll be prompted to log in first.
2. On the Domain name overview page, select the name of the domain that you want to edit.

    ![Select the name of the domain you want to edit.](../../media/dns-123reg/123reg-domains-1.png)
3. On the Manage domain page, under **Advanced domain settings**, choose **Manage DNS**.

    ![Select Manage DNS from the drop-down list.](../../media/dns-123reg/123reg-domains-2.png)
4. On the Manage your DNS page, select the **Advanced DNS** tab.

    ![Select the Advanced DNS tab.](../../media/dns-123reg/123reg-domains-3.png)
5. Add the first CNAME record.

    In the **Type** box for the new record choose **CNAME** from the drop-down list, and then type or copy and paste the other values from the following table.

    | Hostname | Type | Destination CNAME |
    | --- | --- | --- |
    | enterpriseregistration | CNAME | enterpriseregistration.windows.net. **This value MUST end with a period (.)** |
    | enterpriseenrollment | CNAME | enterpriseenrollment.manage.microsoft.com. **This value MUST end with a period (.)** |

    ![Select the CNAME type from the drop-down list, and fill in the values.](../../media/dns-123reg/123reg-domains-cname.png)
6. Select **Add**.

    ![Screenshot of where you select Add to add CNAME records for Mobile Device Management.](../../media/dns-123reg/123reg-domains-cname-add.png)
7. Add the other CNAME record.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).