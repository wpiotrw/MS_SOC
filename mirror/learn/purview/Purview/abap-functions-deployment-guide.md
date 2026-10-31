---
layout: Conceptual
title: SAP ABAP function module deployment guide - Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/abap-functions-deployment-guide
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article outlines the steps to deploy the ABAP function module in your SAP server.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: jingwant
ms.service: purview
ms.subservice: purview-data-map
ms.topic: install-set-up-deploy
ms.date: 2022-08-03T00:00:00.0000000Z
locale: en-us
document_id: 82ec4adf-5f0f-8c9c-9f0c-a8f13a249776
document_version_independent_id: 82ec4adf-5f0f-8c9c-9f0c-a8f13a249776
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/abap-functions-deployment-guide.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: abap-functions-deployment-guide
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/abap-functions-deployment-guide.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b665c3e3-8fc8-4435-ef5a-4d6fb69c7fba
---

# SAP ABAP function module deployment guide - Microsoft Purview | Microsoft Learn

When you scan [SAP ECC](register-scan-sapecc-source), [SAP S/4HANA](register-scan-saps4hana-source), and [SAP BW](register-scan-sap-bw) sources in Microsoft Purview, you need to create the dependent ABAP function module in your SAP server. Microsoft Purview invokes this function module to extract the metadata from your SAP system during scan.

This article describes the steps required to deploy this module.

Note

The following instructions were compiled based on the SAP GUI v. 7.2.

## Prerequisites

Download the SAP ABAP function module source code from the Microsoft Purview governance portal. After you register a source for [SAP ECC](register-scan-sapecc-source), [SAP S/4HANA](register-scan-saps4hana-source), or [SAP BW](register-scan-sap-bw), you can find a download link on top as shown in the following image. You can also see the link when you create a new scan or edit a scan. To download this code, you need to have Data Source Administrator permissions on the root collection in your data map.

![Screenshot that shows the download link for the ABAP function module source code from the Microsoft Purview governance portal.](media/abap-functions-deployment-guide/download-abap-code.png)

## Deploy the module

Follow the instructions to deploy a module.

### Create a package

This step is optional, and an existing package can be used.

1. Sign in to the SAP server and open **Object Navigator** (SE80 transaction).
2. Select **Package** from the list and enter a name for the new package. For example, use **Z\_MITI**. Then select **Display**.
3. In the **Create Package** window, select **Yes**. In the **Package Builder: Create Package** window, enter a value in the **Short Description** box. Select the **Continue** icon.
4. In the **Prompt for local Workbench request** window, select **Own Requests**. Select the **development** request.

### Create a function group

1. In **Object Navigator**, select **Function Group** from the list and enter a name in the input box. For example, use **Z\_MITI\_FGROUP**. Select the **View** icon.
2. In the **Create Object** window, select **yes** to create a new function group.
3. Enter a description in the **Short Text** box and select **Save**.
4. Select a package that was prepared in the **Create a Package** step, and select **Save**.
5. Confirm a request by selecting **Continue**.
6. Activate the function group.

### Create the ABAP function module

1. After the function group is created, select it.
2. Select and hold (or right-click) the function group name in the repository browser. Select **Create** and then select **Function Module**.
3. In the **Function module** box, enter **Z\_MITI\_DOWNLOAD** in case of SAP ECC or S/4HANA and **Z\_MITI\_BW\_DOWNLOAD** in case of SAP BW. Enter a description in the **Short Text** box.

After the module is created, specify the following information:

1. Go to the **Attributes** tab.
2. Under **Processing Type**, select **Remote-Enabled Module**.

    ![Screenshot that shows registering the sources option as Remote-Enabled Module.](media/abap-functions-deployment-guide/processing-type.png)
3. Go to the **Source code** tab. There are two ways to deploy code for the function:

    1. On the main menu, upload the text file you downloaded from the Microsoft Purview governance portal as described in Prerequisites. To do so, select **Utilities** &gt; **More Utilities** &gt; **Upload/Download** &gt; **Upload**.
    2. Alternatively, open the file and copy and paste the contents in the **Source code** area.
4. Go to the **Import** tab and create the following parameters:

    1. *P\_AREA TYPE DD02L-TABNAME* (**Optional** = True)
    2. *P\_LOCAL\_PATH TYPE STRING* (**Optional** = True)
    3. *P\_LANGUAGE TYPE L001TAB-DATA DEFAULT 'E'*
    4. *ROWSKIPS TYPE SO\_INT DEFAULT 0*
    5. *ROWCOUNT TYPE SO\_INT DEFAULT 0*

    Note

    Select the **Pass Value** checkbox for all the parameters.

    ![Screenshot that shows registering the sources option as Import parameters.](media/abap-functions-deployment-guide/import.png)
5. Go to the **Tables** tab and define *EXPORT\_TABLE LIKE TAB512*.

    ![Screenshot that shows the Tables tab.](media/abap-functions-deployment-guide/export-table.png)
6. Go to the **Exceptions** tab and define the exception *E\_EXP\_GUI\_DOWNLOADFAILED*.

    ![Screenshot that shows the Exceptions tab.](media/abap-functions-deployment-guide/exceptions.png)
7. Save the function by selecting **Ctrl+S**. Or select **Function module** and then select **Save** on the main menu.
8. Select the **Activate** icon on the toolbar and then select **Continue**. You can also select **Ctrl+F3**. If prompted, select the generated includes to be activated along with the main function module.

### Test the function

After you finish the previous steps, test the function:

1. Open the **Z\_MITI\_DOWNLOAD** or **Z\_MITI\_BW\_DOWNLOAD** function module you created.
2. On the main menu, select **Function Module** &gt; **Test** &gt; **Test Function Module**. You can also select **F8**.
3. Enter a path to the folder on the local file system in the parameter *P\_LOCAL\_PATH*. Then select the **Execute** icon on the toolbar. You can also select **F8**.
4. Enter the name of the area of interest in the **P\_AREA** field if a file with metadata must be downloaded or updated. After the function finishes working, the folder indicated in the *P\_LOCAL\_PATH* parameter must contain several files with metadata inside. The names of files mimic areas that can be specified in the **P\_AREA** field.

The function finishes its execution and metadata is downloaded much faster if it's launched on the machine that has a high-speed network connection with the SAP server.