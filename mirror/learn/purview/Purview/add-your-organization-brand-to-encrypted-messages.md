---
layout: Conceptual
title: Add your brand to encrypted messages | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/add-your-organization-brand-to-encrypted-messages
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: tommos
author: tommoser
manager: kkunes
ms.date: 2026-11-25T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- MET150
- MOE150
ms.collection:
- purview-compliance
ms.custom: msecd-doc-authoring-1014, seo-marvel-apr2020, seo-marvel-jun2020, admindeeplinkMAC, admindeeplinkEXCHANGE, sfi-ga-nochange
description: Learn how to apply your organization's branding to encrypted email messages and the contents of the encryption portal.
ai-usage: ai-assisted
locale: en-us
document_id: 720ba950-dabf-65c2-2772-208cb87065c9
document_version_independent_id: 720ba950-dabf-65c2-2772-208cb87065c9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/add-your-organization-brand-to-encrypted-messages.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: add-your-organization-brand-to-encrypted-messages
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/add-your-organization-brand-to-encrypted-messages.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/5cf46315-b33f-4e99-8224-a1592697eff9
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/715d24c3-3683-4219-82c5-1e3c813fb7fc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 797f2db8-e340-f817-40f9-7d7278ba7bf9
---

# Add your brand to encrypted messages | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Apply your company branding to customize the look of your organization's encrypted email messages and the encryption portal. You need to apply sufficient permissions to your work or school account before you can get started, for example Compliance Administrator.

First, use Exchange Online PowerShell to create and customize branding templates. Then, apply a branding template to encrypted messages by using either:

- An Exchange mail flow rule.
- A Microsoft Purview Data Loss Prevention (DLP) policy rule.

Use the Get-OMEConfiguration and Set-OMEConfiguration cmdlets in Exchange Online PowerShell to customize these parts of encrypted email messages:

- Introductory text
- Disclaimer text
- URL for Your organization's privacy statement
- Text in the encrypted message portal
- Logo that appears in the email message and encrypted message portal, or whether to use a logo at all
- Background color in the email message and encrypted message portal

You can also revert back to the default look and feel at any time.

If you'd like more control, use Microsoft Purview Advanced Message Encryption to create multiple templates for encrypted emails originating from your organization. Use these templates to control parts of the end-user experience. For example, specify the authentication options available in the encryption portal. Use templates to fulfill several use cases, such as:

- Individual departments, such as Finance, Sales, and so on.
- Different products
- Different geographical regions or countries
- Whether you want to allow emails to be revoked
- Whether you want emails sent to external recipients to expire after a specified number of days.

Once you've created the templates, apply them to encrypted emails sent from your online mailbox by using Exchange mail flow rules or DLP policy rules. If you have Microsoft Purview Advanced Message Encryption, you can revoke any email that you have branded.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## Work with branding templates

You can modify several features within a branding template, and modify, but not remove, the default template. If you have Advanced Message Encryption, you can also create, modify, and remove custom templates. Use Exchange Online PowerShell to work with one branding template at a time.

- [Set-OMEConfiguration](/en-us/powershell/module/exchange/set-omeconfiguration) - Modify the default branding template or a custom branding template that you created.
- [New-OMEConfiguration](/en-us/powershell/module/exchange/new-omeconfiguration) - Create a new branding template, Advanced Message Encryption only.
- [Remove-OMEConfiguration](/en-us/powershell/module/exchange/remove-omeconfiguration) - Remove a custom branding template, Advanced Message Encryption only. You can't delete the default branding template.

## Modify a branding template

Use Exchange Online PowerShell to modify one branding template at a time. If you have Advanced Message Encryption, you can also create, modify, and remove custom templates.

1. Use a work or school account that has sufficient administrator permissions in your organization, such as Compliance Administrator, and connect to Exchange Online PowerShell. For instructions, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Use the Set-OMEConfiguration cmdlet as described in [Set-OMEConfiguration](/en-us/powershell/module/exchange/Set-OMEConfiguration) or use the following graphic and table for guidance.

![Diagram of the customizable parts of an encrypted email template, including disclaimer text, email text, portal text, logo, and background color.](media/ome-template-breakout.png)

| To customize this feature of the encryption experience | Use these commands |
| --- | --- |
| Background color | `Set-OMEConfiguration -Identity "<ConfigurationName>" -BackgroundColor "<#RRGGBB hexadecimal color code or name value>"`<br>**Example:**<br><br>`Set-OMEConfiguration -Identity "Branding Template 1" -BackgroundColor "#ffffff"`<br><br> For more information about background colors, see Background colors. |
| Logo | `Set-OMEConfiguration -Identity "<ConfigurationName>" -Image <Byte[]>`<br>**Example:**<br><br>`Set-OMEConfiguration -Identity "Branding Template 1" -Image ([System.IO.File]::ReadAllBytes('C:\Temp\contosologo.png'))`<br><br> Supported file formats: .png, .jpg, .bmp, or .tiff <br><br> Optimal size of logo file: less than 40 KB <br><br> Optimal size of logo image: 170x70 pixels. If your image exceeds these dimensions, the service resizes your logo for display in the portal. The service doesn't modify the graphic file itself. For best results, use the optimal size. |
| Text next to the sender's name and email address | `Set-OMEConfiguration -Identity "<ConfigurationName>" -IntroductionText "<String up to 1024 characters>"`<br>**Example:**<br><br>`Set-OMEConfiguration -Identity "Branding Template 1" -IntroductionText "has sent you a secure message."` |
| Text that appears on the "Read Message" button | `Set-OMEConfiguration -Identity "<ConfigurationName>" -ReadButtonText "<String up to 1024 characters>"`<br>**Example:**<br><br>`Set-OMEConfiguration -Identity "Message encryption configuration" -ReadButtonText "Read Secure Message."` |
| Text that appears below the "Read Message" button | `Set-OMEConfiguration -Identity "<ConfigurationName>" -EmailText "<String up to 1024 characters>"`<br>**Example:**<br><br>`Set-OMEConfiguration -Identity "Message encryption configuration" -EmailText "Encrypted message from ContosoPharma secure messaging system."` |
| URL for the Privacy Statement link | `Set-OMEConfiguration -Identity "<ConfigurationName>" -PrivacyStatementURL "<URL>"`<br>**Example:**<br><br>`Set-OMEConfiguration -Identity "Branding Template 1" -PrivacyStatementURL "https://contoso.com/privacystatement.html"` |
| Disclaimer statement in the email that contains the encrypted message | `Set-OMEConfiguration -Identity "<OMEConfigurationName>" -DisclaimerText "<Disclaimer statement. String of up to 1024 characters.>"`<br>**Example:**<br><br>`Set-OMEConfiguration -Identity "Branding Template 1" -DisclaimerText "This message is confidential for the use of the addressee only."` |
| Text that appears at the top of the encrypted mail viewing portal | `Set-OMEConfiguration -Identity "<OMEConfigurationName>" -PortalText "<Text for your portal. String of up to 128 characters.>"`<br>**Example:**<br><br>`Set-OMEConfiguration -Identity "Message encryption cfonfiguration" -PortalText "ContosoPharma secure email portal."` |
| To enable or disable authentication with a one-time pass code for this custom template | `Set-OMEConfiguration -Identity "<OMEConfigurationName>" -OTPEnabled <$true|$false>`<br>**Examples:**To enable one-time passcodes for this custom template <br><br>`Set-OMEConfiguration -Identity "Branding Template 1" -OTPEnabled $true`<br><br> To disable one-time passcodes for this custom template <br><br>`Set-OMEConfiguration -Identity "Branding Template 1" -OTPEnabled $false` |
| To enable or disable authentication with supported social identities for this custom template | `Set-OMEConfiguration -Identity "<OMEConfigurationName>" -SocialIdSignIn <$true|$false>`<br>**Examples:**To enable social IDs for this custom template <br><br>`Set-OMEConfiguration -Identity "Branding Template 1" -SocialIdSignIn $true`<br><br> To disable social IDs for this custom template <br><br>`Set-OMEConfiguration -Identity "Branding Template 1" -SocialIdSignIn $false` |

## Create an encrypted message branding template (Advanced Message Encryption)

If you have Microsoft Purview Advanced Message Encryption, you can create custom branding templates for your organization by using the [New-OMEConfiguration](/en-us/powershell/module/exchange/new-omeconfiguration) cmdlet. Once you've created the template, you modify the template by using the Set-OMEConfiguration cmdlet as described in Modify a branding template. You can create multiple templates.

To create a new custom branding template:

1. Use a work or school account that has sufficient administrator permissions in your organization, such as Compliance Administrator, and connect to Exchange Online PowerShell. For instructions, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Use the [New-OMEConfiguration](/en-us/powershell/module/exchange/new-omeconfiguration) cmdlet to create a new template.

    ```powershell
    New-OMEConfiguration -Identity "<OMEConfigurationName>"
    ```

    For example,

    ```powershell
    New-OMEConfiguration -Identity "Custom branding template"
    ```

## Return the default branding template to its original values

To remove all modifications from the default template, including brand customizations, and so on, complete these steps:

1. Use a work or school account that has sufficient administrator permissions in your organization, such as Compliance Administrator, and connect to Exchange Online PowerShell. For instructions, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Use the **Set-OMEConfiguration** cmdlet as described in [Set-OMEConfiguration](/en-us/powershell/module/exchange/Set-OMEConfiguration). To remove your organization's branded customizations from the DisclaimerText, EmailText, and PortalText values, set the value to an empty string, `""`. For all image values, such as Logo, set the value to `"$null"`.

    The following table describes the encryption customization option defaults.

    | To revert this feature of the encryption experience back to the default text and image | Use these commands |
    | --- | --- |
    | Default text that comes with encrypted email messages. The default text appears above the instructions for viewing encrypted messages | `Set-OMEConfiguration -Identity "<OMEConfigurationName>" -EmailText "<empty string>"`<br>**Example:**<br><br>`Set-OMEConfiguration -Identity "Message encryption configuration" -EmailText ""` |
    | Disclaimer statement in the email that contains the encrypted message | `Set-OMEConfiguration -Identity "<OMEConfigurationName>" DisclaimerText "<empty string>"`<br>**Example:**<br><br>`Set-OMEConfiguration -Identity "Message encryption configuration" -DisclaimerText ""` |
    | Text that appears at the top of the encrypted mail viewing portal | `Set-OMEConfiguration -Identity "<OMEConfigurationName>" -PortalText "<empty string>"`<br>**Example reverting back to default:**<br><br>`Set-OMEConfiguration -Identity "Message encryption configuration" -PortalText ""` |
    | Logo | `Set-OMEConfiguration -Identity "<OMEConfigurationName>" -Image <"$null">`<br>**Example reverting back to default:**<br><br>`Set-OMEConfiguration -Identity "Message encryption configuration" -Image $null` |
    | Background color | `Set-OMEConfiguration -Identity "<ConfigurationName>" -BackgroundColor "$null">`<br>**Example reverting back to default:**<br><br>`Set-OMEConfiguration -Identity "Message encryption configuration" -BackgroundColor $null` |

## Remove a custom branding template (Advanced Message Encryption)

You can only remove or delete branding templates that you've made. You can't remove the default branding template.

To remove a custom branding template:

1. Use a work or school account that has sufficient administrator permissions in your organization, such as Compliance Administrator, and connect to Exchange Online PowerShell. For instructions, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Use the **Remove-OMEConfiguration** cmdlet as follows:

    Warning

    The following command permanently removes the specified custom branding template. This action can't be undone, and you can't remove the default branding template.

    ```powershell
    Remove-OMEConfiguration -Identity "<OMEConfigurationName>"
    ```

    For example,

    ```powershell
    Remove-OMEConfiguration -Identity "Branding template 1"
    ```

    For more information, see [Remove-OMEConfiguration](/en-us/powershell/module/exchange/remove-omeconfiguration).

## Apply a branding template to encrypted messages

A branding rule doesn't encrypt a message by itself. Before the branding action runs, the message must be encrypted manually in Outlook or Outlook on the web, or automatically by a DLP policy or Exchange mail flow rule.

Choose the rule type that best matches how your organization identifies messages and how you want external recipients to open them.

| Consideration | Exchange mail flow rule | DLP policy rule |
| --- | --- | --- |
| Admin portal | Exchange admin center | Microsoft Purview portal |
| Rule scope | Uses Exchange mail flow rule conditions | Uses DLP conditions and must be scoped only to Exchange |
| Sender requirement | Configure **The sender is located** as **Inside the organization** | Configure **Content is received from** as **People inside my organization** |
| Encryption | Can encrypt and apply branding in the same mail flow rule, or apply branding to a message encrypted earlier | Can encrypt and apply branding in the same DLP rule, or apply branding to a message encrypted by another supported method |
| Portal access | The branding action doesn't provide a choice between enforced portal access and the native encrypted-message experience | The rule can enforce portal access or allow the native experience in supported clients |

### Use an Exchange mail flow rule

Important

Third-party applications that scan and modify mail can prevent branding from being applied correctly.

After you've either modified the default template or created new branding templates, you can create Exchange mail flow rules to apply your custom branding based on certain conditions. Most importantly, the email must be encrypted. Such a rule applies custom branding to mail sent from your online mailbox in the following scenarios:

- If the email was manually encrypted by the end user using Outlook or Outlook on the web, formerly Outlook Web App
- If the email was automatically encrypted by an Exchange mail flow rule or Microsoft Purview Data Loss Prevention policy

To ensure Microsoft Purview Message Encryption applies your custom branding, set up a mail flow rule to encrypt your messages. The priority of the encryption rule should be higher than the branding rule so that the encryption rule is processed first. By default, if you create the encryption rule before the branding rule, then the encryption rule has a higher priority. For information, see [Define mail flow rules to encrypt email messages](define-mail-flow-rules-to-encrypt-email). For information on setting the priority of a mail flow rule, see [Manage mail flow rules](/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules#set-the-priority-of-a-mail-flow-rule).

1. In a web browser, using a work or school account that has sufficient permissions in your organization, such as Compliance Administrator, [sign in to Microsoft 365](https://support.microsoft.com/article/b9582171-fd1f-4284-9846-bdd72bb28426#ID0EAABAAA=Web_browser).
2. Choose the **Admin** tile.
3. In the Microsoft 365 admin center, choose **Admin centers** &gt; **Exchange**.
4. In the EAC, go to **Mail flow** &gt; **Rules** and select **New**![Icon indicating the button to create a new mail flow rule in the Exchange admin center.](media/457cd93f-22c2-4571-9f83-1b129bcfb58e.gif) &gt; **Create a new rule**. For more information about using the EAC, see [Exchange admin center in Exchange Online](/en-us/exchange/exchange-admin-center).
5. In **Name**, type a name for the rule, such as **Branding for sales department**.
6. In **Apply this rule if**, select the condition **The sender is located inside the organization** and other conditions you want from the list of available conditions. For example, you might want to apply a particular branding template to:

    - All encrypted emails sent from members of the finance department
    - Encrypted emails sent with a certain keyword such as "External" or "Partner"
    - Encrypted emails sent to a particular domain
7. If you've already defined a mail flow rule to apply encryption, skip this step. Otherwise, to configure the mail flow rule to apply encryption, from **Do the following**, select **Modify the message security**, and then select **Apply Office 365 Message Encryption and rights protection**. Select a Rights Management Service (RMS) template from the list and then select **add action**.

    The list of templates includes default templates and options and any custom templates you create. If the list is empty, ensure that you have set up Microsoft Purview Message Encryption. For instructions, see [Set up Microsoft Purview Message Encryption](set-up-new-message-encryption-capabilities). For information about the **Do Not Forward** option, see the [Do Not Forward option for emails](rights-management-usage-rights#do-not-forward-option-for-emails). For information about the **Encrypt Only** option, see [Encrypt Only option for emails](rights-management-usage-rights#encrypt-only-option-for-emails).
8. From **Do the following**, select **Modify the message security** &gt; **Apply custom branding to OME messages**. Next, from the drop-down, select a branding template.

    Select **add action** if you want to specify another action, or select **Save**, and then select **OK**.

### Use a DLP policy rule

Before you begin, create and configure the branding template as described in Work with branding templates. The DLP policy must be scoped only to Exchange, and the rule must apply to messages from people inside your organization.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Go to **Solutions** &gt; **Data Loss Prevention** &gt; **Policies**.
3. Select **Enterprise applications & devices**
4. Create a custom DLP policy, or select an existing policy and edit it.
5. On the page where you choose locations, select **Exchange email** and clear all other locations.
6. Create or edit an advanced DLP rule.
7. Under **Conditions**, add **Content is received from**, and select **People inside my organization**. Add any other conditions that identify the encrypted messages to brand.
8. Make sure messages that match the rule are encrypted by adding a new condition, **Message type is** and selecting **Encrypted**.

    1. To encrypt them in the same DLP rule, under **Actions**, add **Restrict access or encrypt the content in Microsoft 365 locations**, and then select **Encrypt email messages**. This is unnecessary if another supported method encrypts the messages before the branding action runs.
9. Under **Actions**, add **Apply branding to encrypted messages**.
10. Under **Select brand template**, select the OME branding template to apply.
11. Choose whether to select **Make external recipients open message in the encrypted message portal**:

    - Selected (the default for new rules): External recipients open the message in the encrypted message portal. External Outlook recipients don't use the native inline viewing experience.
    - Cleared: External Outlook recipients can use the native inline viewing experience. Recipients whose email service or client doesn't support inline viewing continue to use the encrypted message portal.

    Important

    When this setting is selected, Outlook.com and Hotmail recipients are directed to the encrypted message portal and can't use Microsoft consumer-account single sign-on. Clearing the setting preserves the native experience for supported Outlook.com and Hotmail recipients.
12. Save the rule, finish creating or editing the policy, and choose the appropriate policy mode. For deployment guidance, see [Create and deploy data loss prevention policies](dlp-create-deploy-policy).

## Background color reference

The color names that you can use for the background color are limited. Instead of a color name, you can use a hex code value (`#RRGGBB`). You can use a hex code value that corresponds to a color name, or you can use a custom hex code value. Be sure to enclose the hex code value in quotation marks (for example, `"#f0f8ff"`).

The available background color names and their corresponding hex code values are described in the following table.

| Color name | Color code |
| --- | --- |
| `aliceblue` | #f0f8ff |
| `antiquewhite` | #faebd7 |
| `aqua` | #00ffff |
| `aquamarine` | #7fffd4 |
| `azure` | #f0ffff |
| `beige` | #f5f5dc |
| `bisque` | #ffe4c4 |
| `black` | #000000 |
| `blanchedalmond` | #ffebcd |
| `blue` | #0000ff |
| `blueviolet` | #8a2be2 |
| `brown` | #a52a2a |
| `burlywood` | #deb887 |
| `cadetblue` | #5f9ea0 |
| `chartreuse` | #7fff00 |
| `chocolate` | #d2691e |
| `coral` | #ff7f50 |
| `cornflowerblue` | #6495ed |
| `cornsilk` | #fff8dc |
| `crimson` | #dc143c |
| `cyan` | #00ffff |
| `darkblue` | #00008b |
| `darkcyan` | #008b8b |
| `darkgoldenrod` | #b8860b |
| `darkgray` | #a9a9a9 |
| `darkgreen` | #006400 |
| `darkkhaki` | #bdb76b |
| `darkmagenta` | #8b008b |
| `darkolivegreen` | #556b2f |
| `darkorange` | #ff8c00 |
| `darkorchid` | #9932cc |
| `darkred` | #8b0000 |
| `darksalmon` | #e9967a |
| `darkseagreen` | #8fbc8f |
| `darkslateblue` | #483d8b |
| `darkslategray` | #2f4f4f |
| `darkturquoise` | #00ced1 |
| `darkviolet` | #9400d3 |
| `deeppink` | #ff1493 |
| `deepskyblue` | #00bfff |
| `dimgray` | #696969 |
| `dodgerblue` | #1e90ff |
| `firebrick` | #b22222 |
| `floralwhite` | #fffaf0 |
| `forestgreen` | #228b22 |
| `fuchsia` | #ff00ff |
| `gainsboro` | #dcdcdc |
| `ghostwhite` | #f8f8ff |
| `gold` | #ffd700 |
| `goldenrod` | #daa520 |
| `gray` | #808080 |
| `green` | #008000 |
| `greenyellow` | #adff2f |
| `honeydew` | #f0fff0 |
| `hotpink` | #ff69b4 |
| `indianred` | #cd5c5c |
| `indigo` | #4b0082 |
| `ivory` | #fffff0 |
| `khaki` | #f0e68c |
| `lavender` | #e6e6fa |
| `lavenderblush` | #fff0f5 |
| `lawngreen` | #7cfc00 |
| `lemonchiffon` | #fffacd |
| `lightblue` | #add8e6 |
| `lightcoral` | #f08080 |
| `lightcyan` | #e0ffff |
| `lightgoldenrodyellow` | #fafad2 |
| `lightgray` | #d3d3d3 |
| `lightgrey` | #d3d3d3 |
| `lightgreen` | #90ee90 |
| `lightpink` | #ffb6c1 |
| `lightsalmon` | #ffa07a |
| `lightseagreen` | #20b2aa |
| `lightskyblue` | #87cefa |
| `lightslategray` | #778899 |
| `lightsteelblue` | #b0c4de |
| `lightyellow` | #ffffe0 |
| `lime` | #00ff00 |
| `limegreen` | #32cd32 |
| `linen` | #faf0e6 |
| `magenta` | #ff00ff |
| `maroon` | #800000 |
| `mediumaquamarine` | #66cdaa |
| `mediumblue` | #0000cd |
| `mediumorchid` | #ba55d3 |
| `mediumpurple` | #9370db |
| `mediumseagreen` | #3cb371 |
| `mediumslateblue` | #7b68ee |
| `mediumspringgreen` | #00fa9a |
| `mediumturquoise` | #48d1cc |
| `mediumvioletred` | #c71585 |
| `midnightblue` | #191970 |
| `mintcream` | #f5fffa |
| `mistyrose` | #ffe4e1 |
| `moccasin` | #ffe4b5 |
| `navajowhite` | #ffdead |
| `navy` | #000080 |
| `oldlace` | #fdf5e6 |
| `olive` | #808000 |
| `olivedrab` | #6b8e23 |
| `orange` | #ffa500 |
| `orangered` | #ff4500 |
| `orchid` | #da70d6 |
| `palegoldenrod` | #eee8aa |
| `palegreen` | #98fb98 |
| `paleturquoise` | #afeeee |
| `palevioletred` | #db7093 |
| `papayawhip` | #ffefd5 |
| `peachpuff` | #ffdab9 |
| `peru` | #cd853f |
| `pink` | #ffc0cb |
| `plum` | #dda0dd |
| `powderblue` | #b0e0e6 |
| `purple` | #800080 |
| `red` | #ff0000 |
| `rosybrown` | #bc8f8f |
| `royalblue` | #4169e1 |
| `saddlebrown` | #8b4513 |
| `salmon` | #fa8072 |
| `sandybrown` | #f4a460 |
| `seagreen` | #00ff00 |
| `seashell` | #fff5ee |
| `sienna` | #a0522d |
| `silver` | #c0c0c0 |
| `skyblue` | #87ceeb |
| `slateblue` | #6a5acd |
| `slategray` | #708090 |
| `snow` | #fffafa |
| `springgreen` | #00ff7f |
| `steelblue` | #4682b4 |
| `tan` | #d2b48c |
| `teal` | #008080 |
| `thistle` | #d8bfd8 |
| `tomato` | #ff6347 |
| `turquoise` | #40e0d0 |
| `violet` | #ee82ee |
| `wheat` | #f5deb3 |
| `white` | #ffffff |
| `whitesmoke` | #f5f5f5 |
| `yellow` | #ffff00 |
| `yellowgreen` | #9acd32 |