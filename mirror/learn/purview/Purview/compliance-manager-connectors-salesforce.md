---
layout: Conceptual
title: Salesforce connector setup for Microsoft Purview Compliance Manager | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/compliance-manager-connectors-salesforce
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2025-02-24T00:00:00.0000000Z
audience: Admin
ms.topic: install-set-up-deploy
ms.service: purview
ms.subservice: purview-compliance-manager
ms.collection:
- purview-compliance
- m365solution-compliancemanager
- m365initiative-compliance
search.appverid:
- MOE150
- MET150
description: Configure settings in your Salesforce accounts in order to activate connectors for Microsoft Purview Compliance Manager.
locale: en-us
document_id: 1f1ab6b0-38bf-2151-a4e4-8ec76dd93d89
document_version_independent_id: 1f1ab6b0-38bf-2151-a4e4-8ec76dd93d89
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/compliance-manager-connectors-salesforce.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: compliance-manager-connectors-salesforce
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/compliance-manager-connectors-salesforce.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/eab1aabc-e18c-405b-ac29-e35eb0b15e3b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/574d2eb1-e22a-49c0-b4eb-64e86dbeee6b
platformId: c5d969a6-5d28-f57d-b5dd-062d209b16c3
---

# Salesforce connector setup for Microsoft Purview Compliance Manager | Microsoft Learn

Follow the instructions on this page to enable the connection between your Salesforce account and the Compliance Manager connector for Salesforce.

This process involves obtaining a token for a given Salesforce account. Therefore, if you activate multiple connectors for multiple Salesforce accounts, you'll need to repeat this process for each account in order to get the token.

## Setup steps

1. Sign in to your Salesforce account with your credentials.
2. Go to your account **Settings** and select **Reset My Security Token**. This can be done by any user.
3. Select **Reset Security** to get a new security token sent to your email.

    Important

    If the security token for your account is used anywhere else, resetting the token may cause issues in those locations.
4. Activate connector in Compliance Manager. When you activate a Salesforce connector in Compliance Manager, you'll provide your **Username**, **Password**, and **Security token**. Once you validate the connection during the connector activation process, you're all set up and ready to begin using the connector. Get details at [Working with connectors in Compliance Manager](compliance-manager-connectors).