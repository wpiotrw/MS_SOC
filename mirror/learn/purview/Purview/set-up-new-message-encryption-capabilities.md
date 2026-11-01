---
layout: Conceptual
title: Set up Microsoft Purview Message Encryption | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/set-up-new-message-encryption-capabilities
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-04-22T00:00:00.0000000Z
audience: Admin
ms.topic: install-set-up-deploy
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- MET150
ms.collection:
- purview-compliance
description: Learn about Microsoft Purview Message Encryption that enables protected email communication with people inside and outside your organization.
ms.custom:
- seo-marvel-apr2020
- admindeeplinkMAC
- admindeeplinkEXCHANGE
- sfi-ga-nochange
locale: en-us
document_id: 5eaa1ea7-4b5d-638f-adba-c08d208133c2
document_version_independent_id: 5eaa1ea7-4b5d-638f-adba-c08d208133c2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/set-up-new-message-encryption-capabilities.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: set-up-new-message-encryption-capabilities
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/set-up-new-message-encryption-capabilities.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 0d60a3a2-b210-6cbe-12da-a85bcfe510bb
---

# Set up Microsoft Purview Message Encryption | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Microsoft Purview Message Encryption allows organizations to share encrypted email with anyone on any device. Users can exchange encrypted messages with other Microsoft 365 organizations, as well as third-parties using Outlook.com, Gmail, and other email services.

Follow the steps below to ensure that Microsoft Purview Message Encryption is available in your organization.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## Verify that Azure Rights Management is active

Microsoft Purview Message Encryption uses the protection features from [the Azure Rights Management service](azure-rights-management-learn-about), the encrytion technology used by Microsoft Purview Information Protection to protect emails and documents by using [encryption and access controls](/en-us/azure/information-protection/what-is-azure-rms).

The only prerequisite for using Microsoft Purview Message Encryption is that the Azure Rights Management service must be activated in your organization's tenant. If it is, Microsoft 365 activates message encryption automatically and you don't need to do anything.

The Azure Rights Management service is also activated automatically for most eligible plans, so you probably don't have to do anything in this regard either. For more information, see [Activate the Azure Rights Management service](activate-rights-management-service).

Important

If you use Active Directory Rights Management service (AD RMS) with Exchange Online, you need to [migrate to the Azure Rights Management service](/en-us/azure/information-protection/migrate-from-ad-rms-to-azure-rms) before you can use message encryption. Microsoft Purview Message Encryption is not compatible with AD RMS.

For more information, see:

- [Message Encryption FAQ](ome-faq) to check whether your subscription plan includes Microsoft Purview Information Protection (which includes the Azure Rights Management encryption service).
- [Microsoft Purview Information Protection](https://www.microsoft.com/microsoft-365/business/compliance-management) for information about purchasing an eligible subscription.

### Manually activating Azure Rights Management

If you disabled the Azure Rights Management service, or if it was not automatically activated for any reason, you can activate it manually.

For instructions, see [How to activate or confirm the status of the encryption service](activate-rights-management-service#how-to-activate-or-confirm-the-status-of-the-encryption-service).

## Configure management of your Azure Rights Management tenant key

This is an optional step. Allowing Microsoft to manage the root key for the Azure Rights Management service is the default setting and recommended best practice for most organizations. If this is the case, you don't need to do anything.

There are many reasons, for example compliance requirements, that may necessitate you generating and managing your own root key, also known as "bring your own key" (BYOK). If this is the case, we recommend that you complete the required steps before setting up Microsoft Purview Message Encryption. See [Bring your own key for the Azure Rights Management service root key](rights-management-byok) for more.

## Verify Microsoft Purview Message Encryption configuration in Exchange Online PowerShell

You can verify that your Microsoft 365 tenant is properly configured to use Microsoft Purview Message Encryption in [Exchange Online PowerShell](/en-us/powershell/exchange/exchange-online-powershell).

1. Using a work or school account that has sufficient permissions in your organization, such as Compliance Administrator, start a Windows PowerShell session and connect to Exchange Online. For instructions, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Run the Get-IRMConfiguration cmdlet.

    You should see a value of `$True` for the AzureRMSLicensingEnabled parameter, which indicates that Microsoft Purview Message Encryption is configured in your tenant. If it is not, use Set-IRMConfiguration to set the value of AzureRMSLicensingEnabled to `$True` to enable Microsoft Purview Message Encryption.
3. Run the Test-IRMConfiguration cmdlet using the following syntax:

    ```powershell
    Test-IRMConfiguration [-Sender <email address> -Recipient <email address>]
    ```

    **Example**:

    ```powershell
    Test-IRMConfiguration -Sender securityadmin@contoso.com -Recipient securityadmin@contoso.com
    ```

    - For sender and recipient, use the email address of any user in your Microsoft 365 tenant.

        Your results should be similar to:

        ```console
        Results : Acquiring RMS Templates ...
                   - PASS: RMS Templates acquired.  Templates available: Contoso  - Confidential View Only, Contoso  - Confidential, Do Not
               Forward.
               Verifying encryption ...
                   - PASS: Encryption verified successfully.
               Verifying decryption ...
                   - PASS: Decryption verified successfully.
               Verifying IRM is enabled ...
                   - PASS: IRM verified successfully.
        
               OVERALL RESULT: PASS
        ```
    - Your organization name will replace *Contoso*.
    - The default template names may be different from those displayed above.
4. If the test fails with an error message **Failed to acquire RMS templates**, execute the following commands and run the Test-IRMConfiguration cmdlet to verify that it passes. Connect to the [AIPService module](/en-us/powershell/module/aipservice/?view=azureipps&amp;preserve-view=true) to run the cmdlet.

    ```powershell
    $RMSConfig = Get-AipServiceConfiguration
    $LicenseUri = $RMSConfig.LicensingIntranetDistributionPointUrl
    Set-IRMConfiguration -LicensingLocation $LicenseUri
    Set-IRMConfiguration -InternalLicensingEnabled $true
    ```
5. Run the Remove-PSSession cmdlet to disconnect from the Rights Management service.

    ```powershell
    Remove-PSSession $session
    ```

## Next steps: Define mail flow rules to use Microsoft Purview Message Encryption

If there are previously configured mail flow rules to encrypt email in your organization, you need to update the existing rules to use Microsoft Purview Message Encryption. For new deployments, you need to create new mail flow rules.

Important

If you do not update existing mail flow rules, your users will continue to receive encrypted mail that uses the previous HTML attachment format, instead of the new seamless experience.

Mail flow rules determine under what conditions email messages should be encrypted, as well as conditions for removing that encryption. When you set an action for a rule, any messages that match the rule conditions are encrypted when they're sent.

For steps on creating mail flow rules for message encryption, see [Define mail flow rules to encrypt email messages](define-mail-flow-rules-to-encrypt-email).

To update existing rules to use Microsoft Purview Message Encryption:

1. In the Microsoft 365 admin center, go to **Admin centers** &gt; [**Exchange**](https://go.microsoft.com/fwlink/p/?linkid=2059104).
2. In the Exchange admin center, go to **Mail flow &gt; Rules**.
3. For each rule, in **Do the following**:
    - Select **Modify the message security**.
    - Select **Apply Office 365 Message Encryption and rights protection**.
    - Select **Encrypt** from the RMS template list.
    - Select **Save**.
    - Select **OK**.