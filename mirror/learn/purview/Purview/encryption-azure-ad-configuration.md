---
layout: Conceptual
title: Microsoft Entra configuration for content encrypted by Microsoft Purview Information Protection | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/encryption-azure-ad-configuration
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
ms.reviewer: tommoser
manager: laurawi
ms.date: 2026-10-26T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-encryption
ms.collection:
- purview-compliance
description: How to configure Microsoft Entra cross-tenant access settings and Conditional Access policies for content encrypted with rights management from Microsoft Purview Information Protection.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 3540f811-77e1-e58d-411f-26846522918a
document_version_independent_id: 3540f811-77e1-e58d-411f-26846522918a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/encryption-azure-ad-configuration.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: encryption-azure-ad-configuration
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/encryption-azure-ad-configuration.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 811ad644-33de-110f-0ae5-9808b6a01c71
---

# Microsoft Entra configuration for content encrypted by Microsoft Purview Information Protection | Microsoft Learn

## Service description

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

If you protect sensitive items such as emails and documents by using encryption from the Azure Rights Management service from [Microsoft Purview Information Protection](information-protection), there are some Microsoft Entra configurations that can prevent authorized access to this encrypted content.

Similarly, if your users receive encrypted email from another organization or collaborate with other organizations that encrypt documents by using the Azure Rights Management service, your users might not be able to open that email or document because of how their Microsoft Entra ID is configured.

For example:

- A user can't open encrypted email sent from another organization. Or, a user reports that the recipients in another organization can't open an encrypted email that they sent them.
- Your organization collaborates with another organization on a joint project, and project documents are protected by encrypting them, granting access by using groups in Microsoft Entra ID. Users can't open the documents encrypted by users in the other organization.
- Users can successfully open an encrypted document when they are in the office, but can't when they try to access this document remotely and they're prompted for multifactor authentication (MFA).

To ensure access to the encryption service isn't inadvertently blocked, use the following sections to help configure your organization's Microsoft Entra ID, or relay the information to a Microsoft Entra administrator in another organization. Without access to the Azure Rights Management service, users can't be authenticated and aren't authorized to open encrypted content.

## Cross-tenant access settings and encrypted content

Important

Another organization's cross-tenant access settings can be responsible for either their users being unable to open content that your users have encrypted, or your users being unable to open content encrypted by the other organization.

The message that users see indicates which organization blocked access. You might need to direct the Microsoft Entra admin from another organization to this Cross-tenant access settings and encrypted content section.

By default, there's nothing to configure for cross-tenant authentication to work when users protect content by using encryption from the Azure Rights Management service. However, your organization can restrict access by using Microsoft Entra [External Identities cross-tenant access settings](/en-us/azure/active-directory/external-identities/cross-tenant-access-overview). Conversely, another organization can also configure these settings to restrict access with users in your organization. These settings affect opening any encrypted items, which include encrypted emails and encrypted documents.

For example, another organization might have settings configured that prevent their users from opening content encrypted by your organization. In this scenario, until their Microsoft Entra admin reconfigures their cross-tenant settings, an external user attempting to open that content sees a message that informs them **Access is blocked by your organization** with a reference to **Your tenant administrator**.

Example message for the signed in user from the Fabrikam, Inc organization, when their local Microsoft Entra ID blocks access:

![Example message when the local Microsoft Entra tenant blocks access to encrypted content.](media/blocked-by-your-org.png)

Your users will see a similar message when it's your Microsoft Entra configuration that blocks access.

From the perspective of the signed in user, if it's another Microsoft Entra organization that's responsible for blocking access, the message changes to **Access is blocked by the organization** and displays the domain name of that other organization in the body of the message. For example:

![Example message when another Microsoft Entra tenant blocks access to encrypted content.](media/blocked-by-external-org.png)

Whenever cross-tenant access settings restrict access by applications, they must be configured to allow access to the rights management service, which has the following app ID:

```plaintext
00000012-0000-0000-c000-000000000000
```

If access to the rights management service isn't allowed, users can't be authenticated and authorized to open encrypted content. This configuration can be set as a default setting and as an organizational setting:

- To permit sharing of encrypted content with another organization, create an inbound setting that allows access to Microsoft Rights Management Service (ID: 00000012-0000-0000-c000-000000000000).
- To permit access to encrypted content that users receive from other organizations, create an outbound setting that allows access to Microsoft Rights Management Service (ID: 00000012-0000-0000-c000-000000000000)

When these settings are configured for the encryption service, the application displays **Microsoft Rights Management Services**.

For instructions to configure these cross-tenant access settings, see [Configure cross-tenant access settings for B2B collaboration](/en-us/azure/active-directory/external-identities/cross-tenant-access-settings-b2b-collaboration).

If you configured Microsoft Entra Conditional Access policies that require multifactor authentication (MFA) for users, see Conditional Access policies and encrypted documents.

## Conditional Access policies and encrypted documents

If your organization has implemented [Microsoft Entra Conditional Access policies](/en-us/azure/active-directory/conditional-access/overview) that include **Microsoft Rights Management Services** and the policy extends to external users who need to open documents encrypted by your organization:

- For external users who have a Microsoft Entra account in their own tenant, we recommend you use [External Identities cross-tenant access settings](/en-us/azure/active-directory/external-identities/cross-tenant-access-overview) to configure trust settings for MFA claims from one, many, or all external Microsoft Entra organizations.
- For external users not covered by the previous entry, for example, users who don't have a Microsoft Entra account or you haven't configured cross-tenant access settings for trust settings, these external users must have a guest account in your tenant.

Without one of these configurations, external users can't open the encrypted content and see an error message. The message text might inform them that their account needs to be added as an external user in the tenant, with the incorrect instruction for this scenario to **Sign out and sign in again with a different Microsoft Entra user account**.

If you can't meet these configuration requirements for external users who need to open content encrypted by your organization, you must either remove Microsoft Rights Management Services from the Conditional Access policies, or exclude external users from the policies.

For more information, see the frequently asked question, [I see Microsoft Rights Management Services is listed as an available cloud app for conditional access—how does this work?](azure-rights-management-learn-about#i-see-microsoft-rights-management-services-is-listed-as-an-available-cloud-app-for-conditional-accesshow-does-this-work)

## Guest accounts for external users to open encrypted documents

You might need guest accounts in your Microsoft Entra tenant for external users to open documents encrypted by your organization. Options to create the guest accounts:

- Create these guest accounts yourself. You can specify any email address that these users already use. For example, their Gmail address.

    The advantage of this option is that you can restrict access and rights to specific users by specifying their email address in the encryption settings. The downside is the administration overhead for the account creation and coordination with the label configuration.
- Use [SharePoint and OneDrive integration with Microsoft Entra B2B](/en-us/sharepoint/sharepoint-azureb2b-integration) so that guest accounts are automatically created when your users share links.

    The advantage of this option is minimum administrative overhead because the accounts are created automatically, and simpler label configuration. For this scenario, you must select the encryption option [Add any authenticated user](encryption-sensitivity-labels#requirements-and-limitations-for-add-any-authenticated-users) because you won't know the email addresses in advance. The downside is that this setting doesn't let you restrict access and usage rights to specific users.

External users can also use a Microsoft account to open encrypted documents when they use Windows and Microsoft 365 Apps (formerly Office 365 apps; see [Microsoft 365 Apps name change](/en-us/deployoffice/name-change)) or the standalone edition of Office 2019. More recently supported for other platforms, Microsoft accounts are also supported for opening encrypted documents on macOS (Microsoft 365 Apps, version 16.42+), Android (version 16.0.13029+), and iOS (version 2.42+).

For example, a user in your organization shares an encrypted document with a user outside your organization, and the encryption settings specify a Gmail email address for the external user. This external user can create their own Microsoft account that uses their Gmail email address. Then, after signing in with this account, they can open the document and edit it, according to the usage restrictions specified for them. For a walkthrough example of this scenario, see [Opening and editing the protected document](/en-us/azure/information-protection/secure-collaboration-documents#opening-and-editing-the-protected-document).

Note

The email address for the Microsoft account must match the email address specified to restrict access for the encryption settings.

When a user with a Microsoft account opens an encrypted document in this way, it automatically creates a guest account for the tenant if a guest account with the same name doesn't already exist. When the guest account exists, it can then be used to open documents in SharePoint and OneDrive by using Office for the web, in addition to opening encrypted documents from the supported desktop and mobile Office apps.

However, the automatic guest account isn't created immediately in this scenario, because of replication latency. If you specify personal email addresses as part of your encryption settings, we recommend that you create corresponding guest accounts in Microsoft Entra ID. Then, let these users know that they must use this account to open an encrypted document from your organization.

Tip

Because you can't be sure that external users will be using a supported Office client app, sharing links from SharePoint and OneDrive after creating guest accounts (for specific users) or when you use [SharePoint and OneDrive integration with Microsoft Entra B2B](/en-us/sharepoint/sharepoint-azureb2b-integration-preview) (for any authenticated user) is a more reliable method to support secure collaboration with external users.

## Cross-cloud access settings and encrypted content

Cross-tenant access settings enable cross-cloud access to encrypted documents. As a result, users who are part of an organization in another cloud environment can open Word, Excel, and PowerPoint files that are encrypted by your organization. For example, these users might be in Microsoft Azure Government, or Microsoft Azure China (operated by 21Vianet).

### Supported scenarios

The following scenarios are supported for cross-cloud access to encrypted content:

- Organizations in the Microsoft Azure Commercial cloud can allow access to organizations in the Microsoft Azure Government cloud or Microsoft Azure China (operated by 21Vianet) cloud without contacting Microsoft.
- Organizations in the Microsoft Azure China (operated by 21Vianet) cloud can allow access to organizations in the Microsoft Azure Commercial cloud without contacting Microsoft.
- Encrypted Word, Excel, and PowerPoint files can be shared with users in another cloud environment and viewed on Windows, MacOS, and mobile devices. This scenario doesn't apply to files shared via SharePoint or OneDrive sharing links, but rather to methods like direct email attachments, USB drive, file share, or shared and downloaded from SharePoint.
- Encrypted PDFs and generically encrypted files (.pfile extension) can be shared with users in another cloud environment and viewed using the Microsoft Purview Information Protection Viewer on Windows.
- The user can be, but isn't required to be, a guest in your organization.
- External users and domains can be configured for sensitivity labels that apply encryption when you use [admin-defined permissions](encryption-sensitivity-labels#assign-permissions-now), or specified by users when the labels are configured for [user-defined permissions](encryption-sensitivity-labels#let-users-assign-permissions).
- Encrypted email can be sent in either direction between organizations in the Microsoft Azure Commercial cloud and Microsoft Azure China (operated by 21Vianet) by using Microsoft Purview Message Encryption. Recipients must use the encrypted message portal and authenticate by using a one-time passcode. For more information, see [Manage the use of one-time passcodes for the encrypted message portal](manage-office-365-message-encryption#manage-the-use-of-one-time-pass-codes-for-the-encrypted-message-portal).

### Unsupported scenarios

The following scenarios are currently unsupported for cross-cloud access to encrypted content:

- Native consumption of cross-cloud encrypted email in Outlook clients isn't supported.
- PDF viewers such as Microsoft Edge or Adobe Acrobat are currently unsupported.

### Requirements

Before you configure cross-cloud access, ensure the following requirements are met:

- Microsoft 365 Apps version 2402 or later or Microsoft Office 2024.
- Microsoft Purview Information Protection client 3.1.310.0 or later.
- Administrators on both sides must:
    - Configure cross-tenant access settings to enable cross-cloud access
    - Add the partner organization as a permitted organization
- Users opening encrypted files must have an email address assigned.

### Cross-tenant access settings: Enable cross-cloud collaboration

There's a one-time step required to enable collaboration across different cloud environments:

1. In the Microsoft Entra admin center, navigate to **External identities** &gt; **Cross-tenant access settings**.
2. Select **Microsoft cloud settings**.
3. Select the cloud environment you need to enable for collaboration:
    - Organizations in the Commercial Cloud see both **Microsoft Azure Government** and **Microsoft Azure China (operated by 21Vianet)**.
    - Organizations in a sovereign cloud see only **Microsoft Azure Commercial Cloud**.
4. Select the cloud environment where your partner organization is hosted, and select **Save**.

Note

Both organizations must complete this step, and select the partner cloud.

### Cross-tenant access settings: Configure organizational settings

To configure organizational settings:

1. In the Microsoft Entra admin center, navigate to **External identities** &gt; **Cross-tenant access settings**.
2. Select **Organizational settings**.
3. Select **Add organization**.
4. Enter the **Microsoft Entra tenant ID** for the partner organization.
5. Select **Add**.

The tenant ID is displayed in the **Overview** section of the Microsoft Entra admin center and should be provided by the partner organization.

### Cross-tenant access settings: Trust external MFA claims

If external users aren't invited as guests, inbound trust settings should be configured to trust external MFA claims. If users are invited as guests and you trust external MFA claims, it's [recommended to exclude external users](/en-us/entra/external-id/cross-tenant-access-overview#organizational-settings) from MFA registration in your organization.

Review [Manage cross-tenant access settings for B2B collaboration](/en-us/entra/external-id/authentication-conditional-access#mfa-for-azure-ad-external-users) for configuration details.

### Cross-tenant access settings: Inbound and outbound access settings

The steps to enable the partner cloud and add the partner organization are sufficient to enable both organizations to consume protected content from the partner organization. If you'd like to restrict the cross-cloud collab to only permit document decryption, excluding other services, or to make the relationship one-way, review [Cross-tenant access settings and encrypted content](/en-us/purview/encryption-azure-ad-configuration#cross-tenant-access-settings-and-encrypted-content).

### Changes to domain-based sharing

When the encryption scenario is confined to the same cloud environment, specifying a single domain for the label encryption settings results in authenticating and authorizing all users from the organization that owns the specified domain, regardless of the users' email domain. For more information about this domain-based access, see the note in [Restrict access to content by using sensitivity labels to apply encryption](encryption-sensitivity-labels#add-users-or-groups).

However, the cross-cloud functionality relies on data embedded in [Entra access tokens](/en-us/entra/identity-platform/access-tokens). The feature makes use of two [optional claims](/en-us/entra/identity-platform/optional-claims-reference): `verified_primary_email` and `verified_secondary_email`.

During authorization, these claims are extracted and evaluated against the permissions defined in the label. When the rights management service evaluates domain-based access, it can evaluate only the email suffixes that were provided in the access token. This results in a scenario where the admin-defined permissions or user-defined permissions must contain a domain name that maps exactly to a user's email suffix.

### Cross-cloud common issues

#### External users see "Access is blocked by your organization" when they try to open encrypted files

Cross-tenant access settings aren't configured correctly on one or both sides. Review the Cross-tenant access settings and encrypted content section and the Cross-tenant access settings: Inbound and outbound access settings section.

#### AADSTS90072: Nonguest users see "User account {user@contoso.com} from identity provider 'microsoftonline.com' does not exist in..."

This error indicates that external MFA claims aren't trusted. For configuration details, see [Manage cross-tenant access settings for B2B collaboration](/en-us/entra/external-id/authentication-conditional-access#mfa-for-azure-ad-external-users).