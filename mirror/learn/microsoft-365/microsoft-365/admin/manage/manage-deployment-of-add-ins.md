---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Deploy Office Add-ins in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-deployment-of-add-ins?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: kwekua
author: kwekuako
manager: scotv
ms.date: 2026-03-16T00:00:00.0000000Z
audience: Admin
ms.topic: install-set-up-deploy
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier3
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_NonTOC
- Adm_TOC
- operations-pod
ms.custom:
- AdminSurgePortfolio
- okr_smb
- AdminTemplateSet
- admindeeplinkMAC
- integrated-apps
search.appverid:
- BCS160
- MET150
- MOE150
ms.assetid: 737e8c86-be63-44d7-bf02-492fa7cd9c3f
description: Deploy Office Add-ins to users and groups using centralized deployment in the Microsoft 365 admin center. Follow step-by-step instructions to get started.
locale: en-us
document_id: e62dfa25-e420-38e4-ff47-05cca62d14ec
document_version_independent_id: 5ea03ce0-38b9-e005-a430-e98442e2ec83
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/manage-deployment-of-add-ins.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/manage-deployment-of-add-ins
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/manage-deployment-of-add-ins.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/19e6356c-ba1e-4d22-9557-6222c183f04d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/01e6eca5-e701-4cd9-a21f-56c9258f473e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 89bdc0a7-c492-dc5c-e32f-5dd7387f317a
---

# Deploy Office Add-ins in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn

Note

The [integrated apps portal](test-and-deploy-microsoft-365-apps) is the recommended and most feature-rich way for most customers to centrally deploy Office Add-ins to users and groups within your organization. If that method isn't available for your organization, use the add-in portal as described in Deploy an Office Add-in using the admin center later in this article.

Office Add-ins help you personalize your documents and streamline the way you access information on the web. As an admin, you can deploy Office Add-ins for the users in your organization by using the centralized deployment feature in the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339). For more information, see [Start using your Office Add-in](https://support.microsoft.com/office/82e665c4-6700-4b56-a3f3-ef5441996862).

For more information on how to determine if your organization can support centralized deployment, see [Determine if centralized deployment of Office Add-ins works for your organization](centralized-deployment-of-add-ins).

To learn more about managing add-ins after deployment, see [Manage add-ins in the Microsoft 365 admin center](manage-addins-in-the-admin-center).

Note

There are other ways for deploying Office Add-ins in certain scenarios. For more information, see [Deploy and publish Office Add-ins](/en-us/office/dev/add-ins/publish/publish).

## Recommended rollout strategy for Office Add-ins

To roll out add-ins by using a phased approach, follow these steps:

1. Roll out the add-in to a small set of business stakeholders and members of the IT department. If the deployment is successful, move to the next step.
2. Roll out the add-in to more individuals within the business. Again, evaluate the results and, if successful, continue with full deployment.
3. Perform a full rollout to all users.

Depending on the size of the target audience, you can add or remove roll-out steps.

## Deploy an Office Add-in using the admin center

Before you begin, see [Determine if centralized deployment of add-ins works for your organization](centralized-deployment-of-add-ins).

To deploy an Office Add-in using the Microsoft 365 admin center, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. From the left navigation bar, select **... Show all**, and then select **Settings** &gt; **Integrated apps**.
3. Select the **Add-ins** link near the top of the **Integrated apps** page.
4. Select **Deploy Add-in** at the top of the page.

    [![Screenshot of the Deploy New Add-in button in the admin center.](../../media/deployaddin.png)](../../media/deployaddin.png#lightbox)
5. Select **Next** on the **Deploy a new add-in** wizard.
6. Select an option and follow the instructions. **Office Store** refers to Microsoft Marketplace.

    [![Screenshot of the options for choosing the add-in deployment location.](../../media/chooseofficestore.png)](../../media/chooseofficestore.png#lightbox)
7. If you select the option to add an add-in from Microsoft Marketplace, make your add-in selection.

    You can view available add-ins by categories: **Suggested for you**, **Rating**, or **Name**. After you select an add-in, accept the terms and conditions to proceed.

    [![Screenshot of the add-in selection page in the Microsoft Marketplace.](../../media/addanaddin.png)](../../media/addanaddin.png#lightbox)

    Note

    When you use the Microsoft Marketplace (Microsoft Store) option, updates and enhancements are automatically deployed to users.
8. If you choose to upload a custom add-in, carry out the following steps:

    1. In the **Choose how to upload app** section, do one of the following steps:

        - Select the option to upload the manifest, and then select the **Choose File** button. Navigate to the add-in's manifest and select it.

            Important

            Only add-ins that use the add-in only manifest can be deployed from the add-in portal at this time. To deploy an add-in that uses the Microsoft 365 unified manifest, you must use the integrated apps portal. See [Office Add-ins manifest](/en-us/office/dev/add-ins/develop/add-in-manifests) for information about the difference.
        - Select the option to provide a URL for the manifest, and then fill in the URL.
    2. Select **Upload**.
9. On the next page, select **Everyone**, **Specific users/groups**, or **Just me** to specify who the add-in is deployed to. Use the Search box to find specific users or groups. 

    [![Screenshot of the user and group selection page for add-in deployment.](../../media/selectusers.png)](../../media/selectusers.png#lightbox)

    Note

    To learn about other states that apply to an add-in, see [Add-in states](manage-addins-in-the-admin-center#add-in-states-in-the-microsoft-365-admin-center).
10. Select **Deploy**.
11. A green checkmark appears when the add-in is deployed. To test the add-in, follow the on-page instructions.

    Note

    Users might need to relaunch the relevant Office application to view the add-in icon on the ribbon. Office Add-ins can take 24-72 hours to appear on the ribbon.
12. When finished, select **Next**. If you deployed the add-in to just yourself, select **Change who has access to add-in** to deploy to more users.

    If you deploy the add-in to other members of your organization, follow the instructions to announce the deployment of the add-in. 

    It's good practice to inform users and groups that the deployed add-in is available. Consider sending an email that describes when and how to use the add-in. Include or link to Help content or FAQs that might help users if they have problems with the add-in.

### Considerations when assigning an add-in to users and groups

Exchange admins can assign an add-in to everyone or to specific users and groups. Each option has implications:

- **Everyone**: This option assigns the add-in to every user in the organization. Use this option sparingly and only for add-ins that are truly universal to your organization.
- **Users**: If you assign an add-in to an individual user, and then deploy the add-in to a new user, you must first add the new user.
- **Groups**: If you assign an add-in to a group, users who are added to the group are automatically assigned the add-in. When a user is removed from a group, the user loses access to the add-in. In either case, no additional action is required from the admin.
- **Just me**: If you assign an add-in to just yourself, the add-in is assigned to only your account, which is ideal for testing the add-in.

The right option for your organization depends on your configuration. However, we recommend making assignments by using groups. As an admin, you might find it easier to manage add-ins by using groups and controlling the membership of those groups rather than assigning individual users each time. In some situations, you might want to restrict access to a small set of users by assigning specific users manually.

## Security and permission considerations for admins

Office Add-ins combine a manifest file that contains some metadata about the add-in, but most importantly points to a web application that contains the code and logic. Office Add-ins can range in their capabilities. For example, add-ins can:

- Display data.
- Provide contextual services by reading a user's document.
- Provide value to that user by reading and writing data to and from a user's document.

For more information about the types and capabilities of Office Add-ins, see [Office Add-ins platform overview](/en-us/office/dev/add-ins/overview/office-add-ins), especially the section "Anatomy of an Office Add-in."

To interact with the user's document, the add-in needs to declare what permission it needs in the manifest. A five-level JavaScript API access-permissions model provides the basis for privacy and security for users of task pane add-ins. Most add-ins in Microsoft Marketplace are level **read/write document** with most add-ins supporting at least the **read document** level. For more information about the permission levels, see [Requesting permissions for API use in content and task pane add-ins](/en-us/office/dev/add-ins/develop/requesting-permissions-for-api-use-in-content-and-task-pane-add-ins).

When you update a manifest, typical changes are to an add-in's icon and text. Occasionally, add-in commands change. However, the permissions of the add-in don't change. The web application where the code and logic for the add-in runs can change at any time, which is the nature of web applications.

Updates for add-ins happen as follows:

- **Line-of-business (LOB) add-in**: In this case, where an admin uploaded a manifest, the admin must upload the new manifest file to support metadata changes. The next time a user starts the relevant Microsoft 365 productivity application, the add-in updates.

    Note

    To deploy the update, select the LOB add-in and choose the **Update Button** in the bottom right corner.
- **Microsoft Marketplace add-in**: When an admin selected an add-in from Microsoft Marketplace and then the developer updated the manifest in Microsoft Marketplace, the admin doesn't have to take any action. The next time a user starts the relevant Microsoft 365 productivity application, the add-in updates.