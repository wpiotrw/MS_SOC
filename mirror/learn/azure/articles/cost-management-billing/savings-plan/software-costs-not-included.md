---
layout: Conceptual
title: Software costs not included in compute savings plans - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/software-costs-not-included
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/118/azure-cost-management/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/748a4eaa-0e25-ec11-b6e6-000d3a4f07b8
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
learn_banner_products:
- azure
description: Learn how compute savings plan discounts apply only to infrastructure costs, not software costs.
author: nwokolo
ms.author: onwokolo
ms.reviewer: onwokolo
ms.service: cost-management-billing
ms.subservice: savings-plan
ms.topic: glossary
ms.date: 2026-10-29T00:00:00.0000000Z
locale: en-us
document_id: 88ff629f-0ed1-2ba4-4d35-60974ba06cd3
document_version_independent_id: 118b9b57-8193-8af4-f85a-083604606a47
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/savings-plan/software-costs-not-included.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/savings-plan/software-costs-not-included
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/savings-plan/software-costs-not-included.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/486161dc-fa28-4625-9b1c-1a21d690bc8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5dd28c86-729c-4723-ab5a-57e26fcec2a8
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 1eb69a8a-aafe-746b-c4ff-f19b9a2bd96d
---

# Software costs not included in compute savings plans - Microsoft Cost Management | Microsoft Learn

Compute savings plan discounts apply only to infrastructure costs, not software costs. If you use Windows VMs with a compute savings plan but don't have Azure Hybrid Benefit for those VMs, you're charged for the software meters listed in the following sections.

## Windows software meters not included in savings plan cost

| **MeterId** | **MeterName in usage file** | **Used by VM** |
| --- | --- | --- |
| e7e152ac-f29c-4cce-ad6e-026192c01ef2 | Reservation-Windows Svr Burst (one Core) | B Series |
| cac255a2-9f0f-4c62-8bd6-f0fa449c5f76 | Reservation-Windows Svr Burst (two Core) | B Series |
| 09756b58-3fb5-4390-976d-9ddd14f9ed18 | Reservation-Windows Svr Burst (four Core) | B Series |
| e828cb37-5920-4dc7-b30f-664e4dbcb6c7 | Reservation-Windows Svr Burst (eight Core) | B Series |
| f65a06cf-c9c3-47a2-8104-f17a8542215a | Reservation-Windows Svr (one Core) | All except B Series |
| b99d40ae-41fe-4d1d-842b-56d72f3d15ee | Reservation-Windows Svr (two Core) | All except B Series |
| 1cb88381-0905-4843-9ba2-7914066aabe5 | Reservation-Windows Svr (four Core) | All except B Series |
| 07d9e10d-3e3e-4672-ac30-87f58ec4b00a | Reservation-Windows Svr (six Core) | All except B Series |
| 603f58d1-1e96-460b-a933-ce3775ac7e2e | Reservation-Windows Svr (eight Core) | All except B Series |
| 36aaadda-da86-484a-b465-c8b5ab292d71 | Reservation-Windows Svr (12 Core) | All except B Series |
| 02968a6b-1654-4495-ada6-13f378ba7172 | Reservation-Windows Svr (16 Core) | All except B Series |
| 175434d8-75f9-474b-9906-5d151b6bed84 | Reservation-Windows Svr (20 Core) | All except B Series |
| 77eb6dd0-88f5-4a16-ab39-05d1742efb25 | Reservation-Windows Svr (24 Core) | All except B Series |
| 0d5bdf46-b719-4b1f-a780-b9bdfffd0591 | Reservation-Windows Svr (32 Core) | All except B Series |
| f1214b5c-cc16-445f-be6c-a3bb75f8395a | Reservation-Windows Svr (40 Core) | All except B Series |
| 637b7c77-65ad-4486-9cc7-dc7b3e9a8731 | Reservation-Windows Svr (64 Core) | All except B Series |
| da612742-e7cc-4ca3-9334-0fb7234059cd | Reservation-Windows Svr (72 Core) | All except B Series |
| a485cb8c-069b-4cf3-9a8e-ddd84b323da2 | Reservation-Windows Svr (128 Core) | All except B Series |
| 904c5c71-1eb7-43a6-961c-d305a9681624 | Reservation-Windows Svr (256 Core) | All except B Series |
| 6fdab81b-4284-4df9-8939-c237cc7462fe | Reservation-Windows Svr (96 Core) | All except B Series |

## Cloud services software meters not included in savings plan cost

| **MeterId** | **MeterName in usage file** |
| --- | --- |
| ac9d47ff-ff68-4afc-a145-0c321cf8d0d5 | Cloud Services 1 vCPU License |
| e0434559-19ee-4132-9c46-05ad4044f3f7 | Cloud Services 2 vCPU License |
| 6ecc834e-39b3-48b3-8d10-cc5626bacb66 | Cloud Services 4 vCPU License |
| 13103090-ca72-4825-ab12-7f16c4931d95 | Cloud Services 8 vCPU License |
| ecd2bb6e-45a5-49aa-a58b-3947ba21c364 | Cloud Services 16 vCPU License |
| de2c7f1d-06dc-4b16-bc8b-c2ec5f4c8aee | Cloud Services 20 vCPU License |
| ca1af837-4b35-47f5-8d14-b1988149c4ca | Cloud Services 32 vCPU License |
| dc72ee45-2ab7-4698-b435-e2cf10d1f9f6 | Cloud Services 64 vCPU License |
| 7a803026-244c-4659-834c-11e6b2d6b76f | Cloud Services 80 vCPU License |

## Get rates for meters

For information about getting the pay-as-you-go rates for each meter, see [Download Azure price sheet](download-savings-plan-price-sheet). EA customers should follow the first seven steps in the EA section. Microsoft Customer Agreement customers should follow the first five steps in the MCA section.

## Need help? Contact us.

If you have savings plan questions, contact your account team or [create a support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest). Currently, Microsoft provides expert support for savings plans only in English.