---
layout: Conceptual
title: Cloud-native licensing and cost management with Azure Arc-enabled servers - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/cloud-native/licensing-cost-management
breadcrumb_path: ../../../breadcrumb/azure-management/toc.json
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
author: davidsmatlak
learn_banner_products:
- azure
ms.reviewer: davidsmatlak
ms.author: davidsmatlak
ms.service: azure-arc
ms.subservice: servers-azure-arc
description: Cloud-native licensing options for Azure Arc help reduce overhead of license management and ensure your servers have appropriate, up-to-date coverage.
ms.date: 2026-09-11T00:00:00.0000000Z
ms.topic: concept-article
locale: en-us
document_id: 0566c8b6-1e75-a11d-8f60-1fde05ee9c4c
document_version_independent_id: 7fc4c371-6339-e2d0-8a59-674d1e1a9121
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/cloud-native/licensing-cost-management.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: ../toc.json
asset_id: azure-arc/servers/cloud-native/licensing-cost-management
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/cloud-native/licensing-cost-management.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/fc3f72c2-fb6f-4cea-95ee-b444e52254ee
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f12cf087-582d-48ac-a085-0c19adf1e391
platformId: dd1c7250-cc1a-469f-b3a9-f43715b9a794
---

# Cloud-native licensing and cost management with Azure Arc-enabled servers - Azure Arc | Microsoft Learn

In a traditional setup, licensing for servers can be complex, especially in hybrid environments. Cloud-native licensing models for your Azure Arc-enabled servers provide flexibility and reduce overhead, so you can avoid buying perpetual licenses and doing annual true-ups for compliance. This shift lets you handle your Windows and SQL Server licensing like a cloud service: you only pay for what you use, when you use it, and you can manage it all centrally through Azure. For a system administrator, this means less time tracking license keys or entering activation codes, and more confidence that your servers are properly licensed and receiving critical updates.

Let's take a look at some of the licensing options enabled by Azure Arc.

## Windows Server pay-as-you-go

Historically, if you ran Windows Server on-premises, you activated it with a product key and that was that. By using Azure Arc, Microsoft introduced an alternative: [Windows Server pay-as-you-go licensing](/en-us/windows-server/get-started/windows-server-pay-as-you-go) via Azure.

Essentially, this model turns Windows Server into a subscription. Rather than worrying about buying new licenses for new servers, just connect them to Azure Arc and enable pay-as-you-go. This model is great for environments that fluctuate, or for avoiding large upfront costs. It also enables compliance, since Azure handles the metering.

With this licensing model, you connect your server to Azure Arc and [enable pay-as-you-go](/en-us/windows-server/get-started/windows-server-pay-as-you-go#set-up-windows-server-pay-as-you-go) in the Azure portal (or alternately, enable it when you install the OS and then connect to Azure Arc). The server then uses Azure for activation and billing, without requiring a product key. You see charges on your Azure bill per core, per hour for that server's OS license, similar to how Azure virtual machine (VM) pricing includes Windows licensing. If the server is shut down, you can stop billing by disabling the feature for that machine.

Pay-as-you-go is currently available for Windows Server 2025 and later, with the same pricing for Standard or Datacenter editions. Importantly, no client access licenses (CALs) are required for base functionality.

## Extended Security Updates (ESUs)

One of the pain points with older servers is figuring out what to do when they reach end of support. Windows Server 2012 and Windows Server 2012 R2 reached end of support on October 10, 2023, and Windows Server 2016 reaches end of support on January 12, 2027. Ensuring that these older servers keep getting critical security patches would normally mean purchasing separate [Extended Security Update (ESU)](/en-us/windows-server/get-started/extended-security-updates-overview) licenses for each server.

By [onboarding Windows Server 2012 or Windows Server 2016 machines to Azure Arc](/en-us/azure/azure-arc/servers/prepare-extended-security-updates) and signing up for ESUs in the Azure portal, you can receive security patches for up to three years after each version reaches end of support. For Windows Server 2012 and Windows Server 2012 R2, the ESU period ends on October 13, 2026, and the October 13, 2026, security update is the final update provided through ESUs. Migrate these workloads or upgrade to a supported version of Windows Server before the ESU period ends. You can configure Windows Server 2016 ESUs in the Azure portal starting August 3, 2026, and billing begins January 13, 2027. There's no need to install separate ESU product keys on each server; the Connected Machine agent enables the updates on each enrolled machine. Those servers then become eligible to receive ESU patches through your normal update tools, including Azure Update Manager.

Rather than requiring a lump sum purchase for the full period, ESUs enabled by Azure Arc are pay-as-you-go on a monthly basis. Charges are billed through Azure, so you can use existing Azure credits or commitments and use [Microsoft Cost Management and Billing](/en-us/azure/cost-management-billing/cost-management-billing-overview) to analyze your costs. The Azure portal also provides a central inventory of which servers are ESU-covered, letting you easily determine which servers aren't yet covered by ESUs.

## SQL Server pay-as-you-go

Like Windows, SQL Server traditionally requires buying per-core licenses or using your enterprise agreements. Azure Arc provides more flexible, modern licensing options. If you [connect your on-premises SQL Server instances to Azure Arc](/en-us/sql/sql-server/azure-arc/deployment-options), you have two licensing options: declare your existing license or use pay-as-you-go.

For organizations that prefer a consumption model, Azure Arc offers pay-as-you-go licensing for SQL Server 2012 and later. You pay hourly for the cores in use, so you save costs by avoiding full licensing charges. This consumption-based model is great for scenarios where you only run SQL at certain times or want to avoid a large upfront purchase.

Azure Arc provides flexibility to manage your SQL Server licensing. You can [transition from existing licenses to pay-as-you-go](/en-us/sql/sql-server/azure-arc/manage-pay-as-you-go-transition) as needed. You can even mix and match by keeping existing licenses for some SQL Server instances and using pay-as-you-go for others, and Azure tracks each appropriately. As a system administrator, you can monitor licensing compliance through Azure to get a comprehensive view of each server's licensing status.

## Centralized purchasing and FinOps

By shifting server licensing to Azure subscriptions, you can streamline procurement and improve compliance. Rather than buying licenses once and hoping they're used efficiently, pay-as-you-go means you pay exactly for what runs. If a server is decommissioned, the cost drops automatically. If you deploy an extra SQL Server instance for a week, you pay just for that week.

These processes align with FinOps (Cloud Financial Management) principles: turning software costs into measurable, adjustable cloud spend. It also means no more true-up surprise bills: everything is in your Azure invoice and can be analyzed with [Microsoft Cost Management and Billing](/en-us/azure/cost-management-billing/cost-management-billing-overview).

## Licensing and patching together

Another benefit of Azure Arc's license integration is how it ties into patch management. By using this integration, you can treat servers on down-level, unsupported OS versions just like supported ones in your patch cycles. Azure Arc takes care of making sure the updates flow for all servers. For example, when you enroll a Windows Server 2012 server in ESUs enabled by Azure Arc, Azure Update Manager knows that the server is eligible for patches and includes it in compliance reporting.

Similarly, for Windows Server pay-as-you-go, the Azure portal shows which Arc servers are using pay-as-you-go and are activated, so you don't accidentally let one slip unlicensed. It's a far more transparent and automated system compared to keeping a spreadsheet of product keys. By using this system, you can transform those annual licensing headaches into a simple "just check Azure" routine.