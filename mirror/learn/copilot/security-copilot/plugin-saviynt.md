---
layout: Conceptual
title: Saviynt and  Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-saviynt
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the Saviynt plugin with Microsoft Security Copilot.
ms.date: 2025-08-25T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: concept-article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
ms.reviewer: shivanpatel
search.audiencetype: Admin
locale: en-us
document_id: 149135a6-9d67-0fb2-7fcb-70de65fc3a76
document_version_independent_id: 149135a6-9d67-0fb2-7fcb-70de65fc3a76
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-saviynt.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-saviynt
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-saviynt.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: e10152fe-6561-53b2-b2f7-ff4d82b33070
---

# Saviynt and  Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

Saviynt offers comprehensive insights into identity-related risks. You can use the Saviynt plugin with Microsoft Security Copilot to effectively enrich incidents and identify risky user access.

Some of the capabilities it provides include:

- Obtaining user profile details.
- Retrieving vendor or third-party organization details.
- Accessing comprehensive user access details across applications.
- Identifying dependencies of the access they possess.
- Checking if the identity holds privileged roles.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Prerequisites

Saviynt Identity Cloud API Access: Refer to [Saviynt API Reference](https://saviynt.com/api-reference) for details.

## Know before you begin

Integration with Security Copilot requires a bearer token for API access authorization. You'll need to take the following steps before using the plugin.

1. Follow the steps below to obtain the authorization token:

    1. Login to the Saviynt Tenant using your service account credentials.
    2. Navigate to **Admin &gt; Settings &gt; Webservice Auth Configuration**.
    3. Select **Generate Token**.
    4. Copy the value for the access\_token field in a safe place.

    Note

    Alternatively, you can use Postman to generate the authorization token using the {{url}}/ECM/api/login API. Refer to Saviynt's API documentation for more details.
2. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
3. Access **Manage Plugins** by selecting the **Sources** button from the prompt bar.
4. Next to **Saviynt**, select **Set up**.
5. In the Saviynt settings pane:

    - In the **InstanceURL** field, enter the Saviynt tenant URL (for example, "https://saviynttenant.saviyntcloud.com")
    - In the **Value** field, paste your access\_token, and then select **Save**.

## Sample Saviynt prompts

After the Saviynt plugin is configured, you can use the following capabilities with Security Copilot.

| Capability | Example prompts |
| --- | --- |
| Users | `Get user details for <First Name> <Last Name> using the search criteria FirstName and LastName``Get user details for <username>``Get risk associated with user <username>` |
| Organizations | `Get the organization details for <organization name>``Get a list of organizations that have not been certified for the last six months` |
| Dependent Entitlements | `Get dependent entitlements for "<entitlement name>" for <application>` |
| Access Details | `Get the access details for user <username>` |
| Saviynt Role details | `List the users who have access to Sav Role <Sav Role Name>` |

## Provide feedback

To provide feedback, contact [Saviynt](https://www.saviynt.com/).