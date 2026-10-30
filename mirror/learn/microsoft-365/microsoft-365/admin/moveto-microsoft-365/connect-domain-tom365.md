---
layout: Conceptual
monikers:
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Connect your domain to Microsoft 365 - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/moveto-microsoft-365/connect-domain-tom365?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: heidip
author: MicrosoftHeidi
manager: dansimp
ms.date: 2021-01-07T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: m365-core
ms.subservice: migration
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- highpri
- M365-subscription-management
- Adm_O365
- operations-pod
ms.custom:
- VSBFY23
- AdminSurgePortfolio
- adminvideo
- admindeeplinkMAC
search.appverid:
- BCS160
- MET150
- MOE150
description: Learn how to connect your domain to Microsoft 365.
locale: en-us
document_id: dfe40029-0dbc-feb4-3096-a477ae796d13
document_version_independent_id: dfe40029-0dbc-feb4-3096-a477ae796d13
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/moveto-microsoft-365/connect-domain-tom365.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/moveto-microsoft-365/connect-domain-tom365
moniker_range_name: 2ccba01628bf08e8f21ea76d73b162e1
monikers:
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/moveto-microsoft-365/connect-domain-tom365.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 6da775ae-c21b-6e4f-b23b-23a6e10080cd
---

# Connect your domain to Microsoft 365 - Microsoft 365 admin | Microsoft Learn

Check out all of our small business content on [Small business help & learning](https://go.microsoft.com/fwlink/?linkid=2224585).

Check out [Microsoft 365 small business help](https://go.microsoft.com/fwlink/?linkid=2197659) on YouTube.

## Watch: Connect your domain to Microsoft 365

Check out this video and others on our [YouTube channel](https://go.microsoft.com/fwlink/?linkid=2198216).

Once you've set up Microsoft 365 and moved your email data from Google Workspace, you can connect your domain to Microsoft 365.

First you will need to delete existing DNS records from Google, and then we can add new DNS records from Microsoft 365.

1. Sign into your Google Workspace admin console at https://admin.google.com.
2. Select **Domains**, **Manage domains**, **View details**, **Manage domain**, then **DNS** in the left nav.
3. Scroll down to **Synthetic records**, open **Google Workspace**, select **Delete**, then **Delete** again.
4. Scroll down to **Custom resource records** and delete any existing DNS records that appear, including any you may have created previously for Microsoft 365.
5. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
6. In the left nav, choose, **Show all** &gt; **Settings** &gt; [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).
7. Then choose your default domain.
8. Select **Continue setup**, then, to connect your domain, choose **Continue**.
9. Scroll down to view the DNS records that need to be copied to Google.
10. Open **MX Records**, and under **Points to address or value**, copy the record.
11. Return to Google, and in the **Custom resource records** section, open the record type dropdown and select **MX**.
12. In the **Data** field, paste the record you copied.
13. Then select **Add**.
14. Repeat the process for CNAME and TXT records and add the values in the Google DNS management page.
15. Return to the Microsoft 365 admin center and select **Continue**.

    Your domain setup is complete.