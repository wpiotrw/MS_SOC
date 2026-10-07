---
layout: Conceptual
title: Microsoft Edge Browser Policy Documentation DeveloperToolsAvailabilityAllowlist | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies/developertoolsavailabilityallowlist
breadcrumb_path: /DeployEdge/breadcrumb/toc.json
recommendations: true
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/help/4021566/windows-10-send-feedback-to-microsoft-with-feedback-hub-app
uhfHeaderId: MSDocsHeader-MSEdge
ms.author: gabrielbanda
author: vmliramichael
manager: nuyunzhang
ms.date: 2026-10-07T00:00:00.0000000Z
audience: ITPro
ms.topic: reference
ms.service: microsoft-edge
ms.subservice: edge-admin
ms.localizationpriority: high
ms.collection: M365-modern-desktop
ms.custom: 
description: 'Windows and Mac documentation for supported Microsoft Edge Browser policy: List of URL patterns where developer tools are allowed'
locale: en-us
document_id: a68fb798-d0c9-2cbf-d053-2e534642e6a6
document_version_independent_id: a68fb798-d0c9-2cbf-d053-2e534642e6a6
original_content_git_url: https://github.com/MicrosoftDocs/Edge-Enterprise-pr/blob/live/edgeenterprise/microsoft-edge-policies/DeveloperToolsAvailabilityAllowlist.md
site_name: Docs
depot_name: office.Edge-Enterprise
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Edge-Enterprise/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: microsoft-edge-policies/developertoolsavailabilityallowlist
moniker_range_name: 
monikers: []
item_type: Content
source_path: edgeenterprise/microsoft-edge-policies/DeveloperToolsAvailabilityAllowlist.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 21306358-fc22-acdf-663f-35229fa0eebb
---

# Microsoft Edge Browser Policy Documentation DeveloperToolsAvailabilityAllowlist | Microsoft Learn

## List of URL patterns where developer tools are allowed

## Supported versions

- Windows: ≥ 148
- macOS: ≥ 148
- Android: ≥ 156
- iOS: Not supported

## Description

This policy controls where developer tools can be used in Microsoft Edge by specifying an allowlist of URL patterns.

Developer tools availability is evaluated for each target being inspected. URL patterns are matched against the target's URL, such as a page, a subframe represented by a separate target, an extension, or a web application. Frames that share a target follow that target's policy result.

If you configure this policy and don't configure the [DeveloperToolsAvailabilityBlocklist](developertoolsavailabilityblocklist) policy, developer tools are available only for targets whose URLs match a pattern in this allowlist. If a target's URL doesn't match, developer tools are blocked for that target. For example, a subframe represented by a separate target can't be inspected if its URL isn't on the allowlist, but an allowlisted main-page target remains inspectable. For information about the URL format, see https://go.microsoft.com/fwlink/?linkid=2095322.

If you configure both this policy and the [DeveloperToolsAvailabilityBlocklist](developertoolsavailabilityblocklist) policy, this allowlist takes precedence. A target whose URL matches this allowlist is allowed even if it also matches the blocklist. A target whose URL matches the blocklist but not this allowlist is blocked. A target whose URL matches neither list is governed by the [DeveloperToolsAvailability](developertoolsavailability) policy.

If you disable or don't configure this policy, developer tools availability is determined by the [DeveloperToolsAvailabilityBlocklist](developertoolsavailabilityblocklist) and [DeveloperToolsAvailability](developertoolsavailability) policies.

This policy applies to developer tools, direct Chrome DevTools Protocol (CDP) connections (for example, using --remote-debugging-port or --remote-debugging-pipe), and CDP connections through the chrome.debugger extension API. The [RemoteDebuggingAllowed](remotedebuggingallowed) policy controls whether remote debugging can start. When remote debugging is allowed, this policy still restricts which targets can be inspected.

Blanket host wildcards (that is, "\*" or "[\*]") aren't allowed. To enable developer tools globally, use the [DeveloperToolsAvailability](developertoolsavailability) policy.

This policy supports up to 1,000 entries.

On Android, this policy controls inspection of targets through remote debugging. It does not enable on-device developer tools.

## Supported features

- Can be mandatory: Yes
- Can be recommended: No
- Dynamic Policy Refresh: Yes
- Per Profile: Yes
- Applies to a profile that is signed in with a Microsoft account: No

## Data type

- List of strings

## Windows information and settings

### Group Policy (ADMX) info

- GP unique name: DeveloperToolsAvailabilityAllowlist
- GP name: List of URL patterns where developer tools are allowed
- GP path (Mandatory): Administrative Templates/Microsoft Edge
- GP path (Recommended): N/A
- GP ADMX file name: MSEdge.admx

#### Example value

```
contoso.com
```

```
https://ssl.server.com
```

```
contoso.com/good_path
```

```
https://server.contoso.com:8080/path
```

```
.exact.hostname.com
```

```
file://*
```

### Registry settings

- Path (Mandatory): SOFTWARE\Policies\Microsoft\Edge\DeveloperToolsAvailabilityAllowlist
- Path (Recommended): N/A
- Value name: 1, 2, 3, ...
- Value type: List of REG\_SZ

#### Example registry value

SOFTWARE\Policies\Microsoft\Edge\DeveloperToolsAvailabilityAllowlist\1 =

```
contoso.com
```

SOFTWARE\Policies\Microsoft\Edge\DeveloperToolsAvailabilityAllowlist\2 =

```
https://ssl.server.com
```

SOFTWARE\Policies\Microsoft\Edge\DeveloperToolsAvailabilityAllowlist\3 =

```
contoso.com/good_path
```

SOFTWARE\Policies\Microsoft\Edge\DeveloperToolsAvailabilityAllowlist\4 =

```
https://server.contoso.com:8080/path
```

SOFTWARE\Policies\Microsoft\Edge\DeveloperToolsAvailabilityAllowlist\5 =

```
.exact.hostname.com
```

SOFTWARE\Policies\Microsoft\Edge\DeveloperToolsAvailabilityAllowlist\6 =

```
file://*
```

## Mac information and settings

- Preference Key name: DeveloperToolsAvailabilityAllowlist
- Example value:

```xml
<array>
  <string>contoso.com</string>
  <string>https://ssl.server.com</string>
  <string>contoso.com/good_path</string>
  <string>https://server.contoso.com:8080/path</string>
  <string>.exact.hostname.com</string>
  <string>file://*</string>
</array>
```

## Android information and settings

- Preference Key name: DeveloperToolsAvailabilityAllowlist
- Example value:

```
["contoso.com", "https://ssl.server.com", "contoso.com/good_path", "https://server.contoso.com:8080/path", ".exact.hostname.com", "file://*"]
```