---
layout: Conceptual
title: Configure policy indicators in Insider Risk Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Configure policy indicators in Microsoft Purview Insider Risk Management to define the type of risk activities that you want to detect and investigate.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: how-to
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: itpro
ms.collection:
- highpri
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- highpri
ms.custom: msecd-doc-authoring-1014, admindeeplinkCOMPLIANCE, sfi-image-nochange
ai-usage: ai-assisted
locale: en-us
document_id: d932d95b-419d-55ef-9c75-26c77efed5f8
document_version_independent_id: d932d95b-419d-55ef-9c75-26c77efed5f8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-settings-policy-indicators.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-settings-policy-indicators
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-settings-policy-indicators.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: e64e5a08-0a31-dc2a-dd1e-898b830f518e
---

# Configure policy indicators in Insider Risk Management | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Insider risk policy templates in Microsoft Purview Insider Risk Management define the type of risk activities that you want to detect and investigate. Each policy template is based on specific indicators that correspond to specific triggers and risk activities. All global indicators are disabled by default; **you must select one or more indicators to configure an Insider Risk Management policy**.

Policies collect signals and trigger alerts when users perform activities related to the indicators.

## Types of events and indicators

Insider Risk Management uses different types of events and indicators to collect signals and create alerts:

- **Triggering events**: Events that determine if a user is active in an Insider Risk Management policy. If you add a user to an Insider Risk Management policy that doesn't have a triggering event, the policy doesn't evaluate the user as a potential risk. For example, User A is added to a policy created from the *Data theft by departing users* policy template and the policy and Microsoft 365 HR connector are properly configured. Until User A has a termination date reported by the HR connector, the policy doesn't evaluate User A for potential risk. Another example of a triggering event is if a user has a *High* severity data loss prevention (DLP) policy alert when using *Data leaks* policies.
- **Global settings indicators**: Indicators enabled in global settings for Insider Risk Management define both the indicators available for configuration in policies and the types of events signals collected by Insider Risk Management. For example, if a user copies data to personal cloud storage services or portable storage devices and you select these indicators only in global settings, you can review the user's potentially risky activity in the Activity explorer. If you don't define this user in an Insider Risk Management policy, the policy doesn't evaluate the user as a potential risk and therefore doesn't assign a risk score or generate an alert.
- **Policy indicators**: Indicators included in Insider Risk Management policies determine a risk score for an in-scope user. You enable policy indicators from indicators defined in global settings. The policy indicators activate only after a triggering event occurs for a user. Examples of policy indicators include:

    - A user copies data to personal cloud storage services or portable storage devices.
    - A user account is removed from Microsoft Entra ID.
    - A user shares internal files and folders with unauthorized external parties.

You can use certain policy indicators and sequences to customize triggering events for specific policy templates. When you configure these indicators or sequences in the policy workflow for the *General data leaks* or *Data leaks by priority users* templates, you get more flexibility and customization for your policies and when users are in-scope for a policy. You can also define risk management activity thresholds for these triggering indicators for more fine-grained control in a policy.

## Define the insider risk policy indicators that are enabled in all insider risk policies

To enable policy indicators for all insider risk policies, complete the following steps:

1. Select **Settings**, then select **Policy indicators**.
2. Select one or more policy indicators. The indicators you select on the **Policy indicators** settings page can't be individually configured when creating or editing an insider risk policy in the policy workflow.

    Note

    It might take several hours for new manually added users to appear in the **Users dashboard**. Activities for the previous 90 days for these users might take up to 24 hours to display. To view activities for manually added users, select the user on the **Users dashboard** and open the **User activity** tab in the details pane.

## Two types of policy indicators: built-in indicators and custom indicators

## Indicators and pay-as-you-go billing

Some indicators included in Insider Risk Management require that you enable the [pay-as-you-go billing model](purview-billing-models) for your organization. Depending on your configured billing model, a notification might be displayed prompting you to configure pay-as-you-go billing to use these indicators.

## Built-in indicators vs. custom indicators

Policy indicators are organized into two tabs:

- **Built-in indicators**: Insider Risk Management includes many built-in indicators for various scenarios that you can use right away in your policies. Choose the indicators that you want to activate, then customize indicator thresholds for each indicator level when you create an insider risk policy. This article describes the built-in indicators in more detail.
- **Custom indicators**: Use custom indicators together with the [Insider Risk Indicators (preview) connector](import-insider-risk-indicators) to bring non-Microsoft detections to Insider Risk Management. For example, you might want to extend your detections to include Salesforce and Dropbox and use them alongside the built-in detections provided by the Insider Risk Management solution, which is focused on Microsoft workloads (SharePoint Online and Exchange Online, for example). Create a custom indicator

### Built-in indicators

Insider Risk Management includes the following built-in indicators.

#### Office indicators

These indicators include policy indicators for SharePoint sites, Microsoft Teams, and email messaging.

#### Cloud storage indicators

Important

To use this indicator, enable [pay-as-you-go billing](purview-billing-models) in your organization.

These indicators include policy indicators for Google Drive, Box, and Dropbox that you can use to detect techniques used to determine the environment, gather and steal data, and disrupt the availability or compromise the integrity of a system. To select from [cloud storage indicators](insider-risk-management-configure#connect-to-cloud-apps-in-microsoft-defender), you must [connect cloud storage apps in Microsoft Defender](/en-us/defender-cloud-apps/enable-instant-visibility-protection-and-governance-actions-for-your-apps).

After configuring the cloud storage indicators, you can turn off indicators for the apps you don't want to use in settings. For example, you can select a content download indicator for Box and Google Drive, but not Dropbox.

#### Cloud service indicators

Important

To use this indicator, enable [pay-as-you-go billing](purview-billing-models) in your organization.

These indicators include policy indicators for Amazon S3 and Azure (SQL Server and Storage) that you can use to detect techniques used to avoid detection or risky activities. These techniques might include:

- Disabling trace logs
- Updating or deleting SQL Server firewall rules
- Techniques used to steal data, such as sensitive documents
- Techniques used to disrupt the availability or compromise the integrity of a system
- Techniques used to gain higher-level permissions to systems and data.

To select from [cloud service indicators](insider-risk-management-configure#connect-to-cloud-apps-in-microsoft-defender), you must [connect source service apps in Microsoft Defender](/en-us/defender-cloud-apps/enable-instant-visibility-protection-and-governance-actions-for-your-apps).

#### Network indicators

Important

To use this indicator, enable [pay-as-you-go billing](purview-billing-models) in your organization.

These indicators include HTTP and HTTPS network traffic from third party network security solutions. You can identify sensitive items that are being shared through these interactions. Detection of network traffic activities requires creation of a [collection policy](collection-policies-policy-reference) as a prerequisite. Learn more about [network data security](dlp-network-data-security-learn).

#### Microsoft Entra ID indicators

These indicators include risk detections from [Microsoft Entra ID Protection](/en-us/entra/id-protection/overview-identity-protection). Risk detections are a powerful resource that can include any suspicious or anomalous activity related to a user account in the directory. Microsoft Entra ID Protection risk detections can be linked to an individual user or sign-in event.

User risk detections might flag a legitimate user account as at risk when a potential threat actor gains access to an account by compromising their credentials or when they detect some type of anomalous user activity. Sign-in risk detections represent the probability that a given authentication request isn't the authorized owner of the account.

To maintain relevance of the indicators to Insider Risk Management policies, only Microsoft Entra alerts in a *ConfirmedCompromised* or *Remediated* status state are evaluated. To learn more about the risk detections in Microsoft Entra ID Protection, see [Risks detections in Microsoft Entra ID Protection](/en-us/entra/id-protection/concept-identity-protection-risks).

#### Microsoft Fabric indicators

Important

To use the Microsoft Fabric indicators, enable [pay-as-you-go billing](purview-billing-models) in your organization.

These indicators include policy indicators for Microsoft Fabric workloads such as Power BI and Lakehouse. They help you detect techniques used to:

- Figure out the environment (for example, viewing Power BI reports and dashboards).
- Gather data of interest (for example, downloading Power BI reports).
- Obfuscate the data gathered or change protection (for example, downgrading or removing sensitivity labels of Power BI or Lakehouse assets).
- Exfiltrate the data (for example, sharing Lakehouse data with people outside the organization).

#### Generative AI apps indicators

These indicators include policy indicators for numerous generative AI applications. Use these indicators in policies to analyze interactions (prompts and responses) entered into these applications and help detect inappropriate or risky interactions or sharing of confidential information. These indicators include the following generative AI applications:

- **Microsoft Copilot experiences**: Support for user interactions in [Copilot in Microsoft Fabric](/en-us/fabric/fundamentals/copilot-fabric-overview), [Microsoft Security Copilot](/en-us/copilot/security/microsoft-security-copilot), [Microsoft Copilot Studio](/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio), any connected or cloud AI application.

    Important

    To use the Microsoft Copilot experiences indicator for non-Microsoft 365 AI data, enable [pay-as-you-go billing](/en-us/purview/purview-billing-models) in your organization. Non-Microsoft 365 AI data includes information from other generative AI applications from Microsoft and other connected external AI applications. This data type includes [Copilot in Microsoft Fabric](/en-us/fabric/fundamentals/copilot-fabric-overview), [Microsoft Security Copilot](/en-us/copilot/security/microsoft-security-copilot), [Microsoft Copilot Studio](/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio), and any connected or cloud AI application. There aren't any pay-as-you-go billing requirements or charges for Microsoft 365 detecting inappropriate or risky interaction for Microsoft 365 Copilot data.
- **Enterprise AI apps**: Non-Copilot AI applications connected using [Microsoft Entra](/en-us/entra/fundamentals/what-is-entra) and [Microsoft Purview Data Map](data-map) connectors.

    Important

    To use the Enterprise AI apps indicator, enable [pay-as-you-go billing](purview-billing-models) in your organization.
- **Other AI applications**: AI applications that users in your organization discover from their browser activity.

    Important

    To use this indicator, enable [pay-as-you-go billing](purview-billing-models) in your organization.
- **Azure AI Content Safety indicators**: Support for [Communication Compliance indicators](communication-compliance-policies#select-generative-ai-policy-indicators-for-policy-templates) to identify prompts and responses matching classifiers provided by Azure AI Content Safety like [Prompt shields](/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection) and [Protected Materials](/en-us/azure/ai-services/content-safety/concepts/protected-material).

    Important

    When you select the Azure AI Content Safety indicator, you create a Communication Compliance policy. If you modify this policy in Communication Compliance, you might need to pay for [pay-as-you-go billing](purview-billing-models).

For Microsoft Copilot experiences and Enterprise AI apps, you can select which specific generative AI apps you want to monitor. By default, all available apps are selected. You can deselect apps that aren't relevant to your organization to reduce alert noise and avoid unnecessary pay-as-you-go billing charges. When an app is deselected, signals from that app aren't processed and no cost is incurred.

##### Select generative AI apps to monitor

Note

For **Microsoft Copilot experiences** and **Enterprise AI apps** only, you can review and deselect apps to optimize costs and reduce alert noise.

1. In the Microsoft Purview portal, go to **Insider Risk Management** &gt; **Settings** &gt; **Policy indicators**.
2. Expand **Generative AI apps indicators**.
3. For **Microsoft Copilot experiences** and **Enterprise AI apps**, select **Choose apps to monitor**.
4. From the side panel, you can select or clear the checkbox for each app to include or exclude it from monitoring.
5. Select **Save**.

#### Communication Compliance indicators

These indicators include policy indicators that detect employment stressor events, such as emotional outbursts, bullying, failure to take criticism, inability to work or communicate with a team or group, discrimination, violent threats, extremist behavior, and so on. Insider Risk Management works together with the [Microsoft Purview Communication Compliance solution](communication-compliance) to detect these types of stressors that indicate an unhealthy workplace environment. Employment stressor events can impact user behavior for risky personas (whether initiators or targets of bad behavior) in several ways that relate to insider risks. Counterproductive work behavior can be a precursor to more serious violations, such as sabotaging company assets or leaking sensitive information.

Additionally, you can choose to detect messages matching specific [sensitivity information types (SITs)](sit-sensitive-information-type-learn-about). Including sensitive information inadvertently or maliciously included in messages to user risk scores and their activity history provides investigators with more information to help quickly take actions to mitigate potential data leakage. You can select up to 30 SITs for a policy. Some scenarios might include helping to detect:

- Foreign recruitment
- State actor poaching
- Sharing sensitive information like secret formulas, financial reports, and other proprietary property
- Sharing passwords

Note

You can also [use a Communication Compliance policy as a trigger](communication-compliance-policies#integrate-communication-compliance-with-microsoft-purview-insider-risk-management).

##### How it works

You can choose from these Communication Compliance indicators:

- Sending inappropriate content
- Sending financial regulatory text that might be risky
- Sending inappropriate images

You can also choose to detect sensitive information types included in messages.

When you select **Create policy** from the **Communication Compliance indicators** section:

- A single policy is created in Communication Compliance that detects messages in Microsoft Exchange Online, Microsoft Teams, Microsoft Viva Engage, and Microsoft 365 Copilot and Microsoft 365 Copilot Chat. The Communication Compliance policy is based on the indicators and SITs you select. Each indicator is associated with specific [trainable classifiers](communication-compliance-policies#microsoft-provided-trainable-classifiers) used by Communication Compliance. For more information, see [Content safety classifiers based on large language models](communication-compliance-policies#content-safety-classifiers-based-on-large-language-models).

    Tip

    Select the information icon next to each indicator to see the trainable classifiers that the indicator uses.

    In Communication Compliance, the trainable classifiers and SITs are listed as conditions for the policy.
- The Communication Compliance policy is named "Insider risk indicator" plus the timestamp, for example: "Insider risk indicator 24-05-01T09.27.17Z" or "Insider risk SIT indicator 24-05-01T09.27.17Z".
- Anyone with the *Insider Risk Investigators* role in Insider Risk Management is automatically added as a reviewer for the Communication Compliance policy.

    Note

    After creating the Communication Compliance policy, to add a reviewer to the policy, you must add the reviewer manually to the [*Communication Compliance Investigators* role group](communication-compliance-configure#create-a-custom-policy).
- If you turn off all of the indicators in the **Policy indicators** setting, you pause the Communication Compliance policy. The policy is reenabled if you turn any of the indicators back on.
- You make the Communication Compliance indicators available for new and existing policies in Insider Risk Management that are based on the *Data theft* or *Data leaks* templates.
- If content sent in a message matches any of the trainable classifiers, it results in a policy match in Communication Compliance that can be remediated. For details, see [Investigate and remediate Communication Compliance alerts](communication-compliance-investigate-remediate#investigate-and-remediate-communication-compliance-alerts).
- Indicators included in Insider Risk Management policies determine a risk score for an in-scope user. They activate only after a triggering event occurs for a user.
- *Communication Risk* insights appear in the **Activity explorer** and **User activity** tabs in Insider Risk Management. If you drill down into a policy match from the **Activity explorer** or **User activity** tab, you can learn more about the activity and access a link that opens the Communication Compliance policy. In the Communication Compliance policy, you can see the content of the messages that were sent.

    ![Screenshot of the Insider Risk Management case Content explorer.](media/communication-compliance-link-insider-risk-management-activity-explorer.png)

    Note

    You must have the *Communication Compliance* role or the *Communication Compliance Investigators* role to access the Communication Compliance link.

##### Enable Communication Compliance indicators in Insider Risk Management

To enable Communication Compliance indicators in Insider Risk Management, complete the following steps:

1. In Insider Risk Management, go to **Settings** &gt; **Policy indicators**, then scroll to the **Communication Compliance indicators (preview)** section.
2. Under **Detect messages matching specific trainable classifiers (preview)**, select **Create policy**.

    The policy you create is in Communication Compliance, and the Communication Compliance indicators become available in the **Policy indicators** setting.

    Note

    If you already created a Communication Compliance policy but paused it, selecting **Create policy** resumes the Communication Compliance policy. In this case, the **Status** column in the Communication Compliance **Policies** list shows "Resuming".
3. Select one or more of the Communication Compliance indicators in the **Policy indicators** setting.

    Note

    If you already created a Communication Compliance policy and you select different indicators, the Communication Compliance policy changes to reflect the appropriate trainable classifiers. Turning off all indicators pauses the Communication Compliance policy.
4. Select **Save**.
5. To use the indicators, [create an insider risk management policy](insider-risk-management-configure#step-6-required-create-an-insider-risk-management-policy) or [update an existing policy](insider-risk-management-policies#update-a-policy). The indicators appear on the **Indicators** page of the policy workflow. You can adjust thresholds for the indicators as you would for any other indicators in an Insider Risk Management policy.

    Note

    At this time, real-time analytics for indicator threshold settings aren't available for the Communication Compliance indicators.

#### Data loss prevention alerts indicators

These indicators include policy indicators that integrate with [data loss prevention (DLP)](dlp-learn-about-dlp) policies. By selecting DLP policies as indicators in Insider Risk Management policies, you can automatically detect if a user has existing alerts in connected DLP policies. DLP policies help protect sensitive information and reduce the risks of oversharing data with inappropriate users or organizations.

When an Insider Risk Management alert is generated for a user, you can quickly determine if the user has any high risk alerts associated with DLP policies in your organization without having to navigate to DLP solution in the Microsoft Purview portal. You can review and evaluate the Insider Risk Management activity and associated DLP alerts within Insider Risk Management in a unified view.

##### Supported DLP workloads

The High Severity DLP Alert indicator currently supports alerts generated by DLP policies scoped to the following workloads:

| Supported workload | Description |
| --- | --- |
| **Exchange Online** | DLP policy matches on email messages |
| **SharePoint Online** | DLP policy matches on documents stored in SharePoint sites |
| **OneDrive for Business** | DLP policy matches on documents stored in OneDrive accounts |

Important

The following DLP workloads are **not** currently supported by the High Severity DLP Alert indicator. Alerts generated by DLP policies that apply exclusively to these workloads won't trigger the indicator and won't appear in Insider Risk Management alerts, cases, or activity views:

- **Endpoint DLP**: DLP policy matches on Windows and macOS devices
- **Microsoft Teams**: DLP policy matches in Teams chat and channel messages
- **Microsoft 365 Copilot**: DLP policy matches in Copilot interactions
- **On-premises repositories**: DLP policy matches on on-premises file shares and SharePoint Server
- **Power BI**: DLP policy matches in Power BI datasets

This is by design. Only DLP alerts written to the Microsoft 365 audit log by the supported workloads listed above are evaluated by Insider Risk Management. If your DLP policy spans multiple workloads (for example, Exchange + Endpoint), only the alerts from the supported workloads (Exchange Online, SharePoint Online, and OneDrive for Business) are processed.

##### Configure DLP alerts indicators

**Step 1**: To enable the DLP alerts as indicators, complete the following steps:

1. In Insider Risk Management settings, select **Policy indicators** and then select the **Built-in Indicators** tab.
2. Navigate to **Data loss prevention (DLP) indicators**
3. Select **Add DLP policies**
4. Select the DLP policies that you want to see alerts for in Insider Risk Management.
5. Select **Add**.
6. Select the **Generating alerts from selected DLP policies** checkbox.
7. Select **Save**.

**Step 2**: To assign DLP alerts indicators to a specific Insider Risk Management policy, complete the following steps:

1. [Create a custom policy](insider-risk-management-configure#step-6-required-create-an-insider-risk-management-policy) using one of the following templates:

    - Data theft by departing users
    - Data leaks
    - Data leaks by priority users
    - Data leaks by risky users
    - Risky AI usage
2. Configure the policy as applicable until you reach the **Indicators** page.
3. On the **Indicators** page, navigate to **Data loss prevention (DLP) indicators**.
4. Select the **Generating alerts from selected DLP policies** checkbox.
5. Complete the policy configuration workflow and save the new policy.

#### Device indicators

These policy indicators include activities such as sharing files over the network or with devices. Indicators include activities involving all file types, excluding executable (.exe) and dynamic link library (.dll) file activity. If you select *Device indicators*, the system processes activity for devices with Windows 10 Build 1809 or higher and macOS (three latest released versions) devices. For both Windows and macOS devices, you must onboard devices. Device indicators also include browser signal detection to help your organization detect and act on exfiltration signals for nonexecutable files viewed, copied, shared, or printed in Microsoft Edge and Google Chrome. For more information on configuring Windows devices for integration with insider risk, see Enable device indicators and onboard Windows devices. For more information on configuring macOS devices for integration with insider risk, see Enable device indicators and onboard macOS devices. For more information about browser signal detection, see [Learn about and configure Insider Risk Management browser signal detection](insider-risk-management-browser-support).

Important

Device indicators are included in [collection policy](collection-policies-solution-overview) evaluations. When you configure and deploy a collection policy, if there's a mismatch between an Insider Risk Management policy that includes device indicators and a collection policy in your organization, the collection policy configuration takes precedence. This configuration means that if you configure an Insider Risk Management policy to monitor a specific activity for devices, but you configure the collection policy to filter out that device activity, the device activity isn't collected and isn't available for review in Insider Risk Management.

#### Microsoft Defender for Endpoint indicators (preview)

These indicators come from Microsoft Defender for Endpoint and relate to unapproved or malicious software installation or bypassing security controls. To receive alerts in Insider Risk Management, you must have an active Defender for Endpoint license and insider risk integration enabled. For more information on configuring Defender for Endpoint for Insider Risk Management integration, see [Configure advanced features in Microsoft Defender for Endpoint](/en-us/windows/security/threat-protection/microsoft-defender-atp/advanced-features#share-endpoint-alerts-with-microsoft-compliance-center).

#### Health record access indicators

These policy indicators cover patient medical record access. For example, attempted access to patient medical records in your electronic medical records (EMR) system logs can be shared with Insider Risk Management healthcare policies. To receive these types of alerts in Insider Risk Management, you must have a healthcare-specific data connector and the [HR data connector](import-hr-data) configured.

#### Physical access indicators

These policy indicators cover physical access to sensitive assets. For example, attempted access to a restricted area in your physical badging system logs can be shared with Insider Risk Management policies. To receive these types of alerts in Insider Risk Management, you must have priority physical assets enabled in Insider Risk Management and the [Physical badging data connector](import-physical-badging-data) configured. To learn more about configuring physical access, see [Configure priority physical assets](insider-risk-management-settings-priority-physical-assets).

#### Microsoft Defender for Cloud Apps indicators

These policy indicators come from shared alerts from Defender for Cloud Apps. Automatically enabled anomaly detection in Defender for Cloud Apps immediately starts detecting and collating results, targeting numerous behavioral anomalies across your users and the machines and devices connected to your network. To include these activities in Insider Risk Management policy alerts, select one or more indicators in this section. To learn more about Defender for Cloud Apps analytics and anomaly detection, see [Get behavioral analytics and anomaly detection](/en-us/cloud-app-security/anomaly-detection-policy).

#### Risky Agents indicators (preview)

These policy indicators cover agent interactions with users and sensitive or risky resources. Risky agent prompts, agent generated sensitive responses, accessing sensitive or priority SharePoint files, agents accessing risky websites, or agents using tools with sensitive information are included.

#### Risky AI usage indicators (preview)

These policy indicators cover Microsoft AI tools and applications. Risky prompt behavior from users and AI-generated responses that include sensitive information are both included in these indicators. For example, attempted sharing of sensitive information in an AI tool or application by a user is considered risky activity. Similarly, an AI tool or application returning a response that contains sensitive information is also considered risky behavior.

#### Risky browsing indicators (preview)

These policy indicators cover browsing activity related to websites that are considered malicious or risky and pose potential insider risk that might lead to a security or compliance incident. Risky browsing activity refers to users who visit potentially risky websites, such as those associated with malware, pornography, violence, and other unallowed activities. To include these risk management activities in policy alerts, select one or more indicators in this section. To learn about configuring browser exfiltration signals, see [Insider Risk Management browser signal detection](insider-risk-management-browser-support).

#### Cumulative exfiltration detection indicators

These indicators detect when a user's exfiltration activities across all exfiltration channels over the last 30 days exceed organization or peer group norms. For example, if a user is in a sales role and communicates regularly with customers and partners outside of the organization, their external email activity is likely higher than the organization's average. However, the user's activity might not be unusual compared to the user's teammates, or others with similar job titles. A risk score is assigned if the user's cumulative exfiltration activity is unusual and exceeds organization or peer group norms.

Note

Peer groups are defined based on organization hierarchy, access to shared SharePoint resources, and job titles in Microsoft Entra ID. If you enable cumulative exfiltration detection, your organization agrees to share Microsoft Entra data with the Microsoft Purview portal, including organization hierarchy and job titles. If your organization doesn't use Microsoft Entra ID to maintain this information, detection might be less accurate.

#### Risk score boosters

These indicators raise the risk score for activity for the following reasons:

- *Activity that is above the user's usual activity for that day*: Scores are boosted if the detected activity deviates from the user's typical behavior.
- *User had a previous case resolved as a policy violation*: Scores are boosted if the user had a previous case in Insider Risk Management that was resolved as a policy violation.
- *User is a member of a priority user group*: Scores are boosted if the user is a member of a priority user group.
- *User is detected as a potential high impact user*: When you enable this indicator, users are automatically flagged as potential high-impact users based on the following criteria:

    - The user interacts with more sensitive content compared to others in the organization.
    - The user's level in the organization's Microsoft Entra hierarchy.
    - The total number of users reporting to the user based on the Microsoft Entra hierarchy.
    - The user is a member of a Microsoft Entra built-in role with elevated permissions.

    Note

    When you enable the potential high impact user risk score booster, you agree to share Microsoft Entra data with the Microsoft Purview portal. If your organization doesn't use sensitivity labels or has not configured organization hierarchy in Microsoft Entra ID, this detection might be less accurate. If a user is detected as both a member of a priority user group and also a potential high-impact user, their risk score is only boosted once.

In some cases, you might want to limit the insider risk policy indicators that apply to insider risk policies in your organization. You can turn off the policy indicators for specific areas by disabling them from all insider risk policies in global settings. You can only modify triggering events for policies created from the *Data leaks* or *Data leaks by priority users* templates. Policies created from all other templates don't have customizable triggering indicators or events.

### Custom indicators

Use the **Custom Indicators** tab to create a custom indicator to use as a trigger or as a policy indicator in your policies.

Note

To create a custom indicator to import third-party indicator data, you must first create an [Insider Risk Indicators connector](import-insider-risk-indicators) (preview).

1. In Insider Risk Management settings, select **Policy indicators** and then select the **Custom Indicators** tab.
2. Select **Add custom indicator**.
3. Enter an indicator name and a description (optional).
4. In the **Data connector** list, select the Insider Risk Indicator connector that you created previously.

    When you select a data connector:

    - The name of the source column that you select when you create the connector appears in the **Source column from mapping file** field. If you don't select a source column when you create the connector, **None** appears in this field and you don't need to make a selection.
    - In the **Values in source column** list, select the value that you want to assign to the custom indicator. These values relate to the source column that you specified when you created the connector. For example, if you create a single connector that includes data for two indicators (Salesforce and Dropbox), you see those values in the list.
5. If you want to use a column to set threshold values, in the **Data from mapping file** list, select the column that you want to use for the threshold setting; otherwise, select the **Use only as a triggering event without any thresholds** option.

    Note

    Only fields that have a *Number* data type appear in the **Data from mapping file** list, since a *Number* data type is required to set a threshold value. The data type is specified when you set up the connector.
6. Select **Add indicator**. The indicator is added to the **Custom Indicators** list.

Now you can [add the custom indicator to an insider risk policy](insider-risk-management-configure#step-6-required-create-an-insider-risk-management-policy) in any *Data theft* or *Data leaks* policies that you create or edit.

- If you use the custom indicator as a trigger, select your custom trigger on the **Triggers** page when you create or edit the policy.
- If you use the custom indicator as a policy indicator, select your custom indicator on the **Indicators** page when you create or edit the policy.

Note

After selecting your custom trigger or indicator, make sure to set a custom threshold (don't use the default thresholds). You can't set trigger thresholds on a custom indicator if you select the **Use only as a triggering event without any thresholds** option.

After adding the custom indicator to your policies, the triggers and insights generated based on the custom indicators appear in the **Alerts dashboard**, **Activity explorer**, and **User timeline**.

Important

Wait 24 hours before [running the sample script to upload your data](import-insider-risk-indicators#step-4-run-the-sample-script-to-upload-your-data) after you update the custom indicators and the associated policies. It can take several hours to sync all components. If you immediately upload the data while the updates are syncing, some data might not be scored for risk.

## Create a variant of a built-in indicator

You can [create detection groups](insider-risk-management-settings-detection-groups) and use them with variants of built-in indicators to tailor detections for different sets of users. For example, to reduce the number of false positives for email activities, you might want to create a variant of the *Sending email with attachments to recipients outside the organization* built-in indicator to only detect email sent to personal domains. A variant inherits all the properties of the built-in indicator. You can modify the variant with exclusions or inclusions.

1. In Insider Risk Management settings, select **Policy indicators**.
2. Select **New indicator variant (preview)**. This step opens the **New indicator variant (preview)** pane on the right side of the screen.
3. In the **Base indicator** list, select the indicator that you want to create a variant for.

    Note

    You can create up to ten variants for each built-in indicator and a total of 100 variants across all indicators. If you already created ten variants for a particular built-in indicator, the built-in indicator appears grayed out in the list. Some built-in indicators (Microsoft Defender for Endpoint indicators, for example) don't support variants.
4. Add a name for the variant (or accept the suggested name). A variant name can't be more than 110 characters.
5. Add a description for the variant (optional). The description appears in the policy to help you differentiate it from other indicators or indicator variants. A description for a variant can't be more than 256 characters.
6. Under **Detection group**, select one of the following options:

    - **Ignore activity involving items in selected groups**. Select this option if you want to capture everything except for a few *exclusions*. For example, you might want to use this option to capture all outgoing email except for email sent to specific domains.
    - **Only detect activity involving items in selected groups**. Select this option if you want to specify *inclusions* to capture. For example, select this option if you want to capture only email sent to certain domains.

    Note

    If you didn't already [create a detection group](insider-risk-management-settings-detection-groups), you can't select an option in the **Detection group** section.
7. In the **Select one or more detection groups** list, select the detection groups that you want to apply to the variant. Detection groups are listed under the appropriate detection type heading to help you find the appropriate group. For a single variant, you can add up to five detection groups of a single type. For example, you can add up to five groups of domains, five groups of file types, and so on.

    Note

    Only detection groups that are applicable to the variant appear in the list. For example, a file type detection group won't appear for the *Sharing SharePoint folders with people outside the organization* indicator since it's not applicable.
8. Select **Save**.
9. In the **Next steps** dialog box, if you want to apply the new variant to a specific policy, select the **Policies page** link.

Tip

To make sure that a variant captures all the important activities that you want to detect, you can apply the built-in indicator and the variant of the built-in indicator in the same policy. You can then observe the activities that each indicator captures in alerts and then use only the variant indicator after making sure everything is detected.

### Use a variant in a policy

To use an indicator variant in a policy, complete the following steps:

1. Go to the **Indicators** page of the policy workflow.
2. Find the built-in indicator that includes one or more variants. A small blue box in the variant checkbox marks built-in indicators that have variants. A list appears at the end of the indicator descriptor text to show the number of selected variants. Open the list to see the variants.

    Note

    If you select one or more checkboxes in the variant list, the first-level checkbox for the built-in indicator becomes a solid blue checkbox. If you don't select any of the boxes in the variant list, the first-level checkbox is blank.
3. Select **Next**.
4. In the **Customize thresholds** page, you can customize threshold values for variants individually.

### Investigate insights provided by variants

When you add variants to policies, the dashboard generates alerts. An investigator can view more details in the **Activity explorer** and **User activity** tabs.

### Edit a variant

To edit an existing variant, complete the following steps:

1. Select the blue text at the end of the indicator description text. For example, select **+2** variants as shown in the following screenshot example.

    ![Screenshot showing variant text to select.](media/insider-risk-management-settings-granular-exclusions-edit-variant.png)
2. In the **View/edit indicators** page, select **Edit**.
3. Make your changes.

### Variant limitations

- You can create up to ten variants for each built-in indicator and a total of 100 variants across all indicators.
- You can add up to five detection groups of a single type for a single variant. For example, you can add a maximum of five groups of domains, five groups of file types, and so on.
- Variants don't support sequences, cumulative exfiltration activities, the risk score booster, or real-time analytics for the detections group preview.

### How variants are prioritized against global exclusions and priority content

Insider Risk Management scopes activities in the following priority order:

1. Global exclusions
2. Variant scoping exclusion/inclusion
3. Priority content

## Enable device indicators and onboard Windows devices

To enable the detection of risk activities on Windows devices and include policy indicators for these activities, your Windows devices must meet the following requirements, and you must complete the following onboarding steps. [Learn more about device onboarding requirements](device-onboarding-overview)

### Step 1: Prepare your endpoints

Make sure that the Windows 10 devices you plan to report in Insider Risk Management meet these requirements.

1. The device must run Windows 10 x64 build 1809 or later and have the [Windows 10 update (OS Build 17763.1075)](https://support.microsoft.com/help/4537818/windows-10-update-kb4537818) from February 20, 2020 installed.
2. The user account used to sign in to the Windows 10 device must be an active Microsoft Entra account. The Windows 10 device might be [Microsoft Entra ID](/en-us/azure/active-directory/devices/concept-azure-ad-join), Microsoft Entra hybrid, joined, or registered.
3. Install the Microsoft Edge browser on the endpoint device to detect actions for the cloud upload activity. See [Download the new Microsoft Edge based on Chromium](https://support.microsoft.com/help/4501095/download-the-new-microsoft-edge-based-on-chromium).

Note

Endpoint DLP now supports virtualized environments, which means that the Insider Risk Management solution supports virtualized environments through endpoint DLP. [Learn more about support for virtualized environments in endpoint DLP](endpoint-dlp-getting-started#endpoint-dlp-support-for-virtualized-environments)

### Step 2: Onboard devices

To detect Insider Risk Management activities on a device, you must enable device checking and onboard your endpoints. You perform both actions in Microsoft Purview.

To enable devices that you didn't onboard yet, download the appropriate script and deploy it as outlined in this article.

If you already onboarded devices into [Microsoft Defender for Endpoint](/en-us/windows/security/threat-protection/), they appear in the managed devices list.

### Onboard devices

Use this deployment scenario to enable devices that aren't onboarded yet when you want to detect insider risk activities on Windows devices.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page.
3. Under **Device onboarding**, select **Devices**. The list is empty until you onboard devices.
4. Select **Turn on device onboarding**.

    Note

    While it usually takes about 60 seconds to enable device onboarding, allow up to 30 minutes before engaging with Microsoft Support.
5. Select how you want to deploy to these devices from the **Deployment method** list, then select **Download package**.
6. Follow the appropriate procedures in [Onboarding tools and methods for Windows machines](/en-us/windows/security/threat-protection/microsoft-defender-atp/configure-endpoints). This link takes you to a landing page where you can access Microsoft Defender for Endpoint procedures that match the deployment package you selected in step 5:

    - Onboard Windows machines using Group Policy
    - Onboard Windows machines using Microsoft Endpoint Configuration Manager
    - Onboard Windows machines using Mobile Device Management tools
    - Onboard Windows machines using a local script
    - Onboard non-persistent virtual desktop infrastructure (VDI) machines

When you finish and onboard the endpoint device, it appears in the devices list. The endpoint device starts reporting audit activity logs to Insider Risk Management.

Note

This experience is under license enforcement. Without the required license, data isn't visible or accessible.

### If devices are already onboarded to Microsoft Defender for Endpoint

If you already deployed Microsoft Defender for Endpoint and endpoint devices are reporting in, the endpoint devices appear in the managed devices list. To expand coverage, onboard new devices into Insider Risk Management by going to Step 2: Onboarding devices.

## Enable device indicators and onboard macOS devices

You can onboard macOS devices (Catalina 10.15 or later) into Microsoft 365 to support Insider Risk Management policies by using either Intune or JAMF Pro. For more information and configuration guidance, see [Onboard macOS devices into Microsoft 365 overview (preview)](device-onboarding-macos-overview).

## Indicator level settings

When you create a policy by using the policy workflow, you can configure how the daily number of risk events influences the risk score for insider risk alerts. These indicator settings help you control how the number of occurrences of risk events in your organization affect the risk score and the associated alert severity for these events.

For example, suppose you decide to enable SharePoint indicators in the insider risk policy settings and select custom thresholds for SharePoint events when configuring indicators for a new insider risk *Data leaks* policy. In the insider risk policy workflow, you configure three different daily event levels for each SharePoint indicator to influence the risk score for alerts associated with these events.

For the first daily event level, set the threshold to:

- *10 or more events per day* for a lower impact to the risk score for the events
- *20 or more events per day* for a medium impact to the risk score for the events
- *30 or more events per day* for a higher impact to the risk score for the events

These settings mean:

- If there are 1-9 SharePoint events that take place after the triggering event, risk scores are minimally impacted and tend not to generate an alert.
- If there are 10-19 SharePoint events that take place after a triggering event, the risk score is inherently lower and alert severity levels tend to be at a low level.
- If there are 20-29 SharePoint events that take place after a triggering event, the risk score is inherently higher and alert severity levels tend to be at a medium level.
- If there are 30 or more SharePoint events that take place after a triggering event, the risk score is inherently higher and alert severity levels tend to be at a high level.

Another option for policy thresholds is to assign the policy triggering event to risk management activity that is over the typical daily number of users. Instead of being defined by specific threshold settings, each threshold is dynamically customized for anomalous activities detected for in-scope policy users. If threshold activity for anomalous activities is supported for an individual indicator, you can select **Activity is above user's usual activity for the day** in the policy workflow for that indicator. If this option isn't listed, anomalous activity triggering isn't available for the indicator. If the **Activity is above user's usual activity for the day** option is listed for an indicator, but isn't selectable, you need to enable this option in **Insider risk settings** &gt; **Policy indicators**.

### Use real-time analytics recommendations to set thresholds

Use real-time analytics (preview) to get a guided, data-driven threshold configuration experience. With this experience, you can quickly select the right thresholds for policy indicators. The guided experience helps you efficiently adjust the selection of indicators and thresholds for activity occurrences so you don't have too few or too many policy alerts.

When you turn on analytics:

- The **Apply thresholds specific to your users' activity** option is enabled on the **Indicators** page of the policy workflow. Select this option if you want Insider Risk Management to provide indicator threshold recommendations based on the previous 10 days of user activity in your organization.

    Note

    To use this option, you must select at least one built-in policy indicator. Insider Risk Management doesn't provide recommended thresholds for [custom indicators](insider-risk-management-settings-policy-indicators#custom-indicators) or [variants of built-in indicators](insider-risk-management-settings-detection-groups).
- If you select the **Choose your own thresholds** option on the **Indicators** page of the policy workflow, the defaults for the threshold settings are based on recommended threshold values (based on activity in your organization) instead of the built-in default values. You also see a gauge, a list of the top five indicators, and insights for each indicator.

    ![Insider Risk Management real-time analytics](media/insider-risk-management-real-time-analytics.png)

    - **A.** The gauge shows the approximate number of scoped users whose activities from the previous 10 days exceeded the *lowest daily thresholds* for at least one of the selected built-in indicators for the policy. This gauge helps you estimate the number of alerts that might be generated if all users included in the policy were assigned risk scores.
    - **B.** The top five indicators list is sorted by the number of users exceeding the *lowest daily thresholds*. If your policies generate too many alerts, focus on these indicators to reduce "noise."
    - **C.** Insights for each indicator are displayed for the set of threshold settings for that indicator. The insight shows the approximate number of users whose activities from the previous 10 days exceeded the specified *low thresholds* for the indicator. For example, if the low threshold setting for *Downloading content from SharePoint* is set to 100, the insight shows the number of users in the policy who performed more than 100 download activities on average in the previous 10 days.

Note

[Global exclusions (intelligent detections)](insider-risk-management-settings-intelligent-detections) are taken into account for real-time analytics.

#### Adjust threshold settings manually

If you select the **Choose your own thresholds** option and manually adjust a threshold setting for a specific indicator, the insight for the indicator updates in real time. This feature helps you configure the appropriate thresholds for each indicator to achieve the highest level of alert effectiveness before activating your policies.

To save time and make it easier to understand the impact of manual changes to threshold values, select the **View impact** link in the insight to display the **Users exceeding daily thresholds for indicator** graph. This graph provides sensitivity analysis for each policy indicator.

![Screenshot of the Insider Risk Management View impact graph.](media/insider-risk-management-sensitivity-analysis-graph.png)

Important

This graph isn't available if you select the **Include specific users** option when you create the policy. You must select the **Include all users and groups** option.

Use this graph to analyze the activity patterns of users in your organization for the selected indicator. For example, in the preceding illustration, the threshold indicator for *Sharing SharePoint files with people outside the organization* is set to **38**. The graph shows how many users performed actions that exceeded that threshold value and the distribution of low, medium, and high severity alerts for those actions. Select a bar to see insights for each value. For example, in the previous illustration, the bar for the **50** value is selected and the insight shows that at that threshold value, approximately 22 users each performed at least 50 events on at least one day in the past 10 days.

#### Prerequisites for using real-time analytics

To use real-time analytics (preview), you must [enable insider risk analytics insights](insider-risk-management-configure#step-3-optional-enable-and-view-insider-risk-analytics-insights). After you enable analytics, it can take 24 to 48 hours for insights and recommendations to appear.