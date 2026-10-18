---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Customize the theme for your organization - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/setup/customize-your-organization-theme?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- CSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2026-02-02T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier3
- scotvorg
- highpri
- M365-subscription-management
- Adm_O365
- Adm_TOC
- operations-pod
ms.custom:
- VSBFY23
- AdminSurgePortfolio
- okr_smb
- AdminTemplateSet
- tenant
description: Learn to change the default theme for the top of the navigation bar in Microsoft 365 and customize it to match your company logo or color.
locale: en-us
document_id: 9f6c85cc-1680-588e-f520-bcafb1383d53
document_version_independent_id: ea446e6b-e094-dacd-54cc-e597b2f1354d
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/setup/customize-your-organization-theme.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/setup/customize-your-organization-theme
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/setup/customize-your-organization-theme.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 32c801da-e681-178a-2311-ae3723d2d73c
---

# Customize the theme for your organization - Microsoft 365 admin | Microsoft Learn

Check out all of our small business content on [Small business help & learning](https://go.microsoft.com/fwlink/?linkid=2224585).

As the admin of your organization, you can create multiple themes for the people in your organization, and select which themes apply to different members of your organization. The organization theme is what appears in the top navigation bar for people in your organization.

You can add or update a default theme that applies to everyone in your organization. You can also create up to four additional group themes that can be assigned to multiple Microsoft 365 groups.

## Add or update your organization's theme

1. In the admin center, go to the **Settings** &gt; **Org Settings** page, and then choose the **Organization profile** tab.
2. On the **Organization profile** tab, select **Custom themes**.
3. Choose **Add theme** and add the required info for the tabs.

    All organization themes can be customized using the following tabs.

    | Tab | What can you do? |
    | --- | --- |
    | General | Modify a theme name and assign to up to five groups (if applicable). |
    | Logos | Add your organization logo, including alternate logo for dark theme. |
    | Colors | Customize a color scheme by specifying navigation bar, accent, text and icon colors. |

## General: Modify a theme

Your experience on the General tab depends on whether you're adding or modifying the default theme or a group theme.

### Update the default theme

The default theme is the first theme displayed.

1. If you previously customized a theme for your organization, select **Default Theme** and use one of your saved customizations, or, select **Add theme**.
2. On the **General** page, you can prevent users from overriding their theme and show the user's display name.
3. Select **Save** to save your changes.

Important

The default theme is unique, it can't be renamed and applies to everyone within your organization. To delete the default theme, you have to delete all other themes first.

![Screenshot: General tab showing the default theme for your organization.](../../media/default_theme_panel1.png)

### Create a group theme

You can create up to four additional group themes.

1. On the **General** page, enter a name for your new theme.
2. Under **Groups**, you can select up to 5 Microsoft 365 Groups that can see your group theme, instead of using the default theme. You can also prevent users from overriding their theme and show the user's display name.
3. Select **Save**.

![Screenshot: General tab showing the default theme for a group of users in your organization.](../../media/default-theme-general-users1.png)

## Logos: Specify your theme logos

On the **Logos** page, you can add your logos, and specify the URL where users will navigate to when they select the logo.

- **Default logo**: Add a URL location that points to your logo. Make sure that the URL uses HTTPS. Add an HTTPS image url that allows anonymous access and doesn't require authentication. For default theme, you also have an option to upload a logo image that is less than 10kb. Your default logo can be in the JPG, PNG, GIF, or SVG format. For SVG images, they will be resized to fit 24 pixels vertically. JPG, PNG, GIF images will be scaled to fit 200 x 48 pixels. Logo aspect ratio will always be preserved.
- **Alternate logo**: Add a URL location that points to your logo. Your alternate logo should be optimized for use in Microsoft 365 dark themes. Same requirements as the default logo.
- **On-click link**: Add a URL location that points to your logo. You can use your logo as a link to any company resource, for example, your company's website. If you don't select a URL location for your logo, it'll default to the Microsoft 365 home page.

Select **Save** to save your changes.

![Screenshot: Logos tab showing the logo options.](../../media/logos_tab.png)

You can remove your logos at any time. Just return to the **Logos** page and select **Remove**.

Note

The Microsoft 365 suite header is designed to accommodate a variety of screen sizes, window sizes, and display settings. The responsive behavior of the suite header sometimes results in the logo not showing to give space to other capabilities shown on the suite header. To reduce the likelihood of this behavior a narrower image file is recommended.

## Colors: Choose theme colors

On the **Colors** page, you can set the default colors and choose which logo should be used.

- **Navigation bar color**: Select a color to use for the background of the navigation bar. The navigation bar appears at the top on every page.
- **Text and icon color**: Select a color to use for the text and icons on the top navigation bar.
- **Accent color**: Pick one that shows up well on a white or light background. The accent color is used to color some links and buttons that show up on a white or light background. For example, the accent color is used to color elements in a user's inbox and on their microsoft365.com portal page.
- **Reset color**: Select this link to reset colors to the default colors.

    ![Screenshot: Colors tab showing default theme colors for your organization.](../../media/default-theme-colors1.png)

## Frequently asked questions

### My organization already has a theme for all employees. How will this change?

The default theme will continue to be shown to all employees. Adding a new group theme will only be made available to the Microsoft 365 groups associated with that theme.

### Why don't I see group themes in the Admin Center?

Only global admins can customize company themes. Global readers have read-only access.

Important

Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

### How many different themes can I set up for my organization?

Up to five themes can be created. A default theme and four group themes.

### Can I use security groups or distribution groups instead of Microsoft 365 Groups?

No, new group themes must be mapped to one or more Microsoft 365 groups and not security groups or distribution groups.

### Can I manually assign a theme independent of Microsoft 365 Groups?

No, new group themes must be mapped to one or more Microsoft 365 groups. Users who are members of the Microsoft 365 group will get the theme applied to their group. You can [create and add new members to a Microsoft 365 Group](../create-groups/create-groups) by going to the **Settings** &gt; **Groups** in the admin center.

### What happens if a user is assigned to multiple group themes?

Users who are assigned to multiple group themes will be shown the default theme.

### Why can't I delete the default theme?

The default theme can only be deleted once all group themes are deleted. Make sure you delete all group themes before you try to delete the default theme.

### Why am I receiving an error message every time I upload a logo URL?

Make sure the logo you're using is specified as a publicly addressable URL. Follow these steps for [uploading logos to Azure Blob Storage](/en-us/azure/storage/blobs/storage-upload-process-images?tabs=dotnet) or the [Office 365 Content Delivery Network with SharePoint Online](../../enterprise/use-microsoft-365-cdn-with-spo).

### Why am I receiving the message "Doesn't meet minimum color contrast ratio of 4.5:1"?

The recommended contrast ratio between text, icon or button color and background color is 4.5:1. You can override this recommendation and still save your theme as this is not a requirement.

### If I define a theme, which places in Microsoft 365 will this be used?

Any theme appears in the top navigation bar for everyone in the organization as part of the Microsoft 365 suite header.