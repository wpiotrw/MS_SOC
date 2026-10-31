---
layout: Conceptual
title: Get started with Insider Risk Management forensic evidence | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence-configure
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Get started with Insider Risk Management forensic evidence in Microsoft Purview. Forensic evidence is an investigative tool for viewing captured security-related user activity to help determine whether the user's actions pose a risk and might lead to a security incident.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: article
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-02-27T00:00:00.0000000Z
audience: itpro
ms.collection: m365-security-compliance
locale: en-us
document_id: d9e5ca16-22eb-b083-9add-d3e53ac4fe28
document_version_independent_id: d9e5ca16-22eb-b083-9add-d3e53ac4fe28
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-forensic-evidence-configure.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-forensic-evidence-configure
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-forensic-evidence-configure.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: e33de33b-cbd3-28a5-1f15-5f830f82482a
---

# Get started with Insider Risk Management forensic evidence | Microsoft Learn

Important

Forensic evidence is an opt-in add-on feature in [Microsoft Purview Insider Risk Management](insider-risk-management) that gives security teams visual insights into potential insider data security incidents, with user privacy built in. Forensic evidence includes customizable event triggers and built-in user privacy protection controls, enabling security teams to better investigate, understand and respond to potential insider data risks like unauthorized data exfiltration of sensitive data.

Organizations set the right policies for themselves, including what risky events are highest priority for capturing forensic evidence and what data is most sensitive. Forensic evidence is off by default, policy creation requires dual authorization and usernames can be masked with pseudonymization (which is on by default for Insider Risk Management). Setting up policies and reviewing security alerts within Insider Risk Management leverages strong role-based access controls (RBAC), ensuring that the designated individuals in the organization are taking the right actions with additional auditing capabilities.

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Configuring forensic evidence in your organization is similar to configuring other policies from Insider Risk Management policy templates. In general, you follow the same basic configuration steps to set up forensic evidence, but a few areas require feature-specific configuration actions before you get started with the basic configuration steps.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

### Step 1: Confirm your subscription and configure data storage access

Before you get started with forensic evidence, confirm your [Insider Risk Management subscription](https://aka.ms/M365EnterprisePlans) and any add-ons.

Also, add the following domains to your firewall and proxy server allowlist to support forensic evidence capture storage for your organization:

#### Worldwide - Domain

```
- compliancedrive.microsoft.com
- *.events.data.microsoft.com
- officeclient.microsoft.com
- odc.officeapps.live.com
- hrd.svc.cloud.microsoft
```

#### GCC/GCC High - Domain

```
- *.compliancedrive.microsoft.us
- tb.events.data.microsoft.com
- officeclient.microsoft.com
- odc.officeapps.live.com
- hrd.svc.cloud.microsoft
```

#### DOD - Domain

```
- dod.compliancedrive.apps.mil
- pf.events.data.microsoft.com
- officeclient.microsoft.com
- odc.officeapps.live.com
- hrd.svc.cloud.microsoft
```

For more information on these endpoints, [see Microsoft 365 endpoints](/en-us/microsoft-365/enterprise/microsoft-365-endpoints).

Note

Captures and capture data are stored at these domains and are assigned only to your organization. No other Microsoft 365 organization has access to forensic evidence captures for your organization.

Forensic evidence data is stored in one region where your Exchange Online region is set.

### Step 2: Configure supported devices

To capture forensic evidence, eligible user devices must be onboarded to the [Microsoft Purview portal](purview-portal) and have the Microsoft Purview Client installed.

Important

The Microsoft Purview Client automatically collects general diagnostic data related to device configuration and performance metrics. This data includes information on critical errors, RAM consumption, process failures, and other data. This data helps us assess the client's health and identify any issues. For more details about how diagnostic data might be used, see the Use of Software with Online Services on the [Microsoft Product Terms](https://www.microsoft.com/licensing/product-licensing/products).

For a list of device and configuration requirements, see [Learn about forensic evidence](insider-risk-management-forensic-evidence#device-and-configuration-requirements). To onboard supported devices, complete the steps outlined in the [Onboard Windows 10 and Windows 11 devices into Microsoft 365 overview](device-onboarding-overview) article.

#### Install the Microsoft Purview client

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Forensic Evidence** in the left navigation, then select **Client installation**.
4. Select **Download installer package (x64 version)** to download the installation package for Windows.
5. After downloading the installation package, use your preferred method to install the client on users' devices. These options might include manually installing the client on devices or using tools to help automate the client installation:

    - **Microsoft Intune**: Microsoft Intune is an integrated solution for managing all of your devices. Microsoft brings together [Configuration Manager](/en-us/mem/configmgr/core/understand/introduction) and [Intune](/en-us/mem/intune/fundamentals/what-is-intune), without a complex migration, and with simplified licensing.
    - **Third-party device management solutions**: If your organization uses third-party device management solutions, see the documentation for these tools to install the client.

### Step 3: Configure settings

Forensic evidence has several configuration settings that provide flexibility for the types of security-related user activity captured, capturing parameters, bandwidth limits, and offline capturing options. By configuring forensic evidence capturing, you can create policies based on your requirements. Adding users to a policy requires dual authorization.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Forensic evidence** in the left navigation, then select **Forensic evidence settings**.
4. Select **Forensic evidence capturing** to enable capturing support in your forensic evidence policies. If you turn this setting off, it removes all previously added users for forensic evidence policies.

    Important

    The Microsoft Purview Client used to capture activity on users' devices is licensed under the Use of Software with the Online Services on the [Microsoft Product Terms](https://www.microsoft.com/licensing/product-licensing/products). Customers are solely responsible for using the Insider Risk Management solution, including the Microsoft Purview Client, in compliance with all applicable laws.
5. In the **Capturing window** section, define when to start and stop activity capturing. Available values are *10 seconds*, *30 seconds*, *1 minute*, *3 minutes*, or *5 minutes*.
6. In the **Upload bandwidth limit** section, define the amount of capture data to upload into your data storage account per user, per day. Available values are *100 MB*, *250 MB*, *500 MB*, *1 GB*, or *2 GB*.
7. In the **Offline capturing cache limit** section, define the maximum cache size to store on users' devices when offline capturing is enabled. Available values are *100 MB*, *250 MB*, *500 MB*, *1 GB*, or *2 GB*.
8. Select **Save**.

### Step 4: Create a policy

Forensic evidence policies define the scope of security-related user activity to capture for configured devices. You have two options for capturing forensic evidence:

- **Capture only specific activities (such as printing or exfiltrating files).** With this option, you choose the device activities to capture. You can also choose to capture activity for specific desktop apps and websites. This option lets you focus on just the activities, apps, and websites that present risk.
- **Capture all activities that approved users perform on their devices.** This option typically covers a specific period of time, such as when a particular user is potentially involved in risky activity that might lead to a security incident. All forensic evidence indicators are automatically included, such as device indicators and [Enhanced Phishing Protection indicators](insider-risk-management-forensic-evidence#feature-capabilities). To preserve capacity and user privacy, you can choose to exclude specific desktop apps and websites from the capture.

After you create a policy, include it in forensic evidence requests to control what activity to capture for users whose requests are approved.

Note

Continuous forensic policies (capturing all activities) take precedence over selective forensic evidence policies (capturing only specific activities).

#### Capture only specific activities

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Forensic evidence** in the left navigation, then select **Forensic evidence policies**.
4. Select **Create forensic evidence policy**.
5. On the **Scope** page, select **Specific activities**. This option only captures activities detected by policies that users are included in. These activities are defined by the indicators selected in forensic evidence policies. You can review captures for this option on the **Forensic evidence (preview)** tab on the **Alerts** or **Cases** dashboard.
6. Select **Next**.
7. On the **Name and description** page, complete the following fields:

    - **Name (required)**: Enter a friendly name for the forensic evidence policy. You can't change this name after the policy is created.
    - **Description (optional)**: Enter a description for the forensic evidence policy.
8. Select **Next**.
9. On the **Choose device activities to capture** page:

    1. Select any device activities that you want to capture. The policy only captures the selected activities.

    Note

    If the indicators aren't selectable, you're prompted to turn them on.
10. To capture activity for particular desktop apps and websites in your policy, select the **Opening a specific app or website** check box under **App and web browsing activities to capture**.

    Important

    To capture browsing activities (to include or exclude specific URLs in your forensic evidence policies), make sure to [install the necessary browser extensions](insider-risk-management-browser-support). You also need to turn on at least one browsing indicator. If you haven't already turned on one or more browsing indicators, you're prompted to do so if you choose to include or exclude desktop apps or websites. The triggering event for capturing browsing activities is a URL update in the URL bar that contains the specified URL.

    Select **Next**.
11. (Optional) If you chose to capture activity for particular desktop apps and websites, in the **Add apps and websites you want to capture activity for** page:

    1. To add a desktop app, select **Add desktop apps**, enter the name of an executable file (for example, teams.exe), then select **Add**. Repeat this process for each desktop app that you want to add (up to 25 apps). To find the name of an executable file for the app, open the Task Manager, then view the properties for the app. Here's a list of exe names for some of the common applications: Microsoft Edge (msedge.exe), Microsoft Excel (Excel.exe), the Snipping tool (SnippingTool.exe), Microsoft Teams (Teams.exe), Microsoft Word (WinWord.exe), and Microsoft Remote Desktop Connection (mstsc.exe).

    Note

    Sometimes, the exe names for an app might differ based on the device and the permissions with which the app was opened. For example, on a Windows 11 enterprise device, when Windows PowerShell is opened without administrator permissions, the exe name is WindowsTerminal.exe but when opened with administrator permissions, the exe name changes to powershell.exe. Make sure to include/exclude both exe names in such scenarios.

    1. To add a web app or website, select **Add web apps and websites**, enter a URL (for example, https://teams.microsoft.com), then select **Add**. Repeat this process for each web app or website that you want to add. You can add up to 25 URLs with a character length of 100 for each URL.

    Tip

    If an app has a desktop and web version, add both the desktop executable and the web URL to make sure you capture activity for both.

    1. Select **Next**.
12. On the **Review settings and finish** page, review the settings you chose for the policy and any suggestions or warnings for your selections. Edit any of the policy values or select **Submit** to create and activate the policy.
13. After you complete the policy configuration steps, continue to Step 5.

#### Capture all activities

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Forensic evidence** in the left navigation, then select **Forensic evidence policies**.
4. Select **Create forensic evidence policy**.
5. On the **Scope** page, select **All activities**. This option captures any activity performed by users. You can review captures for this option on the **Forensic evidence (preview)** tab on the **User activity reports (preview)** dashboard.
6. Select **Next**.
7. On the **Name and description** page, complete the following fields:

    - **Name (required)**: Enter a friendly name for the forensic evidence policy. You can't change this name after the policy is created.
    - **Description (optional)**: Enter a description for the forensic evidence policy.
8. Select **Next**.
9. On the **Choose device activities to capture** page, if you want to exclude certain desktop apps and/or web apps or websites from the capture, under **App and web browsing activities to capture**, select the **Exclude specific apps or websites** check box.
10. Select **Next**.
11. If you chose to exclude particular desktop apps and websites from the capture, in the **Exclude applications/URLs** page:

    - To exclude a desktop app from the capture, select **Exclude desktop apps**, enter the name of an executable file (for example, teams.exe), and then select **Add**. Repeat this process for each desktop app that you want to exclude (up to 25 apps). To find the name of an executable file for an app, open the Task Manager, and then view the properties for the app.
    - To exclude a web app or website, select **Exclude web apps and websites**, enter a URL (for example, https://teams.microsoft.com), and then select **Add**. Repeat this process for each web app or website that you want to exclude. You can exclude up to 25 URLs with a character length of 100 for each URL.

    Tip

    If an app has a desktop and web version, add both the desktop executable and the web URL to make sure you exclude both.
12. On the **Review settings and finish** page, review the settings you chose for the policy and any suggestions or warnings for your selections. Edit any of the policy values or select **Submit** to create and activate the policy.
13. After you complete the policy configuration steps, continue to Step 5.

### Step 5: Define and approve users for capturing

Before you can capture security-related user activities, admins must follow the dual authorization process in forensic evidence. This process requires that applicable people in your organization both define and approve the enabling of visual capturing for specific users.

You must request to enable forensic evidence capturing for specific users. When you submit a request, approvers in your organization receive an email notification and can approve or reject the request. If approved, the user appears on the **Approved users** tab and is eligible for capturing. For more information, see these links:

- [Request approval for forensic evidence capturing](insider-risk-management-forensic-evidence-manage#request-capturing-approvals).
- [Approve (or reject) requests for forensic evidence capturing](insider-risk-management-forensic-evidence-manage#approve-or-reject-capturing-requests).