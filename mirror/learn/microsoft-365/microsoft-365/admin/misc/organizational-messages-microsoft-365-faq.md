---
layout: FAQ
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Organizational messages in Microsoft 365 FAQ | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/misc/organizational-messages-microsoft-365-faq?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
summary: >
  <p>This article provides answers to frequently asked questions that administrator might have about organizational messages in Microsoft 365. For more information about organizational messages in Microsoft 365, see <a href="organizational-messages-microsoft-365">Organizational messages in the Microsoft 365 admin center</a>.</p>
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/help/4021566/windows-10-send-feedback-to-microsoft-with-feedback-hub-app
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: true
uhfHeaderId: MSDocsHeader-M365-IT
description: Find answers to common questions about organizational messages in Microsoft 365, including message delivery, permissions, localization, and more.
ms.date: 2026-04-01T00:00:00.0000000Z
f1.keywords:
- NOCSH
ms.author: kwekua
author: kwekuako
manager: scotv
audience: Admin
ms.topic: faq
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- operations-pod
ms.custom: campaignIDs-batch2
search.appverid:
- MET150
- MOE150
locale: en-us
document_id: 3d4f2038-c190-e0a7-97ba-b6d4be739a05
document_version_independent_id: 3d4f2038-c190-e0a7-97ba-b6d4be739a05
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/misc/organizational-messages-microsoft-365-faq.yml
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: faq
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/misc/organizational-messages-microsoft-365-faq
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/misc/organizational-messages-microsoft-365-faq.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: a7609388-7656-48da-ef45-3cedf5d97c8a
---

# Organizational messages in Microsoft 365 FAQ | Microsoft Learn

This article provides answers to frequently asked questions that administrator might have about organizational messages in Microsoft 365. For more information about organizational messages in Microsoft 365, see [Organizational messages in the Microsoft 365 admin center](organizational-messages-microsoft-365).

## Can you tell me more about delivery expectations for these messages?

For non-urgent messages, after the Organizational Messages platform schedules your message, it takes a few hours before the message is eligible to be delivered to end user devices. For example, if you set the **Start Date** to be now or today, you should expect a few hours before any end user devices in your testing tenant receive the message payload.

Windows delivers messages on a pull model, so the system buffers messages on a set period for each of the channels. Since devices might be configured to request content at different times, messages might take 24 or more hours before the message is received and rendered.

Once your message is actively delivering for over 24 hours, you can return to the **Manage messages** experience to review the latest delivery data for your message.

For urgent messages, after the Organizational Messages platform schedules your message, the platform tries to send the message as soon as possible. However, as noted earlier, this process is a best-effort mechanism subject to various conditions, with no guaranteed delivery times.

Note

For Windows Spotlight messages, users who select a message on the Windows lock screen don't see it again for 12 months. Users who don't select the message might see it multiple times.

## My team created organizational messages through other methods outside of the Microsoft 365 admin center. For example, Microsoft Intune, Adoption Score, and Usage reports. How do they work with these messages?

The Organizational messages centralized experience is the one-stop-shop for organizational messages. You should be able to see and manage your other messages from the organizational messages centralized experience, regardless of where they were created.

Note

Adoption Score organizational messages on Office or Outlook channels aren't visible in the centralized experience.

## How do admins get the required permissions?

Reach out to an admin with appropriate permissions and ask them to assign you the [Organizational Messages Writer](/en-us/azure/active-directory/roles/permissions-reference#organizational-messages-writer) or [Organizational Message Approver](/en-us/azure/active-directory/roles/permissions-reference#organizational-messagesapprover) Microsoft Entra role by following these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. From the left navigation bar, select **... Show all**, and then select **Users** to expand it.
3. Under **Users**, select **Active users**.
4. In the **Active users** page, search for and then select the user you want to assign the role to.
5. In the user's details pane, select **Manage roles** under **Roles**.
6. In the **Manage admin roles** pane, select **Admin center access**, and then select **Show all by category**.
7. Scroll down to the **Other** section.
8. In the **Other** section, select the checkbox next to **Organizational Messages Writer** and/or **Organizational Messages Approver**, depending on which roles you want to assign.
9. Select **Save changes**.

## Why do I need to update my Mobile Device Management (MDM) policies?

The MDM policies listed in [Set tenant policies](organizational-messages-microsoft-365#set-tenant-policies) control whether the service delivering the messages can access each location where organizational messages could be delivered. Previously, the configuration service providers (CSPs) only affected consumer scenarios and controlled whether Microsoft messaging can be delivered. However, since you're using the same service, the policies affect admin-created messages as well.

## How can I get my MDM settings for troubleshooting purposes?

1. Right-click on the **Start** menu and select **Run**.
2. In the **Open:** text box of the **Run** window, enter **ms-settings:workplace**, and then select **OK**.
3. In **Accounts &gt; Access work or school** page of the Settings app, under **Related settings**, select **Export** next to **Export your management log files**.
4. The exported management log files are saved at *C:\Users\Public\Documents\MDMDiagnostics*.

## How can I get my user and device ID for troubleshooting purposes?

1. From the **Start** menu, launch the **Feedback Hub** app.
2. In the **Feedback Hub** app, select **Settings** in the bottom left-hand corner.
3. In the **Settings** page, navigate to the **Device Information** section. The **Device ID** and **User ID** are listed in this section.

## Where can I find more information on configuration service provider (CSP) policies related to Organizational Messages?

You can use the [**Experience CSP**](/en-us/windows/client-management/mdm/policy-csp-experience) for policies related to organizational messages. For example:

- [AllowWindowsSpotlight](/en-us/windows/client-management/mdm/policy-csp-experience#allowwindowsspotlight).
- [AllowWindowsTips](/en-us/windows/client-management/mdm/policy-csp-experience#allowwindowstips).
- [AllowWindowsSpotlightOnActionCenter](/en-us/windows/client-management/mdm/policy-csp-experience#allowwindowsspotlightonactioncenter).
- [DisableCloudOptimizedContent](/en-us/windows/client-management/mdm/policy-csp-experience#disablecloudoptimizedcontent).
- [ConfigureWindowsSpotlightOnLockScreen](/en-us/windows/client-management/mdm/policy-csp-experience#configurewindowsspotlightonlockscreen).
- [AllowSpotlightCollection](/en-us/windows/client-management/mdm/policy-csp-experience#allowspotlightcollection).
- [EnableOrganizationalMessages](/en-us/windows/client-management/mdm/policy-csp-experience#enableorganizationalmessages).

## What do the different message states mean?

All messages have a state that indicates their creation or delivery status. For example:

- **Completed** - The message successfully was delivered as defined by start and end dates.
- **Pending** - The organizational messages service registered the message but it isn't delivered yet. Certain details of the message might not be available while in **Pending** state.
- **Failed** - The organizational messages service wasn't able to properly register the message. The message needs to be [copied](organizational-messages-microsoft-365#copy-an-existing-organizational-message) to retry the process.
- **Canceled** - An admin stopped and canceled the message. The cancellation could be either prior or during the delivery of the message.
- **Active** - Message is currently being delivered to your users.
- **Draft** - Message isn't completed or submitted for scheduling and approval. Any tenant writer can [continue a draft and complete the message](organizational-messages-microsoft-365#modify-a-draft-message) through the **Create a message** wizard.
- **Scheduled** - A message is properly authored and is awaiting delivery. At delivery time, the message status changes to **Active**.
- **Rejected** - A message was rejected after an approver reviewed it. Rejecting a message keeps the message from proceeding to a **Scheduled** or **Active** state.
- **Pending approval** - A message is awaiting review by an approver.

## How does localization work in Organizational Messages?

The following locales are supported:

- en-US
- de-DE
- es-ES
- fr-FR
- it-IT
- ja-JP
- ko-KR
- nl-NL
- pl-PL
- pt-BR
- pt-PT
- ru-RU
- tr-TR
- zh-Hans
- zh-Hant

For **pre-made** messages, an Organizational Message is created for all of the listed locales. If the Organizational Messages Writer selects "pre-made Message A" to send to end users, any end user whose first preferred language matches one of the supported languages qualifies to receive "pre-made Message A" in their first preferred language.

For **custom messages**, as long as it's one of the supported locales, the creation of an Organizational Message is restricted to the **Display language** selected in the [**My Account** &gt; **Settings & Privacy**](https://myaccount.microsoft.com/settingsandprivacy/language) setting in the Microsoft 365 admin center.

For example, an Organizational Messages Writer sets their Microsoft 365 admin center display language to French. After the writer creates "Custom Message B", only end users with French as their **[Windows display language](ms-settings:regionlanguage)** in the **[Time & Language &gt; Language & Region](ms-settings:regionlanguage)** page of the Windows Settings app receive "Custom Message B." "Custom Message B" isn't delivered to end users whose **Windows display language** is any language other than French.

Locale fallback:

If the Organizational Messages Writer locale is outside of the supported listed locales, the message isn't delivered to end users. To ensure delivery, verify that your locale maps to one of the supported locales listed earlier. For example:

- fr-CA falls back to fr-FR, and users with all French language locales receive the message.
- lv-LV doesn't map to a supported locale, so users with the lv-LV locale don't receive the message. Consider authoring the message in a supported locale instead.

## Does Organizational Messages support government environments?

No, government environments such as GCC or GCC-H aren't supported at this time.

## Can we still author Get Started messages created previously in Microsoft Intune?

You can view any **Get Started** messages that you created in the Organizational messages experience within Microsoft Intune that aren't complete within the Microsoft 365 admin center experience. However, new Get Started message creation aren't currently supported.

## Are there any pre-made messages for Windows Spotlight?

No pre-made Windows Spotlight messages are available.

## Where are organizational messages delivered in Windows 11?

Organizational messages deliver to the following Windows 11 locations:

- Notifications area.
- Taskbar.
- Windows Spotlight.

Note

Access to the Taskbar experience requires KB5094126 for Windows 11, version 25H2 and 24H2. For more information, see [KB5094126](https://support.microsoft.com/topic/1a9bcba6-5f53-4075-8156-fe11ac631737).

## How can we prevent messages from Microsoft but still allow organizational messages?

To only show organizational messages, follow these steps:

1. Enable all of the policies described in [Set Tenant Policies](organizational-messages-microsoft-365#set-tenant-policies).
2. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
3. From the left navigation bar, select **... Show all**, and then select **Reports** to expand it.
4. Under **Reports**, select [**Organizational messages**](https://admin.cloud.microsoft/?#/organizationalmessages).
5. In the **Organizational messages** page, select the **Settings** gear icon in the top right corner.
6. In the **Settings** pane, deselect the option **Allow Microsoft messages to display**.
7. Select **Save**.

These steps ensure the Organizational messages platform sends only your organization's messages to Windows surfaces.

## How do licenses affect message customization?

- The authoring experiences are automatically disabled if license requirements aren't met.
- Windows custom messages require Windows E3 or E5, or Microsoft 365 E3, or E5.
- Microsoft Teams custom messages require Office 365 E3 or Office 365 E5, or Microsoft 365 E3 or Microsoft 365 E5.
- Pre-made messages might still be available without these licenses.