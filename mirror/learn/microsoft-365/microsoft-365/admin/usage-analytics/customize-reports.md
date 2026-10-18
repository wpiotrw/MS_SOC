---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Customize the reports in Microsoft 365 usage analytics - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/usage-analytics/customize-reports?view=o365-worldwide
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
ms.date: 2026-04-29T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- operations-pod
ms.custom: AdminSurgePortfolio
search.appverid:
- BCS160
- MET150
- MOE150
ms.assetid: 9b76065f-29b9-4b89-8059-c5f9db9ddbf6
description: Learn to customize reports in the browser and Power BI Desktop.
locale: en-us
document_id: 5a146d3a-b3d6-8993-e7f6-1b9da59f4ced
document_version_independent_id: 71a7043f-adcf-42d7-1c4b-670306a764f7
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/usage-analytics/customize-reports.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/usage-analytics/customize-reports
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/usage-analytics/customize-reports.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e4f48d48-dfb7-4973-a019-e504674667cb
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/495840e0-c52f-49d2-a584-185aefeb98c7
platformId: f4246566-7da6-4e9e-4e7e-9f68d7bf41ac
---

# Customize the reports in Microsoft 365 usage analytics - Microsoft 365 admin | Microsoft Learn

Microsoft 365 usage analytics provides a dashboard in Power BI that offers insights into how users adopt and use Microsoft 365. The dashboard is just a starting point to interact with the usage data. You can customize the reports for more personalized insights.

You can also use Power BI Desktop to further customize your reports by connecting them to other data sources to gain richer insights about your business.

## Customizing reports in the browser

The following two examples show how to modify an existing visual and how to create a new visual.

### Modify an existing visual

This example shows how to modify the **Activation** tab within the **Activation/Licensing** report.

1. Within the **Activation/Licensing** report, select the **Activation** tab.
2. Enter the edit mode by choosing the **Edit** button on the top through the ![Screenshot of the more page button in Power BI.](../../media/d8da3c19-3f2d-4bf6-811e-faa804f74770.png) button.

    ![Screenshot of clicking Edit report on the top right navigation in Power BI.](../../media/e2c16663-1fbd-4d7f-887c-0cbb891d3b3d.png)
3. On the top right, choose **Duplicate this page**.

    ![Screenshot of choosing Duplicate this page in Power BI.](../../media/b2d18dcd-6b82-4ce7-ab79-1b24e3721309.png)
4. In the bottom right, choose any of the bar charts that show the count of users activating based on the OS such as Android, iOS, Mac, and more.
5. In the **Visualizations** area to the right, select the **X** next to **Mac Count** to remove it from the visual.

    ![Screenshot of removing Mac Count from the visual in Power BI.](../../media/ce3d8358-df57-4f64-bd25-ac5be7fc8713.png)

### Create a new visual

The following example shows how to create a new visual to track new Viva Engage users on a monthly basis.

1. Go to the **Product Usage** report by using the left navigation and select the **Viva Engage** tab.
2. Switch to edit mode by choosing ![Screenshot of the more page button in Power BI.](../../media/d8da3c19-3f2d-4bf6-811e-faa804f74770.png) and **Edit**.
3. At the bottom of the page, select the ![Screenshot of the add page button in Power BI.](../../media/d3b8c117-17d4-4f53-b078-8fefc2155b24.png) to create a new page.
4. In the **Visualizations** area to the right, choose the **Stacked bar chart** (top row, first from left).

    ![Screenshot of selecting Bar Chart in Power BI.](../../media/214c3fed-6eae-43e6-83fb-708a2d74406e.png)
5. To make the visualization larger, select the bottom right of that visualization and drag to resize it.
6. In the **Fields** area to the right, expand the **Calendar** table.
7. Drag **MonthName** to the fields area, directly below the **Axis** heading in the **Visualizations** area.

    ![Screenshot of dragging Month Name in Power BI.](../../media/bff99987-8c4b-4618-89fd-47df557b0ed7.png)
8. In the **Fields** area to the right, expand the **TenantProductUsage** table.
9. Drag **FirstTimeUsers** to the fields area, directly below the **Value** heading.
10. Drag **Product** to the **Filters** area, directly below the **Visual level filters** heading.
11. In the **Filter Type** area that appears, select the **Viva Engage** check box.

    ![Screenshot of selecting Viva Engage checkbox in Power BI.](../../media/82e99730-0de9-42da-928a-76aab0c3e609.png)
12. Just below the list of visualizations, choose the **Format** icon ![Screenshot of the Format icon in Power BI Visualizations.](../../media/ee0602f3-3df5-4930-b862-db1d90ae4ae2.png) .
13. Expand Title and change the **Title Text** value to **First-Time Viva Engage Users by Month**.
14. Change the **Text Size** value to **12**.
15. Change the title of the new page by editing the name of the page on bottom right.
16. Save the report by selecting **Reading View** on top and then **Save**.

## Customizing the reports in Power BI Desktop

For most customers, modifying the reports and chart visuals in Power BI web is sufficient. However, some customers might need to join this data with other data sources to gain richer insights contextual to their own business. In this case, they can customize and build other reports by using Power BI Desktop. You can download [Power BI Desktop](https://go.microsoft.com/fwlink/p/?linkid=849797) for free.

### Use the reporting APIs

You can start by connecting directly to the ODATA reporting APIs from Microsoft 365 that power these reports.

1. Go to **Get data** &gt; **Other** &gt; **ODATA Feed** &gt; **Connect**.
2. In the URL window, enter `https://reports.office.com/pbi/v1.0/<tenantid>`.

    Note

    The reporting APIs are in preview and are subject to change until they go into production.

    ![Screenshot of OData feed URL for Power BI Desktop.](../../media/c0ef967e-a454-4eba-bc8e-61e113170053.png)
3. When prompted to authenticate, enter your Microsoft 365 (organization or school) admin credentials.

    See the [Microsoft 365 Usage Analytics Overview FAQ](usage-analytics-faq) for more information about who is allowed to access the Microsoft 365 Adoption template app reports.
4. Once you authorize the connection, you see the **Navigator** window that shows the available datasets.

    Select all and choose **Load**.

    This action downloads the data into your Power BI Desktop. Save this file and then you can start creating the reports you need.

    ![Screenshot of ODATA values available in the reporting API in Power BI.](../../media/545b4d17-dbbd-4cfc-b75a-a8b27283d438.png)

### Use the Microsoft 365 usage analytics template

You can also use the Power BI template file that corresponds to the Microsoft 365 usage analytics reports as a starting point to connect to the data. The advantage of using the pbit file is that it already has the connection string established. You can also take advantage of all the custom measures that are created on top of the data that the base schema returns and build on it further.

You can download the Power BI template file from the [Microsoft Download Center](https://download.microsoft.com/download/7/8/2/782ba8a7-8d89-4958-a315-dab04c3b620c/Microsoft%20365%20Usage%20Analytics.pbit). After you download the Power BI template file, follow these steps to get started:

1. Open the pbit file.
2. Enter your tenant ID value in the dialog.

    ![Screenshot of entering your tenant ID to open the pbit file in Power BI.](../../media/071ed0bf-8b9d-49c6-81fc-fd4c6cc85bd3.png)
3. Enter your admin credentials to authenticate to Microsoft 365 when prompted.

    Once authorized, the data is refreshed in the Power BI file.

    Data load might take some time. When it's complete, you can save the file as a .pbix file and continue to customize the reports or bring another data source into this report.
4. Follow [Getting started with Power BI](/en-us/power-bi/fundamentals/desktop-getting-started) documentation to understand how to build reports, publish them to the Power BI service, and share with your organization. Following this path for customization and sharing might require more Power BI licenses. See Power BI [licensing guidance](https://go.microsoft.com/fwlink/p/?linkid=849803) for details.