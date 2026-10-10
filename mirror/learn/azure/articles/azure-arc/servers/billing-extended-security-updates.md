---
layout: Conceptual
title: Billing service for Extended Security Updates for Windows Server through Azure Arc - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/billing-extended-security-updates
breadcrumb_path: ../../breadcrumb/azure-management/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/146/azure-arc/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/5c778dec-0625-ec11-b6e6-000d3a4f0858
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
zone_pivot_group_filename: zone-pivots/azure-management/zone-pivot-groups.json
author: davidsmatlak
learn_banner_products:
- azure
ms.reviewer: davidsmatlak
ms.author: davidsmatlak
ms.service: azure-arc
ms.subservice: servers-azure-arc
description: Learn about billing services for Extended Security Updates for Windows Server 2012 and Windows Server 2016 enabled by Azure Arc.
ms.date: 2026-09-11T00:00:00.0000000Z
ms.topic: concept-article
zone_pivot_groups: extended-security-updates-windows-server
locale: en-us
document_id: 1e65facf-37e3-9939-688e-49816a322db2
document_version_independent_id: 3bd47c41-6ac9-9835-727b-1bea435a3073
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/billing-extended-security-updates.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/billing-extended-security-updates
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/billing-extended-security-updates.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/fc3f72c2-fb6f-4cea-95ee-b444e52254ee
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f12cf087-582d-48ac-a085-0c19adf1e391
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: e62b0760-115d-1352-22df-415bdbc93a8d
---

# Billing service for Extended Security Updates for Windows Server through Azure Arc - Azure Arc | Microsoft Learn

Three factors affect billing for Extended Security Updates (ESUs):

- The number of cores provisioned
- The edition of the license (Standard vs. Datacenter)
- The application of any eligible discounts

Billing is monthly. Decrementing, deactivating, or deleting a license results in charges for up to five more calendar days from the time of decrement, deactivation, or deletion. Reduction in billing isn't immediate. This service bills through Azure and you can use it to decrement a customer's Microsoft Azure Consumption Commitment (MACC) and be eligible for Azure Consumption Discount (ACD).

Note

Licenses or extra cores provisioned after end of support are subject to a one-time back-billing charge during the month in which the license was provisioned. This charge isn't reflective of the recurring monthly bill.

## Back-billing for ESUs enabled by Azure Arc

When you provision licenses after the end of support (EOS) date, you pay back-billing charges for the time elapsed since the EOS date. When you enroll late, you become eligible for all the critical security patches up to that point, and the back-billing charge reflects the value of these critical security patches. The EOS date depends on the version of Windows Server.

::: zone pivot="windows-server-2012"

The EOS date for Windows Server 2012 and 2012 R2 is October 10, 2023. For example, an ESU license provisioned in December 2023 is back-billed for October and November upon provisioning.

The Windows Server 2012 and Windows Server 2012 R2 ESU period ends on October 13, 2026. The October 13, 2026 security update is the final update provided through ESUs. At midnight Coordinated Universal Time (UTC) on October 14, 2026, Windows Server 2012 ESU licenses enabled by Azure Arc are deactivated and stop providing update eligibility. Recurring billing ends as part of deactivation. Because reductions in billing aren't immediate, charges might continue for up to five calendar days after deactivation, consistent with the billing behavior described in this article.

Deactivated license resources remain available to view in Azure, but you can't use them to enroll more servers or receive security updates released after October 13, 2026. Plan to migrate your workloads or upgrade to a supported version of Windows Server before this date.

::: zone-end

::: zone pivot="windows-server-2016"

The EOS date for Windows Server 2016 is January 12, 2027. Licenses provisioned after that date are back-billed to January 12, 2027. Billing for Windows Server 2016 ESUs enabled by Azure Arc begins January 13, 2027.

::: zone-end

If you deactivate and then reactivate a license, you're billed for the window during which the license was deactivated. It's not possible to evade charges by deactivating a license before a critical security patch and reactivating it shortly before.

If the region or the tenant of an ESU license is changed, this change is subject to back-billing charges.

Note

The back-billing cost appears as a separate line item in invoicing. If you acquired a discount for your core Windows Server ESUs enabled by Azure Arc, the same discount might or might not apply to back-billing. Verify that the same discounting, if applicable, is applied to back-billing charges as well.

Estimates in the Azure Cost Management forecast might not accurately project monthly costs. Due to the episodic nature of back-billing charges, the projection of monthly costs might appear as overestimated during initial months.

## Billing associated with modifications to an Azure Arc ESU license

- **License type:** License type (either Standard or Datacenter) is an immutable property. The billing associated with a license is specific to the edition of the provisioned license.

    Note

    If you previously provisioned a Datacenter Virtual Core license, it's charged with and offer the virtualization benefits associated with the pricing of a Datacenter edition license.
- **Core modification:** If you add cores to an existing ESU license, you incur back-billing charges for the time elapsed since EOS. The new cores are regularly billed from the calendar month in which you added them. If you reduce or decrement cores to an existing ESU license, the billing rate reflects the reduced number of cores within five days of the change.
- **Activation:** Licenses are billed for their number and edition of cores from the point at which you activate them. The activated license doesn't need to be linked to any Azure Arc-enabled servers to initiate billing. Activation and reactivation are subject to back-billing. Licenses that you activated but didn't link to any servers might be back-billed if they weren't billed upon creation. You're responsible for deletion of any activated but unlinked ESU licenses.
- **Deactivation or deletion:** Licenses that you deactivate or delete are billed through up to five calendar days from the time of the change.

    Note

    If you delete and then recreate an ESU license, back-billing still applies for the corresponding period. Deletion doesn't exempt you from charges for that period.

    In principle, there are no cases in which back-billing is waived after reactivation or recreation, and there are no conditions under which it can be avoided.

    Before performing reactivation or recreation, always confirm the billing start date and the conditions under which back-billing will occur. Also, review the publicly available information on pricing calculations.

## Billing for transition scenario for Volume Licensing

::: zone pivot="windows-server-2012"

Licenses for Windows Server 2012/R2 ESUs enabled by Azure Arc that have been provisioned with the specification of an Invoice Id for the Year 1 Volume Licensing entitlement won't be charged until October 10, 2024. These licenses won't be back-billed to October 2023. Licenses with Year 1 created after October 10, 2024 will be back-billed to October 10, 2024, the last day of the Year 1 of WS2012/R2 ESU program. Customers don't need to reactivate or recreate licenses between years of the WS2012/R2 ESU program.

::: zone-end

::: zone pivot="windows-server-2016"

Transitioning from Volume Licensing isn't supported for Windows Server 2016 ESUs enabled by Azure Arc.

::: zone-end

## Services included with Windows Server ESUs enabled by Azure Arc

When you purchase Windows Server ESUs enabled by Azure Arc, you get access to more Azure management services at no extra cost for enrolled servers. To learn more, see [Access to Azure services](prepare-extended-security-updates#access-to-azure-services).

Azure Arc-enabled servers give you the flexibility to evaluate and operationalize Azure’s robust security, monitoring, and governance capabilities for your non-Azure infrastructure. These services deliver key value beyond the observability, ease of enrollment, and financial flexibility of Windows Server ESUs enabled by Azure Arc.