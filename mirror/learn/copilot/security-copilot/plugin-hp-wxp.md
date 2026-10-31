---
layout: Conceptual
title: HP Workforce Experience Platform and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-hp-wxp
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use HP Workforce Experience Platform with Microsoft Security Copilot.
ms.date: 2026-02-19T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: concept-article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
ms.reviewer: shivanpatel
search.audiencetype: Admin
locale: en-us
document_id: 8e6b4b9f-911d-a443-f628-03849e8c0ebf
document_version_independent_id: 8e6b4b9f-911d-a443-f628-03849e8c0ebf
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-hp-wxp.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-hp-wxp
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-hp-wxp.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/19ec6774-09b8-473e-a17e-b17b518bbad7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ade36b61-c646-4bd8-87ee-f3a843461962
platformId: 468fb730-7a6e-d0ec-26fe-bc8543315507
---

# HP Workforce Experience Platform and Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

The HP Workforce Experience Platform (WXP) plugin for Security Copilot allows users to query data about their fleet and get responses back quickly and efficiently. This plugin can answer questions about PC warranty, Windows 11 readiness, resource consumption. It can also answer device age/stability/health, security, blue screens, and app performance including hangs and crashes.

Note

This article contains information about non-Microsoft plugins. This is provided to help complete integration scenarios. However, Microsoft doesn't provide troubleshooting support for non-Microsoft plugins. Contact the vendor for support.

## Prerequisites

This section lists the requirements for the integration

- HP Workforce Experience
- Security Copilot

## Know before you begin

The HP Workforce Experience (WXP) plugin for Security Copilot uses OAuth 2.0 for authentication with the WXP service. This requires user credentials for authentication.

### User credentials

1. Sign in into HP Workforce Experience Platform (https://workforceexperience.hp.com/) as an IT Admin.
2. Go to Account Management and select the **Users** tab.
3. Add a user (whoever needs access to the plugin in Security Copilot).
4. When adding a user, an IDP of either HP ID or AAD can be selected. This user can have a role of either Report Admin or IT Admin.

Note

1. This user should be a part of only one customer account in HP Workforce Experience Platform.
2. Irrespective of the IDP selected in the user creation flow, when the OAuth flow is triggered from Security Copilot, an HP ID is required.

### Client Credentials

A key part of the authentication process is client credentials. Client credentials for HP WXP can be obtained from https://developers.hp.com/.

1. Sign up on https://developers.hp.com/ if you don’t have an account already present.
2. Send an email to workforceexperience@hp.com requesting to enable API credentials request access in the PI APIs
3. Alternatively, create a case from https://workforceexperience.hp.com/ . Include the email address used for signup in the developer portal. Additionally request to enable them in the dev portal.
4. Once the case is generated, it takes upto 24 hours for enablement.
5. Go to https://developers.hp.com/hp-proactive-management.
6. Select "Get Credentials" against HP Proactive Insights Analytics.
7. In the redirect URL, enter https://securitycopilot.microsoft.com/auth/v1/callback.
8. Leave "Client ID" empty.
9. Under Attributes -&gt; Scopes, select the checkbox of "Read".
10. Select "Create".
11. The API credentials are generated.
12. To access the credentials, go to your profile by clicking on your email on the top right corner.
13. Select My API Credentials.

### Microsoft Security Copilot Integration Configuration

1. Go to https://securitycopilot.microsoft.com/.
2. Select the Sources icon.
3. Under the "Non-Microsoft" section, find the plugin "HP Workforce Experience".

    Note

    You might see two plugins – one for US and one for EU. Use the plugin based on the region your customer company is created in HP Workforce Experience Platform.
4. Select Setup. A popup window appears.
5. Enter the ClientId and ClientSecret.
6. Enter your user credentials when prompted.

## Sample HP Workforce Experience Platform prompts

1. For some prompts, data would be picked up from Microsoft Intune plugins. To ensure the data is picked up through the HP WXP plugin, in the prompt explicitly request to get the data from HP Workforce Experience Platform.

| **Prompt example** | **Expected output** |
| --- | --- |
| What device warranties expire soon? | A list of devices with warranties expiring soon, if applicable.<br><br>*Example:*<br><br>*`"The following devices have warranties that have already expired: [table with serial numbers, warranty status, and warranty end dates]"`* |
| Which devices aren't compatible with Windows 11? | A list of devices not compatible with Windows 11, if applicable.<br><br>*Example:*<br><br>*`"There are currently no devices that aren't compatible with Windows 11 based on the available data."`* |
| List the top 10 devices that have the least disk space available | A list of devices with the least amount of disk space in your fleet.<br><br>*Example:*<br><br>*`"Here are the top 10 devices with the least disk space available: [table containing device names, device models, and disk space used]`"* |
| What is the DEX score for device [serial number]? | The DEX score of the mentioned device.<br><br>*Example:*<br><br>*`"Your DEX score is [XX.X]. Here are the details of the device contributing to this score: [table containing device name, device model, device manufacturer]"`* |
| When was the last application crash on one of my devices? | Information on the last application that crashed on a device in the fleet.<br><br>*Example:*<br><br>*`"The last application crash on one of your devices occurred on [Month Date Year] at [time]. The application that crashed was [application name] on the device named [device name]. Here are the details of the last crash: [table including device name, application name, and crash date and time]"`* |

## Troubleshoot the HP Workforce Experience Platform plugin

### Errors occur

If you encounter errors occur, such as: *Couldn't complete your request*, or *An unknown error occurred*, make sure the plugin is turned on. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.