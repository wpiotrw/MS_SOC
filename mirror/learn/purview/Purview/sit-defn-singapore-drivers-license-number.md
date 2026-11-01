---
layout: Conceptual
title: Singapore driver's license number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-singapore-drivers-license-number
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2023-09-13T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Singapore driver's license number sensitive information type entity definition.
locale: en-us
document_id: 5447eff9-da5e-64c9-3c96-5507fc2b7aac
document_version_independent_id: 5447eff9-da5e-64c9-3c96-5507fc2b7aac
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-singapore-drivers-license-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-singapore-drivers-license-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-singapore-drivers-license-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: 44005ae8-4ca1-e99f-6142-c1aa6a921316
---

# Singapore driver's license number entity definition | Microsoft Learn

## Format

Nine alphanumeric characters.

## Pattern

- One letter followed by
- seven digits followed by
- One letter

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Checksum

NA

## Definition

A DLP policy has high confidence of detection for this type of sensitive information if, within a proximity of 300 characters:

- The regular expression Regex\_singapore\_driving\_license finds content that matches the pattern.
- A keyword from Keyword\_singapore\_driving\_license or Keywords\_eu\_driver's\_license\_number\_common is found.

A DLP policy has low confidence of detection for this type of sensitive information if, within a proximity of 300 characters:

- The regular expression Regex\_singapore\_driving\_license finds content that matches the pattern.

```xml
      <!-- Singapore Driving License Number -->
      <Entity id="beaa54d7-ec6a-4160-a37b-f3916b68934b" patternsProximity="300" recommendedConfidence="85" relaxProximity="true">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Regex_singapore_driving_license" />
          <Any minMatches="1">
            <Match idRef="Keywords_eu_driver's_license_number_common" />
            <Match idRef="Keyword_singapore_driving_license" />
          </Any>
        </Pattern>
        <Pattern confidenceLevel="65">
          <IdMatch idRef="Regex_singapore_driving_license" />
        </Pattern>
      </Entity>
```

## Keywords

**Keyword\_singapore\_driving-license**

- Licence number
- licence no
- licence#
- lesen memandu
- lesen pemandu
- nombor lesen
- 驾驶执照
- 驾驶 执照
- 驾驶执照号码
- 驾驶 执照 号码

**Keywords\_eu\_driver's\_license\_number\_common**

- driverlic
- driverlics
- driverlicense
- driverlicenses
- driverlicence
- driverlicences
- driver lic
- driver lics
- driver license
- driver licenses
- driver licence
- driver licences
- driverslic
- driverslics
- driverslicence
- driverslicences
- driverslicense
- driverslicenses
- drivers lic
- drivers lics
- drivers license
- drivers licenses
- drivers licence
- drivers licences
- driver'lic
- driver'lics
- driver'license
- driver'licenses
- driver'licence
- driver'licences
- driver' lic
- driver' lics
- driver' license
- driver' licenses
- driver' licence
- driver' licences
- driver'slic
- driver'slics
- driver'slicense
- driver'slicenses
- driver'slicence
- driver'slicences
- driver's lic
- driver's lics
- driver's license
- driver's licenses
- driver's licence
- driver's licences
- dl#
- dls#
- driverlic#
- driverlics#
- driverlicense#
- driverlicenses#
- driverlicence#
- driverlicences#
- driver lic#
- driver lics#
- driver license#
- driver licenses#
- driver licences#
- driverslic#
- driverslics#
- driverslicense#
- driverslicenses#
- driverslicence#
- driverslicences#
- drivers lic#
- drivers lics#
- drivers license#
- drivers licenses#
- drivers licence#
- drivers licences#
- driver'lic#
- driver'lics#
- driver'license#
- driver'licenses#
- driver'licence#
- driver'licences#
- driver' lic#
- driver' lics#
- driver' license#
- driver' licenses#
- driver' licence#
- driver' licences#
- driver'slic#
- driver'slics#
- driver'slicense#
- driver'slicenses#
- driver'slicence#
- driver'slicences#
- driver's lic#
- driver's lics#
- driver's license#
- driver's licenses#
- driver's licence#
- driver's licences#
- driving licence
- driving license
- dlno#
- driv lic
- driv licen
- driv license
- driv licenses
- driv licence
- driv licences
- driver licen
- drivers licen
- driver's licen
- driving lic
- driving licen
- driving licenses
- driving licence
- driving licences
- driving permit
- dl no
- dlno
- dl number