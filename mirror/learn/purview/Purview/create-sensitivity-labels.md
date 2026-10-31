---
layout: Conceptual
title: Create and publish sensitivity labels | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/create-sensitivity-labels
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-10-07T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
- SPO_Content
ms.custom:
- admindeeplinkCOMPLIANCE
- sfi-image-nochange
search.appverid:
- MOE150
- MET150
description: "A requirement for all Microsoft Purview Information Protection solutions: Create, configure, and publish sensitivity labels to classify and protect your organization's data."
locale: en-us
document_id: e960697c-fd5b-e5e9-c295-a27610690b7e
document_version_independent_id: e960697c-fd5b-e5e9-c295-a27610690b7e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/create-sensitivity-labels.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: create-sensitivity-labels
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/create-sensitivity-labels.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/5cf46315-b33f-4e99-8224-a1592697eff9
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/715d24c3-3683-4219-82c5-1e3c813fb7fc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
platformId: c3551a56-a65b-c5db-da91-d8ca8c7ffc74
---

# Create and publish sensitivity labels | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

All Microsoft Purview Information Protection solutions are implemented by using [sensitivity labels](sensitivity-labels). To create and publish these labels, use the [Microsoft Purview portal](purview-portal).

First, create and configure the sensitivity labels that you want to make available for apps and other services. For example, the labels you want users to see and apply from Office apps.

Then, create one or more label policies that contain the labels and policy settings that you configure. When you publish the label policy to your chosen users:

- The labels become visible to these users in their apps that support sensitivity labels
- The policy settings are applied to these users

Note

You might be eligible for the automatic creation of default labels and a default label policy. Even if you have some labels, you might find it useful to see the configuration of these default labels that we're creating for new customers. For example, you can make the same manual configurations to help accelerate your own label deployment.

For more information, see [Default labels and policies for Microsoft Purview Information Protection](default-sensitivity-labels-policies).

## Before you begin

To make sure you have permissions to create and manage sensitivity labels, see [Permissions required to create and manage sensitivity labels](get-started-with-sensitivity-labels#permissions-required-to-create-and-manage-sensitivity-labels).

## Create and configure sensitivity labels

Choose the **Modern label scheme** tab if you don't already have any sensitivity labels or your tenant was created beginning October 1, 2025. Or, you manually [migrated to the modern label scheme](migrate-sensitivity-label-scheme). In both cases, you see a green message bar on the **Sensitivity labels** page that confirms your tenant is successfully migrated to the modern label scheme.

# [Classic label scheme](#tab/classic-label-scheme)
1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Information Protection** &gt; **Sensitivity labels**
2. On the **Sensitivity labels** page, select **+ Create a label** to start the new sensitivity label configuration. For example, from the Microsoft Purview portal:

    [![Screenshot of the Microsoft Purview portal, identifying the option to create a sensitivity label.](media/create-sensitivity-label-full.png)](media/create-sensitivity-label-full.png#lightbox)

    Note

    If you need guidance to create new labels, see [Get started with sensitivity labels](get-started-with-sensitivity-labels#guidance-sensitivity-label-names-descriptions).
3. On the **Define the scope for this label** page, the options selected determine the label's scope for the settings that you can configure and where they'll be visible when they're published:

    ![Screenshot that shows all the scopes for sensitivity labels.](media/sensitivity-labels-scopes.png)

    You can't select **Meetings** unless **Files & other data assets** and **Emails** are also selected. For more information about this dependency and extending labels to [include meetings](sensitivity-labels-meetings), see [Use sensitivity labels to protect calendar items, Teams meetings, and chat](sensitivity-labels-meetings).

    If scope options aren't selected, you see the first page to configure the settings for the scope, but you can't configure them and the labels won't be available for users to select in these apps.
4. Follow the configuration prompts for the label settings.

    For more information about the label settings, see [What sensitivity labels can do](sensitivity-labels#what-sensitivity-labels-can-do) from the overview information and use the help in the UI for individual settings.
5. Repeat these steps to create more labels. However, if you want to create a sublabel, first select the parent label and select **...** for **Actions**, and then select **Create sublabel**.
6. When you've created all the labels you need, review their order and if necessary, move them up or down. To change the order of a label, select **...** for **Actions**, and then select one of the reordering options, such as **Move up** or **Move down**. For more information, see [Label priority (order matters)](sensitivity-labels#label-priority-order-matters) from the overview information.

# [Modern label scheme](#tab/modern-label-scheme)
Note

If you've just migrated your labels to the modern label scheme and as part of the migration process, you were prompted to rename one or more labels, you might temporarily see the old name displayed with name conflicts.

Wait a few minutes and refresh the page. Don't make any edits until you see the new names displayed.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Information Protection** &gt; **Sensitivity labels**
2. On the **Sensitivity labels** page, select **+ Create** and then **Label** to start the new sensitivity label configuration.
3. On the **Define the scope for this label** page, the options selected determine the label's scope for the settings that you can configure and where they'll be visible when they're published:

    ![Screenshot that shows all the scopes for sensitivity labels.](media/sensitivity-labels-scopes.png)

    You can't select **Meetings** unless **Files & other data assets** and **Emails** are also selected. For more information about this dependency and extending labels to [include meetings](sensitivity-labels-meetings), see [Use sensitivity labels to protect calendar items, Teams meetings, and chat](sensitivity-labels-meetings).

    If scope options aren't selected, you see the first page to configure the settings for the scope, but you can't configure them and the labels won't be available for users to select in these apps.
4. Follow the configuration prompts for the label settings.

    For more information about the label settings, see [What sensitivity labels can do](sensitivity-labels#what-sensitivity-labels-can-do) from the overview information and use the help in the UI for individual settings.
5. Repeat these steps to create more labels.
6. If you want to group your labels so that they display together vertically for users, first create a label group. Then move labels into that label group, or create new labels directly from that group:

    1. Select **+ Create** and then **Label group** to start the new label group configuration. Specify a name, display name, label group priority, description for users, and a color.
    2. To move a label into the label group, first select the label and select **...** for **Actions**. Select **Move into group** and select the required label group.

        You won't be able to move the label into the group if it already has a label with the same display name. Label display names must be unique within the group, and all standalone labels must have a unique display name. If they're not unique, the move is prevented with a client error message for **Microsoft.Exchange.Management.UnifiedPolicy.LocalizedDisplayNameConflictException** and the label ID of the duplicate name.
    3. To create a new label for that group, first select the label group and then select **...** for **Actions**. Select **Create label in group** to start the new sensitivity label configuration.
7. When you've created all the labels and label groups you need, review their order and if necessary, move them up or down. To change the order of a label or group, select **...** for **Actions**, and then select one of the reordering options, such as **Move up** or **Move down**. For more information, see [Label priority (order matters)](sensitivity-labels#label-priority-order-matters) from the overview information.
8. If you need to move a label out of a label group, select **...** for **Actions**, and then select **Move label from group**. The label then becomes a standalone label that if required, can be moved into another label group with the **Move into group** action from step 6.

---

To edit an existing label, select it, and then select the **Edit label** icon. For example:

[![Screenshot from the Sensitivity labels page, identifying the option to edit a selected sensitivity label.](media/edit-sensitivity-label-full.png)](media/edit-sensitivity-label-full.png#lightbox)

This action starts the **Edit sensitivity label** configuration, which lets you change all the label settings.

Don't delete a label unless you understand the impact for users. For more information, see the Removing and deleting labels section.

Note

If you edit a label that's already published by using a label policy, no extra steps are needed when you finish the configuration. For example, you don't need to add it to a new label policy for the changes to become available to the same users. However, allow up to 24 hours for the changes to replicate to all apps and services.

Until you publish your labels, they won't be available to select in apps or for services. To publish the labels, they must be added to a label policy.

Important

On this **Labels** tab, do not select the **Publish labels** tab (or the **Publish label** button when you edit a label) unless you need to create a new label policy. You need multiple label policies only if users need different labels or different policy settings. Aim to have as few label policies as possible—it's not uncommon to have just one label policy for the organization.

### Additional label settings with Security & Compliance PowerShell

Additional label settings are available with the [Set-Label](/en-us/powershell/module/exchange/set-label) cmdlet from [Security & Compliance PowerShell](/en-us/powershell/exchange/scc-powershell).

For example:

- Use the *LocaleSettings* parameter for multinational deployments so that users see the label name and tooltip in their local language. The following section has an example configuration that specifies the label name and tooltip text for French, Italian, and German.
- Advanced settings supported by built-in labeling are included in the PowerShell documentation. For more help in specifying these PowerShell advanced settings, see the PowerShell tips for specifying the advanced settings section. For additional advanced settings supported by the Microsoft Purview Information Protection client, see the [separate documentation for these settings](/en-us/powershell/exchange/client-advanced-settings).

#### Example configuration to configure a sensitivity label for different languages

The following example shows the PowerShell configuration for a label named "Public" with placeholder text for the tooltip. In this example, the label name and tooltip text are configured for French, Italian, and German.

As a result of this configuration, users who have Office apps that use those display languages see their label names and tooltips in the same language. Similarly, if you have the Microsoft Purview Information Protection client installed to label files from File Explorer, users who have those language versions of Windows see their label names and tooltips in their local language when they use the right-click actions for labeling.

For the languages that you need to support, use the Office [language identifiers](/en-us/deployoffice/office2016/language-identifiers-and-optionstate-id-values-in-office-2016#language-identifiers) (also known as language tags), and specify your own translation for the label name and tooltip.

Before you run the commands in PowerShell, you must first [connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).

```powershell
$Languages = @("fr-fr","it-it","de-de")
$DisplayNames=@("Publique","Publico","Oeffentlich")
$Tooltips = @("Texte Français","Testo italiano","Deutscher text")
$label = "Public"
$DisplayNameLocaleSettings = [PSCustomObject]@{LocaleKey='DisplayName';
Settings=@(
@{key=$Languages[0];Value=$DisplayNames[0];}
@{key=$Languages[1];Value=$DisplayNames[1];}
@{key=$Languages[2];Value=$DisplayNames[2];})}
$TooltipLocaleSettings = [PSCustomObject]@{LocaleKey='Tooltip';
Settings=@(
@{key=$Languages[0];Value=$Tooltips[0];}
@{key=$Languages[1];Value=$Tooltips[1];}
@{key=$Languages[2];Value=$Tooltips[2];})}
Set-Label -Identity $Label -LocaleSettings (ConvertTo-Json $DisplayNameLocaleSettings -Depth 3 -Compress),(ConvertTo-Json $TooltipLocaleSettings -Depth 3 -Compress)
```

#### PowerShell tips for specifying the advanced settings

Although you can specify a sensitivity label by its name, we recommend using the label GUID to avoid potential confusion over specifying the label name or display name. The label name is unique in your tenant, so you can be sure you're configuring the correct label. The display name isn't unique and could result in configuring the wrong label. To find the GUID and confirm the label's scope:

```powershell
Get-Label | Format-Table -Property DisplayName, Name, Guid, ContentType
```

To remove an advanced setting from a sensitivity label, use the same AdvancedSettings parameter syntax, but specify a null string value. For example:

```powershell
Set-Label -Identity 8faca7b8-8d20-48a3-8ea2-0f96310a848e -AdvancedSettings @{DefaultSharingScope=""}
```

To check your label's configuration, including advanced settings, use the following syntax with your own label GUID:

```powershell
(Get-Label -Identity 8faca7b8-8d20-48a3-8ea2-0f96310a848e).settings
```

## Publish sensitivity labels by creating a label policy

As part of the label policy, you select users and groups to have sensitivity labels and label policy settings. For lower administrative maintenance, groups are recommended rather than individual users. However, if a user is removed from a group you specify, the label policy is automatically removed for that user.

Groups supported: Email-enabled security groups, non-mail enabled security groups, distribution groups, Microsoft 365 groups (that can have [dynamic membership](/en-us/azure/active-directory/users-groups-roles/groups-create-rule)) in Microsoft Entra ID.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Information Protection** &gt; **Publishing policies**.
2. On the **Label policies** page, select **Publish label** to start the **Create policy** configuration. For example, from the Microsoft Purview portal:

    [![Screenshot of the Microsoft Purview portal, identifying the option to publish labels.](media/publish-sensitivity-labels-full.png)](media/publish-sensitivity-labels-full.png#lightbox)

    Note

    For more information about the **Export policies** option that can capture detailed information about these policies and all sensitivity labels in your tenant, see [Export policy configuration in Microsoft Purview](purview-policy-export).

    If you had default sensitivity labels created for you, you also have a [default label publishing policy](default-sensitivity-labels-policies#default-sensitivity-label-policy), which you can modify or supplement with additional policies.
3. On the **Choose sensitivity labels to publish** page, select the **Choose sensitivity labels to publish** link. Select the labels that you want to make available in apps and to services, and then select **Add**.

    Important

    If you're using the classic label scheme: When you select a sublabel, make sure you also select its parent label.
4. For the **Assign admin units**: If your organization is using [administrative units in Microsoft Entra ID](/en-us/azure/active-directory/roles/administrative-units), the label policy can be automatically restricted to specific users by selecting administrative units. If your account has been [assigned administrative units](purview-admin-units#permissions-for-administrative-units), you must select one or more administrative units.

    If you don't want to restrict the policy by using administrative units, or your organization hasn't configured administrative units, keep the default of **Full directory**.
5. Follow the prompts to complete the configuration.

    The policy settings that you see match the scope of the labels that you selected. For example, if you selected labels that have just the **Files & other data assets** scope, you don't see the policy settings **Apply this label by default to groups and sites** and **Require users to apply a label to their groups and sites**.

    For more information about these settings, see [What label policies can do](sensitivity-labels#what-label-policies-can-do) from the overview information and use the help in the UI for individual settings.

    For labels configured for **Microsoft Purview Data Map assets (preview)**: These labels don't have any associated publishing policy settings.
6. Repeat these steps if you need different publishing policy settings for different users or scopes. For example, you want additional labels for a group of users, a different default label for a subset of users, or you have configured labels to have different scopes. For labels that apply protection, **Azure Rights Management doesn't support non-email-enabled security groups or exclusions, so the publishing policy scope doesn't necessarily determine who can access protected content.**
7. If you have more than one label policy that might result in a conflict for a user, review the policy order and if necessary, move them up or down. To change the order of a label policy, select **...** for **Actions**, and then select one of the reordering options. For more information, see [Label policy priority (order matters)](sensitivity-labels#label-policy-priority-order-matters) from the overview information.

Completing the **Create policy** configuration automatically publishes the label policy. To make changes to a published policy, simply edit it. There's no specific publish or republish action for you to select.

To edit an existing label policy, select it, and then select the **Edit Policy** button from the flyout pane:

[![Screenshot that shows the option to edit the selected label policy.](media/edit-sensitivity-label-policy-full.png)](media/edit-sensitivity-label-policy-full.png#lightbox)

This action starts the **Create policy** configuration, which lets you edit which labels are included and the label settings. When you complete the configuration, any changes are automatically replicated to the selected users and services.

### Additional label policy settings with Security & Compliance PowerShell

Additional label policy settings are available with the [Set-LabelPolicy](/en-us/powershell/module/exchange/set-labelpolicy) cmdlet from [Security & Compliance PowerShell](/en-us/powershell/exchange/scc-powershell).

The cmdlet documentation includes the advanced settings that are supported by built-in labeling. For additional advanced settings supported by the Microsoft Purview Information Protection client, see the [separate documentation for these settings](/en-us/powershell/exchange/client-advanced-settings).

## Create and configure protection policies

Protection policies are currently in preview and apply to items stored outside Microsoft 365. For example, in Microsoft Fabric, Microsoft Azure Storage, and Microsoft Data Lake Storage Gen 2.

For more information, see [Authoring and publishing protection policies](data-gov-protection-policy).

## When to expect new labels and changes to take effect

For labels and label policy settings, allow 24 hours for the changes to propagate through the services. There are many external dependencies that each have their own timing cycles, so it's a good idea to wait this 24-hour time period before you spend time troubleshooting labels and label policies for recent changes.

However, there are some scenarios where label and label policy changes can take effect much faster or be longer than 24 hours. For example, for new and deleted sensitivity labels for Word, Excel, and PowerPoint on the web, you might see updates replicate within the hour. But for configurations that depend on populating a new group and group membership changes, or network replication latency and bandwidth restrictions, these changes might take 24-48 hours.

## Use PowerShell for sensitivity labels and their policies

You can now use [Security & Compliance PowerShell](/en-us/powershell/exchange/scc-powershell) to create and configure all the settings you see in your labeling admin center. This means that in addition to using PowerShell for settings that aren't available in the labeling admin centers, you can now fully script the creation and maintenance of sensitivity labels and sensitivity label policies.

See the following documentation for supported parameters and values:

- [New-Label](/en-us/powershell/module/exchange/new-label)
- [New-LabelPolicy](/en-us/powershell/module/exchange/new-labelpolicy)
- [Set-Label](/en-us/powershell/module/exchange/set-label)
- [Set-LabelPolicy](/en-us/powershell/module/exchange/set-labelpolicy)

Tip

When you're configuring advanced settings for a sensitivity label, you might find it helpful to reference the PowerShell tips for specifying the advanced settings section on this page.

You can also use [Remove-Label](/en-us/powershell/module/exchange/remove-label) and [Remove-LabelPolicy](/en-us/powershell/module/exchange/remove-labelpolicy) if you need to script the deletion of sensitivity labels or sensitivity label policies. However, before you delete sensitivity labels, make sure you read the next section.

## Removing and deleting labels

In a production environment, it's unlikely that you'll need to remove sensitivity labels from a label policy, or delete sensitivity labels. It's more likely that you might need to do one or either of these actions during an initial testing phase. Make sure you understand what happens when you do either of these actions.

Removing a label from a label policy is less risky than deleting it, and can always be added back later if needed. You can't delete a label if it's still in a label policy.

When you remove a label from a label policy so that the label is no longer published to the originally specified users, the next time the label policy is refreshed, users no longer see that label to select in their Office apps. If that label is already applied, the label isn't removed from the content or container. For example, users who are using built-in labeling in desktop apps for Word, Excel, and PowerPoint, still see the applied label name on the status bar. An applied container label continues to protect the Teams or SharePoint site.

In comparison, when you delete a label:

- If the label applied encryption, the underlying protection template is archived so that previously protected content can still be opened. Because of this archived protection template, you can't create a new label with the same name. Although it's possible to delete a protection template by using [PowerShell](/en-us/powershell/module/aipservice/remove-aipservicetemplate), don't do this unless you're sure you don't need to open content that was encrypted with the archived template.
- For documents stored in SharePoint or OneDrive and you've [enabled sensitivity labels for Office files](sensitivity-labels-sharepoint-onedrive-files): When you open the document in Office for the web, you won't see the label applied in the app, and the label name no longer displays in the **Sensitivity** column in SharePoint. If the deleted label applied encryption and the services can process the encrypted contents, the encryption is removed. Egress actions from these services result in the same outcome. For example, download, copy to, move to, and open with an Office desktop or mobile app. Although the label information remains in the file's metadata, apps can no longer map the label ID to a display name, so users will assume a file isn't labeled.
- For documents stored outside SharePoint and OneDrive or you haven't enabled sensitivity labels for Office files, and for emails: When you open the content, the label information in the metadata remains, but without the label ID to name mapping, users don't see the applied label name displayed (for example, on the status bar for desktop apps). If the deleted label applied encryption, the encryption remains and users still see the name and description of the now archived protection template.
- For containers, such as sites in SharePoint and Teams: The label is removed and any settings that were configured with that label are no longer enforced. This action typically takes between 48-72 hours for SharePoint sites, and can be quicker for Teams and Microsoft 365 Groups. Until the label deletion process is complete, users might not be able to open the content that was previously protected by the sensitivity label.
- Be aware that without a GUID-to-name mapping available after you delete a label, deleted labels can display as GUIDs rather than label names in applications such as [content explorer](data-classification-content-explorer) and [activity explorer](data-classification-activity-explorer).

As with all label changes, removing a sensitivity label from a label policy or deleting a sensitivity label takes time to replicate to all users and services.