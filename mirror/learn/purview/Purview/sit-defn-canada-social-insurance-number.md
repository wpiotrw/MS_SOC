---
layout: Conceptual
title: Canada social insurance number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-canada-social-insurance-number
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2023-06-01T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Canada social insurance number sensitive information type entity definition.
locale: en-us
document_id: 95e12e19-8c01-00e0-c5ac-f5bf426bd49a
document_version_independent_id: 95e12e19-8c01-00e0-c5ac-f5bf426bd49a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-canada-social-insurance-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-canada-social-insurance-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-canada-social-insurance-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 759e79fe-2799-3dbc-3612-6f3a36c8059c
---

# Canada social insurance number entity definition | Microsoft Learn

## Format

nine digits with optional hyphens or spaces

## Pattern

Formatted:

- three digits
- a hyphen or space
- three digits
- a hyphen or space
- three digits

Unformatted: nine digits

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function Func\_canadian\_sin finds content that matches the pattern.
- At least one of the following patterns:
    - A keyword from Keyword\_sin is found.
    - A keyword from Keyword\_sin\_collaborative is found.
- The checksum passes.

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function Func\_unformatted\_canadian\_sin finds content that matches the pattern.
- A keyword from Keyword\_sin is found.
- The checksum passes.

```xml
    <!-- Canada Social Insurance Number -->
    <Entity id="a2f29c85-ecb8-4514-a610-364790c0773e" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="85">
        <IdMatch idRef="Func_canadian_sin" />
        <Any minMatches="1">
          <Match idRef="Keyword_sin" />
          <Match idRef="Keyword_sin_collaborative" />
        </Any>
      </Pattern>
      <Pattern confidenceLevel="75">
        <IdMatch idRef="Func_unformatted_canadian_sin" />
        <Match idRef="Keyword_sin" />
      </Pattern>
    </Entity>
```

## Keywords

### Keyword\_sin

- sin
- social insurance
- numero d'assurance sociale
- sins
- ssn
- ssns
- social security
- numero d'assurance social
- national identification number
- national id
- sin#
- soc ins
- social ins
- NAS (case sensitive)
- numéro d’assurance social
- numéro d’assurance sociale
- assurance social
- carte d’assurance sociale

### Keyword\_sin\_collaborative

- driver's license
- drivers license
- driver's licence
- drivers licence
- DOB
- Birthdate
- Birthday
- Date of Birth