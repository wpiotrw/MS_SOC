---
layout: Conceptual
title: Checklist Microsoft Customer Agreement Billing Migration - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/microsoft-customer-agreement/checklist-microsoft-customer-agreement-billing-migration
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
description: This guide helps customers who sign a Microsoft Customer Agreement prepare their existing subscriptions for a billing migration.
author: CLodwigDocs
ms.service: cost-management-billing
ms.subservice: microsoft-customer-agreement
ms.topic: article
ms.date: 2026-10-30T00:00:00.0000000Z
ms.author: clodwig
ms.reviewer: clodwig
locale: en-us
document_id: 9f0e72c1-23c1-d62f-03f9-f4691a4bdb35
document_version_independent_id: 6d6d7da7-a0c8-4009-d4df-9a388754690c
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/microsoft-customer-agreement/checklist-microsoft-customer-agreement-billing-migration.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/microsoft-customer-agreement/checklist-microsoft-customer-agreement-billing-migration
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/microsoft-customer-agreement/checklist-microsoft-customer-agreement-billing-migration.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c0439c36-80e3-415f-8e4c-6951e3f1b136
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/2812d699-d85f-4a7f-839d-44e218b35d24
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
platformId: 5da62192-cfde-2ea9-cfbb-4a79b61fc26c
---

# Checklist Microsoft Customer Agreement Billing Migration - Microsoft Cost Management | Microsoft Learn

This article provides early guidance so customers can understand migration impact, confirm readiness, and prepare the required billing configuration for a smooth transition to the Microsoft Customer Agreement (MCA).

## Overview

Before migrating from an Enterprise Agreement (EA), Microsoft Customer Agreement (MCA), or pay-as-you-go subscriptions to a Microsoft Customer Agreement (MCA), review this checklist and follow the required steps to ensure a smooth transition. This checklist helps you:

- Validate readiness and dependencies
- Minimize post-migration issues
- Align stakeholders on required actions
- Top customer actions with MCA. [Learn More](https://www.microsoft.com/licensing/news/top_customer_actions_after_accepting_microsoft_customer_agreement?rtc=1)

## Validate contract and roles

Confirm access to both the source and the destination MCA as a Billing Account Owner.

- EA → MCA: Ensure EA Admin and MCA Billing Account Owner roles are assigned.
- Pay-as-you-go → MCA: Ensure a Global Admin for the pay-as-you-go subscription and MCA Billing Account Owner role.
- MCA → MCA: Confirm Billing Account Owner roles exist in both source and destination MCA billing accounts.[Learn More](/en-us/azure/cost-management-billing/manage/understand-mca-roles)

## No service downtime

Azure services in your subscription keep running without any interruption. We only transition the billing relationship for your Azure subscriptions. There are no changes to existing resources, resource groups, or management groups.

Note

Marketplace Private Offers are market specific. Subscriptions that are associated with Marketplace Private Offers may be blocked from transfer during a country/region change. This happens when the Private Offer is published for a specific market and isn't available in the destination market (EA–Sweden to MCA–United States). This mismatch results in a validation failure. The independent software vendor (ISV) defines market eligibility for a Private Offer at the time of offer publishing, and it can't be modified after the offer is accepted. To proceed with the subscription transfer to MCA, the existing Private Offer must be canceled and repurchased, if available in the target market.

## Download historical data

- Export historical cost and usage data before migration. Historical data doesn't transfer to MCA. We recommend that you save invoices and customer reports for compliance. [View and download Azure usage and charges - Microsoft Cost Management | Microsoft Learn](/en-us/azure/cost-management-billing/understand/download-azure-daily-usage)
- You can continue to view historical charges in the Azure portal under the source billing scope, depending on your billing roles:
    - EA → MCA: Historical charges remain visible in Cost Analysis after migration if you're an Enterprise Administrator or Department Administrator on the EA enrollment. Subscription ownership alone doesn't provide access to EA historical charges because subscription roles don't grant access to the EA billing scope.
    - MCA → MCA: Billing Account Owners and Billing Profile Owners/Contributors can continue to view all historical MCA charges in the Azure portal under the source MCA billing scope. Subscription owners without MCA billing roles can't access historical billing data because they don't have permissions to the MCA billing scope.
    - Pay-as-you-go → MCA: Subscription owners must download all historical invoices and usage data before the transfer, as this information is no longer accessible once the subscription is migrated.

## Review billing hierarchy changes

You use the billing account to manage billing for your Microsoft customer agreement.

- Understand the MCA structure: Billing Account → Billing Profile → Invoice Section → Subscription.
- Each billing profile generates a separate monthly invoice. For example, three billing profiles result in three monthly invoices.
- Map existing departments or subscriptions to MCA invoice sections.
- EA → MCA: You use an invoice section to organize your costs based on your needs, similar to departments in your Enterprise Agreement enrollment. Department becomes invoice sections and department administrators become owners of the respective invoice sections. Enterprise administrators become owners of the billing account and billing profile. [Learn More](/en-us/azure/cost-management-billing/manage/mca-setup-account#understand-changes-to-your-billing-hierarchy)

[![Diagram showing the structure of a Microsoft Customer Agreement.](media/onboard-microsoft-customer-agreement/microsoft-customer-agreement-billing-hierarchy.png)](media/onboard-microsoft-customer-agreement/microsoft-customer-agreement-billing-hierarchy.png#lightbox)

## Identify changes related to Savings Plans and Reservations

Before transferring Azure reservations or Savings Plans, check that the source agreement, destination agreement, and transfer method are supported in the [Azure product transfer hub](/en-us/azure/cost-management-billing/manage/subscription-transfer#product-transfer-support). Under MCA, Azure reservations and Savings Plans are priced in USD. Their billing currency can differ.

### Azure Savings Plan

The EA-to-MCA enrollment migration has Savings Plan outcomes that differ from individual product-transfer requests. During migration, a USD-priced Savings Plan moves to MCA and remains active. A non-USD-priced Savings Plan can't transfer directly as-is. To maintain coverage, choose automatic replacement during the transfer or, with Azure Support assistance, purchase a new MCA plan before requesting cancellation of the original EA plan. Automatic replacement creates a new one-year plan with monthly payments. The support-assisted replacement allows a new three-year plan. Both replacement plans are priced in USD with a new commitment term. The remaining EA plan term doesn't carry over. If you want a three-year plan after automatic replacement has created a one-year plan, contact Azure Support to request cancellation of that new MCA plan and purchase of a new three-year MCA plan. See the [Savings Plan migration guidance](/en-us/azure/cost-management-billing/manage/mca-setup-account#savings-plan-transfers-with-a-non-usd-billing-currency) for commitment and process details.

For reservation outcomes and Savings Plan outcomes in other supported transfer processes, review the [currency-change guidance in the Azure product transfer hub](/en-us/azure/cost-management-billing/manage/subscription-transfer#transfer-reservations-and-savings-plans-with-currency-change). Use the [EA-to-MCA migration guidance](/en-us/azure/cost-management-billing/manage/mca-setup-account#savings-plan-transfers-with-a-non-usd-billing-currency) for the migration process and Savings Plan details.

### Reservations

Confirm that your reservation transfer is supported in the product transfer support table. For a supported transfer, a pricing currency change alone doesn't change the payment schedule. If billing currency changes, a reservation with a monthly payment plan is canceled at its next scheduled payment; an upfront-paid reservation remains active. See the [reservation outcome matrix](/en-us/azure/cost-management-billing/manage/subscription-transfer#transfer-reservations-and-savings-plans-with-currency-change) for the complete guidance.

For cancellation and refund policies, see [Self-service exchanges and refunds for Azure Reservations](/en-us/azure/cost-management-billing/reservations/exchange-and-refund-azure-reservations). If you can't determine the impact on your reservations or savings plans, contact [Azure support](https://portal.azure.com/?#blade/Microsoft_Azure_Support/HelpAndSupportBlade) before transferring.

### Centrally managed SQL Azure Hybrid Benefit

If you use centrally managed SQL Server licenses with Azure Hybrid Benefit under an Enterprise Agreement (EA) and transition to an enterprise Microsoft Customer Agreement (MCA-E), the licenses don't automatically transfer. After migration, manually assign the licenses under the new agreement. For details, see [Complete Enterprise Agreement tasks in your billing account for a Microsoft Customer Agreement](/en-us/azure/cost-management-billing/manage/mca-setup-account#understand-changes-to-your-billing-hierarchy) and [Transition to centrally managed Azure Hybrid Benefit](/en-us/azure/cost-management-billing/scope-level/transition-existing).

## Cost management & reporting

- Recreate the following aspects under MCA:
    - Budgets [Learn More](/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets?tabs=psbudget)
    - Alerts [Learn More](/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets?tabs=psbudget#configure-actual-costs-budget-alerts)
    - Exports [Learn More](/en-us/azure/cost-management-billing/costs/tutorial-improved-exports)
    - Cost Allocation rules [Learn More](/en-us/azure/cost-management-billing/costs/allocate-costs)
    - Cost Management Custom/shared views
- Partner ID associations aren't copied over to the MCA during the billing transition. You must readd any partner ID associations manually after the transition. [Learn More](/en-us/partner-center/membership/link-partner-id-for-azure-performance-pal-dpor#link-to-a-partner-id-by-using-a-pal)
- Update Power BI connect:
    - Use Billing Profile ID instead of EA enrollment number. [Learn More](/en-us/power-bi/connect-data/desktop-connect-azure-cost-management)
- Management groups: Subscriptions in management groups under a Microsoft Customer Agreement aren't supported in Cost Management. Cost Management + Billing is managed with APIs, automation scripts, and Azure portal functionality. [Learn More](/en-us/azure/cost-management-billing/costs/understand-work-scopes#azure-rbac-scopes)
    - Cost Views: Rebuild dashboards and reports using the Billing Account ID, Billing Profile ID, or Invoice Sections ID instead of Management Group scope.
    - APIs: Update endpoints to align with MCA's billing structure.
    - Automation: Modify scripts that rely on Management Group-level scoping.

## API & automation updates

Replace legacy APIs with MCA APIs and updated billing properties. APIs & Automation need to be recreated in MCA.

- Update automation scripts for:
    - Update any programming code to replace EA API calls with MCA API calls. [Learn More](/en-us/azure/cost-management-billing/costs/migrate-cost-management-api)
    - Subscription vending
    - Automatic purchases
    - Third-party cost tools (Terraform, Azure Resource Manager, Bicep)

Note

EA and MCA API schemas differ. [Learn More](/en-us/azure/cost-management-billing/costs/migrate-cost-management-api#apis-to-get-cost-and-usage)

## Technical dependencies

- After you migrate to MCA, the transition is an evolutionary process involving both contractual and technical changes. As billing property IDs are updated, ensure all workloads are aligned with the new Billing Account ID, Billing Profile ID, and Invoice Section ID to maintain billing accuracy and business continuity.
- Check compatibility of dashboards (for example, Emissions Impact Dashboard) and update references to MCA billing scope.

## Invoice setup

- Changes in billing constructs

    - Getting started with MCA billing [Learn More](/en-us/azure/cost-management-billing/understand/mca-overview)
    - Organizing your invoice based on your business needs [Learn More](/en-us/azure/cost-management-billing/manage/mca-section-invoice)
- MCA change: Next day invoicing applies to Microsoft Marketplace products including SaaS (per license & flat rate), professional services, Azure managed app flat fees, Power BI visuals, and Dynamics 365 apps (Dataverse/Power Apps). [Learn more](/en-us/marketplace/billing-invoicing#next-day-invoicing-for-microsoft-customer-agreement-mca-customers)

## Payment setup

- MCA remit-to information differs from EA or pay-as-you-go. [Learn More](/en-us/azure/cost-management-billing/understand/pay-bill#wire-bank-details)
- Notify your accounts payable team.
- Create separate records for EA and MCA invoices.
- Expect a final invoice from the source and new monthly MCA invoices.
- For bank detail verification letters, e-invoicing, and third-party invoicing requirements, contact your Microsoft Account team.

**Pricing calculator role changes**

- After you transition to an MCA, access to negotiated pricing in the Azure Pricing Calculator is restricted to users with specific billing roles, and the permissions required differ from the permissions under an EA.
- Under MCA, users must have permissions at the billing profile level to view negotiated pricing.

    - Supported roles include:
    - Billing Profile Owner
    - Billing Profile Contributor
    - Billing Profile Reader
    - Invoice Manager

    Important

    Users without these roles see **retail pricing only** in the Azure Pricing Calculator.

## Tax and compliance

- Tax exemption certificates: If your account has a tax exemption certificate, create an Azure support request to associate it with your MCA account.
- Billing profile alignment and currency usage: The billing profile's sold-to and bill-to country/region must correspond to the MCA market country/region.

## Support plan

- Support plans don't transfer to MCA. You need to repurchase a Support Plan on your MCA.
- Cancel existing plans per contract terms, otherwise you continue to be billed until the end of your contract terms.
- Migration may affect Unified Support subscriptions. Contact your Microsoft Account Team.