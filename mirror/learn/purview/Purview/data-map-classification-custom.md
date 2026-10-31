---
layout: Conceptual
title: Custom classifications in Microsoft Purview Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-classification-custom
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: pragyarathi
ms.date: 2024-05-16T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to create custom classifications to define data types in your data estate that are unique to your organization in Microsoft Purview Data Map.
ms.custom: sfi-image-nochange
locale: en-us
document_id: 669eda81-d750-5048-6bb3-88dac254fd9f
document_version_independent_id: 669eda81-d750-5048-6bb3-88dac254fd9f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-classification-custom.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-classification-custom
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-classification-custom.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: 5840c928-f45a-423f-82e2-6c42b0145365
---

# Custom classifications in Microsoft Purview Data Map | Microsoft Learn

This article describes how you can create custom classifications in Microsoft Purview Data Map to define data types in your data estate that are unique to your organization. It also describes the creation of custom classification rules that let you find specified data throughout your data estate.

Important

To create a custom classification you need either **data curator** or **data source administrator**[permission on a domain or collection](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections). Permissions at any collection level are sufficient.

## Default system classifications

Data Map provides a large set of default system classifications that represent typical personal data types that you might have in your data estate. See the [list of available system classifications in Data Map](data-map-classification-supported-list).

![select classification](media/create-a-custom-classification-and-classification-rule/classification.png)

You also have the ability to create custom classifications, if any of the default classifications don't meet your needs.

Note

- Our [data sampling rules](data-map-data-sources#sampling-data-for-classification) are applied to both system and custom classifications.
- Custom classifications are only applied to structured data sources like SQL and CosmosDB, and to structured file types like CSV, JSON, and Parquet. Custom classification isn't applied to unstructured data file types like DOC, PDF, and XLSX.

## Steps to create a custom classification

To create a custom classification, follow these steps:

1. You'll need [**data curator** or **data source administrator** permissions on any collection](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections) to be able to create a custom classification.
2. In the Microsoft Purview portal, open the **Data map** solution.
3. Select **Annotation management** select **Classifications**.
4. Select **+ New**.

    ![New classification](media/create-a-custom-classification-and-classification-rule/new-classification.png)

The **Add new classification** pane opens, where you can give your classification a name and a description. It's good practice to use a name-spacing convention, such as `your company name.classification name`.

The Microsoft system classifications are grouped under the reserved `MICROSOFT.` namespace. An example is **MICROSOFT.GOVERNMENT.US.SOCIAL\_SECURITY\_NUMBER**.

The name of your classification must start with a letter followed by a sequence of letters, numbers, and period (.) or underscore characters. As you type, the UX automatically generates a friendly name. This friendly name is what users see when you apply it to an asset in the catalog.

To keep the name short, the system creates the friendly name based on the following logic:

- All but the last two segments of the namespace are trimmed.
- The casing is adjusted so that the first letter of each word is capitalized.
- All underscores (\_) are replaced with spaces.

As an example, if you named your classification **contoso.hr.employee\_ID**, the friendly name is stored in the system as **Hr.Employee ID**.

![Contoso.hr.employee_id](media/create-a-custom-classification-and-classification-rule/contoso-hr-employee-id.png)

Select **OK**, and your new classification is added to your **Custom** classification list.

![Custom classification](media/create-a-custom-classification-and-classification-rule/custom-classification.png)

Selecting the classification in the list opens the classification details page. Here, you find all the details about the classification.

These details include the count of how many instances there are, the formal name, associated classification rules (if any), and the owner name.

![Select classification](media/create-a-custom-classification-and-classification-rule/select-classification.png)

## Custom classification rules

The data map provides a set of default classification rules that are used by the scanner to automatically detect certain data types. You can also add your own custom classification rules to detect other types of data that you might be interested in finding across your data estate. This capability can be powerful when you're trying to find data within your data estate.

Note

Custom classification rules are only supported in the English language.

As an example, let's say that a company named Contoso has employee IDs that are standardized throughout the company with the word "Employee" followed by a GUID to create EMPLOYEE{GUID}. For example, one instance of an employee ID looks like `EMPLOYEE9c55c474-9996-420c-a285-0d0fc23f1f55`.

Contoso can configure the scanning system to find instances of these IDs by creating a custom classification rule. They can supply a regular expression that matches the data pattern, in this case, `\^Employee\[A-Za-z0-9\]{8}-\[A-Za-z0-9\]{4}-\[A-Za-z0-9\]{4}-\[A-Za-z0-9\]{4}-\[A-Za-z0-9\]{12}\$`. Optionally, if the data usually is in a column that they know the name of, such as Employee\_ID or EmployeeID, they can add a column pattern regular expression to make the scan even more accurate. An example regex is Employee\_ID|EmployeeID.

The scanning system can then use this rule to examine the actual data in the column and the column name to try to identify every instance of where the employee ID pattern is found.

## Steps to create a custom classification rule

Create a custom classification that following the instructions in the previous section. You'll add this custom classification in the classification rule configuration so that the system applies it when it finds a match in the column.

1. In the Microsoft Purview portal, open the **Data map** solution.
2. Under **Annotation management**, select the **Classifications rules** section.
3. Select **New**.

    ![Add new classification rule](media/create-a-custom-classification-and-classification-rule/new-classification-rule.png)
4. The **New classification rule** dialog box opens. Fill in the fields and decide whether to create a **regular expression rule** or a **dictionary rule**.

    | Field | Description |
    | --- | --- |
    | Name | Required. The maximum is 100 characters. |
    | Description | Optional. The maximum is 256 characters. |
    | Classification Name | Required. Select the name of the classification from the drop-down list to tell the scanner to apply it if a match is found. |
    | State | Required. The options are enabled or disabled. Enabled is the default. |

    ![Create new classification rule](media/create-a-custom-classification-and-classification-rule/create-new-classification-rule.png)

### Creating a Regular Expression Rule

Important

Regular expressions in custom classifications are case insensitive.

1. If creating a regular expression rule, you'll see the following screen. You could optionally upload a file that will be used to **generate suggested regex patterns** for your rule. Only English language rules are supported.

    ![Create new regex rule](media/create-a-custom-classification-and-classification-rule/create-new-regex-rule.png)
2. If you decide to generate a suggested regex pattern, after uploading a file, select one of the suggested patterns and select **Add to Patterns** to use the suggested data and column patterns. You can tweak the suggested patterns or you may also type your own patterns without uploading a file.

    ![Generate suggested regex](media/create-a-custom-classification-and-classification-rule/suggested-regex.png)

    | Field | Description |
    | --- | --- |
    | Data Pattern | Optional. A regular expression that represents the data that's stored in the data field. The limit is large. In the previous example, the data patterns test for an employee ID that's literally the word `Employee{GUID}`. |
    | Column Pattern | Optional. A regular expression that represents the column names that you want to match. The limit is large. |
3. Under **Data Pattern** you can use the **Minimum match threshold** to set the minimum percentage of the distinct data value matches in a column that must be found by the scanner for the classification to be applied. The suggested value is 60%. If you specify multiple data patterns, this setting is disabled and the value is fixed at 60%.

    Note

    The Minimum match threshold must be at least 1%.
4. You can now verify your rule and **create** it.
5. Test the classification rule before completing the creation process to validate that it will apply tags to your assets. The classifications in the rule will be applied to the sample data uploaded just as it would in a scan. This means all of the system classifications and your custom classification will be matched to the data in your file.

    Input files could include delimited files (CSV, PSV, SSV, TSV), JSON, or XML content. The content will be parsed based on the file extension of the input file. Delimited data might have a file extension that matches any of the mentioned types. For example, TSV data can exist in a file named MySampleData.csv. Delimited content must also have a minimum of three columns.

    ![Test rule before creating](media/create-a-custom-classification-and-classification-rule/test-rule-screen.png)

    ![View applied classifications after uploading a test file](media/create-a-custom-classification-and-classification-rule/test-rule-uploaded-file-result-screen.png)

### Creating a Dictionary Rule

1. If creating a dictionary rule, you'll see the following screen. Upload a file that contains all possible values for the classification you're creating in a single column. Only English language rules are supported.

    ![Create dictionary rule](media/create-a-custom-classification-and-classification-rule/dictionary-rule.png)
2. After the dictionary is generated, you can adjust the minimum match threshold and submit the rule.

    ![Create dictionary rule, with Dictionary-Generated checkmark.](media/create-a-custom-classification-and-classification-rule/dictionary-generated.png)

## Edit or delete a custom classification

To update or edit a custom classification, follow these steps:

1. In the Microsoft Purview portal, open the **Data map** solution.
2. Under **Annotation management** select **Classifications**.
3. Select the **Custom** tab.
4. Select the classification you want to edit, then select the **Edit** button.

    ![Screenshot of the custom classification page, showing a classification selected and the edit button highlighted.](media/create-a-custom-classification-and-classification-rule/select-edit.png)
5. Now can edit the description of this custom classification. Select the **Ok** button when you're finished to save your changes.

To delete a custom classification:

1. After opening the **Data map**, and then **Classifications**, select the **Custom** tab.
2. Select the classification you want to delete, or multiple classifications you want to delete, and then select the **Delete** button. ![Screenshot of the custom classification page, showing a classification selected and the delete button highlighted.](media/create-a-custom-classification-and-classification-rule/select-delete.png)

You can also edit or delete a classification from inside the classification itself. Just select your classification, then select the **Edit** or **Delete** buttons in the top menu.

![Screenshot of a custom classification asset page, with the edit and delete buttons highlighted at the top of the page.](media/create-a-custom-classification-and-classification-rule/edit-inside-asset.png)

## Enable or disable classification rules

1. In your Microsoft Purview account, select the **Data map**, and then **Classification rules**.
2. Select the **Custom** tab.
3. You can check the current status of a classification rule by looking at the **Status** column in the table.
4. Select the classification rule, or multiple classification rules, that you want to enable or disable.
5. Select either the **Enable** or **Disable** buttons in the top menu.

    ![Screenshot of the custom classification rule page, showing a classification rule selected and the enable and disable buttons highlighted.](media/create-a-custom-classification-and-classification-rule/enable-or-disable.png)

You can also update the status of a rule when editing the rule.

## Edit or delete a classification rule

To update or edit a custom classification rule, follow these steps:

1. In your Microsoft Purview account, select the **Data map**, and then **Classification rules**.
2. Select the **Custom** tab.
3. Select the classification rule you want to edit, then select the **Edit** button.

    ![Screenshot of the custom classification rule page, showing a classification rule selected and the edit button highlighted.](media/create-a-custom-classification-and-classification-rule/select-edit-rule.png)
4. Now you can edit the state, the description, and the associated classification rule.
5. Select the **Continue** button.
6. You can upload a new file for your regular expression or dictionary rule to match against, and update your match threshold and column pattern match.
7. Select **Apply** to save your changes. Scans will need to be rerun with the new rule to apply changes across your assets.

To delete a custom classification:

1. After opening the **Data map**, and then **Classification rules**, select the **Custom** tab.
2. Select the classification rule you want to delete, and then select the **Delete** button.

    ![Screenshot of the custom classification rule page, showing a classification rule selected and the delete button highlighted.](media/create-a-custom-classification-and-classification-rule/select-delete-rule.png)