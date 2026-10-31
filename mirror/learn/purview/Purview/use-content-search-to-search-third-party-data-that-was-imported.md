---
layout: Conceptual
title: Use Content Search to search third-party imported data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/use-content-search-to-search-third-party-data-that-was-imported
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use the Content Search eDiscovery tool to search for items imported to mailboxes in Microsoft 365 from a third-party data source by creating queries.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2025-01-01T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- content-search
search.appverid:
- MOE150
- MET150
ms.custom: seo-marvel-apr2020
locale: en-us
document_id: 0efa0dda-0904-36ce-da81-948abb59376b
document_version_independent_id: 0efa0dda-0904-36ce-da81-948abb59376b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/use-content-search-to-search-third-party-data-that-was-imported.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: use-content-search-to-search-third-party-data-that-was-imported
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/use-content-search-to-search-third-party-data-that-was-imported.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: e4956adc-18cf-7723-63e1-5a5b30f76c1a
---

# Use Content Search to search third-party imported data | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

You can use the [Content search eDiscovery tool](ediscovery-content-search) in the Microsoft Purview portal to search for items imported to mailboxes in Microsoft 365 from a third-party data source. You can create a query to search all imported third-party data items or you can create a query to search specific third-party data items. Also, you can also create a query-based retention policy or a query-based eDiscovery hold to preserve third-party data.

Important

The guidance in this article only applies to third-party data imported by a custom partner connector. This article doesn't apply to third-party data that is imported by using the [third-party data connectors](archive-third-party-data#third-party-data-connectors) in the Microsoft Purview portal.

## Create a query to search all third-party data

To search (or place on hold) any type of third-party data that you've imported to Office 365, you can use the `kind:externaldata` message property-value pair in the keyword box for a Content Search or when creating a query-based hold. For example, to search for items imported from any third-party data source and contain the word "contoso" in the Subject property of the imported item, you would use the following query:

```powershell
kind:externaldata AND subject:contoso
```

When creating queries to search and hold third-party data, you can also use conditions to narrow the search results. For more information about creating Content Search queries, see [Keyword queries and search conditions for Content Search](ediscovery-keyword-queries-and-search-conditions).

## Create a query to search specific types of third-party data

Instead of searching all types of third-party data, you can create queries that only search for a specify type of third-party data by using the following message *property: value* pair in the keyword box for a Content Search:

```powershell
itemclass:ipm.externaldata.<third-party data type>*
```

For example, to search Facebook data that contains the word "contoso" in the Subject property, you would use the following query:

```powershell
itemclass:ipm.externaldata.Facebook* AND subject:contoso
```

The following table lists the third-party data types that you can search, and the value to use for the `itemclass:` message property to specifically search for that type of third-party data. The query syntax isn't case-sensitive.

| **Third-party data type** | **Value for `itemclass:` property** |
| --- | --- |
| AIM | `ipm.externaldata.AIM*` |
| American Idol | `ipm.externaldata.AmericanIdol*` |
| AOL with Pivot Client | `ipm.externaldata.Pivot.IM` |
| Apple Juice | `ipm.externaldata.AppleJuice*` |
| Ares | `ipm.externaldata.Ares*` |
| Axs Encrypted | `ipm.externaldata.AxsEncrypted*` |
| Axs Exchange | `ipm.externaldata.AxsExchange*` |
| Axs Local Archive | `ipm.externaldata.AxsLocalArchive*` |
| Axs Placeholder | `ipm.externaldata.AxsPlaceHolder*` |
| Axs Signed | `ipm.externaldata.AxsSigned*` |
| Bazaarvoice | `ipm.externaldata.Bazaarvoice*` |
| Bearshare | `ipm.externaldata.Bearshare*` |
| BitTorrent | `ipm.externaldata.BitTorrent*` |
| Blackberry | `ipm.externaldata.Blackberry*` |
| BlackBerry Call Logs | `ipm.externaldata.BlackBerryCall*` |
| BlackBerry Messenger | `ipm.externaldata.BlackBerryMessenger*` |
| BlackBerry PIN | `ipm.externaldata.BlackBerryPIN*` |
| BlackBerry SMS | `ipm.externaldata.BlackBerrySMS*` |
| Bloomberg | `ipm.externaldata.Bloomberg*` |
| Bloomberg Message | `ipm.externaldata.conversation.Bloomberg Message*` |
| Bloomberg Messaging | `ipm.externaldata.BloombergMessaging*` |
| Box | `ipm.externaldata.Box*` |
| Cisco IM & Presence Server | `ipm.externaldata.Jabber.IM` |
| Cisco Jabber | `ipm.externaldata.Jabber*` |
| CipherCloud for Salesforce Chatter | `ipm.externaldata.Chatter.Post``ipm.externaldata.Chatter.Comment` |
| Direct Connect | `ipm.externaldata.DirectConnect*` |
| Facebook | `ipm.externaldata.Facebook*` |
| FastTrack | `ipm.externaldata.FastTrack*` |
| FXConnect | `ipm.externaldata.FXConnect.chat` |
| Flickr | `ipm.externaldata.Flickr*` |
| Gnutella | `ipm.externaldata.Gnutella*` |
| Google+ | `ipm.externaldata.GooglePlus*` |
| Google Talk | `ipm.externaldata.GoogleTalk*` |
| GoToMyPC | `ipm.externaldata.GoToMyPC*` |
| HipChat | `ipm.externaldata.HipChat*` |
| Hopster | `ipm.externaldata.Hopster*` |
| HubConnex | `ipm.externaldata.HubConnex*` |
| IBM Connections | `ipm.externaldata.Connections*` |
| IBM SameTime | `ipm.externaldata.Sametime*` |
| ICE Chat | `ipm.externaldata.conversation.Ice Chat*` |
| Indii Messenger | `ipm.externaldata.Indii*` |
| Instagram | `ipm.externaldata.Instagram*` |
| Instant Bloomberg | `ipm.externaldata.InstantBloomberg*` |
| InvestEdge | `ipm.externaldata.InvestEdge*` |
| IRC | `ipm.externaldata.IRC*` |
| Jive | `ipm.externaldata.Jive*` |
| JiveApiRetention | `ipm.externaldata.JiveApiRetention*` |
| JXTA | `ipm.externaldata.JXTA*` |
| LinkedIn | `ipm.externaldata.LinkedIn*` |
| MFTP | `ipm.externaldata.MFTP*` |
| Microsoft UC | `ipm.externaldata.MicrosoftUC*` |
| Mind Align | `ipm.externaldata.MindAlign*` |
| Mobile Guard | `ipm.externaldata.MobileGuard*` |
| MSN | `ipm.externaldata.MSN*` |
| MySpace | `ipm.externaldata.MySpace*` |
| NEONetwork | `ipm.externaldata.NEONetwork*` |
| OpenNap | `ipm.externaldata.OpenNap*` |
| Pinterest | `ipm.externaldata.Pinterest*` |
| Pivot | `ipm.externaldata.Pivot*` |
| QQ | `ipm.externaldata.QQ*` |
| Microsoft SharePoint | `ipm.externaldata.SharePoint*` |
| Salesforce Chatter | `ipm.externaldata.Chatter*` |
| Skype for Business | `ipm.externaldata.Skype*` |
| Slack Enterprise Grid | `ipm.externaldata.Slack.IM` |
| SoftEther | `ipm.externaldata.SoftEther*` |
| Squawker | `ipm.externaldata.Squawker*` |
| Symphony | `ipm.externaldata.Symphony*` |
| Thomson Reuters | `ipm.externaldata.Reuters*` |
| Thomson Reuters Eikon Messenger | `ipm.externaldata.ReutersEikon*` |
| Tor | `ipm.externaldata.Tor*` |
| TTT | `ipm.externaldata.TTT*` |
| Twitter | `ipm.externaldata.Twitter*` |
| UBS Chat | `ipm.externaldata.UBS*` |
| Vimeo | `ipm.externaldata.Vimeo*` |
| WinMX | `ipm.externaldata.WinMX*` |
| Winny | `ipm.externaldata.Winny*` |
| Yahoo! | `ipm.externaldata.Yahoo!*` |
| Viva Engage | `ipm.externaldata.yammer*` |
| YellowJacket | `ipm.externaldata.YellowJacket*` |
| YouTube | `ipm.externaldata.YouTube*` |