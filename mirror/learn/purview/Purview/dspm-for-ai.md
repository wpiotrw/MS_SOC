---
layout: Conceptual
title: Learn how Microsoft Purview Data Security Posture Management for AI provides data security and compliance protections for Copilots and other generative AI apps - (classic) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dspm-for-ai
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: helenachen-microsoft
ms.service: purview
ms.subservice: purview-data-security-posture-management
ms.update-cycle: 180-days
ms.date: 2025-12-15T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.collection:
- highpri
- m365copilot
- msec-ai-copilot
description: Use Microsoft Purview Data Security Posture Management for AI to help you protect and manage data security and compliance protections for generative AI apps - (classic).
locale: en-us
document_id: 79b758ae-bae0-2520-99f4-539f3fc3661f
document_version_independent_id: 79b758ae-bae0-2520-99f4-539f3fc3661f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dspm-for-ai.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dspm-for-ai
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dspm-for-ai.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0fc65d4-7c73-4029-a261-7f99ff744363
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b2daec57-5914-4967-8ed3-1d444897ba59
platformId: ed9bb40f-fd98-4cd9-0453-57132a7922f5
---

# Learn how Microsoft Purview Data Security Posture Management for AI provides data security and compliance protections for Copilots and other generative AI apps - (classic) | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Note

This article is for the **classic** version of Data Security Posture Management for AI that's now replaced with a new version that incorporates support for AI apps and agents, new features and broader reach, with simplified management.

These improvements won't be added to this classic version so we invite you to try the new [Data Security Posture Management](data-security-posture-management-learn-about).

Microsoft Purview Data Security Posture Management (DSPM) for AI from the [Microsoft Purview portal](purview-portal) provides a central management location to help you quickly secure data for AI apps and proactively monitor AI use. These apps include Copilots, agents, and other AI apps that use third-party large language modules (LLMs).

Data Security Posture Management for AI offers a set of capabilities so you can safely adopt AI without having to choose between productivity and protection:

- Insights and analytics into AI activity in your organization
- Ready-to-use policies to protect data and prevent data loss in AI prompts
- Data risk assessments to identify, remediate, and monitor potential oversharing of data.
- Compliance controls to apply optimal data handling and storing policies

For a list of supported third-party AI sites, such as those used for Gemini and ChatGPT, see [Supported AI sites by Microsoft Purview for data security and compliance protections](ai-microsoft-purview-supported-sites).

## How to use Data Security Posture Management for AI

To help you more quickly gain insights into AI usage and protect your data, Data Security Posture Management for AI provides some recommended [preconfigured policies](dspm-for-ai-considerations#one-click-policies-from-data-security-posture-management-for-ai) that you can activate with a single click. If you're using [administrative units](purview-admin-units), you must be an unrestricted administrator to create these policies that apply to all users in your organization.

Allow at least 24 hours for these new policies to collect data to display the results in Data Security Posture Management for AI, or reflect any changes that you make to the default settings.

[![Example screenshot of Microsoft Purview Data Security Posture Management for AI.](media/example-dspm.png)](media/example-dspm.png#lightbox)

No activation needed, Data Security Posture Management for AI automatically runs a weekly data risk assessment for the top 100 SharePoint sites based on usage in your organization. You can supplement this with your own custom data risk assessments, currently in preview. These assessments are designed specifically to help you identify, remediate, and monitor potential oversharing of data, so you can be more confident about your organization using Microsoft 365 Copilot and agents, and Microsoft 365 Copilot Chat. 

To get started with Data Security Posture Management for AI, use the [Microsoft Purview portal](purview-portal). You need an account that has [appropriate permissions](ai-microsoft-purview-permissions) for compliance management, such as an account that's a member of the **Microsoft Entra Compliance Administrator** group role.

Tip

The following steps provide a recommended walkthrough to use all the available capabilities from DSPM for AI. If you're interested in using DSPM for AI just for a specific AI app, use the links in the Next steps section.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **DSPM for AI (classic)**.

    [![Selecting the Microsoft Purview Data Security Posture Management for AI solution from the Microsoft Purview portal.](media/dspm-solution.png)](media/example-dspm.png#lightbox)
2. From **Overview**, keep the **All AI apps** view selected. Review the **Get started** section to learn more about Data Security Posture Management for AI, and the immediate actions you can take. Select each one to display the flyout pane to learn more, take actions, and verify your current status.

    | Action | More information |
    | --- | --- |
    | **Turn on Microsoft Purview Audit** | Auditing is on by default for new tenants, so you might already meet this prerequisite. If you do, and users are already assigned licenses for Microsoft 365 Copilot, you start to see insights about Copilot and agents activities from the **Reports** section further down the page. |
    | **Install Microsoft Purview browser extension** | A prerequisite for third-party AI sites. |
    | **Onboard devices to Microsoft Purview** | Also a prerequisite for third-party AI sites. |
    | **Extend your insights for data discovery** | One-click policies for collecting information about users visiting [third-party generative AI sites](ai-microsoft-purview-supported-sites) and sending sensitive information to them. The option is the same as the **Extend your insights** button in the AI data analytics section further down the page. |

    For more information about the prerequisites, see [Prerequisites for Data Security Posture Management for AI](dspm-for-ai-considerations#prerequisites-for-data-security-posture-management-for-ai).

    For more information about the preconfigured policies that you can activate, see [One-click policies from Data Security Posture Management for AI](dspm-for-ai-considerations#one-click-policies-from-data-security-posture-management-for-ai).
3. Then, review the **Recommendations** section and decide whether to implement any options that are relevant to your tenant. View each recommendation to understand how they're relevant to your data and learn more.

    These options include running a data risk assessment across SharePoint sites, creating sensitivity labels and policies to protect your data, and creating some [default policies](dspm-for-ai-considerations#one-click-policies-from-data-security-posture-management-for-ai) to immediately help you detect and protect sensitive data sent to generative AI sites. Examples of recommendations:

    - **Protect your data from potential oversharing risks** by viewing the results of your default data risk assessment to identify and fix issues to help you more confidently deploy Microsoft 365 Copilot.
    - **Protect your data with sensitivity labels** by creating a set of [default sensitivity labels](default-sensitivity-labels-policies) if you don't yet have sensitivity labels, and policies to publish them and automatically label documents and emails.
    - **Protect items with sensitivity labels from Microsoft 365 Copilot and agent processing** by prompting you to select one or more [sensitivity labels](sensitivity-labels#sensitivity-labels-for-microsoft-365-copilot-and-microsoft-365-copilot-chat) that prevent Microsoft 365 Copilot and agents summarizing the labeled data. For more information about this capability, see [Learn about using Microsoft Purview Data Loss Prevention to protect interactions with Microsoft 365 Copilot and Copilot Chat](dlp-microsoft365-copilot-location-learn-about).
    - **Detect risky interactions in AI apps** to calculate user risk by detecting risky prompts and responses in Microsoft 365 Copilot, agents, and other generative AI apps. For more information, see [Risky AI usage](insider-risk-management-policy-templates#risky-ai-usage).
    - **Discover and govern interactions with ChatGPT Enterprise AI** by registering ChatGPT Enterprise workspaces, you can identify potential data exposure risks by detecting sensitive information that's shared with ChatGPT Enterprise.
    - **Get guided assistance to AI regulations**, which uses [control-mapping regulatory templates from Compliance Manager](compliance-manager-regulations).
    - **Secure interactions for Microsoft Copilot experiences**, which captures prompts and responses for Copilot in Fabric, and Security Copilot. Without a policy similar to the one that's created with this recommendation, auditing events are captured for Copilot in Fabric and Security Copilot, but not the prompts and responses.
    - **Detect sensitive info shared with AI via network**, which uses [network data security](dlp-network-data-security-learn) to detect sensitive info types shared with AI apps in browsers, applications, APIs, add-ins, and more, using a Secure Access Service Edge or Security Service Edge integration.
    - **Secure interactions from enterprise apps**, which captures prompts and responses for regulatory compliance from Entra-registered AI apps, ChatGPT Enterprise Connector, and applications built on Microsoft Foundry.
    - **Secure data in Azure AI apps and agents**, which has set up instructions to capture prompts and responses for AI apps that use one or more Azure AI subscriptions.

    You can use the **View all recommendations** link, or **Recommendations** from the navigation pane to see all the available recommendations for your tenant, and their status. When a recommendation is complete or dismissed, you no longer see it on the **Overview** page.
4. Use the **Reports** section or the **Reports** page from the navigation pane to view the results of the default policies created. You need to wait at least a day for the reports to be populated. Select the categories of **Copilot experiences and agents**, **Enterprise AI apps**, and **Other AI apps** to help you identify the specific generative AI app.
5. Use the **Policies** page to monitor the status of the [default one-click policies created](dspm-for-ai-considerations#one-click-policies-from-data-security-posture-management-for-ai) and AI-related policies from other Microsoft Purview solutions. To edit the policies, use the corresponding management solution in the portal. For example, for **DSPM for AI - Unethical behavior in Copilot**, you can [review and remediate the matches](communication-compliance-investigate-remediate) from the **Communication Compliance** solution.

    Note

    If you have the older retention policies for the location **Teams chats and Copilot interactions**, they aren't included on this page. Learn how to [create separate retention policies](create-retention-policies#separate-an-existing-teams-chats-and-copilot-interactions-policy) for Microsoft Copilot Experiences that will be included on this **Policy** page.
6. Select **Apps and agents** to view a dashboard of AI apps and their agents used across your organization so you can identify and manage any potential data security risks. For each agent, view details about sensitive data that they accessed and how they are protected by policies from Microsoft Purview.
7. Select **Activity explorer** to see details of the data collected from your policies.

    This more detailed information includes activity type and user, date and time, AI app category and app, app accessed in, any sensitive information types, files referenced, and sensitive files referenced.

    Examples of activities include **AI interaction**, **Sensitive info types**, and **AI website visit**. Prompts and responses are included in the **AI interaction** events when you have the [right permisisons](ai-microsoft-purview-permissions#permissions-by-activities). You can use the **Web queries** filter in activity explorer to more easily identify which AI interactions have a web query, with the AI interaction flyout pane diplaying the search query text in the **Web references AI app used** section. For more information about the events, see [Activity explorer events](dspm-for-ai-considerations#activity-explorer-events).

    Similar to the report categories, workloads include **Copilot experiences and agents**, **Enterprise AI apps**, and **Other AI Apps**. Examples of an app ID and app host for **Copilot experiences and agents** include **Microsoft 365 Copilots** and **Copilot Studio**. **Enterprise AI apps** includes **ChatGPT Enterprise**. **Other AI Apps** include the apps from the [supported third-party AI sites](ai-microsoft-purview-supported-sites), such as those used for Gemini and ChatGPT.

1. Select **Data risk assessments** to identify and fix potential data oversharing risks in your organization. Because of the power and speed AI can proactively surface content that might be obsolete, over-permissioned, or lacking governance controls, generative AI amplifies the problem of oversharing data. Use data risk assessements to both identify and remediate issues.

    For oversharing insights in SharePoint and OneDrive, use the **Microsoft 365** tab, and the **Fabric** tab for items in Fabric workspaces.

# [Microsoft 365](#tab/m365)
A default data risk assessment automatically runs weekly for the top 100 SharePoint sites based on usage in your organization, and you might have already run a custom assessment as one of the recommendations. However, come back regularly to this option to check the latest weekly results of the default assessment and run custom assessments when you want to check for different users or specific sites. After a custom assessment has run, wait at least 48 hours to see the results that don't update again. You'll need a new assessment to see any changes in the results.

The **Default assessment** displays at the top of the page with a quick summary, such as the total number of items found, the number of sensitive data detected, and the number of links sharing data with anyone. The first time the default assessment is created there's a 4-day delay before results are displayed.

After you select **View details** for more in-depth information, from the list, select each site to access the flyout pane that has tabs for **Overview**, **Identify**, **Protect**, and **Monitor**. Use the information on each tab to learn more, and take recommended actions. For example:

Use the **Identify** tab to identify how much data has been scanned or not scanned for sensitive information types, with an option to initiate an [on-demand classification scan](on-demand-classification) as needed.

Use the **Protect** tab to select options to remediate oversharing, which include:

    - **Restrict access by label**: Use Microsoft Purview Data Loss Prevention to create a DLP policy that prevents Microsoft 365 Copilot and agents from summarizing data when it has sensitivity labels that you select. For more information about how this works and supported scenarios, see [Learn about using Microsoft Purview Data Loss Prevention to protect interactions with Microsoft 365 Copilot and Copilot Chat](dlp-microsoft365-copilot-location-learn-about).
    - **Restrict all items**: Use SharePoint Restricted Content Discovery to list the SharePoint sites to be exempt from Microsoft 365 Copilot. For more information, see [Restrict discovery of SharePoint sites and content](/en-us/sharepoint/restricted-content-discovery).
    - **Create an auto-labeling policy**: When sensitive information is found for unlabeled files, use Microsoft Purview Information Protection to create an auto-labeling policy to automatically apply a sensitivity label for sensitive data. For more information about how to create this policy, see [How to configure auto-labeling policies for SharePoint, OneDrive, and Exchange](apply-sensitivity-label-automatically#how-to-configure-auto-labeling-policies-for-sharepoint-onedrive-and-exchange).
    - **Create retention policies**: When content hasn't been accessed for at least 3 years, use Microsoft Purview Data Lifecycle Management to automatically delete it. For more information about how to create the retention policy, see [Create and configure retention policies](create-retention-policies).

Use the **Monitor** tab to view the number of items in the site shared with anyone, shared with everyone in the organization, shared with specific people, and shared externally. Select **Start a SharePoint site access review** for information [how to use the SharePoint data access governance reports](/en-us/sharepoint/site-access-review).

# [Fabric](#tab/fabric)
Important

Before you can see data risk assessments for Fabric, there's a one-time setup process that requires an app registered in Entra, which is a member of a security group that you specify with the Admin API settings in the Fabric admin portal. For instructions and how to specify the authentication values required to run data risk assessments for Fabric, see [Prerequisites for Fabric data risk assessments](dspm-for-ai-considerations#prerequisites-for-fabric-data-risk-assessments).

Only when these prerequisites are in place and you know the authentication values to specify, select **Set config** for Fabric data risk assessments. In the **Configure Fabric Settings** box, enter the authentication values using **Federated Credentials** (recommended, more secure) or **Client Secret**. Select **Test connection**, and if successful, select **Save**. The default assessment starts scanning.

Once set up, the default data risk assessment automatically runs weekly for the top 100 Fabric workspaces based on usage in your organization. Come back regularly to this option to check the latest weekly results of the default assessment and run custom assessments when you want to check for different users or specific workspaces. After a data risk assessment has run, wait at least 48 hours to see the results that don't update again. You'll need a new assessment to see any changes in the results.

**Supported Fabric item types for scanning**: Dashboard, Report, DataExploration, DataPipeline, KQLQuerySet, Lakehouse, Notebook, SQLAnalyticsEndpoint, and Warehouse

The **Fabric default assessment** displays at the top of the page with a quick summary that includes the sensitive information types found, the total number of items that have and don't have [sensitivity labels to protect them](/en-us/fabric/governance/information-protection), and to whom they are accessible (users, the organization, externally, and groups).

For more in-depth information, from the list, select each workspace to access the flyout pane that has tabs for **Overview**, **Protect**, and **Monitor**. Use the information on each tab to learn more about the scanned data for that workspace.

Use the **Protect** tab to see recommended actions you can take to prevent oversharing by creating a [data loss prevention (DLP) policy](dlp-powerbi-get-started) and apply a [default sensitivity label to new and edited items](/en-us/fabric/governance/sensitivity-label-default-label-policy). Examples of a DLP policy that you can configure for Fabric:

    - When specific sensitive information types are found, block access to people who have this access as a result of the "Anyone with the link" option
    - When specific sensitive information types are found, apply a specific sensitivity label
    - When items with a specific sensitivity label are accessed, attach a policy tip to the item and register an alert in the Microsoft Purview portal

Use the **Monitor** tab to see breakdown numbers of how access is configured: Accessible to specific people, accessible externally, accessible to everybody in your organization, and accessible to a group. Choose the option to run an access review in Microsoft Entra. For more information about this option, see [What are access reviews?](/en-us/entra/id-governance/access-reviews-overview)

---

1. To create your own custom data risk assessment, select **Create custom assessment** to identify potential oversharing issues for all or selected users, the data sources to scan, and run the assessment. 
    Note

    Microsoft 365 custom assessments optionally support item-level scanning with remediation actions when you complete a one-time authentication process. To specify the required settings, you must have a registered Entra application. For more information about the Entra application, see [Prerequisites for Microsoft 365 item-level scanning for data risk assessments](dspm-for-ai-considerations#prerequisites-for-microsoft-365-item-level-scanning-for-data-risk-assessments).

    Select **Item-level** on the **Scan level** page, and then **Authenticate** to specify the Entra application information.
 This data risk assessment is created in the **Custom assessments** category. Wait for the status of your assessment to display **Completed**, and select it to view details. To rerun a custom data risk assessment, and to see results after the 30-day expiration, use the duplicate option to create a new assessment with the same selections. Item-level scanning and remediation for items that are potentially overshared is applicable to Microsoft 365 only, and currently restricted to SharePoint sites. This scan identifies items as potentially overshared if they have a sharing link for external or anonymous users, and also shows any applied sensitivity label and the owner of each item. When the scan is complete, open the custom assessment and view item-level insights from the **Potentially overshared items** tab or the **View items** button from the **Potentially overshared items**banner. The following remediation actions can be taken on the identified potentially overshared items:
    - **Resolve**, for example if you decide the item isn't at risk of oversharing.
    - **Apply sensitivity label** for items that are identified as currently unlabeled or should have a different sensitivity label.
    - **Notify** the site owner with an email notification (not customizable).
    - **Remove sharing link** to remove the existing sharing link so it can no longer be used to access the item. This is an action to be used sparingly because it could prevent people from accessing the item legitimately. In this scenario, the site owner or item owner must then set a less permissive sharing link type for authorized users. If you haven't already, consider [configuring sensitivity labels for a default sharing link](sensitivity-labels-default-sharing-link).

 The email notification contains information and instructions about the potentially overshared items in the site. It also contains options for them to go to the SharePoint site to manage access to the items from there, or to the Microsoft Purview portal for a read-only view of the item-level scan results that only show items and sites that they own. 
    Tip

    Both the default and custom data risk assessments provide an **Export** option that let you save and customize the data into a choice of file formats (Excel, CSV, JSON, TSV).
Limits for Microsoft 365:
    - A maximum of 200,000 items per location, which applies to both a custom data risk assessment and a default data risk assessment. The count of files reported might not be accurate when there are more than 100,000 files per location.
    - OneDrive currently isn't supported for item-level scanning.
    - A current maximum of 10 SharePoint sites for item-level scanning.