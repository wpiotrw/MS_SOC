---
layout: Conceptual
title: Collection policies policy reference | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/collection-policies-policy-reference
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords: CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-11-12T00:00:00.0000000Z
audience: Admin
ms.topic: reference
ms.service: purview
ms.subservice: purview-collection-policies
search.appverid:
- MET150
- SPO160
ms.collection:
- highpri
- purview-compliance
- SPO_Content
recommendations: false
description: Collection policy component and configuration reference. This article provides a detailed anatomy of a collection policy.
ms.custom: seo-marvel-apr2021
ai-usage: ai-assisted
locale: en-us
document_id: b19a59e1-37c5-1732-ccd8-d8d35dbd3cf7
document_version_independent_id: b19a59e1-37c5-1732-ccd8-d8d35dbd3cf7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/collection-policies-policy-reference.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: collection-policies-policy-reference
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/collection-policies-policy-reference.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: c7420f63-d166-d06a-8710-0a772b8ebe5c
---

# Collection policies policy reference | Microsoft Learn

Microsoft Purview collection policies have many components to configure. To create an effective policy, you need to understand the purpose of each component and how its configuration alters the behavior of the policy. This article provides a detailed anatomy of a collection policy.

## Before you begin

If you're new to collection policies, here's a list of the core articles you need as you implement them in your organization:

1. [Collection Policies solution overview](collection-policies-solution-overview)
2. [Collection policy reference](collection-policies-policy-reference) - this article that you're reading now introduces all the components of a DLP policy and how each one influences the behavior of a policy
3. [Create and Deploy collection policies](collection-policies-create-deploy-policy).

## Conditions

Specify conditions to define what **data to detect**. Conditions are optional, but some might be required for other settings. If you don't add conditions, what gets detected depends on the data sources you select later:

- **Devices**: All data is detected, even if it doesn't match your organization's classifiers.
- **All other data sources**: Only data that matches your organization's classifiers is detected.

Collection policies support five conditions:

| Condition | More information |
| --- | --- |
| **Content contains classifiers** | [Sensitive information types](sit-sensitive-information-type-learn-about) and [trainable classifiers](trainable-classifiers-learn-about) to detect. Can be scoped to all classifiers, all classifiers except selected ones, or specific classifiers. The devices data source *doesn't support trainable classifiers*. If you select one, it's ignored. |
| **Content contains sensitivity labels** | [Sensitivity labels](sensitivity-labels) to scope detection to items with specific sensitivity labels applied. Only supported with browser and network cloud apps detection. |
| **Document size equals or is greater than** | Detect files with a size that is greater than a specified number of bytes, kilobytes (KB), megabytes (MB), gigabytes (GB), or terabytes (TB). |
| **Document is equal to or smaller than** | Detect files with a size that is smaller than a specified number of bytes, kilobytes (KB), megabytes (MB), gigabytes (GB), or terabytes (TB). |
| **File extension is** | Detect files with specified file extensions. |

## Activities

Choose which **activities to detect**. Supported activities are specific to the data sources you want to include.

Tip

You can mix activities that support different data sources in a single policy, but you must add all applicable data sources to the policy to support the selected activities.

| Activity | Description | Data source |
| --- | --- | --- |
| **Text sent to or shared with cloud or AI app** | When raw text is uploaded to a cloud app, including generative AI prompts, form submissions, and messages | - Cloud apps- Generative AI |
| **File uploaded to or shared with cloud or AI app** | When a binary file is uploaded to a cloud app or generative AI services | - Cloud apps- Generative AI |
| **Text received from cloud or AI app** | When raw text is downloaded from a cloud app, including generative AI responses | - Cloud apps- Generative AI |
| **File downloaded from cloud or AI app** | When a binary file is downloaded from a cloud app or generative AI service | - Cloud apps- Generative AI |
| **Archive created** | When an archive file is created on an onboarded endpoint device | Devices |
| **File accessed by unallowed app** | When a file is accessed by a [restricted app or app group](dlp-configure-endpoint-settings#restricted-apps-and-app-groups) on an onboarded endpoint device | Devices |
| **File archived** | When a file is added to an archive on an onboarded endpoint device | Devices |
| **File copied to network share** | When a file is copied to a network share on an onboarded endpoint device | Devices |
| **File copied to remote desktop session** | When a file is copied to a remote computer through a remote desktop session on an onboarded endpoint device | Devices |
| **File copied to removable media** | When a file is copied to a removable media, such as a USB flash drive, on an onboarded endpoint device | Devices |
| **File created** | When a file is created on an onboarded endpoint device | Devices |
| **File created on network share** | When a file is created on a network share from an onboarded endpoint device | Devices |
| **File created on removable media** | When a file is created on removable media, such as a USB flash drive, from an onboarded endpoint device | Devices |
| **File deleted** | When a file is deleted from an onboarded endpoint device | Devices |
| **File modified** | When a file is modified from an onboarded endpoint device | Devices |
| **File printed** | When a file is printed from an onboarded endpoint device | Devices |
| **File read** | When a file is read from an onboarded endpoint device | Devices |
| **File renamed** | When a file is renamed from an onboarded endpoint device | Devices |
| **File transferred by Bluetooth** | When a file is transferred by Bluetooth from an onboarded endpoint device | Devices |
| **File uploaded to cloud** | When a file is uploaded to the cloud from an onboarded endpoint device | Devices |
| **Removable media mount** | When removable media, such as a USB flash drive, is mounted on an onboarded endpoint device | Devices |
| **Removable media unmount** | When removable media, such as a USB flash drive, is unmounted on an onboarded endpoint device | Devices |

## Data sources

Data sources define **where to apply** the policy, and directly correlate to the activities added to the policy.

The following data sources are supported:

| Data source | More information | Supported activities |
| --- | --- | --- |
| **Devices** | Devices [onboarded to Microsoft 365](device-onboarding-overview) and managed by your org. | Windows devices [onboarded into Microsoft 365](device-onboarding-overview). |
| **Copilot experiences** | Includes Copilot in Microsoft Fabric and Microsoft Security Copilot only, with support for more experiences coming soon. | - Text sent to or shared with cloud or AI app- Text received from cloud or AI app |
| **Enterprise AI** | Non-Copilot AI apps that are onboarded or connected to your org by using methods like Microsoft Entra registration, Microsoft Foundry, or Microsoft Purview Data Map connectors. Policies can be applied to all Enterprise AI apps or scoped to specific apps. | - Text sent to or shared with cloud or AI app- Text received from cloud or AI app |
| **Unmanaged cloud apps** | Cloud apps sourced in the Defender for Cloud Apps catalog that aren't set up for single sign-on (SSO), allowing users to access personal data through a browser, app, add-in, or API. Policies only detect data while its being shared or transferred (data in motion) via browser and network detection. | **Browser & Network**:- Text sent to or shared with cloud or AI app- File uploaded to or shared with cloud or AI app**Network only**:- Text received from cloud or AI app-File downloaded from cloud or AI app |
| **Adaptive app scopes** | Groups of apps, whose membership is determined based on app metadata, such as category. Currently only "All unmanaged AI apps" - unmanaged cloud apps categorized as generative AI - is supported via browser and network detection. | **Browser & Network**:- Text sent to or shared with cloud or AI app- File uploaded to or shared with cloud or AI app**Network only**:- Text received from cloud or AI app-File downloaded from cloud or AI app |

Note

Some unmanaged AI apps aren't supported in Edge for Business. Adaptive app scopes apply only to the supported unmanaged apps in Edge for Business. To learn more, see [Learn more about which apps are supported](/en-us/purview/dlp-browser-dlp-learn).

### Scoping data sources to users and groups

For each data source, you can choose to scope by:

- **All** users and groups (default)
- **Specific** users and groups
- **All except** specific users and groups

Note

Excluded users and groups take precedence over any included users or groups.

## Other collection policy settings

Depending on the conditions, activities, and data sources you specify, you might need to configure other collection policy settings. When these settings are disabled or grayed out, the policy configuration isn't compatible with the setting.

### Content capture for AI interactions

To help comply with regulatory requirements, you can decide whether to capture and store all detected prompts and responses from any generative AI data sources you add to the policy. This feature is called *content capture*. By using this feature, you can easily discover and protect the captured content later by using other Microsoft Purview policies and solutions. This capability doesn't include content in files shared with generative AI, and only applies to the following data sources:

- Copilot experiences
- Enterprise AI
- Unmanaged cloud apps categorized as generative AI
- All unmanaged AI apps adaptive app scope

Without this setting enabled, content detected in prompts and responses is limited to sensitive information only.

Note

To capture AI content, you must set the **Content contains classifiers** condition to `All`.

### Cloud apps detection

If you add unmanaged cloud apps or adaptive app scopes data sources to the policy, including generative AI, you must choose how to detect this data. You can choose from the following options:

- **Browser** - Detect sensitive data shared with unmanaged cloud apps through the Microsoft Edge browser when on Intune-managed work devices. See [supported unmanaged apps](dlp-browser-dlp-learn#unmanaged-cloud-apps) that can be targeted in policies, see [supported activities](dlp-browser-dlp-learn#activities-you-can-monitor-and-take-action-on) for what user activities can be captured, and see [supported browsers](dlp-browser-dlp-learn#supported-browsers) to confirm your version of the Microsoft Edge browser supports browser detection.
- **Network** - Detect sensitive data shared with unmanaged cloud apps through browsers, apps, APIs, and more, by using an integrated Secure Service Edge (SSE) provider and [Microsoft Purview network data security](dlp-network-data-security-learn).

Important

Microsoft Purview browser and network data security policies don't apply to B2B guest users.

#### Considerations for unmanaged cloud apps policies

Review this information when you configure policies that include unmanaged cloud apps, or when you troubleshoot unexpected policy behavior:

- - When multiple catalog entries exist for the same app with differences in the entry name (for example, QwenAI and Qwen Chat), include all entries for the app to avoid unintended coverage gaps.
- Some unmanaged AI apps like ChatGPT, Runway and Meta AI might intermittently send content in encoded form or through dynamically generated endpoints, which can impact policy enforcement.
- Policies that target unmanaged apps can capture interactions from both the consumer and enterprise versions of an app when the app's URL is shared across instances (for example, ChatGPT consumer and ChatGPT enterprise).
- When you target an unmanaged cloud app in an Edge for Business browser policy, detection is based on the destination app's traffic, which isn't always exactly the same as the originating app.
- Inline evaluation size limits: Microsoft Purview evaluates up to 4 MB of content for uploadText and downloadText, and files up to 3 MB for uploadFile and downloadFile.

Note

The unmanaged cloud app features only apply to the consumer version of Microsoft 365 Copilot. For more information on the enterprise version and available Purview features see, [Learn more about Microsoft 365 Copilot Enterprise protections](/en-us/copilot/microsoft-365/enterprise-data-protection).

### Next steps

After creating a collection policy, you might need to take additional steps depending on the configured settings.

- If you enable **Browser** detection, the Microsoft Edge management service automatically creates the required configuration policies to activate collection policies in Edge for Business. To learn more, see [Activate your Microsoft Purview policy in Microsoft Edge](/en-us/deployedge/microsoft-edge-dlp-purview-configuration).
- If you enable **Network** detection, you must add and configure one or more Secure Access Service Edge (SASE) or non-Microsoft secure enterprise browser integrations to begin detecting network traffic. To learn more, see [SASE provider integrations](collection-policies-create-deploy-policy#sase-provider-integration).

Important

If the [automatic behaviors](/en-us/deployedge/microsoft-edge-dlp-purview-configuration) fail to sync for browser detection, Microsoft Purview shows an error message and policies aren't applied in Edge for Business. An admin with the [required permissions](/en-us/purview/dlp-browser-dlp-learn#unmanaged-cloud-apps) must resync to resolve the error. For more information, see [activate your Microsoft Purview policy in Microsoft Edge](/en-us/deployedge/microsoft-edge-dlp-purview-configuration).

## Pay-as-you-go features

Some collection policy data sources and features are pay-as-you-go and require an Azure subscription to be linked before creating a policy. [Learn more about Microsoft Purview features that use pay-as-you-go-billing here.](purview-billing-models).

- Copilot experiences
- Enterprise AI
- Unmanaged cloud app activity detected through non-Microsoft SASE and secure enterprise browser integrations via [Microsoft Purview network data security](dlp-network-data-security-learn)
    - Microsoft Entra Global Secure Access integration with Purview network data security is licensed per seat and does not require pay-as-you-go. For more information, see [Learn about Microsoft Purview Network Data Security](dlp-network-data-security-learn#licensing).
- Unmanaged cloud app activity detected through [Microsoft Purview policies using inline data protections for the browser](dlp-browser-dlp-learn).

## Privacy notice for Enterprise AI and Network Data Security

Enterprise AI data sources and network data security integrations might require integration with a third-party app or provider. If you choose to enable any third-party integration, it gains access to and might store some policy configuration, including user identifiers. In this case, the third party's terms, conditions, and privacy policy govern the usage and storage of this data.