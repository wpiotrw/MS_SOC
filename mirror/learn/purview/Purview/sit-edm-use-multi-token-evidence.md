---
layout: Conceptual
title: Use multi-token matching for corroborative evidence in EDM SITs | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-edm-use-multi-token-evidence
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-sensitive-information-types
ms.date: 2023-12-11T00:00:00.0000000Z
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Learn how to use multi-token matching for exact data match sensitive information types.
ms.custom: seo-marvel-apr2020
locale: en-us
document_id: e9c1be5b-e136-cd99-53dd-0ccf3c9fe0f4
document_version_independent_id: e9c1be5b-e136-cd99-53dd-0ccf3c9fe0f4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-edm-use-multi-token-evidence.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-edm-use-multi-token-evidence
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-edm-use-multi-token-evidence.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/a3955c7b-f5ee-420d-aff5-d7119738f38b
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31948f4-2f38-404b-ac93-c3c8c5b3ae33
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 90d2d0c8-165c-760e-fea7-da7df1da183d
---

# Use multi-token matching for corroborative evidence in EDM SITs | Microsoft Learn

To use multi-token matching to identify corroborative evidence for your EDM sensitive information types, you must explicitly opt in for multi-token support for each multi-token corroborative evidence field. You can do this either through the new EDM UI experience or through the schema XML update process. Following are the steps for each method.

## Opt-in through the new EDM UI experience

The new EDM UI experience guides you through the process of [creating or editing an EDM schema](sit-get-started-exact-data-match-create-schema#create-the-schema-for-exact-data-match-based-sensitive-information-types) and uploading your data. You can access it from the Microsoft Purview Portal, under **Data classification** &gt; **Sensitive info types** &gt; **Exact data match**.

When you upload a sample file, EDM automatically maps the SIT that can best detect the sample data in each field. If none of the SITs in your environment can detect the sample data in a field, EDM defaults to single-token matching. Single-token matching means that EDM only compares the hashes of individual strings identified in DLP policy fields with each individual string in the content. The field selected as the primary element for your schema must be mapped to a SIT. In contrast, corroborative evidence fields can either be mapped to a SIT or can be configured for either single-token or multi-token matching.

However, if the sample data in a policy field contains multi-token values and if EDM is operating in single-token mode, a warning displays stating that using single-token matching might result in missed detections. In this case, you can switch to multi-token matching. When you use multi-token matching, EDM compares the hashes of consecutive tokens (strings) in the policy fields against consecutive tokens in the content, up to a maximum number of tokens supported by this feature. The current maximum is five (5) tokens. For example, if your field contains the value "Jane Doe", EDM compares the hashes of "Jane", "Doe", and "Jane Doe" with the content. It then produces a match if the hashes of any of these combinations are identical to the hashed value in your data source.

Tip

To ensure multi-token match detection, trim multi-token corroborative evidence fields to the maximum number of tokens supported. Alternatively, map the multi-token fields to a SIT that can fully detect the multi-token data.

In contrast, if you select multi-token matching for a field that only contains single-token data, a warning displays stating that using multi-token matching might result in higher latency. Higher latency in matching occurs because multi-token matching is inefficient. Additionally, multi-token matching isn't required if the actual EDM data that is later hashed and uploaded is expected to be a single-token field. In general, if any of the fields you use for corroborative evidence can be mapped to a SIT, do that instead of relying on single-token or multi-token matching.

Make sure that your sample data is fully representative of your production data. If your sample file doesn't include multi-token values, but your production data does, you might not get a warning for multi-token matches. For instance, this can occur in cases where your sample data includes only single-token values for a `FirstName` field, but your production data includes multi-token values for the same field.

## Opt-in through the EDM schema XML update process

You can also create or update an XML schema to implement multi-token matching for corroborative evidence using PowerShell.

Here's a sample XML schema with multi-token settings for protecting patient records:

```xml
<EdmSchema xmlns="http://schemas.microsoft.com/office/2018/edm">
 <DataStore name="DemoMTCorroborativeEvidenceSchema"
            description="Test" version="1">
  <Field name="Name"
         searchable="false" 
      caseInsensitive="true" 
      ignoredDelimiters="" 
      isMultiToken="false"/>
  <Field name="SSN"
         searchable="true" 
      caseInsensitive="true" 
      ignoredDelimiters="" 
      isMultiToken="false"/>
  <Field name="PatientID" 
      searchable="false" 
      caseInsensitive="true" 
      ignoredDelimiters="" 
      isMultiToken="false"/>
  <Field name="MedicalCondition" 
      searchable="false" 
      caseInsensitive="true" 
      ignoredDelimiters="" 
      isMultiToken="true"/>
  <Field name="Address"
         searchable="false" 
      caseInsensitive="true" 
      ignoredDelimiters="" 
      isMultiToken="true"/>[Learn about exact data match based sensitive information types](sit-learn-about-exact-data-match-based-sits.md#learn-about-exact-data-match-based-sensitive-information-types)
 </DataStore>
</EdmSchema>   

```

Each corroborative evidence field can be configured for multi-token support through the new XML parameter `isMultiToken`. This parameter can be set to `true` or `false`. Any field with `isMultiToken` set to `true` is treated as a multi-token field and is compared with consecutive strings in the content, up to the maximum number of tokens supported by this feature. EDM treats fields with `isMultiToken` set to `false`, or that don’t have this parameter, as single-token fields. These fields are only compared with individual strings in the content.

For more information about what an EDM schema is, see the [Schema](sit-learn-about-exact-data-match-based-sits#schema) section of the [Learn about exact data match based sensitive information types](sit-learn-about-exact-data-match-based-sits#learn-about-exact-data-match-based-sensitive-information-types) article.

For details about creating an EDM schema, see [Create your EDM schema and SIT](sit-create-edm-sit-unified-ux-schema-rule-package#create-your-edm-schema-and-sit).