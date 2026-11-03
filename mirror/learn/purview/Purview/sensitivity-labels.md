---
layout: Conceptual
title: Learn about sensitivity labels | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sensitivity-labels
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.update-cycle: 180-days
ms.date: 2026-10-29T00:00:00.0000000Z
ai-usage: ai-assisted
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
- highpri
- SPO_Content
- m365solution-mip
- m365initiative-compliance
- m365copilot
- msec-ai-copilot
search.appverid:
- MOE150
- MET150
description: Learn how sensitivity labels from Microsoft Purview Information Protection can protect your organization's sensitive content, wherever it's stored.
ms.custom:
- seo-marvel-apr2020
- seo-marvel-jun2020
- msecd-doc-authoring-1030
locale: en-us
document_id: a046ef0e-0423-6221-d8f6-0c987ffda66c
document_version_independent_id: a046ef0e-0423-6221-d8f6-0c987ffda66c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sensitivity-labels.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sensitivity-labels
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sensitivity-labels.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 43dba79e-079c-1f7e-91fa-75b8bf1ea874
---

# Learn about sensitivity labels | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Note

If you're looking for information about sensitivity labels that you see and can select in your Office apps, check their documentation. For example, [Apply sensitivity labels to your files](https://support.microsoft.com/topic/apply-sensitivity-labels-to-your-files-and-email-in-office-2f96e7cd-d5a4-403b-8bd7-4cc636bae0f9).

The information on this page is for IT administrators who can create and configure those labels by using the Microsoft Purview management solution.

To get their work done, people in your organization collaborate with others both inside and outside the organization. This collaboration means that content no longer stays behind a firewall—it can roam everywhere, across devices, apps, and services. When content roams, you want it to do so in a secure, protected way that meets your organization's business and compliance policies.

Sensitivity labels from Microsoft Purview Information Protection let you classify and protect your organization's data, while making sure that user productivity and their ability to collaborate isn't hindered.

The following example from Excel shows how users might see an applied sensitivity label from the window bar, and how they can easily change the label by using the [sensitivity bar](sensitivity-labels-office-apps#sensitivity-bar) that's available with the latest versions of Office. The labels are also available from the **Sensitivity** button on the **Home** tab from the ribbon.

![Sensitivity label on the Excel ribbon and status bar.](media/sensitivity-label-in-excel.png)

To apply sensitivity labels, users must be signed in with their Microsoft 365 work or school account.

Note

For US Government tenants, sensitivity labels are supported for all platforms.

If you use the Microsoft Purview Information Protection client and scanner, see the [Azure Information Protection Premium Government Service Description](/en-us/enterprise-mobility-security/solutions/ems-aip-premium-govt-service-description).

You can use sensitivity labels to:

- **Provide protection settings that include encryption and content markings.** For example, apply a "Confidential" label to a document or email, and that label encrypts the content and applies a "Confidential" watermark. Content markings include headers and footers as well as watermarks, and encryption can also restrict what actions specified people can take on the content.
- **Extend SharePoint protection when files are downloaded** when you configure a default sensitivity label for SharePoint document libraries and select the option to extend protection for unencrypted files. Then, when these files are downloaded, the current SharePoint permissions travel with the labeled file.
- **Protect content in Office apps across different platforms and devices.** Supported by Word, Excel, PowerPoint, and Outlook on the Office desktop apps and Office for the web. Supported on Windows, macOS, iOS, and Android. For other apps, check their documentation.
- **Protect content in third-party apps and services** by using Microsoft Defender for Cloud Apps. With Defender for Cloud Apps, you can detect, classify, label, and protect content in third-party apps and services, such as SalesForce, Box, or DropBox, even if the third-party app or service doesn't read or support sensitivity labels.
- **Identify content for eDiscovery cases**. The condition builder to create search queries in eDiscovery supports sensitivity labels that are applied to content. For example, as part of your eDiscovery case, restrict content to files and emails that have a "Highly Confidential" sensitivity label. Or conversely, exclude content to files and emails that have a "Public" sensitivity label.
- **Protect containers** that include Teams, Microsoft 365 Groups, SharePoint sites, Viva Engage communities, and Loop workspaces. For example, set privacy settings, external user access and external sharing, access from unmanaged devices, and control how channels can be shared with other teams.
- **Protect meetings and chat** by labeling (and optionally, encrypting) meeting invites and any responses, and enforce Teams-specific options for the meeting and chat.
- **Extend sensitivity labels to Power BI**: When you turn on this capability, you can apply and view labels in Power BI, and protect data when it's saved outside the service.
- **Extend sensitivity labels to assets in Microsoft Purview Data Map**: When you turn on this capability, currently in preview, you can apply your sensitivity labels to files and schematized data assets in Microsoft Purview Data Map. The schematized data assets include SQL, Azure SQL, Azure Synapse, Azure Cosmos DB, and AWS RDS.
- **Extend sensitivity labels to third-party apps and services.** Using the Microsoft Information Protection SDK, third-party apps can read sensitivity labels and apply protection settings.
- **Label content without using any protection settings.** You can also just apply a label as a result of identifying the sensitivity of the data. This action provides users with a visual mapping of your organization's data sensitivity, and the labels can generate usage reports and activity data for data that has different levels of sensitivity. Based on this information, you can always choose to apply protection settings later.
- **Protect data when Microsoft 365 Copilot is used.** Copilot and agents recognize and integrate sensitivity labels into the user interactions to help keep labeled data protected. For more information, see the following section Sensitivity labels for Microsoft 365 Copilot and Microsoft 365 Copilot Chat.

In all these cases, sensitivity labels from Microsoft Purview can help you take the right actions on the right content. With sensitivity labels, you can identify the sensitivity of data across your organization, and the label can enforce protection settings that are appropriate for the sensitivity of that data. That protection then stays with the content.

For more information about these and other scenarios that are supported by sensitivity labels, see [Common scenarios for sensitivity labels](get-started-with-sensitivity-labels#common-scenarios-for-sensitivity-labels). To see how your sensitivity labels are being used, view the reports from the [Microsoft Purview portal](https://purview.microsoft.com/informationprotection/purviewmipreports).

New features are being developed all the time that support sensitivity labels, so you might also find it useful to check the [Microsoft 365 roadmap](https://www.microsoft.com/microsoft-365/roadmap?filters=Microsoft%20Information%20Protection&amp;searchterms=label).

## What a sensitivity label is

When you assign a sensitivity label to content, it's like a stamp that you apply. The label is:

- **Customizable.** You can create categories that fit your organization's specific business needs for different levels of sensitive content. For example, you might use categories like Personal, Public, General, Confidential, and Highly Confidential.
- **Clear text.** Because the label is stored in clear text in the metadata for files and emails, third-party apps and services can read it and then apply their own protective actions, if required.
- **Persistent.** Because the label is stored in metadata for files and emails, the label stays with the content, no matter where you save or store it. The label identification that's unique to your organization becomes the basis for applying and enforcing policies that you configure.

When users in your organization view an applied sensitivity label, it appears like a tag on apps and can be easily integrated into their existing workflows. [Users from other organizations or guests can't see your sensitivity labels in apps](sensitivity-labels-office-apps#support-for-external-users-and-labeled-content).

The following example shows an opened email where another user has applied the sensitivity label named **General**, which doesn't apply encryption. The label description supplied by the admin displays more detail to users about the category of data identified by this sensitivity label.

![Sensitivity label applied to an email.](media/sensitivity-label-on-email.png)

Note

Don't confuse sensitivity labels with Outlook's built-in [sensitivity levels](https://support.microsoft.com/office/mark-your-email-as-normal-personal-private-or-confidential-4a76d05b-6c29-4a0d-9096-71784a6b12c1) that indicate the sender's intention but can't provide data security.

Each item that supports sensitivity labels can have a single sensitivity label applied to it from your organization. Documents and emails can have both a sensitivity label and a [retention label](retention#retention-labels) applied to them.

## What sensitivity labels can do

After you apply a sensitivity label to content, such as an email, meeting invite, document, or Loop page, the label enforces any configured protection settings on the content. You can configure a sensitivity label to:

- **Control access to content by using encryption** for emails, meeting invites, and documents to prevent unauthorized people from accessing this data. You can also choose which users or groups have permissions to perform which actions and for how long. For example, you can choose to allow all users in your organization to modify a document while a specific group in another organization can only view it. Alternatively, instead of administrator-defined permissions, you can allow your users to assign permissions to the content when they apply the label.

    For more information about the encryption-based access control settings when you create or edit a sensitivity label, see [Restrict access to content by using encryption in sensitivity labels](encryption-sensitivity-labels).
- **Mark the content** when you use Office apps, by adding watermarks, headers, or footers to email, meeting invites, or documents that have the label applied. You can apply watermarks to documents and Loop components and pages, but not to email or meeting invites. For other apps, check their documentation. Example header and watermark:

    ![Watermark and header applied to document.](media/sensitivity-label-watermark-header.png)

    Content markings also support variables. For example, insert the label name or document name into the header, footer, or watermark. For more information, see [Content markings with variables](sensitivity-labels-office-apps#content-markings-with-variables).

    Need to check when content markings are applied? See [When Office apps apply content marking and encryption](sensitivity-labels-office-apps#when-office-apps-apply-content-marking-and-encryption).

    If you have templates or workflows that are based on specific documents, test those documents with your chosen content markings before you make the label available for users. Some string length restrictions to be aware of:

    Watermarks are limited to 255 characters. Headers and footers are limited to 1,024 characters, except in Excel. Excel has a total limit of 255 characters for headers and footers but this limit includes characters that aren't visible, such as formatting codes. If that limit is reached, the string you enter isn't displayed in Excel.
- **Protect content in containers such as sites and groups** when you enable the capability to [use sensitivity labels with containers](sensitivity-labels-teams-groups-sites).

    You can't configure protection settings for groups and sites until you enable this capability. This label configuration doesn't result in individual items being automatically labeled but instead, the label settings protect content by controlling access to the container where content can be stored. These settings include privacy settings, external user access and external sharing, access from unmanaged devices, private teams discoverability, and sharing controls for channels.
- **Apply the label automatically to files and emails, or recommend a label.** Choose how to identify sensitive information that you want labeled, and the label can be applied automatically, or you can prompt users to apply the label that you recommend by using a policy tip. If you recommend a label, you can customize the prompt but the following example shows the automatically generated text:

    ![Default prompt for a user to assign a required sensitivity label in Excel.](media/sensitivity-label-required-prompt.png)

    For more information about the **Auto-labeling for files and emails** settings when you create or edit a sensitivity label, see [Automatically apply a sensitivity label to Microsoft 365 data](apply-sensitivity-label-automatically) for Office apps, and [Labeling in Microsoft Purview Data Map](data-map-sensitivity-labels).
- **Set the default sharing link type** for SharePoint sites and individual documents. To help prevent users from oversharing, set the [default scope and permissions](sensitivity-labels-default-sharing-link) for when users share documents from SharePoint and OneDrive.

For more label configurations, see [Manage sensitivity labels for Office apps](sensitivity-labels-office-apps).

### Label scopes

When you create a sensitivity label, you choose the label's scope. The scope determines two things:

- Which label settings you can configure for that label
- The availability of the label to apps and services, which includes whether users can see and select the label

This scope configuration means you can have sensitivity labels that are just for items such as files, emails, and meetings, and can't be selected for groups and sites. Similarly, you can have sensitivity labels that are just for groups and sites and can't be selected for items.

![Screenshot that shows scope options for sensitivity labels.](media/sensitivity-labels-scopes.png)

By default, the **Files & other data assets** scope is always selected for a new label. As well as files for Office, Loop, and Power BI, it includes items from Microsoft Fabric, and data assets for Microsoft Purview Data Map when you [extend your sensitivity labels beyond Microsoft 365](data-map-sensitivity-labels). For more information about which items support sensitivity labels:

- For Office files: [Office file types supported](sensitivity-labels-office-apps#office-file-types-supported)
- For Microsoft Loop: [Sensitivity labels to protect Loop components and pages](sensitivity-labels-loop#sensitivity-labels-to-protect-loop-components-and-pages)
- For Power BI: [Supported export paths](/en-us/power-bi/enterprise/service-security-sensitivity-label-overview#supported-export-paths)
- For Microsoft Fabric: [Information protection in Microsoft Fabric](/en-us/fabric/governance/information-protection)
- For Data Map: [Data sources that connect to Data Map](data-map-data-sources)

For other apps, check their documentation. Support for sensitivity labels is continually expanding.

Typically, you select the **Emails** scope together with **Files & other data assets**, because emails often include files as attachments and share the same sensitivity. Many labeling features require both options to be selected, but there might be times when you want a new label to be available for emails only. For more information, see [Scope labels to just files or emails](sensitivity-labels-office-apps#scope-labels-to-just-files-or-emails).

The scope for **Meetings** includes calendar events, Teams meetings options, and Team chat. You must also select the **Files & other data assets** scope and **Emails** scope for this option. For more information about this labeling scenario, see [Use sensitivity labels to protect calendar items, Teams meetings, and chat](sensitivity-labels-meetings).

The **Groups & sites** scope becomes available and selected by default when you [enable sensitivity labels for containers and synchronize labels](sensitivity-labels-teams-groups-sites#how-to-enable-sensitivity-labels-for-containers-and-synchronize-labels). This option lets you protect content in SharePoint sites, Teams sites, Viva Engage communities, and Loop workspaces by labeling those containers but doesn't label the items in them.

Note

Items that were previously in the **Schematized data assets** scope are now included in **Files & other data assets**.

If you don't select one or more scopes, you see the first page of the configuration settings for these scopes, but you can't configure the settings. For these pages that have unavailable options, select **Next** to continue to configure settings for the next scope. Or, select **Back** to change the label's scope.

### Label priority (order matters)

When you create your sensitivity labels in the Microsoft Purview portal, they appear in a list on the **Labels** page from **Information Protection**. In this list, the order of the labels is important because it sets their priority. You want your most restrictive sensitivity label, such as Highly Confidential, to appear at the **bottom** of the list, and your least restrictive sensitivity label, such as Personal or Public, to appear at the **top**.

You can apply just one sensitivity label to an item such as a document, email, or container. If you use the option that requires your users to provide a justification for changing a label to a lower sensitivity for files, emails, and meetings, the order of this list identifies the lower sensitivity. However, this option doesn't apply to sublabels that share the priority of their parent label, and it doesn't apply to data assets or labels that protect containers.

Note

If you're using the [modern label scheme](migrate-sensitivity-label-scheme) that replaces parent labels with label groups, sublabels in the same label group also don't support the justification setting.

The priority of sublabels is used with [automatic labeling](apply-sensitivity-label-automatically), though. When you configure auto-labeling policies, multiple matches can result for more than one label. Then, the last sensitive label is selected, and then if applicable, the last sublabel. When you configure the auto-labeling label setting (rather than auto-labeling policies) for sublabels themselves, the behavior is a little different when these labels share the same parent label or label group. For example, a sublabel configured for automatic labeling is preferred over a sublabel configured for recommended labeling. For more information, see [How multiple conditions are evaluated when they apply to more than one label](apply-sensitivity-label-automatically#how-multiple-conditions-are-evaluated-when-they-apply-to-more-than-one-label).

The priority of sublabels is also used with [label inheritance from email attachments](sensitivity-labels-office-apps#configure-label-inheritance-from-email-attachments).

When you select a sensitivity label, you can change its priority by using the options to move it to the top or bottom of the list if it's not a sublabel, move it up or down by one label, or directly assign a priority number. For example:

![Screenshot that shows options to change the priority of sensitivity labels.](media/sensitivity-label-reorder-options.png)

### Sublabels that use parent labels or label groups

You might often want to logically group sensitivity labels in a two-tier hierarchy, to denote the overall sensitivity level but provide labels with different settings. As an example from the [default sensitivity labels](default-sensitivity-labels-policies):

Confidential

- Anyone (unrestricted)
- All Employees
- Trusted People

In apps, users first see **Confidential** and then must select one of the other sensitivity labels, such as **All Employees**. The applied sensitivity label is then **Confidential \ All Employees**.

Sensitivity labels from the second tier don't inherit any settings from the first tier label, except the label color. In our example, the **Confidential** label is simply a text label with no protection settings, and can't be applied by itself to content.

The initial implementation to group labels in this two-tier hierarchy used parent labels and sublabels. The configuration of parent labels looked the same as the configuration of sublabels, but behaved differently when sublabels were published to users.

To reduce this complexity, label groups are now replacing parent labels. Label groups look and behave the same to users, but have configuration options only for the settings that they support: the label name, descriptions, color, and priority. You can't publish label groups themselves, only the labels within the groupings.

If you're still using parent labels with sublabels: Don't choose a parent label as the default label, or configure a parent label to be automatically applied (or recommended). If you do, the parent label can't be applied.

Example of how sublabels display for users:

![Example of sublabels from a sensitivity label.](media/sensitivity-sublables.png)

If required, you can manually convert parent labels to label groups. For more information, see [Migrate parent sensitivity labels to label groups](migrate-sensitivity-label-scheme).

### Editing or deleting a sensitivity label

If you delete a sensitivity label from the Microsoft Purview portal, the label isn't automatically removed from content, and any protection settings continue to be enforced on content that had that label applied.

If you edit a sensitivity label, the version of the label that you applied to content is what's enforced on that content.

For detailed information about what happens when you delete a sensitivity label and how this action differs from removing it from a sensitivity label policy, see [Removing and deleting labels](create-sensitivity-labels#removing-and-deleting-labels).

### Sensitivity label limitations per tenant

A single tenant can have a high number of sensitivity labels (1,000+), with one exception: If the label applies encryption that specifies the users and permissions, there's a maximum of 500 labels per tenant supported with this configuration. However, as a best practice to lower admin overhead and reduce complexity for your users, try to keep the number of labels to a minimum.

Tip

Real-world deployments show that effectiveness is noticeably reduced when users have more than five main labels or more than five sublabels per main label. You might also find that some applications can't display all your labels when too many are published to the same user.

## What label policies can do

After you create your sensitivity labels, you need to publish them to make them available to people and services in your organization. The sensitivity labels can then be applied to Office documents and emails, and other items that support sensitivity labels.

Unlike retention labels, which are published to locations such as all Exchange mailboxes, sensitivity labels are published to users or groups. Apps that support sensitivity labels can then display them to those users and groups as labels that they can apply.

Although the default is to publish labels to all users in your organization, multiple label policies let you publish different sensitivity labels to different users if needed. For example, all users see labels that they can apply for Public, General, and Confidential, but only users in your legal department also see a Highly Confidential label that they can apply.

All users in the same organization can see the name of a sensitivity label applied to content, even if that label isn't published to them. They don't see sensitivity labels from other organizations.

When you configure a publishing label policy, you can:

- **Choose which users and groups see the labels.** Labels can be published to include or exclude specific users and supported groups. Supported groups include security groups (email-enabled or non-email-enabled), distribution groups, and Microsoft 365 groups. Microsoft 365 groups can also have [dynamic membership](/en-us/azure/active-directory/users-groups-roles/groups-create-rule).

    Important

    The effect of user and group scoping depends on whether the sensitivity label applies protection:

    **Label without protection:** The publishing policy scope determines which users can see and apply the label.

    **Label with protection:** The publishing policy still determines who can see and apply the label. Access to protected content is also subject to Azure Rights Management. Azure Rights Management doesn't support non-email-enabled security groups or exclusions for protection. Make sure the users and groups that need access are supported and authorized by the protection configuration.
- **Specify a default label** for unlabeled documents and Loop components and pages, emails and meeting invites, new containers (when you've [enabled sensitivity labels for containers](sensitivity-labels-teams-groups-sites)), and also a default label for [Power BI content](/en-us/power-bi/admin/service-security-sensitivity-label-default-label-policy). You can specify the same label for all five types of items, or different labels. Users can change the applied default sensitivity label to better match the sensitivity of their content or container.

    Consider using a default label to set a base level of protection settings that you want applied to all your content. However, without user training and other controls, this setting can also result in inaccurate labeling. It's usually not a good idea to select a label that applies encryption as a default label to documents. For example, many organizations need to send and share documents with external users who might not have apps that support the encryption or they might not use an account that can be authorized. For more information about this scenario, see [Sharing encrypted documents with external users](sensitivity-labels-office-apps#sharing-encrypted-documents-with-external-users).
- **Require a justification for changing a label.** For files, emails, and meetings, but not for groups and sites (used by Teams and SharePoint), if a user tries to remove a label or replace it with a label that has a lower priority, by default the user must provide a justification to perform this action. For example, a user opens a document labeled Confidential (order number 3) and replaces that label with one named Public (order number 1). For Office apps, this justification prompt is triggered once per app session. When you use the Microsoft Purview Information Protection client, the prompt is triggered for each file. Administrators can read the justification reason along with the label change in [activity explorer](data-classification-activity-explorer).

    ![Prompt where users enter a justification.](media/sensitivity-label-justification-required.png)
- **Require users to apply a label** for the different types of items and the containers that support sensitivity labels. Also known as mandatory labeling, these options ensure a label must be applied before users can save files and send emails or meeting invites, create new groups or sites, and when they use unlabeled content for Power BI.

    For documents and emails, a label can be assigned manually by the user, automatically as a result of a condition that you configure, or be assigned by default (the default label option previously described). An example prompt when a user is required to assign a label:

    ![Prompt in Outlook asking user to apply required label.](media/sensitivity-labels-mandatory-prompt-outlook.png)

    For more information about mandatory labeling for documents and emails, see [Require users to apply a label to their email and documents](sensitivity-labels-office-apps#require-users-to-apply-a-label-to-their-email-and-documents).

    For containers, a label must be assigned at the time the group or site is created.

    For more information about mandatory labeling for Power BI, see [Mandatory label policy for Power BI](/en-us/power-bi/admin/service-security-sensitivity-label-mandatory-label-policy).

    Consider using this option to help increase your labeling coverage. However, without user training, these settings can result in inaccurate labeling. In addition, unless you also set a corresponding default label, mandatory labeling can frustrate your users with the frequent prompts.
- **Provide help link to a custom help page.** If your users aren't sure what your sensitivity labels mean or how they should be used, you can provide a Learn More URL that appears after the list of available sensitivity labels in the Office apps. For example:

    ![Learn more link on Sensitivity button on Ribbon.](media/sensitivity-label-learn-more.png)

For more label policy configurations, see [Manage sensitivity labels for Office apps](sensitivity-labels-office-apps).

After you create a publishing label policy that assigns new sensitivity labels to users and groups, users start to see those labels in their Office apps. Allow up to 24 hours for the latest changes to replicate throughout your organization.

### Label policy priority (order matters)

You make your sensitivity labels available to users by publishing them in a sensitivity label policy that appears in a list on the **Label policies** page. Just like sensitivity labels (see Label priority (order matters)), the order of the sensitivity label policies is important because it reflects their priority: The label policy with lowest priority is shown at the top of the list with the **lowest** order number, and the label policy with the highest priority is shown at the bottom of the list with the **highest** order number.

A label policy consists of:

- A set of labels.
- The users and groups that will be assigned the policy with labels.
- The scope of the policy and policy settings for that scope (such as default label for files and emails).

You can include a user in multiple label policies, and the user gets all the sensitivity labels and settings from those policies. If there's a conflict in settings from multiple policies, the settings from the policy with the highest priority (highest order number) is applied. In other words, the highest priority wins for each setting.

If you don't see the label policy setting behavior that you expect for a user or group, check the order of the sensitivity label policies. You might need to move the policy down. To reorder the label policies, select a sensitivity label policy, choose the Actions ellipsis for that entry, and then select **Move down** or **Move up**. For example:

![Move option on the page for sensitivity label policies.](media/sensitivity-label-policy-priority.png)

From the preceding screenshot example that shows three label policies, all users are assigned the standard label policy, so it's appropriate it has the lowest priority (lowest order number of 0). Only users in the IT department are assigned the second policy that has the order number 1. For these users, if there are any conflicts in settings between their policy and the standard policy, the settings from their policy wins because it has a higher order number.

Similarly for users in the legal department, who are assigned the third policy with distinct settings. It's likely these users have more stringent settings, so it's appropriate that their policy has the highest order number. It's unlikely a user from the legal department is in a group that's also assigned to the policy for the IT department. But if they are, the order number 2 (highest order number) ensures the settings from the legal department always take priority if there's a conflict.

Note

Remember: If there's a conflict of settings for a user who has multiple policies assigned to them, the setting from the assigned policy with the highest order number is applied.

## Sensitivity labels for Microsoft 365 Copilot and Microsoft 365 Copilot Chat

Microsoft 365 Copilot, Microsoft 365 Copilot Chat, and Copilot agents recognize and use the sensitivity labels that you apply to protect your organization's data. These labels provide an extra layer of protection. For example, in Microsoft 365 Copilot Chat conversations that can reference data from different types of items, users see the sensitivity label with the highest priority (typically, the most restrictive label). Similarly, when Copilot and agents support sensitivity label inheritance, they select the sensitivity label with the highest priority.

If the labels apply encryption from Microsoft Purview Information Protection, Copilot and agents check the usage rights for the user. Then, Copilot and agents return data from an item only if the user is granted permissions to copy (the EXTRACT usage right) from that item.

For more detailed information about how sensitivity labels help protect your data when you use Copilot and other AI apps, see the following articles:

- [Microsoft Purview data security and compliance protections for generative AI apps](ai-microsoft-purview)
- [Use Microsoft Purview to manage data security & compliance for Microsoft 365 Copilot & Microsoft 365 Copilot Chat](ai-m365-copilot)
- [Considerations to manage Microsoft 365 Copilot for security and compliance](ai-m365-copilot-considerations)

## Sensitivity labels and Azure Information Protection

The older labeling client, the Azure Information Protection unified labeling client, is now replaced with the [Microsoft Purview Information Protection client](information-protection-client) to extend labeling on Windows to File Explorer, PowerShell, the on-premises scanner, and provide a viewer for encrypted files.

Office apps support sensitivity labels with a subscription version of Office, such as Microsoft 365 Apps for enterprise.

## Sensitivity labels and the Microsoft Information Protection SDK

Because a sensitivity label is stored in the metadata of a document, third-party apps and services can read from and write to this labeling metadata to supplement your labeling deployment. Additionally, software developers can use the [Microsoft Information Protection SDK](/en-us/information-protection/develop/overview#microsoft-information-protection-sdk) to fully support labeling and encryption capabilities across multiple platforms. To learn more, see the [General Availability announcement on the Tech Community blog](https://techcommunity.microsoft.com/t5/Microsoft-Information-Protection/Microsoft-Information-Protection-SDK-Now-Generally-Available/ba-p/263144).

You can also learn about [partner solutions that are integrated with Microsoft Purview Information Protection](https://techcommunity.microsoft.com/t5/Azure-Information-Protection/Microsoft-Information-Protection-showcases-integrated-partner/ba-p/262657).

## Deployment guidance

For deployment planning and guidance that includes licensing information, permissions, deployment strategy, a list of supported scenarios, and end-user documentation, see [Get started with sensitivity labels](get-started-with-sensitivity-labels).

To learn how to use sensitivity labels to comply with data privacy regulations, see [Deploy information protection for data privacy regulations with Microsoft 365](/en-us/microsoft-365/solutions/information-protection-deploy).