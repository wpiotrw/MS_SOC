---
layout: Conceptual
title: Create an Exact Data Match SIT/rule package | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-get-started-exact-data-match-create-rule-package
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-sensitive-information-types
ms.date: 2026-06-26T00:00:00.0000000Z
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Learn how to create an exact data match (EDM) sensitive information type rule package using the Microsoft Purview portal tool or by manually authoring an XML rule package file.
ms.custom: msecd-doc-authoring-1014, seo-marvel-apr2020, sfi-ga-nochange
ai-usage: ai-assisted
locale: en-us
document_id: 76e9f4a9-b3ee-80d9-f05b-090a75bde21b
document_version_independent_id: 76e9f4a9-b3ee-80d9-f05b-090a75bde21b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-get-started-exact-data-match-create-rule-package.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-get-started-exact-data-match-create-rule-package
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-get-started-exact-data-match-create-rule-package.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: 7abbdb40-029e-b150-dc72-7e9b4ac63828
---

# Create an Exact Data Match SIT/rule package | Microsoft Learn

## Products and services this rule package procedure applies to

- [Create an EDM SIT using the classic experience workflow](sit-create-edm-sit-classic-ux-workflow)

You can create an exact data match (EDM) SIT (SIT) by using the Use the Exact Data Match schema and SIT pattern tool in the Microsoft Purview Portal, or you can create the rule package manually as an XML file. You can also combine the two methods by using one method to create the schema and later using the other method to edit it.

If you are not familiar with EDM-based SITS or their implementation, you should familiarize yourself with:

- [Learn about sensitive information types](sit-sensitive-information-type-learn-about#learn-about-sensitive-information-types)
- [Learn about exact data match based sensitive information types](sit-learn-about-exact-data-match-based-sits#learn-about-exact-data-match-based-sensitive-information-types)
- [Get started with exact data match based sensitive information types](sit-get-started-exact-data-match-based-sits-overview)

### Prerequisites

Perform the steps in these articles:

1. [Export source data for exact data match based sensitive information types](sit-get-started-exact-data-match-export-data#export-source-data-for-exact-data-match-based-sensitive-information-types)
2. [Create the schema for exact data match based sensitive information types](sit-get-started-exact-data-match-create-schema#create-the-schema-for-exact-data-match-based-sensitive-information-types)
3. [Hash and upload the sensitive information source table for exact data match sensitive information types](sit-get-started-exact-data-match-hash-upload#hash-and-upload-the-sensitive-information-source-table-for-exact-data-match-sensitive-information-types)

- Whether you will be creating an EDM SIT using the tool or the rule package XML file via PowerShell, you must have Compliance administrator or Global administrator role to create, test, and deploy a custom SIT through the UI. See [About admin roles in Office 365](/en-us/office365/admin/add-users/about-admin-roles).

Important

Microsoft recommends that you use roles with the fewest permissions. This helps improve security for your organization. Global Administrator is a highly privileged role that should only be used in scenarios where a lesser privileged role can't be used.

- Identify one of the built-in SITs to use as the Primary elements SIT.
    - If none of the built-in SITs will match the data in the column you selected you will have to create a custom SIT that does.
    - If you selected the Ignored Delimiters option for the primary element column in your schema, make sure the custom SIT you create will match data with and without the selected delimiters.
    - If you use a built-in SIT, make sure it will detect exactly the strings you want to select, and not include any surrounding characters or exclude any valid part of the string as stored in your sensitive information table.

See [Sensitive information type entity definitions](sit-sensitive-information-type-entity-definitions#sensitive-information-type-entity-definitions) and [Create custom sensitive information types](sit-create-a-custom-sensitive-information-type).

## Use the Exact Data Match schema and SIT pattern tool

You can use the Exact Data Match schema and SIT pattern tool to create your SIT files to help simplify the process.

An EDM SIT is composed of one or more patterns. Each pattern describes a combination of fields from the schema that will be used to identify sensitive content in a document or email (evidence).

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Information Protection** &gt; **Classifiers** &gt; **EDM classifiers**.
2. 1. Set the **New EDM experience** toggle to **Off**
3. Choose **EDM sensitive info types** and **Create EDM sensitive info type** to open the Sensitive Information Type configuration tool.
4. Select **Choose an existing EDM schema** and pick the schema you created in [Create the schema for exact data match based sensitive information types](sit-get-started-exact-data-match-create-schema#create-the-schema-for-exact-data-match-based-sensitive-information-types). Select **Add**.
5. Choose **Next** and choose **Create pattern**.
6. Pick the **Confidence level** and **Primary element**. To learn more about confidence levels, see [Learn about sensitive information types](sit-sensitive-information-type-learn-about#learn-about-sensitive-information-types).
7. Choose the **Primary element's sensitive info type** to associate it with to define what text in the document will be compared with all the values in the primary element field. See [SIT Entity Definitions](sit-sensitive-information-type-entity-definitions) to learn more about the available sensitive information types.

    Important

    Select a SIT that closely matches the format of the content you want to find. Selecting a SIT that matches unnecessary content, such as one that matches *all* text strings, or *all* numbers can cause excessive load in the system, which can result in sensitive information remaining undetected.
8. Select your **Supporting elements** and match options.
9. Choose **Done**.
10. Choose **Create pattern** if you want to create additional patterns for your EDM SIT.
11. Select **Next**.
12. Choose your desired **Recommended confidence level** and **Character proximity**. This will be the default value for the whole EDM SIT. (For information on character proximity, see [Understanding proximity](sensitive-information-type-learn-about#understanding-proximity)). Select **Next**.
13. Choose **Next** and fill in a **Name** and **Description for admins**.  As you create your schema file, your column headers (data fields) must adhere to the following naming requirements:  - Must start with a letter and must consist of at least three alphanumeric characters.  - Must include only alphanumeric characters.
14. Review and choose **Submit**.

## Edit or delete a SIT pattern

To edit or delete an existing EDM SIT pattern, perform the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Information Protection**&gt; **Classifiers** &gt; **EDM classifiers**.
2. 1. Set the **New EDM experience** toggle to **Off**
3. Choose **EDM sensitive info types**.
4. Pick the EDM SIT you want to edit.
5. Choose **Edit EDM sensitive info type** or **Delete EDM sensitive info type** from the flyout.
6. For the steps to edit an EDM sensitive info type, see Use the Exact Data Match schema and SIT pattern tool.

## Working with specific types of data

For performance reasons, it is critical that you use patterns that will minimize the number of unnecessary matches. For example, you might use a SIT based on the regular expression.

`\b\w*\b`

This regular expression would match every individual word or number in any document or email. Matching every word or number would cause the service to be overloaded with matches and miss detecting true matches. Using more precise patterns can avoid this situation. Here are some recommendations for identifying the right configuration for some common types of data.

**Email addresses**: Email addresses can be easy to identify, but because they are so common in sensitive content, they might cause a significant load in the system if used as a primary field. Use email adderss only as secondary evidence. If they must be used as primary evidence, when you define your custom SIT use logic to exclude items where email addresses are used as `From` or `To` fields in emails. Also use logic to exclude email addresses from your company’s domain to reduce the number of unnecessary strings that need to be matched.

**Phone numbers**: Phone numbers can come in many different formats, including or excluding country/region prefixes, area codes, and separators. To reduce the false negatives while keeping load to a minimum, use them only as secondary elements, exclude all likely separators, like parenthesis and dashes and only include in your sensitive data table the part that will always be present in the phone number.

**People's names**: Don’t use people’s names as primary elements if using a SIT based on a regular expression as the classification element for this EDM type, because they are difficult to distinguish from common words.

If you must use a primary element that is hard to identify with a specific pattern (such as a project code name), that could generate a high volume of matches to be processed, make sure you include keywords in the SIT you use as the classification element for your EDM type. For example, if using project code names that are also regular words, you can use the word `project` as required additional evidence in close proximity to the project name regular expression-based pattern in the SIT you use as the classification element for your EDM type. Or, you might consider using a SIT based on a regular dictionary as the classification element for your EDM SIT.

When trying to match numeric strings, specify the allowed ranges of numbers such as the number of digits or the starting digits, if known. If you need to match a relatively flexible range of numbers, you can use keywords in the base SIT to reduce the number of matches. For example, if trying to match account numbers consisting of 7-11 digits, add the words `account`, `customer`, `acct.` to the SIT as required additional evidence. This reduces the likelihood of unnecessary matches that could result in exceeding the limits of EDM matches that can be processed.

If a field you need to use as a primary element follows a simple pattern that might result in large numbers of matches, and you can’t add the presence of keywords as additional evidence in the SIT, you can instead require a minimum number of occurrences of that pattern. For example, you could use a custom SIT defined in the following way to detect at least 29 other five-digit numbers surrounding a potential five-digit number to match against in your sensitive content:

```xml
 <Entity id="00aa00aa-bb11-cc22-dd33-44ee44ee44ee"
                  patternsProximity="300"
                  recommendedConfidence="85"
                  relaxProximity="false">
                  <Pattern confidenceLevel="85"
                              proximity="300">
                              <IdMatch idRef="MRN"/>
                              <Match idRef="30 AccountNrs"
                                    minCount="30"
                                    proximity="3000"
                                    uniqueResults="true"/>
                  </Pattern>
      </Entity>
      <Regex id="30 AccountNrs">\d{5}</Regex>
```

In some cases, you might have to identify certain account or record identification numbers that for historical reasons don’t follow a standardized pattern. For example, `Medical Record Numbers` can be composed of many different permutations of letters and numbers within the same organization. Even though it might be hard at first to identify a pattern, closer inspection often lets you narrow down a pattern that describes all valid values without causing an excessive number of invalid matches. For example, it might be detected that “all MRNs are at least seven characters in length, have at least two numerical digits in them, and if they have any letters in them, they start with one”. Creating a regular expression based on such criteria should allow you to minimize unnecessary matches while capturing all the desired values, and further analysis might allow increased precision by defining separate patterns that describe different formats.

## Create a rule package manually

This procedure shows you how to create a file in XML format called a rule package (with Unicode encoding), and then upload it into Microsoft Purview using Security & Compliance PowerShell cmdlets.

Note

If the SIT that you map to can detect multi-word corroborative evidence, the secondary elements you define in a manually created rule package can be mapped to the SIT. For example, the name `John Smith` would not match as a secondary element because we'd compare `John` and `Smith` found in the content separately to the term `John Smith` uploaded in one of the fields, if that corroborative evidence field wasn't mapped to a SIT that can detect that pattern.

There’s a limit of 10 rule packages in a Microsoft 365 tenant. Since a rule package can contain an arbitrary number of sensitive information types, you can avoid creating a new rule package each time you want to define a new SIT using this method, instead export an existing rule package and add your sensitive information types to the XML before re- uploading it.

1. Create a rule package in XML format (with Unicode encoding), similar to the following example. (You can copy, modify, and use our example.)

    When you set up your rule package, make sure to correctly reference your .csv, .tsv, or pipe (|) delimited sensitive information source table file and **edm.xml** schema file. You can copy, modify, and use our example. In this sample xml the following fields need to be customized to create your EDM sensitive type:

    - **RulePack id & ExactMatch id**: Use [New-GUID](/en-us/powershell/module/microsoft.powershell.utility/new-guid) to generate a GUID.
    - **Datastore**: This field specifies EDM lookup data store to be used. You provide the data source name of the configured EDM Schema.
    - **idMatch**: This field points to the primary element for EDM.
    - **Matches**: Specifies the field to be used in exact lookup. You provide a searchable field name in EDM Schema for the DataStore.
    - **Classification**: This field specifies the SIT match that triggers EDM lookup. You can use the name or GUID of an existing built-in or custom SIT.

    Note

    Be aware that any string that matches the SIT provided will be hashed and compared to every entry in the sensitive information source table. To avoid performance issues if you choose a custom SIT for the classification element, don't use one that will match a large percentage of content. For example one that matches "any number" or "any five-letter word". You can differentiate it by adding supporting keywords or including formatting in the definition of the custom classification SIT.

    - **Match**: This field points to additional evidence found in proximity of idMatch.
    - **Matches**: You provide any field name in EDM Schema for DataStore.
    - **Resource idRef:** This section specifies the name and description for sensitive type in multiple locales

        - You provide GUID for ExactMatch ID.
        - **Name** & **description**: customize as required.

        ```xml
        <RulePackage xmlns="http://schemas.microsoft.com/office/2018/edm">
           <RulePack id="fd098e03-1796-41a5-8ab6-198c93c62b11">
             <Version build="0" major="2" minor="0" revision="0" />
             <Publisher id="..." />
             <Details defaultLangCode="en-us">
               <LocalizedDetails langcode="en-us">
                 <PublisherName>IP DLP</PublisherName>
                 <Name>Health Care EDM Rulepack</Name>
                 <Description>This rule package contains the EDM sensitive type for health care sensitive types.</Description>
               </LocalizedDetails>
             </Details>
           </RulePack>
           <Rules>
             <ExactMatch id = "E1CC861E-3FE9-4A58-82DF-4BD259EAB371" patternsProximity = "300" dataStore ="PatientRecords" recommendedConfidence = "65" >
               <Pattern confidenceLevel="65">
                 <idMatch matches = "SSN" classification = "U.S. Social Security Number (SSN)" />
               </Pattern>
               <Pattern confidenceLevel="75">
                 <idMatch matches = "SSN" classification = "U.S. Social Security Number (SSN)" />
                 <Any minMatches ="3" maxMatches ="6">
                   <match matches="PatientID" />
                   <match matches="MRN"/>
                   <match matches="FirstName"/>
                   <match matches="LastName"/>
                   <match matches="Phone"/>
                   <match matches="DOB"/>
                 </Any>
               </Pattern>
             </ExactMatch>
             <LocalizedStrings>
               <Resource idRef="E1CC861E-3FE9-4A58-82DF-4BD259EAB371">
                 <Name default="true" langcode="en-us">Patient SSN Exact Match.</Name>
                 <Description default="true" langcode="en-us">EDM Sensitive type for detecting Patient SSN.</Description>
               </Resource>
             </LocalizedStrings>
           </Rules>
        </RulePackage>
        ```
2. Upload the rule package by running the following PowerShell command:

    ```powershell
    New-DlpSensitiveInformationTypeRulePackage -FileData ([System.IO.File]::ReadAllBytes('.\\rulepack.xml'))
    ```

Note

The syntax of the rule package file is the same as for other sensitive information types. For complete details on the syntax of the rule package file and for additional configuration options, and for instructions on modifying and deleting sensitive information types using PowerShell, [Create a custom SIT using PowerShell](sit-create-a-custom-sensitive-information-type-in-scc-powershell#create-a-custom-sensitive-information-type-using-powershell).