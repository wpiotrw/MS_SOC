---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Manage Industry news - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-industry-news?view=o365-worldwide
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
ms.date: 2020-09-24T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_TOC
- operations-pod
ms.custom:
- AdminSurgePortfolio
- admindeeplinkMAC
- tenant
search.appverid:
- MET150
description: Provide your users with up-to-date news headlines about your industry and info from your organization, use the News service to enable a customized news feed for your organization.
locale: en-us
document_id: 92701183-1413-9e14-3109-53c2debe7d8b
document_version_independent_id: c1b54dbd-ac96-4582-b577-f09e8beba365
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/manage-industry-news.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/manage-industry-news
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/manage-industry-news.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 89d35fdb-5974-0938-c73c-c0f34820e865
---

# Manage Industry news - Microsoft 365 admin | Microsoft Learn

Note

Bing news & Industry updates are available only for en-US at this time.

To provide your users with up-to-date news headlines about your industry and info from your organization, use the News service to enable a customized news feed for your organization. You can also enable a daily Industry Updates email, and manage settings for the Bing homepage and Microsoft Edge new tab page.

## What your users will see

You have the option to send your users a daily Industry Updates email with headlines and links to full articles. Users can customize their email updates by following additional topics, choosing when the update is delivered, excluding articles behind paywalls, and selecting the number of articles they want to see.

Signed-in users who go to the Bing homepage see your industry's news feed under the personalized info for your organization.

![Screenshot of image carousel with industry news from the web.](../../media/manage-industry-news-2.jpg)

![Industry Updates page with date and headlines.](../../media/industry-updates-new.png)

They can also see company, industry, and internal news or personalized work information on their Microsoft Edge new tab page.

![Microsoft in news homepage.](../../media/manage-industry-news-3.png)

## News settings

As an admin, you control the News feed settings for your organization, including the selected industry and the Bing homepage, the Microsoft Edge new tab page (Starting with the release of Edge 87), and the email experiences.

1. In the Microsoft 365 admin center, go to **Settings** &gt; **Org settings** &gt; **Services** &gt; [News](https://admin.cloud.microsoft/?#/Settings/Services/:/Settings/L1/BingNews).
2. In the **News** panel, click the **General** tab.
3. In the **Industry** list, select your organization's industries. This determines the general news that appears in your organization news feed. Microsoft may pre-select an industry using information from your account. You can remove or add industries by updating the **Industry** list.
4. In the **Topics** field, enter topics that you want see news articles about. Your users can't change these topics.
5. You can block articles containing keywords in the **Exclude content** field. For example, to avoid articles containing the keyword "bake" from showing up in the news feed, add the keyword "bake" in the **Exclude content** field. Avoid including general terms (the, it, and, etc.); they can block relevant content from appearing in your enterprise news feeds.
6. Select **Save**. It may take up to 24 hours for changes to appear.

## Industry updates in email

You can send a daily email update with relevant industry news to your users' inboxes. To set daily email updates for users:

1. In the Microsoft 365 admin center, go to **Settings** &gt; **Org settings** &gt; **Services** &gt; [News](https://admin.cloud.microsoft/?#/Settings/Services/:/Settings/L1/BingNews).
2. In the **News** panel, click the **Industry Updates** tab.
3. Select **Send daily email updates** to send an email to your users.
4. To give users the ability to customize the news they get in their email updates, select **Allow users to customize their own topics**.

## Bing homepage

You can customize the Bing homepage to include news about your industry.

### Toggle news for Business or Enterprise plans

1. In the Microsoft 365 admin center, go to **Settings** &gt; **Org settings** &gt; **Services** &gt; [News](https://admin.cloud.microsoft/?#/Settings/Services/:/Settings/L1/BingNews).
2. In the **News** panel, click the **Bing homepage** tab, and select **Include on Bing homepage**.

    The industry news appears under the personalized info from your organization on Bing.com.

### Toggle news types for Education plans

1. In the Microsoft 365 admin center, go to **Settings** &gt; **Org settings** &gt; **Services** &gt; [News](https://admin.cloud.microsoft/?#/Settings/Services/:/Settings/L1/BingNews).
2. In the **News** panel, click the **Bing homepage** tab, you have the option to select whether *trending news* or *industry news* show for your users.

![Toggles for industry news and trending news.](../../media/enable-news-for-edu.png)

## Microsoft Edge new tab page

When your users sign in to Microsoft Edge (release 87 or higher) with a valid work or school account, they can see news tailored to your organization.

1. In the Microsoft 365 admin center, go to **Settings** &gt; **Org settings** &gt; **Services** &gt; [News](https://admin.cloud.microsoft/?#/Settings/Services/:/Settings/L1/BingNews).
2. In the **News** panel, click **Microsoft Edge new tab page**.
3. Select **Allow Microsoft 365 content on the new tab page**. When enabled, users can customize their new tab to show information from Microsoft 365, including recommended and recent files, along with frequently used SharePoint sites and other information.
4. Select **Show company information and industry news on the new tab page**. News articles about your organization and industry appear for users that choose to see articles on their new tab.