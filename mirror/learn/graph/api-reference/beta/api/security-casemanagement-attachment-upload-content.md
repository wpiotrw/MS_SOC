---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: Upload attachment content - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/security-casemanagement-attachment-upload-content?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: alfeldsh
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Upload binary content for a case attachment.
ms.date: 2026-08-04T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: apiPageType
locale: en-us
document_id: 88056072-98f4-5235-5a18-60c021a07ecb
document_version_independent_id: d2176415-cd8f-9c8f-8657-38d61a98898c
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/api/security-casemanagement-attachment-upload-content.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/security-casemanagement-attachment-upload-content
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/api/security-casemanagement-attachment-upload-content.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: bd62bfd3-ad74-e8df-09f6-e205bd3b46dd
---

# Upload attachment content - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.security.caseManagement

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Upload binary content for an [attachment](resources/security-casemanagement-attachment). Create the attachment metadata first by using [Create case attachment](security-casemanagement-case-post-attachments).

The maximum file size is 100 MB. Upload files in chunks of no more than 1 MB. For files larger than 1 MB, send one PUT request for each chunk until all byte ranges are uploaded.

This API is available in the following [national cloud deployments](/en-us/graph/deployments).

| Global service | US Government L4 | US Government L5 (DOD) | China operated by 21Vianet |
| --- | --- | --- | --- |
| ✅ | ❌ | ❌ | ❌ |

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permissions | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | CaseManagement.ReadWrite.All | Not available. |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | CaseManagement.ReadWrite.All | Not available. |

Important

For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This API supports the following built-in roles:

- Global Reader
- Security Reader
- Security Operator
- Security Administrator

## HTTP request

```http
PUT /security/caseManagement/cases/{caseId}/attachments/{attachmentId}/content
```

## Request headers

| Name | Description |
| --- | --- |
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |
| Content-Range | The zero-based, inclusive byte range of the chunk and the total file size, in the format `bytes {start}-{end}/{total}`. The total must match the attachment **fileSize**. Required. |
| Content-Type | `application/octet-stream`. Required. |

## Request body

Supply a binary content chunk of no more than 1 MB.

## Response

When all chunks are uploaded successfully, this method returns a `201 Created` response code and no response body.

After upload completes, the service asynchronously scans the attachment for malware. The content isn't available to download until scanning completes successfully.

## Examples

### Request

The following example uploads an 11-byte file in one chunk.

# [HTTP](#tab/http)
```http
PUT https://graph.microsoft.com/beta/security/caseManagement/cases/{caseId}/attachments/{attachmentId}/content
Content-Type: application/octet-stream
Content-Range: bytes 0-10/11

hello world
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

using var requestBody = new MemoryStream(); //stream to upload

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
await graphClient.Security.CaseManagement.Cases["{case-id}"].Attachments["{attachment-id}"].Content.PutAsContentPutResponseAsync(requestBody);

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v0.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-beta-sdk-go"  //other-imports
)

const requestBody := make([]byte, 0)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
graphClient.Security().CaseManagement().Cases().ByCaseId("case-id").Attachments().ByAttachmentId("attachment-id").Content().PutAsContentPutResponse(context.Background(), requestBody, nil)

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

ByteArrayInputStream stream = new ByteArrayInputStream(new byte[0]); //stream to upload
graphClient.security().caseManagement().cases().byCaseId("{case-id}").attachments().byAttachmentId("{attachment-id}").content().put(stream);

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const stream = hello world;

await client.api('/security/caseManagement/cases/{caseId}/attachments/{attachmentId}/content').version('beta').put(stream);

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph_beta import GraphServiceClient
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = BytesIO()

await graph_client.security.case_management.cases.by_case_id('case-id').attachments.by_attachment_id('attachment-id').content.put(request_body)

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

### Response

The following example shows the response after the upload completes.

```http
HTTP/1.1 201 Created
```