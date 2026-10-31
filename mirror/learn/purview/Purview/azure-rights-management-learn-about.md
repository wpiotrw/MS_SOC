---
layout: Conceptual
title: Learn about the Azure Rights Management service | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/azure-rights-management-learn-about
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
ms.reviewer: tommoser
manager: laurawi
ms.date: 2025-08-25T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-encryption
ms.collection:
- purview-compliance
description: Learn about Azure Rights Management, the main encryption service from Microsoft Purview Information Protection.
locale: en-us
document_id: ac2a133d-9941-8add-0b6d-ab6441315f22
document_version_independent_id: ac2a133d-9941-8add-0b6d-ab6441315f22
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/azure-rights-management-learn-about.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: azure-rights-management-learn-about
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/azure-rights-management-learn-about.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 814c9f99-2c8f-53bc-54a8-a6dafdcefa48
---

# Learn about the Azure Rights Management service | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

The Azure Rights Management service is the main cloud-based encryption service from [Microsoft Purview Information Protection](information-protection).

Azure Rights Management helps to protect items such as files and emails across multiple devices that include phones, tablets, and PCs by using encryption, identity, and authorization policies.

For example, when employees email a document to a partner company, or save a document to their cloud drive, the persistent encryption from the Azure Rights Management service helps secure the data.

- **Encryption settings remain with your data**, even when it leaves your organization's boundaries, keeping your content protected both within and outside your organization.
- **Encryption may be legally required** for compliance, legal discovery requirements, or best practices for information management.
- **Use the Azure Rights Management service with Microsoft 365 subscriptions or subscriptions for Microsoft Purview Information Protection**. For more information, see the [Microsoft 365 licensing guidance for security & compliance](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance#information-protection/) page.

The Azure Rights Management service ensures that authorized people and services, such as search and indexing, can continue to read and inspect the encrypted data.

Ensuring ongoing access for authorized people and services, also known as "reasoning over data", is a crucial element in maintaining control of your organization's data. This capability may not be easily accomplished with other information protection solutions that use peer-to-peer encryption.

## Protection features

| Feature | Description |
| --- | --- |
| **Encrypt multiple file types** | In early implementations of Rights Management, only Office files could be encrypted, using built-in Rights Management protection. The Azure Rights Management service provides support for additional file types. For more information, see [Supported file types](information-protection-client#supported-file-types). |
| **Protect files anywhere** | When a file is encrypted, this protection stays with the file, even if it's saved or copied to storage that isn't under the control of IT, such as a cloud storage service. |

## Collaboration features

| Feature | Description |
| --- | --- |
| **Safely share information** | Encrypted files are safe to share with others, such as an attachment to an email or a link to a SharePoint site.  If the sensitive information is within an email message, encrypt the email, or use the **Do Not Forward** option from Outlook. |
| **Support for business-to-business collaboration** | Because Azure Rights Management is a cloud service, there’s usually no need to explicitly configure trusts with other organizations before you can share encrypted content with them. By default, collaboration with other organizations that already have a Microsoft 365 or a Microsoft Entra directory is automatically supported. Some [additional configuration](encryption-azure-ad-configuration) might be needed for advanced configurations or specialized scenarios. For organizations without Microsoft 365 or a Microsoft Entra directory, users can sign up for the free [RMS for individuals](/en-us/azure/information-protection/rms-for-individuals) subscription, or use a Microsoft account for [supported applications](/en-us/previous-versions/azure/information-protection/secure-collaboration-documents#supported-scenarios-for-opening-protected-documents). |

Tip

Attaching encrypted files, rather than encrypting an entire email message, enables you to keep the email text unencrypted.

For example, you may want to include instructions for first-time use if the email is being sent outside your organization. If you attach an encrypted file, the basic instructions can be read by anyone, but only authorized users will be able to open the document, even if the email or document is forwarded to other people.

## Platform support features

The Azure Rights Management service supports a broad range of platforms and applications, including:

| Feature | Description |
| --- | --- |
| **Commonly used devices**not just Windows computers | Client devices include: - Windows computers and phones - Mac computers - iOS tablets and phones - Android tablets and phones |
| **On-premises services** | In addition to working seamlessly with Microsoft 365, you can use the Azure Rights Management service with the following on-premises services when you deploy the [Microsoft Rights Management connector](/en-us/azure/information-protection/deploy-rms-connector): - Exchange Server - SharePoint Server - Windows Server running File Classification Infrastructure |
| **Application extensibility** | The Azure Rights Management service has tight integration with Microsoft 365 applications and services, and extends support for other applications by using the [Microsoft Purview Information Protection client](information-protection-client). The [Microsoft Information Protection SDK](/en-us/information-protection/develop/) provides your internal developers and software vendors with APIs to write custom applications that support the Azure Rights Management service. |

## Infrastructure features

The Azure Rights Management service provides the following features to support IT departments and infrastructure organizations:

- Create simple and flexible policies
- Easy activation
- Auditing and monitoring services
- Ability to scale across your organization
- Maintain IT control over data

Note

Organizations always have the choice to stop using the Azure Rights Management service without losing access to content that was previously protected by Azure Rights Management.

For more information, see [Decommission and deactivate the Azure Rights Management service](deactivate-rights-management-service).

#### Create simple and flexible policies

Encryption settings that are applied with [sensitivity labels](sensitivity-labels) provide a quick and easy method for administrators to apply information protection policies, and for users to apply the correct level of protection for each item as needed.

For example, for a company-wide strategy paper to be shared with all employees, apply a read-only policy to all internal employees. For a more sensitive document, such as a financial report, restrict access to executives only.

For more information, see [Restrict access to content by using sensitivity labels to apply encryption](encryption-sensitivity-labels).

#### Easy activation

For new subscriptions, activation is automatic. For existing subscriptions, [activating the Rights Management service](activate-rights-management-service) requires just two PowerShell commands.

#### Auditing and monitoring services

[Audit and monitor usage](rights-management-usage-logging) of your encrypted files, even after these files leave your organization’s boundaries.

For example, if a Contoso, Ltd employee works on a joint project with three people from Fabrikam, Inc, they might send their Fabrikam partners a document that's encrypted and restricted to *read-only*.

Auditing for the Azure Rights Management service can provide the following information:

- Whether the Fabrikam partners opened the document, and when.
- Whether other people who weren't specified, attempted, and failed to open the document. This might happen if the email was forwarded on, or saved to a shared location.

Administrators can [track document usage and revoke access](track-and-revoke-admin) for Office files. Users can [revoke access](https://support.microsoft.com/office/track-and-revoke-access-to-your-files-1de9a543-c2df-44b6-9464-396b23018f96) for their labeled and encrypted documents as needed.

#### Ability to scale across your organization

Because Azure Rights Management runs as a cloud service with the Azure elasticity to scale up and out, you don’t have to provision or deploy additional on-premises servers.

#### Maintain IT control over data

Organizations can benefit from IT control features, such as:

| Feature | Description |
| --- | --- |
| **Root key management** | Use root key management solutions, such as Bring Your Own Key (BYOK) or Double Key Encryption (DKE). For more information, see: - [Planning and implementing your Azure Rights Management root key](/en-us/azure/information-protection/plan-implement-tenant-key)- [What is Double Key Encryption (DKE)?](double-key-encryption) |
| **Auditing and usage logging** | Use auditing and [usage logging](rights-management-usage-logging) to analyze for business insights, monitor for abuse, and perform forensic analysis for information leaks. |
| **Access delegation** | Delegate access with the [super user feature](encryption-super-users), ensuring that IT can always access encrypted content, even if a document was encrypted by an employee who then leaves the organization.  In comparison, peer-to-peer encryption solutions risk losing access to company data. |
| **Active Directory synchronization** | Synchronize [just the directory attributes that the Azure Rights Management service needs](/en-us/azure/active-directory/hybrid/reference-connect-sync-attributes-synchronized#azure-rms) to support a common identity for your on-premises Active Directory accounts, by using [a hybrid identity solution](/en-us/azure/active-directory/hybrid/), such as Microsoft Entra Connect. |
| **Single-sign on** | Enable single-sign on without replicating passwords to the cloud, by using AD FS. |
| **Migration from AD RMS** | If you've deployed Active Directory Rights Management Services (AD RMS), [migrate to the Azure Rights Management service](/en-us/azure/information-protection/migrate-from-ad-rms-to-azure-rms) without losing access to data that was previously encrypted by AD RMS. |

## Security, compliance, and regulatory requirements

Azure Rights Management supports the following security, compliance, and regulatory requirements:

- **Use of industry-standard cryptography and supports FIPS 140-2.** For more information, see the [Cryptographic controls: Algorithms and key lengths](rights-management-how-does-it-work#cryptographic-controls-algorithms-and-key-lengths) information.
- **Support for nCipher nShield hardware security module (HSM)** to store your root key for the Azure Rights Management service in Microsoft Azure data centers.

    Azure Rights Management uses separate security worlds for its data centers in North America, EMEA (Europe, Middle East and Africa), and Asia, so your keys can be used only in your region.
- **Certification for the following standards**:

    - ISO/IEC 27001:2013 (./includes ISO/IEC 27018)
    - SOC 2 SSAE 16/ISAE 3402 attestations
    - HIPAA BAA
    - EU Model Clause
    - FedRAMP as part of Microsoft Entra ID in Office 365 certification, issued FedRAMP Agency Authority to Operate by HHS
    - PCI DSS Level 1

For more information about these external certifications, see the [Microsoft Trust Center](https://azure.microsoft.com/support/trust-center/compliance/).

## Frequently asked questions

Some of our more frequently asked questions about the Azure Rights Management encryption service from Microsoft Purview Information Protection:

### Do files have to be in the cloud to be encrypted by the Azure Rights Management service?

No, this is a common misconception. The Azure Rights Management service (and Microsoft) doesn't see or store your data as part of the encryption process. Information that you encrypt is never sent to or stored in Azure unless you explicitly store it in Azure or use another cloud service that stores it in Azure.

For more information, see [How the Azure Rights Management service works: Technical details](rights-management-how-does-it-work) to understand how a secret formula that's created and stored on-premises is encrypted by the Azure Rights Management service but remains on-premises.

### What's the difference between Azure Rights Management encryption and encryption in other Microsoft cloud services?

Microsoft provides multiple encryption technologies that enable you to protect your data for different, and often complementary scenarios. For example, while Microsoft 365 offers encryption at-rest for data stored in Microsoft 365, the Azure Rights Management service from Microsoft Purview Information Protection independently encrypts your data so that it's protected regardless of where it's located or how it's transmitted.

These encryption technologies are complementary and using them requires enabling and configuring them independently. When you do so, you might have the option to bring your own key for the encryption, a scenario also known as "BYOK." Enabling BYOK for one of these technologies doesn't affect the others. For example, you can use BYOK for the Azure Rights Management service and not use BYOK for other encryption technologies, and vice versa. The keys used by these different technologies might be the same or different, depending on how you configure the encryption options for each service.

### I see Microsoft Rights Management Services is listed as an available cloud app for conditional access—how does this work?

Yes, you can configure Microsoft Entra Conditional Access for the Azure Rights Management service.

When a user opens a document that's encrypted by the Azure Rights Management service, administrators can block or grant access to users in their tenant, based on the standard conditional access controls. Requiring multifactor authentication (MFA) is one of the most commonly requested conditions. Another one is that devices must be [compliant with your Intune policies](/en-us/mem/intune/protect/conditional-access-intune-common-ways-use) so that, for example, mobile devices meet your password requirements and a minimum operating system version, and computers must be domain-joined.

For more information, see [Conditional Access policies and encrypted documents](encryption-azure-ad-configuration).

Additional information:

| Topic | Details |
| --- | --- |
| **Evaluation frequency** | For Windows computers, the conditional access policies for the Azure Rights Management service are evaluated when the [user environment is initialized](rights-management-how-does-it-work#initializing-the-user-environment) (this process is also known as bootstrapping), and then every 30 days.To fine-tune how often your conditional access policies get evaluated, [configure the token lifetime](/en-us/azure/active-directory/active-directory-configurable-token-lifetimes). |
| **Administrator accounts** | We recommend that you don't add administrator accounts to your conditional access policies because these accounts won't be able to access the Azure Rights Management service when you configure encryption settings for sensitivity labels in the Microsoft Purview portal. |
| **MFA and B2B collaboration** | If you use MFA in your conditional access policies for collaborating with other organizations (B2B), you must use [Microsoft Entra B2B collaboration](/en-us/azure/active-directory/b2b/what-is-b2b) and create guest accounts for the users you want to share with in the other organization. |
| **Terms of Use prompts** | You can [prompt users to accept a terms of use](https://techcommunity.microsoft.com/t5/Azure-Active-Directory-Identity/Updates-to-Azure-AD-Terms-of-Use-functionality-within/ba-p/294822) before they open an encrypted document for the first time. |
| **Cloud apps** | If you use many cloud apps for conditional access, you might not see **Microsoft Information Protection Sync Service** and **Microsoft Rights Management Service** displayed in the list to select. In this case, use the search box at the top of the list. Start typing "Microsoft Information Protection Sync Service" and "Microsoft Rights Management Service" to filter the available apps. Providing you have a supported subscription; you'll then see these options and will be able to select them. |

### I've encrypted a document and now want to change the usage rights or add users—do I need to re-encrypt the document?

If the document was encrypted by using a sensitivity label or rights management template, there's no need to re-encrypt the document. Modify the sensitivity label or rights management template by making your changes to the usage rights or add new groups (or users), and then save these changes:

- When a user hasn't accessed the document before you made the changes, the changes take effect as soon as the user opens the document.
- When a user has already accessed the document, these changes take effect when their [use license](rights-management-usage-rights#rights-management-use-license) expires. Re-encrypt the document only if you can't wait for the use license to expire. For example, remove the sensitivity label that applied the encryption, save, and apply the label again. Re-encrypting effectively creates a new version of the document, and therefore a new use license for the user.

Alternatively, if you have already configured a group for the required permissions, you can change the group membership to include or exclude users and there isn't a need to change the sensitivity label or rights management template. There might be a small delay before the changes take effect because group membership is [cached](rights-management-users-groups#group-membership-caching) by the Azure Rights Management service.

If the document was encrypted by using user-defined permissions, such as the [Let users assign permissions](encryption-sensitivity-labels#let-users-assign-permissions) encryption setting for sensitivity labels, you can't change the permissions for the existing document. You must encrypt the document again and specify all the users and all the usage rights that are required for this new version of the document. To re-encrypt an encrypted document, you must have the [Full Control usage right](rights-management-usage-rights#usage-rights-and-descriptions).

### If I use this encryption solution for my production environment, is my company then locked into the solution?

No, you always remain in control of your data and can continue to access it, even if you decide to no longer use the Azure Rights Management service. For more information, see [Decommission and deactivate the Azure Rights Management service](deactivate-rights-management-service).

### Can I control which of my users can use the Azure Rights Management service to encrypt content?

Yes, when you use [sensitivity labels to encrypt content](/en-us/purview/encryption-sensitivity-labels), label publishing policies define which users see the labels in their apps. If you don't want some users to encrypt content, create a separate label publishing policy for them and in the policy, include only labels that don't apply encryption. For more information, see [Create and configure sensitivity labels and their policies](create-sensitivity-labels).

### When I share an encrypted document with somebody outside my company, how does that user get authenticated?

By default, the Azure Rights Management service uses a Microsoft Entra account and an associated email address for user authentication, which makes business-to-business collaboration seamless for administrators. If the other organization uses Azure services, users already have accounts in Microsoft Entra ID, even if these accounts are created and managed on-premises and then synchronized to Azure. If the organization has Microsoft 365, this service also uses Microsoft Entra ID for the user accounts. If the user's organization doesn't have managed accounts in Azure, they can be authenticated with a guest account. For more information, see [Sharing encrypted documents with external users](sensitivity-labels-office-apps#sharing-encrypted-documents-with-external-users).

The authentication method for these accounts can vary, depending on how the administrator in the other organization has configured the Microsoft Entra accounts. For example, they could use passwords that were created for these accounts, federation, or passwords that were created in Active Directory Domain Services and then synchronized to Microsoft Entra ID.

Other authentication methods:

- If you encrypt an email with an Office document attachment to a user who doesn't have an account in Microsoft Entra ID, the authentication method changes. The Azure Rights Management service is federated with some popular social identity providers, such as Gmail. If the user's email provider is supported, the user can sign in to that service and their email provider is responsible for authenticating them. If the user's email provider isn't supported, or as a preference, the user can apply for a one-time passcode that authenticates them and displays the email with the encrypted document in a web browser.
- The Azure Rights Management service can use Microsoft accounts for supported applications. However, not all applications can open encrypted content when a Microsoft account is used for authentication.

### What type of groups can I use with the Azure Rights Management service?

For most scenarios, you can use any group type in Microsoft Entra ID that has an email address. This rule of thumb always applies when you assign usage rights but there are some exceptions for administering the Azure Rights Management service. For more information, see [the Azure Rights Management service requirements for group accounts](rights-management-users-groups#azure-rights-management-service-requirements-for-group-accounts).

### How do I send an encrypted email to a Gmail or Hotmail account?

When you use Exchange Online and the Azure Rights Management service, you just send the email to the user as an encrypted message. For example, you can select a sensitivity label that automatically applies Do Not Forward for you.

The recipient sees an option to sign in to their Gmail, Yahoo, or Microsoft account, and then they can read the encrypted email. Alternatively, they can choose the option for a one-time passcode to read the email in a browser.

To support this scenario, Exchange Online must be enabled for the Azure Rights Management service and Microsoft Purview Message Encryption.

For more information about the capabilities that include supporting all email accounts on all devices, see the following blog post: [Announcing new capabilities available in Office 365 Message Encryption](https://techcommunity.microsoft.com/t5/Security-Privacy-and-Compliance/Email-Encryption-and-Rights-Protection/ba-p/110801).

### Which file types are supported by the Azure Rights Management service?

The Azure Rights Management service can support all file types. For text, image, Microsoft Office (Word, Excel, PowerPoint) files, PDF files, and some other application file types, the Azure Rights Management service supports native encryption that includes the enforcement of usage rights (permissions). For all other applications and file types, generic encryption provides file encapsulation and authentication to verify if a user is authorized to open the file.

For a list of file types supported for Office apps and services, see [Office file types supported](sensitivity-labels-office-apps#office-file-types-supported) from the sensitivity labeling documentation.

For a list of additional file types that are supported by the Microsoft Purview Information Protection client, see [Supported file types](information-protection-client#supported-file-types) from the information protection client documentation.

### When I open an Office document that's encrypted by the Azure Rights Management service, does the associated temporary file become encrypted by this service as well?

No. In this scenario, the associated temporary file doesn't contain data from the original document but instead, only what the user enters while the file is open. Unlike the original file, the temporary file is obviously not designed for sharing and would remain on the device, protected by local security controls, such as BitLocker and EFS.

### How do we regain access to files that were encrypted by an employee who has now left the organization?

Use the [super user feature](/en-us/purview/encryption-super-users), which grants the Full Control usage rights to authorized users for all items that are encrypted by your tenant. Super users can always read this encrypted content, and if necessary, remove the encryption or re-encrypt the item for different users. This same feature lets authorized services index and inspect items, as needed.

If your content is stored in SharePoint or OneDrive, admins can run the [Unlock-SensitivityLabelEncryptedFile](/en-us/powershell/module/sharepoint-online/unlock-sposensitivitylabelencryptedfile) cmdlet, to remove both the sensitivity label and the encryption. For more information, see [Remove encryption for a labeled document](sensitivity-labels-sharepoint-onedrive-files#remove-encryption-for-a-labeled-document).

### Can Rights Management prevent screen captures?

By not granting the **Copy**[usage right](rights-management-usage-rights), Rights Management can prevent screen captures from many of the commonly used screen capture tools on Windows platforms. In Office for Mac, screen captures can similarly be prevented in Office for Mac, for Word, Excel, and PowerPoint, but not Outlook.

However, for other apps on iOS and for Android, these operating systems don't allow apps to prevent screen captures. In addition, browsers other than Edge can't prevent screen captures. Browser use includes Outlook on the web and Office for the web.

Preventing screen captures can help to avoid accidental or negligent disclosure of confidential or sensitive information. But there are many ways that a user can share data that is displayed on a screen, and taking a screenshot is only one method. For example, a user intent on sharing displayed information can take a picture of it using their camera phone, retype the data, or simply verbally relay it to somebody.

As these examples demonstrate, even if all platforms and all software supported the Rights Management APIs to block screen captures, technology alone can't always prevent users from sharing data that they should not. Rights Management can help to safeguard your important data by using authorization and usage policies, but this enterprise rights management solution should be used with other controls. For example, implement physical security, carefully screen and monitor people who have authorized access to your organization's data, and invest in user education so users understand what data shouldn't be shared.

### What's the difference between a user encrypting an email with Do Not Forward and usage rights that don't include the Forward right?

Despite its name, **Do Not Forward** isn't the opposite of the Forward usage right, or a template. It's actually a set of rights that include restricting copying, printing, and saving the email outside the mailbox, in addition to restricting the forwarding of emails. The rights are dynamically applied to users via the chosen recipients, and not statically assigned by the administrator. For more information, see the [Do Not Forward option for emails](rights-management-usage-rights#do-not-forward-option-for-emails) section in [Configure usage rights for the Azure Rights Management service](rights-management-usage-rights).