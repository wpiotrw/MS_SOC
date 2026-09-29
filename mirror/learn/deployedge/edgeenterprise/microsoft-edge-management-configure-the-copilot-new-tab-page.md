---
layout: Conceptual
title: Configure the Copilot new tab page | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/deployedge/microsoft-edge-management-configure-the-copilot-new-tab-page
breadcrumb_path: /DeployEdge/breadcrumb/toc.json
recommendations: true
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/help/4021566/windows-10-send-feedback-to-microsoft-with-feedback-hub-app
uhfHeaderId: MSDocsHeader-MSEdge
ms.author: katherinegan
author: vmliramichael
manager: archandr
ms.date: 2026-09-08T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: microsoft-edge
ms.localizationpriority: medium
ms.collection: M365-modern-desktop
description: Provides configuration guidance for the Copilot new tab page in Microsoft Edge.
locale: en-us
document_id: e59ba3fb-4b81-e764-7c3c-6357d2ab8ca1
document_version_independent_id: e59ba3fb-4b81-e764-7c3c-6357d2ab8ca1
original_content_git_url: https://github.com/MicrosoftDocs/Edge-Enterprise-pr/blob/live/edgeenterprise/microsoft-edge-management-configure-the-copilot-new-tab-page.md
site_name: Docs
depot_name: office.Edge-Enterprise
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Edge-Enterprise/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: microsoft-edge-management-configure-the-copilot-new-tab-page
moniker_range_name: 
monikers: []
item_type: Content
source_path: edgeenterprise/microsoft-edge-management-configure-the-copilot-new-tab-page.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
platformId: 8b3e6616-75db-d49d-b42b-be7c1cd26cd6
---

# Configure the Copilot new tab page | Microsoft Learn

The Copilot new tab page introduces a refreshed start surface that transforms the browser into a productivity-focused workspace. The experience unifies Microsoft 365 Copilot chat, web search, and work content into a single-entry point. The Copilot side rail provides convenient access to chat, agents and skills, tasks, and Cowork. Through proactive work cards and suggested prompts, the new tab page surfaces important organizational content, such as files and calendar events, to help users prioritize and initiate tasks more efficiently while maintaining enterprise-grade security and compliance standards.

Important

> 
> Starting Microsoft Edge version 153, Discover feed and feed toggle functionality will be limited. We will continue to update and expand functionality as the Copilot new tab page evolves.

Important

> 
> In Microsoft Edge version 148, some users may not see the Work feed, Discover feed, or feed toggle on the Copilot new tab page if their tenant or user locale is outside supported language markets. Feed experiences depend on supported language and market availability.

## Scope

- This feature applies to organizations using Microsoft Edge where users have Copilot new tab page enabled.
- For users without Copilot new tab page enabled, the existing new tab page behavior and related policies remain unchanged.

The availability of the Copilot New Tab Page can be configured through the `CopilotNewTabPageEnabled` policy. For more details on the policy behavior, please visit: [CopilotNewTabPageEnabled | Microsoft Learn](/en-us/deployedge/microsoft-edge-browser-policies/copilotnewtabpageenabled)

## Enabling the Copilot new tab page in the Edge management service

### Prerequisites

Before setting up the configuration policy, ensure you have a Microsoft Entra group set up in the Microsoft 365 Admin Center that includes the target users. Instructions for creating a group can be found here: [Create, edit, or delete a security group in the Microsoft 365 admin center - Microsoft Learn](/en-us/microsoft-365/admin/create-groups/create-groups). You can enable Copilot new tab page for one or more group.

### Configuration steps

1. Navigate to the Edge management service inside the Microsoft 365 Admin Center at https://admin.cloud.microsoft/?#/Edge and sign in with an account that has Global admin or Edge admin privileges.
2. From the top navigation bar, switch to the Copilot tab.
3. Click the dropdown beside **Copilot new tab page** and select **Enabled**. Note: The other settings recommended for Copilot to work successfully will also be set to Enabled when you enable the Copilot new tab page. You can choose to adjust these individually.
4. If you’re ready to save the configuration, click Assign configuration in the banner that appears at the top of the page.

### Option 1: Enable Copilot features in an existing configuration policy

1. From the Edge management service homepage, click the **Copilot tab**.
2. Configure the **Copilot new tab page** feature.
3. Under **Assign configuration to**, choose **An existing configuration policy**, then click **Next**.
4. Select the desired configuration policy from the dropdown and click **Save configuration** to finish enabling Copilot features.
5. Optional: You can navigate directly to the Enterprise AI settings page for that configuration policy by clicking **View configuration**.

### Option 2: Enable Copilot features in a new configuration policy

1. From the Edge management service homepage, click the **Copilot tab**.
2. Configure the **Copilot new tab page** feature.
3. Under **Assign configuration to**, choose **A new configuration policy**, then click Next.
4. Type a name for your configuration policy in the Name field, and optionally, provide a description. Click **Create new policy** to proceed.
5. Choose whether to assign the new policy to **All users** or to **One or more groups**.
6. If you selected One or more groups, select the appropriate security groups using the picker.
7. Click **Assign policy** to complete creating your configuration policy with Copilot features enabled.

## Verifying that the Copilot new tab page is enabled

1. Sign in to Microsoft Edge with an account assigned to the updated configuration profile. *\*Note: Updates may take up to 90 minutes to be downloaded to devices targeted by the configuration profile.\**
2. For testing, you can navigate to edge://policy on a targeted device and click **Reload Policies** to fetch changes. Verify that the `CopilotNewTabPageEnabled` policy values show as TRUE, then restart the browser.
3. Open a new tab and verify that the new tab page is showing the updated Copilot experience.

## What your users see

Upon enabling, users will see the default Copilot new tab page experience with work cards enabled, alongside the app launcher for navigating to Microsoft 365 apps, pinned quick links, and a refreshed theme setting experience.

Users will also see an updated search box that allows them to quickly navigate to sites, search the web, or send a query directly to Microsoft 365 Copilot.

Important

> 
> **Known limitation:** Users without a Microsoft 365 Copilot license may observe limitations in Copilot Prompt Card content.

![image1.](media/microsoft-edge-configure-the-copilot-new-tab-page/img1.png)

![image2.](media/microsoft-edge-configure-the-copilot-new-tab-page/img2.png)

The Copilot side rail brings chat, agents and skills, tasks, and Cowork directly into the new tab page, giving users a consistent place to access Copilot capabilities as they work. The side rail can be collapsed or expanded based on the user’s preferred workflow, with this preference remembered for future new tabs.

If users manually turn off Work Cards using the gear settings toggle on the Copilot new tab page, they will instead see chat chips, which are suggested chat prompts, along with the other available feature.

![image3.](media/microsoft-edge-configure-the-copilot-new-tab-page/img3.png)

## Discover Feed

The Discover feed, which brings curated news and content to your new tab. Please review your current configuration and plan to validate your setup when the feature is available. 

Users can personalize their Discover feed language and content to better curate the feed.

![image4.](media/microsoft-edge-configure-the-copilot-new-tab-page/img4.png)

![image5.](media/microsoft-edge-configure-the-copilot-new-tab-page/img5.png)

## New tab page policies

The policy behavior outlined in this section applies exclusively to users who have the Copilot new tab page enabled. For all other users, the existing new tab page policies remain unchanged.

Some new tab page policies will be supported automatically when the Copilot new tab page is turned on, but others are obsolete or not yet supported.

### Supported new tab page policies

| **Component** | **Policy / configuration** |
| --- | --- |
| App Launcher | Edge policy: [`NewTabPageAppLauncherEnabled`](/en-us/deployedge/microsoft-edge-browser-policies/newtabpageapplauncherenabled) |
| Background Image | Edge policy: [`NewTabPageAllowedBackgroundTypes`](/en-us/deployedge/microsoft-edge-browser-policies/newtabpageallowedbackgroundtypes) |
| Discover Feed | Edge policy: [`ConfigureNTPFeedTabVisibility`](/en-us/deployedge/microsoft-edge-browser-policies/configurentpfeedtabvisibility) |
| Discover Feed | Edge policy: [`SetNTPDefaultFeedTab`](/en-us/deployedge/microsoft-edge-browser-policies/setntpdefaultfeedtab) |
| Organization logo | Microsoft 365 admin center: Org settings &gt; Organization profile &gt; Add theme &gt; Logo |
| Organization logo | Edge policy: [`NewTabPageCompanyLogoEnabled`](/en-us/deployedge/microsoft-edge-browser-policies/newtabpagecompanylogoenabled) |
| Organization logo | Edge policy: [`NewTabPageCompanyLogoBackplateColor`](/en-us/deployedge/microsoft-edge-browser-policies/newtabpagecompanylogobackplatecolor) |
| Quick Links | Edge policy: [NewTabPageHideDefaultTopSites](/en-us/deployedge/microsoft-edge-browser-policies/newtabpagehidedefaulttopsites) |
| Quick Links | Edge policy: [NewTabPageManagedQuickLinks](/en-us/deployedge/microsoft-edge-browser-policies/newtabpagemanagedquicklinks) |
| Quick Links | Edge policy: [NewTabPageQuickLinksEnabled](/en-us/deployedge/microsoft-edge-browser-policies/newtabpagequicklinksenabled) |

### Unsupported new tab page policies

| **Component** | **Policy / configuration experience** |
| --- | --- |
| Copilot Chat Button on other new tab pages | [`NewTabPageBingChatEnabled`](/en-us/deployedge/microsoft-edge-browser-policies/newtabpagebingchatenabled) |
| Discover Feed | News &gt; Microsoft Edge new tab page &gt; Choose default feed for Microsoft Edge new tab page |
| Discover Feed | `NewTabPageContentEnabled` |

We will continue to update functionality and expand policy support as the Copilot new tab page evolves.

For more information on Microsoft Edge policies, see [Microsoft Edge Browser Policy Documentation | Microsoft Learn](/en-us/deployedge/microsoft-edge-policies)

## FAQ and troubleshooting

### Why do my users see different new tab page layouts?

- Users see the Copilot new tab page only when the setting is enabled for them by your organization. If it isn’t enabled, they’ll continue to see the existing Microsoft Edge new tab page experience.

### Can users collapse and hide the Copilot side rail?

Yes. Users can collapse or expand the Copilot side rail through the top-left navigation icon based on their preferred workflow. The selected preference is remembered when users open future new tabs.

### How do I customize the Discover feed settings?

Users can personalize their Discover feed language and content to better curate their feed.

To customize Discover feed settings:

1. Select the **Discover** feed toggle.
2. Select the **Settings (gear icon)** in the top-left corner.
3. Select **Feed settings**.
4. Choose your preferred language and content options.

![image7.](media/microsoft-edge-configure-the-copilot-new-tab-page/img7.png)

### When I click on my Copilot prompts, I see “This prompt is no longer available".

![image8.](media/microsoft-edge-configure-the-copilot-new-tab-page/img8.png)

If Copilot prompts are showing an error, please try refreshing your account session and ensure your Edge and Copilot accounts match:

1. Go to https://m365.cloud.microsoft.
2. Select the account picker in the bottom-left corner.
3. Sign out of your account.
4. Sign back in.

### Can users turn off Work cards?

- Yes. Users can turn off **Cards** the new tab page Settings (sliders icon).
- Yes. Users can switch between **Work cards** and **Chat chips** from the new tab page Settings (gear icon).

### I see errors on Work cards. What should I do?

- Confirm you’re signed in to Microsoft Edge and that **“Sync is on”** in your profile settings.

![image6.](media/microsoft-edge-configure-the-copilot-new-tab-page/img6.png)

- If “Setting up sync” or “Not syncing” is showing, sign out of Microsoft Edge and sign back in. If the issue continues, see [Diagnose and fix Microsoft Edge sync issues | Microsoft Learn](/en-us/deployedge/microsoft-edge-troubleshoot-enterprise-sync).
- If **Sync is on** and the issue persists, close Microsoft Edge and reopen it, or restart the device to ensure sync is up to date. If Microsoft Edge does not close, use Task Manager to end the Microsoft Edge process, and then reopen the browser.

### How do I change the background?

- Open the new tab page Settings (gear icon), then select **Theme settings Change background**. From there, you can choose refresh daily, no image, upload an image, or select a different theme.

### How do I turn off this experience?

- Depending on your organization’s settings, you may be able to turn off this experience. Open the new tab page Settings (gear icon), select **Manage Copilot new tab page More settings** (edge://settings/ai), and then turn off the “Copilot new tab page” setting.