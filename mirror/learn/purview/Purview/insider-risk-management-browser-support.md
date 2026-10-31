---
layout: Conceptual
title: Learn about and configure Insider Risk Management browser signal detection | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-browser-support
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about Insider Risk Management browser signal detection in Microsoft Purview
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: article
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-07-30T00:00:00.0000000Z
audience: itpro
ms.collection:
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- highpri
locale: en-us
document_id: 0fbd5aa4-205c-aeb9-0e5e-1523432cfa8a
document_version_independent_id: 0fbd5aa4-205c-aeb9-0e5e-1523432cfa8a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-browser-support.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-browser-support
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-browser-support.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: b81dc050-4302-9edc-c48a-2a2aa942e8d3
---

# Learn about and configure Insider Risk Management browser signal detection | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

In Microsoft Purview Insider Risk Management, you can use browser signal detection with the following templates:

- [Data theft by departing users](insider-risk-management-policy-templates#data-theft-by-departing-users)
- [Data leaks](insider-risk-management-policy-templates#data-leaks)
- [Forensic evidence](insider-risk-management-forensic-evidence#capturing-options)
- [Risky browser usage (preview)](insider-risk-management-policy-templates#risky-browser-usage-preview)

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Browsers and templates

Users often use web browsers to access both sensitive and nonsensitive files within an organization. Insider Risk Management enables your organization to detect and act on browser exfiltration signals for all nonexecutable files viewed in [Microsoft Edge](https://www.microsoft.com/edge) and [Google Chrome](https://www.google.com/chrome) browsers. With these signals, analysts and investigators can quickly act when in-scope policy users perform any of the following risky activities while using these browsers:

- Copying files to personal cloud storage
- Printing files to local or network devices
- Transferring or copying files to a network share
- Copying files to USB devices
- Browsing potentially risky websites

Microsoft Edge detects signals for these events by using built-in browser capabilities and the *Microsoft Compliance Extension* add-on. In Google Chrome, customers use the *Microsoft Compliance Extension* for signal detection.

The following table summarizes identified risk activities and extension support for each browser:

| Detected activities | Microsoft Edge | Google Chrome |
| --- | --- | --- |
| Browsing potentially risky websites | Extension | Extension |
| Files copied to personal cloud storage | Native | Extension |
| Files copied to USB devices | Extension | Extension |
| Files printed to local or network devices | Native | Extension |
| Files transferred or copied to a network share | Extension | Extension |

The following table summarizes activities by template:

| Detected activities | Data theft by departing users | Data leaks | Risky browser usage |
| --- | --- | --- | --- |
| Browsing potentially risky websites | No | No | Yes |
| Files copied to personal cloud storage | Yes | Yes | No |
| Files copied to USB devices | Yes | Yes | No |
| Files printed to local or network devices | Yes | Yes | No |
| Files transferred or copied to a network share | Yes | Yes | No |

## Forensic evidence

For forensic evidence, you can capture all types of browsing activities; you're not limited to the browsing indicators of the [Risky browser usage template](insider-risk-management-policy-templates#risky-browser-usage-preview). You can specify the desktop apps and websites that you want to include or exclude. To capture browsing activity for forensic evidence, you must install the extensions described in this article, and you must also turn on at least one risky browsing indicator in the insider risk settings.

## Common requirements

Before installing the Microsoft Edge add-on or Google Chrome extension, ensure that devices for in-scope policy users meet the following requirements:

- Latest Windows 10 x64 build is recommended, minimum Windows 10 x64 build 1809 for signal detection support. Browser signal detection isn't currently supported on non-Windows devices.
- Current [Microsoft 365 subscription](insider-risk-management-configure#subscriptions-and-licensing) with Insider Risk Management support.
- Devices must be [onboarded](insider-risk-management-settings-policy-indicators#enable-device-indicators-and-onboard-windows-devices) to the Microsoft Purview portal.

For specific browser configuration requirements, see the Microsoft Edge and Google Chrome sections later in this article.

## Additional requirements

If you use policies based on the *Risky browser usage* template, select at least one *Browsing indicator* in **Insider Risk Management** &gt; **Settings** &gt; **Policy indicators**.

## Configure browser signal detection for Microsoft Edge

### Microsoft Edge browser requirements

- Meet the common requirements
- Latest Microsoft Edge x64, version 91.0.864.41 or higher
- Latest *Microsoft Compliance Extension* add-on, version 1.0.0.44 or higher
- Edge.exe isn't configured as an unallowed browser

### Option 1: Basic setup (recommended for testing with Microsoft Edge)

Use this option to configure a single-machine self-host for each device in your organization when testing browser signal detection.

1. Go to [Microsoft Compliance Extension](https://microsoftedge.microsoft.com/addons/detail/microsoft-compliance-exte/lcmcgbabdcbngcbcfabdncmoppkajglo).
2. Install the extension.

### Option 2: Intune setup for Microsoft Edge

Use this option to configure the extension and requirements for your organization by using Intune.

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431).
2. Go to **Devices** &gt; **Configuration Profiles**.
3. Select **Create Profile**.
4. Select **Windows 10 and later** as the platform.
5. Select **Settings catalog** as the profile type.
6. Select **Create**.
7. Enter a name and optional description on the **Basics** tab, then select **Next**.
8. Select **Add settings** on the **Configuration settings** tab.
9. Select **Administrative Templates** &gt; **Microsoft Edge** &gt; **Extensions**.
10. Select **Control which extensions are installed silently**.
11. Change the toggle to **Enabled**.
12. Enter the following value for the extensions and app IDs and update URL: `lcmcgbabdcbngcbcfabdncmoppkajglo`.
13. Select **Next**.
14. Add or edit scope tags on the **Scope tags** tab as needed, then select **Next**.
15. Add the required deployment users, devices, and groups on the **Assignments** tab, then select **Next**.
16. Select **Create**.

### Option 3: Group Policy setup for Microsoft Edge

Use this option to configure the extension and requirements organization-wide by using Group Policy.

**Step 1: Import the latest Microsoft Edge Administrative Template (.admx) file.**

Devices must be manageable by using Group Policies. Import all [Microsoft Edge Administrative Templates](https://www.microsoft.com/edge/business/download) into the Group Policy Central Store. For more information, see [How to create and manage the Central Store for Group Policy Administrative Templates in Windows](/en-us/troubleshoot/windows-client/group-policy/create-and-manage-central-store).

**Step 2: Add the *Microsoft Compliance Extension* add-on to the *Force Install* list.**

1. In the **Group Policy Management Editor**, go to your Organizational Unit (OU).
2. Expand the following path **Computer/User configuration** &gt; **Policies** &gt; **Administrative templates** &gt; **Classic administrative templates** &gt; **Microsoft Edge** &gt; **Extensions**. This path might vary depending on the configuration of your organization.
3. Select **Configure which extensions are installed silently.**
4. Right-click and select **Edit**.
5. Check **Enabled**.
6. Select **Show**.
7. For **Value**, add the following entry: *lcmcgbabdcbngcbcfabdncmoppkajglo;https://edge.microsoft.com/extensionwebstorebase/v1/crx*
8. Select **OK**, then select **Apply**.

## Configure browser signal detection for Google Chrome

Insider Risk Management browser signal detection support for Google Chrome is enabled through the *Microsoft Compliance Extension*. This extension also supports Endpoint DLP on Chrome. For more information about Endpoint DLP support, see [Get started with the Microsoft Compliance Extension (preview)](dlp-chrome-get-started).

### Google Chrome browser requirements

- Meet common requirements
- Latest version of Google Chrome x64
- Latest *Microsoft Compliance Extension* version (2.0.0.183 or higher)
- Chrome.exe isn't configured as an unallowed browser

### Option 1: Basic setup (recommended for testing with Chrome)

Use this option to configure a single-machine self-host for each device in your organization when testing browser signal detection.

1. Go to [Microsoft Compliance Extension](https://chrome.google.com/webstore/detail/microsoft-compliance-exte/echcggldkblhodogklpincgchnpgcdco).
2. Install the extension.

### Option 2: Intune setup for Chrome

Use this option to configure the extension and requirements for your organization by using Intune.

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431).
2. Go to **Devices** &gt; **Configuration Profiles**.
3. Select **Create Profile**.
4. Select **Windows 10 and later** as the platform.
5. Select **Settings catalog** as the profile type.
6. Select **Custom** as the template name.
7. Select **Create**.
8. Enter a name and optional description on the **Basics** tab, then select **Next**.
9. Select **Add settings** on the **Configuration settings** tab.
10. Select **Administrative Templates** &gt; **Google** &gt; **Google Chrome** &gt; **Extensions**.
11. Select **Configure the list of force-installed apps and extensions**.
12. Change the toggle to **Enabled**.
13. Enter the following value for the extensions and app IDs and update URL: `echcggldkblhodogklpincgchnpgcdco;https://clients2.google.com/service/update2/crx`
14. Select **Next**.
15. Add or edit scope tags on the **Scope tags** tab as needed, then select **Next**.
16. Add the required deployment users, devices, and groups on the **Assignments** tab, then select **Next**.
17. Select **Create**.

### Option 3: Group Policy setup for Chrome

Use this option to configure the extension and requirements organization-wide by using Group Policy.

#### Step 1: Import the Chrome Administrative Template file

Your devices must be manageable by using Group Policy. Import all [Chrome Administrative Templates](https://chromeenterprise.google/browser/download/) into the Group Policy Central Store. For more information, see [How to create and manage the Central Store for Group Policy Administrative Templates in Windows](/en-us/troubleshoot/windows-client/group-policy/create-and-manage-central-store).

#### Step 2: Add the Chrome extension to the Force Install list

1. In the **Group Policy Management Editor**, go to your organizational unit (OU).
2. Expand the following path **Computer/User configuration** &gt; **Policies** &gt; **Administrative templates** &gt; **Classic administrative templates** &gt; **Google** &gt; **Google Chrome** &gt; **Extensions**. This path might vary depending on the configuration for your organization.
3. Select **Configure the list of force installed extensions**.
4. Right-click and select **Edit**.
5. Select **Enabled**.
6. Select **Show**.
7. For **Value**, add the following entry: *echcggldkblhodogklpincgchnpgcdco;https://clients2.google.com/service/update2/crx*
8. Select **OK**, then select **Apply**.

## Test and verify Insider Risk Management browser signal detections

1. Create an Insider Risk Management policy with device indicators enabled.
2. To test signal detection for files copied to personal cloud storage, complete the following steps from a supported Windows device:

    - Open a file sharing website (Microsoft OneDrive, Google Drive, etc.) with the browser type that you configured for signal detection.
    - With the browser, upload a nonexecutable file to the website.
3. To test signal detection for files printed to local or network devices, files transferred or copied to a network share, and files copied to USB devices, complete the following steps from a supported Windows device:

    - Open a nonexecutable file directly in the browser. You must open the file directly through File Explorer or open it in a new browser tab for viewing rather than a webpage.
    - Print the file.
    - Save the file to a USB device.
    - Save the file to a network drive.
4. After you create your first Insider Risk Management policy, you start receiving alerts from activity indicators after about 24 hours. Check the [Alerts dashboard](insider-risk-management-activities#standard-alert-dashboard) for Insider Risk Management alerts for the tested activities.