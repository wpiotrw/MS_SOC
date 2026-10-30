---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Connect DNS Records at Namecheap to Microsoft 365 - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-namecheap?view=o365-worldwide
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
ms.date: 2026-06-12T00:00:00.0000000Z
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
ms.assetid: 54ae2002-b38e-43a1-82fa-3e49d78fda56
description: Learn how to connect DNS records at Namecheap to Microsoft 365. Add TXT, MX, CNAME, and SRV records for email, Teams, and Intune. Get started today.
locale: en-us
document_id: 2a5a6649-19ba-86b0-bd19-2250c9b66968
document_version_independent_id: 17867a08-ec7c-f5bb-7a03-94e9027ff0f8
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/dns/create-dns-records-at-namecheap.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/dns/create-dns-records-at-namecheap
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/dns/create-dns-records-at-namecheap.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 0baeff09-f46a-24c6-ec1a-d68532cf619c
---

# Connect DNS Records at Namecheap to Microsoft 365 - Microsoft 365 admin | Microsoft Learn

If Namecheap hosts your domain's DNS, follow the steps in this article to verify domain ownership and manually add the DNS records required for Microsoft 365 services such as email, Microsoft Teams, and device management. After you add these records at Namecheap, your domain is ready to work with Microsoft 365.

This article covers the creation of the following DNS records at Namecheap:

| **Service** | **DNS record types** |
| --- | --- |
| [**Domain verification**](create-dns-records-at-namecheap?&amp;tabs=domain-verify#add-microsoft-365-dns-records-at-namecheap) | TXT |
| [**Email**](create-dns-records-at-namecheap?&amp;tabs=email#add-microsoft-365-dns-records-at-namecheap) | MX, CNAME (Autodiscover), TXT (SPF) |
| [**Microsoft Teams**](create-dns-records-at-namecheap?&amp;tabs=teams#add-microsoft-365-dns-records-at-namecheap) | SRV (2), CNAME (2) |
| [**Microsoft Intune/MDM**](create-dns-records-at-namecheap?&amp;tabs=intune-mdm#add-microsoft-365-dns-records-at-namecheap) | CNAME (2) |

Note

Namecheap is a non-Microsoft site. Microsoft doesn't control the Namecheap site. Additionally, Namecheap might change their website and tools so that the steps in this article are no longer valid. For support with Namecheap's site and tools, contact Namecheap support.

## Before you begin

- You must own a domain registered with Namecheap.
- You must add the domain in the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339). If the domain isn't added in the Microsoft 365 admin center, follow the steps in [Add a domain](/en-us/admin/setup/add-domain#add-a-domain) to add your domain before you start adding DNS records at Namecheap.

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

## Sign in to Namecheap to manage your domain's DNS records

To add DNS records at Namecheap, sign in to your Namecheap account and then go to the page where you can manage your domain's DNS records. Follow these steps to get there:

1. Sign in to your Namecheap domains page by going to the Namecheap [Log in to your account](https://www.namecheap.com/myaccount/login.aspx?ReturnUrl=%2f) page.

    [![Screenshot of the Namecheap account login page showing username and password fields for signing in to manage DNS records.](../../media/1827f9fc-4dc9-4f9d-a392-7817c47b00b3.png)](../../media/1827f9fc-4dc9-4f9d-a392-7817c47b00b3.png#lightbox)
2. On the landing page, under **Account**, choose **Domain List** from the drop-down list.

    [![Screenshot of the Namecheap Account drop-down menu showing the Domain List option selected to manage domain DNS settings.](../../media/3f457d64-4589-422c-ae34-fc24b0e819eb.png)](../../media/3f457d64-4589-422c-ae34-fc24b0e819eb.png#lightbox)
3. On the **Domain List** page, select the domain that you want to edit, and then select **Manage**.

    [![Screenshot of the Namecheap Domain List page with the Manage option highlighted, used to access DNS record settings for a domain.](../../media/fb2020d8-707c-4148-835e-304ac6244d66.png)](../../media/fb2020d8-707c-4148-835e-304ac6244d66.png#lightbox)
4. Select **Advanced DNS**.

    [![Screenshot of the Namecheap domain management page with the Advanced DNS tab selected to access DNS record configuration.](../../media/05a4f0b9-1d27-448e-9954-2b23304c5f65.png)](../../media/05a4f0b9-1d27-448e-9954-2b23304c5f65.png#lightbox)

## Add Microsoft 365 DNS records at Namecheap

To add required DNS records at Namecheap for Microsoft 365 services, select the tab based on which DNS records you need to add:

- [**Domain Verification**](create-dns-records-at-namecheap?&amp;tabs=domain-verify#add-microsoft-365-dns-records-at-namecheap).
- [**Email**](create-dns-records-at-namecheap?&amp;tabs=email#add-microsoft-365-dns-records-at-namecheap).
- [**Microsoft Teams**](create-dns-records-at-namecheap?&amp;tabs=teams#add-microsoft-365-dns-records-at-namecheap).
- [**Microsoft Intune/Mobile Device Management for Microsoft 365**](create-dns-records-at-namecheap?&amp;tabs=intune-mdm#add-microsoft-365-dns-records-at-namecheap).

# [Domain Verify](#tab/domain-verify)
#### Add a TXT record for domain ownership verification

Before you can use your domain with Microsoft 365, you need to prove you own the domain. Your ability to sign in to your account at your domain registrar and create the DNS record proves to Microsoft that you own the domain. This process involves creating a TXT record at your domain registrar with a specific value that Microsoft can look for. When Microsoft finds the record with the correct value, your domain is verified. The TXT record is used only to verify that you own your domain. It doesn't affect anything else and can be deleted once domain verification is complete.

Note

The procedures in this section assume that you started the process of [adding a domain](/en-us/admin/setup/add-domain#add-a-domain), but you didn't verify domain ownership yet.

To add the TXT record for domain verification at Namecheap, follow these steps:

1. Get the **TXT** value specific for your domain from the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339). For help on finding the value of your TXT record in the Microsoft 365 admin center, see [Gather the information you need to create DNS records](../get-help-with-domains/information-for-dns-records#step-1-find-the-txt-record-value-and-verify).
2. If you're not already signed in to the Namecheap **Advanced DNS** page for your domain, follow the steps in Sign in to Namecheap to manage your domain's DNS records to get there.
3. In the **HOST RECORDS** section, select **ADD NEW RECORD**.

    [![Screenshot of the Namecheap Host Records section with the ADD NEW RECORD button highlighted to add a new DNS record.](../../media/8849abfe-deb6-4f6a-b56d-e69be9a28b0f.png)](../../media/8849abfe-deb6-4f6a-b56d-e69be9a28b0f.png#lightbox)
4. In the **Type** drop-down, select **TXT Record**. The **Type** drop-down automatically appears when you select **ADD NEW RECORD**.

    [![Screenshot of the Namecheap Type drop-down menu with TXT Record selected for adding a domain verification DNS record.](../../media/a5b40973-19b5-4c32-8e1b-1521aa971836.png)](../../media/a5b40973-19b5-4c32-8e1b-1521aa971836.png#lightbox)
5. In the boxes for the new record, enter the values from the following table:

    | **Type** | **Host** | **Value** | **TTL** |
    | --- | --- | --- | --- |
    | TXT | @ | *MS=msXXXXXXXX* | 30 min |

    - In the **Value** field, replace *MS=msXXXXXXXX* with the TXT value you gathered earlier from the Microsoft 365 admin center. The value shown in the table is only an example.
    - Select the **TTL** value from the drop-down menu.

    [![Screenshot of the Namecheap new record fields with host, value, and TTL values entered for the domain verification TXT record.](../../media/fe75c0fd-f85c-4bef-8068-edaf9779b7f1.png)](../../media/fe75c0fd-f85c-4bef-8068-edaf9779b7f1.png#lightbox)
6. Select the **Save Changes** ✅ check mark icon or select the **Save All Changes** button located just below the record you added.

    [![Screenshot of the Namecheap Save Changes check mark icon used to save the domain verification TXT record entry.](../../media/b48d2c67-66b5-4aa4-8e59-0c764f236fac.png)](../../media/b48d2c67-66b5-4aa4-8e59-0c764f236fac.png#lightbox)
7. Wait a few minutes for the TXT record to propagate before continuing.

Now that you added the TXT record at your domain registrar's site, go back to the Microsoft 365 admin center and complete the domain ownership verification process. When Microsoft 365 finds the correct TXT record, your domain is verified.

To verify the record in the Microsoft 365 admin center, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. From the left navigation bar, select **... Show all**, and then select **Settings** to expand it.
3. Under **Settings**, select [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).
4. In the **Domains** page, select the ellipsis **⋮** next to the domain that you're verifying, and then select **Start setup**.

    [![Screenshot of the Microsoft 365 admin center Domains page with the Start setup option selected to begin domain verification.](../../media/dns-ionos/ionos-domainconnects-2.png)](../../media/dns-ionos/ionos-domainconnects-2.png#lightbox)
5. In the **Verify you own your domain** page, make sure **Add a TXT record to the domain's DNS records** is selected, and then select **Continue**.
6. On the **Add a record to verify domain ownership** page, select **Verify**.
7. After you verify domain ownership, the **How do you want to connect your domain?** page appears. The rest of the wizard walks you through adding additional DNS records to connect your domain to Microsoft 365 services. For more information, see the following article or the following sections in this article:

    - [Connect to Microsoft services by adding DNS records](../get-help-with-domains/create-dns-records-at-any-dns-hosting-provider?&amp;tabs=manual#step-2-connect-to-microsoft-services-by-adding-dns-records).
    - [Add an MX record to enable email delivery to Microsoft 365](create-dns-records-at-namecheap?&amp;tabs=email#add-an-mx-record-to-enable-email-delivery-to-microsoft-365).
    - [Add a CNAME record so email accounts are automatically set up in Outlook and other email clients](create-dns-records-at-namecheap?&amp;tabs=email#add-a-cname-record-so-email-accounts-are-automatically-set-up-in-outlook-and-other-email-clients).
    - [Add an SPF TXT record to help prevent email spam](create-dns-records-at-namecheap?&amp;tabs=email#add-an-spf-txt-record-to-help-prevent-email-spam).
    - [DNS records for Microsoft Teams](create-dns-records-at-namecheap?&amp;tabs=teams#dns-records-for-microsoft-teams).
    - [DNS records for Microsoft Intune and Mobile Device Management for Microsoft 365](create-dns-records-at-namecheap?&amp;tabs=intune-mdm#dns-records-for-microsoft-intune-and-mobile-device-management-for-microsoft-365).

# [Email](#tab/email)
#### DNS records for Microsoft 365 email

Microsoft 365 email requires three types of DNS records:

- An MX record for email delivery.
- A CNAME record for email account discovery.
- A TXT record for SPF email spam protection.

To add each of these types of records at Namecheap, follow the steps in the following sections.

##### Add an MX record to enable email delivery to Microsoft 365

To add the MX record for email at Namecheap, follow these steps:

1. Get the **MX** value specific for your domain from the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339). For help on finding the value of your MX record in the Microsoft 365 admin center, see [Gather the information you need to create DNS records](../get-help-with-domains/information-for-dns-records#step-2-find-the-mx-record-value-for-email-and-more).
2. If you're not already signed in to the Namecheap **Advanced DNS** page for your domain, follow the steps in Sign in to Namecheap to manage your domain's DNS records to get there.
3. In the **MAIL SETTINGS** section, select **Custom MX** from the **Email Forwarding** drop-down list. You might have to scroll down the drop-down list to find it.

    [![Screenshot of the Namecheap Mail Settings section with Custom MX selected from the Email Forwarding drop-down menu.](../../media/40199e2c-42cf-4c3f-9936-3cbe5d4e81a4.png)](../../media/40199e2c-42cf-4c3f-9936-3cbe5d4e81a4.png#lightbox)
4. Select **ADD NEW RECORD**.

    [![Screenshot of the Namecheap Mail Settings section showing the ADD NEW RECORD button used to add a new MX DNS record.](../../media/8d169b81-ba48-4d51-84ea-a08fa1616457.png)](../../media/8d169b81-ba48-4d51-84ea-a08fa1616457.png#lightbox)
5. In the boxes for the new record, enter the values from the following table:

    | **Type** | **Host** | **Value** | **Priority** | **TTL** |
    | --- | --- | --- | --- | --- |
    | MX Record | @ | 0 *&lt;mx-value&gt;*.mail.protection.outlook.com. | 0 | 30 min |

    - In the **Value** field, replace *&lt;mx-value&gt;* with the MX value you gathered earlier from the Microsoft 365 admin center. Make sure this entry ends with a period (**.**). The value shown in the table is only an example.
    - The **Priority** box is the unnamed box to the right of the **Value** box. For more information about priority, see [What is MX priority?](../setup/domains-faq#what-is-mx-priority)
    - Select the **TTL** value from the drop-down menu.

    [![Screenshot of the Namecheap new record fields showing host, value, priority, and TTL values entered for the MX email record.](../../media/f3b76d62-5022-48c1-901b-8615a8571309.png)](../../media/f3b76d62-5022-48c1-901b-8615a8571309.png#lightbox)
6. Select the **Save Changes** ✅ check mark icon.

    [![Screenshot of the Namecheap Save Changes check mark icon used to save the MX record for Microsoft 365 email delivery.](../../media/ef4e3112-36d2-47c8-a478-136a565dd71d.png)](../../media/ef4e3112-36d2-47c8-a478-136a565dd71d.png#lightbox)
7. Remove all previous MX records except for the one that you just added. Use the following two-step process to remove each of them:

    1. First, select **Delete** (trash can) for the record that you want to remove.

        [![Screenshot of the Namecheap Delete trash can icon used to remove an existing MX record from the DNS settings.](../../media/7a7a751f-29c2-495f-8f55-98ca37ce555a.png)](../../media/7a7a751f-29c2-495f-8f55-98ca37ce555a.png#lightbox)
    2. Second, select **Yes** to confirm the deletion.

        [![Screenshot of the Namecheap confirmation dialog with the Yes button selected to confirm deletion of an MX record.](../../media/85ebc0c7-8787-43ee-9e7b-647375b3345c.png)](../../media/85ebc0c7-8787-43ee-9e7b-647375b3345c.png#lightbox)

##### Add a CNAME record so email accounts are automatically set up in Outlook and other email clients

To add a CNAME record for email account discovery at Namecheap, follow these steps:

1. If you're not already signed in to the Namecheap **Advanced DNS** page for your domain, follow the steps in Sign in to Namecheap to manage your domain's DNS records to get there.
2. In the **HOST RECORDS** section, select **ADD NEW RECORD**.

    [![Screenshot of the Host Records section with ADD NEW RECORD highlighted.](../../media/8849abfe-deb6-4f6a-b56d-e69be9a28b0f.png)](../../media/8849abfe-deb6-4f6a-b56d-e69be9a28b0f.png#lightbox)
3. In the **Type** drop-down, select **CNAME Record**. The **Type** drop-down automatically appears when you select **ADD NEW RECORD**.

    [![Screenshot of the Namecheap Type drop-down menu with CNAME Record selected for adding an Autodiscover DNS record.](../../media/0898f3b2-06ab-4364-a86a-a603a25b39f4.png)](../../media/0898f3b2-06ab-4364-a86a-a603a25b39f4.png#lightbox)
4. In the empty boxes for the new record, select **CNAME** for the **Record Type**, and then enter the values from the following table:

    | **Type** | **Host** | **Value** | **TTL** |
    | --- | --- | --- | --- |
    | CNAME | autodiscover | autodiscover.outlook.com. | Automatic |

    Important

    Make sure the **Value***autodiscover.outlook.com.* ends with a period (**.**).

    [![Screenshot of the Namecheap new record fields showing host and value entries for the Autodiscover CNAME DNS record.](../../media/f79c5679-34eb-4544-8517-caa2e8a4111a.png)](../../media/f79c5679-34eb-4544-8517-caa2e8a4111a.png#lightbox)
5. Select the **Save Changes** ✅ check mark icon.

    [![Screenshot of the Namecheap Save Changes check mark icon used to save the Autodiscover CNAME record for Microsoft 365 email.](../../media/91a5cce4-ca41-41ec-b976-aafe681a4d68.png)](../../media/91a5cce4-ca41-41ec-b976-aafe681a4d68.png#lightbox)

##### Add an SPF TXT record to help prevent email spam

Important

If your domain already has an SPF record, don't create a new one for Microsoft 365. Instead, add the required Microsoft 365 values to the existing record so that you have a *single* SPF record that includes both sets of values.

To add an SPF TXT record for email spam protection at Namecheap, follow these steps:

1. If you're not already signed in to the Namecheap **Advanced DNS** page for your domain, follow the steps in Sign in to Namecheap to manage your domain's DNS records to get there.
2. In the **HOST RECORDS** section, select **ADD NEW RECORD**.

    [![Screenshot of the Host Records section with ADD NEW RECORD highlighted.](../../media/8849abfe-deb6-4f6a-b56d-e69be9a28b0f.png)](../../media/8849abfe-deb6-4f6a-b56d-e69be9a28b0f.png#lightbox)
3. In the **Type** drop-down, select **TXT Record**. The **Type** drop-down automatically appears when you select **ADD NEW RECORD**.

    [![Screenshot of the Namecheap Type drop-down menu with TXT Record selected for adding an SPF record to prevent email spam.](../../media/c5d1fddb-28b5-48ec-91c9-3e5d3955ac80.png)](../../media/c5d1fddb-28b5-48ec-91c9-3e5d3955ac80.png#lightbox)
4. In the boxes for the new record, enter the values from the following table:

    | **Type** | **Host** | **Value** | **TTL** |
    | --- | --- | --- | --- |
    | TXT | @ | v=spf1 include:spf.protection.outlook.com -all | 30 min |

    - Select the **TTL** value from the drop-down menu.
    - Use copy and paste for this entry so that all of the spacing remains correct.

    [![Screenshot of the Namecheap new record fields showing host, value, and TTL entries for the SPF TXT record to prevent email spam.](../../media/ea0829f1-990b-424b-b26e-9859468318dd.png)](../../media/ea0829f1-990b-424b-b26e-9859468318dd.png#lightbox)
5. Select the **Save Changes** ✅ check mark icon.

    [![Screenshot of the Namecheap Save Changes check mark icon used to save the SPF TXT record for Microsoft 365 email spam protection.](../../media/f2846c36-ace3-43d8-be5d-a65e2c267619.png)](../../media/f2846c36-ace3-43d8-be5d-a65e2c267619.png#lightbox)

# [Teams](#tab/teams)
#### DNS records for Microsoft Teams

Microsoft Teams needs four records:

- Two SRV records for user-to-user communication.
- Two CNAME records to sign in and connect users to the service.

Only add these DNS records if your organization uses Microsoft Teams.

##### Add the two required SRV records for Microsoft Teams

To add SRV records for Microsoft Teams at Namecheap, follow these steps:

1. If you're not already signed in to the Namecheap **Advanced DNS** page for your domain, follow the steps in Sign in to Namecheap to manage your domain's DNS records to get there.
2. In the **HOST RECORDS** section, select **ADD NEW RECORD**.

    [![Screenshot of the Host Records section with ADD NEW RECORD highlighted.](../../media/8849abfe-deb6-4f6a-b56d-e69be9a28b0f.png)](../../media/8849abfe-deb6-4f6a-b56d-e69be9a28b0f.png#lightbox)
3. In the **Type** drop-down, select **SRV Record**. The **Type** drop-down automatically appears when you select **ADD NEW RECORD**.

    [![Screenshot of the Namecheap Type drop-down menu with SRV Record selected for adding DNS records required by Microsoft Teams.](../../media/fd55cd7c-2243-4de1-8d39-2c3f7ea3ae51.png)](../../media/fd55cd7c-2243-4de1-8d39-2c3f7ea3ae51.png#lightbox)
4. In the empty boxes for the new records, enter the values from the following table:

    | **Service** | **Protocol** | **Priority** | **Weight** | **Port** | **Target** | **TTL** |
    | --- | --- | --- | --- | --- | --- | --- |
    | \_sip | \_tls | 100 | 1 | 443 | sipdir.online.lync.com. | Automatic |
    | \_sipfederationtls | \_tcp | 100 | 1 | 5061 | sipfed.online.lync.com. | Automatic |

    Important

    Make sure both **Target** fields *sipdir.online.lync.com.* and *sipfed.online.lync.com.* end with a period (**.**).

    [![Screenshot of the Namecheap new record fields showing service, protocol, priority, weight, port, and target values for Microsoft Teams SRV records.](../../media/ff9566ea-0096-4b7f-873c-027080a23b56.png)](../../media/ff9566ea-0096-4b7f-873c-027080a23b56.png#lightbox)
5. Select the **Save Changes** ✅ check mark icon.

    [![Screenshot of the Namecheap Save Changes check mark icon used to save the SRV DNS records required for Microsoft Teams.](../../media/48a8dee4-c66d-449d-8759-9e9784c82b13.png)](../../media/48a8dee4-c66d-449d-8759-9e9784c82b13.png#lightbox)
6. Add the other SRV record by choosing the values from the second row of the table.

##### Add the two required CNAME records for Microsoft Teams

To add CNAME records for Microsoft Teams at Namecheap, follow these steps:

1. If you're not already signed in to the Namecheap **Advanced DNS** page for your domain, follow the steps in Sign in to Namecheap to manage your domain's DNS records to get there.
2. In the **HOST RECORDS** section, select **ADD NEW RECORD**.

    [![Screenshot of the Host Records section with ADD NEW RECORD highlighted.](../../media/8849abfe-deb6-4f6a-b56d-e69be9a28b0f.png)](../../media/8849abfe-deb6-4f6a-b56d-e69be9a28b0f.png#lightbox)
3. In the **Type** drop-down, select **CNAME**. The **Type** drop-down automatically appears when you select **ADD NEW RECORD**.

    [![Screenshot of the Namecheap Type drop-down menu with CNAME selected for adding DNS records required by Microsoft Teams.](../../media/fd55cd7c-2243-4de1-8d39-2c3f7ea3ae51.png)](../../media/fd55cd7c-2243-4de1-8d39-2c3f7ea3ae51.png#lightbox)
4. In the empty boxes for the new records, enter the values from the following table:

    | **Type** | **Host** | **Value** | **TTL** |
    | --- | --- | --- | --- |
    | CNAME | sip | sipdir.online.lync.com. | Automatic |
    | CNAME | lyncdiscover | webdir.online.lync.com. | Automatic |

    Important

    Make sure both **Value** fields *sipdir.online.lync.com.* and *webdir.online.lync.com.* end with a period (**.**).

    [![Screenshot of the Namecheap new record fields showing host and value entries for the sip and lyncdiscover CNAME records for Microsoft Teams.](../../media/91a5cce4-ca41-41ec-b976-aafe681a4d68.png)](../../media/91a5cce4-ca41-41ec-b976-aafe681a4d68.png#lightbox)
5. Select the **Save Changes** ✅ check mark icon.

    [![Screenshot of the Namecheap Save Changes check mark icon used to save the CNAME DNS records required for Microsoft Teams connectivity.](../../media/91a5cce4-ca41-41ec-b976-aafe681a4d68.png)](../../media/91a5cce4-ca41-41ec-b976-aafe681a4d68.png#lightbox)
6. Add the other CNAME record by choosing the values from the second row of the table.

# [Intune/MDM](#tab/intune-mdm)
#### DNS records for Microsoft Intune and Mobile Device Management for Microsoft 365

Microsoft Intune and Mobile Device Management for Microsoft 365 help you secure and remotely manage devices that connect to your domain. Mobile Device Management for Microsoft 365 needs two CNAME records so that users can enroll devices to the service. Only add these records if your organization uses Microsoft Intune or Mobile Device Management for Microsoft 365.

##### Add the two required CNAME records for Microsoft Intune and Mobile Device Management for Microsoft 365

To add CNAME records for Microsoft Intune and Mobile Device Management for Microsoft 365 at Namecheap, follow these steps:

1. If you're not already signed in to the Namecheap **Advanced DNS** page for your domain, follow the steps in Sign in to Namecheap to manage your domain's DNS records to get there.
2. In the **HOST RECORDS** section, select **ADD NEW RECORD**.

    [![Screenshot of the Host Records section with ADD NEW RECORD highlighted.](../../media/8849abfe-deb6-4f6a-b56d-e69be9a28b0f.png)](../../media/8849abfe-deb6-4f6a-b56d-e69be9a28b0f.png#lightbox)
3. In the **Type** drop-down, select **CNAME Record**. The **Type** drop-down automatically appears when you select **ADD NEW RECORD**.

    [![Screenshot of the Type drop-down with CNAME Record selected.](../../media/0898f3b2-06ab-4364-a86a-a603a25b39f4.png)](../../media/0898f3b2-06ab-4364-a86a-a603a25b39f4.png#lightbox)
4. In the empty boxes for the new records, enter the values from the first row in the following table.

    | **Type** | **Host** | **Value** | **TTL** |
    | --- | --- | --- | --- |
    | CNAME | enterpriseregistration | enterpriseregistration.windows.net. | Automatic |
    | CNAME | enterpriseenrollment | enterpriseenrollment-s.manage.microsoft.com. | Automatic |

    Important

    Make sure both **Value** fields *enterpriseregistration.windows.net.* and *enterpriseenrollment-s.manage.microsoft.com.* end with a period (**.**).

    [![Screenshot of the Namecheap new record fields showing host and value entries for the enterprise registration and enrollment CNAME records.](../../media/f79c5679-34eb-4544-8517-caa2e8a4111a.png)](../../media/f79c5679-34eb-4544-8517-caa2e8a4111a.png#lightbox)
5. Select the **Save Changes** ✅ check mark icon.

    [![Screenshot of the Namecheap Save Changes check mark icon used to save the CNAME records for Microsoft Intune device enrollment.](../../media/91a5cce4-ca41-41ec-b976-aafe681a4d68.png)](../../media/91a5cce4-ca41-41ec-b976-aafe681a4d68.png#lightbox)
6. Add the other CNAME record by choosing the values from the second row of the table.

---

## Support

If you don't find what you're looking for, check the [**Domains FAQ**](../setup/domains-faq).

Tip

Some configuration tasks might be complex to perform. For technical support, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. At the bottom right, select **Help & Support**.
3. In the **Support Assistant** pane that opens, enter your question.
4. Review the results. If you still have questions, select **Contact support**.

To learn about your options for contacting support, see [Get support for Microsoft 365 for business](/en-us/microsoft-365/admin/get-help-support).