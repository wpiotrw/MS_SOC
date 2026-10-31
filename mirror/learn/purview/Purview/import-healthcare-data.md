---
layout: Conceptual
title: Set up a connector to import generic healthcare audit data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/import-healthcare-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Administrators can set up a data connector to import electronic healthcare records (EHR) data from their healthcare system to Microsoft 365. This lets you use EHR data in insider risk management policies to help you detect unauthorized access activity to patient data by your employees.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-03-30T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-connectors
search.appverid:
- MET150
ms.collection:
- purview-compliance
- data-connectors
ai-usage: ai-assisted
ms.custom: sfi-image-nochange
locale: en-us
document_id: e71dca11-35c4-7e7a-7691-61de72672149
document_version_independent_id: e71dca11-35c4-7e7a-7691-61de72672149
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/import-healthcare-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: import-healthcare-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/import-healthcare-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 4ead10e5-46a4-55cf-ac10-bb3a31da8661
---

# Set up a connector to import generic healthcare audit data | Microsoft Learn

You can set up a data connector to import auditing data for user activity in your organization's Electronic Healthcare Records (EHR) system. Auditing data from your healthcare EHR system includes data for events related to accessing a patient's health records. Microsoft Purview [Insider Risk Management solution](insider-risk-management) uses healthcare EHR auditing data to help protect your organization from unauthorized access to patient information.

Setting up a Healthcare connector consists of the following tasks:

- Creating an app in Microsoft Entra ID to access an API endpoint that accepts a tab-separated text file containing healthcare EHR auditing data.
- Creating a text file with all the required fields as defined in the connector schema.
- Creating a Healthcare connector instance in the [Microsoft Purview portal](purview-portal).
- Running a script to push healthcare EHR auditing data to the API endpoint.
- Optionally, scheduling the script to run automatically to import the auditing data.

## Before you begin

- Assign the Data Connector Admin role to the user who creates the Healthcare connector in Step 3. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).
- Determine how to retrieve or export the data from your organization's healthcare EHR system (on a daily basis) and create a text file that's described in Step 2. The script that you run in Step 4 pushes the data in the text file to the API endpoint.
- Understand that the sample script you run in Step 4 pushes the healthcare EHR auditing data from a text file to the connector API so that the insider risk management solution can use it. This sample script isn't supported under any Microsoft standard support program or service. The sample script is provided AS IS without warranty of any kind. Microsoft further disclaims all implied warranties including, without limitation, any implied warranties of merchantability or of fitness for a particular purpose. You assume all risk arising from the use or performance of the sample script and documentation. In no event shall Microsoft, its authors, or anyone else involved in the creation, production, or delivery of the scripts be liable for any damages whatsoever (including, without limitation, damages for loss of business profits, business interruption, loss of business information, or other pecuniary loss) arising out of the use of or inability to use the sample scripts or documentation, even if Microsoft has been advised of the possibility of such damages.

## Step 1: Create an app in Microsoft Entra ID

First, create and register a new app in Microsoft Entra ID. The app corresponds to the Healthcare connector that you create in Step 3. When you create the app, Microsoft Entra ID can authenticate the push request for a text file containing healthcare EHR auditing data. During the creation of this Microsoft Entra app, save the following information. You use these values in later steps.

- Microsoft Entra application ID (also called the *app Id* or *client Id*)
- Microsoft Entra application secret (also called the *client secret*)
- Tenant Id (also called the *directory Id*)

For step-by-step instructions for creating an app in Microsoft Entra ID, see [Register an application with the Microsoft identity platform](%5Cazure%5Cactive-directory%5Cdevelop%5Cquickstart-register-app).

## Step 2: Prepare a text file with healthcare EHR auditing data

Next, create a text file that contains information about employees' access to patient health records in your organization's healthcare EHR system. As previously explained, determine how to generate this text file from your healthcare EHR system. The Healthcare connector workflow requires a text file with tab-separated values to map that data in the text file with required connector schema. The supported file formats are comma (.csv), pipe (.psv), or tab (.tsv) separated text files.

Note

The maximum size of the text file that contains the auditing data is 3 GB. The maximum number of rows is 5 million. Also, be sure to only include the relevant auditing data from your healthcare EHR system.

The following table lists the fields that are required to enable insider risk management scenarios. A subset of these fields is mandatory. These fields are highlighted with an asterisk (\*). If the text file is missing any of the mandatory fields, the file isn't validated and the data in the file isn't imported.

| Field | Category |
| --- | --- |
| Creation Time\*Event Name\*Workstation IdEvent SectionEvent Category | These fields are used to identify access activity events in your healthcare EHR system. |
| Patient Reg IdPatient First Name\*Patient Middle Name Patient Last Name\* Patient Address Line 1\* Patient Address Line 2Patient City\* Patient Zip Code\* Patient State Patient Country Patient Department | These fields are used to identify patient profile information. |
| Restricted Access Reason\* Restricted Access Comment | These fields are used to identify access to restricted records. |
| Email Address (UPN) or SamAccountName\*Employee User Name  Employee Id  Employee Last Name ^1^ Employee First Name ^1^ | These fields are used to identify employee profile information for address and name matching required to determine access to Family/Neighbor/Employee records. |
|  |  |

Note

^1^This field might not be available by default in your healthcare EHR system. You need to configure the export to ensure the text file contains this field.

## Step 3: Create the Healthcare connector

In this step, you create a Healthcare connector in the Microsoft Purview portal. After you run the script in Step 4, the connector processes the text file you created in Step 2 and pushes it to the API endpoint you set up in Step 1. Be sure to copy the JobId generated when you create the connector. You need the JobId when you run the script.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. From the list, select **Healthcare (preview)**.
5. Accept the terms of service.
6. On the **Authentication credentials** page, enter the following information and select **Next**:

    1. Enter or paste the Microsoft Entra application ID for the Azure app that you created in Step 1.
    2. Enter a name for the healthcare connector.
7. On the **File mapping method** page, select one of the following options and select **Next**:

    - **Upload a sample file**. Select **Upload sample file** to upload the file that you prepared in Step 2. With this option, you can quickly select column names in your text file from a drop-down list to map the columns to the required schema for the healthcare connector.

    Or

    - **Manually provide the mapping details**. Type the name of the columns in your text file to map the columns to the required schema for the healthcare connector.
8. On the **File mapping details** page, complete one of the following steps, depending on whether you uploaded a sample file in the previous step:

    - Use the dropdown lists to map the columns from the sample file to each required field for the healthcare connector.

    Or

    - For each field, type the column name from the file that you prepared in Step 2 that corresponds to the field for the healthcare connector.
9. On the **Review** page, review your settings and select **Finish** to create the connector.

    A status page confirms the connector was created. This page contains two important items that you need to complete the next step to run the sample script to upload your healthcare EHR auditing data.

    - **Job ID.** You need this job ID to run the script in the next step. You can copy it from this page or from the connector flyout page.
    - **Link to sample script.** Select the **here** link to go to the GitHub site to access the sample script. The link opens a new window. Keep this window open so that you can copy the script in Step 4. Alternatively, you can bookmark the destination or copy the URL so you can access it again when you run the script. This link is also available on the connector flyout page.
10. Select **Done**.

    The new connector appears in the list on the **Connectors** tab.
11. Select the Healthcare connector that you just created to display the flyout page, which contains properties and other information about the connector.

If you haven't already done so, copy the values for the **Azure App ID** and **Connector job ID**. You need these values to run the script in the next step. You can also download the script from the flyout page or using the link in the next step.

Select **Edit** to change the Azure App ID or the column header names that you defined on the **File mapping** page.

## Step 4: Run the sample script to upload your healthcare EHR auditing data

The last step in setting up a Healthcare connector is to run a sample script that uploads the healthcare EHR auditing data in the text file (that you created in Step 1) to the Microsoft cloud. Specifically, the script uploads the data to the Healthcare connector. After you run the script, the Healthcare connector that you created in Step 3 imports the healthcare EHR auditing data to your Microsoft 365 organization where other compliance tools, such as the Insider Risk Management solution, can access it. After you run the script, consider scheduling a task to run it automatically on a daily basis so the most current employee termination data is uploaded to the Microsoft cloud. For more information, see (Optional) Step 6: Schedule the script to run automatically.

Note

As previously stated, the maximum size of the text file that contains the auditing data is 3 GB. The maximum number of rows is 5 million. The script that you run in this step takes about 30 to 40 minutes to import the auditing data from large text files. Additionally, the script divides large text files into smaller blocks of 100K rows, and then imports those blocks sequentially.

1. Go to the window that you left open from the previous step to access the GitHub site with the sample script. Alternatively, open the bookmarked site or use the URL that you copied. You can also access the script [here](https://github.com/microsoft/m365-compliance-connector-sample-scripts/blob/main/sample_script.ps1).
2. Select the **Raw** button to display the script in text view.
3. Copy all the lines in the sample script and save them to a text file.
4. Modify the sample script for your organization, if necessary.
5. Save the text file as a Windows PowerShell script file by using a filename suffix of `.ps1`; for example, `HealthcareConnector.ps1`.
6. Open a Command Prompt on your local computer, and go to the directory where you saved the script.
7. Run the following command to upload the healthcare audit data in the text file to Microsoft cloud; for example:

    ```powershell
    .\HealthcareConnector.ps1 -tenantId <tenantId> -appId <appId>  -appSecret <appSecret>  -jobId <jobId>  -filePath '<filePath>'
    ```

The following table describes the parameters to use with this script and their required values. Use the information you obtained in the previous steps for these values.

| Parameter | Description |
| --- | --- |
| tenantId | This is the Id for your Microsoft 365 organization that you obtained in Step 1. You can also obtain the tenant Id for your organization on the **Overview** blade in the Microsoft Entra admin center. This value identifies your organization. |
| appId | This is the Microsoft Entra application Id for the app that you created in Microsoft Entra ID in Step 1. Microsoft Entra ID uses this value for authentication when the script attempts to access your Microsoft 365 organization. |
| appSecret | This is the Microsoft Entra application secret for the app that you created in Microsoft Entra ID in Step 1. This value is also used for authentication. |
| jobId | This is the job ID for the Healthcare connector that you created in Step 3. This value associates the healthcare EHR auditing data that you upload to the Microsoft cloud with the Healthcare connector. |
| filePath | This is the file path for the text file (stored on the same system as the script) that you created in Step 2. Try to avoid spaces in the file path; otherwise use single quotation marks. |
|  |  |

Here's an example of the syntax for the Healthcare connector script using actual values for each parameter:

```powershell
.\HealthcareConnector.ps1 -tenantId aaaabbbb-0000-cccc-1111-dddd2222eeee -appId 00001111-aaaa-2222-bbbb-3333cccc4444 -appSecret Aa1Bb~2Cc3.-Dd4Ee5Ff6Gg7Hh8Ii9_Jj0Kk1Ll2 -jobId 00001111-aaaa-2222-bbbb-3333cccc4444 -filePath 'C:\Users\contosoadmin\Desktop\Data\healthcare_audit_records.csv'
```

If the upload is successful, the script displays the **Upload Successful** message.

Note

If you have problems running the previous command because of execution policies, see [About Execution Policies](/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) and [Set-ExecutionPolicy](/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) for guidance about setting execution policies.

## Step 5: Monitor the Healthcare connector

After you create the Healthcare connector and push your EHR auditing data, you can view the connector and upload status in the Microsoft Purview portal. If you schedule the script to run automatically on a regular basis, you can also view the current status after the last time the script runs.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select the Healthcare connector that you created to display the flyout page. This page contains the properties and information about the connector.
4. Under **Last import**, select the **Download log** link to open (or save) the status log for the connector. This log contains information about each time the script runs and uploads the data from the text file to the Microsoft cloud.

    The `RecordsSaved` field indicates the number of rows in the text file that the script uploads. For example, if the text file contains four rows, the value of the `RecordsSaved` fields is 4, if the script successfully uploads all the rows in the text file.

If you don't run the script in Step 4, a link to download the script appears under **Last import**. You can download the script and then follow the steps to run the script.

## (Optional) Step 6: Schedule the script to run automatically

To make sure tools like the Insider Risk Management solution always have the latest auditing data from your healthcare EHR system, schedule the script to run automatically every day. You also need to update the EHR auditing data in the same text file on a similar schedule so it contains the latest information about patient records access activities by your employees. The goal is to upload the most current auditing data so the Healthcare connector can make it available to the insider risk management solution.

Use the Task Scheduler app in Windows to automatically run the script every day.

1. On your local computer, select the Windows **Start** button and type **Task Scheduler**.
2. Select the **Task Scheduler** app to open it.
3. In the **Actions** section, select **Create Task**.
4. On the **General** tab, type a descriptive name for the scheduled task, such as **Healthcare connector script**. You can also add an optional description.
5. Under **Security options**, do the following things:

    1. Decide whether to run the script only when you're logged on to the computer or run it when you're logged on or not.
    2. Make sure the **Run with the highest privileges** checkbox is selected.
6. Select the **Triggers** tab, select **New**, and then do the following things:

    1. Under **Settings**, select the **Daily** option, then select a date and time to run the script for the first time. The script runs every day at the same specified time.
    2. Under **Advanced settings**, make sure the **Enabled** checkbox is selected.
    3. Select **Ok**.
7. Select the **Actions** tab, select **New**, and then do the following things:

    ![Action settings to create a new scheduled task for the healthcare connector script.](media/generichealthcareconnectorscheduletask1.png)

    1. In the **Action** dropdown list, make sure that **Start a program** is selected.
    2. In the **Program/script** box, select **Browse**, go to the following location, and select it so the path is displayed in the box: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`.
    3. In the **Add arguments (optional)** box, paste the same script command that you ran in Step 4. For example, `.\HealthcareConnector.ps1 -tenantId "aaaabbbb-0000-cccc-1111-dddd2222eeee" -appId "00001111-aaaa-2222-bbbb-3333cccc4444" -appSecret "Aa1Bb~2Cc3.-Dd4Ee5Ff6Gg7Hh8Ii9_Jj0Kk1Ll2" -jobId "00001111-aaaa-2222-bbbb-3333cccc4444" -filePath "C:\Healthcare\audit\records.txt"`
    4. In the **Start in (optional)** box, paste the folder location of the script that you ran in Step 4. For example, C:\Healthcare\audit.
    5. Select **Ok** to save the settings for the new action.
8. In the **Create Task** window, select **Ok** to save the scheduled task. You might be prompted to enter your user account credentials.

    The new task appears in the Task Scheduler Library.

    ![The new task for the healthcare connector script is displayed in the Task Scheduler Library.](media/healthcareconnectortaskschedulerlibrary.png)

    The last time the script ran and the next time it's scheduled to run is displayed. You can double-select the task to edit it.

    You can also verify the last time the script ran on the flyout page of the corresponding Healthcare connector in the Microsoft Purview portal.