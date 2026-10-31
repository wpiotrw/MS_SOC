---
layout: Conceptual
title: Learn about Adaptive Protection in data loss prevention | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-adaptive-protection-learn
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-03-31T00:00:00.0000000Z
audience: ITPro
ms.topic: article
ms.service: purview
ms.subservice: purview-adaptive-protection
ms.collection:
- purview-compliance
search.appverid:
- MET150
description: Learn how insider risk management and data loss prevention work together to dynamically protect your organization from risky user activities.
ms.custom: sfi-ga-nochange
locale: en-us
document_id: 293eaa1c-34bd-e904-8c78-1d1c76f8739d
document_version_independent_id: 293eaa1c-34bd-e904-8c78-1d1c76f8739d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-adaptive-protection-learn.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-adaptive-protection-learn
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-adaptive-protection-learn.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
platformId: 09bc1c3a-212f-ddee-2727-83a702fb0076
---

# Learn about Adaptive Protection in data loss prevention | Microsoft Learn

Adaptive Protection in Microsoft Purview integrates Microsoft Purview Insider Risk Management with Microsoft Purview Data Loss Prevention (DLP). When insider risk identifies a user who is engaging in risky behavior, they are dynamically assigned to a inside risk level. Then Adaptive Protection can automatically create a DLP policy to help protect the organization against the risky behavior that's associated with that inside risk level. As users insider risk levels change in insider risk management, the DLP policies applied to users can adjust.

You can manually create DLP policies that help protect against risky behaviors that insider risk identifies too.

Refer to [Help dynamically mitigate risks with Adaptive Protection](insider-risk-management-adaptive-protection) to learn about Adaptive Protection and how to configure it.

## How Adaptive Protection shows up in DLP policies

If you're unfamiliar with DLP policies, you should review these articles before working with Adaptive Protection:

- [Learn about data loss prevention](dlp-learn-about-dlp)
- [Plan for data loss prevention (DLP)](dlp-overview-plan-for-dlp)
- [Data Loss Prevention policy reference](dlp-policy-reference)
- [Design a data loss prevention policy](dlp-policy-design)

Once Adaptive Protection is configured in insider risk, a condition called **User's risk level for Adaptive Protection is** will be available to use in rules that are configured for policies scoped to Exchange Online, Devices, and Teams locations.

The condition **Insider risk level for Adaptive Protection is** has three values:

- **Elevated risk level**
- **Moderate risk level**
- **Minor risk level**

These insider risk level profiles are defined in insider risk. You can select one, two or all three in a policy rule. Learn more about [insider risk levels](insider-risk-management-adaptive-protection#insider-risk-levels).

You can manually configure DLP policies that are part of Adaptive Protection and also use the [quick setup configuration in insider risk](insider-risk-management-adaptive-protection#quick-setup) to create DLP policies automatically from a template.

### Manual configuration

You manually configure an Adaptive Protection DLP policy just like you would [configure any other policy](dlp-create-deploy-policy). Just select the **Insider risk level for Adaptive Protection is** condition and the insider risk level profiles that you want, configure all the other policy options and deploy the policy according to your normal procedures.

### Quick setup configuration

If quick setup is used to configure Adaptive Protection in insider risk, DLP policies are created automatically, so you should be on the lookout for them. Quick setup will create one policy for Teams and Exchange Online with two rules, one for the elevated risk profile and one for the moderate and minor insider risk levels. It will also create one policy for Devices with two rules, one for the elevated risk profile and one for the moderate and minor insider risk levels.

Tip

Insider risk presents a view of just the DLP policies that use the **Insider risk level for Adaptive Protection is** condition. Open **Microsoft Purview portal** &gt; **Insider risk management** &gt; **Adaptive protection** to see the list. You'll need DLP to be in one of these roles to access the insider risk node:

> 
> - Compliance administrator
> - Compliance Data administrator
> - Organization management (Users who are not global administrators must be Exchange administrators to see and take action on devices that are managed by Basic Mobility and Security for Microsoft 365)
> - Global administrator
> - DLP compliance management
> - View-only DLP compliance management
> 

Important

Microsoft recommends that you use roles with the fewest permissions. This helps improve security for your organization. Global Administrator is a highly privileged role that should only be used in scenarios where a lesser privileged role can't be used.

#### Policy values for Teams and Exchange online DLP policy

This is the configuration for the Teams and Exchange DLP policy created during Quick Setup. The policy name is **Adaptive Protection policy for Teams and Exchange DLP**.

##### Rule: Adaptive Protection block rule for Teams and Exchange DLP

| DLP policy element | Configured value |
| --- | --- |
| Conditions | **Insider risk level for Adaptive Protection is**- **Elevated Risk Level** AND - **Content is Shared from Microsoft 365 With people outside my organization** |
| Actions | **Restrict access or encrypt the content in Microsoft 365 locations**- **Block only people outside your organization** |
| User Notification | **On**- **Notify user with a policy tip**– **Notify the user who sent, shared, or last modified the content** |
| User Override | **Off** |
| Incident reports | **On**- **Severity Level – Low**- **Send alert every time an activity matches the rule** |
| Additional Options | **Off** |
| Status | **Run the policy in simulation mode**- **Policy Tips** not selected |

##### Rule: Adaptive Protection audit rule for Teams and Exchange DLP

| DLP policy element | Configured value |
| --- | --- |
| Conditions | **Insider risk level for Adaptive Protection is**- **Moderate Risk Level, Minor Risk Level** AND - **Content is Shared from Microsoft 365 With people outside my organization** |
| Actions | None |
| User Notification | **On**- **Notify user with a policy tip**- **Notify the user who sent, shared, or last modified the content** |
| User Override | **Off** |
| Incident reports | **On**- **Severity Level – Low**- **Send alert every time an activity matches the rule** |
| Additional Options | **Off** |
| Status | **Run the policy in simulation mode**- **Policy tips** not selected |

#### Policy values for Devices DLP policy

This is the configuration for the Devices DLP policy created during Quick Setup. The policy name is **Adaptive Protection policy for Endpoint DLP**.

Important

For Adaptive Protection to work on Devices, you must either enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) or if you are manually creating the Adaptive Protection policy, select the **File Type is** condition.

Important

If a user is targeted by a default Adaptive Protection Device DLP policy and is targeted by an independent Device DLP policy, only the actions of the *most restrictive* policy will be applied.

##### Rule: Adaptive Protection block rule for Endpoint DLP

| DLP policy element | Configured value |
| --- | --- |
| Conditions | **Insider risk level for Adaptive Protection is**- **Elevated Risk Level** AND - **File Type is**- **Word processing**- **Spreadsheet**- **Presentation**- **Archive**- **Mail** |
| Actions | **Audit or Restrict activities on Devices**- **Upload to a restricted cloud service domain or access from unallowed browsers - Block** **File activities for all apps**- **Apply restrictions to specific activity**- **Copy to clipboard – Block**- **Copy to removable USB device – Block**- **Copy to network share – Block**- **Print – Block** **Restricted App activities - Access by restricted apps - Block** |
| User Notification | **Off** |
| User Override | **Off** |
| Incident reports | **On**- **Severity Level – Low**- **Send alert every time an activity matches the rule** |
| Additional Options | **Off** |
| Status | **Run the policy in simulation mode**- **Policy Tips** option not selected |

##### Rule: Adaptive Protection rule for Endpoint DLP

| DLP policy element | Configured value |
| --- | --- |
| Conditions | **Insider risk level for Adaptive Protection is**- **Moderate Risk Level, Minor Risk Level** AND - **File Type is**- **Word processing**- **Spreadsheet**- **Presentation**- **Archive**- **Mail** |
| Actions | **Audit or Restrict activities on Devices**- **Upload to a restricted cloud service domain or access from unallowed browsers – Audit** **File activities for all apps**- **Apply restrictions to specific activity**- **Copy to clipboard – Audit**- **Copy to removable USB device – Audit**- **Copy to network share – Audit**-**Print – Audit** **Restricted App activities**- **Access by restricted apps - Audit** |
| User Notification | **Off** |
| User Override | **Off** |
| Incident reports | **On**- **Severity Level – Low**- **Send alert every time an activity matches the rule** |
| Additional Options | **Off** |
| Status | **Run the policy in simulation mode**- **Policy tips** option not selected |