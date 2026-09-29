---
layout: Conceptual
title: Use sensitivity labels to protect collaborative workspaces (groups and sites) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-05-07T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
- SPO_Content
ms.custom:
- admindeeplinkSPO
- no-azure-ad-ps-ref
- sfi-ga-blocked
- sfi-image-nochange
search.appverid:
- MOE150
- MET150
description: Use sensitivity labels to protect collaborative workspaces that include SharePoint and Teams sites, Microsoft 365 groups, Viva Engage communities, and Loop workspaces.
locale: en-us
document_id: 7f95a739-c527-1c8b-6ea5-b3ab01be617d
document_version_independent_id: 7f95a739-c527-1c8b-6ea5-b3ab01be617d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sensitivity-labels-teams-groups-sites.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sensitivity-labels-teams-groups-sites
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sensitivity-labels-teams-groups-sites.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: e7fb04ce-0c23-bde8-8476-25f14e5abb9a
---

# Use sensitivity labels to protect collaborative workspaces (groups and sites) | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

In addition to using [sensitivity labels](sensitivity-labels) to protect items such as documents and emails, you can also use sensitivity labels to protect content in the following containers: Microsoft Teams sites, Microsoft 365 groups, SharePoint sites, Viva Engage communities, and Loop workspaces. To protect these collaborative workspaces, use the following label settings:

- Privacy (public or private)
- External user access
- External sharing from SharePoint sites
- Access from unmanaged devices
- Authentication contexts
- Prevent discovery of private teams for users who have this capability
- Shared channels control for team invitations
- Default sharing link for a SharePoint site (PowerShell-only configuration)
- Site sharing settings (PowerShell-only configuration)
- Default label for channel meetings

Important

The settings for unmanaged devices and authentication contexts work in conjunction with Microsoft Entra Conditional Access. You must configure this dependent feature if you want to use a sensitivity label for these settings. Additional information is included in the instructions that follow.

Support for container-level protection by using sensitivity labels is growing all the time. Refer to the documentation for each collaborative workspace and the [Microsoft public roadmap](https://www.microsoft.com/microsoft-365/roadmap?msockid=305e5dff038362fc15a64e2f02396376&amp;filters=&amp;searchterms=Microsoft%2CPurview) to learn about new capabilities.

When you apply a sensitivity label to a supported container, the label automatically applies the sensitivity category and configured protection settings to the workspace.

Be aware that some label options can extend configuration settings to site owners that are otherwise restricted to administrators. When you configure and publish the label settings for external sharing options and the authentication context, a site owner can now set and change these options for a site by applying or changing the sensitivity label for a team or site. Don't configure these specific label settings if you don't want site owners to be able to make these changes.

Items in these containers however, do not inherit the labels and therefore don't apply any item-level label settings, such as content markings and encryption. So that users can label their documents in SharePoint sites or team sites, make sure you've [enabled sensitivity labels for Office files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files).

Container labels don't support displaying [other languages](create-sensitivity-labels#additional-label-settings-with-security--compliance-powershell) and display the original language only for the label name and description.

## Using sensitivity labels for containers

Before you enable and configure sensitivity labels for containers, users can see and apply sensitivity labels to items in their apps. For example, from Word:

[![A sensitivity label displayed in the Word desktop app.](media/sensitivity-label-word.png)](media/sensitivity-label-word.png#lightbox)

After you enable and configure sensitivity labels for containers, users can additionally see and apply sensitivity labels to containers that support them. These include Microsoft team sites, Microsoft 365 groups, SharePoint sites, Viva Engage communities, and Loop workspaces. For example, when you create a new team site from SharePoint:

![A sensitivity label when creating a team site from SharePoint.](media/sensitivity-labels-new-team-site.png)

After a sensitivity label has been applied to a site, you must have the following role to change that label in SharePoint or Teams:

- For a group-connect site: Microsoft 365 group [Owners](/en-us/microsoft-365/admin/create-groups/office-365-groups)
- For a site that isn't group-connected: SharePoint [site admin](/en-us/sharepoint/site-permissions#site-admins)

Note

Sensitivity labels for containers support [Teams shared channels](/en-us/MicrosoftTeams/shared-channels). If a team has any shared channels, they automatically inherit sensitivity label settings from their parent team, and that label can't be removed or replaced with a different label.

## How to enable sensitivity labels for containers and synchronize labels

If you haven't yet enabled sensitivity labels for containers, do the following set of steps as a one-time procedure:

1. Because this feature uses Microsoft Entra functionality, follow the instructions from the Microsoft Entra documentation to enable sensitivity label support: [Assign sensitivity labels to Microsoft 365 groups in Microsoft Entra ID](/en-us/azure/active-directory/users-groups-roles/groups-assign-sensitivity-labels).
2. You now need to synchronize your sensitivity labels to Microsoft Entra ID. First, [connect to Security & Compliance PowerShell](/en-us/powershell/exchange/office-365-scc/connect-to-scc-powershell/connect-to-scc-powershell).

    For example, in a PowerShell session that you run as administrator, sign in with a global administrator account.
3. Then run the following command to ensure your sensitivity labels can be used with Microsoft 365 groups:

    ```powershell
    Execute-AzureAdLabelSync
    ```

## How to configure groups and site settings for containers

After sensitivity labels are enabled for containers as described in the previous section, you can then configure protection settings for groups and sites in the sensitivity labeling configuration. Until sensitivity labels are enabled for containers, the settings are visible but you can't configure them.

1. Follow the general instructions to [create or edit a sensitivity label](create-sensitivity-labels#create-and-configure-sensitivity-labels) and make sure you select **Groups & sites** for the label's scope:

    ![Sensitivity label scope option for Groups &amp; sites.](media/groupsandsites-scope-options-sensitivity-label.png)

    When only this scope is selected for the label, the label isn't displayed in Office apps that support sensitivity labels and can't be applied to files and emails. Having this separation of labels can be helpful for both users and administrators, but can also add to the complexity of your label deployment.

    For example, you need to carefully review your [label ordering](sensitivity-labels#label-priority-order-matters) because SharePoint detects when a labeled document is uploaded to a labeled site. In this scenario, an audit event and email are automatically generated when the document has a higher priority sensitivity label than the site's label. For more information, see the Auditing sensitivity label activities section on this page.
2. Then, on the **Define protection settings for groups and sites** page, select the options you want to configure:

    - **Privacy and external user access settings** to configure the **Privacy** and **External users access** settings.
    - **External sharing and Conditional Access settings** to configure the **Control external sharing from labeled SharePoint sites** and **Use Microsoft Entra Conditional Access to protect labeled SharePoint sites** setting.
    - **Private teams discoverability and shared channel controls** to configure the settings to prevent users who can discover private teams from finding a private team with this sensitivity label applied, and channel sharing controls for invitations to other teams.

    **Apply a label to channel meetings**: This additional option is applicable only if you are editing an existing label where the scope includes meetings, and you've configured [labels to protect meetings](sensitivity-labels-meetings). Select a sensitivity label to automatically apply to channel meetings and all channel chats. For non-channel meetings, you can select a default label as a policy setting.
3. If you selected **Privacy and external user access settings**, now configure the following settings:

    - **Privacy**: Keep the default of **Public** if you want anyone in your organization to access the container where this label is applied.

        Select **Private** if you want access to be restricted to only approved members in your organization.

        Select **None** when you want to protect content in the container by using the sensitivity label, but still let users configure the privacy setting themselves.

        The settings of **Public** or **Private** set and lock the privacy setting when you apply this label to the container. Your chosen setting replaces any previous privacy setting that might be configured for the container, and locks the privacy value so it can be changed only by first removing the sensitivity label from the container. After you remove the sensitivity label, the privacy setting from the label remains and users can now change it again.
    - **External user access**: Control whether the owner can add guests to the container, similar to [Manage guest access in Microsoft 365 groups](/en-us/microsoft-365/admin/create-groups/manage-guest-access-in-groups).
4. If you selected **External sharing and Conditional Access settings**, now configure the following settings:

    - **Control external sharing from labeled SharePoint sites**: Select this option to then select either external sharing for anyone, new and existing guests, existing guests, or only people in your organization. For more information about this configuration and settings, see the SharePoint documentation, [Turn external sharing on or off for a site](/en-us/sharepoint/change-external-sharing-site).
    - **Use Microsoft Entra Conditional Access to protect labeled SharePoint sites**: Select this option only if your organization has configured and is using [Microsoft Entra Conditional Access](/en-us/azure/active-directory/conditional-access/overview). Then, select one of the following settings:

        - **Determine whether users can access SharePoint sites from unmanaged devices**: This option uses the SharePoint feature that uses Microsoft Entra Conditional Access to block or limit access to SharePoint and OneDrive content from unmanaged devices. For more information, see [Control access from unmanaged devices](/en-us/sharepoint/control-access-from-unmanaged-devices) from the SharePoint documentation. The option you specify for this label setting is the equivalent of running a PowerShell command for a site, as described in steps 3-5 from the [Block or limit access to a specific SharePoint site or OneDrive](/en-us/sharepoint/control-access-from-unmanaged-devices#block-or-limit-access-to-a-specific-sharepoint-site-or-onedrive) section from the SharePoint instructions.

            For additional configuration information, see More information about the dependencies for the unmanaged devices option at the end of this section.
        - **Choose an existing authentication context**: This option lets you enforce more stringent access conditions when users access SharePoint sites that have this label applied. These conditions are enforced when you select an existing authentication context that has been created and published for your organization's Conditional Access deployment. If users don't meet the configured conditions or if they use apps that don't support authentication contexts, they are denied access.

            For additional configuration information, see More information about the dependencies for the authentication context option at the end of this section.

            Examples for this label configuration:

            - You choose an authentication context that is configured to require [multifactor authentication (MFA)](/en-us/azure/active-directory/conditional-access/untrusted-networks). This label is then applied to a SharePoint site that contains highly confidential items. As a result, when users from an untrusted network attempt to access a document in this site, they see the MFA prompt that they must complete before they can access the document.
            - You choose an authentication context that is configured for [terms-of-use (ToU) policies](/en-us/azure/active-directory/conditional-access/terms-of-use). This label is then applied to a SharePoint site that contains items that require a terms-of-use acceptance for legal or compliance reasons. As a result, when users attempt to access a document in this site, they see a terms-of-use document that they must accept before they can access the original document.
5. If you selected **Private teams discoverability and shared channel controls**:

    - For **Private teams discoverability**, use the **Allow users to discover private teams that have this label applied** checkbox when you've configured a [Teams policy that allows private teams discovery](/en-us/microsoftteams/search-private-teams):

        - When the checkbox is selected (the default setting), a private team with the sensitivity label applied will be discoverable for a user who is allowed to discover private teams.
        - When the checkbox is cleared, a private team with the sensitivity label applied will remain hidden and won't be discoverable for all users.
    - For **Teams shared channels**, when a team has a sensitivity label applied, you can allow or prevent other teams from being invited to the original team's shared channels. For more information about shared channels, see [Shared channels in Microsoft Teams](/en-us/microsoftteams/shared-channels).

        Important

        These options for Teams shared channels have a dependency on the settings on the previous **Privacy and external user access** page. If you select an option that's not compatible with these previous settings, you see a validation message to change your selection. Alternatively, you can go back in the configuration to change the dependent setting.

        Options include **Internal only**, **Same label only**, and **Private team only**. Only the last option can potentially remove previously invited teams, and none of the options affect invitations to individual users.

The site and group settings take effect when you apply the label to a container that supports sensitivity labels. If the [label's scope](sensitivity-labels#label-scopes) includes files and emails, other label settings such as encryption and content marking aren't applied to the items within the container.

If your sensitivity label isn't already published, now publish it by [adding it to a sensitivity label policy](create-sensitivity-labels#publish-sensitivity-labels-by-creating-a-label-policy). The users who are assigned a sensitivity label policy that includes this label will be able to select it for sites and groups.

##### More information about the dependencies for the unmanaged devices option

If you don't configure the dependent conditional access policy for SharePoint as documented in [Use app-enforced restrictions](/en-us/sharepoint/app-enforced-restrictions), the option you specify here will have no effect. Additionally, it will have no effect if it's less restrictive than a configured setting at the tenant level. If you have configured an organization-wide setting for unmanaged devices, choose a label setting that's either the same or more restrictive

For example, if your tenant is configured for **Allow limited, web-only access**, the label setting that allows full access will have no effect because it's less restrictive. For this tenant-level setting, choose the label setting to block access (more restrictive) or the label setting for limited access (the same as the tenant setting).

Because you can configure the SharePoint settings separately from the label configuration, there's no check in the sensitivity label configuration that the dependencies are in place. These dependencies can be configured after the label is created and published, and even after the label is applied. However, if the label is already applied, the label setting won't take effect until after the user next authenticates.

##### More information about the dependencies for the authentication context option

To display in the drop-down list for selection, authentication contexts must be created, configured, and published as part of your Microsoft Entra Conditional Access configuration. For more information and instructions, see the [Configure authentication contexts](/en-us/azure/active-directory/conditional-access/concept-conditional-access-cloud-apps#configure-authentication-contexts) section from the Microsoft Entra Conditional Access documentation.

Not all apps support authentication contexts. If a user with an unsupported app connects to the site that's configured for an authentication context, they see either an access denied message or they are prompted to authenticate but rejected. The apps that currently support authentication contexts:

- Office for the web, which includes Outlook for the web
- Microsoft Teams for Windows and macOS (excludes Teams web app)
- Microsoft Planner
- Microsoft 365 Apps for Word, Excel, and PowerPoint; minimum versions:

    - Windows: 2103
    - macOS: 16.45.1202
    - iOS: 2.48.303
    - Android: 16.0.13924.10000
- Microsoft 365 Apps for Outlook; minimum versions:

    - Windows: 2103
    - macOS: 16.45.1202
    - iOS: 4.2109.0
    - Android: 4.2025.1
- OneDrive sync app, minimum versions:

    - Windows: 21.002
    - macOS: 21.002
    - iOS: 12.30
    - Android: Not yet supported

Known limitations:

- For the OneDrive sync app, supported for OneDrive only and not for other sites.
- The following features and apps might be incompatible with authentication contexts, so we encourage you to check that these continue to work after a user successfully accesses a site by using an authentication context:

    - Workflows that use Power Apps or Power Automate
    - Third-party apps

### Configure settings for the default sharing link type for a site by using PowerShell advanced settings

In addition to the label settings for sites and groups that you can configure from the Microsoft Purview portal, you can also configure the default sharing link type for a site. Sensitivity labels for documents can also be configured for a default sharing link type. These settings that help to prevent over-sharing are automatically selected when users select the **Share** button in their Office apps.

For more information and instructions, see [Use sensitivity labels to configure the default sharing link type for sites and documents in SharePoint and OneDrive](sensitivity-labels-default-sharing-link).

### Configure site sharing permissions by using PowerShell advanced settings

Another PowerShell advanced setting that you can configure for the sensitivity label to be applied to a SharePoint site is **MembersCanShare**. This setting is the equivalent configuration that you can set from the SharePoint admin center &gt; **Site permissions** &gt; **Site Sharing** &gt; **Change how members can share** &gt; **Sharing permissions**.

The three options are listed with the equivalent values for the PowerShell advanced setting **MembersCanShare**:

| Option from the SharePoint admin center | Equivalent PowerShell value for MembersCanShare |
| --- | --- |
| **Site owners and members can share files, folders, and the site. People with Edit permissions can share files and folders.** | MemberShareAll |
| **Site owners and members, and people with Edit permissions can share files and folders, but only site owners can share the site.** | MemberShareFileAndFolder |
| **Only site owners can share files, folders, and the site.** | MemberShareNone |

For more information about these configuration options, see [Change how members can share](/en-us/microsoft-365/community/sharepoint-security-a-team-effort#change-how-members-can-share) from the SharePoint community documentation.

Example, where the sensitivity label GUID is **8faca7b8-8d20-48a3-8ea2-0f96310a848e**:

```powershell
Set-Label -Identity 8faca7b8-8d20-48a3-8ea2-0f96310a848e -AdvancedSettings @{MembersCanShare="MemberShareNone"}
```

For more help in specifying PowerShell advanced settings, see [PowerShell tips for specifying the advanced settings](create-sensitivity-labels#powershell-tips-for-specifying-the-advanced-settings).

## Sensitivity label management

Use the following guidance for when you create, modify, or delete sensitivity labels that are configured for sites and groups.

### Creating and publishing labels that are configured for sites and groups

Use the following guidance to publish a label for your users when that label is configured for site and group settings:

1. After you create and configure the sensitivity label, add this label to a label policy that applies to just a few test users.
2. Wait for the change to replicate:

    - New label: Wait at least one hour, unless your configured settings include Teams shared channel controls. If that's the case, wait at least 24 hours.
    - Existing label: Wait at least 24 hours.

    For more information about the timing of labels, see [When to expect new labels and changes to take effect](create-sensitivity-labels#when-to-expect-new-labels-and-changes-to-take-effect).
3. After this wait period, use one of the test user accounts to create a team, Microsoft 365 group, or SharePoint site with the label that you created in step 1.
4. If there are no errors during this creation operation, you know it's safe to publish the label to all users in your tenant.

### Modifying published labels that are configured for sites and groups

As a best practice, don't change the site and group settings for a sensitivity label after the label has been applied to teams, groups, or sites. If you do, remember to wait at least 24 hours for the changes to replicate to all containers that have the label applied.

In addition, if your changes include the **External users access** setting:

- The new setting applies to new users but not to existing users. For example, if this setting was previously selected and as a result, guest users accessed the site, these guest users can still access the site after this setting is cleared in the label configuration.
- The privacy settings for the group properties hiddenMembership and roleEnabled aren't updated.

### Deleting published labels that are configured for sites and groups

If you delete a sensitivity label that has the site and group settings enabled, and that label is included in one or more label policies, this action can result in creation failures for new teams, groups, and sites. To avoid this situation, use the following guidance:

1. Remove the sensitivity label from all label policies that include the label.
2. Wait at least one hour.
3. After this wait period, try creating a team, group, or site and confirm that the label is no longer visible.
4. If the sensitivity label isn't visible, you can now safely delete the label.

## How to apply sensitivity labels to containers

You're now ready to apply the sensitivity label or labels to the following containers:

- Microsoft 365 group in Microsoft Entra ID
- Microsoft Teams team site
- Microsoft 365 group in Outlook on the web
- SharePoint site
- [Loop workspaces](sensitivity-labels-loop)
- [Viva Engage communities](/en-us/viva/engage/manage-engage-communities/community-sensitivity-labeling)

You can use PowerShell if you need to apply a sensitivity label to multiple sites.

### Apply sensitivity labels to Microsoft 365 groups

You're now ready to apply the sensitivity label or labels to Microsoft 365 groups. Return to the Microsoft Entra documentation for instructions:

- [Assign a label to a new group in Azure portal](/en-us/azure/active-directory/users-groups-roles/groups-assign-sensitivity-labels#assign-a-label-to-a-new-group-in-azure-portal)
- [Assign a label to an existing group in Azure portal](/en-us/azure/active-directory/users-groups-roles/groups-assign-sensitivity-labels#assign-a-label-to-an-existing-group-in-azure-portal)
- [Remove a label from an existing group in Azure portal](/en-us/azure/active-directory/users-groups-roles/groups-assign-sensitivity-labels#remove-a-label-from-an-existing-group-in-azure-portal).

### Apply a sensitivity label to a new team

Users can select sensitivity labels when they create new teams in Microsoft Teams. When they select the label from the **Sensitivity** dropdown, the privacy setting might change to reflect the label configuration. Depending on the external users access setting you selected for the label, users can or can't add people outside the organization to the team.

[Learn more about sensitivity labels for Teams](/en-us/microsoftteams/sensitivity-labels)

![The privacy setting when creating a new team.](media/privacy-setting-new-team.png)

After you create the team, the sensitivity label appears in the upper-right corner of all channels.

![The sensitivity label appears on the team.](media/privacy-setting-teams.png)

The service automatically applies the same sensitivity label to the Microsoft 365 group and the connected SharePoint team site.

### Apply a sensitivity label to a new group in Outlook on the web

In Outlook on the web, when you create a new group, you can select or change the **Sensitivity** option for published labels:

![Creating a group and selecting an option under Sensitivity.](media/sensitivity-label-new-group.png)

### Apply a sensitivity label to a new site

Admins and end users can select sensitivity labels when they [create modern team sites and communication sites](/en-us/sharepoint/create-site-collection), and expand **Advanced settings**:

![Creating a site and selecting an option under Sensitivity.](media/sensitivity-label-new-communication-site.png)

The dropdown box displays the label names for the selection, and the help icon displays all the label names with their tooltip, which can help users determine the correct label to apply.

When the label is applied, and users browse to the site, they see the name of the label and applied policies. For example, this site has been labeled as **Confidential**, and the privacy setting is set to **Private**:

[![A site that has a sensitivity label applied.](media/sensitivity-label-site.png)](media/sensitivity-label-site.png#lightbox)

### Use PowerShell to apply a sensitivity label to multiple sites

You can use the [Set-SPOSite](/en-us/powershell/module/sharepoint-online/set-sposite) and [Set-SPOTenant](/en-us/powershell/module/sharepoint-online/set-spotenant) cmdlet with the *SensitivityLabel* parameter from the current [SharePoint Online Management Shell](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online) to apply a sensitivity label to many sites. You can use the same procedure to replace an existing label. The sites can be any SharePoint site collection, or a OneDrive site.

Make sure you have version 16.0.19418.12000 or later of the SharePoint Online Management Shell.

1. Open a PowerShell session with the **Run as Administrator** option.
2. If you don't know your label GUID: [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell) and get the list of sensitivity labels and their GUIDs.

    ```powershell
    Get-Label |ft Name, Guid
    ```
3. Now [connect to SharePoint Online PowerShell](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online) and store your label GUID as a variable. For example:

    ```powershell
    $Id = [GUID]("e48058ea-98e8-4940-8db0-ba1310fd955e")
    ```
4. Create a new variable that identifies multiple sites that have an identifying string in common in their URL. For example:

    ```powershell
    $sites = Get-SPOSite -IncludePersonalSite $true -Limit all -Filter "Url -like 'documents"
    ```
5. Run the following command to apply the label to these sites. Using our examples:

    ```powershell
    $sites | ForEach-Object {Set-SPOTenant $_.url -SensitivityLabel $Id}
    ```

This series of commands lets you label multiple sites across your tenant with the same sensitivity label, which is why you use the Set-SPOTenant cmdlet, rather than the Set-SPOSite cmdlet that's for per-site configuration. However, use the Set-SPOSite cmdlet when you need to apply a different label to specific sites by repeating the following command for each of these sites: `Set-SPOSite -Identity <URL> -SensitivityLabel "<labelguid>"`

## View and manage sensitivity labels in the SharePoint admin center

To view, sort, and search the applied sensitivity labels, use [**Active sites**](https://go.microsoft.com/fwlink/?linkid=2185220) in the SharePoint admin center. You might need to first add the **Sensitivity** column:

[![The Sensitivity column on the Active sites page.](media/manage-site-sensitivity-labels.png)](media/manage-site-sensitivity-labels.png#lightbox)

For more information about managing sites from the Active sites page, including how to add a column, see [Manage sites in the SharePoint admin center](/en-us/sharepoint/manage-sites-in-new-admin-center).

You can also change and apply a label from this page:

1. Select the site name to open the details pane.
2. Select the **Policies** tab, and then select **Edit** for the **Sensitivity** setting.
3. From the **Edit sensitivity setting** pane, select the sensitivity label you want to apply to the site. Unlike user apps, where sensitivity labels can be assigned to specific users, the admin center displays all container labels for your tenant. After you've chosen a sensitivity label, select **Save**.

For information about managing sensitivity labels for containers in SharePoint Embedded, which are the equivalent of sites, see [Manage SharePoint Embedded containers in SharePoint Admin Center](/en-us/sharepoint/dev/embedded/administration/consuming-tenant-admin/ctaux).

## Support for sensitivity labels

When you use admin centers that support sensitivity labels, with the exception of the Microsoft Entra admin center, you see all sensitivity labels for your tenant. In comparison, user apps and services that filter sensitivity labels according to publishing policies can result in you seeing a subset of those labels. The Microsoft Entra admin center also filters the labels according to publishing policies.

The following apps and services support sensitivity labels configured for sites and group settings:

- Admin centers:

    - SharePoint admin center
    - Teams admin center
    - Microsoft 365 admin center
    - Microsoft Purview portal
- User apps and services:

    - SharePoint
    - Teams
    - Outlook on the web and for Windows, macOS, iOS, and Android
    - Forms
    - Stream
    - Planner
    - Loop
    - Viva Engage

The following apps and services don't currently support sensitivity labels configured for sites and group settings:

- Admin centers:

    - Exchange admin center
- User apps and services:

    - Dynamics 365
    - Project
    - Power BI
    - My Apps portal

## Auditing sensitivity label activities

Important

If you use label separation by selecting just the **Groups & sites** scope for labels that protect containers: Because of the **Detected document sensitivity mismatch** audit event and email described in this section, consider [ordering labels](sensitivity-labels#label-priority-order-matters) before labels that have a scope for **Files & other data assets**.

If somebody uploads a document to a site that's protected with a sensitivity label and their document has a [higher priority](sensitivity-labels#label-priority-order-matters) sensitivity label than the sensitivity label applied to the site, this action isn't blocked. For example, you've applied the **General** label to a SharePoint site, and somebody uploads to this site a document labeled **Confidential**. Because a sensitivity label with a higher priority identifies content that's more sensitive than content that has a lower priority order, this situation could be a security concern.

Although the action isn't blocked, it automatically generates an email that's sent to the person who uploaded the document, and also sent to site owners and site admins (maximum of 100 in total). As a result, both the user and these administrators can identify documents that have this misalignment of label priority and take action if needed. For example, delete or move the uploaded document from the site.

Important

If the file is in the Preservation Hold library, it's not supported to interact with files in this location. Files can automatically move into the Preservation Hold library as a result of compliance requirements to automatically retain files that users delete or are cloud attachments. For more information, see [Learn about retention for SharePoint and OneDrive](retention-policies-sharepoint).

It wouldn't be a security concern if the document has a lower priority sensitivity label than the sensitivity label applied to the site. For example, a document labeled **General** is uploaded to a site labeled **Confidential**. In this scenario, an auditing event and email aren't generated.

Note

Just as for the policy option that requires users to provide a justification for changing a label to a lower classification, sublabels for the same parent label are all considered to have the same priority.

To search the audit log for this event, look for **Detected document sensitivity mismatch** from the **File and page activities** category.

The automatically generated email has the subject **Incompatible sensitivity label detected** and the email message explains the labeling mismatch with a link to the uploaded document and site. It also contains a line for your own internal documentation: **HelpLink : Troubleshooting Guide**. You must configure the hyperlink for the troubleshooting guide by using the [Set-SPOTenant](/en-us/powershell/module/sharepoint-online/set-spotenant) cmdlet with the *LabelMismatchEmailHelpLink* parameter. For example:

```PowerShell
Set-SPOTenant –LabelMismatchEmailHelpLink "https://support.contoso.com"
```

The email message also has a Microsoft documentation link that provides basic information for users to change the sensitivity label: [Apply sensitivity labels to your files and email in Office](https://support.microsoft.com/office/apply-sensitivity-labels-to-your-files-and-email-in-office-2f96e7cd-d5a4-403b-8bd7-4cc636bae0f9)

Except for the internal URL that you must specify, these automated emails can't be customized. However, you can prevent them from being sent when you use the following PowerShell command from [Set-SPOTenant](/en-us/powershell/module/sharepoint-online/set-spotenant):

```PowerShell
Set-SPOTenant -BlockSendLabelMismatchEmail $True
```

When somebody adds or removes a sensitivity label to or from a site or group, these activities are also audited but without automatically generating an email.

All these auditing events can be found in the [Sensitivity label activities](audit-log-activities#sensitivity-label-activities) section from the audit log activities documentation.

## How to disable sensitivity labels for containers

You can turn off sensitivity labels for Microsoft Teams, Microsoft 365 groups, and SharePoint sites by using the same instructions from [Enable sensitivity label support in PowerShell](/en-us/azure/active-directory/users-groups-roles/groups-assign-sensitivity-labels#enable-sensitivity-label-support-in-powershell). However, to disable the feature, in step 5, specify `$setting["EnableMIPLabels"] = "False"`.

In addition to making all the settings unavailable for groups and sites when you create or edit sensitivity labels, this action reverts which property the containers use for their configuration. Enabling sensitivity labels for Microsoft Teams, Microsoft 365 groups, and SharePoint sites switches the property used from **Classification** to **Sensitivity**. When you disable sensitivity labels for containers, the containers ignore the Sensitivity property and use the Classification property again.

This means that any label settings from sites and groups previously applied to containers won't be enforced, and containers no longer display the labels.

If these containers have Microsoft Entra classification values applied to them, the containers revert to using the classifications again. Be aware that any new sites or groups that were created after enabling the feature won't display a label or have a classification. For these containers, and any new containers, you can now apply classification values. For more information, see [SharePoint "modern" sites classification](/en-us/sharepoint/dev/solution-guidance/modern-experience-site-classification) and [Create classifications for Office groups in your organization](/en-us/microsoft-365/enterprise/manage-microsoft-365-groups-with-powershell).