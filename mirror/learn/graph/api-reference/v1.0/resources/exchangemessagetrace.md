---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: exchangeMessageTrace resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/exchangemessagetrace?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: Huajian-MSIT
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: outlook
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
toc.title: Message trace
description: Represents the trace information for an email message as it passes through the Exchange Online organization
ms.date: 2026-01-27T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 5db9b899-ab4d-6442-df8e-b7a7413616ca
document_version_independent_id: bf6c66cb-e407-94f3-324a-82c887006d77
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/exchangemessagetrace.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/exchangemessagetrace
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/exchangemessagetrace.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: ff796a98-c109-4865-808e-b3ab2c6b2f13
---

# exchangeMessageTrace resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents the trace information for an email message as it passes through the Exchange Online organization. Message trace enables tenant administrators to track the lifecycle of an email, determine its delivery status—whether delivered, pending, failed, or quarantined—and understand the actions applied to it.

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List message traces](../messagetracingroot-list-messagetraces) | [exchangeMessageTrace](exchangemessagetrace) collection | Get a list of [exchangeMessageTrace](exchangemessagetrace) objects. |
| [Get details by recipient](../exchangemessagetrace-getdetailsbyrecipient) | [exchangeMessageTraceDetail](exchangemessagetracedetail) collection | Get a list of [exchangeMessageTraceDetail](exchangemessagetracedetail) objects filtered on the recipient. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| fromIP | String | The source IP address. For incoming messages, this value is the public IP address of the SMTP email server that sent the message. Supports `$filter` (`eq`). |
| id | String | The unique identifier for the message trace. Supports `$filter` (`eq`). |
| messageId | String | The Message-ID header field of the message. The format of the Message-ID depends on the messaging server that sent the message. Supports `$filter` (`eq`). |
| receivedDateTime | DateTimeOffset | The date and time when the message was received by Exchange Online. The timestamp is in UTC format. Supports `$filter` (`ge`, `le`). |
| recipientAddress | String | The SMTP email address of the user that the message was addressed to. Supports `$filter` (`eq`). |
| senderAddress | String | The SMTP email address of the user the message was purportedly from. Supports `$filter` (`eq`). |
| size | Int32 | The size of the message in bytes. |
| status | exchangeMessageTraceStatus | The delivery status of the message. The possible values are: `gettingStatus`, `pending`, `failed`, `delivered`, `expanded`, `quarantined`, `filteredAsSpam`, `unknownFutureValue`, `recalled`. Use the `Prefer: include-unknown-enum-members` request header to get the following value in this evolvable enum: `recalled`. Supports `$filter` (`eq`). |
| subject | String | The subject line of the message. Supports `$filter` (`contains`, `startsWith`, `endsWith`). |
| toIP | String | The destination IP address. For outgoing messages, this value is the public IP address in the resolved MX record for the destination domain. For incoming messages to Exchange Online, this value is blank. Supports `$filter` (`eq`). |

## Prerequisites

Before you can use the [List message traces](../messagetracingroot-list-messagetraces) or [Get details by recipient](../exchangemessagetrace-getdetailsbyrecipient) APIs, you must provision a service principal in your tenant for the Microsoft application with the following application (client) ID: `8bd644d1-64a1-4d4b-ae52-2e0cbf64e373`. Provisioning the service principal creates a local representation of the application in your tenant and enables authentication and authorization for these APIs.

To provision the service principal, you can follow these steps:

1. Connect to Microsoft Graph PowerShell: 

    ```PowerShell
    Connect-MgGraph -Scopes "Application.ReadWrite.All"
    ```
2. Run the following command to provision the service principal: 

    ```PowerShell
    New-MgServicePrincipal -AppId 8bd644d1-64a1-4d4b-ae52-2e0cbf64e373
    
    ```

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.exchangeMessageTrace",
  "fromIP": "String",
  "id": "String (identifier)",
  "messageId": "String",
  "receivedDateTime": "String (timestamp)",
  "recipientAddress": "String",
  "senderAddress": "String",
  "size": "Int32",
  "status": "String",
  "subject": "String",
  "toIP": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/exchangemessagetrace?view=graph-rest-beta&accept=text/markdown)
