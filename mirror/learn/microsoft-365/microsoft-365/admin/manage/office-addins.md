---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Deploy and manage Office Add-ins through the integrated apps portal - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/office-addins?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2026-08-20T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- Adm_TOC
- operations-pod
ms.custom:
- AdminSurgePortfolio
- integrated-apps
search.appverid: MET150
ROBOTS: NOINDEX, NOFOLLOW
description: An overview of how to deploy and manage Office Add-ins.
locale: en-us
document_id: a9bdfbb5-f570-2964-c2bf-a125fb49518c
document_version_independent_id: a9bdfbb5-f570-2964-c2bf-a125fb49518c
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/office-addins.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/office-addins
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/office-addins.md
platformId: e37db237-bf67-2a52-5791-4e5059787c7f
---

# Deploy and manage Office Add-ins through the integrated apps portal - Microsoft 365 admin | Microsoft Learn

## What are Office add-ins?

Office Add-ins help users get things done right from their Office applications. They're made by Microsoft or non-Microsoft developers either for use within their own organizations or made available to the public in the [Microsoft Marketplace](https://marketplace.microsoft.com). For more information, see [Start using your Office Add-in](https://support.microsoft.com/office/82e665c4-6700-4b56-a3f3-ef5441996862).

## Before you begin

To manage and deploy Office Add-ins through the integrated apps portal in the Microsoft 365 admin center, users need Microsoft 365 Business licenses (Business Basic, Business Standard, Business Premium), Office 365 Enterprise licenses (E1, E3, E5, or F3), or Microsoft 365 Enterprise licenses (E3, E5, or F3). Users also need to sign in to Office by using their organizational ID and have Exchange Online and active Exchange Online mailboxes. Your subscription directory must either be in or federated to Microsoft Entra ID.

### Office requirements

You can deploy add-ins by using the integrated apps portal for Outlook, Excel, Word, and PowerPoint add-ins. These add-ins run across multiple platforms, including Windows, Mac, iPad, and in a browser. Outlook add-ins also work on mobile (iOS and Android).

For Word, Excel, and PowerPoint add-ins, you can deploy add-ins through the integrated apps portal only on Windows, Mac, and the web (not iPad). Additionally, your users must meet the following version requirements:

- On a Windows device, Version 1704 or later of Microsoft 365 Business licenses (Business Basic, Business Standard, Business Premium), Office 365 Enterprise licenses (E1/E3/E5/F3), or Microsoft 365 Enterprise licenses (E3/E5/F3).
- On a Mac, Version 15.34 or later.

For Outlook, your users must meet these version requirements:

- Version 1701 or later of Microsoft 365 Business licenses (Business Basic, Business Standard, Business Premium), Office 365 Enterprise licenses (E1/E3/E5/F3), or Microsoft 365 Enterprise licenses (E3/E5/F3).
- Version 1808 or later of Office Professional Plus 2019 or Office Standard 2019.
- Version 16.0.4494.1000 or later of Office Professional Plus 2016 (MSI) or Office Standard 2016 (MSI).
- Version 15.0.4937.1000 or later of Office Professional Plus 2013 (MSI) or Office Standard 2013 (MSI).
- Version 16.0.9318.1000 or later of Office 2016 for Mac.
- Version 2.75.0 or later of Outlook mobile for iOS.
- Version 2.2.145 or later of Outlook mobile for Android.

Note

MSI versions of Outlook show admin-installed or deployed add-ins in the appropriate Outlook ribbon, not the *My add-ins"* section.

### Exchange Online requirements

Microsoft Exchange stores the add-in manifests within your organization's tenant. The admin deploying add-ins and the users receiving those add-ins must be on a version of Exchange Online that supports OAuth authentication. Use the `Test-OAuthConnectivity` PowerShell cmdlet to verify OAuth connectivity per user.

Deployment through the integrated apps portal doesn't support the following scenarios:

- Add-ins that target Word, Excel, or PowerPoint in Office 2013.
- An on-premises directory service.
- Add-in deployment to an Exchange on-premises Mailbox.
- Deployment of Component Object Model (COM) or Visual Studio Tools for Office (VSTO) add-ins.
- Deployments of Microsoft 365 that don't include Exchange Online such as Microsoft 365 Apps for Business and Microsoft 365 Apps for Enterprise.

## Controls for managing Office add-ins

As an admin, you can manage Office add-ins in your organization as follows:

- Deploy an Office Add-in for users in your organization.
- Manage how users can install and use Office Add-ins.
- Upload custom Office Add-ins for your organization.

### Prepare to deploy and manage Office Add-ins via the integrated apps portal

Important

Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that you should limit to emergency scenarios when you can't use an existing role. To learn more, see [About admin roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

Currently, Exchange admins and Global admins can deploy add-ins from the integrated apps portal.

Add-in deployment is supported on three platforms: Windows, Mac, and on the web. It's also supported on iOS and Android for Outlook add-ins.

### User experience with admin-deployed add-ins

After an admin deploys an add-in from the portal, the next time a user opens the relevant Office application, the add-in automatically downloads. If the add-in supports add-in commands, the add-in's custom buttons automatically appear in the ribbon within the Office application.

Add-ins no longer appear for users if the admin turns off or deletes the add-in. They also stop appearing if the user is removed from Microsoft Entra ID or from a group that the add-in is assigned to. To learn how to perform these actions, see the following section, Deploy your Office Add-ins.

## Deploy your Office Add-ins

Deploying an add-in means you're preinstalling the add-in for a specific set of users in your organization. The admin fully controls all management actions taken on a deployed add-in. You can find, test, and fully deploy apps published by Microsoft and other partners. By purchasing and licensing the apps from the admin center, you add Microsoft and Microsoft partner apps to your list from a single location.

1. In the admin center, in the left navigation, choose **Settings**, and then choose **Integrated apps**.
2. In the **Deployed Apps** list, select **Get apps** to view the apps.
3. On the **Microsoft 365 Apps published apps** page, select the app you want to deploy by choosing **Get it now**. Accept the permissions and select **Continue**.
4. Select **Deploy** at the top of the page next to the message that refers to waiting to be deployed. If the app selected is linked to a SaaS offer by an independent software vendor (ISV), all the other apps that are part of this linked offer appear on the **Configuration** page. If you choose to deploy all of the apps, select **Next**. Otherwise, select **Edit**, and choose which apps you want to deploy. Some apps require you to add users before you can select **Deploy**.
5. Select **Add users**, and then select either **Entire organization**, **Specific users/groups**, or **Just me**. Specific users/groups can be a Microsoft 365 group, a security group, or a distribution group.
6. Select **Next** to go to the **Accept permission request** page. The app capabilities and permissions of each of the apps are listed. If the app needs consent, select **Accept permissions**.

    Important

    Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that you should limit to emergency scenarios when you can't use an existing role. To learn more, see [About admin roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

    Only a global administrator can give consent.
7. Select **Next** to review the deployment and choose **Finish deployment**. You can view the deployment from the **Overview** tab by choosing **View this deployment**. In the Microsoft 365 admin center, you can see the status of each deployed app and the date you deployed the app.

It can take up to 24 hours for an add-in to show up for client for all users.

### Considerations when deploying an add-in to users and groups

Admins can deploy an add-in to everyone or to specific users and groups. Each option has implications.

- **Everyone**: This option assigns the add-in to every user in the organization. Use this option sparingly and only for add-ins that are truly universal to your organization.
- **Users**: If you assign an add-in to an individual user, and then deploy the add-in to a new user, you must first add the new user.
- **Groups**: If you assign an add-in to a group, users who are added to the group are automatically assigned the add-in. When a user is removed from a group, the user loses access to the add-in. In either case, no other action is required from the admin.
- **Just me**: If you assign an add-in to just yourself, the add-in is assigned to only your account, which is ideal for testing the add-in.

The right option for your organization depends on your configuration. However, we recommend making assignments by using groups. As an admin, you might find it easier to manage add-ins by using groups and controlling the membership of those groups rather than assigning individual users each time. In some situations, you might want to restrict access to a small set of users by making assignments to specific users by assigning users manually. For example, consider assigning the add-in to a small set of users first for purposes of testing it.

### Recommended approach for deploying Office Add-ins

To roll out add-ins by using a phased approach, we recommend the following actions.

1. Roll out the add-in to a small set of business stakeholders and members of the IT department. If the deployment is successful, move to step 2.
2. Roll out the add-in to more individuals within the business. Again, evaluate the results and, if successful, continue with full deployment.
3. Perform a full rollout to all users.

Depending on the size of the target audience, you can add or remove roll-out steps.

### Scenarios where Exchange admin can't deploy an add-in

There are two cases where an Exchange admin can't deploy an add-in:

- An add-in needs permission for Microsoft Graph APIs and needs consent from a global admin.
- An add-in is linked to two or more apps, another admin (Exchange or global) deployed at least one of those linked apps, and the user assignment isn't uniform. You can only deploy add-ins when the user assignment is the same for all the already deployed apps.

### Edit users for deployed add-ins

After deployment, admins can edit the users for deployed add-ins.

1. In the admin center, select **Settings**, and then select **Integrated apps**.
2. On the **Integrated apps** page, you see a list of apps that are either single add-ins or add-ins that are linked with other apps.
3. Select an app, and then scroll down to select **Edit Users** or select the **User** tab in the overview pane.
4. Select the user group you want to deploy the add-in to.
5. Review the app information, and then select **Update**.

Important

Use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that you should limit to emergency scenarios when you can't use an existing role. To learn more, see [About admin roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

Only the admin who deployed the add-in or a global admin can manage that add-in.

### Update deployed add-ins

After deployment, admins can approve updates for the deployed add-ins.

1. In the admin center, select **Settings** and then select **Integrated apps**.
2. On the **Integrated apps** page, it displays a list of apps that are either single add-ins or add-ins that are linked with other apps.
3. Select an app with **Status** of **More apps available** to open the **Manage** pane. The status of **More apps available** indicates that there are more integrations from the ISVs that aren't yet deployed.
4. On the **Overview** tab, select **Deploy**. Some apps require you to add users before you can select **Deploy**.
5. Select **Users**, select **Is this a test deployment**, and then select either **Entire organization**, **Specific users/groups**, or **Just me**. You can also select **Test deployment** if you prefer to wait to deploy the app to the entire organization. Specific users or groups can be a Microsoft 365 group, a security group, or a distribution group.
6. Select **Update** and then select **Done**. You can now select **Deploy** on the **Overview** tab.
7. Review the app information, and then select **Deploy**.
8. Select **Done** on the **Deployment completed** page, and review the details of the test or full deployment on the **Overview** tab.
9. If the app has a status of **Update pending**, select the app to open the **Manage** pane and update the app.
10. To update only users, select the **Users** tab and make the appropriate change. Select **Update** after making your changes.

### Delete a deployed add-in

You can also delete an add-in that you deployed.

1. In the admin center, select **Settings**, then select **Integrated apps**.
2. Select any row to display the management pane.
3. Select the **Configuration** tab.
4. Select the add-in that you want to delete and then select **Remove**.

Important

Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. To learn more, see [About admin roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

If another admin deployed the add-in, the **Remove** button is disabled. Only the admin who deployed the app or a global admin can delete the add-in.

## Manage how users install and use Office add-ins

When you manage how users install and use Office add-ins, you decide who can install and use add-ins in your organization. Unlike deploying an add-in that preinstalls for selected users, managing an add-in means you decide which users can self-install Office add-ins from the stores on the Microsoft applications.

### Word, Outlook, and PowerPoint

1. To manage users' ability to self-install and use Office add-ins from the Word, Excel, and PowerPoint stores, go to the Microsoft 365 admin center.
2. Choose **Settings** and then select **Org Settings**.
3. Scroll down and select **User owned apps and services**.
4. Check or clear the option to allow or prevent users from accessing all Word, Excel, and PowerPoint add-ins.

Options available in non-educational tenants:

![Let user access Microsoft Marketplace settings.](../../media/user-owned-apps-and-services.png)

Options available in educational tenants:

![Let user access Microsoft Marketplace settings for EDU.](../../media/user-owned-apps-and-services-edu.png)

The user's license information defines whether a user is a faculty member, staff member, or student. The Age Group property determines whether the student is an adult.

Note

For more information, see the following articles.

- [Learn how to review the user's license type and assign or unassign licenses as required](assign-licenses-to-users).
- [Understand how to configure the Age Group property in the Microsoft Encarta admin center](/en-us/entra/fundamentals/how-to-manage-user-profile-info).

This setting doesn't affect any deployed Office add-ins on Word, Excel, and PowerPoint. You can continue to deploy Office add-ins to users in your organization, even if the setting is turned off.

### Outlook

Important

Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. To learn more, see [About admin roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

1. To manage users' ability to self-install and use Office add-ins from the Outlook store, sign in to the classic Exchange admin center as a global administrator.
2. Go to **Permissions** and then select **User Roles**.
3. Select an existing role assignment policy or create a new policy.
4. Type a name for the policy if you're creating a new policy.
5. Select the following roles: **My Custom Apps**, **My MarketPlaceApps**, and **My ReadWriteMailbox Apps**.
6. Select **Save**.

    - Once you create the policy, assign it to users in your organization.
    - You can also create multiple policies and assign them to different users within your organization.
7. Activating these checkboxes turns on access to Outlook add-ins for the users assigned to the policy.
8. Deactivating these checkboxes turns off access to Outlook add-ins for users assigned to the policy.

Note

This setting doesn't affect any deployed Outlook add-ins. You can continue to deploy Outlook add-ins to users in your organization, even if the setting is turned off.

Microsoft is now partnering with leading developers to create unified apps that work across Outlook, Word, Excel, PowerPoint, Teams, and the Microsoft 365 App (formerly known as Office.com). Any settings made for Office Add-ins continue to be honored as long as they stay as add-ins. When Office add-ins are upgraded to work across different Microsoft applications, you can learn to manage them from here. For more information, see [Apps for Microsoft 365 that work across application hosts](/en-us/microsoft-365/admin/manage/teams-apps-work-on-outlook-and-m365#controls-for-managing-cross-application-apps).

## Upload custom Office add-ins in your organization

You can also upload custom line-of-business add-ins and deploy them to users in your organization.

1. In the admin center, in the left navigation, choose **Settings** and then **Integrated apps**.
2. Select **Upload custom apps**. The **Upload Apps to deploy** wizard opens. The admin center supports custom line-of-business add-ins for Word, PowerPoint, Excel, and Outlook.
3. The next steps depend on whether the add-in uses the XML-formatted add-in only manifest or the unified manifest for Microsoft 365. For information about the difference, see [Office Add-ins manifest](/en-us/office/dev/add-ins/develop/add-in-manifests).

    - **Add-in only manifest**:

        1. Select **Office Add-in** on the **App type** dropdown.
        2. In the **Choose how to upload app** section, do one of the following:

            - Select the option to upload the manifest, and then select the **Choose File** button. Navigate to the add-in's manifest and complete the upload.
            - Select the option to provide a URL for the manifest, fill in the URL, and then select **Validate**.

            Note

            The uploaded manifest size can't exceed 512 KB.
    - **Unified manifest for Microsoft 365**:

        1. Select **Teams app** on the **App type** dropdown (*not***Office Add-in**).
        2. Select the **Choose File** button. Navigate to the add-in's zip-formatted app package file (which contains the manifest) and complete the upload.
4. Select **Next**.
5. Select **Add users**, and then choose either **Entire organization**, **Specific users/groups**, or **Just me**. Specific users or groups can be a Microsoft 365 group, a security group, or a distribution group.
6. Select **Next** to view the **Accept permission request** page. The app capabilities and permissions of the apps are listed. If the app needs consent, select **Accept permissions**.

    Important

    Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that you should limit to emergency scenarios when you can't use an existing role. To learn more, see [About admin roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

    Only a global administrator can give consent.
7. Select **Next** to review the deployment and choose **Finish deployment**. You can view the deployment from the **Overview** tab by choosing **View this deployment**.

## More about Office Add-ins security

Office Add-ins combine a manifest file that contains some metadata about the add-in, but most importantly points to a web application that contains all the code and logic. Add-ins can range in their capabilities, but usually read and write data to and from the user's documents.

For more information about the types and capabilities of Office Add-ins, see [Office Add-ins platform overview](/en-us/office/dev/add-ins/overview/office-add-ins), especially the section *Components of an Office Add-in*.

To interact with the user's document, the add-in needs to declare what permission it needs in the manifest. A five-level JavaScript API access-permissions model provides the basis for privacy and security for users of task pane add-ins. Most of the add-ins in the Microsoft Marketplace are level **read/write document** with almost all add-ins supporting at least the **read document** level. For more information about the permission levels, see [Requesting permissions for API use in content and task pane add-ins](/en-us/office/dev/add-ins/develop/requesting-permissions-for-api-use-in-content-and-task-pane-add-ins).

When a manifest is updated, the typical changes are to an add-in's icon and text. Occasionally, add-in commands change. However, the permissions of the add-in don't change. The web application where all the code and logic for the add-in runs can change at any time, which is the nature of web applications.

Updates for add-ins happen as follows.

- **Line-of-business add-in**: In this case, where an admin uploaded a manifest, the admin must upload the new manifest file to support metadata changes. The next time a user starts the relevant Microsoft 365 productivity application, the add-in updates.
- **Microsoft Marketplace add-in**: When an admin selected an add-in from Microsoft Marketplace and then the developer updated the manifest in Microsoft Marketplace, the admin doesn't have to take any action. The next time a user starts the relevant Microsoft 365 productivity application, the add-in updates.

Note

There are other ways for deploying Office Add-ins in certain scenarios. For more information, see [Deploy and publish Office Add-ins](/en-us/office/dev/add-ins/publish/publish).