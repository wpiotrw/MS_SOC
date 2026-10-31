---
layout: Conceptual
title: Configure IRM to use an on-premises AD RMS server | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/configure-irm-to-use-an-on-premises-ad-rms-server
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- MET150
ms.assetid: 3ecde857-4b7c-451d-b4aa-9eeffc8a8c61
ms.collection:
- purview-compliance
description: Learn how to configure Information Rights Management (IRM) in Exchange Online to use an Active Directory Rights Management Service (AD RMS) server.
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 6207fc32-8204-8a9f-eecf-7d67f9e0b093
document_version_independent_id: 6207fc32-8204-8a9f-eecf-7d67f9e0b093
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/configure-irm-to-use-an-on-premises-ad-rms-server.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: configure-irm-to-use-an-on-premises-ad-rms-server
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/configure-irm-to-use-an-on-premises-ad-rms-server.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1cfdec6-b0c3-4209-818c-736879856e0e
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d0723c1-cf38-4c30-ab3d-5df787b33270
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
platformId: ec0479d6-ebf0-a884-57dc-146a1b4a3b04
---

# Configure IRM to use an on-premises AD RMS server | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

For use with on-premises deployments, Information Rights Management (IRM) in Exchange Online uses Active Directory Rights Management Services (AD RMS), an information protection technology in Windows Server 2008 and later. IRM protection is applied to email by applying an AD RMS rights policy template to an email message. Rights are attached to the message itself so that protection occurs online and offline and inside and outside of your organization's firewall.

This topic shows you how to configure IRM to use an AD RMS server. For information about using Microsoft Purview Message Encryption with Microsoft Entra ID and the Azure Rights Management service, see the [Message encryption FAQ](ome-faq).

To learn more about IRM in Exchange Online, see [Information Rights Management in Exchange Online](information-rights-management-in-exchange-online).

## What do you need to know before you begin?

- Estimated time to complete this task: 30 minutes
- You need to be assigned permissions before you can perform this procedure or procedures. To see what permissions you need, see the "Information Rights Management" entry in the [Messaging policy and compliance permissions](/en-us/Exchange/permissions/feature-permissions/policy-and-compliance-permissions) topic.
- The AD RMS server must be running Windows Server 2008 or later. For details about how to deploy AD RMS, see [Installing an AD RMS Cluster](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc726041%28v=ws.11%29).
- For details about how to install and configure Windows PowerShell and connect to the service, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
- For information about keyboard shortcuts that may apply to the procedures in this topic, see [Keyboard shortcuts for the Exchange admin center in Exchange Online](/en-us/Exchange/accessibility/keyboard-shortcuts-in-admin-center).

## How do you do this?

Complete the following steps to export the trusted publishing domain, import it into Exchange Online, distribute a rights policy template, and enable IRM.

### Step 1: Use the AD RMS console to export a trusted publishing domain (TPD) from an AD RMS server

The first step is to export a trusted publishing domain (TPD) from the on-premises AD RMS server to an XML file. The TPD contains the following settings needed to use RMS features:

- The server licensor certificate (SLC) used for signing and encrypting certificates and licenses
- The URLs used for licensing and publishing
- The AD RMS rights policy templates that were created with the specific SLC for that TPD

When you import the TPD, it's stored and protected in Exchange Online.

1. Open the Active Directory Rights Management Services console, and then expand the AD RMS cluster.
2. In the console tree, expand **Trust Policies**, and then click **Trusted Publishing Domains**.
3. In the results pane, select the certificate for the domain you want to export.
4. In the **Actions** pane, click **Export Trusted Publishing Domain**.
5. In the **Publishing domain file** box, click **Save As** to save the file to a specific location on the local computer. Type a file name, making sure to specify the `.xml` file name extension, and then click **Save**.
6. In the **Password** and **Confirm Password** boxes, type a strong password that will be used to encrypt the trusted publishing domain file. You will have to specify this password when you import the TPD to your cloud-based email organization.

### Step 2: Use the Exchange Management Shell to import the TPD to Exchange Online

After the TPD is exported to an XML file, you have to import it to Exchange Online. When a TPD is imported, your organization's AD RMS templates are also imported. When the first TPD is imported, it becomes the default TPD for your cloud-based organization. If you import another TPD, you can use the `-Default` switch on the `Import-RMSTrustedPublishingDomain` cmdlet to make that TPD the default for your organization, so its templates are available to users.

To import the TPD into Exchange Online so the associated AD RMS templates become available to your organization, run the following command in Exchange Online PowerShell:

```powershell
Import-RMSTrustedPublishingDomain -FileData ([System.IO.File]::ReadAllBytes('<path to exported TPD file>')) -Name "<name of TPD>" -ExtranetLicensingUrl <URL> -IntranetLicensingUrl <URL>
```

The following table describes each parameter:

| Parameter | Value to provide |
| --- | --- |
| *FileData* | The byte content of the exported TPD XML file. Specify the full file path in the `ReadAllBytes` method. |
| *Name* | A display name for the TPD in Exchange Online. |
| *ExtranetLicensingUrl* | The external licensing URL of the AD RMS cluster. |
| *IntranetLicensingUrl* | The internal licensing URL of the AD RMS cluster. |

You can obtain the values for the *ExtranetLicensingUrl* and *IntranetLicensingUrl* parameters in the Active Directory Rights Management Services console. Select the AD RMS cluster in the console tree. The licensing URLs are displayed in the results pane. These URLs are used by email clients when content has to be decrypted and when Exchange Online needs to determine which TPD to use.

When you run this command, you'll be prompted for a password. Enter the password that you specified when you exported the TPD from your AD RMS server.

The following example imports an exported TPD file and specifies the internal and external licensing URLs required for AD RMS integration. In this case, the TPD XML file was exported from the AD RMS server and saved to the desktop of the Administrator account. The Name parameter is used to specify a name for the imported TPD.

```powershell
Import-RMSTrustedPublishingDomain -FileData ([System.IO.File]::ReadAllBytes('C:\Users\Administrator\Desktop\ExportTPD.xml')) -Name "Exported TPD" -ExtranetLicensingUrl https://corp.contoso.com/_wmcs/licensing -IntranetLicensingUrl https://rmsserver/_wmcs/licensing
```

For detailed syntax and parameter information, see [Import-RMSTrustedPublishingDomain](/en-us/powershell/module/exchange/import-rmstrustedpublishingdomain).

#### How do you know that you successfully imported the TPD?

To verify that you have successfully imported the TPD, run the **Get-RMSTrustedPublishingDomain** cmdlet to retrieve TPDs in your Exchange Online organization. For details, see the examples in [Get-RMSTrustedPublishingDomain](/en-us/powershell/module/exchange/get-rmstrustedpublishingdomain).

### Step 3: Use the Exchange Management Shell to distribute an AD RMS rights policy template

After you import the TPD, you must make sure an AD RMS rights policy template is distributed. A distributed template is visible to Outlook on the web (formerly known as Outlook Web App) users, who can then apply the templates to an email message.

To verify which RMS templates are available in the default TPD after the import, list all templates by running the following command:

```powershell
Get-RMSTemplate -Type All | fl
```

If the value of the *Type* parameter is `Archived`, the template isn't visible to users. Only distributed templates in the default TPD are available in Outlook on the web.

To make a specific RMS template available to users in Outlook on the web, set its type to Distributed by running the following command:

```powershell
Set-RMSTemplate -Identity "<name of the template>" -Type Distributed
```

For example, to distribute the Company Confidential template so that users can apply it to messages, run the following command:

```powershell
Set-RMSTemplate -Identity "Company Confidential" -Type Distributed
```

For detailed syntax and parameter information, see [Get-RMSTemplate](/en-us/powershell/module/exchange/get-rmstemplate) and [Set-RMSTemplate](/en-us/powershell/module/exchange/set-rmstemplate).

#### The Do Not Forward template

When you import the default TPD from your on-premises organization into Exchange Online, one AD RMS rights policy template named **Do Not Forward** is imported. By default, this template is distributed when you import the default TPD. You can't use the **Set-RMSTemplate** cmdlet to modify the **Do Not Forward** template.

When the **Do Not Forward** template is applied to a message, only the recipients addressed in the message can read the message. Additionally, recipients can't do the following:

- Forward the message to another person.
- Copy content from the message.
- Print the message.

Important

The **Do Not Forward** template can't prevent information in a message from being copied with third-party screen capture programs, cameras, or users manually transcribing the information

You can create additional AD RMS rights policy templates on the AD RMS server in your on-premises organization to meet your IRM protection requirements. If you create additional AD RMS rights policy templates, you have to export the TPD from the on-premises AD RMS server again and refresh the TPD in the cloud-based email organization.

#### How do you know that you successfully distributed the AD RMS rights policy template?

To verify that you have successfully distributed and AD RMS rights policy template, run the **Get-RMSTemplate** cmdlet to check the template's properties. For details, see the examples in [Get-RMSTemplate](/en-us/powershell/module/exchange/get-rmstemplate).

### Step 4: Use the Exchange Management Shell to enable IRM

After you import the TPD and distribute an AD RMS rights policy template, enable internal licensing so that Exchange Online can apply and consume IRM-protected content. Run the following command to enable IRM for your cloud-based email organization.

```powershell
Set-IRMConfiguration -InternalLicensingEnabled $true
```

For detailed syntax and parameter information, see [Set-IRMConfiguration](/en-us/powershell/module/exchange/set-irmconfiguration).

#### How do you know that you successfully enabled IRM?

To verify that you have successfully enabled IRM, run the [Get-IRMConfiguration](/en-us/powershell/module/exchange/get-irmconfiguration) cmdlet to check IRM configuration in the Exchange Online organization.

## Verify that IRM is working

### Verify the full IRM configuration

To verify that you have successfully imported the TPD and enabled IRM, do the following:

- Use the **Test-IRMConfiguration** cmdlet to test IRM functionality. For details, see the [Test-IRMConfiguration examples](/en-us/powershell/module/exchange/test-irmconfiguration#examples).
- Compose a new message in Outlook on the web and IRM-protect it by selecting **Set permissions** option from the extended menu (![Image of the More Options button used to open additional actions in Outlook on the web.](media/itpro-eac-moreoptionsicon.gif)).