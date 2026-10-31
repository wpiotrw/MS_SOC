---
layout: Conceptual
title: Get started with Insider Risk Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-configure
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Configure Insider Risk Management in your organization.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: get-started
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-11-14T00:00:00.0000000Z
audience: itpro
ms.collection:
- highpri
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- highpri
ms.custom:
- admindeeplinkCOMPLIANCE
- sfi-ga-nochange
locale: en-us
document_id: 9ae0ab35-8913-1821-5588-6481b8303445
document_version_independent_id: 9ae0ab35-8913-1821-5588-6481b8303445
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-configure.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-configure
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-configure.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 66f7c5b0-e0e8-3df7-7fa0-d61dc8477d47
---

# Get started with Insider Risk Management | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Use Insider Risk Management policies to identify risky activities and management tools to act on risk alerts in your organization. Complete the following steps to set up prerequisites and configure an Insider Risk Management policy.

Important

The Insider Risk Management solution provides a tenant-level option to help customers facilitate internal governance at the user level. Tenant-level administrators can set up permissions to provide access to this solution for members of your organization and set up data connectors in the Microsoft Purview portal to import relevant data to support user-level identification of potentially risky activity. Customers acknowledge insights related to the individual user's behavior, character, or performance materially related to employment can be calculated by the administrator and made available to others in the organization. In addition, customers acknowledge that they must conduct their own full investigation related to the individual user's behavior, character, or performance materially related to employment, and not just rely on insights from the Insider Risk Management service. Customers are solely responsible for using the Insider Risk Management service, and any associated feature or service in compliance with all applicable laws, including laws relating to individual user identification and any remediation actions.

For more information about how insider risk policies can help you manage risk in your organization, see [Learn about Insider Risk Management](insider-risk-management).

## Subscriptions and licensing

Before getting started with Insider Risk Management, confirm your [Microsoft 365 subscription](https://www.microsoft.com/microsoft-365/compare-all-microsoft-365-plans) and any add-ons. To access and use Insider Risk Management, administrators need to verify their organization has a supported subscription and assign the appropriate licenses to users. For more information about subscriptions and licensing, see the [subscription requirements](https://aka.ms/M365EnterprisePlans) for Insider Risk Management.

Important

Insider Risk Management is currently available in tenants hosted in geographical regions and countries supported by Azure service dependencies. To verify that Insider Risk Management is supported for your organization, see [Azure dependency availability by country/region](/en-us/troubleshoot/azure/general/dependency-availability-by-country).

If you don't have an existing Microsoft 365 Enterprise E5 plan and want to try Insider Risk Management, you can [add Microsoft 365](/en-us/microsoft-365/commerce/try-or-buy-microsoft-365) to your existing subscription or [sign up for a trial](https://www.microsoft.com/microsoft-365/enterprise) of Microsoft 365 Enterprise E5.

## Pay-as-you-go billing

Some indicators included in Insider Risk Management are only available if you enable the [pay-as-you-go billing model](purview-billing-models) for your organization. For more information, see [Configure policy indicators in Insider Risk Management](insider-risk-management-settings-policy-indicators#built-in-indicators-vs-custom-indicators).

This feature uses pay-as-you-go billing or per-user licensing for Microsoft Purview capabilities or both. To help you understand and manage your usage, Microsoft Purview provides a **Usage center** in the Microsoft Purview portal. For more information, see [Manage pay-as-you-go and per-user licensing usage](purview-billing-usage). To learn more about Purview billing, see [Purview billing models.](purview-billing-models).

## Recommended actions

Recommended actions can help your organization quickly get started with Insider Risk Management. Recommended actions, which are included on the **Overview** page, help guide you through the steps to configure and deploy policies.

![Insider Risk Management recommended actions.](media/insider-risk-recommended-actions.png)

The following recommendations help you get started with or maximize your Insider Risk Management configuration:

- **Turn on auditing**: When turned on, Microsoft 365 records user and admin activity in your organization to the audit log. Insider risk policies and analytics scans use this log to detect risk activities.
- **Get permissions to use Insider Risk Management**: The level of access you have to Insider Risk Management features depends on which role group you're assigned. To access and configure recommended actions, users must be assigned to the *Insider Risk Management* or *Insider Risk Management Admins* role groups.
- **Choose policy indicators**: Indicators are essentially the risk management activities you want to detect and investigate. You can choose indicators to detect activity across several Microsoft 365 locations and services.
- **Scan for potential insider risks**: Run an analytics scan to discover potential insider risks occurring in your organization. After evaluating results, review recommended policies to set up.
- **Assign permissions to others**: If there are additional team members who are responsible for managing insider risk features, assign them to the appropriate role groups.
- **Create your first policy**: To receive alerts on potentially risky activities, set up policies based on predefined templates that define the user activities you want to detect and investigate.
- **Configure data risk graph**: Use data risk graph to view connections between assets, users, and their activities using an interactive graph experience.

Each recommended action included in this experience has four attributes:

- **Action**: Name and description of the recommended action.
- **Status**: Status of the recommended action. Values are *Not started*, *In progress*, *Saved for later*, or *Completed*.
- **Required or optional**: Whether the recommended action is required or optional for Insider Risk Management features to function as expected.
- **Estimated time to complete**: Estimated time to complete the recommended action in minutes.

Select a recommendation from the list to get started with configuring Insider Risk Management. Each recommended action guides you through the required action for the recommendation, including any requirements, what to expect, and the impact of configuring the feature in your organization. Each recommended action is automatically marked as complete when configured or you can manually select the action as complete when configured.

## Step 1 (required): Assign permissions for Insider Risk Management

To use any of the Insider Risk Management-related tools in the Microsoft Purview portal, users need the appropriate permissions. The easiest way to assign roles is to add the user to the appropriate role group on the **Role groups** page in the [Microsoft Purview portal](purview-portal).

For step-by-step guidance, see [Assign permissions in Insider Risk Management](insider-risk-management-permissions).

## Step 2 (required): Enable the Microsoft 365 audit log

Insider Risk Management uses Microsoft 365 audit logs for user insights and risk management activities identified in policies and analytics insights. The Microsoft 365 audit logs are a summary of all activities within your organization and Insider Risk Management policies might use these activities for generating policy insights.

Auditing is enabled for Microsoft 365 organizations by default. Some organizations might have disabled auditing for specific reasons. If auditing is disabled for your organization, it might be because another administrator has turned it off. We recommend confirming that it's OK to turn auditing back on when completing this step.

For step-by-step instructions to turn on auditing, see [Turn audit log search on or off](audit-log-enable-disable). After you turn on auditing, a message is displayed that says the audit log is being prepared and that you can run a search in a couple of hours after the preparation is complete. You only have to do this action once. For more information about the using the Microsoft 365 audit log, see [Search the audit log](audit-search).

## Step 3 (optional): Enable and view insider risk analytics insights

If you enable Insider Risk Management analytics, you can:

- **Scan for potential insider risks before creating policies.** You can conduct an evaluation of potential insider risks in your organization without configuring any insider risk policies. This evaluation can help your organization identify potential areas of higher user risk and help determine the type and scope of Insider Risk Management policies you might want to configure. This evaluation might also help you determine needs for additional licensing or future optimization of existing policies. Analytics scan results might take up to 48 hours before insights are available as reports for review. To learn more about analytics insights, see [Insider Risk Management settings: Analytics](insider-risk-management-settings-analytics) and check out the [Insider Risk Management Analytics video](https://www.youtube.com/watch?v=5c0P5MCXNXk) to help understand how analytics can help accelerate the identification of potential insider risks and help you to quickly take action.
- **Receive real-time recommendations for indicator threshold settings.** Manually tuning policies to reduce "noise" can be a very time-consuming experience that requires you to do a lot of trial and error to determine the desired configuration for your policies. If analytics is turned on, Insider Risk Management can provide real-time recommendations for indicator thresholds. You can also manually adjust the provided recommendations and see in real time how many users are brought into scope of the policy based on the changes you make. [Learn more about real-time indicator threshold recommendations](insider-risk-management-settings-policy-indicators#use-real-time-analytics-recommendations-to-set-thresholds)

Note

To enable insider risk analytics, you must be a member of the *Insider Risk Management*, *Insider Risk Management Admins*, or Microsoft 365 *Global admin* role group.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

### Enable insider risk analytics

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. On the **Overview** tab, on the **Scan for insider risks in your organization** card, select **Run scan**. This action turns on analytics scanning for your organization. You can also turn on scanning by going to **Insider risk settings** &gt; **Analytics** and enabling **Scan your tenant's user activity to identify potential insider risks**.
4. On the **Analytics details** pane, select **Run scan to start the scan for your organization**. Analytics scan results might take up to 48 hours before insights are available as reports for review.

After reviewing the analytics insights, choose the insider risk policies and configure the associated prerequisites that best meet your organization's insider risk mitigation strategy.

## Step 4 (recommended): Configure prerequisites for policies

Most Insider Risk Management policies have prerequisites that you must configure for policy indicators to generate relevant activity alerts. Configure the appropriate prerequisites depending on the policies you plan to configure for your organization.

### Connect to cloud apps in Microsoft Defender

Insider Risk Management includes the following cloud indicators (preview):

- Cloud storage indicators, including Google Drive, Box, and Dropbox
- Cloud service indicators, including Amazon S3 and Azure (Storage and SQL Server)

#### Cloud storage indicators

Use cloud storage indicators to detect the following activities in Google Drive, Box, and Dropbox:

- **Discovery:** Techniques used to figure out the environment​
- **Collection:** Techniques used to gather data of interest
- **Exfiltration:** Techniques used to steal data, such as sensitive documents
- **Deletion (impact):** Techniques used to disrupt the availability or compromise the integrity of a system

#### Cloud service indicators

Use cloud service indicators to detect the following activities in Amazon S3 and Azure:

- **Defense evasion:** Techniques used to avoid detection of risky activities by disabling trace logs​ or by updating or deleting SQL Server firewall rules
- **Exfiltration:** Techniques used to steal data, such as sensitive documents
- **Deletion (impact):** Techniques used to disrupt the availability or compromise the integrity of a system
- **Privilege escalation:** Techniques used to gain higher-level permissions to systems and data

#### Prerequisites for accessing cloud indicators

To select from cloud indicators in Insider Risk Management settings and policies, you must [first connect to the relevant cloud apps in Microsoft Defender](/en-us/defender-cloud-apps/enable-instant-visibility-protection-and-governance-actions-for-your-apps), if you didn't already.

After connecting to the apps, you can find the indicators on the [Policy indicators settings](insider-risk-management-settings-policy-indicators) page and from individual policies.

### Configure Insider Risk Indicator (preview) connector

You can extend Insider Risk Management by importing detections for non-Microsoft (third-party) workloads. For example, you might want to extend your detections to include Salesforce and Dropbox activities and use them alongside the built-in detections provided by the Insider Risk Management solution, which focuses on Microsoft services like SharePoint Online and Exchange Online.

To bring your own detections to the Insider Risk Management solution, import preprocessed, aggregated detections from security information and event management (SIEM) solutions such as Microsoft Sentinel or Splunk. Import a sample file into the Insider Risk Indicators connector workflow. The connector workflow analyzes the sample file and configures the required schema.

Note

Currently, you can't import "raw" detection signals into Insider Risk Management. You can only import preprocessed aggregations as a file.

You can use a custom indicator as:

- A trigger to bring a user into the scope of a policy.
- A policy indicator to score the user for risk.

For step-by-step guidance to configure the Insider Risk Indicators connector for your organization, see the [Insider Risk Indicators connector](import-insider-risk-indicators) article. After you configure the connector, return to these configuration steps.

### Configure Microsoft 365 HR connector

Insider Risk Management supports importing user and log data imported from third-party risk management and human resources platforms. The Microsoft 365 Human Resources (HR) data connector allows you to pull in human resources data from CSV files, including user termination dates, last employment dates, performance improvement plan notifications, performance review actions, and job level change status. This data helps drive alert indicators in Insider Risk Management policies and is an important part of configuring full risk management coverage in your organization. If you configure more than one HR connector for your organization, Insider Risk Management automatically pulls indicators from all HR connectors.

The Microsoft 365 HR connector is required when using the following policy templates:

- Data leaks by risky users
- Departing user data theft
- Patient data misuse
- Security policy violations by departing users
- Security policy violations by risky users

For step-by-step guidance to configure the Microsoft 365 HR connector for your organization, see the [Set up a connector to import HR data](import-hr-data) article. After you configure the HR connector, return to these configuration steps.

### Configure a Microsoft Healthcare connector

Insider Risk Management supports importing user and log data from third-party electronic medical record (EMR) systems. The Microsoft Healthcare connector enables you to bring in activity data from your EMR system through CSV files, including improper patient record access, suspicious volume activities, and editing and exporting activities. This data helps drive alert indicators in Insider Risk Management policies and plays an important role in configuring full risk management coverage in your organization.

If you configure more than one Healthcare connector for your organization, Insider Risk Management automatically supports event and activity signals from all Healthcare connectors. The Microsoft 365 Healthcare connector is required when using the following policy template:

- Patient data misuse

For step-by-step guidance to configure a healthcare-specific connector for your organization, see [Set up a connector to import healthcare data](import-healthcare-data). After you configure a connector, return to these configuration steps.

### Configure data loss prevention (DLP) policies

Insider Risk Management supports using DLP policies to help identify the intentional or accidental exposure of sensitive information to unwanted parties for high severity level DLP alerts. When you configure an Insider Risk Management policy with any of the **Data leaks** templates, you can assign a specific DLP policy to the policy for these types of alerts.

Tip

You can also use Adaptive Protection in Insider Risk Management to dynamically apply DLP protection controls to high-risk users while maintaining productivity for lower-risk users. [Learn more about Adaptive Protection](insider-risk-management-adaptive-protection).

Data loss policies help identify users to activate risk scoring in Insider Risk Management for high severity DLP alerts for sensitive information. They're an important part of configuring full risk management coverage in your organization. For more information about Insider Risk Management and DLP policy integration and planning considerations, see [Insider Risk Management policies](insider-risk-management-policy-templates#data-leaks).

Important

Make sure you complete the following steps:

- Understand and properly configure the users included in both the DLP and Insider Risk Management policies to produce the policy coverage you expect.
- Configure the **Incident reports** setting in the DLP policy for Insider Risk Management used with these templates for *High* severity level alerts. Insider Risk Management alerts aren't generated from DLP policies with the **Incident reports** field set at *Low* or *Medium*.

A DLP policy is optional when using the following policy templates:

- Data leaks
- Data leaks by priority users

For step-by-step guidance to configure DLP policies for your organization, see [Create and Deploy data loss prevention policies](dlp-create-deploy-policy). After you configure a DLP policy, return to these configuration steps.

Note

Endpoint DLP now supports virtualized environments, which means that the Insider Risk Management solution supports virtualized environments through endpoint DLP. [Learn more about support for virtualized environments in endpoint DLP](endpoint-dlp-getting-started#endpoint-dlp-support-for-virtualized-environments).

### Configure sharing of insider risk levels with Microsoft Defender and DLP alerts

You can share insider risk levels from Insider Risk Management (preview) to bring unique user context to Microsoft Defender and DLP alerts. Insider Risk Management analyzes user activities over a period of 90-120 days and looks for anomalous behavior over that period. Adding this data to Microsoft Defender and DLP alerts enhances the data available in those solutions to help analysts prioritize alerts. [Learn more about sharing user risk severity levels with Microsoft Defender and DLP alerts](insider-risk-management-settings-share-data).

Sharing Insider Risk Management user risk severity levels also enhances the [Microsoft Security Copilot](/en-us/security-copilot/microsoft-security-copilot). For example, in Security Copilot, you might want to start by asking Copilot to summarize a DLP alert, then ask Copilot to show the insider risk level associated with the user flagged in the alert. Or you might want to ask why the user is considered a high-risk user. The user risk information in this case comes from Insider Risk Management. Security Copilot seamlessly integrates Insider Risk Management with DLP to assist with investigations. [Learn more about using the standalone version of Copilot for combined DLP/Insider Risk Management investigations](copilot-in-purview-promptbooks).

### Configure priority user groups

Insider Risk Management supports assigning priority user groups to policies to help identify unique risk activities for users with critical positions, high levels of data and network access, or a past history of risk behavior. Creating a priority user group and assigning users to the group helps scope policies to the unique circumstances presented by these users.

To enable the *priority user groups* risk score booster, go to the *Insider Risk Management settings* page, then select **Policy indicators** and **Risk score boosters**. Analysts and investigators can review and prioritize these users' risk severity to help triage alerts in accordance with your organization's risk policies and standards.

A priority user group is required when using the following policy templates:

- Security policy violations by priority users
- Data leaks by priority users

See the [Getting started with Insider Risk Management settings](insider-risk-management-settings-priority-user-groups) article for step-by-step configuration guidance.

### Configure Physical badging connector

Insider Risk Management supports importing user and log data from physical control and access platforms. The Physical badging connector lets you pull in access data from JSON files, including user IDs, access point IDs, access time and dates, and access status. This data helps drive alert indicators in Insider Risk Management policies and is an important part of configuring full risk management coverage in your organization. If you configure more than one Physical badging connector for your organization, Insider Risk Management automatically pulls indicators from all Physical badging connectors. Information from the Physical badging connector supplements other insider risk signals when using all insider risk policy templates.

Important

For Insider Risk Management policies to use and correlate signal data related to departing and terminated users with event data from your physical control and access platforms, you must also configure the Microsoft 365 HR connector. If you enable the Physical badging connector without enabling the Microsoft 365 HR connector, Insider Risk Management policies only process events for unauthorized physical access for users in your organization.

See the [Set up a connector to import physical badging data](import-physical-badging-data) article for step-by-step guidance to configure the Physical badging connector for your organization. After you configure the connector, return to these configuration steps.

### Configure Microsoft Defender for Endpoint

[Microsoft Defender for Endpoint](/en-us/windows/security/threat-protection/microsoft-defender-atp/microsoft-defender-advanced-threat-protection) is an enterprise endpoint security platform designed to help enterprise networks prevent, detect, investigate, and respond to advanced threats. To gain better visibility of security violations in your organization, you can import and filter Defender for Endpoint alerts for activities used in policies created from Insider Risk Management security violation policy templates.

If you create security violation policies, you need to configure Microsoft Defender for Endpoint in your organization and enable Defender for Endpoint for Insider Risk Management integration in the Defender Security Center to import security violation alerts. For more information about requirements, see the [Minimum requirements for Microsoft Defender for Endpoint](/en-us/windows/security/threat-protection/microsoft-defender-atp/minimum-requirements) article.

For step-by-step guidance to configure Defender for Endpoint for Insider Risk Management integration, see the [Configure advanced features in Defender for Endpoint](/en-us/windows/security/threat-protection/microsoft-defender-atp/advanced-features#share-endpoint-alerts-with-microsoft-compliance-center) article. After you configure Microsoft Defender for Endpoint, return to these configuration steps.

### Configure forensic evidence

Having visual context is crucial for security teams during forensic investigations to get better insights into risky user activities that might lead to a security incident. With customizable event triggers and built-in user privacy protection controls, forensic evidence enables customizable capturing across devices to help your organization better mitigate, understand, and respond to potential data risks like unauthorized data exfiltration of sensitive data.

For step-by-step guidance to configure forensic evidence for your organization, see the [Get started with Insider Risk Management forensic evidence](insider-risk-management-forensic-evidence-configure) article.

### Configure optical character recognition

Microsoft Purview can scan for sensitive content in documents to help protect those documents from inappropriate exposure. When you enable optical character recognition (OCR) in Microsoft Purview, data classifiers, such as sensitive information types and trainable classifiers, can also detect characters in stand-alone images. After configuring OCR settings (preview), your existing insider risk policies apply to both images and documents.

For the OCR preview, Insider Risk Management supports scanning in the following locations: Windows endpoint devices, SharePoint Online, and Teams. Exchange Online and OneDrive aren't supported for the preview.

OCR settings don't apply to forensic evidence clips in Insider Risk Management.

[Learn more about setting up OCR scanning and pay-as-you-go billing](ocr-learn-about).

## Step 5 (required): Configure insider risk settings

[Insider risk settings](insider-risk-management-settings) apply to all Insider Risk Management policies, regardless of the template you choose when creating a policy. You configure settings by using **Settings** located at the top of Insider Risk Management pages. These settings control privacy, indicators, global exclusions, detection groups, intelligent detections, and more. [Learn more about settings to consider before you creating a policy](insider-risk-management-settings).

## Step 6 (required): Create an Insider Risk Management policy

Insider Risk Management policies include assigned users and define which types of risk indicators are configured for alerts. Before potentially risky activities can trigger alerts, you must configure a policy. Use the policy workflow to create new Insider Risk Management policies.

Note

To create a custom trigger or indicator for a non-Microsoft workload, see [Custom indicators](insider-risk-management-settings-policy-indicators#custom-indicators).

### Create policy

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Policies** in the left navigation.
4. Select **Create policy** to open the policy workflow.
5. On the **Policy template** page, choose a policy category and then select the template for the new policy. These templates consist of conditions and indicators that define the risk activities you want to detect and investigate. Review the template prerequisites, triggering events, and detected activities to confirm this policy template fits your needs.

    Important

    Some policy templates have prerequisites that you must configure for the policy to generate relevant alerts. If you didn't configure the applicable policy prerequisites, see **Step 4**.

    Select **Next** to continue.
6. On the **Name and description** page, complete the following fields:

    - **Name (required)**: Enter a friendly name for the policy. You can't change this name after you create the policy.
    - **Description (optional)**: Enter a description for the policy.

    Select **Next** to continue.
7. If [admin units exist for your tenant](purview-admin-units), you see the **Admin units** page. Otherwise, you see the **Users and groups** page and can skip to the next step.

    If you want to scope the policy to one or more admin units, select **Add admin units**, then select the admin units that you want to apply to the policy.

    Note

    You can only see the admin units that are scoped to your role. If you're an unrestricted administrator, you can see all admin units for the tenant. To view a summary of the role groups and admin units that you're assigned to, select **View my permissions**.

    Select **Next** to continue.
8. On the **Users and groups** page, select one of the following options:

    - **Include all users and groups**. When you select this option, Insider Risk Management looks for triggering events for all users and groups in your organization to start assigning risk scores for the policy.

        If your policy is [scoped by one or more admin units](purview-admin-units), this option selects all users and groups within the administrative units.

        Note

        To take advantage of real-time analytics (preview) for indicator threshold settings, you must scope your policy to **Include all users and groups**. Real-time analytics enables you to see estimates of the number of users that could potentially match a given set of policy conditions in real time. This feature helps you efficiently adjust the selection of indicators and thresholds of activity occurrence so you don’t have too few or too many policy alerts. Scoping your policy to **Include all users and groups** also provides better overall protection across your tenant. For more information on real-time analytics for indicator threshold settings, [see Indicator level settings](insider-risk-management-settings-policy-indicators#indicator-level-settings).

        Note

        Insider Risk Management supports selection of following types of groups in policies - Microsoft 365 groups, Distribution groups, and Security groups (both mail-enabled and non-mail-enabled types) with a limitation that non-mail-enabled Security groups cannot be selected if your policy is [scoped by one or more admin units](purview-admin-units). For more information on different types of groups, see [Compare Groups](/en-us/microsoft-365/admin/create-groups/compare-groups).
    - **Include specific users and groups**. Select this option to define which users or groups are included in the policy.

        If your policy is [scoped by one or more admin units](purview-admin-units), you can only choose users within the admin unit scope.

        Note

        Guest accounts aren't supported.
    - **Adaptive scope**. This option appears if you select the **Include specific users and groups** option. Select **Add or edit adaptive scopes** to [apply an adaptive scope to the policy](purview-adaptive-scopes). You must create the adaptive scope before you create or edit the policy. If the policy is also [scoped by one or more admin units](purview-admin-units), the adaptive scopes available to you are limited by the admin units. [Learn how adaptive scopes work together with admin units](purview-adaptive-scopes#how-adaptive-scopes-work-with-microsoft-entra-administrative-units).
    - **Add or edit priority user groups**. This option appears only if you choose the *Data leaks by priority users* template. Select this option, then add or edit priority user groups.

        Note

        If the policy template is based on priority user groups, you can't select an [admin unit](purview-admin-units) to scope the policy. Priority user groups aren't currently supported for use with admin units.

    Select **Next** to continue.
9. Use the **Exclude users and groups (optional) (preview)** page if you want to exclude certain users or groups from the policy scope. For example, you might want to create a policy that detects potentially risky actions for people in the whole organization but excludes executive-level sales managers. Select **Add users to exclude** or **Add groups to exclude** to select the users or groups that you want to exclude. If your policy is [scoped by one or more admin units](purview-admin-units), you can only exclude users or groups that are within the admin unit scope.

    Select **Next** to continue.
10. On the **Content to prioritize** page, assign the sources to prioritize, if needed. Prioritizing these sources increases the chance of generating a high severity alert for these sources. Select one of the following choices:

    - **I want to prioritize content**. Select this option to prioritize *SharePoint sites*, *Sensitivity labels*, *Sensitive info types*, and *File extensions* content types. If you choose this option, you must select at least one priority content type.
    - **I don't want to specify priority content right now**. Select this option to skip the priority content detail pages in the workflow.

    Select **Next** to continue.
11. If you select **I want to prioritize content** in the previous step, you see the detail pages for *SharePoint sites*, *sensitivity labels*, *sensitive info types*, *file extensions*, and *Scoring*. Use these detail pages to define the SharePoint, sensitive info types, sensitivity labels, trainable classifiers, and file extensions to prioritize in the policy. The *Scoring* detail page allows you to scope the policy to only assign risk scores and generate alerts for specified activities that include priority content.

    - **SharePoint sites**: Select **Add SharePoint site** and select the SharePoint sites you have access to and want to prioritize. For example, *"group1@contoso.sharepoint.com/sites/group1"*.

        Note

        If your policy is [scoped by one or more admin units](purview-admin-units), you still see all SharePoint sites, not just SharePoint sites scoped to your admin units since admin units don't support SharePoint sites.
    - **Sensitive info type**: Select **Add sensitive info type** and select the sensitivity types you want to prioritize. For example, *"U.S. Bank Account Number"* and *"Credit Card Number"*.
    - **Sensitivity labels**: Select **Add sensitivity label** and select the labels you want to prioritize. For example, *"Confidential"* and *"Secret"*.
    - **Trainable classifiers**: Select **Add trainable classifier** and select the trainable classifiers you want to prioritize. For example, *Source code*.
    - **File extensions**: Add up to 50 file extensions. You can include or omit the '.' with the file extension. For example, *.py* or *py* would prioritize Python files.
    - **Scoring**: Decide whether to assign risk scores to all risk management activities detected by this policy or only for activities that include priority content. Choose **Get alerts for all activity** or **Get alerts only for activity that includes priority content**.

    Select **Next** to continue.
12. If you select the *Data leaks* or *Data leaks by priority users* templates, you see options on the **Triggers for this policy** page for custom-triggering events and policy indicators. You can select a DLP policy or indicators for triggering events that bring users assigned to the policy in-scope for activity scoring. If you select the **User matches a data loss prevention (DLP) policy triggering event** option, you must select a DLP policy from the DLP policy dropdown list to enable triggering indicators for the DLP Policy for this Insider Risk Management policy. If you select the **User performs an exfiltration activity triggering event** option, you must select one or more of the listed indicators for the policy triggering event.

    Note

    Priority user groups aren't currently supported for admin units. If you're creating a policy based on the *Data leaks by priority users* template or the *Security policy violations by priority users* template, you can't select admin units for scoping the policy. Unrestricted administrators can select priority user groups without selecting admin units, but restricted or scoped administrators can't create these policies at all.

    Important

    If you're unable to select a listed indicator or sequence, it's because they aren't currently enabled for your organization. To make them available to select and assign to the policy, select the **Turn on indicators** prompt.

    If you select other policy templates, custom triggering events aren't supported. The built-in policy triggering events apply. Skip to Step 15 without defining policy attributes.
13. If you select the *Data leaks by risky users* or *Security policy violations by risky users* templates, you see options on the **Triggers for this policy** page for integration with Communication Compliance and HR data connector events. You can assign risk scores when users send messages that contain potentially threatening, harassing, or discriminatory language or bring users into the policy scope after risky user events are reported in your HR system. If you select the **Risk triggers from Communication Compliance (preview)** option, you can accept the default Communication Compliance policy (automatically created), choose a previously created policy scope for this trigger, or create another scoped policy. If you select **HR data connector events**, you must configure an HR data connector for your organization.

    Select **Next** to continue.
14. If you select the *Data leaks* or *Data leaks by priority users* templates and select the **User performs an exfiltration activity and associated indicators**, you can choose custom or default thresholds for the indicator triggering events that you select. Choose either the **Use default thresholds (Recommended)** or **Use custom thresholds for the triggering events**.

    Select **Next** to continue.
15. If you select **Use custom thresholds for the triggering events**, for each triggering event indicator that you selected in Step 10, choose the appropriate level to generate the desired level of activity alerts. You can use the recommended thresholds, custom thresholds, or thresholds based on anomalous activities (for certain indicators) over the daily norm for users.

    Select **Next** to continue.
16. On the **Policy indicators** page, you see the [indicators](insider-risk-management-settings-policy-indicators) that you define as available on the **Insider risk settings** &gt; **Indicators** page [which include indicator variants if you have defined any](insider-risk-management-settings-detection-groups#create-a-detection-group). Select the indicators you want to apply to the policy.

    Important

    If indicators on this page can't be selected, select the indicators you want to enable for all policies. You can use **Turn on indicators** in the workflow or select indicators on the **Insider Risk Management** &gt; **Settings** &gt; **Policy indicators** page.

    If you select at least one *Office* or *Device* indicator, select the **Risk score boosters** as appropriate. Risk score boosters only apply for selected indicators. If you select a *Data theft* or *Data leaks* policy template, select one or more **Sequence detection** methods and a **Cumulative exfiltration detection** method to apply to the policy. If you select the *Risky browser usage* policy template, select one or more of the **Browsing indicators**.

    Select **Next** to continue.
17. On the **Decide whether to use default or custom indicator thresholds** page, choose custom or default thresholds for the policy indicators that you select. Choose either the **Use default thresholds for all indicators** or **Specify custom thresholds** for the selected policy indicators. If you select **Specify custom thresholds**, choose the appropriate level to generate the desired level of activity alerts for each policy indicator.

    Tip

    To view a graph that helps you determine appropriate threshold settings, select the **View impact** link in the insight for each set of threshold settings. [Learn more about manually customizing thresholds](insider-risk-management-settings-policy-indicators#use-real-time-analytics-recommendations-to-set-thresholds).

    Select **Next** to continue.
18. On the **Review** page, review the settings you chose for the policy and any suggestions or warnings for your selections. Select **Edit** to change any of the policy values or select **Submit** to create and activate the policy.