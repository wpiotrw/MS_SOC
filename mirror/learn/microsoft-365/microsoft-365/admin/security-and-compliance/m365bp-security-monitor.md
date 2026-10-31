---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Monitor Microsoft 365 Business Premium and Defender for Business - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365bp-security-monitor?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: vpattnaik
author: vpattnai
manager: dansimp
audience: Admin
ms.topic: how-to
ms.service: m365-core
ms.subservice: security
ms.date: 2025-08-14T00:00:00.0000000Z
ms.localizationpriority: medium
ms.collection:
- M365-Campaigns
- m365solution-smb
- highpri
- m365-security
- tier2
- essentials-manage
- trust-pod
ms.custom:
- MiniMaven
- compliance
search.appverid:
- BCS160[Email and calendars](#email-and-calendars)
- MET150
description: Use this article as a security operations (SecOps) guide to monitor and maintain security in Microsoft 365 Business Premium and Microsoft Defender for Business.
locale: en-us
document_id: 391361f4-edb7-7a88-e032-c4e4481b2937
document_version_independent_id: 391361f4-edb7-7a88-e032-c4e4481b2937
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/security-and-compliance/m365bp-security-monitor.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/security-and-compliance/m365bp-security-monitor
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/security-and-compliance/m365bp-security-monitor.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c671beaa-a830-4c9f-aceb-97379ee031ca
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b11ae577-8d18-47ab-998c-ea182a941e71
- https://authoring-docs-microsoft.poolparty.biz/devrel/cd48b104-e308-4e08-a405-66f04a7df418
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/8921374c-4dbe-4ed0-b011-a39e18bfbd98
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/87b1d24d-826d-4337-90a0-b6c35e4561f2
- https://authoring-docs-microsoft.poolparty.biz/devrel/ac23bdb5-c078-4620-8ee2-60eba45e97f8
platformId: 3a9d0a3b-941f-119b-6a60-7375489f0c2b
---

# Monitor Microsoft 365 Business Premium and Defender for Business - Microsoft 365 admin | Microsoft Learn

In Microsoft 365 Business Premium or the standalone version of [Microsoft Defender for Business](/en-us/defender-business/mdb-overview), you need to prepare a plan for security maintenance and security operations. It's important to keep your systems, devices, user accounts, and security policies up to date to help protect against attacks. You can use this article as a guide to prepare your plan.

Security tasks are typically done by members of the Security Administrators and Security Operators roles. For more information, see the following articles:

- [Learn more about admin roles](../add-users/about-admin-roles)
- [Assign security roles and permissions](/en-us/defender-business/mdb-roles-permissions)

Tip

For information about general maintenance tasks in Business Premium, see [Maintain Microsoft 365 Business Premium](/en-us/microsoft-365/business-premium/m365bp-mdb-maintain-environment).

## Daily security tasks

| Task | Description |
| --- | --- |
| **Check the Microsoft Defender Vulnerability Management dashboard** | Get a snapshot of the vulnerability of your organization to cybersecurity threats. A high exposure score means your organization is more vulnerable to exploitation.  To check your score, do the following steps: <br>1. In the Microsoft Defender portal, go to the **Microsoft Defender Vulnerability Management dashboard** at https://security.microsoft.com/tvm_dashboard/Endpoint.<br>2. On the **Microsoft Defender Vulnerability Management dashboard** page, go to the **Organization exposure score** card. A higher exposure score means your devices are more vulnerable to exploitation.<br>3. Select **Improve score** to see more details and security recommendations to improve (lower) your exposure score.<br><br> Awareness of your exposure score helps you to: <br>- Quickly understand and identify high-level takeaways about the state of security in your organization.<br>- Detect and respond to areas that require investigation or action to improve the current state.<br>- Communicate with peers and management about the results of security efforts.<br><br> For more information, see [Use your vulnerability management dashboard in Microsoft Defender for Business](/en-us/defender-business/mdb-view-tvm-dashboard). |
| **Review pending actions in the Action center** | As threats are detected, remediation actions come into play. Depending on the threat and your security settings configuration, remediation actions are taken automatically or only after approval, so you need to regularly monitor remediation actions.  To check pending actions, do the following steps: <br>1. In the Defender portal, go to the **Action Center** page at https://security.microsoft.com/action-center/.<br>2. On the **Action Center** page, use the **Pending** tab to view and approve or reject any pending actions. Actions on the **Pending** tab can arise from anti-virus protection, anti-malware protection, automated investigations, manual response activities, or live response sessions.<br>3. Use the **History** tab to view completed actions.<br><br> For more information, see [Review remediation actions in the Action center](/en-us/defender-business/mdb-review-remediation-actions). |
| **Review devices with threat detections** | Learn about threat detections on devices so you can promptly take any required actions (for example, isolate the device).  To review devices with threat detections, do the following steps: <br>1. In the Defender portal, go to the **Security report** page at https://security.microsoft.com/reports.<br>2. On the **Security report** page, use the information in the **Devices** section to see detected threats and details about detected malware on devices.<br><br> For more information, see [Security report](/en-us/defender-business/mdb-reports#security-report). |
| **Check incidents and alerts** | Incidents are created as threats are detected and alerts are triggered.  To check your incidents and alerts, do the following steps: <br>1. In the Defender portal, go to the **Incidents** page at https://security.microsoft.com/incidents.<br>2. On the **Incidents** page. incidents and the associated alerts are displayed.<br>3. When you select an incident from the list, a details flyout opens where you can learn more about the alert. The details flyout contains the alert title, a list of affected assets (for example, endpoints or user accounts), available actions, links to view more information, and a link to an alert details page.<br><br> For more information, see [View and manage incidents in Microsoft Defender for Business](/en-us/defender-business/mdb-view-manage-incidents). |
| **Run a scan or automated investigation** | You can initiate a scan or an automated investigation on a device that has a high risk level or detected threats. Depending on the results, remediation actions are taken automatically or after approval.  To run a scan or automated investigation on a device, do the following steps: <br>1. In the Defender portal, go to the **Device inventory** page at https://security.microsoft.com/machines.<br>2. On the **Device inventory** page, select a device from the list by clicking anywhere in the row other than the check box or the **Name** value.<br>3. At the top of the devices details flyout that opens, select ![](../../media/m365-cc-sc-more-actions-icon.png)**More actions**, and then select ![](../../media/m365-cc-sc-link-alert-icon.png)**Run antivirus scan** or ![](../../media/m365-cc-sc-initiate-automated-investigation-icon.png)**Initiate Automated Investigation**.<br><br> For more information, see [Manage devices in Microsoft Defender for Business](/en-us/defender-business/mdb-manage-devices). |

## Weekly security tasks

| Task | Description |
| --- | --- |
| **Monitor and improve your Microsoft Secure Score** | Microsoft Secure Score is a measurement of your organization's security posture. Higher numbers indicate your organization needs fewer improvement actions. By using Secure Score, you can: <br>- Report on the current state of your organization's security posture.<br>- Improve your security posture by providing discoverability, visibility, guidance, and control.<br>- Compare with benchmarks and establish key performance indicators (KPIs).<br><br> To check your score, do the following steps: <br>1. In the Defender portal, go to the **Microsoft Secure Score** page at https://security.microsoft.com/exposure-secure-score.<br>2. On the **Microsoft Secure Score** page, review and make decisions about the remediations and actions in order to improve your overall Microsoft secure score.<br><br> For more information, see [Assess your security posture with Microsoft Secure Score](/en-us/defender-xdr/microsoft-secure-score-improvement-actions). |
| **Monitor and improve your Microsoft Secure Score for Devices** | Remediate issues using the security recommendations list. As you do, your Microsoft Secure Score for Devices improves and your organization becomes more resilient against cybersecurity threats and vulnerabilities.  To check your secure score for devices, do the following steps: <br>1. In the Microsoft Defender portal, go to the **Microsoft Defender Vulnerability Management dashboard** at https://security.microsoft.com/tvm_dashboard/Endpoint.<br>2. On the **Microsoft Defender Vulnerability Management dashboard** page, go to the **Microsoft Secure Score for Devices** card, and then do one of the following steps to open the **Security recommendations**page:<br>    - Select the data in one of the available categories (for example, **Application**, **OS**, **Network**, \*\*Accounts, or **Security controls**) to open the **Security recommendations** page filtered by that category.<br>    - Select **Improve score** to open the the **Security recommendations** page unfiltered<br>3. On the **Security recommendations** page, select an entry from the list. The details flyout that opens has **General** **Remediation options**, and **Exposed devices** tabs that contain details related to the recommendation.<br>4. On the **Remediation options** tab, select **Remediation options**, fill out the form, and then select **Submit**.<br>5. Send a follow-up notification email to your security admin to approve or reject the request.<br>6. View the status of the remediation on the **Remediation** page at https://security.microsoft.com/remediation/remediation-activities.<br>/For more information, see[Use your vulnerability management dashboard in Microsoft Defender for Business](/en-us/defender-business/mdb-view-tvm-dashboard). |

## Monthly security tasks

| Task | Description |
| --- | --- |
| **Run security reports** | Many security reports are available on the **Reports** page in the Defender portal at https://security.microsoft.com/securityreports. For more information, see the following articles: <br>- [Reports in Microsoft Defender for Business](/en-us/defender-business/mdb-reports)<br>- [View email security reports in the Microsoft Defender portal](/en-us/defender-office-365/reports-email-security)<br>- [View Defender for Office 365 reports in the Microsoft Defender portal](/en-us/defender-office-365/reports-defender-for-office-365)<br>- [Mail flow reports in the new Exchange admin center in Exchange Online](/en-us/exchange/monitoring/mail-flow-reports/mail-flow-reports) |

## As needed security tasks

| Task | Description |
| --- | --- |
| **Manage false positives and false negatives** | False positives are good items identified as bad. False negatives are bad items that aren't identified as threats. False positives and false negatives happen in any threat protection solution, including Defender for Office 365 Plan 1 and Defender for Business, which are both included in Microsoft 365 Business Premium. Fortunately, you can take steps to address and reduce false positives and false negatives: <br>- **Devices**: See [Address false positives/negatives in Microsoft Defender for Endpoint](/en-us/defender-endpoint/defender-endpoint-false-positives-negatives).<br>- **Email & collaboration**: See the following articles:<br><br>- [Handle false negative email messages in Defender for Office 365](/en-us/defender-office-365/step-by-step-guides/how-to-handle-false-negatives-in-microsoft-defender-for-office-365)<br>- &gt;[Handle false positive email messages in Defender for Office 365](/en-us/defender-office-365/step-by-step-guides/how-to-handle-false-positives-in-microsoft-defender-for-office-365)<br>. |
| **Strengthen your security posture** | Defender for Business includes the **Microsoft Defender Vulnerability Management dashboard** that gives your organization an exposure score, shows information about exposed devices, and shows relevant security recommendations. Use the dashboard to reduce your organization's exposure to threats and improve your security posture.  For more information, see the following articles: <br>- [Use your vulnerability management dashboard in Microsoft Defender for Business](/en-us/defender-business/mdb-view-tvm-dashboard)<br>- [Dashboard insights](/en-us/defender-vulnerability-management/tvm-dashboard-insights)<br><br>. |
| **Adjust security policies** | Reports display information about detected threats, device status, and more. Sometimes it's necessary to adjust your security policies or apply more strict or less strict settings to specific groups of users.  For more information, see the following articles: <br>- **Devices**: See [View or edit policies in Microsoft Defender for Business](/en-us/defender-business/mdb-view-edit-create-policies).<br>- **Email & collaboration**: See the following articles:<br>[Recommended email and collaboration threat policy settings for cloud organizations](/en-us/defender-office-365/recommended-settings-for-eop-and-office365)    - [Configuration analyzer for threat policies in cloud organizations](/en-us/defender-office-365/configuration-analyzer-for-security-policies)<br>    - [Configure threat policies in Defender for Office 365](/en-us/defender-office-365/mdo-deployment-guide#step-2-configure-threat-policies) |
| **Admin submissions** | Sometimes it's necessary to submit suspicious or misjudged email messages, email attachments, or URLs to Microsoft for further analysis. Reporting these items is critical to train the system to reduce false positives and false negatives, and to improve threat detection accuracy.  For more information, see the following articles: <br>- [Submit suspected spam, phish, URLs, legitimate email getting blocked, and email attachments to Microsoft](/en-us/defender-office-365/submissions-admin)<br>[Admin review for user reported messages](/en-us/defender-office-365/submissions-admin-review-user-reported-messages) |
| **Protect priority accounts** | Accounts for executives, leaders, or other users with access to sensitive, proprietary, or high priority information are valuable targets for attackers. If compromised, these accounts pose a serious threat to the security and stability of your organization. We call these types of accounts *priority accounts*. In Business Premium, you can designate specific users as priority accounts so they receive targeted and more appropriate protections.  For more information, see the following articles: <br>- [Admin account security in Microsoft 365 for business](m365b-account-security-admins)<br>- [Security recommendations for priority accounts in Microsoft 365](/en-us/defender-office-365/priority-accounts-security-recommendations)<br>- [Manage and monitor priority accounts](../setup/priority-accounts)<br>- [User tags (priority accounts) in reports and features](/en-us/defender-office-365/user-tags-about#user-tags-in-reports-and-features) |
| **Protect high-risk devices** | The overall risk assessment of a device is based on a combination of factors (for example, the type and severity of active alerts on the device). As you resolve active alerts, approve remediation activities, and suppresses subsequent alerts, the risk level decreases.  For more information, see [Manage devices in Microsoft Defender for Business](/en-us/defender-business/mdb-manage-devices). |
| **Onboard or offboard devices** | As you replace or retire devices, purchase new devices, or your business needs change, you can onboard or offboard devices from Defender for Business. For more information, see the following articles: <br>- &gt;[Onboard devices to Microsoft Defender for Business](/en-us/defender-business/mdb-onboard-devices)<br>- [Offboard devices from Microsoft Defender for Business](/en-us/defender-business/mdb-offboard-devices) |
| **Remediate an item** | Several remediation actions are available. Some actions are taken automatically, and others await approval. <br>1. In the Defender portal, go to the **Device inventory** page at https://security.microsoft.com/machines.<br>2. On the **Device inventory** page, select a device from the list by clicking anywhere in the row other than the check box or the **Name** value (for example, select a device with a higher **Risk level** or **Exposure level** value).<br>3. At the top of the devices details flyout that opens, select ![](../../media/m365-cc-sc-more-actions-icon.png)**More actions**, and then select and available action. For example, you might select ![](../../media/m365-cc-sc-link-alert-icon.png)**Run antivirus scan** or ![](../../media/m365-cc-sc-initiate-automated-investigation-icon.png)**Initiate Automated Investigation**.<br><br> For more information, see [Manage devices in Microsoft Defender for Business](/en-us/defender-business/mdb-manage-devices). |

## Remediation actions for devices

The following table summarizes remediation actions that are available for devices in Microsoft 365 Business Premium and Defender for Business:

| Source | Actions |
| --- | --- |
| **Automated investigations** | - Quarantine a file<br>- Remove a registry key<br>- Kill a process<br>- Stop a service<br>- Disable a driver<br>- Remove a scheduled task |
| **Manual response actions** | - Run antivirus scan<br>- Isolate device<br>- Add an indicator to block or allow a file |
| **Live response** | - Collect forensic data<br>- Analyze a file<br>- Run a script<br>- Send a suspicious entity to Microsoft for analysis<br>- Remediate a file<br>- Proactively hunt for threats |