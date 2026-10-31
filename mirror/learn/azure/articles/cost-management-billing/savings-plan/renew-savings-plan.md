---
layout: Conceptual
title: Automatically renew your savings plan - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/renew-savings-plan
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
description: Learn how you can automatically renew a savings plan to continue getting discounts.
author: nwokolo
ms.reviewer: onwokolo
ms.service: cost-management-billing
ms.subservice: savings-plan
ms.topic: how-to
ms.date: 2026-10-29T00:00:00.0000000Z
ms.author: onwokolo
locale: en-us
document_id: cd474b53-be47-7a62-941c-c548f5e80cde
document_version_independent_id: 450dc6f0-ceef-810b-1b24-95ee541a3644
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/savings-plan/renew-savings-plan.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/savings-plan/renew-savings-plan
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/savings-plan/renew-savings-plan.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 49a7a046-6317-08bd-0288-8b4b9bef0380
---

# Automatically renew your savings plan - Microsoft Cost Management | Microsoft Learn

You can automatically purchase a replacement savings plan when an existing savings plan expires. Automatic renewal lets you continue receiving savings plan discounts without closely monitoring the expiration date. The renewal setting is turned off by default. To enable or disable renewal before the existing plan expires, select your savings plan under **Savings plans** in the Azure portal, and then go to the renewal settings. Renewing a savings plan creates a new savings plan when the existing one expires. It doesn't extend the term of the existing savings plan.

## Required renewal permissions

The following permissions are required to renew a savings plan:

Billing admin for Enterprise Agreements (EA) and Microsoft Customer Agreements (MCA):

- You must be either a billing profile owner or billing profile contributor for an MCA account.
- You must be an EA administrator with write access to an EA account.
- You must be a Savings plan purchaser.

For Microsoft Partner Agreements (MPA):

- You must be an owner of the existing savings plan.
- You must be an owner of the subscription.

## Set up renewal

In the Azure portal, search for **Savings plan** and select it.

1. Select the savings plan.
2. Select **Renewal**.
3. Select **Automatically renew this savings plan**.

## If you don't automatically renew

Your services continue to run normally. You're charged pay-as-you-go rates for your usage after the savings plan expires. You can't renew an expired savings plan - to continue to receive savings, you can buy a new savings plan.

## Default renewal settings

By default, the renewal inherits all properties except the automatic renewal setting from the expiring savings plan. A savings plan renewal purchase has the same billing subscription, term, billing frequency, and savings plan commitment. The new savings plan also inherits the scope setting. However, you can explicitly set the hourly commitment, billing frequency, and commitment term to optimize your savings. To view current rates and discounts, select your savings plan under **Savings plans** in the Azure portal.

## When the new savings plan is purchased

A new savings plan is purchased when the existing savings plan expires. Azure attempts to prevent any gap between the two savings plans. This continuity helps keep your costs predictable and your discounts uninterrupted.

## Change parent savings plan after setting renewal

If you make any of the following changes to the expiring savings plan, the savings plan renewal is canceled:

- Transferring the savings plan from one account to another
- Renewing the enrollment

## New savings plan permissions

Azure copies the permissions from the expiring savings plan to the new savings plan. Additionally, the subscription account administrator of the savings plan purchase has access to the new savings plan.

## Potential renewal problems

Azure may not process the renewal if:

- Payment can't be collected
- A system error occurs during renewal
- The EA agreement is renewed into a different EA

You'll receive an email notification if any of the preceding conditions occur, and the renewal is deactivated.

## Renewal notification

Renewal notification emails are sent 30 days before expiration and again on the expiration date. The sending email address is `azure-noreply@microsoft.com`. You might want to add the email address to your safe senders or allowlist.

Emails are sent to different people depending on your purchase method:

- EA customers - Emails are sent to the notification contacts set in the Azure portal or Enterprise Administrators who are automatically enrolled to receive usage notifications.
- MPA - No email notifications are currently sent for Microsoft Partner Agreement subscriptions.

## Need help? Contact us.

If you have savings plan questions, contact your account team or [create a support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest). Currently, Microsoft provides expert support for savings plans only in English.