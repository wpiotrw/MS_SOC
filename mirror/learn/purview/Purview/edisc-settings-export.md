---
layout: Conceptual
title: Configure export settings in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-settings-export
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Manage eDiscovery export download settings, including pre-authorized links for large export packages. Learn when to enable resumable downloads based on your environment, security requirements, and network conditions.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-19T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: b2cc73bb-4b6d-9ca2-6f3f-8cc6f4ee454a
document_version_independent_id: b2cc73bb-4b6d-9ca2-6f3f-8cc6f4ee454a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-settings-export.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-settings-export
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-settings-export.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/e2c04606-9985-4e10-b018-2943639291c7
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f257d737-c427-4ae9-949f-35f6148166cf
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 77bd556c-7b0f-10d2-6724-49631b35d9d5
---

# Configure export settings in eDiscovery | Microsoft Learn

Note

This setting isn't available in DoD cloud organizations.

Export settings let you manage download links for all exports in eDiscovery. When exporting large eDiscovery results, network interruptions and browser limitations might affect the download experience. Whether you enable the **Enable export download via pre-authorized link** option depends on your environment, security requirements, network bandwidth, and the tools you plan to use.

Note

For export download best practices, see [Best practices for downloading export packages](edisc-search-export).

Use a pre-authorized link when downloading large export packages or when your network connection might be limited. Large exports take longer to download, which naturally increases the chances of a network interruption during the process. Pre-authorized links are designed for this scenario. By using a pre-authorized link, the download can resume when interrupted. Using a pre-authorized link works with tools that support parallel or chunked downloads, such as third-party download accelerators or browser extensions. When you initiate the download, the pre-authorized download link is generated. The link acts like an access token, so tools can download data without repeated sign-ins.

These links grant direct access to your export. If shared, anyone with the link can access the data. To reduce risk, set the shortest possible expiration time based on the size of your export. You can configure export package download link availability for the following durations:

- 1 hour
- 6 hours
- 12 hours
- 24 hours (default)
- 48 hours
- 72 hours
- 168 hours

Disable pre-authorized link for high bandwidth environments. The standard signed-in download method without pre-authorized links is ideal when you have an ExpressRoute connection with high bandwidth to Microsoft. The standard signed-in download method doesn't generate a pre-authorized token, reducing the risk of link misuse. Each session requires sign-in. If the download is interrupted, you need to re-authenticate and restart. Browser resume behavior varies and isn't guaranteed.

## Enable preauthorized export download links

Important

Don't share export download links with anyone. Treat these links as secrets.

Changing this setting to turn preauthorized links on or off only applies to future export downloads. It doesn't affect existing links. For example, if you enable preauthorized links with a one-day expiration, any links you created before you disable the setting remain valid until they expire. Turning off the pre-authorized export download link setting doesn't retroactively change the behavior of existing links.

To enable preauthorized export download links for your organization:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery *Administrator* permissions.
2. Select the **eDiscovery** solution card, then go to **Settings** &gt; **eDiscovery** &gt; **Export**.
3. Select the toggle for **Enable export download via pre-authorized link**.
4. Select a duration in **Export Link Settings**.
5. Select **Save**.