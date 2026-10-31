---
layout: Conceptual
title: Considerations for deploying Microsoft Purview Data Security Posture Management (DSPM) for AI | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dspm-for-ai-considerations
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: helenachen-microsoft
ms.service: purview
ms.subservice: purview-data-security-posture-management
ms.date: 2026-05-01T00:00:00.0000000Z
ms.update-cycle: 180-days
audience: Admin
ms.topic: reference
ms.collection:
- highpri
- m365copilot
- msec-ai-copilot
description: Learn about deployment details for Microsoft Purview Data Security Posture Management for AI.
locale: en-us
document_id: 7045f0c5-f018-9560-8696-c1a79dc3fcc8
document_version_independent_id: 7045f0c5-f018-9560-8696-c1a79dc3fcc8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dspm-for-ai-considerations.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dspm-for-ai-considerations
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dspm-for-ai-considerations.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
platformId: e77a62c7-d28d-2378-e0e1-4d0d88a897e0
---

# Considerations for deploying Microsoft Purview Data Security Posture Management (DSPM) for AI | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Note

This article is for the **classic** version of Data Security Posture Management for AI that's now replaced with a new version that incorporates support for AI apps and agents, new features and broader reach, with simplified management.

These improvements won't be added to this classic version so we invite you to try the new [Data Security Posture Management](data-security-posture-management-learn-about).

For the most part, Data Security Posture Management for AI is easy to use and self-explanatory, guiding you through prerequisites and preconfigured reports and policies. Use this section to complement that information and provide additional details that you might need.

## Prerequisites for Data Security Posture Management for AI

To use Data Security Posture Management for AI from the Microsoft Purview portal, you must have the following prerequisites:

- You have the [right permissions](ai-microsoft-purview-permissions).
- Required for monitoring interactions with Copilot and agents:

    - Microsoft Purview auditing is enabled for your organization. Although this is the default, you might want to check the instructions for [Turn auditing on or off](audit-log-enable-disable).
    - For Microsoft 365 Copilot and agents, users are [assigned a license for Microsoft 365 Copilot](/en-us/microsoft-365-copilot/microsoft-365-copilot-enable-users#assign-licenses).
    - For Copilot in Fabric and Security Copilot:

        - The [enterprise version of Microsoft Purview data governance](data-governance-free-version-upgrade-to-enterprise), to support the required APIs.
        - A collection policy, such as the one created from the recommendation or remediation action **Secure interactions for Microsoft Copilot experiences**.
- Required for monitoring interactions and applying DLP policies to other AI apps in Edge:

    - An Edge configuration policy is required to activate the Microsoft Purview integration in Edge. For configuration information, see [Activate your DLP policy in Microsoft Edge](/en-us/deployedge/microsoft-edge-dlp-purview-configuration).
- Required for monitoring interactions with third-party generative AI sites:

    - Devices are [onboarded to Microsoft Purview](device-onboarding-overview), required for:

        - Gaining visibility into sensitive information that's shared with third-party generative AI sites. For example, a user pastes credit card numbers into ChatGPT.
        - Applying endpoint DLP policies to warn or block users from sharing sensitive information with third-party generative AI sites. For example, a user identified as elevated risk in Adaptive Protection is blocked with the option to override when they paste credit card numbers into ChatGPT.
    - The [Microsoft Purview browser extension](insider-risk-management-browser-support#configure-browser-signal-detection-for-microsoft-edge) is deployed to Windows users and required to discover visits to third-party generative AI sites by using an Insider Risk Management policy. The browser extension is also required for Endpoint DLP policies on Windows when you use Chrome.
- For [Entra-registered AI apps](ai-entra-registered), they are [integrated with the Microsoft Purview SDK](/en-us/purview/developer) to support all the Microsoft Purview capabilities.
- For AI apps other than Microsoft 365 Copilot and Microsoft Facilitator, you've set up [pay-as-you-go billing](purview-billing-models) for your organization. When this billing model is applicable for specific configurations, you'll see notifications and instructions in the UI.

You'll find more information about the prerequisites for auditing, device onboarding, and the browser extension in Data Security Posture Management for AI: Navigate to **Overview** &gt; **Get started** section.

For a list of currently supported third-party AI apps, see [Supported AI sites by Microsoft Purview for data security and compliance protections](ai-microsoft-purview-supported-sites).

Note

If you're using [administrative units](purview-admin-units), restricted administrators won't be able to create the one-click policies that apply to all users. You must be an unrestricted administrator to create these policies. Restricted administrators see the results only for users in their assigned administrative unit for the **Policies** page, and in the reports and activity explorer in Microsoft Purview Data Security Posture Management for AI.

## Prerequisites for Fabric data risk assessments

Use the following instructions to meet the prerequisites to run data risk assessments for Fabric workspaces, and [before you select **Set config** in DSPM for AI](dspm-for-ai?tabs=fabric#data-assessments).

For steps 1 and 2, use one of the following [Entra roles for the required permissions](/en-us/entra/identity/role-based-access-control/permissions-reference):

- Cloud Application Administrator
- Application Administrator
- Privileged Role Administrator

For step 3, you must be a [Fabric administrator](/en-us/fabric/admin/roles).

1. In the Microsoft Entra admin portal, [create and configure a registered app](/en-us/entra/identity-platform/howto-create-service-principal-portal) to be the service principal authentication for Fabric. You will authenticate the app in one of two ways: With **Federated Credentials** (recommended) or **Client Secret**. The federated credentials option is more secure because it lets Kubernetes workloads authenticate to Azure services without hard‑coding secrets, while ensuring each pod only has the permissions it needs. For more information about this authentication method, see [Overview of federated identity credentials in Microsoft Entra ID](/en-us/graph/api/resources/federatedidentitycredentials-overview).

    After you've created this registered app and still in the Entra admin portal, copy and store the **Application (client) ID**, which is always required to setup data risk assessments for Fabric. Then, to authenticate with federated credentials, work with your compliance administrator to identify and enter the **OIDC Issuer URL**, **Namespace**, and **Service Account Name** under **Edit connection**. Enter these values into the corresponding fields in **Your App name** &gt; **Certificates & Secrets** &gt; **Federated Credentials** &gt; **Kubernetes accessing Azure resources**. Alternatively, to authenticate with a client secret, store the **Client Secret** value to then enter in the Microsoft Purview portal:

    - To locate the **Application (client) ID**: In the Microsoft Entra admin portal, **Identity** &gt; **Applications** &gt; **App registrations**, select the app you created for Fabric. The **Application (client) ID** is displayed on the **Overview** tab.
    - [Create a client secret for this app](/en-us/entra/identity-platform/howto-create-service-principal-portal#option-3-create-a-new-client-secret). Copy and securely save the value immediately. It will only be shown once.
2. Now navigate to **Groups** to add the registered app as a group member to a new or existing security group. Its type displays as **Enterprise application**.
3. In the Fabric admin portal, navigate to **Tenant settings** &gt; **Admin API settings** and enable the options **Service principals can access read-only admin APIs** and **Service principals can access admin APIs used for updates**. For both of these, in the **Apply to:** sections, select **Specific security groups** and specify the security group that you configured in the previous step. Select **Apply** to save and apply these tenant settings.

For more information about steps 1-2, see [Enable service principal authentication for admin APIs](/en-us/fabric/admin/enable-service-principal-admin-apis).

For more information about the tenant settings and support for information protection in Fabric, see [Tenant settings index](/en-us/fabric/admin/tenant-settings-index) and [Information protection in Microsoft Fabric](/en-us/fabric/governance/information-protection).

## Prerequisites for Microsoft 365 item-level scanning for data risk assessments

Use the following instructions to create an Entra application with the required permissions for Microsoft 365 item-level scanning in a custom data risk assessment.

You must have one of the following [Entra roles to create and configure the required registered app](/en-us/entra/identity/role-based-access-control/permissions-reference):

- Cloud Application Administrator
- Application Administrator
- Privileged Role Administrator

In the Entra admin portal, [create and configure a registered app](/en-us/entra/identity-platform/howto-create-service-principal-portal) with the following settings:

- **Supported account types**: **Accounts in this organizational directory only**
- **API permissions**: **Microsoft APIs** &gt; **Microsoft Graph** &gt; **Application permissions**

    - **Application: Application.Read.All**
    - **Directory: Directory.Read.All**
    - **Files: Files.ReadWrite.All**
    - **SensitivityLabels: SensitivityLabels.Read.All**
    - **Sites: Sites.ReadWrite.All**
    - **User: User.Read.All**
- Grant admin consent for your tenant

Now [create a client secret for this app](/en-us/entra/identity-platform/howto-create-service-principal-portal#option-3-create-a-new-client-secret). Copy and securely save the value immediately. It will only be shown once.

You'll also need the registered application's ID, which is displayed as **Application (client) ID** in the **Overview** tab.

## One-click policies from Data Security Posture Management for AI

After the default policies are created, you can view and edit them at any time from their respective solution areas in the portal. For example, you want to scope the policies to specific users during testing, or for business requirements. Or, you want to add or remove classifiers that are used to detect sensitive information. Use the **Policies** page to quickly navigate to the right place in the portal.

Some policies, such as **DSPM for AI - Capture interactions for Copilot experiences** and **DSPM for AI - Detect sensitive info shared with AI via network** are [collection policies](collection-policies-solution-overview) that you can edit, and if necessary, delete like any other collection policy. For more information, see [Accessing collection policies](collection-policies-solution-overview#accessing-collection-policies).

If you delete any of the policies, their status on the **Policies** page displays **PendingDeletion** and continues to show as created in their respective recommendation cards until the deletion process is complete.

For sensitivity labels and their policies, view and edit these independently from Data Security Posture Management for AI, by navigating to **Information Protection** in the portal. For more information, use the configuration links in [Default labels and policies to protect your data](default-sensitivity-labels-policies).

For more information about the supported DLP actions and which platforms support them, see the first two rows in the table from [Endpoint activities you can monitor and take action on](endpoint-dlp-learn-about#endpoint-activities-you-can-monitor-and-take-action-on).

For the default policies that use Adaptive Protection, this capability is turned on if it's not already on, using default risk levels for all users and groups to dynamically enforce protection actions. For more information, see [Quick setup](insider-risk-management-adaptive-protection#quick-setup)

Note

Any default policies created while Data Security Posture Management for AI was in preview and named Microsoft Purview AI Hub won't be changed. For example, policy names will retain their **Microsoft AI Hub -** prefix.

### Default policies for data discovery using Data Security Posture Management for AI

- DLP policy: **DSPM for AI: Detect sensitive info added to AI sites**

    Source: **Extend your insights for data discovery**

    This policy discovers sensitive content pasted or uploaded in Microsoft Edge, Chrome, and Firefox to AI sites. This policy covers all users and groups in your org in audit mode only.
- Insider risk management policy: **DSPM for AI - Detect when users visit AI sites**

    Source: **Extend your insights for data discovery**

    This policy detects when users use a browser to visit AI sites.
- Insider risk management policy: **DSPM for AI - Detect risky AI usage**

    Source: Recommendation **Detect risky interactions in AI apps**

    This policy helps calculate user risk by detecting risky prompts and responses in Microsoft 365 Copilot, agents, and other generative AI apps.
- Communication Compliance: **DSPM for AI - Unethical behavior in AI apps**

    Source: Recommendation **Detect unethical behavior in AI apps**

    This policy detects sensitive information in prompts and responses in Microsoft 365 Copilot, agents, and other generative AI apps. This policy covers all users and groups in your organization.
- Collection policy: **DSPM for AI - Capture interactions for Copilot experiences**

    Source: Recommendation **Secure interactions in Microsoft Copilot experiences**

    This policy captures prompts and responses for data security posture and regulatory compliance from Copilot in Fabric, and Security Copilot. Manage them in Microsoft Purview solutions like eDiscovery, Data Lifecycle Management, and more.
- Collection policy: **DSPM for AI - Detect sensitive info shared with AI via network**

    Source: Recommendation **Extend insights into sensitive data in AI app interactions**

    This policy detects sensitive information shared with AI apps in browsers, applications, APIs, add-ins, and more, using a Secure Access Service Edge (SASE) or Security Service Edge (SSE) integration.

    Important

    This policy requires that you manually add one or more Secure Access Service Edge (SASE) or Security Service Edge (SSE) integrations in [Data Loss Prevention settings](collection-policies-create-deploy-policy#sase-provider-integration). The detection of AI interactions is dependent on the network partner implementation.

    If you want to capture prompts and responses in addition to detecting sensitive information, you must edit the collection policy and select the [option to capture content](collection-policies-solution-overview#content-capture-for-ai-interactions).
- Collection policy: **DSPM for AI - Capture interactions for enterprise AI apps**

    Source: Recommendation **Secure interactions from enterprise apps**

    This policy captures prompts and responses for regulatory compliance from enterprise AI apps, such as Chat GPT Enterprise and AI apps connected through Microsoft Entra or Microsoft Foundry, so they can be managed in Microsoft Purview solutions like eDiscovery, Data Lifecycle Management, and more.
- Collection policy: **DSPM for AI - Detect sensitive info shared in AI prompts in Edge**

    Source: **Extend your insights for data discovery**

    This policy detects prompts sent to generative AI apps in Microsoft Edge and discovers sensitive information shared in prompt contents. This policy covers all users and groups in your organization in audit mode only and doesn't capture content.

### Default policies from data security to help you protect sensitive data used in generative AI

- DLP policy **DSPM for AI - Block sensitive info from AI sites**

    Source: Recommendation **Fortify your data security**

    This policy uses Adaptive Protection to give a block-with-override to elevated risky users attempting to paste or upload sensitive information to other AI apps in Edge, Chrome, and Firefox. This policy covers all users and groups in your org in test mode.
- DLP policy **DSPM for AI - Block elevated risk users from submitting prompts to AI apps in Microsoft Edge**

    Source: Recommendation **Fortify your data security**

    Using Adaptive Protection, this policy blocks elevated, moderate, and minor risk users attempting to put information in AI apps while using Microsoft Edge. Users included in this policy will be blocked from using unprotected browsers because this policy includes [unmanaged apps](/en-us/purview/dlp-browser-dlp-learn#unmanaged-cloud-apps).
- DLP policy **DSPM for AI - Block sensitive info from AI apps in Edge**

    Source: Recommendation **Fortify your data security**

    This policy detects inline for a selection of common sensitive information types and blocks prompts from being sent to AI apps while using Microsoft Edge. Users included in this policy will be blocked from using unprotected browsers because this policy includes [unmanaged apps](/en-us/purview/dlp-browser-dlp-learn#unmanaged-cloud-apps).
- DLP policy **DSPM for AI - Protect sensitive data from Copilot processing**

    Source: Recommendation **Protect items with sensitivity labels from Microsoft 365 Copilot and agent processing**

    This policy blocks Microsoft 365 Copilot and agents from processing items with the sensitivity labels selected in this policy.
- Information Protection - **Sensitivity labels and policies**

    Source: Recommendation **Protect your data with sensitiivity labels**

    This recommendation creates [default sensitivity labels and sensitivity label policies](default-sensitivity-labels-policies). If you've already configured sensitivity labels and their policies, this configuration is skipped.

## Activity explorer events

Use the following information to help you understand the events you might see in the activity explorer from Data Security Posture Management for AI. References to a generative AI site can include Microsoft 365 Copilot, Microsoft 365 Copilot Chat, agents, other Microsoft copilots, and third-party AI sites.

| Event | Description |
| --- | --- |
| AI interaction | User interacted with a generative AI site. Details include the prompts and responses, except for unmanaged AI apps in Edge where text prompts only are included. For Microsoft 365 Copilot and Microsoft 365 Copilot Chat, this event requires auditing to be turned on. For Copilot in Fabric and Security Copilot, and for non-Copilot AI apps, prompts and responses require a collection policy with content capture selected to capture these interactions. |
| AI website visit | User browsed to a generative AI site. |
| DLP rule match | A data loss prevention rule was matched when a user interacted with a generative AI site. Includes DLP for Microsoft 365 Copilot. |
| Sensitive info types | Sensitive information types were found while a user interacted with a generative AI site. For Microsoft 365 Copilot and Microsoft 365 Copilot Chat, this event requires auditing to be turned on but doesn't require any active policies. |

Known issues:

- The **AI interaction** event doesn't always display text for the prompt and response. Sometimes, the prompt and response spans consecutive entries. Other scenarios can include:

    - Microsoft Facilitator AI-generated notes, no prompt or response is displayed
    - When a user doesn't have a mailbox hosted in Exchange Online, no prompt or response is displayed
- The **Sensitive info types detected** event doesn't display the user risk level.
- For Microsoft Facilitator AI-generated notes, **AI interaction** events can't be linked to **Sensitive info types detected** events.
- For collection policies, no prompt or response is displayed if the option to [capture content](collection-policies-solution-overview#content-capture-for-ai-interactions) isn't selected in the policy. For example, the one-click policy **DSPM for AI - Detect sensitive info shared with AI via network** doesn't select this option when the policy is automatically created, but you can manually edit the policy and select this option after the policy is created.