---
layout: Conceptual
title: Learn about Insider Risk Management policy templates | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about Insider Risk Management policy templates.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: article
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-07-18T00:00:00.0000000Z
audience: itpro
ms.collection:
- purview-compliance
ms.custom: admindeeplinkCOMPLIANCE
locale: en-us
document_id: 152661ed-d00b-1ba9-1613-d0f9841c0b86
document_version_independent_id: 152661ed-d00b-1ba9-1613-d0f9841c0b86
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-policy-templates.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-policy-templates
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-policy-templates.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 69ed0953-0384-d4e8-1575-62552b291d96
---

# Learn about Insider Risk Management policy templates | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

## Policy templates

Insider Risk Management templates are predefined policy conditions that define the types of risk indicators and risk scoring model used by the policy. Each policy must have an assigned template in the policy creation workflow before the policy is created. Insider Risk Management supports up to 100 policies for each policy template. When you create a new insider risk policy with the policy workflow, choose from one of the following policy templates:

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

### Data theft by departing users

When users leave your organization, there are specific risk indicators typically associated with potential data theft by departing users. This policy template uses exfiltration indicators for risk scoring and focuses on detection and alerts in this risk area. Data theft for departing users might include downloading files from SharePoint Online, printing files, and copying data to personal cloud messaging and storage services near their employment resignation and end dates. When you use either the Microsoft HR connector or the option to automatically check for user account deletion in Microsoft Entra for your organization, this template starts scoring for risk indicators relating to these activities and how they correlate with user employment status. This can include [cloud indicators](insider-risk-management-configure#connect-to-cloud-apps-in-microsoft-defender) for services such as Box, Dropbox, Google Drive, Amazon S3, and Azure.

Important

When you use this template, you can configure a Microsoft 365 HR connector to periodically import resignation and termination date information for users in your organization. See the [Import data with the HR connector](import-hr-data) article for step-by-step guidance to configure the Microsoft 365 HR connector. If you choose not to use the HR connector, select the User account deleted from Microsoft Entra option when configuring trigger events in the policy workflow.

### Data leaks

Protecting data and preventing data leaks is a constant challenge for most organizations, particularly with the rapid growth of new data created by users, devices, and services. Users can create, store, and share information across services and devices, which makes managing data leaks increasingly complex and difficult. Data leaks can include accidental oversharing of information outside your organization or data theft with malicious intent. This template scores real-time detections of suspicious SharePoint Online data downloads, file and folder sharing, printing files, and copying data to personal cloud messaging and storage services.

When you use a *Data leaks* template, you can assign a DLP policy to trigger indicators in the insider risk policy for high severity alerts in your organization. Whenever a high severity alert is generated by a DLP policy rule and added to the Office 365 audit log, insider risk policies created with this template automatically examine the high severity DLP alert. If the alert contains an in-scope user defined in the insider risk policy, the alert is processed by the insider risk policy as a new alert and assigned an insider risk severity and risk score. You can also choose to assign selected indicators as triggering events for a policy. This flexibility and customization helps scope the policy to only the activities covered by the indicators. This policy allows you to evaluate this alert in context with other activities included in the case.

This template can also include [cloud indicators](insider-risk-management-configure#connect-to-cloud-apps-in-microsoft-defender) for services such as Box, Dropbox, Google Drive, Amazon S3, and Azure.

#### Data leaks policy guidelines

When creating or modifying data loss prevention policies for use with Insider Risk Management policies, consider the following guidelines:

- Prioritize data exfiltration events and be selective when assigning **Incident reports** settings to *High* when configuring rules in your DLP policies. For example, emailing sensitive documents to a known competitor should be a *High* alert level exfiltration event. Over-assigning the *High* level in the **Incident reports** settings in other DLP policy rules can increase the noise in the Insider Risk Management alert workflow and make it more difficult for your data investigators and analysts to properly evaluate these alerts. For example, assigning *High* alert levels to access denial activities in DLP policies makes it more challenging to evaluate truly risky user behavior and activities.
- When using a DLP policy as the triggering event, make sure you understand and properly configure the users included in both the DLP and Insider Risk Management policies. Only users included in Insider Risk Management policies using the **Data leaks** template have high severity DLP policy alerts processed. Additionally, only users included in a rule for a high severity DLP alert are analyzed by the Insider Risk Management policy for consideration. Don't unknowingly configure the included users in both your DLP and insider risk policies in a conflicting manner.

    For example, if your DLP policy rules are scoped to only users on the Sales Team and the insider risk policy created from the **Data leaks** template has defined all users as in-scope, the insider risk policy only processes high severity DLP alerts for the users on the Sales Team. The insider risk policy doesn't receive any high priority DLP alerts for users to process that aren't defined in the DLP rules in this example. Conversely, if your Insider Risk Management policy created from **Data leaks** templates is scoped to only users on the Sales Team and the assigned DLP policy is scoped to all users, the insider risk policy only processes high severity DLP alerts for members of the Sales Team. The Insider Risk Management policy ignores high severity DLP alerts for all users not on the Sales Team.
- Make sure the **Incident reports** rule setting in the DLP policy used for this Insider Risk Management template is configured for *High* severity level alerts. The *High* severity level is the triggering events and Insider Risk Management alerts aren't generated from rules in DLP policies with the **Incident reports** field set at *Low* or *Medium*.

    ![DLP policy alert setting.](media/insider-risk-dlp-policy-high-severity.png)

    Note

    When creating a new DLP policy using the built-in templates, select the **Create or customize advanced DLP rules** option to configure the **Incident reports** setting for the *High* severity level.
- DLP alerts generated exclusively from Endpoint DLP, Microsoft Teams DLP, and Microsoft 365 Copilot DLP aren't currently evaluated by the DLP alert indicator.
- If your DLP policy covers multiple workloads, only the alerts originating from supported workloads are ingested. For more information about supported workloads, see [Configure policy indicators in Insider Risk Management](insider-risk-management-settings-policy-indicators#supported-dlp-workloads).

Each Insider Risk Management policy created from the **Data leaks** template can have up to 20 DLP policies assigned when using this triggering event option. Consider creating a dedicated DLP policy that combines the different activities you want to detect and act as triggering events for insider risk policies that use the **Data leaks** template.

For step-by-step guidance to configure DLP policies for your organization, see [Create and Deploy data loss prevention policies](dlp-create-deploy-policy).

### Data leaks by priority users

Protecting data and preventing data leaks for users in your organization might depend on their position, level of access to sensitive information, or risk history. Data leaks can include accidental oversharing of highly sensitive information outside your organization or data theft with malicious intent. With an assigned data loss prevention (DLP) policy as a triggering event option, this template starts scoring real-time detections of suspicious activity and results in an increased likelihood of insider risk alerts and alerts with higher severity levels. Priority users are defined in [priority user groups](insider-risk-management-settings-priority-user-groups) configured in the Insider Risk Management settings area.

As with the **Data leaks** template, you can choose a DLP policy to trigger indicators in the insider risk policy for high severity alerts in your organization. Follow the Data leaks policy guidelines for DLP policies when creating a policy with the DLP option when using this template. You can also choose to assign selected indicators as triggering events for a policy. This flexibility and customization help scope the policy to only the activities covered by the indicators. Additionally, you need to assign priority user groups created in **Insider Risk Management** &gt; **Settings** &gt; **Priority user groups** to the policy.

### Data leaks by risky users

When users experience employment stressors, they might become risky users, which might increase the chances of insider risk activity. This template starts scoring user activity when an indicator associated with risky user is identified. Examples include performance improvement notifications, poor performance reviews, changes to job level status, or email and other messages that might signal risk activities. Data leaks for risky users might include downloading files from SharePoint Online and copying data to personal cloud messaging and storage services.

When using this template, you must either configure an HR connector, select the option to [integrate Communication Compliance risk signals](/en-us/microsoft-365/compliance/communication-compliance-policies#policy-for-insider-risk-management-integration-preview) from user messages, or do both. The HR connector enables the periodic import of performance improvement notifications, poor performance review statuses, or job level change information for users in your organization. Communication Compliance risk integration imports signals for user messages that might contain potentially threatening, harassing, or discriminatory text content. Associated alerts generated in Communication Compliance don't need to be triaged, remediated, or changed in status to be integrated with the Insider Risk Management policy.

To configure an HR connector, see the [Import data with the HR connector](import-hr-data) article. To configure integration with Communication Compliance, select this option in the workflow when you configure the policy.

### Patient data misuse (preview)

Protecting healthcare record data and preventing the misuse of patient personal data is a significant concern for organizations in the healthcare industry. This misuse might include confidential data leaks to unauthorized persons, fraudulent modification of patient records, or the theft of patient healthcare records. Preventing this misuse of patient data helps meet the regulatory requirements of the Health Insurance Portability and Accountability Act (HIPAA) and the Health Information Technology for Economic and Clinical Health (HITECH) Act. Both of these acts establish the requirements for safeguarding patient protected health information (PHI).

This policy template enables risk scoring for internal users that detects suspicious activities associated with records hosted on existing electronic medical record (EMR) systems. Detection focuses on unauthorized access, viewing, modification, and export of patient data. You need to configure a connector the [Microsoft Healthcare connector](import-healthcare-data) to support detection of access, exfiltration, or obfuscation activities in your EMR system.

When using this template, you must also configure a Microsoft HR connector to periodically import organization profile data for users in your organization. See the [Set up a connector to import HR data](import-hr-data) article for step-by-step guidance to configure the Microsoft 365 HR connector.

### Risky Agents (preview)

This template helps you detect activities of agents hosted on [Microsoft Copilot Studio](ai-copilot-studio) and Microsoft Foundry. The use of agents within your organization introduces new risk opportunities. Agents interact with other users, other agents, and tools. Misconfigured agents could send sensitive data externally, or sensitive data could be shared at a user's request.

This policy detects risky prompts, agents generating sensitive responses, agents accessing sensitive or priority SharePoint files, agents accessing risky websites, and agents sharing SharePoint files with people outside of the organization. It also tracks activity above the agent's baseline.

This policy template is applied by default for all organizations.

### Risky AI usage

The use of AI tools and applications in many organizations presents new risk opportunities that might be difficult to identify and help mitigate. Users might inadvertently or purposefully create prompts in Microsoft AI tools that might contain [sensitive information](sit-sensitive-information-type-learn-about) or risky intent. Additionally, AI tools might inappropriately use sensitive information to provide responses to user prompts that might expose your organization to increased risks.

To help protect against these risks, this policy can help detect and enable risk scoring for these types of prompts and responses across AI tools in your organization. Detection focuses on user browsing activities to generative AI websites, user prompts and AI responses containing sensitive information in [Microsoft 365 Copilot](/en-us/copilot/microsoft-365/microsoft-365-copilot-overview), [Microsoft Copilot](/en-us/copilot/overview), and agents. Detection of risky activity by this policy also contributes to the user risk scoring in [Adaptive Protection](insider-risk-management-adaptive-protection).

When using this template, you must [configure](insider-risk-management-browser-support) the Microsoft Insider risk extension (on Microsoft Edge browser) or Microsoft Purview extension (on Chrome browser) on the user devices. We also recommend optionally configuring a [Microsoft HR connector](import-hr-data) to detect departing users and configuring a [Communication Compliance policy](communication-compliance-policies) to detect inappropriate content in messages for wider detection coverage. This policy can also be created as a one-click policy in [Microsoft Purview Data Security Posture Management (DSPM) for AI](dspm-for-ai) when you take action on the recommendation **Detect risky interactions in AI apps**.

### Risky browser usage (preview)

Identifying user visits to potentially inappropriate or unacceptable websites on organization devices and networks is an important part of minimizing security, legal, and regulatory risks. Users who inadvertently or purposefully visit these types of websites might expose the organization to legal actions from other users, violate regulatory requirements, elevate network security risks, or jeopardize current and future business operations and opportunities. This misuse is often defined in an organization's acceptable use policy for user devices and organization network resources but is often difficult to quickly identify and act on.

To help protect against these risks, this policy detects and enables risk scoring for web browsing that might violate your organization's acceptable use policy, such as visiting sites that pose a threat (phishing sites, for example) or that contain adult content. Several types of categories are available for automatic categorization of web browsing activities by users included in the policy.

This policy template has several prerequisites. For more information, see [Learn about and configure Insider Risk Management browser signal detection](/en-us/microsoft-365/compliance/insider-risk-management-browser-support).

### Security policy violations

In many organizations, users have permission to install software on their devices or to modify device settings to help with their tasks. Either inadvertently or with malicious intent, users might install malware or disable important security features that help protect information on their device or on your network resources. This policy template uses security alerts from Microsoft Defender for Endpoint to start scoring these activities and focus detection and alerts to this risk area. Use this template to provide insights for security policy violations in scenarios when users might have a history of security policy violations that might be an indicator of insider risk.

You need to configure Microsoft Defender for Endpoint in your organization and enable Defender for Endpoint for Insider Risk Management integration in the Defender Security Center to import security violation alerts. For more information on configuring Defender for Endpoint for Insider Risk Management integration, see [Configure advanced features in Defender for Endpoint](/en-us/windows/security/threat-protection/microsoft-defender-atp/advanced-features#share-endpoint-alerts-with-microsoft-compliance-center).

### Security policy violations by departing users

Departing users, whether they're leaving on positive or negative terms, might pose higher risks for security policy violations. To help protect against inadvertent or malicious security violations for departing users, this policy template uses Defender for Endpoint alerts to provide insights into security-related activities. These activities include the user installing malware or other potentially harmful applications and disabling security features on their devices. When you use the [Microsoft HR connector](import-hr-data) or the option to automatically check for user account deletion in Microsoft Entra for your organization, this template starts scoring for risk indicators relating to these security activities and how they correlate with user employment status.

You need to configure Microsoft Defender for Endpoint in your organization and enable Defender for Endpoint for Insider Risk Management integration in the Defender Security Center to import security violation alerts. For more information on configuring Defender for Endpoint for Insider Risk Management integration, see [Configure advanced features in Defender for Endpoint](/en-us/windows/security/threat-protection/microsoft-defender-atp/advanced-features#share-endpoint-alerts-with-microsoft-compliance-center).

### Security policy violations by priority users

Protecting against security violations for users in your organization might depend on their position, level of access to sensitive information, or risk history. Because security violations by priority users might have a significant impact on your organization's critical areas, this policy template starts scoring on these indicators, and uses Microsoft Defender for Endpoint alerts to provide insights into security-related activities for these users. These activities might include the priority users installing malware or other potentially harmful applications and disabling security features on their devices. Priority users are defined in priority user groups configured in the Insider Risk Management settings area.

You need to configure Microsoft Defender for Endpoint in your organization and enable Defender for Endpoint for Insider Risk Management integration in the Defender Security Center to import security violation alerts. For more information on configuring Defender for Endpoint for Insider Risk Management integration, see [Configure advanced features in Defender for Endpoint](/en-us/windows/security/threat-protection/microsoft-defender-atp/advanced-features#share-endpoint-alerts-with-microsoft-compliance-center). Additionally, you need to assign priority user groups created in **Insider Risk Management** &gt; **Settings** &gt; **Priority user groups** to the policy.

### Security policy violations by risky users

Users who experience employment stressors might be at higher risk for inadvertent or malicious security policy violations. These stressors could include being placed on a performance improvement plan, receiving a poor performance review, or experiencing a demotion. This policy template starts risk scoring based on these indicators and activities associated with these types of events.

When you use this template, you must configure an HR connector, or select the option to [integrate Communication Compliance risk signals](/en-us/microsoft-365/compliance/communication-compliance-policies#policy-for-insider-risk-management-integration-preview) from user messages, or both. The HR connector enables the periodic import of performance improvement notifications, poor performance review statuses, or job level change information for users in your organization. Communication Compliance risk integration imports signals for user messages that might contain potentially threatening, harassing, or discriminatory text content. Associated alerts generated in Communication Compliance don't need to be triaged, remediated, or changed in status to be integrated with the Insider Risk Management policy. To configure an HR connector, see the [Import data with the HR connector](import-hr-data) article. To configure integration with Communication Compliance, select this option in the workflow when you configure the policy.

You also need to configure Microsoft Defender for Endpoint in your organization and enable Defender for Endpoint for Insider Risk Management integration in the Defender Security Center to import security violation alerts. For more information on configuring Defender for Endpoint for Insider Risk Management integration, see [Configure advanced features in Defender for Endpoint](/en-us/windows/security/threat-protection/microsoft-defender-atp/advanced-features#share-endpoint-alerts-with-microsoft-compliance-center).

## Policy template prerequisites and triggering events

Depending on the template you choose for an Insider Risk Management policy, the triggering events and policy prerequisites vary. Triggering events are prerequisites that determine if a user is active for an Insider Risk Management policy. If you add a user to an Insider Risk Management policy but the user doesn't have a triggering event, the policy doesn't evaluate the user's activity unless you manually add the user in the Users dashboard. Policy prerequisites are required items so that the policy receives the signals or activities necessary to evaluate risk.

The following table lists the triggering events and prerequisites for policies created from each Insider Risk Management policy template:

| Policy template | Triggering events for policies | Prerequisites |
| --- | --- | --- |
| **Data leaks by priority users** | Data leak policy activity that creates a *High severity* alert or built-in exfiltration event triggers | DLP policy configured for *High severity* alerts (Exchange Online, SharePoint Online, or OneDrive for Business workloads only)  OR  Customized triggering indicators  Priority user groups configured in insider risk settings |
| **Data leaks by risky users** | - Performance improvement, poor performance, or job level change indicators from HR connector.  - Messages containing potentially threatening, harassing, or discriminatory language | Microsoft 365 HR connector configured for disgruntlement indicators  AND/OR  Communication Compliance integration and dedicated disgruntlement policy |
| **Data leaks** | Data leak policy activity that creates a *High severity* alert or built-in exfiltration event triggers | DLP policy configured for *High severity* alerts (Exchange Online, SharePoint Online, or OneDrive for Business workloads only)  OR  Customized triggering indicators |
| **Data theft by departing users** | Resignation or termination date indicator from HR connector or Microsoft Entra account deletion | (optional) Microsoft 365 HR connector configured for termination and resignation date indicators |
| **Patient data misuse** | Defense evasion of security controls from EMR systems  User and patient address matching indicators from HR systems | Healthcare access indicators selected in policy or insider risk settings  Microsoft 365 HR connector configured for address matching  Microsoft Healthcare or Epic connector configured |
| **Risky Agents** | - Exposing agent to risky prompts  - Agent generating sensitive responses  - Accessing sensitive or priority SharePoint files  - Accessing risky websites  - Sharing SharePoint files with people outside the organization  - Activity is above agent's usual activity for the day | Copilot Studio agents  Microsoft Foundry agents |
| **Risky AI usage** |  | Microsoft Insider risk extension (on Microsoft Edge browser) or Microsoft Purview extension (on Chrome browser) must be installed on the user's devices  At least one browsing indicator selected in the policy  AND  (optional) Microsoft 365 HR connector configured for termination and resignation date indicators  (optional) A Communication Compliance policy detecting inappropriate content in messages |
| **Risky browser usage** | User browsing activity related to security that matches at least one selected *Browsing indicator* | See the complete list of prerequisites in the [browser signal detection article](/en-us/microsoft-365/compliance/insider-risk-management-browser-support) |
| **Security policy violations by departing users** | Resignation or termination date indicators from HR connector or Microsoft Entra account deletion | (optional) Microsoft 365 HR connector configured for termination and resignation date indicators  Active Microsoft Defender for Endpoint subscription  Configuration of Microsoft Defender for Endpoint integration with Microsoft Purview portal |
| **Security policy violations by priority users** | Defense evasion of security controls or unwanted software detected by Microsoft Defender for Endpoint | Active Microsoft Defender for Endpoint subscription  Configuration of Microsoft Defender for Endpoint integration with Microsoft Purview portal  Priority user groups configured in insider risk settings |
| **Security policy violations by risky users** | - Performance improvement, poor performance, or job level change indicators from HR connector.  - Messages containing potentially threatening, harassing, or discriminatory language | Microsoft 365 HR connector configured for risk indicators  AND/OR  Communication Compliance integration and dedicated risky user policy  AND  Active Microsoft Defender for Endpoint subscription  Configuration of Microsoft Defender for Endpoint integration with Microsoft Purview portal |
| **Security policy violations** | Defense evasion of security controls or unwanted software detected by Microsoft Defender for Endpoint | Active Microsoft Defender for Endpoint subscription  Configuration of Microsoft Defender for Endpoint integration with Microsoft Purview portal |

## Policy template limits

Insider Risk Management policy templates use limits to manage the volume and rate of processing for risk activities for included users and for integration with supporting Microsoft 365 services. Each policy template supports a maximum number of included users who can actively receive risk scores for the policy. The policy can effectively process and report potentially risky activities. Included users are users with triggering events for the policy.

The limit for each policy calculates the total number of unique users receiving risk scores per policy template type. If the number of users for a policy template type nears or exceeds the user limit, the policy performance reduces. To view the current number of users for a policy, go to the Policy tab and the Users in scope column. These maximum limits apply to users across all policies using a given policy template.

For user scope limits for specific policy templates, see [Limits in Insider Risk Management](insider-risk-management-limits#maximum-number-of-users-in-scope-for-a-policy-template).

## Integration with collection policies

Depending on your configuration, collection policies might impact Insider Risk Management policy behavior. When you configure and deploy a collection policy, the collection policy configuration takes precedence if there's a mismatch between an Insider Risk Managment policy that includes device indicators and a collection policy in your organization. This configuration means that if you configure an Insider Risk Management policy to monitor a specific activity for devices, but you configure the collection policy to filter out that device activity, the device activity isn't collected and isn't available for review in Insider Risk Management.