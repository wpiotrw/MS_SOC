---
layout: Conceptual
title: Set up a connector to import HR data to the US Government cloud | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/import-hr-data-us-government
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Administrators in the US Government cloud can set up a data connector to import employee data from their organization's human resources (HR) system to Microsoft 365. This lets you use HR data in insider risk management policies to help you detect activity by specific users that may pose an internal threat to your organization.
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
ms.custom:
- admindeeplinkCOMPLIANCE
- sfi-image-nochange
ROBOTS: NOINDEX, NOFOLLOW
ai-usage: ai-assisted
locale: en-us
document_id: 28e7f0ff-3883-fff7-7dc2-acd0971d7732
document_version_independent_id: 28e7f0ff-3883-fff7-7dc2-acd0971d7732
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/import-hr-data-US-government.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: import-hr-data-us-government
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/import-hr-data-US-government.md
platformId: d37cc9c4-8508-18c5-6f85-affa6ba6b34b
---

# Set up a connector to import HR data to the US Government cloud | Microsoft Learn

You can set up a data connector to import human resources (HR) data to your US Government organization. HR-related data includes the date an employee submitted their resignation and date of the employee's last day. Microsoft information protection solutions, such as the [insider risk management solution](insider-risk-management), use this HR data to help protect your organization from malicious activity or data theft inside your organization. Setting up an HR connector consists of creating an app in Microsoft Entra that's used for authentication by connector, creating a CSV mapping files that contains your HR data, creating a data connector in the Microsoft Purview portal, and then running a script (on a scheduled basis) that ingests the HR data in the CSV file to the Microsoft cloud. Then the data connector is used by the insider risk management tool to access the HR data that you imported to your Microsoft 365 US Government organization.

## Before you begin

- The user who creates the HR connector in Step 3 must be assigned the Data Connector Admin role. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).

    Note

    The Data Connector Admin role currently isn't supported in US Government GCC High and DoD environments. Therefore, the user who creates the HR connector in GCC High and DoD environments must be assigned the Mailbox Import Export role in Exchange Online. By default, no role group in Exchange Online has this role assigned. You can add the Mailbox Import Export role to the Organization Management role group in Exchange Online. Or you can create a new role group, assign the Mailbox Import Export role, and then add the appropriate users as members. For more information, see the [Create role groups](/en-us/Exchange/permissions-exo/role-groups?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#create-role-groups) or [Modify role groups](/en-us/Exchange/permissions-exo/role-groups?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#modify-role-groups) sections in the article "Manage role groups in Exchange Online".
- Determine how to retrieve or export the data from your organization's HR system (on a regular basis) and add it to the CSV file that's described in Step 2. The script that you run in Step 4 uploads the HR data in the CSV file to the Microsoft cloud.
- The sample script that you run in Step 4 uploads HR data to the Microsoft cloud so that other Microsoft tools, such as the insider risk management solution, can use it. This sample script isn't supported under any Microsoft standard support program or service. The sample script is provided AS IS without warranty of any kind. Microsoft further disclaims all implied warranties including, without limitation, any implied warranties of merchantability or of fitness for a particular purpose. You assume all risk arising from the use or performance of the sample script and documentation. In no event shall Microsoft, its authors, or anyone else involved in the creation, production, or delivery of the scripts be liable for any damages whatsoever (including, without limitation, damages for loss of business profits, business interruption, loss of business information, or other pecuniary loss) arising out of the use of or inability to use the sample scripts or documentation, even if Microsoft has been advised of the possibility of such damages.

## Step 1: Create an app in Microsoft Entra ID

First, create and register a new app in Microsoft Entra ID. The app corresponds to the HR connector that you create in Step 3. When you create the app, Microsoft Entra ID can authenticate the HR connector. The app also authenticates the script that you run in Step 4 to upload your HR data to the Microsoft cloud. During the creation of this Microsoft Entra app, save the following information. You use these values in later steps.

- Microsoft Entra application ID (also called the *app Id* or *client Id*)
- Microsoft Entra application secret (also called the *client secret*)
- Tenant Id (also called the *directory Id*)

For step-by-step instructions for creating an app in Microsoft Entra ID, see [Register an application with the Microsoft identity platform](/en-us/azure/active-directory/develop/quickstart-register-app?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

## Step 2: Prepare a CSV file with your HR data

In this step, you create a CSV file that contains information about employees who left your organization. As explained in the Before You Begin section, you need to decide how to generate this CSV file from your organization's HR system. The following example shows a completed CSV file (opened in Note Pad) that contains the three required parameters (columns). It's much easier to edit the CSV file in Microsoft Excel.

```text
EmailAddress,TerminationDate,LastWorkingDate
sarad@contoso.com,2019-04-23T15:18:02.4675041+05:30,2019-04-29T15:18:02.4675041+05:30
pilarp@contoso.com,2019-04-24T09:15:49Z,2019-04-29T15:18:02.7117540
```

The first row, or header row, of the CSV file lists the required column names. You choose the name used in each column header (the ones in the following example are suggestions). However, you must specify the same column names when you create the HR connector in Step 3. Don't include spaces in the column names.

The following table describes each column in the CSV file:

| Column name | Description |
| --- | --- |
| **EmailAddress** | Specifies the email address of the terminated employee. |
| **TerminationDate** | Specifies the date the person's employment was officially terminated in your organization. For example, this date might be when the employee gives their notice about leaving your organization. This date might be different from the date of the person's last day of work. Use the following date format: `yyyy-mm-ddThh:mm:ss.nnnnnn+|-hh:mm`, which is the [ISO 8601 date and time format](https://www.iso.org/iso-8601-date-and-time-format.html). |
| **LastWorkingDate** | Specifies the last day of work for the terminated employee. Use the following date format: `yyyy-mm-ddThh:mm:ss.nnnnnn+|-hh:mm`, which is the [ISO 8601 date and time format](https://www.iso.org/iso-8601-date-and-time-format.html). |
|  |  |

After you create the CSV file with the required HR data, store it on the same system as the script that you run in Step 4. Be sure to implement an update strategy so the CSV file always contains the most current information. This strategy ensures that whatever script you run, the most current employee termination data is uploaded to the Microsoft cloud.

## Step 3: Create the HR connector

In this step, you create an HR connector in the Microsoft Purview portal. When you run the script in Step 4, the HR connector ingests the HR data from the CSV file to your Microsoft 365 organization. Be sure to copy the job ID that's generated when you create the connector. You'll use the job ID when you run the script.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. From the list, select **HR**.
5. On the **Authentication credentials** page, enter the following information and then select **Next**:

    1. Enter or paste the Microsoft Entra application ID for the Azure app that you created in Step 1.
    2. Enter a name for the HR connector.
6. On the **File mapping** page, enter the names of the three column headers (also called *parameters*) from the CSV file that you created in Step 2 in each of the appropriate boxes. The names aren't case-sensitive. As previously explained, the names that you enter in these boxes must match the parameter names in your CSV file. For example, the following screenshot shows the parameter names from the example in sample CSV file shown in Step 2.

    ![Column heading names match the ones in the CSV file.](media/hrconnectorwizard3.png)
7. On the **Review** page, review your settings and then select **Finish** to create the connector.

    A status page is displayed that confirms the connector was created. This page contains two important things that you need to complete the next step to run the sample script to upload your HR data.

    ![Review page with job ID and link to github for sample script.](media/hrconnector_confirmation.png)

    1. **Job ID.** You need this job ID to run the script. You can copy it from this page or from the connector flyout page.
    2. **Link to sample script.** Select the **here** link to go to the GitHub site to access the sample script (the link opens a new window). Keep this window open so that you can copy the script in Step 4. Alternatively, you can bookmark the destination or copy the URL so you can access it again in Step 4. This link is also available on the connector flyout page.
8. Select **Done**.

    The new connector is displayed in the list on the **Connectors** tab.
9. Select the HR connector that you just created to display the flyout page, which contains properties and other information about the connector.

    ![Flyout page for new HR connector.](media/hrconnectorwizard7.png)

    If you didn't already, copy the values for the **Azure App ID** and **Connector job ID**. You need these values to run the script in the next step. You can also download the script from the flyout page (or download it using the link in the next step).

    Select **Edit** to change the Azure App ID or the column header names that you defined on the **File mapping** page.

## Step 4: Run the sample script to upload your HR data

To set up an HR connector, run a sample script that uploads the HR data in the CSV file (created in Step 2) to the Microsoft cloud. The script specifically uploads the data to the HR connector. After you run the script, the HR connector that you created in Step 3 imports the HR data to your Microsoft 365 organization where other compliance tools, such as the Insider risk management solution, can access it. Consider scheduling a task to run the script automatically on a daily basis so the most current employee termination data is uploaded to the Microsoft cloud. For more information, see Schedule the script to run automatically.

1. Go to the window you left open from the previous step to access the GitHub site with the sample script. Alternatively, open the bookmarked site or use the URL that you copied.
2. Select the **Raw** button to display the script in text view.
3. Copy all the lines in the sample script and save them to a text file.
4. Modify the sample script for your organization, if necessary.
5. Save the text file as a Windows PowerShell script file by using a filename suffix of `.ps1`; for example, `HRConnector.ps1`.
6. Open a Command Prompt on your local computer, and go to the directory where you saved the script.
7. Run the following command to upload the HR data in the CSV file to the Microsoft cloud; for example:

    ```powershell
    .\HRConnector.ps1 -tenantId <tenantId> -appId <appId>  -appSecret <appSecret>  -jobId <jobId>  -csvFilePath '<csvFilePath>'
    ```

    The following table describes the parameters to use with this script and their required values. Use the information you obtained in the previous steps for these values.

    | Parameter | Description |
    | --- | --- |
    | `tenantId` | The Id for your Microsoft 365 organization that you obtained in Step 1. You can also get the tenant Id for your organization on the **Overview** blade in the Microsoft Entra admin center. This value identifies your organization. |
    | `appId` | The Microsoft Entra application Id for the app that you created in Microsoft Entra ID in Step 1. Microsoft Entra ID uses this value for authentication when the script attempts to access your Microsoft 365 organization. |
    | `appSecret` | The Microsoft Entra application secret for the app that you created in Microsoft Entra ID in Step 1. This value is also used for authentication. |
    | `jobId` | The job ID for the HR connector that you created in Step 3. This value associates the HR data that you upload to the Microsoft cloud with the HR connector. |
    | `csvFilePath` | The file path for the CSV file (stored on the same system as the script) that you created in Step 2. Try to avoid spaces in the file path; otherwise use single quotation marks. |
    |  |  |

    Here's an example of the syntax for the HR connector script using actual values for each parameter:

    ```powershell
     .\HRConnector.ps1 -tenantId aaaabbbb-0000-cccc-1111-dddd2222eeee -appId 00001111-aaaa-2222-bbbb-3333cccc4444 -appSecret Aa1Bb~2Cc3.-Dd4Ee5Ff6Gg7Hh8Ii9_Jj0Kk1Ll2 -jobId 00001111-aaaa-2222-bbbb-3333cccc4444 -csvFilePath 'C:\Users\contosoadmin\Desktop\Data\employee_termination_data.csv'
    ```

    If the upload is successful, the script displays the **Upload Successful** message.

    Note

    If you have problems running the previous command because of execution policies, see [About Execution Policies](/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) and [Set-ExecutionPolicy](/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) for guidance about setting execution policies.

## Step 5: Monitor the HR connector

After you create the HR connector and run the script to upload your HR data, you can view the connector and upload status in the Microsoft Purview portal. If you schedule the script to run automatically on a regular basis, you can also view the current status after the last time the script ran.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select the HR connector that you created to display the flyout page. This page contains the properties and information about the connector.
4. Under **Progress**, select the **Download log** link to open (or save) the status log for the connector. This log contains information about each time the script runs and uploads the data from the CSV file to the Microsoft cloud.

    ![HR connector log file displays number rows from CSV file that were uploaded.](media/hrconnectorlogfile.png)

    The `RecordsSaved` field indicates the number of rows in the CSV file that uploaded. For example, if the CSV file contains four rows, the value of the `RecordsSaved` fields is 4, if the script successfully uploaded all the rows in the CSV file.

If you didn't run the script in Step 4, a link to download the script is displayed under **Last import**. You can download the script and then follow the steps in Step 4 to run it.

## (Optional) Step 6: Schedule the script to run automatically

To make sure tools like the insider risk management solution always have the latest HR data from your organization, schedule the script to run automatically on a recurring basis, such as once a day. This schedule requires that you update the HR data in the CSV file on a similar (if not the same) schedule so that it contains the latest information about employees who leave your organization. The goal is to upload the most current HR data so that the HR connector can make it available to the insider risk management solution.

Use the Task Scheduler app in Windows to automatically run the script every day.

1. On your local computer, select the Windows **Start** button and then type **Task Scheduler**.
2. Select the **Task Scheduler** app to open it.
3. In the **Actions** section, select **Create Task**.
4. On the **General** tab, type a descriptive name for the scheduled task, such as **HR Connector Script**. You can also add an optional description.
5. Under **Security options**, complete the following steps:

    1. Decide whether to run the script only when you're logged on to the computer or run it when you're logged on or not.
    2. Make sure that the **Run with the highest privileges** checkbox is selected.
6. Select the **Triggers** tab, select **New**, and then complete the following steps:

    1. Under **Settings**, select the **Daily** option, and then select a date and time to run the script for the first time. The script runs every day at the same specified time.
    2. Under **Advanced settings**, make sure the **Enabled** checkbox is selected.
    3. Select **Ok**.
7. Select the **Actions** tab, select **New**, and then complete the following steps:

    ![Action settings to create a new scheduled task for the HR connector script.](media/hrconnectorscheduletask1.png)

    1. In the **Action** dropdown list, make sure that **Start a program** is selected.
    2. In the **Program/script** box, select **Browse**, and go to the following location and select it so the path is displayed in the box: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`.
    3. In the **Add arguments (optional)** box, paste the same script command that you ran in Step 4. For example, `.\HRConnector.ps1 -tenantId "aaaabbbb-0000-cccc-1111-dddd2222eeee" -appId "00001111-aaaa-2222-bbbb-3333cccc4444" -appSecret "Aa1Bb~2Cc3.-Dd4Ee5Ff6Gg7Hh8Ii9_Jj0Kk1Ll2"  -jobId "00001111-aaaa-2222-bbbb-3333cccc4444" -csvFilePath "C:\Users\contosoadmin\Desktop\Data\employee_termination_data.csv"`
    4. In the **Start in (optional)** box, paste the folder location of the script that you ran in Step 4. For example, `C:\Users\contosoadmin\Desktop\Scripts`.
    5. Select **Ok** to save the settings for the new action.
8. In the **Create Task** window, select **Ok** to save the scheduled task. You might be prompted to enter your user account credentials.

    The new task is displayed in the Task Scheduler Library.

    ![The new task is displayed in the Task Scheduler Library.](media/hrconnectortaskschedulerlibrary.png)

    The last time the script ran and the next time it's scheduled to run is displayed. You can double-select the task to edit it.

    You can also verify the last time the script ran on the flyout page of the corresponding HR connector in the Microsoft Purview portal.