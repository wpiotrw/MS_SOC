---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: 'userDataSecurityAndGovernance: processContent - Microsoft Graph v1.0 | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/userdatasecurityandgovernance-processcontent?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: ReezaAli149
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
toc.title: 'userDataSecurityAndGovernance: processContent'
description: Process content against data protection policies in the context of the current, or specified, user.
ms.date: 2026-04-22T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: apiPageType
locale: en-us
document_id: b58a8da2-a05c-8adb-9013-21c9b721710e
document_version_independent_id: fe5e1a4b-eeaa-d186-fe79-b7af7380fb19
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/api/userdatasecurityandgovernance-processcontent.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/userdatasecurityandgovernance-processcontent
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/api/userdatasecurityandgovernance-processcontent.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: d129a20a-e586-459d-e8e8-60c28202644e
---

# userDataSecurityAndGovernance: processContent - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Process [content](resources/processcontentrequest) against data protection policies in the context of the current, or specified, user.

This API is available in the following [national cloud deployments](/en-us/graph/deployments).

| Global service | US Government L4 | US Government L5 (DOD) | China operated by 21Vianet |
| --- | --- | --- | --- |
| ✅ | ✅ | ✅ | ❌ |

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permissions | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | Content.Process.User | Content.Process.All |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | Content.Process.User | Content.Process.All |

## HTTP request

```http
POST /me/dataSecurityAndGovernance/processContent
```

Note

Calling the `/me` endpoint requires a signed-in user and therefore a delegated permission. Application permissions aren't supported when using the `/me` endpoint.

```http
POST /users/{userId}/dataSecurityAndGovernance/processContent
```

## Request headers

| Name | Description |
| --- | --- |
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |
| Content-Type | application/json. Required. |
| If-None-Match | Optional. This value is used by the API to determine if the policy state changed since the last call to the API. The value is from the Etag header returned from [protectionScopes compute](userprotectionscopecontainer-compute). If newly computed Etag value doesn't match the value passsed in this header, protectionScopeState property returned will be "modified" and the app needs to refresh by calling [protectionScopes compute](userprotectionscopecontainer-compute). |
| Client-Request-Id | String (GUID recommended). Optional. Unique identifier for this request, which is used for tracing and debugging in logs and support interactions. If an ID is not provided, one may be generated automatically. We recommend that you specify the ID to make tracing and debugging easier. The same ID that was sent in the request will be returned in the response. |

## Request body

In the request body, supply a JSON representation of the parameters.

The following table lists the parameters that are required when you call this action.

| Parameter | Type | Description |
| --- | --- | --- |
| contentToProcess | [processContentRequest](resources/processcontentrequest) | Required. The object containing the content entries and metadata (activity, device, application) to be evaluated for the specified user. |

## Response

If successful, this action returns a `200 OK` response code and a [processContentResponse](resources/processcontentresponse) in the response body or `202 Accepted`, `204 No Content` with no response body.

### Response headers

| Name | Description |
| --- | --- |
| ETag | An indicator that can be used to detect if configured policy state changed. If the policy state changed, the ETag value will change and protectionScopeState property returned will be "modified" and the app needs to refresh by calling [protectionScopes compute](userprotectionscopecontainer-compute). |

## Examples

### Example 1: Enterprise app

#### Request

The following example shows a request from an enterprise app, which can be a non-AI app or an AI app. The text that you send using `data` can be any text from your app — for example, a document body, a chat message, or the user's prompt if your app is an AI app.

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/me/dataSecurityAndGovernance/processContent
Content-Type: application/json
Client-Request-Id: 50dc805c-3af4-42d9-ad16-a746235cc736

{
    "contentToProcess": {
       "contentEntries": [
          {
             "@odata.type": "microsoft.graph.processConversationMetadata",
             "identifier": "07785517-9081-4fe7-a9dc-85bcdf5e9075",
             "content": {
                "@odata.type": "microsoft.graph.textContent", 
                "data": "Write an acceptance letter for Alex Wilber with Credit card number 4532667785213500, ssn: 120-98-1437 at One Microsoft Way, Redmond, WA 98052"
             },
             "name":"PC Purview API Explorer message",
             "correlationId": "d63eafd2-e3a9-4c1a-b726-a2e9b9d9580d",
             "sequenceNumber": 0, 
             "isTruncated": false,
             "createdDateTime": "2025-05-27T17:23:20",
             "modifiedDateTime": "2025-05-27T17:23:20"
          }
       ],
       "activityMetadata": { 
          "activity": "uploadText"
       },
       "deviceMetadata": {
          "deviceType": "Unmanaged",
          "operatingSystemSpecifications": {
             "operatingSystemPlatform": "Windows 11",
             "operatingSystemVersion": "10.0.26100.0" 
          },
          "ipAddress": "127.0.0.1"
       },
       "protectedAppMetadata": {
          "name": "PC Purview API Explorer",
          "version": "0.2",
          "applicationLocation":{
             "@odata.type": "microsoft.graph.policyLocationApplication",
             "value": "83ef208a-0396-4893-9d4f-d36efbffc8bd"
          }
       },
       "integratedAppMetadata": {
          "name": "PC Purview API Explorer",
          "version": "0.2" 
       }
    }
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Me.DataSecurityAndGovernance.ProcessContent;
using Microsoft.Graph.Models;

var requestBody = new ProcessContentPostRequestBody
{ContentToProcess = new ProcessContentRequest{	ContentEntries = new List<ProcessContentMetadataBase>	{		new ProcessConversationMetadata		{			OdataType = "microsoft.graph.processConversationMetadata",			Identifier = "07785517-9081-4fe7-a9dc-85bcdf5e9075",			Content = new TextContent			{				OdataType = "microsoft.graph.textContent",				Data = "Write an acceptance letter for Alex Wilber with Credit card number 4532667785213500, ssn: 120-98-1437 at One Microsoft Way, Redmond, WA 98052",			},			Name = "PC Purview API Explorer message",			CorrelationId = "d63eafd2-e3a9-4c1a-b726-a2e9b9d9580d",			SequenceNumber = 0L,			IsTruncated = false,			CreatedDateTime = DateTimeOffset.Parse("2025-05-27T17:23:20"),			ModifiedDateTime = DateTimeOffset.Parse("2025-05-27T17:23:20"),		},	},	ActivityMetadata = new ActivityMetadata	{		Activity = UserActivityType.UploadText,	},	DeviceMetadata = new DeviceMetadata	{		DeviceType = "Unmanaged",		OperatingSystemSpecifications = new OperatingSystemSpecifications		{			OperatingSystemPlatform = "Windows 11",			OperatingSystemVersion = "10.0.26100.0",		},		IpAddress = "127.0.0.1",	},	ProtectedAppMetadata = new ProtectedApplicationMetadata	{		Name = "PC Purview API Explorer",		Version = "0.2",		ApplicationLocation = new PolicyLocationApplication		{			OdataType = "microsoft.graph.policyLocationApplication",			Value = "83ef208a-0396-4893-9d4f-d36efbffc8bd",		},	},	IntegratedAppMetadata = new IntegratedApplicationMetadata	{		Name = "PC Purview API Explorer",		Version = "0.2",	},},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Me.DataSecurityAndGovernance.ProcessContent.PostAsync(requestBody, (requestConfiguration) =>
{requestConfiguration.Headers.Add("Client-Request-Id", "50dc805c-3af4-42d9-ad16-a746235cc736");
});

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  abstractions "github.com/microsoft/kiota-abstractions-go"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphusers "github.com/microsoftgraph/msgraph-sdk-go/users"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

headers := abstractions.NewRequestHeaders()
headers.Add("Client-Request-Id", "50dc805c-3af4-42d9-ad16-a746235cc736")

configuration := &graphusers.DataSecurityAndGovernanceProcessContentRequestBuilderPostRequestConfiguration{Headers: headers,
}
requestBody := graphusers.NewItemProcessContentPostRequestBody()
contentToProcess := graphmodels.NewProcessContentRequest()

processContentMetadataBase := graphmodels.NewProcessConversationMetadata()
identifier := "07785517-9081-4fe7-a9dc-85bcdf5e9075"
processContentMetadataBase.SetIdentifier(&identifier) 
content := graphmodels.NewTextContent()
data := "Write an acceptance letter for Alex Wilber with Credit card number 4532667785213500, ssn: 120-98-1437 at One Microsoft Way, Redmond, WA 98052"
content.SetData(&data) 
processContentMetadataBase.SetContent(content)
name := "PC Purview API Explorer message"
processContentMetadataBase.SetName(&name) 
correlationId := "d63eafd2-e3a9-4c1a-b726-a2e9b9d9580d"
processContentMetadataBase.SetCorrelationId(&correlationId) 
sequenceNumber := int64(0)
processContentMetadataBase.SetSequenceNumber(&sequenceNumber) 
isTruncated := false
processContentMetadataBase.SetIsTruncated(&isTruncated) 
createdDateTime , err := time.Parse(time.RFC3339, "2025-05-27T17:23:20")
processContentMetadataBase.SetCreatedDateTime(&createdDateTime) 
modifiedDateTime , err := time.Parse(time.RFC3339, "2025-05-27T17:23:20")
processContentMetadataBase.SetModifiedDateTime(&modifiedDateTime) 

contentEntries := []graphmodels.ProcessContentMetadataBaseable {processContentMetadataBase,
}
contentToProcess.SetContentEntries(contentEntries)
activityMetadata := graphmodels.NewActivityMetadata()
activity := graphmodels.UPLOADTEXT_USERACTIVITYTYPE 
activityMetadata.SetActivity(&activity) 
contentToProcess.SetActivityMetadata(activityMetadata)
deviceMetadata := graphmodels.NewDeviceMetadata()
deviceType := "Unmanaged"
deviceMetadata.SetDeviceType(&deviceType) 
operatingSystemSpecifications := graphmodels.NewOperatingSystemSpecifications()
operatingSystemPlatform := "Windows 11"
operatingSystemSpecifications.SetOperatingSystemPlatform(&operatingSystemPlatform) 
operatingSystemVersion := "10.0.26100.0"
operatingSystemSpecifications.SetOperatingSystemVersion(&operatingSystemVersion) 
deviceMetadata.SetOperatingSystemSpecifications(operatingSystemSpecifications)
ipAddress := "127.0.0.1"
deviceMetadata.SetIpAddress(&ipAddress) 
contentToProcess.SetDeviceMetadata(deviceMetadata)
protectedAppMetadata := graphmodels.NewProtectedApplicationMetadata()
name := "PC Purview API Explorer"
protectedAppMetadata.SetName(&name) 
version := "0.2"
protectedAppMetadata.SetVersion(&version) 
applicationLocation := graphmodels.NewPolicyLocationApplication()
value := "83ef208a-0396-4893-9d4f-d36efbffc8bd"
applicationLocation.SetValue(&value) 
protectedAppMetadata.SetApplicationLocation(applicationLocation)
contentToProcess.SetProtectedAppMetadata(protectedAppMetadata)
integratedAppMetadata := graphmodels.NewIntegratedApplicationMetadata()
name := "PC Purview API Explorer"
integratedAppMetadata.SetName(&name) 
version := "0.2"
integratedAppMetadata.SetVersion(&version) 
contentToProcess.SetIntegratedAppMetadata(integratedAppMetadata)
requestBody.SetContentToProcess(contentToProcess)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
processContent, err := graphClient.Me().DataSecurityAndGovernance().ProcessContent().Post(context.Background(), requestBody, configuration)

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.users.item.datasecurityandgovernance.processcontent.ProcessContentPostRequestBody processContentPostRequestBody = new com.microsoft.graph.users.item.datasecurityandgovernance.processcontent.ProcessContentPostRequestBody();
ProcessContentRequest contentToProcess = new ProcessContentRequest();
LinkedList<ProcessContentMetadataBase> contentEntries = new LinkedList<ProcessContentMetadataBase>();
ProcessConversationMetadata processContentMetadataBase = new ProcessConversationMetadata();
processContentMetadataBase.setOdataType("microsoft.graph.processConversationMetadata");
processContentMetadataBase.setIdentifier("07785517-9081-4fe7-a9dc-85bcdf5e9075");
TextContent content = new TextContent();
content.setOdataType("microsoft.graph.textContent");
content.setData("Write an acceptance letter for Alex Wilber with Credit card number 4532667785213500, ssn: 120-98-1437 at One Microsoft Way, Redmond, WA 98052");
processContentMetadataBase.setContent(content);
processContentMetadataBase.setName("PC Purview API Explorer message");
processContentMetadataBase.setCorrelationId("d63eafd2-e3a9-4c1a-b726-a2e9b9d9580d");
processContentMetadataBase.setSequenceNumber(0L);
processContentMetadataBase.setIsTruncated(false);
OffsetDateTime createdDateTime = OffsetDateTime.parse("2025-05-27T17:23:20");
processContentMetadataBase.setCreatedDateTime(createdDateTime);
OffsetDateTime modifiedDateTime = OffsetDateTime.parse("2025-05-27T17:23:20");
processContentMetadataBase.setModifiedDateTime(modifiedDateTime);
contentEntries.add(processContentMetadataBase);
contentToProcess.setContentEntries(contentEntries);
ActivityMetadata activityMetadata = new ActivityMetadata();
activityMetadata.setActivity(UserActivityType.UploadText);
contentToProcess.setActivityMetadata(activityMetadata);
DeviceMetadata deviceMetadata = new DeviceMetadata();
deviceMetadata.setDeviceType("Unmanaged");
OperatingSystemSpecifications operatingSystemSpecifications = new OperatingSystemSpecifications();
operatingSystemSpecifications.setOperatingSystemPlatform("Windows 11");
operatingSystemSpecifications.setOperatingSystemVersion("10.0.26100.0");
deviceMetadata.setOperatingSystemSpecifications(operatingSystemSpecifications);
deviceMetadata.setIpAddress("127.0.0.1");
contentToProcess.setDeviceMetadata(deviceMetadata);
ProtectedApplicationMetadata protectedAppMetadata = new ProtectedApplicationMetadata();
protectedAppMetadata.setName("PC Purview API Explorer");
protectedAppMetadata.setVersion("0.2");
PolicyLocationApplication applicationLocation = new PolicyLocationApplication();
applicationLocation.setOdataType("microsoft.graph.policyLocationApplication");
applicationLocation.setValue("83ef208a-0396-4893-9d4f-d36efbffc8bd");
protectedAppMetadata.setApplicationLocation(applicationLocation);
contentToProcess.setProtectedAppMetadata(protectedAppMetadata);
IntegratedApplicationMetadata integratedAppMetadata = new IntegratedApplicationMetadata();
integratedAppMetadata.setName("PC Purview API Explorer");
integratedAppMetadata.setVersion("0.2");
contentToProcess.setIntegratedAppMetadata(integratedAppMetadata);
processContentPostRequestBody.setContentToProcess(contentToProcess);
var result = graphClient.me().dataSecurityAndGovernance().processContent().post(processContentPostRequestBody, requestConfiguration -> {requestConfiguration.headers.add("Client-Request-Id", "50dc805c-3af4-42d9-ad16-a746235cc736");
});

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const processContentResponse = {
    contentToProcess: {
       contentEntries: [
          {
             '@odata.type': 'microsoft.graph.processConversationMetadata',
             identifier: '07785517-9081-4fe7-a9dc-85bcdf5e9075',
             content: {
                '@odata.type': 'microsoft.graph.textContent', 
                data: 'Write an acceptance letter for Alex Wilber with Credit card number 4532667785213500, ssn: 120-98-1437 at One Microsoft Way, Redmond, WA 98052'
             },
             name: 'PC Purview API Explorer message',
             correlationId: 'd63eafd2-e3a9-4c1a-b726-a2e9b9d9580d',
             sequenceNumber: 0, 
             isTruncated: false,
             createdDateTime: '2025-05-27T17:23:20',
             modifiedDateTime: '2025-05-27T17:23:20'
          }
       ],
       activityMetadata: { 
          activity: 'uploadText'
       },
       deviceMetadata: {
          deviceType: 'Unmanaged',
          operatingSystemSpecifications: {
             operatingSystemPlatform: 'Windows 11',
             operatingSystemVersion: '10.0.26100.0' 
          },
          ipAddress: '127.0.0.1'
       },
       protectedAppMetadata: {
          name: 'PC Purview API Explorer',
          version: '0.2',
          applicationLocation: {
             '@odata.type': 'microsoft.graph.policyLocationApplication',
             value: '83ef208a-0396-4893-9d4f-d36efbffc8bd'
          }
       },
       integratedAppMetadata: {
          name: 'PC Purview API Explorer',
          version: '0.2' 
       }
    }
};

await client.api('/me/dataSecurityAndGovernance/processContent').post(processContentResponse);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Users\Item\DataSecurityAndGovernance\ProcessContent\ProcessContentRequestBuilderPostRequestConfiguration;
use Microsoft\Graph\Generated\Users\Item\DataSecurityAndGovernance\ProcessContent\ProcessContentPostRequestBody;
use Microsoft\Graph\Generated\Models\ProcessContentRequest;
use Microsoft\Graph\Generated\Models\ProcessContentMetadataBase;
use Microsoft\Graph\Generated\Models\ProcessConversationMetadata;
use Microsoft\Graph\Generated\Models\TextContent;
use Microsoft\Graph\Generated\Models\ActivityMetadata;
use Microsoft\Graph\Generated\Models\UserActivityType;
use Microsoft\Graph\Generated\Models\DeviceMetadata;
use Microsoft\Graph\Generated\Models\OperatingSystemSpecifications;
use Microsoft\Graph\Generated\Models\ProtectedApplicationMetadata;
use Microsoft\Graph\Generated\Models\PolicyLocationApplication;
use Microsoft\Graph\Generated\Models\IntegratedApplicationMetadata;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new ProcessContentPostRequestBody();
$contentToProcess = new ProcessContentRequest();
$contentEntriesProcessContentMetadataBase1 = new ProcessConversationMetadata();
$contentEntriesProcessContentMetadataBase1->setOdataType('microsoft.graph.processConversationMetadata');
$contentEntriesProcessContentMetadataBase1->setIdentifier('07785517-9081-4fe7-a9dc-85bcdf5e9075');
$contentEntriesProcessContentMetadataBase1Content = new TextContent();
$contentEntriesProcessContentMetadataBase1Content->setOdataType('microsoft.graph.textContent');
$contentEntriesProcessContentMetadataBase1Content->setData('Write an acceptance letter for Alex Wilber with Credit card number 4532667785213500, ssn: 120-98-1437 at One Microsoft Way, Redmond, WA 98052');
$contentEntriesProcessContentMetadataBase1->setContent($contentEntriesProcessContentMetadataBase1Content);
$contentEntriesProcessContentMetadataBase1->setName('PC Purview API Explorer message');
$contentEntriesProcessContentMetadataBase1->setCorrelationId('d63eafd2-e3a9-4c1a-b726-a2e9b9d9580d');
$contentEntriesProcessContentMetadataBase1->setSequenceNumber(0);
$contentEntriesProcessContentMetadataBase1->setIsTruncated(false);
$contentEntriesProcessContentMetadataBase1->setCreatedDateTime(new \DateTime('2025-05-27T17:23:20'));
$contentEntriesProcessContentMetadataBase1->setModifiedDateTime(new \DateTime('2025-05-27T17:23:20'));
$contentEntriesArray []= $contentEntriesProcessContentMetadataBase1;
$contentToProcess->setContentEntries($contentEntriesArray);

$contentToProcessActivityMetadata = new ActivityMetadata();
$contentToProcessActivityMetadata->setActivity(new UserActivityType('uploadText'));
$contentToProcess->setActivityMetadata($contentToProcessActivityMetadata);
$contentToProcessDeviceMetadata = new DeviceMetadata();
$contentToProcessDeviceMetadata->setDeviceType('Unmanaged');
$contentToProcessDeviceMetadataOperatingSystemSpecifications = new OperatingSystemSpecifications();
$contentToProcessDeviceMetadataOperatingSystemSpecifications->setOperatingSystemPlatform('Windows 11');
$contentToProcessDeviceMetadataOperatingSystemSpecifications->setOperatingSystemVersion('10.0.26100.0');
$contentToProcessDeviceMetadata->setOperatingSystemSpecifications($contentToProcessDeviceMetadataOperatingSystemSpecifications);
$contentToProcessDeviceMetadata->setIpAddress('127.0.0.1');
$contentToProcess->setDeviceMetadata($contentToProcessDeviceMetadata);
$contentToProcessProtectedAppMetadata = new ProtectedApplicationMetadata();
$contentToProcessProtectedAppMetadata->setName('PC Purview API Explorer');
$contentToProcessProtectedAppMetadata->setVersion('0.2');
$contentToProcessProtectedAppMetadataApplicationLocation = new PolicyLocationApplication();
$contentToProcessProtectedAppMetadataApplicationLocation->setOdataType('microsoft.graph.policyLocationApplication');
$contentToProcessProtectedAppMetadataApplicationLocation->setValue('83ef208a-0396-4893-9d4f-d36efbffc8bd');
$contentToProcessProtectedAppMetadata->setApplicationLocation($contentToProcessProtectedAppMetadataApplicationLocation);
$contentToProcess->setProtectedAppMetadata($contentToProcessProtectedAppMetadata);
$contentToProcessIntegratedAppMetadata = new IntegratedApplicationMetadata();
$contentToProcessIntegratedAppMetadata->setName('PC Purview API Explorer');
$contentToProcessIntegratedAppMetadata->setVersion('0.2');
$contentToProcess->setIntegratedAppMetadata($contentToProcessIntegratedAppMetadata);
$requestBody->setContentToProcess($contentToProcess);
$requestConfiguration = new ProcessContentRequestBuilderPostRequestConfiguration();
$headers = ['Client-Request-Id' => '50dc805c-3af4-42d9-ad16-a746235cc736',
];
$requestConfiguration->headers = $headers;

$result = $graphServiceClient->me()->dataSecurityAndGovernance()->processContent()->post($requestBody, $requestConfiguration)->wait();

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.users.item.data_security_and_governance.process_content.process_content_request_builder import ProcessContentRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from msgraph.generated.users.item.datasecurityandgovernance.process_content.process_content_post_request_body import ProcessContentPostRequestBody
from msgraph.generated.models.process_content_request import ProcessContentRequest
from msgraph.generated.models.process_content_metadata_base import ProcessContentMetadataBase
from msgraph.generated.models.process_conversation_metadata import ProcessConversationMetadata
from msgraph.generated.models.text_content import TextContent
from msgraph.generated.models.activity_metadata import ActivityMetadata
from msgraph.generated.models.user_activity_type import UserActivityType
from msgraph.generated.models.device_metadata import DeviceMetadata
from msgraph.generated.models.operating_system_specifications import OperatingSystemSpecifications
from msgraph.generated.models.protected_application_metadata import ProtectedApplicationMetadata
from msgraph.generated.models.policy_location_application import PolicyLocationApplication
from msgraph.generated.models.integrated_application_metadata import IntegratedApplicationMetadata
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = ProcessContentPostRequestBody(content_to_process = ProcessContentRequest(	content_entries = [		ProcessConversationMetadata(			odata_type = "microsoft.graph.processConversationMetadata",			identifier = "07785517-9081-4fe7-a9dc-85bcdf5e9075",			content = TextContent(				odata_type = "microsoft.graph.textContent",				data = "Write an acceptance letter for Alex Wilber with Credit card number 4532667785213500, ssn: 120-98-1437 at One Microsoft Way, Redmond, WA 98052",			),			name = "PC Purview API Explorer message",			correlation_id = "d63eafd2-e3a9-4c1a-b726-a2e9b9d9580d",			sequence_number = 0,			is_truncated = False,			created_date_time = "2025-05-27T17:23:20",			modified_date_time = "2025-05-27T17:23:20",		),	],	activity_metadata = ActivityMetadata(		activity = UserActivityType.UploadText,	),	device_metadata = DeviceMetadata(		device_type = "Unmanaged",		operating_system_specifications = OperatingSystemSpecifications(			operating_system_platform = "Windows 11",			operating_system_version = "10.0.26100.0",		),		ip_address = "127.0.0.1",	),	protected_app_metadata = ProtectedApplicationMetadata(		name = "PC Purview API Explorer",		version = "0.2",		application_location = PolicyLocationApplication(			odata_type = "microsoft.graph.policyLocationApplication",			value = "83ef208a-0396-4893-9d4f-d36efbffc8bd",		),	),	integrated_app_metadata = IntegratedApplicationMetadata(		name = "PC Purview API Explorer",		version = "0.2",	),),
)

request_configuration = RequestConfiguration()
request_configuration.headers.add("Client-Request-Id", "50dc805c-3af4-42d9-ad16-a746235cc736")

result = await graph_client.me.data_security_and_governance.process_content.post(request_body, request_configuration = request_configuration)

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

#### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json
Client-Request-Id: 50dc805c-3af4-42d9-ad16-a746235cc736

{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#microsoft.graph.processContentResponse",
  "protectionScopeState": "notModified",
  "policyActions": [],
  "processingErrors": []
}
```

### Example 2: AI Agent

#### Request

The following example shows a request sent from an AI agent. In the request, notice that there's an `agents` array which is of type `aiAgentInfo`. In this example, `data` is used to send the user's prompt.

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/users/5def8f26-aff8-4db6-a08c-0fcf8f1aa2ba/dataSecurityAndGovernance/processContent
Content-Type: application/json

{
    "contentToProcess": {
      "contentEntries": [
        {
          "@odata.type": "microsoft.graph.processConversationMetadata",
          "identifier": "42837765-85c9-4a28-a165-27b6aaa5f635",
          "content": {
            "@odata.type": "microsoft.graph.textContent",
            "data": "For application 123456789, Write an acceptance letter for Alex Wilber with Credit card number 0000111122223333, ssn: 000-11-2222 at One Microsoft Way, Redmond, WA 98052"
          },
          "agents": [
            {
              "@odata.type": "microsoft.graph.aiAgentInfo",
              "blueprintId": "c84571c6-5ef3-4af7-aed2-0491cfd362a0",
              "identifier": "89515a70-a236-43be-b977-3ff0b454f853",
              "name": "Demo Agent",
              "version": "1.0"
            }
          ],
          "name":"PC Purview API Explorer message",
          "correlationId": "1cd5e33a-c78f-46e4-a242-74b0ef910486",
          "sequenceNumber": 0,
             "isTruncated": false,
             "createdDateTime": "2026-04-08T20:52:08",
             "modifiedDateTime": "2026-04-08T20:52:08"
          }
       ],
       "activityMetadata": { 
          "activity": "uploadText"
       },
       "deviceMetadata": {
          "operatingSystemSpecifications": {
             "operatingSystemPlatform": "Windows 11",
             "operatingSystemVersion": "10.0.26200.0" 
          },
          "ipAddress": "127.0.0.1"
       },
       "protectedAppMetadata": {
          "name": "PC Purview API Explorer",
          "version": "0.2",
          "applicationLocation":{
             "@odata.type": "microsoft.graph.policyLocationApplication",
             "value": "83ef198a-0396-4893-9d4f-d36efbffc8bd"
          }
       },
       "integratedAppMetadata": {
          "name": "PC Purview API Explorer",
          "version": "0.1" 
       }
    }
}

```

# [C#](#tab/csharp)
```
Snippet not available
```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Go](#tab/go)
```
Snippet not available
```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Java](#tab/java)
```
Snippet not available
```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const processContentResponse = {
    contentToProcess: {
      contentEntries: [
        {
          '@odata.type': 'microsoft.graph.processConversationMetadata',
          identifier: '42837765-85c9-4a28-a165-27b6aaa5f635',
          content: {
            '@odata.type': 'microsoft.graph.textContent',
            data: 'For application 123456789, Write an acceptance letter for Alex Wilber with Credit card number 0000111122223333, ssn: 000-11-2222 at One Microsoft Way, Redmond, WA 98052'
          },
          agents: [
            {
              '@odata.type': 'microsoft.graph.aiAgentInfo',
              blueprintId: 'c84571c6-5ef3-4af7-aed2-0491cfd362a0',
              identifier: '89515a70-a236-43be-b977-3ff0b454f853',
              name: 'Demo Agent',
              version: '1.0'
            }
          ],
          name: 'PC Purview API Explorer message',
          correlationId: '1cd5e33a-c78f-46e4-a242-74b0ef910486',
          sequenceNumber: 0,
             isTruncated: false,
             createdDateTime: '2026-04-08T20:52:08',
             modifiedDateTime: '2026-04-08T20:52:08'
          }
       ],
       activityMetadata: { 
          activity: 'uploadText'
       },
       deviceMetadata: {
          operatingSystemSpecifications: {
             operatingSystemPlatform: 'Windows 11',
             operatingSystemVersion: '10.0.26200.0' 
          },
          ipAddress: '127.0.0.1'
       },
       protectedAppMetadata: {
          name: 'PC Purview API Explorer',
          version: '0.2',
          applicationLocation: {
             '@odata.type': 'microsoft.graph.policyLocationApplication',
             value: '83ef198a-0396-4893-9d4f-d36efbffc8bd'
          }
       },
       integratedAppMetadata: {
          name: 'PC Purview API Explorer',
          version: '0.1' 
       }
    }
};

await client.api('/users/5def8f26-aff8-4db6-a08c-0fcf8f1aa2ba/dataSecurityAndGovernance/processContent').post(processContentResponse);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PHP](#tab/php)
```
Snippet not available
```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Python](#tab/python)
```
Snippet not available
```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

#### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#microsoft.graph.processContentResponse",
  "protectionScopeState": "modified",
  "policyActions": [
    {
      "@odata.type": "#microsoft.graph.restrictAccessAction",
      "action": "restrictAccess",
      "restrictionAction": "block"
    }
  ],
  "processingErrors": []
}
```

### Example 3: Network provider app

#### Request

The following example shows a request.

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/users/5def8f26-aff8-4db6-a08c-0fcf8f1aa2ba/dataSecurityAndGovernance/processContent
Content-Type: application/json

{"contentToProcess": {	"contentEntries": [		{			"@odata.type": "#microsoft.graph.processConversationMetadata",			"identifier": "f7af180f-dc2e-467c-9719-757e1c61eabf",			"content": {				"@odata.type": "#microsoft.graph.textContent",				"data": "some data"			},			"correlationId": "d63eafd2-e3a9-4c1a-b726-a2e9b9d95811",			"sequenceNumber": 0,			"name": "Test Content"		}	],	"activityMetadata": {		"activity": "uploadText"	},	"deviceMetadata": {		"deviceType": "unmanaged",		"ipAddress": null,		"operatingSystemSpecifications": {			"operatingSystemPlatform": "Windows",			"operatingSystemVersion": "11.1"		}	},	"integratedAppMetadata": {		"name": "My Entra App",		"version": "0.1"	},	"protectedAppMetadata": {		"name": "My Entra App",		"version": "0.1",		"applicationLocation": {			"@odata.type": "#microsoft.graph.policyLocationUrl",			"value": "https://gemini.google.com"		}	}}
}

```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Users.Item.DataSecurityAndGovernance.ProcessContent;
using Microsoft.Graph.Models;

var requestBody = new ProcessContentPostRequestBody
{ContentToProcess = new ProcessContentRequest{	ContentEntries = new List<ProcessContentMetadataBase>	{		new ProcessConversationMetadata		{			OdataType = "#microsoft.graph.processConversationMetadata",			Identifier = "f7af180f-dc2e-467c-9719-757e1c61eabf",			Content = new TextContent			{				OdataType = "#microsoft.graph.textContent",				Data = "some data",			},			CorrelationId = "d63eafd2-e3a9-4c1a-b726-a2e9b9d95811",			SequenceNumber = 0L,			Name = "Test Content",		},	},	ActivityMetadata = new ActivityMetadata	{		Activity = UserActivityType.UploadText,	},	DeviceMetadata = new DeviceMetadata	{		DeviceType = "unmanaged",		IpAddress = null,		OperatingSystemSpecifications = new OperatingSystemSpecifications		{			OperatingSystemPlatform = "Windows",			OperatingSystemVersion = "11.1",		},	},	IntegratedAppMetadata = new IntegratedApplicationMetadata	{		Name = "My Entra App",		Version = "0.1",	},	ProtectedAppMetadata = new ProtectedApplicationMetadata	{		Name = "My Entra App",		Version = "0.1",		ApplicationLocation = new PolicyLocationUrl		{			OdataType = "#microsoft.graph.policyLocationUrl",			Value = "https://gemini.google.com",		},	},},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Users["{user-id}"].DataSecurityAndGovernance.ProcessContent.PostAsync(requestBody);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphusers "github.com/microsoftgraph/msgraph-sdk-go/users"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

requestBody := graphusers.NewProcessContentPostRequestBody()
contentToProcess := graphmodels.NewProcessContentRequest()

processContentMetadataBase := graphmodels.NewProcessConversationMetadata()
identifier := "f7af180f-dc2e-467c-9719-757e1c61eabf"
processContentMetadataBase.SetIdentifier(&identifier) 
content := graphmodels.NewTextContent()
data := "some data"
content.SetData(&data) 
processContentMetadataBase.SetContent(content)
correlationId := "d63eafd2-e3a9-4c1a-b726-a2e9b9d95811"
processContentMetadataBase.SetCorrelationId(&correlationId) 
sequenceNumber := int64(0)
processContentMetadataBase.SetSequenceNumber(&sequenceNumber) 
name := "Test Content"
processContentMetadataBase.SetName(&name) 

contentEntries := []graphmodels.ProcessContentMetadataBaseable {processContentMetadataBase,
}
contentToProcess.SetContentEntries(contentEntries)
activityMetadata := graphmodels.NewActivityMetadata()
activity := graphmodels.UPLOADTEXT_USERACTIVITYTYPE 
activityMetadata.SetActivity(&activity) 
contentToProcess.SetActivityMetadata(activityMetadata)
deviceMetadata := graphmodels.NewDeviceMetadata()
deviceType := "unmanaged"
deviceMetadata.SetDeviceType(&deviceType) 
ipAddress := null
deviceMetadata.SetIpAddress(&ipAddress) 
operatingSystemSpecifications := graphmodels.NewOperatingSystemSpecifications()
operatingSystemPlatform := "Windows"
operatingSystemSpecifications.SetOperatingSystemPlatform(&operatingSystemPlatform) 
operatingSystemVersion := "11.1"
operatingSystemSpecifications.SetOperatingSystemVersion(&operatingSystemVersion) 
deviceMetadata.SetOperatingSystemSpecifications(operatingSystemSpecifications)
contentToProcess.SetDeviceMetadata(deviceMetadata)
integratedAppMetadata := graphmodels.NewIntegratedApplicationMetadata()
name := "My Entra App"
integratedAppMetadata.SetName(&name) 
version := "0.1"
integratedAppMetadata.SetVersion(&version) 
contentToProcess.SetIntegratedAppMetadata(integratedAppMetadata)
protectedAppMetadata := graphmodels.NewProtectedApplicationMetadata()
name := "My Entra App"
protectedAppMetadata.SetName(&name) 
version := "0.1"
protectedAppMetadata.SetVersion(&version) 
applicationLocation := graphmodels.NewPolicyLocationUrl()
value := "https://gemini.google.com"
applicationLocation.SetValue(&value) 
protectedAppMetadata.SetApplicationLocation(applicationLocation)
contentToProcess.SetProtectedAppMetadata(protectedAppMetadata)
requestBody.SetContentToProcess(contentToProcess)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
processContent, err := graphClient.Users().ByUserId("user-id").DataSecurityAndGovernance().ProcessContent().Post(context.Background(), requestBody, nil)

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.users.item.datasecurityandgovernance.processcontent.ProcessContentPostRequestBody processContentPostRequestBody = new com.microsoft.graph.users.item.datasecurityandgovernance.processcontent.ProcessContentPostRequestBody();
ProcessContentRequest contentToProcess = new ProcessContentRequest();
LinkedList<ProcessContentMetadataBase> contentEntries = new LinkedList<ProcessContentMetadataBase>();
ProcessConversationMetadata processContentMetadataBase = new ProcessConversationMetadata();
processContentMetadataBase.setOdataType("#microsoft.graph.processConversationMetadata");
processContentMetadataBase.setIdentifier("f7af180f-dc2e-467c-9719-757e1c61eabf");
TextContent content = new TextContent();
content.setOdataType("#microsoft.graph.textContent");
content.setData("some data");
processContentMetadataBase.setContent(content);
processContentMetadataBase.setCorrelationId("d63eafd2-e3a9-4c1a-b726-a2e9b9d95811");
processContentMetadataBase.setSequenceNumber(0L);
processContentMetadataBase.setName("Test Content");
contentEntries.add(processContentMetadataBase);
contentToProcess.setContentEntries(contentEntries);
ActivityMetadata activityMetadata = new ActivityMetadata();
activityMetadata.setActivity(UserActivityType.UploadText);
contentToProcess.setActivityMetadata(activityMetadata);
DeviceMetadata deviceMetadata = new DeviceMetadata();
deviceMetadata.setDeviceType("unmanaged");
deviceMetadata.setIpAddress(null);
OperatingSystemSpecifications operatingSystemSpecifications = new OperatingSystemSpecifications();
operatingSystemSpecifications.setOperatingSystemPlatform("Windows");
operatingSystemSpecifications.setOperatingSystemVersion("11.1");
deviceMetadata.setOperatingSystemSpecifications(operatingSystemSpecifications);
contentToProcess.setDeviceMetadata(deviceMetadata);
IntegratedApplicationMetadata integratedAppMetadata = new IntegratedApplicationMetadata();
integratedAppMetadata.setName("My Entra App");
integratedAppMetadata.setVersion("0.1");
contentToProcess.setIntegratedAppMetadata(integratedAppMetadata);
ProtectedApplicationMetadata protectedAppMetadata = new ProtectedApplicationMetadata();
protectedAppMetadata.setName("My Entra App");
protectedAppMetadata.setVersion("0.1");
PolicyLocationUrl applicationLocation = new PolicyLocationUrl();
applicationLocation.setOdataType("#microsoft.graph.policyLocationUrl");
applicationLocation.setValue("https://gemini.google.com");
protectedAppMetadata.setApplicationLocation(applicationLocation);
contentToProcess.setProtectedAppMetadata(protectedAppMetadata);
processContentPostRequestBody.setContentToProcess(contentToProcess);
var result = graphClient.users().byUserId("{user-id}").dataSecurityAndGovernance().processContent().post(processContentPostRequestBody);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const processContentResponse = {contentToProcess: {	contentEntries: [		{			'@odata.type': '#microsoft.graph.processConversationMetadata',			identifier: 'f7af180f-dc2e-467c-9719-757e1c61eabf',			content: {				'@odata.type': '#microsoft.graph.textContent',				data: 'some data'			},			correlationId: 'd63eafd2-e3a9-4c1a-b726-a2e9b9d95811',			sequenceNumber: 0,			name: 'Test Content'		}	],	activityMetadata: {		activity: 'uploadText'	},	deviceMetadata: {		deviceType: 'unmanaged',		ipAddress: null,		operatingSystemSpecifications: {			operatingSystemPlatform: 'Windows',			operatingSystemVersion: '11.1'		}	},	integratedAppMetadata: {		name: 'My Entra App',		version: '0.1'	},	protectedAppMetadata: {		name: 'My Entra App',		version: '0.1',		applicationLocation: {			'@odata.type': '#microsoft.graph.policyLocationUrl',			value: 'https://gemini.google.com'		}	}}
};

await client.api('/users/5def8f26-aff8-4db6-a08c-0fcf8f1aa2ba/dataSecurityAndGovernance/processContent').post(processContentResponse);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Users\Item\DataSecurityAndGovernance\ProcessContent\ProcessContentPostRequestBody;
use Microsoft\Graph\Generated\Models\ProcessContentRequest;
use Microsoft\Graph\Generated\Models\ProcessContentMetadataBase;
use Microsoft\Graph\Generated\Models\ProcessConversationMetadata;
use Microsoft\Graph\Generated\Models\TextContent;
use Microsoft\Graph\Generated\Models\ActivityMetadata;
use Microsoft\Graph\Generated\Models\UserActivityType;
use Microsoft\Graph\Generated\Models\DeviceMetadata;
use Microsoft\Graph\Generated\Models\OperatingSystemSpecifications;
use Microsoft\Graph\Generated\Models\IntegratedApplicationMetadata;
use Microsoft\Graph\Generated\Models\ProtectedApplicationMetadata;
use Microsoft\Graph\Generated\Models\PolicyLocationUrl;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new ProcessContentPostRequestBody();
$contentToProcess = new ProcessContentRequest();
$contentEntriesProcessContentMetadataBase1 = new ProcessConversationMetadata();
$contentEntriesProcessContentMetadataBase1->setOdataType('#microsoft.graph.processConversationMetadata');
$contentEntriesProcessContentMetadataBase1->setIdentifier('f7af180f-dc2e-467c-9719-757e1c61eabf');
$contentEntriesProcessContentMetadataBase1Content = new TextContent();
$contentEntriesProcessContentMetadataBase1Content->setOdataType('#microsoft.graph.textContent');
$contentEntriesProcessContentMetadataBase1Content->setData('some data');
$contentEntriesProcessContentMetadataBase1->setContent($contentEntriesProcessContentMetadataBase1Content);
$contentEntriesProcessContentMetadataBase1->setCorrelationId('d63eafd2-e3a9-4c1a-b726-a2e9b9d95811');
$contentEntriesProcessContentMetadataBase1->setSequenceNumber(0);
$contentEntriesProcessContentMetadataBase1->setName('Test Content');
$contentEntriesArray []= $contentEntriesProcessContentMetadataBase1;
$contentToProcess->setContentEntries($contentEntriesArray);

$contentToProcessActivityMetadata = new ActivityMetadata();
$contentToProcessActivityMetadata->setActivity(new UserActivityType('uploadText'));
$contentToProcess->setActivityMetadata($contentToProcessActivityMetadata);
$contentToProcessDeviceMetadata = new DeviceMetadata();
$contentToProcessDeviceMetadata->setDeviceType('unmanaged');
$contentToProcessDeviceMetadata->setIpAddress(null);
$contentToProcessDeviceMetadataOperatingSystemSpecifications = new OperatingSystemSpecifications();
$contentToProcessDeviceMetadataOperatingSystemSpecifications->setOperatingSystemPlatform('Windows');
$contentToProcessDeviceMetadataOperatingSystemSpecifications->setOperatingSystemVersion('11.1');
$contentToProcessDeviceMetadata->setOperatingSystemSpecifications($contentToProcessDeviceMetadataOperatingSystemSpecifications);
$contentToProcess->setDeviceMetadata($contentToProcessDeviceMetadata);
$contentToProcessIntegratedAppMetadata = new IntegratedApplicationMetadata();
$contentToProcessIntegratedAppMetadata->setName('My Entra App');
$contentToProcessIntegratedAppMetadata->setVersion('0.1');
$contentToProcess->setIntegratedAppMetadata($contentToProcessIntegratedAppMetadata);
$contentToProcessProtectedAppMetadata = new ProtectedApplicationMetadata();
$contentToProcessProtectedAppMetadata->setName('My Entra App');
$contentToProcessProtectedAppMetadata->setVersion('0.1');
$contentToProcessProtectedAppMetadataApplicationLocation = new PolicyLocationUrl();
$contentToProcessProtectedAppMetadataApplicationLocation->setOdataType('#microsoft.graph.policyLocationUrl');
$contentToProcessProtectedAppMetadataApplicationLocation->setValue('https://gemini.google.com');
$contentToProcessProtectedAppMetadata->setApplicationLocation($contentToProcessProtectedAppMetadataApplicationLocation);
$contentToProcess->setProtectedAppMetadata($contentToProcessProtectedAppMetadata);
$requestBody->setContentToProcess($contentToProcess);

$result = $graphServiceClient->users()->byUserId('user-id')->dataSecurityAndGovernance()->processContent()->post($requestBody)->wait();

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.users.item.datasecurityandgovernance.process_content.process_content_post_request_body import ProcessContentPostRequestBody
from msgraph.generated.models.process_content_request import ProcessContentRequest
from msgraph.generated.models.process_content_metadata_base import ProcessContentMetadataBase
from msgraph.generated.models.process_conversation_metadata import ProcessConversationMetadata
from msgraph.generated.models.text_content import TextContent
from msgraph.generated.models.activity_metadata import ActivityMetadata
from msgraph.generated.models.user_activity_type import UserActivityType
from msgraph.generated.models.device_metadata import DeviceMetadata
from msgraph.generated.models.operating_system_specifications import OperatingSystemSpecifications
from msgraph.generated.models.integrated_application_metadata import IntegratedApplicationMetadata
from msgraph.generated.models.protected_application_metadata import ProtectedApplicationMetadata
from msgraph.generated.models.policy_location_url import PolicyLocationUrl
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = ProcessContentPostRequestBody(content_to_process = ProcessContentRequest(	content_entries = [		ProcessConversationMetadata(			odata_type = "#microsoft.graph.processConversationMetadata",			identifier = "f7af180f-dc2e-467c-9719-757e1c61eabf",			content = TextContent(				odata_type = "#microsoft.graph.textContent",				data = "some data",			),			correlation_id = "d63eafd2-e3a9-4c1a-b726-a2e9b9d95811",			sequence_number = 0,			name = "Test Content",		),	],	activity_metadata = ActivityMetadata(		activity = UserActivityType.UploadText,	),	device_metadata = DeviceMetadata(		device_type = "unmanaged",		ip_address = None,		operating_system_specifications = OperatingSystemSpecifications(			operating_system_platform = "Windows",			operating_system_version = "11.1",		),	),	integrated_app_metadata = IntegratedApplicationMetadata(		name = "My Entra App",		version = "0.1",	),	protected_app_metadata = ProtectedApplicationMetadata(		name = "My Entra App",		version = "0.1",		application_location = PolicyLocationUrl(			odata_type = "#microsoft.graph.policyLocationUrl",			value = "https://gemini.google.com",		),	),),
)

result = await graph_client.users.by_user_id('user-id').data_security_and_governance.process_content.post(request_body)

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

#### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#microsoft.graph.processContentResponse",
  "protectionScopeState": "modified",
  "policyActions": [
    {
      "@odata.type": "#microsoft.graph.restrictAccessAction",
      "action": "restrictAccess",
      "restrictionAction": "block"
    }
  ],
  "processingErrors": []
}
```

### Example 4: Network provider app with file content

#### Request

The following example shows a request.

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/users/5def8f26-aff8-4db6-a08c-0fcf8f1aa2ba/dataSecurityAndGovernance/processContent
Content-Type: application/json

{"contentToProcess": {	"contentEntries": [		{			"@odata.type": "#microsoft.graph.processFileMetadata",			"identifier": "f7af180f-dc2e-467c-9719-757e1c61eabf",			"content": {			"@odata.type": "#microsoft.graph.textContent",				"data": "Base64 encoded content"			},			"name": "Test File.docx",			"correlationId": "d63eafd2-e3a9-4c1a-b726-a2e9b9d95822",			"createdDateTime": "2024-07-23T01:31:40.2020463Z",			"modifiedDateTime": "2024-09-17T13:45:21.0000000Z",			"correlationId": "9d84223c-521c-42f4-8f35-3cdeabe515d3",			"length": 17352,			"isTruncated": false,			"ownerId": "ffe1ca70-6e5b-4120-abf0-472034ba05d4",			"customProperties": {				"Department": "Finance",				"ReviewerName": "John Smith"			}		}	],	"activityMetadata": {		"activity": "uploadFile"	},	"deviceMetadata": {		"deviceType": "unmanaged",		"operatingSystemSpecifications": {			"operatingSystemPlatform": "Windows",			"operatingSystemVersion": "11.1"		}	},	"integratedAppMetadata": {		"name": "Network Proxy App",		"version": "1.0.0"	},	"protectedAppMetadata": {		"name": "My App",		"version": "0.1",		"applicationLocation": {			"@odata.type": "#microsoft.graph.policyLocationUrl",			"value": "https://gemini.google.com"		}	}}
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Users.Item.DataSecurityAndGovernance.ProcessContent;
using Microsoft.Graph.Models;

var requestBody = new ProcessContentPostRequestBody
{ContentToProcess = new ProcessContentRequest{	ContentEntries = new List<ProcessContentMetadataBase>	{		new ProcessFileMetadata		{			OdataType = "#microsoft.graph.processFileMetadata",			Identifier = "f7af180f-dc2e-467c-9719-757e1c61eabf",			Content = new TextContent			{				OdataType = "#microsoft.graph.textContent",				Data = "Base64 encoded content",			},			Name = "Test File.docx",			CorrelationId = "d63eafd2-e3a9-4c1a-b726-a2e9b9d95822",			CreatedDateTime = DateTimeOffset.Parse("2024-07-23T01:31:40.2020463Z"),			ModifiedDateTime = DateTimeOffset.Parse("2024-09-17T13:45:21.0000000Z"),			CorrelationId = "9d84223c-521c-42f4-8f35-3cdeabe515d3",			Length = 17352L,			IsTruncated = false,			OwnerId = "ffe1ca70-6e5b-4120-abf0-472034ba05d4",			CustomProperties = new CustomMetadataDictionary			{				AdditionalData = new Dictionary<string, object>				{					{						"Department" , "Finance"					},					{						"ReviewerName" , "John Smith"					},				},			},		},	},	ActivityMetadata = new ActivityMetadata	{		Activity = UserActivityType.UploadFile,	},	DeviceMetadata = new DeviceMetadata	{		DeviceType = "unmanaged",		OperatingSystemSpecifications = new OperatingSystemSpecifications		{			OperatingSystemPlatform = "Windows",			OperatingSystemVersion = "11.1",		},	},	IntegratedAppMetadata = new IntegratedApplicationMetadata	{		Name = "Network Proxy App",		Version = "1.0.0",	},	ProtectedAppMetadata = new ProtectedApplicationMetadata	{		Name = "My App",		Version = "0.1",		ApplicationLocation = new PolicyLocationUrl		{			OdataType = "#microsoft.graph.policyLocationUrl",			Value = "https://gemini.google.com",		},	},},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Users["{user-id}"].DataSecurityAndGovernance.ProcessContent.PostAsync(requestBody);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphusers "github.com/microsoftgraph/msgraph-sdk-go/users"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

requestBody := graphusers.NewProcessContentPostRequestBody()
contentToProcess := graphmodels.NewProcessContentRequest()

processContentMetadataBase := graphmodels.NewProcessFileMetadata()
identifier := "f7af180f-dc2e-467c-9719-757e1c61eabf"
processContentMetadataBase.SetIdentifier(&identifier) 
content := graphmodels.NewTextContent()
data := "Base64 encoded content"
content.SetData(&data) 
processContentMetadataBase.SetContent(content)
name := "Test File.docx"
processContentMetadataBase.SetName(&name) 
correlationId := "d63eafd2-e3a9-4c1a-b726-a2e9b9d95822"
processContentMetadataBase.SetCorrelationId(&correlationId) 
createdDateTime , err := time.Parse(time.RFC3339, "2024-07-23T01:31:40.2020463Z")
processContentMetadataBase.SetCreatedDateTime(&createdDateTime) 
modifiedDateTime , err := time.Parse(time.RFC3339, "2024-09-17T13:45:21.0000000Z")
processContentMetadataBase.SetModifiedDateTime(&modifiedDateTime) 
correlationId := "9d84223c-521c-42f4-8f35-3cdeabe515d3"
processContentMetadataBase.SetCorrelationId(&correlationId) 
length := int64(17352)
processContentMetadataBase.SetLength(&length) 
isTruncated := false
processContentMetadataBase.SetIsTruncated(&isTruncated) 
ownerId := "ffe1ca70-6e5b-4120-abf0-472034ba05d4"
processContentMetadataBase.SetOwnerId(&ownerId) 
customProperties := graphmodels.NewCustomMetadataDictionary()
additionalData := map[string]interface{}{"Department" : "Finance", "ReviewerName" : "John Smith", 
}
customProperties.SetAdditionalData(additionalData)
processContentMetadataBase.SetCustomProperties(customProperties)

contentEntries := []graphmodels.ProcessContentMetadataBaseable {processContentMetadataBase,
}
contentToProcess.SetContentEntries(contentEntries)
activityMetadata := graphmodels.NewActivityMetadata()
activity := graphmodels.UPLOADFILE_USERACTIVITYTYPE 
activityMetadata.SetActivity(&activity) 
contentToProcess.SetActivityMetadata(activityMetadata)
deviceMetadata := graphmodels.NewDeviceMetadata()
deviceType := "unmanaged"
deviceMetadata.SetDeviceType(&deviceType) 
operatingSystemSpecifications := graphmodels.NewOperatingSystemSpecifications()
operatingSystemPlatform := "Windows"
operatingSystemSpecifications.SetOperatingSystemPlatform(&operatingSystemPlatform) 
operatingSystemVersion := "11.1"
operatingSystemSpecifications.SetOperatingSystemVersion(&operatingSystemVersion) 
deviceMetadata.SetOperatingSystemSpecifications(operatingSystemSpecifications)
contentToProcess.SetDeviceMetadata(deviceMetadata)
integratedAppMetadata := graphmodels.NewIntegratedApplicationMetadata()
name := "Network Proxy App"
integratedAppMetadata.SetName(&name) 
version := "1.0.0"
integratedAppMetadata.SetVersion(&version) 
contentToProcess.SetIntegratedAppMetadata(integratedAppMetadata)
protectedAppMetadata := graphmodels.NewProtectedApplicationMetadata()
name := "My App"
protectedAppMetadata.SetName(&name) 
version := "0.1"
protectedAppMetadata.SetVersion(&version) 
applicationLocation := graphmodels.NewPolicyLocationUrl()
value := "https://gemini.google.com"
applicationLocation.SetValue(&value) 
protectedAppMetadata.SetApplicationLocation(applicationLocation)
contentToProcess.SetProtectedAppMetadata(protectedAppMetadata)
requestBody.SetContentToProcess(contentToProcess)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
processContent, err := graphClient.Users().ByUserId("user-id").DataSecurityAndGovernance().ProcessContent().Post(context.Background(), requestBody, nil)

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.users.item.datasecurityandgovernance.processcontent.ProcessContentPostRequestBody processContentPostRequestBody = new com.microsoft.graph.users.item.datasecurityandgovernance.processcontent.ProcessContentPostRequestBody();
ProcessContentRequest contentToProcess = new ProcessContentRequest();
LinkedList<ProcessContentMetadataBase> contentEntries = new LinkedList<ProcessContentMetadataBase>();
ProcessFileMetadata processContentMetadataBase = new ProcessFileMetadata();
processContentMetadataBase.setOdataType("#microsoft.graph.processFileMetadata");
processContentMetadataBase.setIdentifier("f7af180f-dc2e-467c-9719-757e1c61eabf");
TextContent content = new TextContent();
content.setOdataType("#microsoft.graph.textContent");
content.setData("Base64 encoded content");
processContentMetadataBase.setContent(content);
processContentMetadataBase.setName("Test File.docx");
processContentMetadataBase.setCorrelationId("d63eafd2-e3a9-4c1a-b726-a2e9b9d95822");
OffsetDateTime createdDateTime = OffsetDateTime.parse("2024-07-23T01:31:40.2020463Z");
processContentMetadataBase.setCreatedDateTime(createdDateTime);
OffsetDateTime modifiedDateTime = OffsetDateTime.parse("2024-09-17T13:45:21.0000000Z");
processContentMetadataBase.setModifiedDateTime(modifiedDateTime);
processContentMetadataBase.setCorrelationId("9d84223c-521c-42f4-8f35-3cdeabe515d3");
processContentMetadataBase.setLength(17352L);
processContentMetadataBase.setIsTruncated(false);
processContentMetadataBase.setOwnerId("ffe1ca70-6e5b-4120-abf0-472034ba05d4");
CustomMetadataDictionary customProperties = new CustomMetadataDictionary();
HashMap<String, Object> additionalData = new HashMap<String, Object>();
additionalData.put("Department", "Finance");
additionalData.put("ReviewerName", "John Smith");
customProperties.setAdditionalData(additionalData);
processContentMetadataBase.setCustomProperties(customProperties);
contentEntries.add(processContentMetadataBase);
contentToProcess.setContentEntries(contentEntries);
ActivityMetadata activityMetadata = new ActivityMetadata();
activityMetadata.setActivity(UserActivityType.UploadFile);
contentToProcess.setActivityMetadata(activityMetadata);
DeviceMetadata deviceMetadata = new DeviceMetadata();
deviceMetadata.setDeviceType("unmanaged");
OperatingSystemSpecifications operatingSystemSpecifications = new OperatingSystemSpecifications();
operatingSystemSpecifications.setOperatingSystemPlatform("Windows");
operatingSystemSpecifications.setOperatingSystemVersion("11.1");
deviceMetadata.setOperatingSystemSpecifications(operatingSystemSpecifications);
contentToProcess.setDeviceMetadata(deviceMetadata);
IntegratedApplicationMetadata integratedAppMetadata = new IntegratedApplicationMetadata();
integratedAppMetadata.setName("Network Proxy App");
integratedAppMetadata.setVersion("1.0.0");
contentToProcess.setIntegratedAppMetadata(integratedAppMetadata);
ProtectedApplicationMetadata protectedAppMetadata = new ProtectedApplicationMetadata();
protectedAppMetadata.setName("My App");
protectedAppMetadata.setVersion("0.1");
PolicyLocationUrl applicationLocation = new PolicyLocationUrl();
applicationLocation.setOdataType("#microsoft.graph.policyLocationUrl");
applicationLocation.setValue("https://gemini.google.com");
protectedAppMetadata.setApplicationLocation(applicationLocation);
contentToProcess.setProtectedAppMetadata(protectedAppMetadata);
processContentPostRequestBody.setContentToProcess(contentToProcess);
var result = graphClient.users().byUserId("{user-id}").dataSecurityAndGovernance().processContent().post(processContentPostRequestBody);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const processContentResponse = {contentToProcess: {	contentEntries: [		{			'@odata.type': '#microsoft.graph.processFileMetadata',			identifier: 'f7af180f-dc2e-467c-9719-757e1c61eabf',			content: {			'@odata.type': '#microsoft.graph.textContent',				data: 'Base64 encoded content'			},			name: 'Test File.docx',			correlationId: 'd63eafd2-e3a9-4c1a-b726-a2e9b9d95822',			createdDateTime: '2024-07-23T01:31:40.2020463Z',			modifiedDateTime: '2024-09-17T13:45:21.0000000Z',			correlationId: '9d84223c-521c-42f4-8f35-3cdeabe515d3',			length: 17352,			isTruncated: false,			ownerId: 'ffe1ca70-6e5b-4120-abf0-472034ba05d4',			customProperties: {				Department: 'Finance',				ReviewerName: 'John Smith'			}		}	],	activityMetadata: {		activity: 'uploadFile'	},	deviceMetadata: {		deviceType: 'unmanaged',		operatingSystemSpecifications: {			operatingSystemPlatform: 'Windows',			operatingSystemVersion: '11.1'		}	},	integratedAppMetadata: {		name: 'Network Proxy App',		version: '1.0.0'	},	protectedAppMetadata: {		name: 'My App',		version: '0.1',		applicationLocation: {			'@odata.type': '#microsoft.graph.policyLocationUrl',			value: 'https://gemini.google.com'		}	}}
};

await client.api('/users/5def8f26-aff8-4db6-a08c-0fcf8f1aa2ba/dataSecurityAndGovernance/processContent').post(processContentResponse);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Users\Item\DataSecurityAndGovernance\ProcessContent\ProcessContentPostRequestBody;
use Microsoft\Graph\Generated\Models\ProcessContentRequest;
use Microsoft\Graph\Generated\Models\ProcessContentMetadataBase;
use Microsoft\Graph\Generated\Models\ProcessFileMetadata;
use Microsoft\Graph\Generated\Models\TextContent;
use Microsoft\Graph\Generated\Models\CustomMetadataDictionary;
use Microsoft\Graph\Generated\Models\ActivityMetadata;
use Microsoft\Graph\Generated\Models\UserActivityType;
use Microsoft\Graph\Generated\Models\DeviceMetadata;
use Microsoft\Graph\Generated\Models\OperatingSystemSpecifications;
use Microsoft\Graph\Generated\Models\IntegratedApplicationMetadata;
use Microsoft\Graph\Generated\Models\ProtectedApplicationMetadata;
use Microsoft\Graph\Generated\Models\PolicyLocationUrl;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new ProcessContentPostRequestBody();
$contentToProcess = new ProcessContentRequest();
$contentEntriesProcessContentMetadataBase1 = new ProcessFileMetadata();
$contentEntriesProcessContentMetadataBase1->setOdataType('#microsoft.graph.processFileMetadata');
$contentEntriesProcessContentMetadataBase1->setIdentifier('f7af180f-dc2e-467c-9719-757e1c61eabf');
$contentEntriesProcessContentMetadataBase1Content = new TextContent();
$contentEntriesProcessContentMetadataBase1Content->setOdataType('#microsoft.graph.textContent');
$contentEntriesProcessContentMetadataBase1Content->setData('Base64 encoded content');
$contentEntriesProcessContentMetadataBase1->setContent($contentEntriesProcessContentMetadataBase1Content);
$contentEntriesProcessContentMetadataBase1->setName('Test File.docx');
$contentEntriesProcessContentMetadataBase1->setCorrelationId('d63eafd2-e3a9-4c1a-b726-a2e9b9d95822');
$contentEntriesProcessContentMetadataBase1->setCreatedDateTime(new \DateTime('2024-07-23T01:31:40.2020463Z'));
$contentEntriesProcessContentMetadataBase1->setModifiedDateTime(new \DateTime('2024-09-17T13:45:21.0000000Z'));
$contentEntriesProcessContentMetadataBase1->setCorrelationId('9d84223c-521c-42f4-8f35-3cdeabe515d3');
$contentEntriesProcessContentMetadataBase1->setLength(17352);
$contentEntriesProcessContentMetadataBase1->setIsTruncated(false);
$contentEntriesProcessContentMetadataBase1->setOwnerId('ffe1ca70-6e5b-4120-abf0-472034ba05d4');
$contentEntriesProcessContentMetadataBase1CustomProperties = new CustomMetadataDictionary();
$additionalData = ['Department' => 'Finance','ReviewerName' => 'John Smith',
];
$contentEntriesProcessContentMetadataBase1CustomProperties->setAdditionalData($additionalData);
$contentEntriesProcessContentMetadataBase1->setCustomProperties($contentEntriesProcessContentMetadataBase1CustomProperties);
$contentEntriesArray []= $contentEntriesProcessContentMetadataBase1;
$contentToProcess->setContentEntries($contentEntriesArray);

$contentToProcessActivityMetadata = new ActivityMetadata();
$contentToProcessActivityMetadata->setActivity(new UserActivityType('uploadFile'));
$contentToProcess->setActivityMetadata($contentToProcessActivityMetadata);
$contentToProcessDeviceMetadata = new DeviceMetadata();
$contentToProcessDeviceMetadata->setDeviceType('unmanaged');
$contentToProcessDeviceMetadataOperatingSystemSpecifications = new OperatingSystemSpecifications();
$contentToProcessDeviceMetadataOperatingSystemSpecifications->setOperatingSystemPlatform('Windows');
$contentToProcessDeviceMetadataOperatingSystemSpecifications->setOperatingSystemVersion('11.1');
$contentToProcessDeviceMetadata->setOperatingSystemSpecifications($contentToProcessDeviceMetadataOperatingSystemSpecifications);
$contentToProcess->setDeviceMetadata($contentToProcessDeviceMetadata);
$contentToProcessIntegratedAppMetadata = new IntegratedApplicationMetadata();
$contentToProcessIntegratedAppMetadata->setName('Network Proxy App');
$contentToProcessIntegratedAppMetadata->setVersion('1.0.0');
$contentToProcess->setIntegratedAppMetadata($contentToProcessIntegratedAppMetadata);
$contentToProcessProtectedAppMetadata = new ProtectedApplicationMetadata();
$contentToProcessProtectedAppMetadata->setName('My App');
$contentToProcessProtectedAppMetadata->setVersion('0.1');
$contentToProcessProtectedAppMetadataApplicationLocation = new PolicyLocationUrl();
$contentToProcessProtectedAppMetadataApplicationLocation->setOdataType('#microsoft.graph.policyLocationUrl');
$contentToProcessProtectedAppMetadataApplicationLocation->setValue('https://gemini.google.com');
$contentToProcessProtectedAppMetadata->setApplicationLocation($contentToProcessProtectedAppMetadataApplicationLocation);
$contentToProcess->setProtectedAppMetadata($contentToProcessProtectedAppMetadata);
$requestBody->setContentToProcess($contentToProcess);

$result = $graphServiceClient->users()->byUserId('user-id')->dataSecurityAndGovernance()->processContent()->post($requestBody)->wait();

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.users.item.datasecurityandgovernance.process_content.process_content_post_request_body import ProcessContentPostRequestBody
from msgraph.generated.models.process_content_request import ProcessContentRequest
from msgraph.generated.models.process_content_metadata_base import ProcessContentMetadataBase
from msgraph.generated.models.process_file_metadata import ProcessFileMetadata
from msgraph.generated.models.text_content import TextContent
from msgraph.generated.models.custom_metadata_dictionary import CustomMetadataDictionary
from msgraph.generated.models.activity_metadata import ActivityMetadata
from msgraph.generated.models.user_activity_type import UserActivityType
from msgraph.generated.models.device_metadata import DeviceMetadata
from msgraph.generated.models.operating_system_specifications import OperatingSystemSpecifications
from msgraph.generated.models.integrated_application_metadata import IntegratedApplicationMetadata
from msgraph.generated.models.protected_application_metadata import ProtectedApplicationMetadata
from msgraph.generated.models.policy_location_url import PolicyLocationUrl
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = ProcessContentPostRequestBody(content_to_process = ProcessContentRequest(	content_entries = [		ProcessFileMetadata(			odata_type = "#microsoft.graph.processFileMetadata",			identifier = "f7af180f-dc2e-467c-9719-757e1c61eabf",			content = TextContent(				odata_type = "#microsoft.graph.textContent",				data = "Base64 encoded content",			),			name = "Test File.docx",			correlation_id = "d63eafd2-e3a9-4c1a-b726-a2e9b9d95822",			created_date_time = "2024-07-23T01:31:40.2020463Z",			modified_date_time = "2024-09-17T13:45:21.0000000Z",			correlation_id = "9d84223c-521c-42f4-8f35-3cdeabe515d3",			length = 17352,			is_truncated = False,			owner_id = "ffe1ca70-6e5b-4120-abf0-472034ba05d4",			custom_properties = CustomMetadataDictionary(				additional_data = {						"department" : "Finance",						"reviewer_name" : "John Smith",				}			),		),	],	activity_metadata = ActivityMetadata(		activity = UserActivityType.UploadFile,	),	device_metadata = DeviceMetadata(		device_type = "unmanaged",		operating_system_specifications = OperatingSystemSpecifications(			operating_system_platform = "Windows",			operating_system_version = "11.1",		),	),	integrated_app_metadata = IntegratedApplicationMetadata(		name = "Network Proxy App",		version = "1.0.0",	),	protected_app_metadata = ProtectedApplicationMetadata(		name = "My App",		version = "0.1",		application_location = PolicyLocationUrl(			odata_type = "#microsoft.graph.policyLocationUrl",			value = "https://gemini.google.com",		),	),),
)

result = await graph_client.users.by_user_id('user-id').data_security_and_governance.process_content.post(request_body)

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

#### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#microsoft.graph.processContentResponse",
  "protectionScopeState": "modified",
  "policyActions": [
    {
      "@odata.type": "#microsoft.graph.restrictAccessAction",
      "action": "restrictAccess",
      "restrictionAction": "block"
    }
  ],
  "processingErrors": []
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/userdatasecurityandgovernance-processcontent?view=graph-rest-beta&accept=text/markdown)
