---
layout: Conceptual
title: Microsoft Purview Endpoint DLP on macOS 27 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/endpoint-dlp-macos-27-changes
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how macOS 27 permission changes affect Microsoft Purview Endpoint DLP protection, configuration, notifications, and device monitoring.
author: pan11gadi
ms.author: pangadi
manager: pangadi
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.topic: concept-article
ms.custom: msecd-doc-authoring-1023
ms.date: 2026-08-26T00:00:00.0000000Z
ai-usage: ai-generated
locale: en-us
document_id: 78ca2351-9b23-874f-27ff-6cdb1aa9dd10
document_version_independent_id: 78ca2351-9b23-874f-27ff-6cdb1aa9dd10
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/endpoint-dlp-macos-27-changes.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: endpoint-dlp-macos-27-changes
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/endpoint-dlp-macos-27-changes.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 385729c1-177b-ce68-0f54-011213b97159
---

# Microsoft Purview Endpoint DLP on macOS 27 | Microsoft Learn

Microsoft Purview Endpoint Data Loss Prevention (Endpoint DLP) uses macOS permissions to identify websites, applications, files, and active content involved in user activities. This information helps Endpoint DLP evaluate policies and apply protection actions for activities such as uploading sensitive data to websites and cloud services or copying sensitive content to a browser.

Before macOS 27 (Golden Gate), Endpoint DLP relied on the **Accessibility** permission for browser and website visibility. In macOS 27, **Device Control and Data Access** manages this capability. Users can disable this permission after it's deployed through mobile device management (MDM), which can affect Endpoint DLP's ability to get browser and website context. To help maintain data protection coverage, administrators can configure protection modes, monitor permission status, and guide users to restore the required permission when needed.

This article describes the changes introduced in macOS 27, their impact on Endpoint DLP, and how administrators can prepare their organization. Administrators can configure protection modes, monitor affected devices, and validate deployment readiness.

Important

Use Endpoint DLP client version 101.26072 or later with this macOS 27 guidance.

## Prerequisites

- Endpoint DLP client version 101.26072 or later.
- Familiarity with [onboarding macOS devices into Microsoft Purview](device-onboarding-macos-overview).

## Permission changes in macOS 27

On macOS 27, Endpoint DLP uses **Device Control and Data Access** permission to support browser visibility, activity monitoring, and policy enforcement. The permission lets Endpoint DLP identify the active browser, website, application, and file associated with user activity. This context supports policies for activities such as uploading sensitive files and pasting sensitive content into browsers.

In macOS 27, the permission is under **Settings** &gt; **Privacy & Security** &gt; **Device Control and Data Access**. In earlier macOS versions, the permission is under **Settings** &gt; **Privacy & Security** &gt; **Accessibility**.

In some macOS interfaces, management profiles, and diagnostic logs, Microsoft Endpoint DLP might appear as `com.microsoft.dlp.daemon.app` or `com.microsoft.dlp.daemon`. These identifiers refer to the Endpoint DLP application.

![Screenshot of macOS Device Control and Data Access settings with permission enabled for com.microsoft.dlp.daemon.](media/endpoint-dlp-macos-27/device-control-data-access.png)

## Behavior when permission is turned off

When Endpoint DLP detects that a user turned off the Microsoft Purview Endpoint DLP permission under **Device Control and Data Access**, Endpoint DLP can no longer get URL and browser context for Safari, Chrome, and Firefox. Endpoint DLP responds by:

1. Displaying a notification that prompts the user to restore the permission (see the following screenshot).

![Screenshot of an Endpoint DLP notification that says Accessibility is turned off and provides an option to open System Settings.](media/endpoint-dlp-macos-27/accessibility-disabled-notification.png)

1. Applying administrator-configured protection settings when browser URL context is unavailable.

Administrators can configure separate protection modes for:

- Uploading sensitive files to websites and cloud services
- Copying sensitive data to a browser

## Protection modes

Endpoint DLP provides **Enforce**, **Audit**, and **Off** modes for cloud egress and paste-to-browser activities when the permission is unavailable. The default for both settings is **Enforce**.

### Uploading sensitive files to websites and cloud services

**Setting name:** Restricted protection mode for cloud egress

This setting controls how Endpoint DLP handles uploads of sensitive files when browser and website context are unavailable.

- **Enforce**: Applies upload protection. Endpoint DLP treats supported non-Edge browsers, such as Safari, Chrome, and Firefox, as restricted destinations and enforces the most restrictive applicable policy action.
- **Audit**: Records and monitors the condition without enforcing upload restrictions.
- **Off**: Doesn't apply permission-related upload protection.

### Copying sensitive data to a browser

**Setting name:** Restricted protection mode for paste to browser

This setting controls how Endpoint DLP handles copy-and-paste activities into browsers when browser and website context are unavailable.

- **Enforce**: Applies policy actions, such as block or warn.
- **Audit**: Records events without enforcing restrictions.
- **Off**: Doesn't apply permission-related browser copy-and-paste protection.

### Permission notification

**Setting name:** Permission notification (`notification`)

Endpoint DLP can notify users when the permission is turned off. The notification explains why permission is required and prompts the user to restore access. Administrators can customize the notification message.

The profile settings map to the following configuration keys:

| Customer scenario | Setting name | Configuration key |
| --- | --- | --- |
| Uploading sensitive files to websites and cloud services | Restricted protection mode for cloud egress | `unallowedBrowserMode` |
| Copying sensitive data to a browser | Restricted protection mode for paste to browser | `pasteToBrowserMode` |
| Permission notification | Permission notification | `notification` |

The following source fragment sets both protection modes to Enforce:

```xml
 <key>accessibility</key>
                    <dict>
                        <key>enforcement</key>
                        <dict>
                            <key>unallowedBrowserMode</key>
                            <string>enforce</string>
                            <key>pasteToBrowserMode</key>
                            <string>enforce</string>
                        </dict>
                        <key>notification</key>
                        <dict>
                            <key>Microsoft Endpoint DLP will report this device as non-compliant. Additional restrictions will be in effect until Accessibility has been re-enabled for Microsoft Endpoint DLP</key>
                            <string/>
                        </dict>
                    </dict>
```

## MDM configuration options

Microsoft provides configuration samples for Microsoft Intune and Jamf Pro. These options configure the protection modes and the message that prompts users to turn on the permission.

- **Microsoft Intune**: Use the sample [`com.microsoft.wdav.mobileconfig`](https://github.com/microsoft/mdatp-xplat/blob/master/macos/settings/data_loss_prevention/accessibility/com.microsoft.wdav.mobileconfig) configuration profile as the starting point for deployment.
- **Jamf Pro with `schema.json`**: Update the existing Microsoft Defender for Endpoint preferences configuration profile to use the latest [`schema.json`](https://github.com/microsoft/mdatp-xplat/blob/master/macos/schema/schema.json). The configuration is under **Data Loss Prevention** &gt; **Accessibility**.
- **Jamf Pro with a property list**: Use the sample [`com.microsoft.wdav.plist`](https://github.com/microsoft/mdatp-xplat/blob/master/macos/settings/data_loss_prevention/accessibility/com.microsoft.wdav.plist).

![Screenshot of Jamf Pro Data Loss Prevention configuration with Accessibility enforcement and notification settings.](media/endpoint-dlp-macos-27/jamf-accessibility-settings.jpg)

## Audit mode

Audit mode lets administrators assess the effect of unavailable permissions before they enable enforcement. Endpoint DLP continues to detect when the permission is turned off and can notify users to restore access, but it doesn't apply the additional restricted protection behavior for cloud egress or paste-to-browser activities.

Audit mode can reduce user disruption while administrators identify affected devices. During this assessment, controls that would normally apply when browser context is unavailable aren't enforced. This condition can leave a temporary protection gap until the permission is restored or enforcement is enabled.

The following source fragment sets both protection modes to Audit:

```xml
<key>accessibility</key>
                    <dict>
                        <key>enforcement</key>
                        <dict>
                            <key>unallowedBrowserMode</key>
                            <string>audit</string>
                            <key>pasteToBrowserMode</key>
                            <string>audit</string>
                        </dict>
                        <key>notification</key>
                        <dict>
                            <key>Microsoft Endpoint DLP will report this device as non-compliant. Additional restrictions will be in effect until Accessibility has been re-enabled for Microsoft Endpoint DLP</key>
                            <string/>
                        </dict>
                    </dict>
```

## Permission monitoring

Monitor Endpoint DLP permission status in Microsoft Purview. The device details pane shows the **Accessibility** configuration status for an onboarded macOS device. A status of **Installed** indicates the required permission is configured, while **Not updated** indicates the permission isn't available to Endpoint DLP and requires administrator attention. See the following screenshot examples.

![Screenshot of Microsoft Purview device details showing Accessibility with an Installed status.](media/endpoint-dlp-macos-27/accessibility-enabled-device-status.png)

![Screenshot of Microsoft Purview device details showing Accessibility with a Not updated status.](media/endpoint-dlp-macos-27/accessibility-disabled-device-status.png)

## Administrator readiness

Preparing Endpoint DLP for macOS 27 includes the following activities:

1. Review the updated macOS deployment guidance for Endpoint DLP.
2. Deploy or validate the required Endpoint DLP permission configuration on managed macOS devices.
3. Upgrade to Endpoint DLP client version 101.26072 or later.
4. Monitor the **Device Onboarding** page for devices that report the permission as off.
5. Configure user notifications and educate users to restore the permission if it's turned off.