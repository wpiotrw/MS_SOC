---
layout: Conceptual
title: Set up a connector to import third-party insider risk detections (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/import-insider-risk-indicators
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Administrators can set up a data connector to import pre-processed aggregated detections and use them in Microsoft Purview Insider Risk Management. This lets you extend your detections to third-party workloads such as Salesforce or Dropbox and use them alongside the built-in detections of insider risk management.
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
ms.custom: admindeeplinkCOMPLIANCE
ai-usage: ai-assisted
locale: en-us
document_id: d5ac3b6c-3f66-da5a-2882-d00cb9db704e
document_version_independent_id: d5ac3b6c-3f66-da5a-2882-d00cb9db704e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/import-insider-risk-indicators.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: import-insider-risk-indicators
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/import-insider-risk-indicators.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 251ff89e-e40a-0328-1aab-781d10a8e09f
---

# Set up a connector to import third-party insider risk detections (preview) | Microsoft Learn

You can set up a connector to extend the Microsoft Purview Insider Risk Management solution to include third-party (non-Microsoft) detections. For example, you might want to extend your detections to include Salesforce and Dropbox activities and use them alongside the built-in detections provided by insider risk management, which focuses on Microsoft services like SharePoint Online and Exchange Online.

To bring your own detections to the insider risk management solution, import preprocessed, aggregated detections from security information and event management (SIEM) solutions such as Microsoft Sentinel or Splunk. Import a sample file into the Insider Risk Indicators connector workflow. The connector workflow analyzes the sample file and configures the required schema for insider risk management.

Note

Currently, you can't import "raw" detection signals into insider risk management. You can only import preprocessed aggregations as a file.

## Overall process

Bringing your own detections to insider risk management is a three-step process:

1. In Microsoft Purview, create the Insider Risk Indicators (preview) connector as described in this article.
2. In the insider risk management solution, [create custom indicators](insider-risk-management-settings-policy-indicators#custom-indicators).
3. In the insider risk management solution, [use the custom indicators in policies as triggers or indicators and define thresholds](insider-risk-management-configure#step-6-required-create-an-insider-risk-management-policy).

When user activity crosses the threshold value that you specify for the policy, the user is brought into scope of the insider risk management policy and is scored for risk. An alert is generated and analysts can investigate the alert using custom indicator details.

Note

You can only use custom indicators with the *Data theft* and *Data leaks* templates.

## Before you begin

- **Determine the scenarios and data you want to import to Microsoft 365**. This determination helps you decide how many CSV files and Insider Risk Indicator connectors you need to create and how to structure the CSV files. The types of triggers and indicators you want to create determine the imported data. See Determining how many CSV files to prepare for indicator data.
- **Determine how to retrieve or export the data from your internal system and add it to the CSV files that you prepare in Step 2**. The script that you run in Step 4 uploads the data in the CSV files to the insider risk management solution.
- **Assign the *Data Connector Admin* role** to the user who creates the connector in Step 3. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).

Important

The sample script that you run in Step 4 uploads your data to the Microsoft cloud so that the insider risk management solution can use it. This sample script isn't supported under any Microsoft standard support program or service. The sample script is provided AS IS without warranty of any kind. Microsoft further disclaims all implied warranties including, without limitation, any implied warranties of merchantability or of fitness for a particular purpose. You assume all risk arising from the use or performance of the sample script and documentation. In no event shall Microsoft, its authors, or anyone else involved in the creation, production, or delivery of the scripts be liable for any damages whatsoever (including, without limitation, damages for loss of business profits, business interruption, loss of business information, or other pecuniary loss) arising out of the use of or inability to use the sample scripts or documentation, even if Microsoft has been advised of the possibility of such damages.

### Determining how many CSV files to prepare for indicator data

In Step 3, you can prepare separate CSV files that contain data for each indicator or prepare a single CSV file that contains data for two or more indicators.

Here are some guidelines to help you determine how many CSV files to prepare:

- If the insider risk management policy you want to implement requires multiple indicators, consider using a single CSV file that contains the data for all the indicators. As a general rule, the number of connectors that you need to create is determined by the services in a CSV file. For example, if a CSV file contains all the services required to support your insider risk management implementation, you only need one connector. Having fewer CSV files allows you to have fewer connectors to create and manage. If you have two separate CSV files that each contain a single service, you need to create two connectors.
- The method for generating or collecting the data might determine the number of CSV files. For example, if the different types of data used to configure a connector are located in a single system in your organization, you might be able to export the data to a single CSV file. But if data is distributed across different systems, it might be easier to export data to different CSV files. How you retrieve or export data from your systems might determine the number of CSV files you need.

## Step 1: Create an app in Microsoft Entra ID

First, create and register a new app in Microsoft Entra ID for the connector that you create in Step 3. When you create this app, Microsoft Entra ID can authenticate the connector when it runs and attempts to access your organization. Use this app to authenticate the script that you run in Step 4 to upload your data to the Microsoft cloud. When you create the Microsoft Entra app, save the following information:

- Microsoft Entra application ID (app ID or client ID)
- Microsoft Entra application secret (client secret)
- Tenant ID (directory ID)

Use these values in Steps 3 and 4. For step-by-step instructions on creating an app in Microsoft Entra ID, see [Register an application with the Microsoft identity platform](/en-us/azure/active-directory/develop/quickstart-register-app?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

## Step 2: Prepare CSV file(s) with your insider risk indicators data

Next, prepare a CSV file that contains the indicator data that the connector imports to Microsoft 365. The insider risk management solution uses this data. You can import data for the following scenarios:

- Create a trigger that, when activated, brings a user into scope for a policy. [Example 1 below](import-insider-risk-indicators#example-1-prepare-a-csv-file-for-a-simple-trigger-that-brings-a-user-into-scope-for-a-policy) shows how to prepare a CSV file for a 'home-grown' trigger that predicts the probability of an employee leaving an organization.
- Create a policy indicator that monitors user activities. [Example 2 below](import-insider-risk-indicators#example-2-prepare-a-single-csv-file-to-create-multiple-policy-indicators) shows how to prepare a single CSV file for multiple indicators (one for Dropbox and one for Salesforce).

For each scenario, provide the corresponding indicator data in one or more CSV files. See Determining how many CSV files to use for indicator data.

After you create the CSV file with the required indicator data, store it on the local computer that you run the script on in Step 4. Implement an update strategy to make sure that the CSV file always contains the most current information so that whenever you run the script, the most current indicator data is uploaded to the Microsoft cloud and accessible to the insider risk management solution.

Important

The column names described in the following sections are examples, not required parameters. You can use any column names in your CSV files. However, the column names that you use in a CSV file must be mapped to a data type when you create the connector in Step 3. Also note that the sample CSV files in the following sections are shown in NotePad. It's much easier to view and edit CSV files in Microsoft Excel.

### Example 1: Prepare a CSV file for a simple trigger that brings a user into scope for a policy

This example shows how to structure a CSV file to create a 'home-grown' trigger that could be used to predict the probability of an employee leaving an organization. This example uses the following sample data:

```text
UserPrincipalName,PredictionTime,PredictionScore,ModelInfo
sarad@contoso.com,2023-04-20T05:52:56.962686Z,6,Model accuracy: 67%, Model name: LeaverPrediction_M1
sarad@contoso.com,2023-04-24T05:52:56.962686Z,9,Model accuracy: 67%, Model name: LeaverPrediction_M1
sarad@contoso.com,2023-04-24T05:52:56.962686Z,3,Model accuracy: 67%, Model name: LeaverPrediction_M1
```

The following table describes each column in the CSV file.

| Column | Description |
| --- | --- |
| UserPrincipalName | The Microsoft Entra UserPrincipalName (UPN) used to identify the user. |
| Prediction Time | Mandatory field that displays the date/time that the activity occurred. Use the following date format: `yyyy-mm-ddThh:mm:ss.nnnnnn+|-hh:mm`, which is the [ISO 8601 date and time format](https://www.iso.org/iso-8601-date-and-time-format.html) |
| Prediction Score | Risky activity score. This field is used for the trigger threshold setting. Only *Number* fields can be used for threshold settings. |
| Model Info | Extra field used to track information about the prediction model. |

Note

Only the UserPrincipalName and date/time fields are mandatory. All other fields are optional but can be helpful for the analyst or investigator in decision making when they triage alerts (these fields appear in the Activity explorer and in alerts and cases).

When you create the connector in Step 3, you'll use the data in the `PredictionScore` field as a threshold value for the trigger. If a user crosses the threshold value that you set later in the policy, the user is brought into the scope of the policy.

### Example 2: Prepare a single CSV file to create multiple policy indicators

This example shows how to create multiple policy indicators (one for Dropbox and one for Salesforce) from a single CSV file. This example uses the following sample data:

```text
User_Principal_Name,Display_Name,Alert_Severity,Alert_Count,Aggregation_Date,Source_Workload,AdditionalInfo_Salesforce,AdditionalInfo_Dropbox
sarad@contoso.com,Salesforce - Sensitive report downloaded and emailed externally,High,10,2023-04-24T05:52:56.962686Z,Salesforce,text,text
sarad@contoso.com,Salesforce - Anomalous download of sales lead reports,Medium,6,2023-04-24T05:52:56.962686Z,Salesforce,text,text
bradh@contoso.com,Salesforce - Printing sales reports,Low,50,2023-04-24T05:52:56.962686Z,Salesforce,text,text
bradh@contoso.com,Salesforce - Excessive modifications to sensitive reports,Medium,3,2023-04-24T05:52:56.962686Z,Salesforce,text,text
sarad@contoso.com,Dropbox - Sensitive files saved to personal Dropbox,High,14,2023-04-24T05:52:56.962686Z,Dropbox,text,text
bradh@contoso.com,Dropbox - Anomalous file copy activity,Medium,5,2023-04-24T05:52:56.962686Z,Dropbox,text,text
```

The following table describes each column in the CSV file.

| Column | Description |
| --- | --- |
| UserPrincipalName | The Microsoft Entra UserPrincipalName (UPN) used to identify the user. |
| Display Name | Name of the risky activity. |
| Alert Severity | Severity categories: *Low*, *Medium*, and *High*. |
| Alert Count | Number of incidences of each activity. Data in this field is used for the indicator threshold setting. |
| Aggregation Date | Mandatory field that displays the date/time that the activity occurred. Use the following date format: `yyyy-mm-ddThh:mm:ss.nnnnnn+|-hh:mm`, which is the [ISO 8601 date and time format](https://www.iso.org/iso-8601-date-and-time-format.html) |
| Source Workload | This is the key field for the multiple indicators scenario. Select this field for the **Source column** field when you create the connector, and use the values in this field (**Dropbox** and **Salesforce**) in the **Related values in source column** field in the connector. |
| Additional Info Salesforce | Any additional info that you want to note about the Salesforce indicator |
| Additional Info Dropbox | Any additional info that you want to note about the Dropbox indicator |

See the following example to see how you use this CSV file when creating the data connector.

## Step 3: Create the Insider Risk Indicators connector

Create a connector in the Microsoft Purview portal. After you run the script in Step 4, the connector imports the data from the CSV file and uploads it to your Microsoft 365 organization.

Note

Before you create a connector, make sure that you have a list of the scenarios and the corresponding CSV column names for each scenario.

### Example 1: Create a connector file for a simple trigger

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. From the list, select **Insider Risk Indicators (preview)**.
5. Review the terms of service, then select **Accept** if you want to continue creating the connector.
6. On the **Authentication** page, complete the following steps:

    1. Enter a name for the connector.
    2. Paste the Microsoft Entra application ID for the Azure app that you created in Step 1.
    3. Select **Next**.
7. On the **Sample file** page:

    1. Select **Upload sample file**, then select the CSV file that you want to upload.
    2. In the **Source column** list, select **None (Single source)**.
    3. In the **Verify sample data and data type** section, review each field to make sure that the right data types are assigned to each field. If a field is used later as a threshold value, make sure that it has a *Number* data type. For example, in this scenario, the `PredictionScore` field is used as a threshold value and the data type is set appropriately to *Number*.
8. Select **Next**.
9. On the **Data mapping** page:

    1. Enter the values for **Event time (UTC time)** and **Microsoft 365 user email address** based on the appropriate values from the CSV file. These fields are mandatory for the connector.
    2. In the **Default** field, use the list to select each field you want to include from the CSV file. For example, select a Number field to use later as a threshold value for the indicator or select other fields to use as supporting information.
10. Select **Next**.
11. On the **Finish** page, review all the information, and if everything looks correct, select **Finish**.
12. Copy the job ID for the connector. You need it for the next step.
13. Go to Step 4 to run the script that uploads the data to Microsoft 365.

### Example 2: Create a connector that includes multiple policy indicators

This example shows how to set up a single connector to create multiple policy indicators for Salesforce and Dropbox. You could create two separate connectors, but creating a single connector that works for both can reduce overall file maintenance.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. From the list, select **Insider Risk Indicators (preview)**.
5. Review the terms of service, then select **Accept** if you want to continue creating the connector.
6. On the **Authentication** page, enter the following information:

    1. Enter a name for the connector.
    2. Paste the Microsoft Entra application ID for the Azure app that you created in Step 2.
    3. Select **Next**.
7. On the **Sample file** page:

    1. Select **Upload sample file**, then select the CSV file that you want to upload.
    2. In the **Source column** list, select the column to use as the source. In the example CSV file, the source column is `SourceWorkload`, since it stores the values for the two separate workloads (Salesforce and Dropbox).
    3. In the **Related values in source column** field, enter the related values. For this example, enter `Salesforce,Dropbox`. Don't include spaces between values.

    Important

    Make sure that the values you enter in the **Related values in source column** field match the values in the **Source column** list. The connector fails if the column values don't match.

    1. In the **Verify sample data and data type** section, review each field to make sure that the right data types are assigned for each field. If a field is used later as a threshold value, make sure that it has a Number data type. For example, in this example scenario, the `AlertCount` field is used as a threshold value and the data type is set appropriately to *Number*.
    2. Select **Next**.
8. On the **Data mapping** page:

    1. Enter the values for **Event time (UTC time)** and **Microsoft 365 user email address** based on the appropriate values from the CSV file. These fields are mandatory and common to both indicators you're creating for this example.
    2. Select the columns from your sample file that you want to map to the two workloads, Salesforce and Dropbox.

    Tip

    You can use the same process described previously to create multiple policy indicators based on severity levels. For example, you can use a single connector to create separate Low, Medium, and High indicators. In the **Source column** list, select the field that holds the values for the separate workloads (Low, Medium, High). Enter those workload values in the **Related values in source column** field. Map the appropriate fields in the **Data mapping** page.
9. Select **Next**.
10. On the **Finish** page, review all the information, and if everything looks correct, select **Finish**.
11. Copy the job ID for the connector. You need it for the next step.
12. Go to the next step (Step 4) to run the script that uploads the data to Microsoft 365.

## Step 4: Run the sample script to upload your data

The last step in setting up a connector is running a sample script that uploads the data in the CSV file. When you run the script, the connector you created in Step 3 imports the data to your Microsoft 365 organization where the insider risk management solution can access it. After you run the script, consider scheduling a task to run it automatically on a daily basis so the most current data is uploaded to the Microsoft cloud. For more information, see Schedule the script to run automatically.

### Before running the script

- Make sure to add the *webhook.ingestion.office.com* domain to your firewall allowlist for your organization. If this domain is blocked, the script doesn't run.
- Make sure to wait 24 hours before uploading the data after you update the custom indicators and the associated policies. This waiting period ensures all components sync. If you immediately upload the data while the updates are syncing, some data might not be scored for risk.
- Make sure that all combinations of UPN and timestamp to be imported are unique. If any record in the uploaded CSV file contains the same timestamp and UPN as other records in the file, the record is dropped.

### Run the sample script

1. Go to the window that you left open from the previous step to access the GitHub site with the sample script. Alternatively, open the bookmarked site or use the URL that you copied. You can also access the script at https://github.com/microsoft/m365-compliance-connector-sample-scripts/blob/main/sample_script.ps1.
2. Select the **Raw** button to display the script in text view.
3. Copy all the lines in the sample script, and save them to a text file.
4. Modify the sample script for your organization, if necessary.
5. Save the text file as a Windows PowerShell script file by using a filename suffix of `.ps1`; for example, `HRConnector.ps1`. Alternatively, you can use the GitHub filename for the script, which is `upload_termination_records.ps1`.
6. Open a command prompt on your local computer, and then go to the directory where you saved the script.
7. Run the following command to upload the data in the CSV file to the Microsoft cloud; for example:

    ```powershell
    .\HRConnector.ps1 -tenantId <tenantId> -appId <appId>  -appSecret <appSecret>  -jobId <jobId>  -filePath '<filePath>'
    ```

    The following table describes the parameters to use with this script and their required values. The information you obtained in the previous steps is used in the values for these parameters.

    | Parameter | Description |
    | --- | --- |
    | `tenantId` | This is the ID for your Microsoft 365 organization that you obtained in Step 1. You can also obtain the tenant ID for your organization on the **Overview** blade in the Microsoft Entra admin center. This value identifies your organization. |
    | `appId` | This is the Microsoft Entra application ID for the app that you created in Microsoft Entra ID in Step 1. This value is used by Microsoft Entra ID for authentication when the script attempts to access your Microsoft 365 organization. |
    | `appSecret` | This is the Microsoft Entra application secret for the app that you created in Microsoft Entra ID in Step 1. This value is also used for authentication. |
    | `jobId` | This is the job ID for the connector that you created in Step 3. This value associates the data that is uploaded to the Microsoft cloud with the connector. |
    | `filePath` | This is the file path for the file (stored on the same system as the script) that you created in Step 1. Try to avoid spaces in the file path; otherwise use single quotation marks. |

    Here's an example of the syntax for the connector script using actual values for each parameter:

    ```powershell
     .\HRConnector.ps1 -tenantId aaaabbbb-0000-cccc-1111-dddd2222eeee -appId 00001111-aaaa-2222-bbbb-3333cccc4444 -appSecret Aa1Bb~2Cc3.-Dd4Ee5Ff6Gg7Hh8Ii9_Jj0Kk1Ll2 -jobId 00001111-aaaa-2222-bbbb-3333cccc4444 -filePath 'C:\Users\contosoadmin\Desktop\Data\insider_risk_indicator_data.csv'
    ```

    If the upload is successful, the script displays the **Upload Successful** message.

    Note

    If you have problems running the previous command because of execution policies, see [About Execution Policies](/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) and [Set-ExecutionPolicy](/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) for guidance about setting execution policies.

## Step 5: Monitor the connector

After you create the connector and run the script to upload your data, view the connector and upload status in the Microsoft Purview portal. If you schedule the script to run automatically on a regular basis, you can view the current status after the last time the script runs.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select the HR connector that you created to display the flyout page. This page contains the properties and information about the connector.
4. Under **Progress**, select the **Download log** link to open (or save) the status log for the connector. This log contains information about each time the script runs and uploads the data from the CSV file to the Microsoft cloud.

    The `RecordsSaved` field indicates the number of rows in the CSV file that uploaded. For example, if the CSV file contains four rows, the value of the `RecordsSaved` field is 4 if the script successfully uploads all the rows in the CSV file.

If you don't run the script in Step 4, a link to download the script is displayed under **Last import**. You can download the script and then follow the steps to run the script.

## (Optional) Step 6: Schedule the script to run automatically

To make sure the insider risk management solution always has the latest data from your organization, schedule the script to run automatically on a recurring basis, such as once a day. This schedule requires updating the data in the CSV file on a similar (if not the same) schedule so that it contains the latest information. The goal is to upload the most current data so that the connector can make it available to the insider risk management solution.

Use the Task Scheduler app in Windows to automatically run the script every day.

1. On your local computer, select the Windows **Start** button and type **Task Scheduler**.
2. Select the **Task Scheduler** app.
3. In the **Actions** section, select **Create Task**.
4. On the **General** tab, enter a descriptive name for the scheduled task. For example, **HR Connector Script**. You can also add an optional description.
5. Under **Security options**, complete the following steps:

    1. Decide whether to run the script only when you're logged on to the computer or when you're logged on or not.
    2. Make sure that the **Run with the highest privileges** check box is selected.
6. Select the **Triggers** tab, select **New**, and complete the following steps:

    1. Under **Settings**, select the **Daily** option, and select a date and time to run the script for the first time. The script runs every day at the same specified time.
    2. Under **Advanced settings**, make sure that the **Enabled** check box is selected.
    3. Select **OK**.
7. Select the **Actions** tab, select **New**, and complete the following steps:

    1. In the **Action** dropdown list, make sure that **Start a program** is selected.
    2. In the **Program/script** box, select **Browse**, then go to the following location and select it so the path is displayed in the box: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`.
    3. In the **Add arguments (optional)** box, paste the same script command that you ran in Step 4. For example, `.\HRConnector.ps1 -tenantId "aaaabbbb-0000-cccc-1111-dddd2222eeee" -appId "00001111-aaaa-2222-bbbb-3333cccc4444" -appSecret "Aa1Bb~2Cc3.-Dd4Ee5Ff6Gg7Hh8Ii9_Jj0Kk1Ll2"  -jobId "00001111-aaaa-2222-bbbb-3333cccc4444" -filePath "C:\Users\contosoadmin\Desktop\Data\insider_risk_indicator_data.csv"`
    4. In the **Start in (optional)** box, paste the folder location of the script that you ran in Step 4. For example, `C:\Users\contosoadmin\Desktop\Scripts`.
    5. Select **OK** to save the settings for the new action.
8. In the **Create Task** window, select **OK** to save the scheduled task. You might be prompted to enter your user account credentials.

    The new task appears in the Task Scheduler Library. You see the last time the script ran and the next time it's scheduled to run. Double-click the task to edit it.

    You can also verify the last time the script ran on the flyout page of the corresponding connector in the Microsoft Purview portal.

## (Optional) Step 7: Upload data using Power Automate templates

You can upload the CSV data by using Power Automate templates and define triggers. For example, you can configure a Power Automate template to trigger when new connector files are available in SharePoint or OneDrive locations. You can also streamline this process by storing confidential information like the Microsoft Entra application secret (created in Step 1) in Azure Key Vault and use it with Power Automate for authentication.

Complete the following steps to automatically upload data when new files become available on OneDrive for Business:

1. Download the *ImportHRDataforIRM.zip* package from the [GitHub site](https://github.com/microsoft/m365-compliance-connector-sample-scripts/blob/main/ImportHRDataforIRM.zip).
2. In [Power Automate](https://make.preview.powerautomate.com), go to **My flows**.
3. Select **Import** and upload the *ImportHRDataforIRM.zip* package.
4. After the package is uploaded, update the content (name and OneDrive for Business connection) and select **Import**.
5. Select **Open flow** and update the parameters. The following table describes the parameters to use in this Power Automate flow and their required values. The information you obtained in the previous steps is used in the values for these parameters.

| **Parameter** | **Description** |
| --- | --- |
| `appId` | This is the Microsoft Entra application ID for the app that you created in Microsoft Entra ID in Step 1. This value is used by Microsoft Entra ID for authentication when the script attempts to access your Microsoft 365 organization. |
| `appSecret` | This is the Microsoft Entra application secret for the app that you created in Microsoft Entra ID in Step 1. This secret is used for authentication. |
| `fileLocation` | This is the OneDrive for Business location where Power Automate monitors for 'new file created' activities to trigger this flow. |
| `jobId` | Identifier for the connector created in Step 3. This identifier associates the data uploaded to the Microsoft cloud with the connector. |
| `tenantId` | Identifier for your Microsoft 365 organization obtained in Step 1. You can also obtain the tenant ID for your organization on the **Overview** blade in the Microsoft Entra admin center. Microsoft uses this tenant ID to identify your organization. |
| `URI` | Verify that the value for this parameter is *https://webhook.ingestion.office.com/api/signals* |

1. Select **Save**.
2. Go to **Flow overview** and select **Turn on**.
3. Test the flow manually by uploading a new file to your OneDrive for Business folder and verify that it runs successfully. This process might take a few minutes after the upload before the flow is triggered.
4. You can now monitor the connector as described in Step 5.

If needed, you can update the flow to create triggers based on file availability and modification events on SharePoint and other data sources supported by Power Automate flows.