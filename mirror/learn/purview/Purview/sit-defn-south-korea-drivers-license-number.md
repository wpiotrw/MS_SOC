---
layout: Conceptual
title: South Korea driver's license number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-south-korea-drivers-license-number
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
description: South Korea driver's license number sensitive information type entity definition.
locale: en-us
document_id: f6a4d501-3b4b-24b5-4a7a-03fe7b637571
document_version_independent_id: f6a4d501-3b4b-24b5-4a7a-03fe7b637571
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-south-korea-drivers-license-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-south-korea-drivers-license-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-south-korea-drivers-license-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: 62eecbb1-4244-8ea0-1716-c42010b32c69
---

# South Korea driver's license number entity definition | Microsoft Learn

## Format

10 or 12 digits with optional hyphens.

## Pattern

Pattern 1:

- two digits
- optional hyphen
- six digits
- optional hyphen
- two digits

Pattern 2:

- optional 2 digits (allowed digits are 11-26 and 28)
- optional hyphen
- two digits
- optional hyphen
- six digits
- optional hyphen
- two digits

## Checksum

Not applicable

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A Data Loss Passport (DLP) policy has high confidence of detection for this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_south_korea_driver's_license_10digits` or `Regex_south_korea_driver's_license_12digits` finds content that matches the pattern.
- A keyword from `Keyword_south_korea_driver's_license` or `Keywords_eu_driver's_license_number_common` is found.

A DLP policy has low confidence of detection for this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_south_korea_driver's_license_12digits` finds content that matches the pattern.

```xml
      <!-- South Korea Driver's License Number -->
      <Entity id="3da0b024-4c08-406b-9f9e-de96accd0209" patternsProximity="300" recommendedConfidence="85">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Regex_south_korea_driver's_license_10digits" />
          <Any minMatches="1">
            <Match idRef="Keywords_eu_driver's_license_number_common" />
            <Match idRef="Keyword_south_korea_driver's_license" />
          </Any>
        </Pattern>
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Regex_south_korea_driver's_license_12digits" />
          <Any minMatches="1">
            <Match idRef="Keywords_eu_driver's_license_number_common" />
            <Match idRef="Keyword_south_korea_driver's_license" />
          </Any>
        </Pattern>
        <Pattern confidenceLevel="65">
          <IdMatch idRef="Regex_south_korea_driver's_license_12digits" />
        </Pattern>
      </Entity>
```

## Keywords

**Keyword\_south\_korea\_driver's\_license**

- 운전면허번호
- 운전면허 번호
- 운전 면허 번호
- 운전면허증 번호
- 운전면허증

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