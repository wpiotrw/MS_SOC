---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Create DNS records for Microsoft using Windows-based DNS - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-using-windows-based-dns?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: frankroj
author: frankroj
manager: dansimp
ms.date: 2026-06-16T00:00:00.0000000Z
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
- AdminTemplateSet
- domains
search.appverid:
- BCS160
- MET150
- MOE150
ms.assetid: 9eec911d-5773-422c-9593-40e1147ffbde
description: Learn to verify your domain and set up DNS records for email, Microsoft Teams Online, and other services at Windows-based DNS for Microsoft.
locale: en-us
document_id: d93d2308-0cb6-9479-f45b-7701a12dd0ee
document_version_independent_id: e4038958-6a2b-a982-ccfd-37bf3d9b03a3
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/dns/create-dns-records-using-windows-based-dns.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/dns/create-dns-records-using-windows-based-dns
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/dns/create-dns-records-using-windows-based-dns.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/fc3f72c2-fb6f-4cea-95ee-b444e52254ee
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f12cf087-582d-48ac-a085-0c19adf1e391
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 382de8ec-de16-3914-c015-90919e716f42
---

# Create DNS records for Microsoft using Windows-based DNS - Microsoft 365 admin | Microsoft Learn

If you host your own DNS records using Windows-based DNS, follow the steps in this article to manually add the DNS records required for Microsoft 365 services such as email, Microsoft Teams, and device management. After you add these records in Windows based DNS, your domain is ready to work with Microsoft 365.

To get started, you need to find your DNS records in Windows-based DNS so you can update them. Also, if you're planning to synchronize your on-premises Active Directory with Microsoft, see Non-routable email address used as a UPN in your on-premises Active Directory.

Trouble with mail flow or other issues after adding DNS records, see [Troubleshoot issues after changing your domain name or DNS records](../get-help-with-domains/find-and-fix-issues).

Note

When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](../get-help-with-domains/find-and-fix-issues).

## Find your DNS records in Windows-based DNS

To access DNS management for your domain in Windows Server, follow these steps:

1. Sign in to your Windows Server as an administrator.
2. Right-click **Start**, and then select **Run**.
3. In the **Run** dialog box, enter **dnsmgmt.msc**, and then select **OK**.
4. In the **DNS Manager** window, expand ***&lt;DNS server name&gt;* &gt; Forward Lookup Zones**.
5. Select your domain. You're now ready to create the DNS records.

## Add a TXT record for domain ownership verification

Before you can use your domain with Microsoft 365, you need to prove you own the domain. Your ability to create the DNS record on your Windows Server DNS server proves to Microsoft that you own the domain. This process involves creating a TXT record Windows Server DNS server with a specific value that Microsoft can look for. When Microsoft finds the record with the correct value, your domain is verified. The TXT record is used only to verify that you own your domain. It doesn't affect anything else and can be deleted once domain verification is complete.

Note

The procedures in this section assume that you started the process of [adding a domain](/en-us/admin/setup/add-domain#add-a-domain), but you didn't verify domain ownership yet.

To add the TXT record for domain verification on your Windows Server DNS server, follow these steps:

1. Get the **TXT** value specific for your domain from the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339). For help on finding the value of your TXT record in the Microsoft 365 admin center, see [Gather the information you need to create DNS records](../get-help-with-domains/information-for-dns-records#step-1-find-the-txt-record-value-and-verify).
2. If not already open, open **DNS Manager** as described in Find your DNS records in Windows-based DNS.
3. In **DNS Manager**, go to the **Action** menu and then select **Other New Records...**
4. Under **Select a resource record type:** in the **Resource Record Type** window, select **Text (TXT)**, and then select **Create Record...**
5. In the **New Resource Record** dialog box, enter the following values for the TXT record required for email:

    - **Record name:** @
    - **Text:***&lt;Enter the TXT value from the Microsoft 365 admin center that you obtained in step 1 here&gt;*
6. Select **OK**.

Important

In some versions of Windows Server DNS Manager, the domain might be set up so that when you create a txt record, the home name defaults to the parent domain. In this situation, when adding a TXT record, set the host name to blank (no value) instead of setting it to **@** or the domain name.

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

## Non-routable email address used as a UPN in your on-premises Active Directory

If you're planning to synchronize your on-premises Active Directory with Microsoft, make sure that the Active Directory user principal name (UPN) suffix is a valid domain suffix. Domain suffixes such as **@contoso.local** aren't supported. If you need to change your UPN suffix, see [How to prepare a non-routable domain for directory synchronization](../../enterprise/prepare-a-non-routable-domain-for-directory-synchronization).

## Add MX record

To add an MX record so email for your domain comes to Microsoft, follow these steps:

1. Get the **MX** value specific for your domain from the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339). For help on finding the value of your MX record in the Microsoft 365 admin center, see [Gather the information you need to create DNS records](../get-help-with-domains/information-for-dns-records#step-2-find-the-mx-record-value-for-email-and-more).

    The MX record looks like the following example:

    *&lt;MX token&gt;*.mail.protection.outlook.com

    Where *&lt;MX token&gt;* is a value like *MSxxxxxxx*.
2. If not already open, open **DNS Manager** as described in Find your DNS records in Windows-based DNS.
3. In **DNS Manager**, go to the **Action** menu and then select **New Mail Exchanger (MX)...**
4. In the **New Resource Record** dialog box, enter the following values:

    - **Host or child domain:***&lt;Leave this field blank&gt;*
    - **Fully qualified domain name (FQDN) of mail server:** Enter the **MX** value as determined from the Microsoft 365 admin center.
    - **Preference:** Enter the priority value for the MX record (normally **0** or **10**).
5. Select **OK**.
6. Remove any previous MX records. If you have any old MX records for this domain that route email somewhere else, select the check box next to each old record, and then select **Delete** &gt; **OK**.

## Add CNAME records

To add the required CNAME records for your domain to work with Microsoft services, follow these steps:

1. If not already open, open **DNS Manager** as described in Find your DNS records in Windows-based DNS.
2. In **DNS Manager**, go to the **Action** menu and then select **New Alias (CNAME)...**
3. In the **New Resource Record** dialog box, enter the following values for the CNAME record required for email:

    - **Alias name:** autodiscover
    - **Fully qualified domain name (FQDN) for target host:** autodiscover.outlook.com
4. Select **OK**.
5. Repeat the steps to also add the following CNAME records required for Teams and Mobile Device Management (MDM)/Microsoft Intune:

    - Teams:

        - **Alias name:** sip
        - **Fully qualified domain name (FQDN) for target host:** sipdir.online.lync.com
        - **Alias name:** lyncdiscover
        - **Fully qualified domain name (FQDN) for target host:** webdir.online.lync.com
    - Mobile Device Management (MDM)/Microsoft Intune:

        - **Alias name:** enterpriseregistration
        - **Fully qualified domain name (FQDN) for target host:** enterpriseregistration.windows.net
        - **Alias name:** enterpriseenrollment
        - **Fully qualified domain name (FQDN) for target host:** enterpriseenrollment-s.manage.microsoft.com

## Add a TXT record for SPF to help prevent email spam

Important

You can't have more than one TXT record for SPF for a domain. If your domain has more than one SPF record, email errors, delivery issues, and spam classification issues can all occur. If you already have an SPF record for your domain, don't create a new one for Microsoft. Instead, add the required Microsoft values to the current record so that you have a *single* SPF record that includes both sets of values.

To add the SPF TXT record for your domain to help prevent email spam, follow these steps:

1. If not already open, open **DNS Manager** as described in Find your DNS records in Windows-based DNS.
2. In **DNS Manager**, go to the **Action** menu and then select **Other New Records...**
3. Under **Select a resource record type:** in the **Resource Record Type** window, select **Text (TXT)**, and then select **Create Record...**
4. In the **New Resource Record** dialog box, enter the following values for the TXT record required for email:

    - **Record name:** @
    - **Text:** =spf1 include:spf.protection.outlook.com -all

    Note

    - You might already have other strings in the TXT value for this record (such as strings for marketing email). Leave those strings in place and add this one, placing double-quotes (**"**) around each string to separate them.
    - In some versions of Windows Server DNS Manager, the domain might be set up so that when you create a txt record, the home name defaults to the parent domain. In this situation, when adding a TXT record, set the host name to blank (no value) instead of setting it to **@** or the domain name.
5. Select **OK**.

## Add SRV records

To add the two SRV records that are required for Teams, follow these steps:

1. If not already open, open **DNS Manager** as described in Find your DNS records in Windows-based DNS.
2. In **DNS Manager**, go to the **Action** menu and then select **Other New Records...**
3. Under **Select a resource record type:** in the **Resource Record Type** window, select **Service Location (SRV)**, and then select **Create Record...**
4. In the **New Resource Record** dialog box, enter the following values:

    - **Service:** \_sip
    - **Protocol:** \_tls
    - **Priority:** 100
    - **Weight:** 1
    - **Port number:** 443
    - **Host offering this service:** sipdir.online.lync.com
5. Select **OK**.

## Support

If you don't find what you're looking for, check the [**Domains FAQ**](../setup/domains-faq).

Tip

Some configuration tasks might be complex to perform. For technical support, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. At the bottom right, select **Help & Support**.
3. In the **Support Assistant** pane that opens, enter your question.
4. Review the results. If you still have questions, select **Contact support**.

To learn about your options for contacting support, see [Get support for Microsoft 365 for business](/en-us/microsoft-365/admin/get-help-support).