---
layout: Conceptual
title: End of Life Azure VM size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/lifecycle/end-of-life-sizes-list
breadcrumb_path: ../../../breadcrumb/azure-compute/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/94/azure-virtual-machines/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/ec2f1827-be25-ec11-b6e6-000d3a4f0f1c
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: mattmcinnes
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: iamwilliew
ms.author: mattmcinnes
ms.update-cycle: 1095-days
description: A list of Azure VM size series in the End of Life lifecycle stage and their modernization guides.
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: concept-article
ms.date: 2026-09-25T00:00:00.0000000Z
locale: en-us
document_id: 36de598f-b378-693b-4493-8639daa85e99
document_version_independent_id: 3c67710b-9b8d-d587-a35a-66372ed09462
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/lifecycle/end-of-life-sizes-list.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/lifecycle/end-of-life-sizes-list
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/lifecycle/end-of-life-sizes-list.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/a3955c7b-f5ee-420d-aff5-d7119738f38b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31948f4-2f38-404b-ac93-c3c8c5b3ae33
platformId: 9c62df53-653f-6db7-77d1-51198dbd7510
---

# End of Life Azure VM size series - Azure Virtual Machines | Microsoft Learn

This article lists the size series in the *End of Life* lifecycle stage. End of Life series have an announced retirement. For series that need them, *modernization guides* help you move to replacement sizes.

Note

End of Life series **aren't retired yet** and can still be used until their retirement date. However, series with an announced retirement have restrictions when you deploy through new subscriptions. To view retired size series, see [Retired and retiring VM size series](retirements-and-capacity-restrictions#retired-and-retiring-vm-size-series).

## What are End of Life size series?

End of Life virtual machine size series run on older hardware and have an announced retirement date. While they're still supported until retirement, plan and complete your modernization to Current or Extended sizes. Use Current sizes for new deployments.

To learn more about the Current, Extended, End of Life, and Retired lifecycle stages, see the [VM lifecycle overview](lifecycle-overview).

## General purpose End of Life sizes

| Series name | Modernization guide |
| --- | --- |
| B-series (V1) | [Modernization guide](retirement/retired-sizes-modernization-guide) |
| Standard D-series | [Modernization guide](retirement/retired-sizes-modernization-guide) |
| DS-series | [Modernization guide](retirement/retired-sizes-modernization-guide) |
| Dv1 and Dsv1-series | [Modernization guide](retirement/retired-sizes-modernization-guide) |
| Dv2 and Dsv2-series | [Modernization guide](retirement/retired-sizes-modernization-guide) |
| Dv3 and Dsv3-series | [Modernization guide](retirement/retired-sizes-modernization-guide) |
| Av2 and Amv2-series | [Modernization guide](retirement/retired-sizes-modernization-guide) |
| DCsv3 and DCdsv3-series | [Modernization guide](../retirement/dcsv3-series-retirement) |

For general purpose sizes that are retired or have an announced retirement date, see [retired general purpose sizes](retirements-and-capacity-restrictions#general-purpose-retired-sizes).

## Compute optimized End of Life sizes

| Series name | Modernization guide |
| --- | --- |
| F-series | [Modernization guide](retirement/retired-sizes-modernization-guide) |
| Fs-series | [Modernization guide](retirement/retired-sizes-modernization-guide) |
| Fsv2-series | [Modernization guide](retirement/retired-sizes-modernization-guide) |

For compute optimized sizes that are retired or have an announced retirement date, see [retired compute optimized sizes](retirements-and-capacity-restrictions#compute-optimized-retired-sizes).

## Memory optimized End of Life sizes

| Series name | Modernization guide |
| --- | --- |
| Ev3 and Esv3-series | [Modernization guide](retirement/retired-sizes-modernization-guide) |
| GS-series | [Modernization guide](retirement/retired-sizes-modernization-guide) |
| G-series | [Modernization guide](retirement/retired-sizes-modernization-guide) |
| Memory-optimized D-series | [Modernization guide](retirement/retired-sizes-modernization-guide) |
| Memory-optimized DS-series | [Modernization guide](retirement/retired-sizes-modernization-guide) |
| Msv2 and Mdsv2 isolated sizes | [Modernization guide](retirement/msv2-mdsv2-retirement) |

For memory optimized sizes that are retired or have an announced retirement date, see [retired memory optimized sizes](retirements-and-capacity-restrictions#memory-optimized-retired-sizes).

## Storage optimized End of Life sizes

| Series name | Modernization guide |
| --- | --- |
| Lsv1-series | [Modernization guide](retirement/retired-sizes-modernization-guide) |
| Lsv2-series | [Modernization guide](retirement/retired-sizes-modernization-guide) |

For storage optimized sizes that are retired or have an announced retirement date, see [retired storage optimized sizes](retirements-and-capacity-restrictions#storage-optimized-retired-sizes).

## GPU accelerated End of Life sizes

| Series name | Modernization guide |
| --- | --- |
| NVv3-series | [Modernization guide](retirement/nvv3-series-retirement) |
| NVv4-series | [Modernization guide](retirement/nvv4-retirement) |

For GPU accelerated sizes that are retired or have an announced retirement date, see [retired GPU accelerated sizes](retirements-and-capacity-restrictions#gpu-accelerated-retired-sizes).

## FPGA accelerated End of Life sizes

| Series name | Modernization guide |
| --- | --- |
| NP-series | [Modernization guide](retirement/np-series-retirement) |

For FPGA accelerated sizes that are retired or have an announced retirement date, see [retired FPGA accelerated sizes](retirements-and-capacity-restrictions#fpga-accelerated-retired-sizes).

## HPC End of Life sizes

| Series name | Modernization guide |
| --- | --- |
| HC-series | [Modernization guide](retirement/hc-series-retirement) |
| HBv2-series | [Modernization guide](retirement/hbv2-series-retirement) |

For HPC sizes that are retired or have an announced retirement date, see [retired HPC sizes](retirements-and-capacity-restrictions#hpc-retired-sizes).

## ADH End of Life sizes

For ADH sizes that are retired or have an announced retirement date, see [retired ADH sizes](retirements-and-capacity-restrictions#adh-retired-sizes).