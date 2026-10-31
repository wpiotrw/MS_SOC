---
layout: Conceptual
title: Set up a connector to import HR data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/import-hr-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Administrators can set up a data connector to import user data from their organization's human resources (HR) system to insider risk management policies.
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
ai-usage: ai-assisted
locale: en-us
document_id: 4da4c960-55af-42d4-b59a-c7c87dc0f57f
document_version_independent_id: 4da4c960-55af-42d4-b59a-c7c87dc0f57f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/import-hr-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: import-hr-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/import-hr-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 8f5bea59-33ac-caac-c631-7bfca3e3be73
---

# Set up a connector to import HR data | Microsoft Learn

You can set up a data connector to import human resources (HR) data related to events such as a user's resignation or a change in a user's job level. The insider risk management solution uses the HR data to generate risk indicators that help you identify possible malicious activity or data theft by users inside your organization.

Setting up a connector for HR data that insider risk management policies use to generate risk indicators involves creating a CSV file that contains the HR data, creating an app in Microsoft Entra for authentication, creating an HR data connector in the [Microsoft Purview portal](purview-portal), and running a script (on a scheduled basis) that ingests the HR data in CSV files to the Microsoft cloud so it's available to the insider risk management solution.

## Before you begin

- Determine which HR scenarios and data to import to Microsoft 365. This determination helps you decide how many CSV files and HR connectors you need to create, and how to generate and structure the CSV files. The insider risk management policies you want to implement determine the HR data you import. For more information, see Step 1.
- Determine how to retrieve or export the data from your organization's HR system (regularly) and add it to the CSV files that you create in Step 1. The script that you run in Step 4 uploads the HR data in the CSV files to the Microsoft cloud.
- Assign the Data Connector Admin role to the user who creates the HR connector in Step 3. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).
- Understand that the sample script you run in Step 4 uploads your HR data to the Microsoft cloud so that the insider risk management solution can use it. This sample script isn't supported under any Microsoft standard support program or service. The sample script is provided AS IS without warranty of any kind. Microsoft further disclaims all implied warranties including, without limitation, any implied warranties of merchantability or of fitness for a particular purpose. You assume all risk arising from the use or performance of the sample script and documentation. In no event shall Microsoft, its authors, or anyone else involved in the creation, production, or delivery of the scripts be liable for any damages whatsoever (including, without limitation, damages for loss of business profits, business interruption, loss of business information, or other pecuniary loss) arising out of the use of or inability to use the sample scripts or documentation, even if Microsoft has been advised of the possibility of such damages.
- This data connector is available in GCC environments in the Microsoft 365 US Government cloud. Third-party applications and services might involve storing, transmitting, and processing your organization's customer data on third-party systems that are outside of the Microsoft 365 infrastructure and therefore aren't covered by the Microsoft Purview and data protection commitments. Microsoft makes no representation that use of this product to connect to third-party applications implies that those third-party applications are FedRAMP compliant. For step-by-step instructions for setting up an HR connector in a GCC environment, see [Set up a connector to import HR data in US Government](import-hr-data-us-government).
- Add the *webhook.ingestion.office.com* domain to your firewall allowlist for your organization.

## Step 1: Prepare a CSV file with your HR data

First, create a CSV file that contains the HR data the connector imports to Microsoft 365. The insider risk solution uses this data to generate potential risk indicators. You can import data for the following HR scenarios to Microsoft 365:

- Employee resignation. Information about employees who leave your organization.
- Job level changes. Information about job level changes for employees, such as promotions and demotions.
- Performance reviews. Information about employee performance.
- Performance improvement plans. Information about performance improvement plans for employees.
- Employee profile (preview). General information about an employee.

The type of HR data to import depends on the insider risk management policy and corresponding policy template you want to implement. The following table shows which HR data type each policy template requires:

| Policy template | HR data type |
| --- | --- |
| Data theft by departing users | Employee resignations |
| Data leaks | Not applicable |
| Data leaks by priority users | Not applicable |
| Data leaks by risky users | Job level changes, Performance reviews, Performance improvement plans |
| Security policy violations | Not applicable |
| Security policy violations by departing users | Employee resignations |
| Security policy violations by priority users | Not applicable |
| Security policy violations by risky users | Job level changes, Performance reviews, Performance improvement plans |
| Offensive language in email | Not applicable |
| Healthcare policy | Employee profile |
|  |  |

For more information about policy templates for insider risk management, see [Insider risk management policies](insider-risk-management-policy-templates#policy-templates).

For each HR scenario, provide the corresponding HR data in one or more CSV files. The number of CSV files to use for your insider risk management implementation is discussed later in this section.

After you create the CSV file with the required HR data, store it on the local computer where you run the script in Step 4. Implement an update strategy to make sure the CSV file always contains the most current information so that whatever you run the script, the most current HR data is uploaded to the Microsoft cloud and accessible to the insider risk management solution.

Important

The column names described in the following sections aren't required parameters, but only examples. You can use any column name in your CSV files. However, you *must* map the column names you use in a CSV file to the data type when you create the HR connector in Step 3. Also note that the sample CSV files in the following sections are shown in NotePad view. It's much easier to view and edit CSV files in Microsoft Excel. The following sections describe the required CSV data for each HR scenario.

### CSV file for employee resignation data

Here's an example of a CSV file for employee resignation data.

```text
UserPrincipalName,ResignationDate,LastWorkingDate
sarad@contoso.com,2019-04-23T15:18:02.4675041+05:30,2019-04-29T15:18:02.4675041+05:30
pilarp@contoso.com,2019-04-24T09:15:49Z,2019-04-29T15:18:02.7117540
```

The following table describes each column in the CSV file for employee resignation data.

| Column | Description |
| --- | --- |
| **UserPrincipalName** | The Microsoft Entra UserPrincipalName (UPN) used to identify the terminated user. |
| **ResignationDate** | Specifies the date the user's employment is officially terminated or the user resigns from your organization. For example, this date might be when the user gives their notice about leaving your organization. This date might be different from the date of the person's last day of work. Use the following date format: `yyyy-mm-ddThh:mm:ss.nnnnnn| -hh:mm`, which is the [ISO 8601 date and time format](https://www.iso.org/iso-8601-date-and-time-format.html). |
| **LastWorkingDate** | Specifies the last day of work for the terminated user. This date can't be more than six months prior or one year in advance from the time of upload. Use the following date format: `yyyy-mm-ddThh:mm:ss.nnnnnn| -hh:mm`, which is the [ISO 8601 date and time format](https://www.iso.org/iso-8601-date-and-time-format.html). |
|  |  |

### CSV file for job level changes data

Here's an example of a CSV file for job level changes data.

```text
UserPrincipalName,EffectiveDate,OldLevel,NewLevel
sarad@contoso.com,2019-04-23T15:18:02.4675041+05:30,Level 61 - Sr. Manager,Level 60- Manager
pillar@contoso.com,2019-04-23T15:18:02.4675041+05:30,Level 62 - Director,Level 60- Sr. Manager
```

The following table describes each column in the CSV file for job level changes data.

| Column | Description |
| --- | --- |
| **UserPrincipalName** | The Microsoft Entra UserPrincipalName (UPN) used to specify the user's email address. |
| **EffectiveDate** | Specifies the date that the user's job level is officially changed. Use the following date format: `yyyy-mm-ddThh:mm:ss.nnnnnn+ | -hh:mm`, which is the [ISO 8601 date and time format](https://www.iso.org/iso-8601-date-and-time-format.html). |
| **Remarks** | Specifies the remarks that evaluator provides about the change of job level. You can enter a limit of 200 characters. This parameter is optional. You don't have to include it in the CSV file. |
| **OldLevel** | Specifies the user's job level before it was changed. This is a free-text parameter and can contain hierarchical taxonomy for your organization. This parameter is optional. You don't have to include it in the CSV file. |
| **NewLevel** | Specifies the user's job level after it was changed. This is a free-text parameter and can contain hierarchical taxonomy for your organization. This parameter is optional. You don't have to include it in the CSV file. |
|  |  |

### CSV file for performance review data

Here's an example of a CSV file for performance data.

```text
UserPrincipalName,EffectiveDate,Remarks,Rating
sarad@contoso.com,2019-04-23T15:18:02.4675041+05:30,Met expectations but bad attitude,2-Below expectation
pillar@contoso.com,2019-04-23T15:18:02.4675041+05:30, Multiple conflicts with the team
```

The following table describes each column in the CSV file for performance review data.

| Column | Description |
| --- | --- |
| **UserPrincipalName** | The Microsoft Entra UserPrincipalName (UPN) used to specify the user's email address. |
| **EffectiveDate** | Specifies the date that the user is officially informed about the result of their performance review. This date can be the date when the performance review cycle ends. Use the following date format: `yyyy-mm-ddThh:mm:ss.nnnnnn+ | -hh:mm`, which is the [ISO 8601 date and time format](https://www.iso.org/iso-8601-date-and-time-format.html). |
| **Remarks** | Specifies any remarks that evaluator provides to the user for the performance review. This is a text parameter with a limit of 200 characters. This parameter is optional. You don't have to include it in the CSV file. |
| **Rating** | Specifies the rating provided for the performance review. This is a text parameter and can contain any free-form text that your organization uses to recognize the evaluation. For example, "3 Met expectations" or "2 Below average". This is a text parameter with a limit of 25 characters. This parameter is optional. You don't have to include it in the CSV file. |
|  |  |

### CSV file for performance improvement plan data

Here's an example of a CSV file for the data for the performance improvement plan data.

```text
UserPrincipalName,EffectiveDate,ImprovementRemarks,PerformanceRating
sarad@contoso.com,2019-04-23T15:18:02.4675041+05:30,Met expectation but bad attitude,2-Below expectation
pillar@contoso.com,2019-04-23T15:18:02.4675041+05:30, Multiple conflicts with the team
```

The following table describes each column in the CSV file for performance review data.

| Column | Description |
| --- | --- |
| **UserPrincipalName** | The Microsoft Entra UserPrincipalName (UPN) used to specify the user's email address. |
| **EffectiveDate** | Specifies the date when the user is officially informed about their performance improvement plan. You must use the following date format: `yyyy-mm-ddThh:mm:ss.nnnnnn+ | -hh:mm`, which is the [ISO 8601 date and time format](https://www.iso.org/iso-8601-date-and-time-format.html). |
| **Remarks** | Specifies any remarks that evaluator provides about the performance improvement plan. This is a text parameter with a limit of 200 characters. This is an optional parameter. You don't have to include it in the CSV file. |
| **Rating** | Specifies any rating or other information related to the performance review. This is a text parameter and can contain any free form text that your organization uses to recognize the evaluation. For example, "3 Met expectations" or "2 Below average". This is a text parameter with limit of 25 characters. This is an optional parameter. You don't have to include it in the CSV file. |
|  |  |

### CSV file for employee profile data (preview)

Note

The capability to create an HR connector for employee profile data is in public preview. To create an HR connector that supports employee profile data, go to the **Data connectors** page in the Microsoft Purview portal, select the **Connectors** tab, then select **Add a connector** &gt; **HR**. Follow the steps to create a connector in Step 3: Create the HR connector.

Here's an example of a CSV file for employee profile data.

```text
UserPrincipalName,UserName,EmployeeFirstName,EmployeeLastName,EmployeeAddLine1,EmployeeAddLine2,EmployeeCity,EmployeeState,EmployeeZipCode,EmployeeDept,EmployeeType,EmployeeRole
jackq@contoso.com,jackq,jack,qualtz,50 Oakland Ave,#206,City,Florida,32104,Orthopaedic,Regular,Nurse
```

The following table describes each column in the CSV file for employee profile data.

| Column | Description |
| --- | --- |
| UserPrincipalName^\*^ | The Microsoft Entra UserPrincipalName (UPN) used to specify the user's email address. |
| EmployeeFirstName^\*^ | First name of the employee. |
| EmployeeLastName^\*^ | Last name of the employee. |
| EmployeeAddressLine1^\*^ | Street address of the employee. |
| EmployeeAddressLine2 | Secondary address information, such as apartment number, for employee. |
| EmployeeCity | City of residence for employee. |
| EmployeeState | State of residence for employee. |
| EmployeeZipCode^\*^ | Zip code of residence for employee. |
| EmployeeCountry | Country of residence for employee. |
| EmployeeDepartment | Employee's department in the organization. |
| EmployeeType | Employment type for employee, such as Regular, Exempt, or Contractor. |
| EmployeeRole | Employees's role, designation, or job title in the organization. |
|  |  |

Note

^\*^ This column is mandatory. If a mandatory column is missing, the CSV file isn't validated and other data in the file isn't imported.

Create an HR connector that only imports employee profile data. For this connector, frequently refresh the employee profile data, preferably every 15 to 20 days. Employee profile records are deleted if you don't update them in the past 30 days.

### Determining how many CSV files to use for HR data

In Step 3, you can choose to create separate connectors for each HR data type or a single connector for all data types. You can use separate CSV files that contain data for one HR scenario (like the examples of the CSV files described in the previous sections). Alternatively, you can use a single CSV file that contains data for two or more HR scenarios. Here are some guidelines to help you determine how many CSV files to use for HR data.

- If the insider risk management policy that you want to implement requires multiple HR data types, consider using a single CSV file that contains all the required data types.
- The method for generating or collecting the HR data might determine the number of CSV files. For example, if the different types of HR data used to configure an HR connector are located in a single HR system in your organization, then you might be able to export the data to a single CSV file. But if data is distributed across different HR systems, then it might be easier to export data to different CSV files. For example, employee resignation data might be located in a different HR system than job level or performance review data. In this case, it might be easier to have separate CSV files rather than having to manually combine the data into a single CSV file. So, how you retrieve or export data from your HR systems might determine how many CSV files you need.
- As a general rule, the data types in a CSV file determine the number of HR connectors that you need to create. For example, if a CSV file contains all the data types required to support your insider risk management implementation, then you only need one HR connector. But if you have two separate CSV files that each contain a single data type, then you have to create two HR connectors. An exception to this rule is that if you add an **HRScenario** column to a CSV file (see the next section), you can configure a single HR connector that can process different CSV files.
- For each CSV file, you can ingest up to 500 records at once. To ingest a larger number of records, upload multiple CSV files, each with fewer than 500 records.

### Configure a single CSV file for multiple HR data types

You can add multiple HR data types to a single CSV file. This configuration is useful if the insider risk management solution you're implementing requires multiple HR data types or if the data types are located in a single HR system in your organization. Having fewer CSV files always allows you to have fewer HR connectors to create and manage.

Here are requirements for configuring a CSV file with multiple data types:

- Add the required columns (and optional columns if you use them) for each data type and the corresponding column name in the header row. If a data type doesn't correspond to a column, leave the value blank.
- Add an **HRScenario** column to the CSV file. The HR connector uses this column to identify which rows in the CSV file contain which type HR data. The values in this column identify the type of HR data in each row. For example, values that correspond to the HR scenarios could be `Resignation`, `Job level change`, `Performance review`, `Performance improvement plan`, and `Employee profile`.
- If you have multiple CSV files that contain an **HRScenario** column, make sure that each file uses the same column name and the same values that identify the specific HR scenarios.

The following example shows a CSV file that contains the **HRScenario** column. The values in the HRScenario column identify the type of data in the corresponding row. The following sample covers four HR scenarios `Resignation`, `Job level change`, `Performance review`, and `Performance improvement plan`.

```text
HRScenario,EmailAddress,ResignationDate,LastWorkingDate,EffectiveDate,Remarks,Rating,OldLevel,NewLevel
Resignation,sarad@contoso.com,2019-04-23T15:18:02.4675041+05:30,2019-04-29T15:18:02.4675041+05:30,,,,
Resignation,pilarp@contoso.com,2019-04-24T09:15:49Z,2019-04-29T15:18:02.7117540,,,,
Job level change,sarad@contoso.com,2019-04-23T15:18:02.4675041+05:30,,,,,Level 61 Sr. Manager, Level 60 Manager
Job level change,pillarp@contoso.com,2019-04-23T15:18:02.4675041+05:30,,,,,Level 62 Director,Level 60 Sr Manager
Performance review,sarad@contoso.com,,,2019-04-23T15:18:02.4675041+05:30,Met expectation but bad attitude,2 Below expectations,,
Performance review,pillarp@contoso.com,,,2019-04-23T15:18:02.4675041+05:30, Multiple conflicts with the team,,
Performance improvement plan,sarad@contoso.com,,,2019-04-23T15:18:02.4675041+05:30,Met expectations but bad attitude,2 Below expectations,,
Performance improvement plan,pillarp@contoso.com,,,2019-04-23T15:18:02.4675041+05:30,Multiple conflicts with the team,,
```

Note

You can use any name for the column that identifies HR data type because you map the name of the column in your CSV file as the column that identifies the HR data type when you set up the connector in Step 3. You also map the values used for the data type column when you set up the connector.

### Add the HRScenario column to a CSV file that contains a single data type

Based on your organization's HR systems and how you export HR data to a CSV file, you might need to create multiple CSV files that each contain a single HR data type. In this case, you can still create a single HR connector to import data from different CSV files. To do this, add an HRScenario column to the CSV file and specify the HR data type. Then, you can run the script for each CSV file but use the same job ID for the connector. For more information, see Step 4.

## Step 2: Create an app in Microsoft Entra ID

Next, create and register a new app in Microsoft Entra ID. The app corresponds to the HR connector that you create in Step 3. When you create this app, Microsoft Entra ID can authenticate the HR connector when it runs and attempts to access your organization. This app also authenticates the script that you run in Step 4 to upload your HR data to the Microsoft cloud. During the creation of this Microsoft Entra app, save the following information. You use these values in Step 3 and Step 4.

- Microsoft Entra application ID (also called the *app ID* or *client ID*)
- Microsoft Entra application secret (also called the *client secret*)
- Tenant ID (also called the *directory Id*)

For step-by-step instructions for creating an app in Microsoft Entra ID, see [Register an application with the Microsoft identity platform](/en-us/azure/active-directory/develop/quickstart-register-app?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

## Step 3: Create the HR connector

The next step is to create an HR connector in the Microsoft Purview portal. After you run the script in Step 4, the HR connector that you create will ingest the HR data from the CSV file to your Microsoft 365 organization. Before you create a connector, be sure that you have a list of the HR scenarios and the corresponding CSV column names for each one. You have to map the data required for each scenario to the actual column names in your CSV file when configuring the connector. Alternatively, you can upload a sample CSV file when configuring the connector and the workflow help you map the name of the columns to the required data types.

After you complete this step, be sure to copy the job ID that's generated when you create the connector. You use the job ID when you run the script.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. From the list, select **HR (preview)**.
5. On the **Setup the connection** page, do the following and then select **Next**:

    1. Type or paste the Microsoft Entra application ID for the Azure app that you created in Step 2.
    2. Type a name for the HR connector.
6. On the HR scenarios page, select one or more HR scenarios that you want to import data for and then select **Next**.

    ![Select one or more HR scenarios.](media/hrconnectorscenarios.png)
7. On the file mapping method page, select a file type if necessary, and then select one of the following options and then select **Next**.

    - **Upload a sample file**. If you select this option, select **Upload sample file** to upload the CSV file that you prepared in Step 1. This option allows you to quickly select column names in your CSV file from a drop-down list to map them to the data types for the HR scenarios that you previously selected.

    OR

    - **Manually provide the mapping details**. If you select this option, you have to type the name of the columns in your CSV file to map them to the data types for the HR scenarios that you previously selected.
8. On the File mapping details page, do one of the following, depending on whether you uploaded a sample CSV file and whether you're configuring the connector for a single HR scenario or for multiple scenarios. If you uploaded a sample file, you don't have to type the column names. You pick them from a dropdown list.

    - If you selected a single HR scenario in the previous step, then type the column header names (also called *parameters*) from the CSV file that you created in Step 1 in each of the appropriate boxes. The column names that you type aren't case-sensitive, but be sure to include spaces if the column names in your CSV file include spaces. As previously explained, the names you type in these boxes must match the parameter names in your CSV file. For example, the following screenshot shows the parameter names from the sample CSV file for the employee resignation HR scenario shown in Step 1.
    - If you selected multiple data types in the previous step, then you need to enter identifier column name that will identify the HR data type in your CSV file. After entering the identifier column name, type the value that identifies this HR data type, and type the column header names for selected data types from the CSV file(s) that you created in Step 1 in each of the appropriate boxes for each selected data type. As previously explained, the names that you type in these boxes must match the column names in your CSV file.
9. On the **Review** page, review your settings and then select **Finish** to create the connector.

    A status page is displayed that confirms the connector was created. This page contains two important things that you need to complete the next step to run the sample script to upload your HR data.

    ![Review page with job ID and link to github for sample script.](media/hrconnector_confirmation.png)

    1. **Job ID.** You'll need this job ID to run the script in the next step. You can copy it from this page or from the connector flyout page.
    2. **Link to sample script.** Select the **here** link to go to the GitHub site to access the sample script (the link opens a new window). Keep this window open so that you can copy the script in Step 4. Alternatively, you can bookmark the destination or copy the URL so you can access it again when you run the script. This link is also available on the connector flyout page.
10. Select **Done**.

    The new connector is displayed in the list on the **Connectors** tab.
11. Select the HR connector that you just created to display the flyout page, which contains properties and other information about the connector.

    ![Flyout page for new HR connector.](media/hrconnectorwizard7.png)

If you haven't already done so, you can copy the values for the **Azure App ID** and **Connector job ID**. You'll need these to run the script in the next step. You can also download the script from the flyout page (or download it using the link in the next step.)

You can also select **Edit** to change the Azure App ID or the column header names that you defined on the **File mapping** page.

## Step 4: Run the sample script to upload your HR data

Important

You must add the *webhook.ingestion.office.com* domain to your firewall allowlist for your organization. If you block this domain, the script doesn't run.

The last step in setting up an HR connector is to run a sample script that uploads the HR data in the CSV file (that you created in Step 1) to the Microsoft cloud. Specifically, the script uploads the data to the HR connector. After you run the script, the HR connector that you created in Step 3 imports the HR data to your Microsoft 365 organization where other compliance tools, such as the Insider risk management solution, can access it. After you run the script, consider scheduling a task to run it automatically on a daily basis so the most current employee termination data is uploaded to the Microsoft cloud. For more information, see Schedule the script to run automatically.

1. Go to the window that you left open from the previous step to access the GitHub site with the sample script. Alternatively, open the bookmarked site or use the URL that you copied. You can also access the script [here](https://github.com/microsoft/m365-compliance-connector-sample-scripts/blob/main/sample_script.ps1).
2. Select the **Raw** button to display the script in text view.
3. Copy all the lines in the sample script and save them to a text file.
4. Modify the sample script for your organization, if necessary.
5. Save the text file as a Windows PowerShell script file by using a filename suffix of `.ps1`; for example, `HRConnector.ps1`. Alternatively, you can use the GitHub filename for the script, which is `upload_termination_records.ps1`.
6. Open a command prompt on your local computer, and go to the directory where you saved the script.
7. Run the following command to upload the HR data in the CSV file to the Microsoft cloud; for example:

    ```powershell
    .\HRConnector.ps1 -tenantId <tenantId> -appId <appId>  -appSecret <appSecret>  -jobId <jobId>  -filePath '<filePath>'
    ```

    The following table describes the parameters to use with this script and their required values. The information you obtained in the previous steps is used in the values for these parameters.

    | Parameter | Description |
    | --- | --- |
    | `tenantId` | This is the ID for your Microsoft 365 organization that you obtained in Step 2. You can also obtain the tenant ID for your organization on the **Overview** blade in the Microsoft Entra admin center. This value identifies your organization. |
    | `appId` | This is the Microsoft Entra application ID for the app that you created in Microsoft Entra ID in Step 2. This value is used by Microsoft Entra ID for authentication when the script attempts to access your Microsoft 365 organization. |
    | `appSecret` | This is the Microsoft Entra application secret for the app that you created in Microsoft Entra ID in Step 2. This value is also used for authentication. |
    | `jobId` | This is the job ID for the HR connector that you created in Step 3. This value associates the HR data that is uploaded to the Microsoft cloud with the HR connector. |
    | `filePath` | This is the file path for the file (stored on the same system as the script) that you created in Step 1. Try to avoid spaces in the file path; otherwise use single quotation marks. |
    |  |  |

    Here's an example of the syntax for the HR connector script using actual values for each parameter:

    ```powershell
    .\HRConnector.ps1 -tenantId aaaabbbb-0000-cccc-1111-dddd2222eeee -appId 00001111-aaaa-2222-bbbb-3333cccc4444 -appSecret Aa1Bb~2Cc3.-Dd4Ee5Ff6Gg7Hh8Ii9_Jj0Kk1Ll2 -jobId 00001111-aaaa-2222-bbbb-3333cccc4444 -filePath 'C:\Users\contosoadmin\Desktop\Data\employee_termination_data.csv'
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

    The `RecordsSaved` field indicates the number of rows in the CSV file that you uploaded. For example, if the CSV file contains four rows, the value of the `RecordsSaved` fields is 4, if the script successfully uploads all the rows in the CSV file.

If you didn't run the script in Step 4, a link to download the script is displayed under **Last import**. You can download the script and then follow the steps to run the script.

## (Optional) Step 6: Schedule the script to run automatically

To make sure tools like the insider risk management solution always have access to the latest HR data from your organization, schedule the script to run automatically on a recurring basis, such as once a day. This schedule requires updating the HR data in the CSV file on a similar (if not the same) schedule so that it contains the latest information about employees who leave your organization. The goal is to upload the most current HR data so that the HR connector can make it available to the insider risk management solution.

Use the Task Scheduler app in Windows to automatically run the script every day.

1. On your local computer, select the Windows **Start** button and then type **Task Scheduler**.
2. Select the **Task Scheduler** app to open it.
3. In the **Actions** section, select **Create Task**.
4. On the **General** tab, type a descriptive name for the scheduled task, such as **HR Connector Script**. You can also add an optional description.
5. Under **Security options**, complete the following steps:

    1. Decide whether to run the script only when you're logged on to the computer or run it when you're logged on or not.
    2. Make sure that the **Run with the highest privileges** checkbox is selected.
6. Select the **Triggers** tab, select **New**, and then complete the following steps:

    1. Under **Settings**, select the **Daily** option, then select a date and time to run the script for the first time. The script runs every day at the same specified time.
    2. Under **Advanced settings**, make sure the **Enabled** checkbox is selected.
    3. Select **Ok**.
7. Select the **Actions** tab, select **New**, and then complete the following steps:

    ![Action settings to create a new scheduled task for the HR connector script.](media/hrconnectorscheduletask1.png)

    1. In the **Action** dropdown list, make sure that **Start a program** is selected.
    2. In the **Program/script** box, select **Browse**, go to the following location, and select it so the path displays in the box: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`.
    3. In the **Add arguments (optional)** box, paste the same script command that you ran in Step 4. For example, `.\HRConnector.ps1 -tenantId "aaaabbbb-0000-cccc-1111-dddd2222eeee" -appId "00001111-aaaa-2222-bbbb-3333cccc4444" -appSecret "Aa1Bb~2Cc3.-Dd4Ee5Ff6Gg7Hh8Ii9_Jj0Kk1Ll2"  -jobId "00001111-aaaa-2222-bbbb-3333cccc4444" -filePath "C:\Users\contosoadmin\Desktop\Data\employee_termination_data.csv"`
    4. In the **Start in (optional)** box, paste the folder location of the script that you ran in Step 4. For example, `C:\Users\contosoadmin\Desktop\Scripts`.
    5. Select **Ok** to save the settings for the new action.
8. In the **Create Task** window, select **Ok** to save the scheduled task. You might be prompted to enter your user account credentials.

    The new task appears in the Task Scheduler Library.

    ![The new task is displayed in the Task Scheduler Library.](media/hrconnectortaskschedulerlibrary.png)

    The last time the script ran and the next time it's scheduled to run displays. You can double-select the task to edit it.

    You can also verify the last time the script ran on the flyout page of the corresponding HR connector in the Microsoft Purview portal.

## (Optional) Step 7: Upload data by using Power Automate templates

You can upload HR data by using Power Automate templates and define triggers. For example, you can configure a Power Automate template to trigger when new HR connector files are available in SharePoint or OneDrive locations. You can also streamline this process by storing confidential information like Microsoft Entra application secret (created in **Step 2**) in Azure Key Vault and use it with Power Automate for authentication.

Complete the following steps to automatically upload HR data when new files become available on OneDrive for Business:

1. Download the *ImportHRDataforIRM.zip* package from the [GitHub site](https://github.com/microsoft/m365-compliance-connector-sample-scripts/blob/main/ImportHRDataforIRM.zip).
2. In [Power Automate](https://make.preview.powerautomate.com), go to **My flows**.
3. Select **Import** and upload the *ImportHRDataforIRM.zip* package.
4. After the package is uploaded, update the content (name and OneDrive for Business connection), and select **Import**.

    ![Power Automate flow import.](media/hr-connector-pa-import-flow.png)
5. Select **Open flow** and update the parameters. The following table describes the parameters to use in this Power Automate Flow and their required values. Use the information you obtained in the previous steps for these values.

| **Parameter** | **Description** |
| --- | --- |
| App ID | This is the Microsoft Entra application ID for the app that you created in Microsoft Entra ID in **Step 2**. Microsoft Entra ID uses this application ID for authentication when the script attempts to access your Microsoft 365 organization. |
| App Secret | This is the Microsoft Entra application secret for the app that you created in Microsoft Entra ID in **Step 2**. This application secret is used for authentication. |
| File location | This is the OneDrive for Business location where Power Automate monitors for 'new file created' activities to trigger this flow. |
| Job ID | Identifier for the HR connector created in **Step 3**. This identifier associates the HR data uploaded to the Microsoft cloud with the HR connector. |
| Tenant ID | Identifier for your Microsoft 365 organization obtained in **Step 2**. You can also obtain the tenant ID for your organization on the **Overview** blade in the Microsoft Entra admin center. This identifier is used to identify your organization. |
| URI | Verify that the value for this parameter is *https://webhook.ingestion.office.com/api/signals* |
|  |  |

![Power Automate flow.](media/hr-connector-pa-flow.png)

1. Select **Save**.
2. Go to **Flow overview** and select **Turn on**.

    ![Turn on the Power Automate flow.](media/hr-connector-pa-turn-on.png)
3. Test the flow manually by uploading a new file to your OneDrive for Business folder and verify that it ran successfully. This process might take a few minutes after the upload before the flow is triggered.

    ![Power Automate flow test.](media/hr-connector-pa-test.png)
4. You can now monitor the HR connector as described in **Step 5**.

If needed, you can update the flow to create triggers based on file availability and modification events on SharePoint and other data sources supported by Power Automate Flows.

## Existing HR connectors

On December 13, 2021, Microsoft released the employee profile data scenario for HR connectors. If you created an HR connector before this date, Microsoft migrates the existing instances of your organization's HR connectors so your HR data continues to be imported to the Microsoft cloud. You don't have to do anything to maintain this functionality. You can keep using these connectors without disruption.

If you want to implement the employee profile data scenario, create a new HR connector and configure it as required. After you create a new HR connector, run the script by using the job ID of the new connector and CSV files with employee profile data previously described in this article.