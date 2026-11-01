---
layout: Conceptual
title: Indonesia Drivers License Number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-indonesia-drivers-license-number
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2024-04-05T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Indonesia Drivers License Number sensitive information type entity definition.
locale: en-us
document_id: 9a9c6397-26d9-c89c-0656-e81de26741d2
document_version_independent_id: 9a9c6397-26d9-c89c-0656-e81de26741d2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-indonesia-drivers-license-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-indonesia-drivers-license-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-indonesia-drivers-license-number.md
cmProducts: []
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 63319505-cbf0-cb51-6918-79f652625cac
---

# Indonesia Drivers License Number entity definition | Microsoft Learn

## Format

Twelve or Fourteen digits

## Pattern

Twelve digits:

- any digit between 4-9
- followed by any digit between 0-9
- followed either 0 or 1
- followed by any nine digits between 0-9

Fourteen digits

- four digits
- followed by hyphen -
- four digits
- followed by hyphen -
- six digits

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regex `Regex_indonesia_drivers_license_number` finds content that matches the pattern.
- A keyword from `Keyword_indonesia_drivers_license_number` is found.

A DLP policy has low confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regex `Regex_indonesia_drivers_license_number` finds content that matches the pattern.
- A keyword from `Keyword_indonesia_drivers_license_number` is found.

```xml
<!-- Indonesia Drivers License Number -->
    <Entity id="67d902ee-c3ce-44a2-81ac-e9746e7d60a1" patternsProximity="300" recommendedConfidence="75" relaxProximity="true">
      <Pattern confidenceLevel="75">
        <IdMatch idRef="Regex_indonesia_drivers_license_number" />
        <Match idRef="Keyword_indonesia_drivers_license_number" />
      </Pattern>
      <Pattern confidenceLevel="65">
        <IdMatch idRef="Regex_indonesia_drivers_license_number" />
      </Pattern>
    </Entity>
```

## Keywords

### Keyword\_indonesia\_drivers\_license\_number

- SIM
- Surat Ijin Mengemudi
- SMART SIM
- Non-SMART SIM
- nomor SIM
- nomor lisensi
- DriverLic
- DriverLics
- DriverLicense
- DriverLicenses
- Driver Lic
- Driver Lics
- Driver License
- Driver Licenses
- DriversLic
- DriversLics
- DriversLicense
- DriversLicenses
- Drivers Lic
- Drivers Lics
- Drivers License
- Drivers Licenses
- Driver'Lic
- Driver'Lics
- Driver'License
- Driver'Licenses
- Driver' Lic
- Driver' Lics
- Driver' License
- Driver' Licenses
- Driver'sLic
- Driver'sLics
- Driver'sLicense
- Driver'sLicenses
- Driver's Lic
- Driver's Lics
- Driver's License
- Driver's Licenses
- DriverLic#
- DriverLics#
- DriverLicense#
- DriverLicenses#
- Driver Lic#
- Driver Lics#
- Driver License#
- Driver Licenses#
- DriversLic#
- DriversLics#
- DriversLicense#
- DriversLicenses#
- Drivers Lic#
- Drivers Lics#
- Drivers License#
- Drivers Licenses#
- Driver'Lic#
- Driver'Lics#
- Driver'License#
- Driver'Licenses#
- Driver' Lic#
- Driver' Lics#
- Driver' License#
- Driver' Licenses#
- Driver'sLic#
- Driver'sLics#
- Driver'sLicense#
- Driver'sLicenses#
- Driver's Lic#
- Driver's Lics#
- Driver's License#
- Driver's Licenses#